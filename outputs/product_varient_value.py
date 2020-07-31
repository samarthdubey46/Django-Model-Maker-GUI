from django.db import models
class product_varient_value(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	varient_value = models.CharField(max_length=500,blank=False) # 
	fk_varient_id = models.ForeignKey(g_product_varients,on_delete=models.CASCADE) # 

class product_varient_valueSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product_varient_value
		fields="__all__"
class product_varient_valueView(viewsets.ModelViewSet):
	queryset=models.product_varient_value.objects.all()
	serializer_class=srealizer.product_varient_valueSerliazer
# fk_varient_id -> g_product_varients 
