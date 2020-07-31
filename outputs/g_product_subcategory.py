from django.db import models
class g_product_subcategory(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_product_id = models.ForeignKey(product,on_delete=models.CASCADE) # Not Sure ForiegnKey_Name
	desc = models.CharField(max_length=500,blank=False) # 

class g_product_subcategorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_product_subcategory
		fields="__all__"
class g_product_subcategoryView(viewsets.ModelViewSet):
	queryset=models.g_product_subcategory.objects.all()
	serializer_class=srealizer.g_product_subcategorySerliazer