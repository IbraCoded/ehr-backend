# tenants/models.py

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    # TenantMixin already provides the primary key (usually 'id' as a UUIDField

    name = models.CharField(max_length=100, unique=True)
    # subdomain = models.CharField(max_length=50, unique=True) # You can also use a Domain model for this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    auto_create_schema = True  # Automatically create schema for this tenant. its is already set to True by default in TenantMixin but lets explicitly set it

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'tenants' 

class Domain(DomainMixin):
    pass