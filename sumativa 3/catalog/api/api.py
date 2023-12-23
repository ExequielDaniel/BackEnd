from ninja import NinjaAPI, Redoc
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import ServiceInputSchema,ServiceOutputSchema, ServiceCreatedResponseSchema, ServiceDeletedResponseSchema
from django.utils import timezone
from services.models import Service, Provider, Contact, Address
from typing import List
from datetime import datetime

api = NinjaAPI(docs=Redoc())

# GET Servicios


@api.get("/services", response={200: List[ServiceOutputSchema]})
def get_services(request):
    services = Service.objects.filter(thru_date__isnull=True).select_related("provider")
    services_with_related = services.prefetch_related("address_set", "contact_set")
    
    result = []
    for service in services_with_related:
        addresses = [address.to_dict() for address in service.address_set.all()]
        contacts = [contact.to_dict() for contact in service.contact_set.all()]
        
        service_data = {
            "id": service.id,
            "name": service.name,
            "description": service.description,
            "price": service.price,
            "from_date": service.from_date,
            "provider": {
                "id": service.provider.id,
                "fantasy_name": service.provider.fantasy_name,
                "enabled": service.provider.enabled,
            },
            "addresses": addresses,
            "contacts": contacts,
        }
        result.append(service_data)

    return result



# GET Service
@api.get("/services/{service_id}", response={200: ServiceOutputSchema})
def get_service(request, service_id: int):
    service = get_object_or_404(Service, id=service_id, thru_date__isnull=True)
    return service.to_dict()

# POST Service
@api.post("/services", response={200: ServiceCreatedResponseSchema})
def create_service(request, service: ServiceInputSchema):
    with transaction.atomic():
        provider = get_object_or_404(Provider, id=service.provider)
        new_service = Service.objects.create(
            name=service.name,
            description=service.description,
            provider=provider,
            price=service.price,
        )
    return {"message": "Service created successfully"}

# DELETE Service
# Utiliza el nuevo esquema de respuesta en la operación DELETE
@api.delete("/services/{service_id}", response={200: ServiceDeletedResponseSchema})
def delete_service(request, service_id: int):
    with transaction.atomic():
        service = get_object_or_404(Service, id=service_id, thru_date__isnull=True)
        service.thru_date = timezone.now()
        service.save()
    return {"message": "Service deleted successfully"}