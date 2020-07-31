from django.db import models
class g_seller_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	product_type = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class g_seller_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_seller_category
		fields="__all__"
class g_seller_categoryView(viewsets.ModelViewSet):
	queryset=models.g_seller_category.objects.all()
	serializer_class=srealizer.g_seller_categorySerliazer


