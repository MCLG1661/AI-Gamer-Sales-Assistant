from src.diagnosis import (
    classify_customer_profile,
    classify_opportunity_type,
    classify_price_sensitivity,
    diagnose_opportunity,
)
from src.models import (
    CustomerContext,
    CustomerProfile,
    Level,
    OpportunityType,
)


def test_high_ticket_opportunity():
    context = CustomerContext(
        need="Notebook gamer",
        budget=6000,
    )

    assert classify_opportunity_type(context) == OpportunityType.HIGH_TICKET


def test_mixed_opportunity():
    context = CustomerContext(
        need="Upgrade de computador",
        budget=3000,
    )

    assert classify_opportunity_type(context) == OpportunityType.MIXED


def test_low_ticket_opportunity():
    context = CustomerContext(
        need="Mouse gamer",
        budget=500,
    )

    assert classify_opportunity_type(context) == OpportunityType.LOW_TICKET


def test_rational_customer_profile():
    context = CustomerContext(
        need="Notebook para jogos com bom desempenho e SSD",
        budget=6000,
    )

    assert classify_customer_profile(context) == CustomerProfile.RATIONAL


def test_hybrid_customer_profile():
    context = CustomerContext(
        need="Quero montar um setup bonito com ótimo desempenho",
        budget=7000,
    )

    assert classify_customer_profile(context) == CustomerProfile.HYBRID


def test_price_sensitivity():
    context = CustomerContext(
        need="Notebook gamer",
        budget=6000,
    )

    assert classify_price_sensitivity(context) == Level.LOW


def test_complete_diagnosis():
    context = CustomerContext(
        need="Notebook para estudar e jogar com bom desempenho",
        budget=6000,
        usage=["estudo", "jogos"],
        urgency=Level.MEDIUM,
    )

    diagnosis = diagnose_opportunity(context)

    assert diagnosis.opportunity_type == OpportunityType.HIGH_TICKET
    assert diagnosis.customer_profile == CustomerProfile.RATIONAL
    assert diagnosis.urgency == Level.MEDIUM
    assert diagnosis.price_sensitivity == Level.LOW
    assert diagnosis.loss_risk == Level.MEDIUM
    assert len(diagnosis.rationale) == 5