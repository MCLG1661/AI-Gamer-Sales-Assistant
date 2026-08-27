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

    h1, h2, h3, h4 {
        color: #f5f7ff !important;
    }

    p, label {
        color: #d9e0ef;
    }

    div.stButton > button[kind="primary"] {
        border: 0;
        border-radius: 9px;
        min-height: 46px;
        font-weight: 700;
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

    hr {
        border-color: rgba(255, 255, 255, 0.08) !important;
    }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


def render_hero() -> None:
    """Renderiza o cabeçalho principal do produto."""

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

    st.markdown(
        hero_html,
        unsafe_allow_html=True,
    )