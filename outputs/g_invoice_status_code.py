from django.db import models
class g_invoice_status_code(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	invoice_status_code = models.IntegerField(blank=False) # 
	invoice_status_description = models.CharField(max_length=500,blank=False) # 

class g_invoice_status_codeSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_invoice_status_code
		fields="__all__"
class g_invoice_status_codeView(viewsets.ModelViewSet):
	queryset=models.g_invoice_status_code.objects.all()
	serializer_class=srealizer.g_invoice_status_codeSerliazer


