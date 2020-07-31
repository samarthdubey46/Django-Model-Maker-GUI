from django.db import models
class shipment_items(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_order_item_id = models.ForeignKey(order_items,on_delete=models.CASCADE) # 
	fk_shipment_id = models.ForeignKey(shipment,on_delete=models.CASCADE) # 

class shipment_itemsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.shipment_items
		fields="__all__"
class shipment_itemsView(viewsets.ModelViewSet):
	queryset=models.shipment_items.objects.all()
	serializer_class=srealizer.shipment_itemsSerliazer


# fk_order_item_id -> order_items 
# fk_shipment_id -> shipment 
