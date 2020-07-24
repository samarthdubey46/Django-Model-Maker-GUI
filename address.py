from django.db import models
class address(models.Model):
	is_active = models.BooleanField(default=False,blank=False) // 
	create_update_at = models.DateTimeField(blank=False) // 
	fk_zone = models.ForeignKey(m_zone,on_delete=models.CASCADE) // 
	fk_address_type = models.ForeignKey(m_address_type,on_delete=models.CASCADE) // 
	line1 = models.CharField(max_length=500,blank=False) // 
	line2 = models.CharField(max_length=500,blank=False) // 
	line3 = models.CharField(max_length=500,blank=False) // 
