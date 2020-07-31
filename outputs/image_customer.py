from django.db import models
class image_customer(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	profile_picture = models.ImageField(blank=False) # 
	is_valid = models.BooleanField(default=False,blank=False) # 
	uri = models.URLField(max_length=500,blank=False) # 

class image_customerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.image_customer
		fields="__all__"
class image_customerView(viewsets.ModelViewSet):
	queryset=models.image_customer.objects.all()
	serializer_class=srealizer.image_customerSerliazer


# fk_customer_id -> customer 
