from django.db import models
class seller_reviews(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	Review = models.CharField(max_length=500,blank=False) # 
	rating = models.CharField(max_length=500,blank=False) # 
	isvalid = models.BooleanField(default=False,blank=False) # 
	likes = models.IntegerField(blank=False) # 

class seller_reviewsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_reviews
		fields="__all__"
class seller_reviewsView(viewsets.ModelViewSet):
	queryset=models.seller_reviews.objects.all()
	serializer_class=srealizer.seller_reviewsSerliazer


# fk_customer_id -> customer 
# fk_seller_id -> seller 
