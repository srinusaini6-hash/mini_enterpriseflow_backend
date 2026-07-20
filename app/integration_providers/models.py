from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class IntegrationProvider(Base):
    __tablename__ = "integration_providers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    provider_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
        index=True,
    )
    # Examples:
    # GOOGLE
    # MICROSOFT
    # JIRA
    # TRELLO
    # ASANA
    # ZOOM
    # HRMS
    # ERP
    # CRM

    provider_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )
    # Examples:
    # CALENDAR
    # TASK
    # STORAGE
    # HRMS
    # CRM

    auth_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    # Examples:
    # OAUTH
    # API_KEY
    # WEBHOOK

    base_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )