from django.db import models
from django.contrib.auth.models import User

class Abroad(models.Model) :
    title = models.CharField(max_length=100,verbose_name="国际团购旅游方案名")
    description = models.CharField(max_length=350,verbose_name="国际团购旅游方案介绍")
    price = models.CharField(max_length=100,verbose_name="团购价格")
    image =models.ImageField(upload_to='abroad/images/',verbose_name="团购旅游图片")
    url = models.URLField(blank=True,verbose_name="国际团购旅游资源链接")
    class Meta:
        verbose_name = "国际团购旅游"
        verbose_name_plural = "国际团购旅游"

    def __str__(self):
        return self.title
class Review(models.Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='abroad_review')
    abroad= models.ForeignKey(Abroad,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
      return self.text
