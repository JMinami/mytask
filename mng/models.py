from django.db import models

# Create your models here.


CONDITION_CHOICEES = (
    (1, '未着手'),
    (2, '未完了'),
    (3, '完了')
)
class task(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    overview = models.CharField(max_length=100)
    condition = models.IntegerField(choices=CONDITION_CHOICEES,
                                    blank=True, null=True)
    add_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class progress(models.Model):
    task = models.ForeignKey(task, on_delete=models.CASCADE,blank=True, null=True)
    date = models.DateField()
    progress = models.IntegerField(default=0)
    content = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.task.name + " / " +self.date.strftime('%Y年%m月%d日')



