from django.db import models
class g_product_varient(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	varient_name = models.CharField(max_length=500,blank=False) # 
	varint_desc = models.CharField(max_length=500,blank=False) # 

class g_product_varientSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_product_varient
		fields="__all__"
class g_product_varientView(viewsets.ModelViewSet):
	queryset=models.g_product_varient.objects.all()
	serializer_class=srealizer.g_product_varientSerliazer
