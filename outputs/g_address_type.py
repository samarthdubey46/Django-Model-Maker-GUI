from django.db import models
class g_address_type(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	type_name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class g_address_typeSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_address_type
		fields="__all__"
class g_address_typeView(viewsets.ModelViewSet):
	queryset=models.g_address_type.objects.all()
	serializer_class=srealizer.g_address_typeSerliazer


