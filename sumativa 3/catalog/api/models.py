from ninja import Schema
from typing import List
from services.models import Provider, Address, Contact, Service

class ProviderInputSchema(Schema):
    fantasy_name: str
    tax_name: str
    tax_id: str
    enabled: bool

class ProviderOutputSchema(ProviderInputSchema):
    id: int

class AddressInputSchema(Schema):
    address1: str
    address2: str
    zipcode: str
    city: str
    region: str
    country: str

class AddressOutputSchema(AddressInputSchema):
    id: int

class ContactInputSchema(Schema):
    first_name: str
    last_name: str
    email: str
    phone: str
    mobile: str

class ContactOutputSchema(ContactInputSchema):
    id: int

class ServiceInputSchema(Schema):
    name: str
    description: str
    provider: int
    price: int

class ServiceOutputSchema(ServiceInputSchema):
    id: int
    from_date: str
    thru_date: str
    addresses: List[AddressOutputSchema]  # Utilizar "addresses" en lugar de "address_set"
    contacts: List[ContactOutputSchema]   # Utilizar "contacts" en lugar de "contact_set"


class ServiceCreatedResponseSchema(Schema):
    message: str

class ServiceDeletedResponseSchema(Schema):
    message: str
