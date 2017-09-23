from django.shortcuts import render
from .models import group, question


#общий список групп вопросов
def list(request):
    groups = group.objects.filter()
    return render(request, "list.html", {'groups': groups})


#список вопросов определенной группы
def answers(request):
    questions = question.objects.filter()
    return render(request, "answer.html", {'questions': questions})


#список определенного вопроса
def question_id(request, question_id = 1):
    ques = question.objects.get(id=question_id)
    return render(request, "question_id.html", {'ques': ques})