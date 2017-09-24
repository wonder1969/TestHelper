from django.db import models



class group(models.Model):
    group_name = models.TextField(verbose_name="Название группы вопросов")

    def __str__(self):
        return self.group_name


class question(models.Model):
    question_number = models.IntegerField(verbose_name="Номер вопрос")
    question_name = models.TextField(verbose_name="Вопрос")
    question_answer = models.TextField(verbose_name="Ответ на вопрос", blank=True, null=True)
    question_group = models.ForeignKey(group)

    def __str__(self):
        return self.question_name