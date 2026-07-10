from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.database import Base


class AIInsight(Base):
    """
    Stores rule-based AI insights generated
    from analytics data.
    """

    __tablename__ = "ai_insights"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id"),
        nullable=True,
    )

    insight_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        default="LOW",
    )

    generated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    generated_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )