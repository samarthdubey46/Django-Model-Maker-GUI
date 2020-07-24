
from django.db import models
class m_city(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	city = models.CharField(max_length=500,blank=False) // 
	fk_city_id = models.ForeignKey(m_state,on_delete=models.CASCADE) // 
	pincode = models.CharField(max_length=500,blank=False) // 
