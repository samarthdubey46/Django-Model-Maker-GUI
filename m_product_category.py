
class m_product_category(models.Model):
	is_active = models.BooleanField(blank=False) // 	
	create_update_at = models.CharField(max_length=500 ,blank=False) // 	
	product_type = models.CharField(max_length=500 ,blank=False) // 	
	description = models.CharField(max_length=500 ,blank=True) // 	
	desc = models.CharField(max_length=500 ,blank=False) // 	
