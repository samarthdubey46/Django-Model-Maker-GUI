from django.db import models
class seller_highlights(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	highlight_1 = models.ImageField(blank=False) # 
	highlight_2 = models.ImageField(blank=False) # 
	highlight_3 = models.ImageField(blank=False) # 
	highlight_3 = models.ImageField(blank=False) # 
	highlight_4 = models.ImageField(blank=False) # 
	highlight_6 = models.ImageField(blank=False) # 
	highlight_7 = models.ImageField(blank=False) # 
	highlight_8 = models.ImageField(blank=False) # 

class seller_highlightsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_highlights
		fields="__all__"
class seller_highlightsView(viewsets.ModelViewSet):
	queryset=models.seller_highlights.objects.all()
	serializer_class=srealizer.seller_highlightsSerliazer


# fk_seller_id -> seller 
