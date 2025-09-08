Task 5: Contact Manager API (Complete Integration Project)

Goal: Create a full Contact Management System using SQLModel + FastAPI + Security.

Features:

Contact model: id, name, email, phone, user_id (foreign key).

Endpoints:

POST /contacts/ — add new contact (only logged-in user).

GET /contacts/ — list user’s contacts.

PUT /contacts/{id} — update.

DELETE /contacts/{id} — delete.

Dependency injection for DB.

Security: JWT-based authentication.

Middleware to log IP address of every request.

Enable CORS.