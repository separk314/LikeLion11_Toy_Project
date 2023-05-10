from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    
    class Meta:
        abstract = True
        ordering = ['created_at']

class Visit(BaseModel):
    visit_id = models.AutoField(primary_key=True)
    writer = models.CharField(verbose_name="작성자", max_length=20)
    content = models.TextField(verbose_name="내용")