Task 3: Job Application Tracker (Relational DB + Search)

Goal: Build a Job Application Tracker with SQLModel.


Features:

JobApplication model: company, position, status, date_applied.

Each user can only access their own applications (auth required).

Endpoints:

POST /applications/ — add new job application.

GET /applications/ — list all.

GET /applications/search?status=pending.

Use error handling for invalid queries.

Use middleware to reject requests if User-Agent header is missing.