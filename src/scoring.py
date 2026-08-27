from dataclasses import dataclass

from src.models import (
    CustomerProfile,
    Level,
    OpportunityDiagnosis,
    OpportunityType,
)


@dataclass
class OpportunityScore:
    """Resultado da priorização comercial da oportunidade."""

    score: int
    priority: str
    next_best_action: str
    reasons: list[str]


def calculate_opportunity_score(
    diagnosis: OpportunityDiagnosis,
) -> OpportunityScore:
    """
    Calcula um score comercial entre 0 e 100.

    O score combina:
    - valor potencial da oportunidade;
    - urgência;
    - perfil identificado;
    - sensibilidade a preço;
    - risco de perda.
    """

    score = 20
    reasons: list[str] = []

    # Potencial comercial
    if diagnosis.opportunity_type == OpportunityType.HIGH_TICKET:
        score += 25
        reasons.append("Oportunidade de alto valor.")

    elif diagnosis.opportunity_type == OpportunityType.MIXED:
        score += 18
        reasons.append(
            "Oportunidade com potencial comercial intermediário."
        )

    elif diagnosis.opportunity_type == OpportunityType.LOW_TICKET:
        score += 10
        reasons.append("Oportunidade de menor ticket.")

    # Urgência
    if diagnosis.urgency == Level.HIGH:
        score += 20
        reasons.append("Cliente demonstra alta urgência de compra.")

    elif diagnosis.urgency == Level.MEDIUM:
        score += 12
        reasons.append("Existe urgência moderada para a decisão.")

    elif diagnosis.urgency == Level.LOW:
        score += 5
        reasons.append("A decisão de compra apresenta baixa urgência.")

    # Perfil
    if diagnosis.customer_profile == CustomerProfile.HYBRID:
        score += 15
        reasons.append(
            "Perfil híbrido permite trabalhar argumentos técnicos "
            "e emocionais."
        )

    elif diagnosis.customer_profile in {
        CustomerProfile.RATIONAL,
        CustomerProfile.EMOTIONAL,
    }:
        score += 10
        reasons.append("Perfil de compra identificado.")

    # Sensibilidade a preço
    if diagnosis.price_sensitivity == Level.LOW:
        score += 15
        reasons.append(
            "Baixa sensibilidade a preço favorece geração de valor."
        )

    elif diagnosis.price_sensitivity == Level.MEDIUM:
        score += 8
        reasons.append("Sensibilidade a preço moderada.")

    elif diagnosis.price_sensitivity == Level.HIGH:
        reasons.append(
            "Alta sensibilidade a preço exige maior defesa de valor."
        )

    # Risco de perda
    if diagnosis.loss_risk == Level.HIGH:
        score -= 10
        reasons.append(
            "Alto risco de perda exige ação comercial imediata."
        )

    elif diagnosis.loss_risk == Level.MEDIUM:
        score -= 5
        reasons.append(
            "Existe risco moderado de perda da oportunidade."
        )

    elif diagnosis.loss_risk == Level.LOW:
        score += 5
        reasons.append(
            "Baixo risco de perda da oportunidade."
        )

    score = max(0, min(score, 100))

    priority = classify_priority(score)

    next_best_action = determine_next_best_action(
        diagnosis=diagnosis,
        score=score,
    )

    return OpportunityScore(
        score=score,
        priority=priority,
        next_best_action=next_best_action,
        reasons=reasons,
    )


def classify_priority(score: int) -> str:
    """Converte o score numérico em prioridade comercial."""

    if score >= 70:
        return "Alta"

    if score >= 45:
        return "Média"

    return "Baixa"


def determine_next_best_action(
    diagnosis: OpportunityDiagnosis,
    score: int,
) -> str:
    """Define a próxima melhor ação comercial."""

    if diagnosis.loss_risk == Level.HIGH:
        return (
            "Priorizar contato e reduzir o risco de perda "
            "antes de ampliar a oferta."
        )

    if diagnosis.price_sensitivity == Level.HIGH:
        return (
            "Reforçar valor, aderência e benefícios "
            "antes de negociar preço."
        )

    if diagnosis.customer_profile == CustomerProfile.UNDEFINED:
        return (
            "Aprofundar a qualificação para identificar "
            "os principais motivadores de compra."
        )

    if score >= 70:
        return (
            "Avançar para fechamento, reforçando a recomendação "
            "principal e explorando oportunidades de expansão da cesta."
        )

    if score >= 45:
        return (
            "Consolidar a proposta de valor e tratar as principais "
            "objeções antes do fechamento."
        )

    return (
        "Manter a oportunidade em desenvolvimento e coletar "
        "mais contexto antes de avançar."
    )