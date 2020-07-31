from django.db import models
class product(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_price_descsion_factor = models.ForeignKey(g_price_descsion_factor,on_delete=models.CASCADE) # Not Sure
	fk_product_subcategory = models.ForeignKey(g_product_subcategory,on_delete=models.CASCADE) # 
	fk_product_category = models.ForeignKey(g_product_category,on_delete=models.CASCADE) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	fk_product_varient = models.ForeignKey(g_product_varient,on_delete=models.CASCADE) # 
	fk_currency = models.ForeignKey(g_currency,on_delete=models.CASCADE,blank=True) # 
	fk_photos = models.ForeignKey(product_photos,on_delete=models.CASCADE,blank=True) # 
	product_name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 
	price = models.CharField(max_length=500,blank=False) # 
	total_count = models.IntegerField(blank=False) # 
	percent_discount = models.DecimalField(max_digits=500,decimal_places=2,blank=True) # 

class productSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product
		fields="__all__"
class productView(viewsets.ModelViewSet):
	queryset=models.product.objects.all()
	serializer_class=srealizer.productSerliazer


# fk_price_descsion_factor -> g_price_descsion_factor 
# fk_product_category -> g_product_category 
# fk_product_subcategory -> g_product_subcategory 
# fk_seller_id -> seller
# fk_product_varient -> product_varients 
# fk_currency -> g_currency 
# fk_photos -> product_photos