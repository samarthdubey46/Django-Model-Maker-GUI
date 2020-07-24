from django.db import models
class m_zone(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	fk_state_id = models.ForeignKey(m_state,on_delete=models.CASCADE) // 
	fk_city_id = models.ForeignKey(m_city,on_delete=models.CASCADE) // 
	fk_country_id = models.ForeignKey(m_country,on_delete=models.CASCADE) // 
	zone_name = models.CharField(max_length=500,blank=False) // 
