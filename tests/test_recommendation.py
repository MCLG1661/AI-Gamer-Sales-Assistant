from src.diagnosis import diagnose_opportunity
from src.models import CustomerContext, Level
from src.recommendation import (
    build_sales_recommendation,
    infer_primary_category,
    recommend_cross_sell,
    recommend_main_offer,
    recommend_upsell,
)


def test_infer_notebook_category():
    context = CustomerContext(
        need="Preciso de um notebook para estudar",
        budget=5000,
    )

    assert infer_primary_category(context) == "notebook"


def test_infer_desktop_category():
    context = CustomerContext(
        need="Quero montar um PC gamer",
        budget=7000,
    )

    assert infer_primary_category(context) == "desktop"


def test_recommend_main_notebook():
    context = CustomerContext(
        need="Notebook para estudar e jogar",
        budget=6000,
        usage=["estudo", "jogos"],
    )

    product = recommend_main_offer(context)

    assert product is not None
    assert product["name"] == "Notebook Gamer Entry"


def test_recommend_upsell():
    context = CustomerContext(
        need="Notebook gamer",
        budget=6000,
        usage=["jogos"],
    )

    main_product = recommend_main_offer(context)
    upsell = recommend_upsell(main_product, context)

    assert isinstance(upsell, list)


def test_recommend_cross_sell():
    context = CustomerContext(
        need="Notebook para jogar",
        budget=6000,
        usage=["jogos"],
    )

    main_product = recommend_main_offer(context)
    cross_sell = recommend_cross_sell(main_product, context)

    assert len(cross_sell) <= 3
    assert any(
        product["category"] in {"mouse", "keyboard", "headset", "monitor"}
        for product in cross_sell
    )


def test_complete_sales_recommendation():
    context = CustomerContext(
        need="Notebook para estudar e jogar",
        budget=6000,
        usage=["estudo", "jogos"],
        urgency=Level.MEDIUM,
    )

    diagnosis = diagnose_opportunity(context)
    recommendation = build_sales_recommendation(
        context,
        diagnosis,
    )

    assert recommendation.main_offer == "Notebook Gamer Entry"
    assert recommendation.value_argument is not None
    assert isinstance(recommendation.upsell, list)
    assert isinstance(recommendation.cross_sell, list)