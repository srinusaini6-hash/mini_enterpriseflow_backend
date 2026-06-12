from sqlalchemy import select

from app.workspaces.models import Workspace


class WorkspaceService:

    @staticmethod
    def create_workspace(db, payload):

        workspace = Workspace(
            tenant_id=1,
            name=payload.name,
            slug=payload.slug,
            description=payload.description,
            visibility=payload.visibility,
            created_by=1
        )

        db.add(workspace)
        db.commit()
        db.refresh(workspace)

        return workspace

    @staticmethod
    def list_workspaces(db):

        return db.scalars(
            select(Workspace)
        ).all()

    @staticmethod
    def get_workspace(db, workspace_id):

        return db.scalar(
            select(Workspace).where(
                Workspace.id == workspace_id
            )
        )

    @staticmethod
    def update_workspace(
        db,
        workspace_id,
        payload
    ):

        workspace = db.scalar(
            select(Workspace).where(
                Workspace.id == workspace_id
            )
        )

        if not workspace:
            return {"message": "Workspace not found"}

        workspace.name = payload.name
        workspace.description = payload.description
        workspace.visibility = payload.visibility

        db.commit()
        db.refresh(workspace)

        return workspace

    @staticmethod
    def archive_workspace(
        db,
        workspace_id
    ):

        workspace = db.scalar(
            select(Workspace).where(
                Workspace.id == workspace_id
            )
        )

        if not workspace:
            return {"message": "Workspace not found"}

        workspace.is_archived = True

        db.commit()

        return {
            "message": "Workspace archived successfully"
        }

    @staticmethod
    def restore_workspace(
        db,
        workspace_id
    ):

        workspace = db.scalar(
            select(Workspace).where(
                Workspace.id == workspace_id
            )
        )

        if not workspace:
            return {"message": "Workspace not found"}

        workspace.is_archived = False

        db.commit()

        return {
            "message": "Workspace restored successfully"
        }