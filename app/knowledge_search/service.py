from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.knowledge_search.models import KnowledgeSearch


class KnowledgeSearchService:

    @staticmethod
    def create(db: Session, data):
        article = KnowledgeSearch(**data.dict())

        db.add(article)
        db.commit()
        db.refresh(article)

        return article

    @staticmethod
    def get_all(db: Session):
        return db.query(KnowledgeSearch).all()

    @staticmethod
    def get_by_id(db: Session, article_id: int):
        return (
            db.query(KnowledgeSearch)
            .filter(KnowledgeSearch.id == article_id)
            .first()
        )

    @staticmethod
    def search(db: Session, keyword: str):
        return (
            db.query(KnowledgeSearch)
            .filter(
                or_(
                    KnowledgeSearch.title.ilike(f"%{keyword}%"),
                    KnowledgeSearch.content.ilike(f"%{keyword}%"),
                    KnowledgeSearch.category.ilike(f"%{keyword}%")
                )
            )
            .all()
        )

    @staticmethod
    def delete(db: Session, article_id: int):
        article = (
            db.query(KnowledgeSearch)
            .filter(KnowledgeSearch.id == article_id)
            .first()
        )

        if not article:
            return False

        db.delete(article)
        db.commit()

        return True