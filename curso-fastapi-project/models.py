# importando libreria
from pydantic import BaseModel
from sqlmodel import SQLModel

class CustomerBase(SQLModel):
    name : str
    age : int
    description : str | None
    email : str

class CustomerCreate(CustomerBase):
    pass

class Customer(SQLModel, table=True):
    id : int | None =  None

class Transaction(BaseModel):
    id : int
    amount : int
    description : str 

 
class Invoice(BaseModel):
    id : int
    customer : Customer
    transactions : list[Transaction]
    total : int

    @property
    def total(self):
        return sum(transactions.amount for transaction in self.transactions)    