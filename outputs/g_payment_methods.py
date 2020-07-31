from django.db import models
class g_payment_methods(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	payment_method = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class g_payment_methodsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_payment_methods
		fields="__all__"
class g_payment_methodsView(viewsets.ModelViewSet):
	queryset=models.g_payment_methods.objects.all()
	serializer_class=srealizer.g_payment_methodsSerliazer


