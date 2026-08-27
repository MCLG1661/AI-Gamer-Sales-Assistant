import streamlit as st

from src.diagnosis import diagnose_opportunity
from src.models import CustomerContext, Level
from src.recommendation import build_sales_recommendation


st.set_page_config(
    page_title="AI Gamer Sales Assistant",
    page_icon="🎮",
    layout="wide",
)


LEVEL_MAP = {
    "Não informada": Level.UNDEFINED,
    "Baixa": Level.LOW,
    "Média": Level.MEDIUM,
    "Alta": Level.HIGH,
}


def format_currency(value: float | None) -> str:
    if value is None:
        return "Não informado"

    return (
        f"R$ {value:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


st.title("🎮 AI Gamer Sales Assistant")
st.caption(
    "Assistente consultivo para diagnóstico, recomendação "
    "e estratégia comercial no mercado gamer."
)

st.markdown(
    """
    Transforme a necessidade do cliente em uma análise estruturada de
    **oportunidade, produto, abordagem comercial e fechamento**.
    """
)

st.divider()


# =========================================================
# 1. QUALIFICAÇÃO
# =========================================================

st.subheader("1. Qualificação do cliente")

col1, col2 = st.columns(2)

with col1:
    need = st.text_area(
        "Necessidade do cliente",
        placeholder=(
            "Ex.: Preciso de um notebook para meu filho estudar, "
            "mas ele também quer jogar com bom desempenho."
        ),
        height=120,
    )

    budget = st.number_input(
        "Orçamento máximo (R$)",
        min_value=0.0,
        step=500.0,
        value=0.0,
    )

    urgency_label = st.selectbox(
        "Urgência da compra",
        list(LEVEL_MAP.keys()),
    )

with col2:
    usage = st.multiselect(
        "Principais usos",
        [
            "estudo",
            "jogos",
            "trabalho",
            "streaming",
            "setup",
            "mobilidade",
            "comunicação",
        ],
    )

    mobility = st.selectbox(
        "Mobilidade é importante?",
        ["Não informado", "Sim", "Não"],
    )

    decision_maker = st.text_input(
        "Quem decide a compra?",
        placeholder="Ex.: Pai, mãe, próprio usuário...",
    )


analyze = st.button(
    "Analisar oportunidade",
    type="primary",
    use_container_width=True,
)


# =========================================================
# ANÁLISE
# =========================================================

if analyze:

    if not need.strip():
        st.warning(
            "Informe a necessidade do cliente antes de iniciar a análise."
        )
        st.stop()

    context = CustomerContext(
        need=need.strip(),
        budget=budget if budget > 0 else None,
        usage=usage,
        mobility=(
            True
            if mobility == "Sim"
            else False
            if mobility == "Não"
            else None
        ),
        urgency=LEVEL_MAP[urgency_label],
        decision_maker=decision_maker.strip() or None,
    )

    diagnosis = diagnose_opportunity(context)

    recommendation = build_sales_recommendation(
        context,
        diagnosis,
    )

    st.divider()

    # =====================================================
    # 2. DIAGNÓSTICO
    # =====================================================

    st.subheader("2. Diagnóstico da oportunidade")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Oportunidade",
        diagnosis.opportunity_type.value,
    )

    c2.metric(
        "Perfil",
        diagnosis.customer_profile.value,
    )

    c3.metric(
        "Sensibilidade a preço",
        diagnosis.price_sensitivity.value,
    )

    c4.metric(
        "Risco de perda",
        diagnosis.loss_risk.value,
    )

    st.divider()

    # =====================================================
    # 3. OFERTA PRINCIPAL
    # =====================================================

    st.subheader("3. Oferta principal")

    if recommendation.main_offer:

        offer_col, rationale_col = st.columns([1, 1])

        with offer_col:
            st.success(
                f"Produto recomendado: {recommendation.main_offer}"
            )

            st.metric(
                "Preço",
                format_currency(
                    recommendation.main_offer_price
                ),
            )

            st.markdown("#### Principais características")

            for feature in recommendation.main_offer_features:
                st.write(f"• {feature}")

        with rationale_col:
            st.markdown("#### Por que esta recomendação?")

            st.write(recommendation.value_argument)

            if context.budget is not None:
                st.write(
                    f"**Orçamento informado:** "
                    f"{format_currency(context.budget)}"
                )

            st.write(
                f"**Perfil identificado:** "
                f"{diagnosis.customer_profile.value}"
            )

            st.write(
                f"**Tipo da oportunidade:** "
                f"{diagnosis.opportunity_type.value}"
            )

        st.divider()

        # =================================================
        # 4. ESTRATÉGIA COMERCIAL
        # =================================================

        st.subheader("4. Estratégia comercial")

        col_up, col_premium, col_cross = st.columns(3)

        with col_up:
            st.markdown("#### Upsell")

            if recommendation.upsell:
                for product in recommendation.upsell:
                    st.write(f"⬆️ {product}")
            else:
                st.write(
                    "Nenhum upgrade dentro do orçamento "
                    "foi identificado."
                )

        with col_premium:
            st.markdown("#### Alternativa premium")

            if recommendation.premium_alternative:
                st.write(
                    f"⭐ {recommendation.premium_alternative}"
                )

                st.write(
                    format_currency(
                        recommendation.premium_alternative_price
                    )
                )

                st.caption(
                    "Opção superior, mas acima do orçamento "
                    "máximo informado."
                )
            else:
                st.write(
                    "Nenhuma alternativa premium identificada."
                )

        with col_cross:
            st.markdown("#### Cross-sell")

            if recommendation.cross_sell:
                for product in recommendation.cross_sell:
                    st.write(f"➕ {product}")
            else:
                st.write(
                    "Nenhum produto complementar identificado."
                )

        st.divider()

        # =================================================
        # 5. FECHAMENTO
        # =================================================

        st.subheader("5. Abordagem de fechamento")

        st.info(
            recommendation.closing_trigger
            or "Sem estratégia de fechamento definida."
        )

    else:
        st.warning(
            recommendation.value_argument
            or "Nenhuma recomendação encontrada."
        )

    # =====================================================
    # TRANSPARÊNCIA
    # =====================================================

    with st.expander("Como o diagnóstico foi construído"):
        for item in diagnosis.rationale:
            st.write(f"• {item}")

    st.caption(
        "Protótipo educacional: catálogo, produtos, preços e regras "
        "comerciais são simulados e não representam estoque real."
    )