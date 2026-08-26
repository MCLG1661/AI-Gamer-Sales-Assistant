from src.catalog import (
    filter_by_budget,
    filter_by_category,
    filter_by_use_case,
    find_products,
    load_catalog,
)


def test_catalog_loads_products():
    products = load_catalog()

    assert len(products) >= 8
    assert all("name" in product for product in products)
    assert all("price" in product for product in products)


def test_filter_by_budget():
    products = load_catalog()

    filtered = filter_by_budget(products, 500)

    assert filtered
    assert all(product["price"] <= 500 for product in filtered)


def test_filter_by_use_case():
    products = load_catalog()

    filtered = filter_by_use_case(products, ["estudo"])

    assert filtered
    assert all("estudo" in product["use_cases"] for product in filtered)


def test_filter_by_category():
    products = load_catalog()

    filtered = filter_by_category(products, "notebook")

    assert filtered
    assert all(product["category"] == "notebook" for product in filtered)


def test_find_notebook_with_budget_and_use_case():
    products = find_products(
        budget=6000,
        use_cases=["estudo", "jogos"],
        category="notebook",
    )

    assert len(products) == 1
    assert products[0]["name"] == "Notebook Gamer Entry"
    assert products[0]["price"] == 4299


def test_find_products_returns_highest_price_first():
    products = find_products(
        budget=7000,
        use_cases=["jogos"],
    )

    prices = [product["price"] for product in products]

    assert prices == sorted(prices, reverse=True)