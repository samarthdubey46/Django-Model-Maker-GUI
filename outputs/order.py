from django.db import models
class order(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_payment = models.ForeignKey(customer_payment,on_delete=models.CASCADE) # 
	fk_order_status_code = models.ForeignKey(g_order_status_codes,on_delete=models.CASCADE) # 
	fk_address = models.ForeignKey(address,on_delete=models.CASCADE) # 

class orderSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.order
		fields="__all__"
class orderView(viewsets.ModelViewSet):
	queryset=models.order.objects.all()
	serializer_class=srealizer.orderSerliazer


# fk_customer_id -> customer 
# fk_payment -> customer_payment 
# fk_order_status_code -> g_order_status_codes 
# fk_address -> address 
