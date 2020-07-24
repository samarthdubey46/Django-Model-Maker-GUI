from django.db import models
class m_country(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	country = models.CharField(max_length=500,blank=False) // 
