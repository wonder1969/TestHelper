from django.shortcuts import render
from .models import group, question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf


#общий список групп вопросов
def list(request):
    groups = group.objects.filter().order_by('-id')
    return render(request, "list.html", {'groups': groups})


#список вопросов определенной группы
def answers(request, group_id = 1):
    questions = question.objects.filter(question_group=group_id).order_by('question_number')
    return render(request, "answer.html", {'questions': questions})


#список определенного вопроса
def question_id(request, question_id = 1):
    ques = question.objects.get(id=question_id)
    return render(request, "question_id.html", {'ques': ques})


def regist(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return HttpResponseRedirect("/")
        else:
            args['form']=newuser_form
    return render_to_response('logon.html',args)


def logout(request):
    auth.logout(request)
    return redirect("/")