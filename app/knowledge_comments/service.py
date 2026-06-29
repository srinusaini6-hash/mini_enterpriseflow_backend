from sqlalchemy.orm import Session

from app.knowledge_comments.models import KnowledgeComment


def create_comment(db: Session, payload):
    comment = KnowledgeComment(**payload.dict())

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def get_comments(db: Session):
    return db.query(KnowledgeComment).all()


def get_comment(db: Session, comment_id: int):
    return db.query(KnowledgeComment).filter(
        KnowledgeComment.id == comment_id
    ).first()


def get_comments_by_article(db: Session, article_id: int):
    return db.query(KnowledgeComment).filter(
        KnowledgeComment.article_id == article_id
    ).all()


def delete_comment(db: Session, comment_id: int):
    comment = db.query(KnowledgeComment).filter(
        KnowledgeComment.id == comment_id
    ).first()

    if comment:
        db.delete(comment)
        db.commit()

    return comment