from django.db import models

class ConsentLog(models.Model):
    patient_id = models.UUIDField(unique=True)
    hospital_id = models.CharField(max_length=100)
    token = models.CharField(max_length=50, unique=True)
    expiry_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('revoked', 'Revoked')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consent for {self.patient_id} to {self.hospital_id}"

    class Meta:
        app_label = 'consents'