import zoneinfo
from fastapi import FastAPI
from datetime import datetime
# Importando modelos de nuestro achivo
from models import Customer, Transaction, Invoice, CustomerCreate
from db import SessionDep


app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hola Andres"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}")

async def time(iso_code:str):
    iso = iso_code.upper()
    timeZoneStr=country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timeZoneStr)
    return{"time": datetime.now(tz)}


db_customers:list[Customer] = []
current_id : int = 0


@app.post("/customers",response_model=Customer)
async def create_customer(customer_data:CustomerCreate, session:SessionDep):
    # Simulando auto agregado de ID de una BD
    customer = Customer.model_validate(customer_data.model_dump())
    
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer


@app.get("/customers", response_model=list[Customer])
async def list_customer():
    return db_customers



@app.post("/transactions")
async def create_transactions(transactions_data:Transaction):
    return transactions_data

@app.post("/invoices")
async def create_invoices(invoice_data:Invoice):
    return invoice_data