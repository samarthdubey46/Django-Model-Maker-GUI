class g_product_subcategoryView(viewsets.ModelViewSet):
	queryset=models.g_product_subcategory.objects.all()
	serializer_class=serelizers.g_product_subcategorySerliazerclass
class g_payment_methodsView(viewsets.ModelViewSet):
	queryset=models.g_payment_methods.objects.all()
	serializer_class=serelizers.g_payment_methodsSerliazer


class sellerView(viewsets.ModelViewSet):
	queryset=models.seller.objects.all()
	serializer_class=serelizers.sellerSerliazer

class orderView(viewsets.ModelViewSet):
	queryset=models.order.objects.all()
	serializer_class=serelizers.orderSerliazer

class order_itemsView(viewsets.ModelViewSet):
	queryset=models.order_items.objects.all()
	serializer_class=serelizers.order_itemsSerliazer

class g_cityView(viewsets.ModelViewSet):
	queryset=models.g_city.objects.all()
	serializer_class=serelizers.g_citySerliazerclass
class addressView(viewsets.ModelViewSet):
	queryset=models.address.objects.all()
	serializer_class=serelizers.addressSerliazer

class product_photosView(viewsets.ModelViewSet):
	queryset=models.product_photos.objects.all()
	serializer_class=serelizers.product_photosSerliazer


class g_seller_categoryView(viewsets.ModelViewSet):
	queryset=models.g_seller_category.objects.all()
	serializer_class=serelizers.g_seller_categorySerliazer


class customer_paymentView(viewsets.ModelViewSet):
	queryset=models.customer_payment.objects.all()
	serializer_class=serelizers.customer_paymentSerliazer

class g_address_typeView(viewsets.ModelViewSet):
	queryset=models.g_address_type.objects.all()
	serializer_class=serelizers.g_address_typeSerliazer


class shipmentView(viewsets.ModelViewSet):
	queryset=models.shipment.objects.all()
	serializer_class=serelizers.shipmentSerliazer
 
class g_order_status_codesView(viewsets.ModelViewSet):
	queryset=models.g_order_status_codes.objects.all()
	serializer_class=serelizers.g_order_status_codesSerliazer


class g_product_varientView(viewsets.ModelViewSet):
	queryset=models.g_product_varient.objects.all()
	serializer_class=serelizers.g_product_varientSerliazer
class seller_reviewsView(viewsets.ModelViewSet):
	queryset=models.seller_reviews.objects.all()
	serializer_class=serelizers.seller_reviewsSerliazer

class zoneView(viewsets.ModelViewSet):
	queryset=models.Zone.objects.all()
	serializer_class=serelizers.ZoneSerliazerclass 
class shipment_itemsView(viewsets.ModelViewSet):
	queryset=models.shipment_items.objects.all()
	serializer_class=serelizers.shipment_itemsSerliazer
 
class customerView(viewsets.ModelViewSet):
	queryset=models.customer.objects.all()
	serializer_class=serelizers.customerSerliazer

class g_product_categoryView(viewsets.ModelViewSet):
	queryset=models.m_product_category.objects.all()
	serializer_class=serelizers.m_product_categorySerliazerclass 
class productView(viewsets.ModelViewSet):
	queryset=models.product.objects.all()
	serializer_class=serelizers.productSerliazer

class product_varient_valueView(viewsets.ModelViewSet):
	queryset=models.product_varient_value.objects.all()
	serializer_class=serelizers.product_varient_valueSerliazer


class seller_sub_categoryView(viewsets.ModelViewSet):
	queryset=models.seller_sub_category.objects.all()
	serializer_class=serelizers.seller_sub_categorySerliazer
class g_countryView(viewsets.ModelViewSet):
	queryset=models.g_country.objects.all()
	serializer_class=serelizers.g_countrySerliazerclass 
class image_customerView(viewsets.ModelViewSet):
	queryset=models.image_customer.objects.all()
	serializer_class=serelizers.image_customerSerliazer


class g_invoice_status_codeView(viewsets.ModelViewSet):
	queryset=models.g_invoice_status_code.objects.all()
	serializer_class=serelizers.g_invoice_status_codeSerliazer


class seller_photoView(viewsets.ModelViewSet):
	queryset=models.seller_photo.objects.all()
	serializer_class=serelizers.seller_photoSerliazer

class seller_question_answerView(viewsets.ModelViewSet):
	queryset=models.seller_question_answer.objects.all()
	serializer_class=serelizers.seller_question_answerSerliazer

class seller_highlightsView(viewsets.ModelViewSet):
	queryset=models.seller_highlights.objects.all()
	serializer_class=serelizers.seller_highlightsSerliazer


class invoiceView(viewsets.ModelViewSet):
	queryset=models.invoice.objects.all()
	serializer_class=serelizers.invoiceSerliazer

class g_stateView(viewsets.ModelViewSet):
	queryset=models.g_state.objects.all()
	serializer_class=serelizers.g_stateSerliazer