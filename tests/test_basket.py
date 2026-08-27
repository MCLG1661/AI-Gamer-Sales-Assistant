from src.basket import (
    build_basket,
    get_products_by_names,
    select_complementary_products,
)


def test_get_products_by_names():
    products = get_products_by_names(
        [
            "Mouse Gamer Precision",
            "Headset Gamer Surround",
        ]
    )

    names = {product["name"] for product in products}

    assert "Mouse Gamer Precision" in names
    assert "Headset Gamer Surround" in names


def test_select_complementary_products_respects_available_budget():
    selected = select_complementary_products(
        [
            "Mouse Gamer Precision",
            "Headset Gamer Surround",
            "Teclado Mecânico Gamer",
        ],
        available_budget=600,
    )

    total = sum(product["price"] for product in selected)

    assert total <= 600


def test_build_basket_stays_within_budget():
    basket = build_basket(
        main_product_name="Notebook Gamer Entry",
        main_product_price=4299,
        cross_sell_names=[
            "Mouse Gamer Precision",
            "Headset Gamer Surround",
            "Teclado Mecânico Gamer",
        ],
        budget=6000,
    )

    assert basket.within_budget is True
    assert basket.basket_total <= 6000
    assert basket.final_remaining_budget >= 0


def test_build_basket_calculates_remaining_budget():
    basket = build_basket(
        main_product_name="Notebook Gamer Entry",
        main_product_price=4299,
        cross_sell_names=[
            "Mouse Gamer Precision",
            "Headset Gamer Surround",
        ],
        budget=6000,
    )

    expected_total = 4299 + 249 + 349

    assert basket.basket_total == expected_total
    assert basket.final_remaining_budget == 6000 - expected_total


def test_build_basket_without_declared_budget():
    basket = build_basket(
        main_product_name="Notebook Gamer Entry",
        main_product_price=4299,
        cross_sell_names=[
            "Mouse Gamer Precision",
            "Headset Gamer Surround",
        ],
        budget=None,
    )

    assert basket.within_budget is True
    assert basket.remaining_budget is None
    assert basket.final_remaining_budget is None
    assert len(basket.complementary_products) == 2