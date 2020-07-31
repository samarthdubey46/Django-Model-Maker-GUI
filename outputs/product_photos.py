from django.db import models
class product_photos(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	image_1 = models.ImageField(blank=False) # 
	image_2 = models.ImageField(blank=True) # 
	image_3 = models.ImageField(blank=True) # 
	image_4 = models.ImageField(blank=True) # 
	image_5 = models.ImageField(blank=True) # 
	image_6 = models.ImageField(blank=True) # 
	image_7 = models.ImageField(blank=True) # 

class product_photosSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product_photos
		fields="__all__"
class product_photosView(viewsets.ModelViewSet):
	queryset=models.product_photos.objects.all()
	serializer_class=srealizer.product_photosSerliazer


