from fastapi import FastAPI, HTTPException, Path, Query
from models import Contact

app = FastAPI()

# In-memory storage
contacts_db = {}

@app.post("/contacts/", response_model=Contact)
def add_contact(contact: Contact):
    name_key = contact.name.lower()
    if name_key in contacts_db:
        raise HTTPException(status_code=400, detail="Contact already exists.")
    contacts_db[name_key] = contact
    return contact

@app.get("/contacts/", response_model=Contact)
def get_contact_by_query(name: str = Query(..., description="Name of the contact to retrieve")):
    name_key = name.lower()
    contact = contacts_db.get(name_key)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contact

@app.post("/contacts/{name}", response_model=Contact)
def update_contact(
    name: str = Path(..., description="Name of the contact to update"),
    phone: str = Query(None),
    email: str = Query(None)
):
    name_key = name.lower()
    if name_key not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found.")

    contact = contacts_db[name_key]

    # Update fields if provided
    if phone:
        contact.phone = phone
    if email:
        try:
            contact.email = email  # Will validate EmailStr
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid email format")

    contacts_db[name_key] = contact
    return contact

@app.delete("/contacts/{name}")
def delete_contact(name: str = Path(...)):
    name_key = name.lower()
    if name_key not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found.")
    del contacts_db[name_key]
    return {"message": f"Contact '{name}' deleted successfully."}
