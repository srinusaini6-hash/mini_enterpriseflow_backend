from datetime import date, datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict


# ==========================================================
# Analytics Snapshot
# ==========================================================

class AnalyticsSnapshotBase(BaseModel):
    tenant_id: int
    snapshot_type: str
    snapshot_date: date
    data_json: Dict[str, Any]


class AnalyticsSnapshotCreate(AnalyticsSnapshotBase):
    pass


class AnalyticsSnapshotResponse(AnalyticsSnapshotBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# Task Analytics
# ==========================================================

class TaskAnalyticsResponse(BaseModel):
    total_tasks: int
    created_tasks: int
    completed_tasks: int
    pending_tasks: int
    overdue_tasks: int
    average_completion_time: float

    tasks_by_status: Dict[str, int]
    tasks_by_priority: Dict[str, int]

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# Task Trends
# ==========================================================

class TaskTrend(BaseModel):
    period: str
    created: int
    completed: int


class TaskTrendResponse(BaseModel):
    trends: List[TaskTrend]


# ==========================================================
# Productivity
# ==========================================================

class ProductivityRecord(BaseModel):
    user_id: Optional[int] = None
    user_name: Optional[str] = None

    department_id: Optional[int] = None
    department_name: Optional[str] = None

    team_id: Optional[int] = None
    team_name: Optional[str] = None

    completed_tasks: int


class ProductivityResponse(BaseModel):
    productivity: List[ProductivityRecord]


# ==========================================================
# Approval Analytics
# ==========================================================

class ApprovalAnalyticsResponse(BaseModel):
    total_approvals: int
    pending_approvals: int
    approved_approvals: int
    rejected_approvals: int
    escalated_approvals: int
    average_turnaround_time_days: float


class ApprovalBottleneckResponse(BaseModel):
    approver: str
    pending_count: int


class ApprovalTrendResponse(BaseModel):
    date: str
    total_approvals: int


# ==========================================================
# SLA Analytics
# ==========================================================

class SLAAnalyticsResponse(BaseModel):
    total_sla_records: int
    active_sla_records: int
    completed_within_sla: int
    breached_sla_count: int
    escalated_sla_count: int

    average_resolution_time: float
    sla_compliance_percentage: float


# ==========================================================
# Document Analytics
# ==========================================================

class DocumentAnalyticsResponse(BaseModel):
    total_documents_uploaded: int
    total_downloads: int
    storage_usage: float

    most_downloaded_documents: List[Dict[str, Any]]
    recent_uploads: List[Dict[str, Any]]