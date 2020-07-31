from django.db import models
class g_city(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	city = models.CharField(max_length=500,blank=False) # 
	fk_state_id = models.ForeignKey(g_state,on_delete=models.CASCADE) # 

class g_citySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_city
		fields="__all__"
class g_cityView(viewsets.ModelViewSet):
	queryset=models.g_city.objects.all()
	serializer_class=srealizer.g_citySerliazer