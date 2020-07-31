from django.db import models
class customer_payment(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_payment_method = models.ForeignKey(g_payment_methods,on_delete=models.CASCADE) # 
	credit_card_number = models.IntegerField(blank=False) # 
	payment_method_detail = models.CharField(max_length=500,blank=False) # 

class customer_paymentSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.customer_payment
		fields="__all__"
class customer_paymentView(viewsets.ModelViewSet):
	queryset=models.customer_payment.objects.all()
	serializer_class=srealizer.customer_paymentSerliazer


# fk_customer_id -> customer 
# fk_payment_method -> g_payment_methods 
