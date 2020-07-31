from django.db import models
class seller_sub_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class seller_sub_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_sub_category
		fields="__all__"
class seller_sub_categoryView(viewsets.ModelViewSet):
	queryset=models.seller_sub_category.objects.all()
	serializer_class=srealizer.seller_sub_categorySerliazer


