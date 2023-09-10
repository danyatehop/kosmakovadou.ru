from datetime import datetime

from email.mime.text import MIMEText

from django.shortcuts import render
from .forms import Comment_form, Feedback_form
from .models import (Article, CommentArticle, 
                     CommentDevelop, Development,
                     Feedback, Portfolio,
                     Section, Page)

import os
import smtplib


# Create your views here.
def index(request):
    context = render_map()
    return render(request, "index.html", context)

def render_map():
    try:
        section_map = Section.objects.all()
        page_map = Page.objects.all()
        
        context = {
            'section_map': section_map,
            'page_map': page_map
            }

    except:
        context=None
    
    return context

def section(request, section_id):
    
    try:
        section_list = Section.objects.get(id=section_id)
        page_list = Page.objects.filter(section_id=section_id)
        context = render_map()
        context['section_list'] = section_list
        context['page_list'] = page_list
    except:
        context = None
    return render(request, 'section.html', context)

def page(request, page_id):
    try:
        page_details = Page.objects.get(id=page_id)
        context = render_map()
        context['page_details'] = page_details
    except:
        context = None
    return render(request, "page.html", context)


def portfolio(request):
    try:
        portfolio_list = Portfolio.objects.order_by("-portfolio_date")
        context = render_map()
        context['portfolio_list'] = portfolio_list
    except:
        context = None
    return render(request, "portfolio.html", context)


def developments(request):
    try:
        develop_list = Development.objects.order_by("-develop_date")
        context = render_map()
        context['develop_list'] = develop_list
    except:
        context = None
    return render(request, "developments.html", context)


def news(request):
    
    try:
        article_list = Article.objects.order_by("-article_date")
        context = render_map()
        context['article_list'] = article_list
    except:
        context = None
    return render(request, "news.html", context)


def page_arlicle(request, article_id):

    user_form = Comment_form()
    send = False
    error = False

    if request.method == "POST":

        user_form = Comment_form(request.POST)

        if user_form.is_valid():

            passwd = os.environ.get("PWD")

            smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru:465')

            smtpObj.login('kir.donetz@yandex.ru',passwd)

            title_article = Article.objects.get(id=article_id).title

            mail_text = (f'Новость: {title_article}\n'
                        f'Имя: {request.POST.get("surname")}\n'
                        f'Фамилия: {request.POST.get("firstname")}\n'
                        f'Отчество: {request.POST.get("middlename")}\n'
                        f'Почтовый адрес: {request.POST.get("email")}\n'
                        f'Номер телефона: {request.POST.get("phone")}\n'
                        f'Текст коментария: {request.POST.get("body")}\n'
                        f'Дата отправки отзыва: {datetime.now()}')
            
            msg = MIMEText(mail_text)
            msg['subject'] = "Новый комментарий на сайте 'kosmakovadou.ru'"

            smtpObj.sendmail("kir.donetz@yandex.ru","kir.donetz@yandex.ru", str(msg))

            CommentArticle.objects.create(
                surname=request.POST.get("surname"), 
                firstname=request.POST.get("firstname"),
                middlename=request.POST.get("middlename"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                body=request.POST.get("body"),
                feedback_date=datetime.now(),
                article_id=article_id
                )
            send = True
        else:
            send = False
            error = True

    page_details = Article.objects.get(id = article_id)


    user_form = Comment_form()    
    comment_list = (CommentArticle.objects.filter(article = article_id) & 
                    CommentArticle.objects.filter(is_pub = True)).order_by("-publish_date")
    
    context = render_map()
    context['error'] = error
    context['form'] = user_form
    context['page_details'] = page_details
    context['comment_list'] = comment_list
    context['send'] = send

    return render(request, "page_article.html", context)


def page_develop(request, develop_id):

    user_form = Comment_form()
    send = False
    error = False

    if request.method == "POST":

        user_form = Comment_form(request.POST)

        if user_form.is_valid():

            passwd = os.environ.get("PWD")

            smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru:465')

            smtpObj.login('kir.donetz@yandex.ru', passwd)

            title_develop = Development.objects.get(id=develop_id).title

            mail_text = (f'Разработка: {title_develop}\n'
                        f'Имя: {request.POST.get("surname")}\n'
                        f'Фамилия: {request.POST.get("firstname")}\n'
                        f'Отчество: {request.POST.get("middlename")}\n'
                        f'Почтовый адрес: {request.POST.get("email")}\n'
                        f'Номер телефона: {request.POST.get("phone")}\n'
                        f'Текст коментария: {request.POST.get("body")}\n'
                        f'Дата отправки отзыва: {datetime.now()}')
            
            msg = MIMEText(mail_text)
            msg['subject'] = "Новый комментарий на сайте 'kosmakovadou.ru'"

            smtpObj.sendmail("kir.donetz@yandex.ru","kir.donetz@yandex.ru", str(msg))

            CommentDevelop.objects.create(
                surname=request.POST.get("surname"), 
                firstname=request.POST.get("firstname"),
                middlename=request.POST.get("middlename"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                body=request.POST.get("body"),
                feedback_date=datetime.now(),
                develop_id=develop_id
                )
            send = True
        else:
            send = False
            error = True

    user_form = Comment_form()

    page_details = Development.objects.get(id = develop_id)
  
    comment_list = (CommentDevelop.objects.filter(develop = develop_id) & 
                    CommentDevelop.objects.filter(is_pub = True)).order_by("-publish_date")
    
    context = render_map()
    context['error'] = error
    context['form'] = user_form
    context['page_details'] = page_details
    context['comment_list'] = comment_list
    context['send'] = send
    return render(request, "page_develop.html", context) 


def feedback(request):

    userform = Feedback_form()
    send = False
    error = False

    if request.method == "POST":

        userform = Feedback_form(request.POST)

        if userform.is_valid():
            
            passwd = os.environ.get("PWD")

            smtpObj = smtplib.SMTP_SSL('smtp.yandex.ru:465')

            smtpObj.login('kir.donetz@yandex.ru', passwd)

            mail_text = (f'Имя: {request.POST.get("surname")}\n'
                        f'Фамилия: {request.POST.get("firstname")}\n'
                        f'Отчество: {request.POST.get("middlename")}\n'
                        f'Почтовый адрес: {request.POST.get("email")}\n'
                        f'Номер телефона: {request.POST.get("phone")}\n'
                        f'Текст отзыва: {request.POST.get("body")}\n'
                        f'Дата отправки отзыва: {datetime.now()}')
            
            msg = MIMEText(mail_text)

            msg['subject'] = "Новый отзыв на сайте 'kosmakovadou.ru'"

            Feedback.objects.create(
                surname=request.POST.get("surname"), 
                firstname=request.POST.get("firstname"),
                middlename=request.POST.get("middlename"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                body=request.POST.get("body"),
                feedback_date=datetime.now()
                )

            smtpObj.sendmail("kir.donetz@yandex.ru","kir.donetz@yandex.ru", str(msg))
            send = True
            context = { "send": send }

        else:
            error = True

    else:
        send = False

    try:
        feedback_list = Feedback.objects.filter(is_pub = True).order_by("-publish_date")
    except:
        feedback_list = False

    userform = Feedback_form()

    context = render_map()
    context['error'] = error
    context['form'] = userform
    context['send'] = send
    context['feedback_list'] = feedback_list

    return render(request, "feedback.html", context)

    