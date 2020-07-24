from django.db import models
class m_product_sub_category(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	fk_product_id = models.ForeignKey(m_product_category,on_delete=models.CASCADE) // 
	product_sub_category = models.CharField(max_length=500,blank=False) // 
	desc = models.CharField(max_length=500,blank=False) // 
