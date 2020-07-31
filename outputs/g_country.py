from django.db import models
class g_country(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 

class g_countrySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_country
		fields="__all__"
class g_countryView(viewsets.ModelViewSet):
	queryset=models.g_country.objects.all()
	serializer_class=srealizer.g_countrySerliazer