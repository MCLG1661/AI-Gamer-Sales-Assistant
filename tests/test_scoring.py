from src.models import (
    CustomerProfile,
    Level,
    OpportunityDiagnosis,
    OpportunityType,
)
from src.scoring import (
    calculate_opportunity_score,
    classify_priority,
    determine_next_best_action,
)


def test_priority_high():
    assert classify_priority(70) == "Alta"
    assert classify_priority(95) == "Alta"


def test_priority_medium():
    assert classify_priority(45) == "Média"
    assert classify_priority(69) == "Média"


def test_priority_low():
    assert classify_priority(0) == "Baixa"
    assert classify_priority(44) == "Baixa"


def test_high_value_opportunity_generates_high_score():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.HIGH_TICKET,
        customer_profile=CustomerProfile.HYBRID,
        urgency=Level.HIGH,
        price_sensitivity=Level.LOW,
        loss_risk=Level.LOW,
    )

    result = calculate_opportunity_score(diagnosis)

    assert result.score == 100
    assert result.priority == "Alta"
    assert result.reasons


def test_score_is_never_above_100():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.HIGH_TICKET,
        customer_profile=CustomerProfile.HYBRID,
        urgency=Level.HIGH,
        price_sensitivity=Level.LOW,
        loss_risk=Level.LOW,
    )

    result = calculate_opportunity_score(diagnosis)

    assert 0 <= result.score <= 100


def test_high_loss_risk_prioritizes_retention_action():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.HIGH_TICKET,
        customer_profile=CustomerProfile.RATIONAL,
        urgency=Level.HIGH,
        price_sensitivity=Level.LOW,
        loss_risk=Level.HIGH,
    )

    action = determine_next_best_action(
        diagnosis=diagnosis,
        score=80,
    )

    assert "reduzir o risco de perda" in action.lower()


def test_high_price_sensitivity_prioritizes_value_argument():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.LOW_TICKET,
        customer_profile=CustomerProfile.RATIONAL,
        urgency=Level.LOW,
        price_sensitivity=Level.HIGH,
        loss_risk=Level.LOW,
    )

    action = determine_next_best_action(
        diagnosis=diagnosis,
        score=40,
    )

    assert "reforçar valor" in action.lower()


def test_undefined_profile_requests_more_qualification():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.MIXED,
        customer_profile=CustomerProfile.UNDEFINED,
        urgency=Level.MEDIUM,
        price_sensitivity=Level.MEDIUM,
        loss_risk=Level.MEDIUM,
    )

    action = determine_next_best_action(
        diagnosis=diagnosis,
        score=50,
    )

    assert "aprofundar a qualificação" in action.lower()


def test_high_score_recommends_closing():
    diagnosis = OpportunityDiagnosis(
        opportunity_type=OpportunityType.HIGH_TICKET,
        customer_profile=CustomerProfile.RATIONAL,
        urgency=Level.MEDIUM,
        price_sensitivity=Level.LOW,
        loss_risk=Level.LOW,
    )

    action = determine_next_best_action(
        diagnosis=diagnosis,
        score=80,
    )

    assert "avançar para fechamento" in action.lower()