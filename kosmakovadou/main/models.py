from django.db import models
from django.utils import timezone
   

class Portfolio(models.Model):

    title = models.CharField("Заголовок", max_length=140)
    description = models.CharField("Описание", max_length=500)
    body = models.TextField("Основной текст", max_length=5000)
    portfolio_date = models.DateTimeField("Дата публикации", default=timezone.now)


class Development(models.Model):

    title = models.CharField("Заголовок", max_length=140)
    description = models.CharField("Описание", max_length=500)
    body = models.TextField("Основной текст", max_length=6000)
    develop_date = models.DateTimeField("Дата публикации", default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolut_url(self):
        return f"/develop/{self.id}"


class Article(models.Model):

    title = models.CharField("Заголовок", max_length=140)
    description = models.CharField("Описание", max_length=500)
    body = models.TextField("Основной текст", max_length=5000)
    article_date = models.DateTimeField("Дата публикации", default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return f"/article/{self.id}"


class Feedback(models.Model):

    surname = models.CharField("Фамилия", max_length=15)
    firstname = models.CharField("Имя", max_length=15)
    middlename = models.CharField("Отчество", max_length=15)
    email = models.EmailField("Адрес электронной почты", 
                              help_text="Не обязательное поле", 
                              blank=True)
    phone = models.CharField("Номер телефона", 
                             help_text="Не обязательное поле", 
                             max_length=18, 
                             blank=True)
    body = models.TextField("Ваш отзыв") 
    feedback_date = models.DateTimeField("Дата отправки отзыва", default=timezone.now)
    publish_date = models.DateTimeField("Дата публикации отзыва", default=timezone.now)
    is_pub = models.BooleanField("Опубликовать", default=False)
    
    def get_absolut_url(self):
        return f"/feedback/{self.id}"


class CommentArticle(models.Model):

    surname = models.CharField("Фамилия", max_length=15)
    firstname = models.CharField("Имя", max_length=15)
    middlename = models.CharField("Отчество", max_length=15)
    email = models.EmailField("Адрес электронной почты", 
                              help_text="Не обязательное поле", 
                              blank=True)
    phone = models.CharField("Номер телефона", 
                             help_text="Не обязательное поле", 
                             max_length=18, 
                             blank=True)
    body = models.TextField("Ваш комментарий") 
    feedback_date = models.DateTimeField("Дата отправки отзыва", default=timezone.now)
    publish_date = models.DateTimeField("Дата публикации отзыва", default=timezone.now)
    is_pub = models.BooleanField("Опубликовать", default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class CommentDevelop(models.Model):

    surname = models.CharField("Фамилия", max_length=15)
    firstname = models.CharField("Имя", max_length=15)
    middlename = models.CharField("Отчество", max_length=15)
    email = models.EmailField("Адрес электронной почты", 
                              help_text="Не обязательное поле", 
                              blank=True)
    phone = models.CharField("Номер телефона", 
                             help_text="Не обязательное поле", 
                             max_length=18, 
                             blank=True)
    body = models.TextField("Ваш комментарий") 
    feedback_date = models.DateTimeField("Дата отправки отзыва", default=timezone.now)
    publish_date = models.DateTimeField("Дата публикации отзыва", default=timezone.now)
    is_pub = models.BooleanField("Опубликовать", default=False)
    develop = models.ForeignKey(Development, on_delete=models.CASCADE)
    

class Section(models.Model):

    name = models.CharField("Заголовок раздела", max_length=70)
    text = models.TextField("Содержимое раздела", max_length=5000)

    def __str__(self):
        return self.name
    
    def get_absolut_url(self):
        return f"/section/{self.id}"


class Page(models.Model):

    name = models.CharField("Заголовок страницы", max_length=70)
    description = models.CharField("Краткое описание страницы", max_length=500)
    text = models.TextField("Содержимое страницы", max_length=5000)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolut_url(self):
        return f"/section/page/{self.id}"
