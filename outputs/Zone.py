from django.db import models
class zone(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_country_id = models.ForeignKey(g_country,on_delete=models.CASCADE) # 
	fk_state_id = models.ForeignKey(g_state,on_delete=models.CASCADE) # 
	fk_city_id = models.ForeignKey(g_city,on_delete=models.CASCADE) # 
	zone_name = models.CharField(max_length=500,blank=False) # 

class zoneSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.Zone
		fields="__all__"
class zoneView(viewsets.ModelViewSet):
	queryset=models.Zone.objects.all()
	serializer_class=srealizer.ZoneSerliazer