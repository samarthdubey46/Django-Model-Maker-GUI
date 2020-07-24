from django.db import models
class m_address_type(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	address_type_name = models.CharField(max_length=500,blank=False) // 
	desc = models.CharField(max_length=500,blank=False) // 
