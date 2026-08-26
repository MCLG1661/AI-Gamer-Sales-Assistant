from src.models import (
    CustomerContext,
    CustomerProfile,
    Level,
    OpportunityDiagnosis,
    OpportunityType,
)


def classify_opportunity_type(context: CustomerContext) -> OpportunityType:
    if context.budget is None:
        return OpportunityType.UNDEFINED

    if context.budget >= 5000:
        return OpportunityType.HIGH_TICKET

    if context.budget >= 1500:
        return OpportunityType.MIXED

    return OpportunityType.LOW_TICKET


def classify_price_sensitivity(context: CustomerContext) -> Level:
    if context.budget is None:
        return Level.UNDEFINED

    if context.budget < 1500:
        return Level.HIGH

    if context.budget < 5000:
        return Level.MEDIUM

    return Level.LOW


def classify_customer_profile(context: CustomerContext) -> CustomerProfile:
    technical_signals = {
        "fps",
        "performance",
        "desempenho",
        "ram",
        "ssd",
        "gpu",
        "placa de vídeo",
        "processador",
    }

    emotional_signals = {
        "design",
        "estética",
        "presente",
        "sonho",
        "bonito",
        "setup",
    }

    searchable_text = " ".join(
        [
            context.need or "",
            context.expected_performance or "",
            " ".join(context.usage),
        ]
    ).lower()

    has_technical = any(signal in searchable_text for signal in technical_signals)
    has_emotional = any(signal in searchable_text for signal in emotional_signals)

    if has_technical and has_emotional:
        return CustomerProfile.HYBRID

    if has_technical:
        return CustomerProfile.RATIONAL

    if has_emotional:
        return CustomerProfile.EMOTIONAL

    return CustomerProfile.UNDEFINED


def classify_loss_risk(context: CustomerContext) -> Level:
    if context.urgency == Level.HIGH:
        return Level.HIGH

    if context.urgency == Level.MEDIUM:
        return Level.MEDIUM

    if context.budget is not None:
        return Level.MEDIUM

    return Level.LOW


def diagnose_opportunity(context: CustomerContext) -> OpportunityDiagnosis:
    opportunity_type = classify_opportunity_type(context)
    customer_profile = classify_customer_profile(context)
    price_sensitivity = classify_price_sensitivity(context)
    loss_risk = classify_loss_risk(context)

    rationale = [
        f"Tipo da oportunidade: {opportunity_type.value}",
        f"Perfil do cliente: {customer_profile.value}",
        f"Urgência: {context.urgency.value}",
        f"Sensibilidade a preço: {price_sensitivity.value}",
        f"Risco de perda: {loss_risk.value}",
    ]

    return OpportunityDiagnosis(
        opportunity_type=opportunity_type,
        customer_profile=customer_profile,
        urgency=context.urgency,
        price_sensitivity=price_sensitivity,
        loss_risk=loss_risk,
        rationale=rationale,
    )