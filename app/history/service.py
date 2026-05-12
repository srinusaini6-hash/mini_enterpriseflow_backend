from app.history.models import TaskHistory


def create_history(
    db,
    task_id,
    changed_by,
    field_name,
    old_value,
    new_value
):

    history = TaskHistory(
        task_id=task_id,
        changed_by=changed_by,
        field_name=field_name,
        old_value=str(old_value),
        new_value=str(new_value)
    )

    db.add(history)
    db.commit()