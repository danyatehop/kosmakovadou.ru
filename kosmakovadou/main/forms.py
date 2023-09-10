from django import forms
from captcha.fields import CaptchaField

class Feedback_form(forms.Form):

    surname = forms.CharField(max_length=15, label="Фамилия")
    firstname = forms.CharField(max_length=15, label="Имя")
    middlename = forms.CharField(max_length=15, label="Отчество")
    email = forms.EmailField(help_text="- не обязательное поле", label="Адрес электронной почты", required=False)
    phone = forms.CharField(help_text="- не обязательное поле", max_length=18, label="Номер вашего телефона", 
                            widget=forms.TextInput(attrs={'placeholder': 'Номер без восьмёрки'}),
                            required=False)
    body = forms.CharField(widget=forms.Textarea, label="Ваш отзыв")
    captcha = CaptchaField(label="Введите ответ на математический пример")
    

class Comment_form(forms.Form):
    surname = forms.CharField(max_length=15, label="Фамилия")
    firstname = forms.CharField(max_length=15, label="Имя")
    middlename = forms.CharField(max_length=15, label="Отчество")
    email = forms.EmailField(help_text="- не обязательное поле", label="Адрес электронной почты", required=False)
    phone = forms.CharField(help_text="- не обязательное поле", max_length=18, label="Номер вашего телефона", 
                            widget=forms.TextInput(attrs={'placeholder': 'Номер без восьмёрки'}),
                            required=False)
    body = forms.CharField(widget=forms.Textarea, label="Ваш комментарий")
    captcha = CaptchaField(label="Введите ответ на математический пример")
