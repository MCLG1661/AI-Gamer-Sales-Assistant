from src.catalog import find_products, load_catalog
from src.models import CustomerContext, OpportunityDiagnosis, SalesRecommendation


def infer_primary_category(context: CustomerContext) -> str | None:
    text = " ".join(
        [
            context.need or "",
            " ".join(context.usage),
        ]
    ).lower()

    if "notebook" in text or context.mobility is True:
        return "notebook"

    if "pc" in text or "desktop" in text:
        return "desktop"

    if "monitor" in text:
        return "monitor"

    if "mouse" in text:
        return "mouse"

    if "teclado" in text:
        return "keyboard"

    if "headset" in text:
        return "headset"

    return None


def recommend_main_offer(
    context: CustomerContext,
) -> dict | None:
    category = infer_primary_category(context)

    products = find_products(
        budget=context.budget,
        use_cases=context.usage,
        category=category,
    )

    if not products:
        return None

    return products[0]


def recommend_upsell(
    main_product: dict | None,
    context: CustomerContext,
) -> list[dict]:
    """Sugere upgrade somente quando estiver dentro do orçamento declarado."""
    if main_product is None:
        return []

    catalog = load_catalog()

    candidates = [
        product
        for product in catalog
        if product["category"] == main_product["category"]
        and product["price"] > main_product["price"]
    ]

    if context.budget is not None:
        candidates = [
            product
            for product in candidates
            if product["price"] <= context.budget
        ]

    return sorted(
        candidates,
        key=lambda product: product["price"],
    )[:1]


def recommend_premium_alternative(
    main_product: dict | None,
    context: CustomerContext,
) -> dict | None:
    """Identifica opção superior acima do orçamento sem tratá-la como upsell."""
    if main_product is None or context.budget is None:
        return None

    catalog = load_catalog()

    candidates = [
        product
        for product in catalog
        if product["category"] == main_product["category"]
        and product["price"] > context.budget
    ]

    if not candidates:
        return None

    return min(
        candidates,
        key=lambda product: product["price"],
    )


def recommend_cross_sell(
    main_product: dict | None,
    context: CustomerContext,
) -> list[dict]:
    if main_product is None:
        return []

    catalog = load_catalog()

    accessory_categories = {
        "mouse",
        "keyboard",
        "headset",
        "monitor",
    }

    cross_sell = [
        product
        for product in catalog
        if product["category"] in accessory_categories
        and product["category"] != main_product["category"]
    ]

    if "jogos" in [use.lower() for use in context.usage]:
        priority = {
            "mouse": 1,
            "headset": 2,
            "keyboard": 3,
            "monitor": 4,
        }

        cross_sell.sort(
            key=lambda product: priority.get(
                product["category"],
                99,
            )
        )

    return cross_sell[:3]


def build_sales_recommendation(
    context: CustomerContext,
    diagnosis: OpportunityDiagnosis,
) -> SalesRecommendation:
    main_product = recommend_main_offer(context)
    upsell_products = recommend_upsell(main_product, context)
    premium_product = recommend_premium_alternative(main_product, context)
    cross_sell_products = recommend_cross_sell(main_product, context)

    if main_product is None:
        return SalesRecommendation(
            value_argument=(
                "Não foi encontrado um produto compatível com "
                "os critérios informados."
            )
        )

    value_argument = (
        f"{main_product['name']} é a opção mais aderente ao contexto "
        f"informado, considerando orçamento, uso e perfil da oportunidade."
    )

    return SalesRecommendation(
        main_offer=main_product["name"],
        main_offer_price=main_product["price"],
        main_offer_features=main_product["features"],
        value_argument=value_argument,
        upsell=[
            product["name"]
            for product in upsell_products
        ],
        premium_alternative=(
            premium_product["name"]
            if premium_product
            else None
        ),
        premium_alternative_price=(
            premium_product["price"]
            if premium_product
            else None
        ),
        cross_sell=[
            product["name"]
            for product in cross_sell_products
        ],
        closing_trigger=(
            f"{main_product['name']} atende ao cenário informado "
            "respeitando o orçamento e as necessidades identificadas."
        ),
    )