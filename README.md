# Mini EnterpriseFlow Backend

Backend API built using FastAPI + MySQL for enterprise workflow and collaboration management.

---

# Features

## Authentication
- JWT Authentication
- Refresh Token Support
- Protected APIs
- Role Based Access Control

---

## Task Management
- Create Tasks
- Update Tasks
- Delete Tasks
- Soft Delete & Restore
- Pagination
- Filtering
- Sorting

---

## Approval Workflow
- Submit Approval Requests
- Approve Requests
- Reject Requests
- Approval History

---

## Notifications
- Real-Time Notifications
- Mark Notifications as Read
- Delete Notifications

---

## Comments & Collaboration
- Add Comments
- Reply to Comments
- Task Discussion System

---

## File Management
- Upload Attachments
- Download Attachments
- Delete Attachments

---

## Document Management
- Upload Documents
- Download Documents
- Get Documents

---

## Task History
- Create Task History
- Update Task History
- Delete Task History
- View Task Activity Logs

---

## Saved Filters
- Save Task Filters
- Get Saved Filters
- Delete Saved Filters

---

## Dashboard
- Employee Dashboard
- Manager Dashboard
- Admin Dashboard

---

## Export Features
- Export Tasks CSV
- Export Approvals CSV

---

## Background Tasks
- Background Email Sending
- Async Processing

---

## WebSocket Features
- Real-Time Communication
- Live Updates

---

## Admin Features
- Manage Users
- Create Departments
- Audit Logs

---

# Tech Stack

- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- WebSockets
- Background Tasks
- Uvicorn

---

# Project Structure

```bash
mini_enterpriseflow_backend/
│
├── app/
│   ├── admin/
│   ├── approvals/
│   ├── attachments/
│   ├── auth/
│   ├── background/
│   ├── comments/
│   ├── dashboard/
│   ├── database/
│   ├── documents/
│   ├── exports/
│   ├── history/
│   ├── middleware/
│   ├── notifications/
│   ├── realtime/
│   ├── saved_filters/
│   ├── tasks/
│   ├── users/
│   ├── utils/
│   ├── websocket/
│   └── main.py
│
├── uploads/
├── requirements.txt
├── README.md
└── .env
```

---

# API Modules

## Authentication APIs
- POST `/auth/register`
- POST `/auth/login`
- POST `/auth/refresh`
- GET `/auth/me`

---

## Task APIs
- POST `/tasks/`
- GET `/tasks/`
- PUT `/tasks/{task_id}`
- DELETE `/tasks/{task_id}`
- PUT `/tasks/restore/{task_id}`

---

## Notification APIs
- GET `/notifications/`
- PUT `/notifications/{notification_id}`
- DELETE `/notifications/{notification_id}`

---

## Comment APIs
- POST `/comments/`
- GET `/comments/{task_id}`
- POST `/comments/reply`

---

## Attachment APIs
- POST `/attachments/upload`
- GET `/attachments/download/{attachment_id}`
- DELETE `/attachments/{attachment_id}`

---

## History APIs
- POST `/history/`
- GET `/history/{task_id}`
- PUT `/history/{history_id}`
- DELETE `/history/{history_id}`

---

## Saved Filter APIs
- POST `/filters/`
- GET `/filters/`
- DELETE `/filters/{filter_id}`

---

## Export APIs
- GET `/exports/tasks`
- GET `/exports/approvals`

---

## Background Task APIs
- POST `/background/send-email`

---

## Document APIs
- POST `/documents/upload`
- GET `/documents/download/{document_id}`
- GET `/documents/`

---

## Approval APIs
- GET `/approvals/`
- POST `/approvals/`
- PUT `/approvals/approve/{request_id}`
- PUT `/approvals/reject/{request_id}`

---

## Admin APIs
- GET `/admin/users`
- DELETE `/admin/users/{user_id}`
- POST `/admin/departments`
- GET `/admin/audit-logs`

---

## Dashboard APIs
- GET `/dashboard/`

---

## WebSocket APIs
- WebSocket `/ws/{user_id}`

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/mini-enterpriseflow-backend.git
```

---

## Move to Project Folder

```bash
cd mini_enterpriseflow_backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux/Mac
```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

Open Browser:

```bash
http://127.0.0.1:8000/docs
```

---

# Database

Database Used:
- MySQL

Example Database Name:
```bash
enterpriseflow
```

---

# Task Status

✅ Task 3 — Advanced Backend Features & Business Workflow Module Completed Successfully