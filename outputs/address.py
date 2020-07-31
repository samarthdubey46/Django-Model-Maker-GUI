from django.db import models
class address(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	line1 = models.CharField(max_length=500,blank=False) # 
	fk_address_type = models.ForeignKey(g_address_types,on_delete=models.CASCADE) # 
	line2 = models.CharField(max_length=500,blank=False) # 
	line3 = models.CharField(max_length=500,blank=False) # 
	zip = models.IntegerField(blank=False) # 
	fk_zone = models.ForeignKey(zone,on_delete=models.CASCADE) # 

class addressSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.address
		fields="__all__"
class addressView(viewsets.ModelViewSet):
	queryset=models.address.objects.all()
	serializer_class=srealizer.addressSerliazer

	
# fk_address_type -> g_address_types 
# fk_zone -> zone 
