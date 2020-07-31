class g_product_subcategorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_product_subcategory
		fields="__all__"
class g_payment_methodsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_payment_methods
		fields="__all__"
class sellerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller
		fields="__all__"
class orderSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.order
		fields="__all__"
class order_itemsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.order_items
		fields="__all__"
class g_citySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_city
		fields="__all__"
class addressSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.address
		fields="__all__"
class product_photosSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product_photos
		fields="__all__"
class g_seller_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_seller_category
		fields="__all__"
class customer_paymentSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.customer_payment
		fields="__all__"
class g_address_typeSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_address_type
		fields="__all__"
class shipmentSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.shipment
		fields="__all__"
class g_order_status_codesSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_order_status_codes
		fields="__all__"
class g_product_varientSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_product_varient
		fields="__all__"
class seller_reviewsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_reviews
		fields="__all__"
class zoneSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.Zone
		fields="__all__"
class shipment_itemsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.shipment_items
		fields="__all__"
class customerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.customer
		fields="__all__"
class g_product_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.m_product_category
		fields="__all__"
class productSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product
		fields="__all__"
class product_varient_valueSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.product_varient_value
		fields="__all__"
class seller_sub_categorySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_sub_category
		fields="__all__"
class g_countrySerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_country
		fields="__all__"
class image_customerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.image_customer
		fields="__all__"
class g_invoice_status_codeSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_invoice_status_code
		fields="__all__"
class seller_photoSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_photo
		fields="__all__"
class seller_question_answerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_question_answer
		fields="__all__"
class seller_highlightsSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_highlights
		fields="__all__"
class invoiceSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.invoice
		fields="__all__"
class g_stateSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.g_state
		fields="__all__"
