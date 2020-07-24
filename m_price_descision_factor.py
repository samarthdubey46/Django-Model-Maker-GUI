from django.db import models
class m_price_descision_factor(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	price_descsion_factor = models.CharField(max_length=500,blank=False) // 
	desc = models.CharField(max_length=500,blank=False) // 
