from django.db import models
class shipment(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_order_id = models.ForeignKey(order,on_delete=models.CASCADE) # 
	fk_invoice_number = models.ForeignKey(invoice,on_delete=models.CASCADE) # 
	shipment_tracking_number = models.IntegerField(blank=False) # 
	fk_delivery_man = models.ForeignKey(delivery_man,on_delete=models.CASCADE) # 
	fk_address = models.ForeignKey(address,on_delete=models.CASCADE) # 
	shipment_date = models.DateTimeField(blank=False) # 

class shipmentSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.shipment
		fields="__all__"
class shipmentView(viewsets.ModelViewSet):
	queryset=models.shipment.objects.all()
	serializer_class=srealizer.shipmentSerliazer


# fk_order_id -> order 
# fk_invoice_number -> invoice 
# fk_delivery_man -> delivery_man 
# fk_address -> address 
