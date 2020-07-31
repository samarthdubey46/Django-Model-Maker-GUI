from django.db import models
class seller_photo(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	photo_url = models.ImageField(blank=False) # 
	fk_photo_type = models.ForeignKey(photo_type,on_delete=models.CASCADE) # 
	isvalid = models.BooleanField(default=False,blank=False) # 

class seller_photoSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_photo
		fields="__all__"
class seller_photoView(viewsets.ModelViewSet):
	queryset=models.seller_photo.objects.all()
	serializer_class=srealizer.seller_photoSerliazer


# fk_seller_id -> seller 
# fk_photo_type -> photo_type 
