from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'country', 'established_date', 'logo' ,'website', 'email', 'contact_number','is_active','created_at', 'updated_at']
