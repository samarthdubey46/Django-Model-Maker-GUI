from django.db import models
class order_items(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_product_type = models.ForeignKey(product,on_delete=models.CASCADE) # 
	fk_order_id = models.ForeignKey(order,on_delete=models.CASCADE) # 
	fk_order_item_status_code = models.ForeignKey(g_order_status_codes,on_delete=models.CASCADE) # 
	quantity = models.IntegerField(blank=False) # 
	price = models.DecimalField(max_digits=500,decimal_places=2,blank=False) # 
	rma_number = models.IntegerField(blank=False) # 
	rma_issued_by = models.IntegerField(blank=False) # 
	rma_issued_date = models.DateTimeField(blank=False) # more to add

class order_itemsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.order_items
		fields="__all__"
class order_itemsView(viewsets.ModelViewSet):
	queryset=models.order_items.objects.all()
	serializer_class=srealizer.order_itemsSerliazer


# fk_product_type -> product 
# fk_order_id -> order 
# fk_order_item_status_code -> g_order_status_codes 
