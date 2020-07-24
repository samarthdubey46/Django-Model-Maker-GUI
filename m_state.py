from django.db import models
class m_state(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	state = models.CharField(max_length=500,blank=False) // 
	fk_country_id = models.ForeignKey(m_country,on_delete=models.CASCADE) // 
