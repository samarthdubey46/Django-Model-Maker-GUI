from django.db import models
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

class seller_question_answerSerliazer(serializers.ModelSerializer):
	class Meta:
		model=models.seller_question_answer
		fields="__all__"
class seller_question_answerView(viewsets.ModelViewSet):
	queryset=models.seller_question_answer.objects.all()
	serializer_class=srealizer.seller_question_answerSerliazer


# fk_customer_id -> customer 
# fk_seller_id -> seller 
