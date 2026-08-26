import json
from pathlib import Path
from typing import Optional


CATALOG_PATH = Path(__file__).resolve().parent.parent / "data" / "products.json"


def load_catalog(path: Path = CATALOG_PATH) -> list[dict]:
    """Carrega o catálogo estruturado de produtos."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def filter_by_budget(
    products: list[dict],
    budget: Optional[float],
) -> list[dict]:
    """Retorna produtos dentro do orçamento informado."""
    if budget is None:
        return products

    return [
        product
        for product in products
        if product["price"] <= budget
    ]


def filter_by_use_case(
    products: list[dict],
    use_cases: list[str],
) -> list[dict]:
    """Filtra produtos compatíveis com pelo menos um caso de uso."""
    if not use_cases:
        return products

    normalized_uses = {use.lower() for use in use_cases}

    return [
        product
        for product in products
        if normalized_uses.intersection(
            use.lower() for use in product["use_cases"]
        )
    ]


def filter_by_category(
    products: list[dict],
    category: Optional[str],
) -> list[dict]:
    """Filtra produtos por categoria."""
    if not category:
        return products

    return [
        product
        for product in products
        if product["category"].lower() == category.lower()
    ]


def find_products(
    budget: Optional[float] = None,
    use_cases: Optional[list[str]] = None,
    category: Optional[str] = None,
) -> list[dict]:
    """Consulta o catálogo combinando orçamento, uso e categoria."""
    products = load_catalog()

    products = filter_by_budget(products, budget)
    products = filter_by_use_case(products, use_cases or [])
    products = filter_by_category(products, category)

    return sorted(
        products,
        key=lambda product: product["price"],
        reverse=True,
    )