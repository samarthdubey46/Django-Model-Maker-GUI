class g_product_subcategory(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_product_id = models.ForeignKey(product,on_delete=models.CASCADE) # Not Sure ForiegnKey_Name
	desc = models.CharField(max_length=500,blank=False) # 

class g_payment_methods(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	payment_method = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class seller(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 
	fk_seller_sub_category = models.ForeignKey(g_seller_sub_category,on_delete=models.CASCADE) # 
	fk_open_hours = models.ForeignKey(opening_hours,on_delete=models.CASCADE) # 
	rating = models.DecimalField(max_digits=500,decimal_places=2,blank=False) # 
	phone_number_1 = models.CharField(max_length=500,blank=False) # 
	phone_number_2 = models.CharField(max_length=500,blank=True) # 
	email = models.EmailField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=True) # 
	fk_seller_photos = models.ForeignKey(seller_photo,on_delete=models.CASCADE) # 

class order(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_payment = models.ForeignKey(customer_payment,on_delete=models.CASCADE) # 
	fk_order_status_code = models.ForeignKey(g_order_status_codes,on_delete=models.CASCADE) # 
	fk_address = models.ForeignKey(address,on_delete=models.CASCADE) # 

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

class g_city(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	city = models.CharField(max_length=500,blank=False) # 
	fk_state_id = models.ForeignKey(g_state,on_delete=models.CASCADE) # 

class address(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	line1 = models.CharField(max_length=500,blank=False) # 
	fk_address_type = models.ForeignKey(g_address_types,on_delete=models.CASCADE) # 
	line2 = models.CharField(max_length=500,blank=False) # 
	line3 = models.CharField(max_length=500,blank=False) # 
	zip = models.IntegerField(blank=False) # 
	fk_zone = models.ForeignKey(zone,on_delete=models.CASCADE) # 

class product_photos(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	image_1 = models.ImageField(blank=False) # 
	image_2 = models.ImageField(blank=True) # 
	image_3 = models.ImageField(blank=True) # 
	image_4 = models.ImageField(blank=True) # 
	image_5 = models.ImageField(blank=True) # 
	image_6 = models.ImageField(blank=True) # 
	image_7 = models.ImageField(blank=True) # 

class g_seller_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	product_type = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class customer_payment(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_payment_method = models.ForeignKey(g_payment_methods,on_delete=models.CASCADE) # 
	credit_card_number = models.IntegerField(blank=False) # 
	payment_method_detail = models.CharField(max_length=500,blank=False) # 

class g_address_type(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	type_name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class shipment(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_order_id = models.ForeignKey(order,on_delete=models.CASCADE) # 
	fk_invoice_number = models.ForeignKey(invoice,on_delete=models.CASCADE) # 
	shipment_tracking_number = models.IntegerField(blank=False) # 
	fk_delivery_man = models.ForeignKey(delivery_man,on_delete=models.CASCADE) # 
	fk_address = models.ForeignKey(address,on_delete=models.CASCADE) # 
	shipment_date = models.DateTimeField(blank=False) # 

class g_order_status_codes(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	order_status_desc = models.CharField(max_length=500,blank=False) # 
	order_status_code = models.IntegerField(blank=False) # 

class g_product_varient(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	varient_name = models.CharField(max_length=500,blank=False) # 
	varint_desc = models.CharField(max_length=500,blank=False) # 

class seller_reviews(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	Review = models.CharField(max_length=500,blank=False) # 
	rating = models.CharField(max_length=500,blank=False) # 
	isvalid = models.BooleanField(default=False,blank=False) # 
	likes = models.IntegerField(blank=False) # 

class zone(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_country_id = models.ForeignKey(g_country,on_delete=models.CASCADE) # 
	fk_state_id = models.ForeignKey(g_state,on_delete=models.CASCADE) # 
	fk_city_id = models.ForeignKey(g_city,on_delete=models.CASCADE) # 
	zone_name = models.CharField(max_length=500,blank=False) # 

class shipment_items(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_order_item_id = models.ForeignKey(order_items,on_delete=models.CASCADE) # 
	fk_shipment_id = models.ForeignKey(shipment,on_delete=models.CASCADE) # 

class customer(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	gender = models.CharField(max_length=500,blank=False) # 
	first_name = models.CharField(max_length=500,blank=False) # 
	middle_name = models.CharField(max_length=500,blank=True) # 
	last_name = models.CharField(max_length=500,blank=False) # 
	email_addess = models.EmailField(max_length=500,blank=True) # 
	phone_1 = models.IntegerField(blank=False) # 
	phone_2 = models.IntegerField(blank=False) # 
	zone_fk = models.ForeignKey(zone,on_delete=models.CASCADE) # 
	date_last_conntected = models.DateTimeField(blank=False) # 
	fk_image = models.ForeignKey(image_customer,on_delete=models.CASCADE) # 

class g_product_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	product_type = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 
	fk_product_sub_category = models.ForeignKey(g_product_subcategory,on_delete=models.CASCADE) # 

class product(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_price_descsion_factor = models.ForeignKey(g_price_descsion_factor,on_delete=models.CASCADE) # Not Sure
	fk_product_subcategory = models.ForeignKey(g_product_subcategory,on_delete=models.CASCADE) # 
	fk_product_category = models.ForeignKey(g_product_category,on_delete=models.CASCADE) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	fk_product_varient = models.ForeignKey(g_product_varient,on_delete=models.CASCADE) # 
	fk_currency = models.ForeignKey(g_currency,on_delete=models.CASCADE,blank=True) # 
	fk_photos = models.ForeignKey(product_photos,on_delete=models.CASCADE,blank=True) # 
	product_name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 
	price = models.CharField(max_length=500,blank=False) # 
	total_count = models.IntegerField(blank=False) # 
	percent_discount = models.DecimalField(max_digits=500,decimal_places=2,blank=True) # 

class product_varient_value(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	varient_value = models.CharField(max_length=500,blank=False) # 
	fk_varient_id = models.ForeignKey(g_product_varients,on_delete=models.CASCADE) # 

class seller_sub_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 
	desc = models.CharField(max_length=500,blank=False) # 

class g_country(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	name = models.CharField(max_length=500,blank=False) # 

class image_customer(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	profile_picture = models.ImageField(blank=False) # 
	is_valid = models.BooleanField(default=False,blank=False) # 
	uri = models.URLField(max_length=500,blank=False) # 

class g_invoice_status_code(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	invoice_status_code = models.IntegerField(blank=False) # 
	invoice_status_description = models.CharField(max_length=500,blank=False) # 

class seller_photo(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	photo_url = models.ImageField(blank=False) # 
	fk_photo_type = models.ForeignKey(photo_type,on_delete=models.CASCADE) # 
	isvalid = models.BooleanField(default=False,blank=False) # 

class seller_question_answer(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_customer_id = models.ForeignKey(customer,on_delete=models.CASCADE) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	question = models.CharField(max_length=500,blank=False) # 
	answer = models.CharField(max_length=500,blank=True) # 
	likes = models.IntegerField(blank=False) # 
	dislikes = models.IntegerField(blank=False) # 
	isvalid = models.BooleanField(default=False,blank=False) # 

class seller_highlights(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	fk_seller_id = models.ForeignKey(seller,on_delete=models.CASCADE) # 
	highlight_1 = models.ImageField(blank=False) # 
	highlight_2 = models.ImageField(blank=False) # 
	highlight_3 = models.ImageField(blank=False) # 
	highlight_3 = models.ImageField(blank=False) # 
	highlight_4 = models.ImageField(blank=False) # 
	highlight_6 = models.ImageField(blank=False) # 
	highlight_7 = models.ImageField(blank=False) # 
	highlight_8 = models.ImageField(blank=False) # 

class invoice(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) #
	fk_order_id = models.ForeignKey(order,on_delete=models.CASCADE) # 
	fk_invoice_status_code = models.ForeignKey(g_invoice_status_code,on_delete=models.CASCADE) # 
	invoice_details = models.CharField(max_length=500,blank=False) # 

class g_state(models.Model):
	is_active = models.BooleanField(default=False,blank=False) # 
	create_update_at = models.DateTimeField(blank=False) # 
	state = models.CharField(max_length=500,blank=False) # 
	fk_country_id = models.ForeignKey(g_country,on_delete=models.CASCADE) # globals

