
from django.db import models
class customer(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	gender = models.CharField(max_length=500,blank=False) # 
	first_name = models.CharField(max_length=500,blank=False) # 
	middle_name = models.CharField(max_length=500,blank=True) # 
	last_name = models.CharField(max_length=500,blank=False) # 
	email_addess = models.EmailField(max_length=500,blank=True) # 
	phone_1 = models.IntegerField(blank=False) # 
	phone_2 = models.IntegerField(blank=False) # 
	zone_fk = models.ForeignKey(zone,on_delete=models.CASCADE) # 
	date_last_conntected = models.DateTimeField(blank=False) # 
	fk_image = models.ForeignKey(image_customer,on_delete=models.CASCADE) # 

class customerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.customer
		fields="__all__"
class customerView(viewsets.ModelViewSet):
	queryset=models.customer.objects.all()
	serializer_class=srealizer.customerSerliazer


# zone_fk -> zone 
# fk_image -> image_customer 
