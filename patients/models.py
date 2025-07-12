from django.db import models
from django.contrib.auth.models import User
import uuid
from encrypted_model_fields.fields import EncryptedCharField

class PatientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_id = models.UUIDField(unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Patient {self.user.username}"

    class Meta:
        app_label = 'patients'

class Patient(models.Model):
    patient_id = EncryptedCharField(max_length=100, unique=True)
    first_name = EncryptedCharField(max_length=100)
    last_name = EncryptedCharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        app_label = 'patients'