from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    established_date = models.DateField()
    logo = models.ImageField(upload_to='brand_logos/')  # Assuming you want to store brand logos as images
    website = models.URLField(blank=True)  # Website URL of the brand (optional)
    email = models.EmailField(blank=True)  # Email address of the brand (optional)
    contact_number = models.CharField(max_length=20, blank=True)  # Contact number of the brand (optional)
    is_active = models.BooleanField(default=True)  # Whether the brand is active or not
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
