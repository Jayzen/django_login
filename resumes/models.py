from django.db import models


# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    content = models.TextField(default="content", verbose_name="内容")

    class Meta:
        verbose_name = "简历"
        verbose_name_plural = "简历列表"

    def __str__(self):
        return self.name


