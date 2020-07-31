from django.db import models
class g_order_status_codes(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	order_status_desc = models.CharField(max_length=500,blank=False) # 
	order_status_code = models.IntegerField(blank=False) # 

class g_order_status_codesSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_order_status_codes
		fields="__all__"
class g_order_status_codesView(viewsets.ModelViewSet):
	queryset=models.g_order_status_codes.objects.all()
	serializer_class=srealizer.g_order_status_codesSerliazer


