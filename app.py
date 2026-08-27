import streamlit as st

from src.basket import build_basket
from src.diagnosis import diagnose_opportunity
from src.message_engine import (
    build_instagram_message,
    build_whatsapp_message,
)
from src.models import CustomerContext, Level
from src.recommendation import build_sales_recommendation
from src.scoring import calculate_opportunity_score
from src.ui import (
    apply_product_theme,
    render_commercial_cockpit,
    render_hero,
    render_sidebar,
)


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


apply_product_theme()
render_sidebar()
render_hero()
render_commercial_cockpit()

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


# =========================================================
# AÇÕES
# =========================================================

button_col1, button_col2 = st.columns([3, 1])

with button_col1:
    analyze = st.button(
        "Analisar oportunidade",
        type="primary",
        use_container_width=True,
    )

with button_col2:
    reset = st.button(
        "↻ Nova análise",
        type="secondary",
        use_container_width=True,
    )

if reset:
    st.session_state.clear()
    st.rerun()


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

    opportunity_score = calculate_opportunity_score(
        diagnosis,
    )

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

    # =====================================================
    # SALES INTELLIGENCE
    # =====================================================

    st.markdown("### Sales Intelligence")

    score_col, priority_col = st.columns([1, 1])

    with score_col:
        st.metric(
            "Opportunity Score",
            f"{opportunity_score.score}/100",
        )

    with priority_col:
        st.metric(
            "Prioridade comercial",
            opportunity_score.priority,
        )

    st.markdown("#### Próxima melhor ação")

    st.info(
        opportunity_score.next_best_action
    )

    with st.expander(
        "Por que esta oportunidade recebeu este score?"
    ):
        for reason in opportunity_score.reasons:
            st.write(f"• {reason}")

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
        # 4. BASKET INTELLIGENCE
        # =================================================

        basket = build_basket(
            main_product_name=recommendation.main_offer,
            main_product_price=recommendation.main_offer_price,
            cross_sell_names=recommendation.cross_sell,
            budget=context.budget,
        )

        st.subheader("4. Basket Intelligence")

        b1, b2, b3, b4 = st.columns(4)

        b1.metric(
            "Orçamento",
            format_currency(basket.budget),
        )

        b2.metric(
            "Oferta principal",
            format_currency(basket.main_product_price),
        )

        b3.metric(
            "Total da solução",
            format_currency(basket.basket_total),
        )

        b4.metric(
            "Saldo restante",
            format_currency(basket.final_remaining_budget),
        )

        st.markdown("#### Complementos selecionados")

        if basket.complementary_products:
            for product in basket.complementary_products:
                st.write(
                    f"➕ {product['name']} — "
                    f"{format_currency(product['price'])}"
                )
        else:
            st.write(
                "Nenhum complemento foi adicionado dentro do orçamento."
            )

        if basket.within_budget:
            st.success(
                "A solução montada permanece dentro do orçamento informado."
            )
        else:
            st.error(
                "A composição ultrapassa o orçamento informado."
            )

        st.divider()

        # =================================================
        # 5. ESTRATÉGIA COMERCIAL
        # =================================================

        st.subheader("5. Estratégia comercial")

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
            st.markdown("#### Cross-sell sugerido")

            if recommendation.cross_sell:
                for product in recommendation.cross_sell:
                    st.write(f"➕ {product}")
            else:
                st.write(
                    "Nenhum produto complementar identificado."
                )

        st.divider()

        # =================================================
        # 6. FECHAMENTO
        # =================================================

        st.subheader("6. Abordagem de fechamento")

        st.info(
            recommendation.closing_trigger
            or "Sem estratégia de fechamento definida."
        )

        st.divider()

        # =================================================
        # 7. MENSAGEM FINAL
        # =================================================

        st.subheader("7. Mensagem final")

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

        tab_whatsapp, tab_instagram = st.tabs(
            [
                "💬 WhatsApp",
                "📱 Instagram / DM",
            ]
        )

        with tab_whatsapp:
            st.text_area(
                "Mensagem pronta para WhatsApp",
                value=whatsapp_message,
                height=320,
            )

        with tab_instagram:
            st.text_area(
                "Mensagem pronta para Instagram / DM",
                value=instagram_message,
                height=180,
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