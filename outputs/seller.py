from django.db import models
class seller(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 
	fk_seller_sub_category = models.ForeignKey(g_seller_sub_category,on_delete=models.CASCADE) # 
	fk_open_hours = models.ForeignKey(opening_hours,on_delete=models.CASCADE) # 
	rating = models.DecimalField(max_digits=500,decimal_places=2,blank=False) # 
	phone_number_1 = models.CharField(max_length=500,blank=False) # 
	phone_number_2 = models.CharField(max_length=500,blank=True) # 
	email = models.EmailField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=True) # 
	fk_seller_photos = models.ForeignKey(seller_photo,on_delete=models.CASCADE) # 

class sellerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller
		fields="__all__"
class sellerView(viewsets.ModelViewSet):
	queryset=models.seller.objects.all()
	serializer_class=srealizer.sellerSerliazer


# fk_seller_sub_category -> g_seller_sub_category 
# fk_open_hours -> opening_hours 
# fk_seller_photos -> seller_photo 

