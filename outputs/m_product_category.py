from django.db import models
class g_product_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	product_type = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class g_product_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.m_product_category
		fields="__all__"
class g_product_categoryView(viewsets.ModelViewSet):
	queryset=models.m_product_category.objects.all()
	serializer_class=srealizer.m_product_categorySerliazer