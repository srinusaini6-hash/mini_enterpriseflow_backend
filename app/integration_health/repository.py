from sqlalchemy.orm import Session

from app.integration_health.models import IntegrationHealth
from app.integration_health.schemas import (
    IntegrationHealthCreate,
    IntegrationHealthUpdate,
)


def create_integration_health(
    db: Session,
    health: IntegrationHealthCreate,
):
    db_health = IntegrationHealth(
        integration_id=health.integration_id,
        health_status=health.health_status,
        response_time=health.response_time,
        remarks=health.remarks,
    )

    db.add(db_health)
    db.commit()
    db.refresh(db_health)

    return db_health


def get_all_integration_health(
    db: Session,
):
    return db.query(IntegrationHealth).all()


def get_integration_health_by_id(
    db: Session,
    health_id: int,
):
    return (
        db.query(IntegrationHealth)
        .filter(IntegrationHealth.id == health_id)
        .first()
    )


def update_integration_health(
    db: Session,
    health_id: int,
    health: IntegrationHealthUpdate,
):
    db_health = (
        db.query(IntegrationHealth)
        .filter(IntegrationHealth.id == health_id)
        .first()
    )

    if not db_health:
        return None

    update_data = health.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_health, key, value)

    db.commit()
    db.refresh(db_health)

    return db_health


def delete_integration_health(
    db: Session,
    health_id: int,
):
    db_health = (
        db.query(IntegrationHealth)
        .filter(IntegrationHealth.id == health_id)
        .first()
    )

    if not db_health:
        return None

    db.delete(db_health)
    db.commit()

    return db_health