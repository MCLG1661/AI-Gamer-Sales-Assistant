from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class CustomerProfile(str, Enum):
    RATIONAL = "Racional"
    EMOTIONAL = "Emocional"
    HYBRID = "Híbrido"
    UNDEFINED = "Não definido"


class OpportunityType(str, Enum):
    LOW_TICKET = "Low Ticket"
    MIXED = "Misto"
    HIGH_TICKET = "High Ticket"
    UNDEFINED = "Não definido"


class Level(str, Enum):
    LOW = "Baixa"
    MEDIUM = "Média"
    HIGH = "Alta"
    UNDEFINED = "Não definida"


@dataclass
class CustomerContext:
    """Informações coletadas durante a qualificação do cliente."""

    need: str
    budget: Optional[float] = None
    usage: list[str] = field(default_factory=list)
    expected_performance: Optional[str] = None
    mobility: Optional[bool] = None
    urgency: Level = Level.UNDEFINED
    decision_maker: Optional[str] = None
    channel: Optional[str] = None


@dataclass
class OpportunityDiagnosis:
    """Diagnóstico comercial gerado a partir do contexto do cliente."""

    opportunity_type: OpportunityType = OpportunityType.UNDEFINED
    customer_profile: CustomerProfile = CustomerProfile.UNDEFINED
    urgency: Level = Level.UNDEFINED
    price_sensitivity: Level = Level.UNDEFINED
    loss_risk: Level = Level.UNDEFINED
    rationale: list[str] = field(default_factory=list)


@dataclass
class SalesRecommendation:
    """Estrutura da recomendação comercial produzida pelo assistente."""

    main_offer: Optional[str] = None
    main_offer_price: Optional[float] = None
    main_offer_features: list[str] = field(default_factory=list)
    value_argument: Optional[str] = None
    upsell: list[str] = field(default_factory=list)
    premium_alternative: Optional[str] = None
    premium_alternative_price: Optional[float] = None
    cross_sell: list[str] = field(default_factory=list)
    closing_trigger: Optional[str] = None
    final_message: Optional[str] = None