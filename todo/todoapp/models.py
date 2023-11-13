from django.db import models

class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=200)
    is_complete = models.BooleanField('Завершено', default=False)
    user = models.CharField('Имя', max_length=200)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title


