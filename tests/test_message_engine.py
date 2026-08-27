from src.basket import build_basket
from src.diagnosis import diagnose_opportunity
from src.message_engine import (
    build_instagram_message,
    build_whatsapp_message,
)
from src.models import CustomerContext, Level
from src.recommendation import build_sales_recommendation


def build_test_scenario():
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

    basket = build_basket(
        main_product_name=recommendation.main_offer,
        main_product_price=recommendation.main_offer_price,
        cross_sell_names=recommendation.cross_sell,
        budget=context.budget,
    )

    return context, diagnosis, recommendation, basket


def test_whatsapp_message_contains_main_offer():
    context, diagnosis, recommendation, basket = build_test_scenario()

    message = build_whatsapp_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert "Notebook Gamer Entry" in message
    assert "R$ 4.299,00" in message


def test_whatsapp_message_contains_basket_total():
    context, diagnosis, recommendation, basket = build_test_scenario()

    message = build_whatsapp_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert "Total da solução" in message
    assert "R$ 5.296,00" in message


def test_whatsapp_message_mentions_remaining_budget():
    context, diagnosis, recommendation, basket = build_test_scenario()

    message = build_whatsapp_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert "Saldo em relação ao orçamento informado" in message
    assert "R$ 704,00" in message


def test_whatsapp_message_separates_premium_alternative():
    context, diagnosis, recommendation, basket = build_test_scenario()

    message = build_whatsapp_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert "Notebook Gamer Performance" in message
    assert "R$ 6.499,00" in message
    assert "acima do orçamento" in message


def test_instagram_message_is_shorter_than_whatsapp():
    context, diagnosis, recommendation, basket = build_test_scenario()

    whatsapp_message = build_whatsapp_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    instagram_message = build_instagram_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert len(instagram_message) < len(whatsapp_message)


def test_instagram_message_contains_main_offer_and_total():
    context, diagnosis, recommendation, basket = build_test_scenario()

    message = build_instagram_message(
        context,
        diagnosis,
        recommendation,
        basket,
    )

    assert "Notebook Gamer Entry" in message
    assert "R$ 5.296,00" in message