from django.db import models
class g_state(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	state = models.CharField(max_length=500,blank=False) # 
	fk_country_id = models.ForeignKey(g_country,on_delete=models.CASCADE) # 

class g_stateSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_state
		fields="__all__"
class g_stateView(viewsets.ModelViewSet):
	queryset=models.g_state.objects.all()
	serializer_class=srealizer.g_stateSerliazer