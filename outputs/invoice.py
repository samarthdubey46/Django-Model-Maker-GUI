from django.db import models
class invoice(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) #
	fk_order_id = models.ForeignKey(order,on_delete=models.CASCADE) # 
	fk_invoice_status_code = models.ForeignKey(g_invoice_status_code,on_delete=models.CASCADE) # 
	invoice_details = models.CharField(max_length=500,blank=False) # 

class invoiceSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.invoice
		fields="__all__"
class invoiceView(viewsets.ModelViewSet):
	queryset=models.invoice.objects.all()
	serializer_class=srealizer.invoiceSerliazer


# fk_order_id -> order 
# fk_invoice_status_code -> g_invoice_status_code 
