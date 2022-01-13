from django.db import models
import uuid
class wareHouse(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    def __str__(self):
        return self.name

class inventory(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False,
         unique=True)
    name = models.CharField(max_length=128)
    SKU = models.CharField(max_length=64, blank=True)
    warehouse = models.ForeignKey(wareHouse, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name