import streamlit as st


def apply_product_theme() -> None:
    """Aplica a identidade visual do AI Gamer Sales Assistant."""

    css = """
    <style>
    .stApp {
        background:
            radial-gradient(
                circle at 20% 0%,
                rgba(111, 66, 193, 0.16),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 10%,
                rgba(0, 188, 212, 0.10),
                transparent 25%
            ),
            #050a13;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* HERO */

    .gamer-hero {
        padding: 1.8rem 2rem;
        border: 1px solid rgba(151, 91, 255, 0.45);
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            rgba(111, 45, 189, 0.22),
            rgba(5, 10, 19, 0.92) 60%
        );
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.22);
        margin-bottom: 1.2rem;
    }

    .gamer-eyebrow {
        color: #a970ff;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }

    .gamer-title {
        color: #ffffff;
        font-size: 2.25rem;
        line-height: 1.15;
        font-weight: 800;
        margin-bottom: 0.8rem;
    }

    .gamer-title-accent {
        background: linear-gradient(
            90deg,
            #a970ff,
            #4d7cff,
            #21d4d8
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .gamer-subtitle {
        color: #b8c2d8;
        font-size: 1rem;
        line-height: 1.6;
        max-width: 850px;
    }

    /* SIDEBAR */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #080d18 0%,
                #070b14 100%
            );
        border-right: 1px solid rgba(139, 92, 246, 0.24);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.4rem;
    }

    .sidebar-brand {
        margin-bottom: 1.3rem;
    }

    .sidebar-title {
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 800;
        line-height: 1.25;
    }

    .sidebar-accent {
        color: #a970ff;
    }

    .sidebar-version {
        color: #8892aa;
        font-size: 0.76rem;
        margin-top: 0.3rem;
    }

    .sidebar-section {
        color: #777f95;
        font-size: 0.69rem;
        font-weight: 800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 1.4rem;
        margin-bottom: 0.6rem;
    }

    .sidebar-item {
        color: #cfd6e6;
        font-size: 0.87rem;
        padding: 0.24rem 0;
    }

    .sidebar-status {
        margin-top: 1.4rem;
        padding: 0.8rem 0.9rem;
        background: rgba(27, 38, 60, 0.62);
        border: 1px solid rgba(75, 222, 163, 0.20);
        border-radius: 10px;
    }

    .status-online {
        color: #4ade80;
        font-weight: 700;
    }

    .status-detail {
        color: #969fb3;
        font-size: 0.78rem;
        margin-top: 0.3rem;
    }

    /* COCKPIT */

    .cockpit-label {
        color: #818aa2;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.10em;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }

    .cockpit-card {
        min-height: 104px;
        padding: 1rem 1.05rem;
        border-radius: 13px;
        border: 1px solid rgba(118, 91, 211, 0.25);
        background:
            linear-gradient(
                150deg,
                rgba(24, 33, 54, 0.88),
                rgba(11, 16, 28, 0.92)
            );
    }

    .cockpit-value {
        color: #ffffff;
        font-size: 1.55rem;
        font-weight: 800;
        line-height: 1.1;
    }

    .cockpit-name {
        color: #8f99af;
        font-size: 0.78rem;
        margin-top: 0.4rem;
    }

    /* STREAMLIT */

    h1, h2, h3, h4 {
        color: #f5f7ff !important;
    }

    p, label {
        color: #d9e0ef;
    }

    [data-testid="stMetric"] {
        background: rgba(15, 22, 38, 0.78);
        border: 1px solid rgba(118, 91, 211, 0.20);
        border-radius: 12px;
        padding: 1rem;
    }

    /* BOTÃO PRINCIPAL */

    div.stButton > button[kind="primary"] {
        border: 0;
        border-radius: 9px;
        min-height: 46px;
        font-weight: 700;
        color: #ffffff !important;
        background: linear-gradient(
            90deg,
            #7447db,
            #315fe4
        );
    }

    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 22px rgba(83, 86, 230, 0.30);
    }

    /* BOTÃO SECUNDÁRIO */

    div.stButton > button[kind="secondary"] {
        border: 1px solid rgba(151, 91, 255, 0.55);
        border-radius: 9px;
        min-height: 46px;
        font-weight: 700;
        color: #e8eaf6 !important;
        background: rgba(111, 66, 193, 0.12);
    }

    div.stButton > button[kind="secondary"]:hover {
        border-color: #a970ff;
        color: #ffffff !important;
        background: rgba(111, 66, 193, 0.24);
        transform: translateY(-1px);
        box-shadow: 0 8px 22px rgba(111, 66, 193, 0.18);
    }

    div.stButton > button[kind="secondary"]:focus {
        color: #ffffff !important;
        border-color: #a970ff;
        background: rgba(111, 66, 193, 0.24);
    }

    div.stButton > button[kind="secondary"]:active {
        color: #ffffff !important;
        border-color: #b78cff;
        background: rgba(111, 66, 193, 0.32);
    }

    hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


def render_hero() -> None:
    """Renderiza o cabeçalho principal."""

    hero_html = (
        '<div class="gamer-hero">'
        '<div class="gamer-eyebrow">'
        'AI • SALES INTELLIGENCE • GAMING'
        '</div>'
        '<div class="gamer-title">'
        '🎮 AI Gamer <span class="gamer-title-accent">'
        'Sales Assistant'
        '</span>'
        '</div>'
        '<div class="gamer-subtitle">'
        'Inteligência comercial para transformar necessidades '
        'do cliente em diagnóstico, recomendação de produto, '
        'composição de cesta e abordagem de vendas.'
        '</div>'
        '</div>'
    )

    st.markdown(hero_html, unsafe_allow_html=True)


def render_sidebar() -> None:
    """Renderiza a navegação e o status do produto."""

    with st.sidebar:
        st.markdown(
            (
                '<div class="sidebar-brand">'
                '<div class="sidebar-title">'
                '🎮 AI Gamer<br>'
                '<span class="sidebar-accent">Sales Assistant</span>'
                '</div>'
                '<div class="sidebar-version">'
                'Sales Intelligence • MVP v0.3'
                '</div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="sidebar-section">Jornada comercial</div>',
            unsafe_allow_html=True,
        )

        journey = [
            "① Qualificação",
            "② Diagnóstico",
            "③ Oferta",
            "④ Basket Intelligence",
            "⑤ Estratégia",
            "⑥ Fechamento",
            "⑦ Mensagem final",
        ]

        for item in journey:
            st.markdown(
                f'<div class="sidebar-item">{item}</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            '<div class="sidebar-section">Inteligência</div>',
            unsafe_allow_html=True,
        )

        intelligence = [
            "◈ Customer Profiling",
            "◈ Opportunity Diagnosis",
            "◈ Recommendation Engine",
            "◈ Basket Intelligence",
            "◈ Sales Messaging",
        ]

        for item in intelligence:
            st.markdown(
                f'<div class="sidebar-item">{item}</div>',
                unsafe_allow_html=True,
            )

        st.markdown(
            (
                '<div class="sidebar-status">'
                '<div class="status-online">● Engine operacional</div>'
                '<div class="status-detail">'
                '33 testes automatizados passando'
                '</div>'
                '</div>'
            ),
            unsafe_allow_html=True,
        )


def render_commercial_cockpit() -> None:
    """Renderiza indicadores do produto e do fluxo comercial."""

    st.markdown(
        '<div class="cockpit-label">Commercial Intelligence Cockpit</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    cards = [
        (
            col1,
            "7",
            "Etapas comerciais",
        ),
        (
            col2,
            "3",
            "Perfis de cliente",
        ),
        (
            col3,
            "5",
            "Módulos de inteligência",
        ),
        (
            col4,
            "2",
            "Canais de mensagem",
        ),
    ]

    for column, value, name in cards:
        with column:
            st.markdown(
                (
                    '<div class="cockpit-card">'
                    f'<div class="cockpit-value">{value}</div>'
                    f'<div class="cockpit-name">{name}</div>'
                    '</div>'
                ),
                unsafe_allow_html=True,
            )