from dataclasses import dataclass, field

from src.catalog import load_catalog


@dataclass
class BasketResult:
    """Resultado da composição comercial dentro do orçamento do cliente."""

    main_product: str
    main_product_price: float
    budget: float | None
    remaining_budget: float | None
    complementary_products: list[dict] = field(default_factory=list)
    basket_total: float = 0.0
    final_remaining_budget: float | None = None

    @property
    def within_budget(self) -> bool:
        if self.budget is None:
            return True

        return self.basket_total <= self.budget


def get_products_by_names(
    product_names: list[str],
) -> list[dict]:
    """Recupera produtos do catálogo a partir de seus nomes."""
    catalog = load_catalog()
    names = set(product_names)

    return [
        product
        for product in catalog
        if product["name"] in names
    ]


def select_complementary_products(
    product_names: list[str],
    available_budget: float | None,
) -> list[dict]:
    """
    Seleciona produtos complementares respeitando o saldo disponível.

    Quando existe orçamento, os produtos são adicionados somente se
    couberem no saldo restante. Sem orçamento declarado, mantém todos
    os complementos recomendados.
    """
    products = get_products_by_names(product_names)

    if available_budget is None:
        return products

    selected = []
    remaining = available_budget

    for product in products:
        if product["price"] <= remaining:
            selected.append(product)
            remaining -= product["price"]

    return selected


def build_basket(
    main_product_name: str,
    main_product_price: float,
    cross_sell_names: list[str],
    budget: float | None,
) -> BasketResult:
    """Monta uma solução comercial completa a partir da oferta principal."""

    remaining_budget = (
        budget - main_product_price
        if budget is not None
        else None
    )

    available_for_cross_sell = (
        max(remaining_budget, 0)
        if remaining_budget is not None
        else None
    )

    complementary_products = select_complementary_products(
        cross_sell_names,
        available_for_cross_sell,
    )

    complementary_total = sum(
        product["price"]
        for product in complementary_products
    )

    basket_total = main_product_price + complementary_total

    final_remaining_budget = (
        budget - basket_total
        if budget is not None
        else None
    )

    return BasketResult(
        main_product=main_product_name,
        main_product_price=main_product_price,
        budget=budget,
        remaining_budget=remaining_budget,
        complementary_products=complementary_products,
        basket_total=basket_total,
        final_remaining_budget=final_remaining_budget,
    )