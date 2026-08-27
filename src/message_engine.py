from src.basket import BasketResult
from src.models import (
    CustomerContext,
    OpportunityDiagnosis,
    SalesRecommendation,
)


def format_currency(value: float | None) -> str:
    if value is None:
        return "valor não informado"

    return (
        f"R$ {value:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def build_whatsapp_message(
    context: CustomerContext,
    diagnosis: OpportunityDiagnosis,
    recommendation: SalesRecommendation,
    basket: BasketResult,
) -> str:
    """
    Gera uma mensagem comercial consultiva para WhatsApp.

    A mensagem deve respeitar o orçamento declarado, apresentar a
    recomendação principal, contextualizar os complementos e evitar
    pressão comercial excessiva.
    """

    if not recommendation.main_offer:
        return (
            "Com as informações disponíveis, ainda não encontrei uma opção "
            "que atenda bem aos critérios informados. Podemos ajustar o "
            "orçamento, o tipo de uso ou as prioridades para refinar a busca."
        )

    lines = [
        "Com base no que você me contou, encontrei uma opção que faz sentido "
        "para o seu cenário.",
        "",
        f"🎮 {recommendation.main_offer} — "
        f"{format_currency(recommendation.main_offer_price)}",
    ]

    if recommendation.main_offer_features:
        features = ", ".join(recommendation.main_offer_features)
        lines.append(f"Principais características: {features}.")

    lines.extend(
        [
            "",
            recommendation.value_argument
            or "A recomendação foi construída considerando o seu contexto.",
        ]
    )

    if basket.complementary_products:
        lines.append("")
        lines.append("Também é possível completar a solução com:")

        for product in basket.complementary_products:
            lines.append(
                f"• {product['name']} — {format_currency(product['price'])}"
            )

        lines.extend(
            [
                "",
                f"Total da solução: {format_currency(basket.basket_total)}",
            ]
        )

        if basket.final_remaining_budget is not None:
            lines.append(
                f"Saldo em relação ao orçamento informado: "
                f"{format_currency(basket.final_remaining_budget)}"
            )

    if recommendation.premium_alternative:
        lines.extend(
            [
                "",
                "Se quiser considerar uma opção acima do orçamento, existe "
                f"também o {recommendation.premium_alternative} por "
                f"{format_currency(recommendation.premium_alternative_price)}.",
            ]
        )

    lines.extend(
        [
            "",
            (
                "Se essa configuração estiver alinhada ao que você procura, "
                "podemos seguir por ela ou ajustar algum ponto antes da decisão."
            ),
        ]
    )

    return "\n".join(lines)


def build_instagram_message(
    context: CustomerContext,
    diagnosis: OpportunityDiagnosis,
    recommendation: SalesRecommendation,
    basket: BasketResult,
) -> str:
    """
    Gera uma versão mais curta da abordagem para Instagram ou DM.
    """

    if not recommendation.main_offer:
        return (
            "Ainda não encontrei uma opção totalmente aderente ao que você "
            "busca. Posso refinar a recomendação com mais alguns detalhes."
        )

    message = (
        f"🎮 Para o seu cenário, eu recomendaria o "
        f"{recommendation.main_offer} por "
        f"{format_currency(recommendation.main_offer_price)}."
    )

    if basket.complementary_products:
        message += (
            f" Com os complementos selecionados, a solução fica em "
            f"{format_currency(basket.basket_total)}, "
            "mantendo a composição dentro do orçamento informado."
        )

    message += (
        " Se quiser, podemos ajustar a configuração ou comparar com uma "
        "alternativa de maior performance."
    )

    return message