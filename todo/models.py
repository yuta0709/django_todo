from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='タスク名', max_length=255, blank=False, null=False)
    is_done = models.BooleanField(verbose_name='完了', default=False)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now=True)

    def __str__(self):
        if self.is_done:
            is_done = '✔'
        else:
            is_done = '✖'
        return '{} : {}'.format(is_done, self.title)
