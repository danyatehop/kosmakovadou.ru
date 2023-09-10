from django.contrib import admin
from django import forms
from .models import (Portfolio, Development, 
                     Article, Feedback, 
                     CommentArticle, CommentDevelop,
                     Section, Page)


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'


class DevelopAdminForm(forms.ModelForm):
    body = forms.CharField(label="Текст разработки", widget=CKEditorUploadingWidget())
    class Meta:
        model = Development
        fields = '__all__'


class SectionAdminForm(forms.ModelForm):
    text = forms.CharField(label="Содержимое раздела", widget=CKEditorUploadingWidget())
    class Meta:
        model = Development
        fields = '__all__'


class PageAdminForm(forms.ModelForm):
    text = forms.CharField(label="Содержимое страницы", widget=CKEditorUploadingWidget())
    class Meta:
        model = Development
        fields = '__all__'

admin.site.register(Portfolio)

@admin.register(Development)
class DevelopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'comment_count')
    form = DevelopAdminForm

    def comment_count(self, obj):
        result = CommentDevelop.objects.filter(develop_id=obj).count()
        return result
    
    comment_count.short_description="Количество комментариев"

@admin.register(Article)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'comment_count')
    form = ArticleAdminForm

    def comment_count(self, obj):
        result = CommentArticle.objects.filter(article_id=obj).count()
        return result
    
    comment_count.short_description="Количество комментариев"

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
    list_display = ('name', 'page_count')

    def page_count(self, obj):
        result = Page.objects.filter(section_id=obj).count()
        return result
    
    page_count.short_description="Количество привязанных страниц"

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display=('name', 'section')
    list_filter=(('section', admin.EmptyFieldListFilter),)
    empty_value_display = 'Без секции'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('body', 'surname', 'firstname', 'middlename', 'is_pub')
    list_filter=('is_pub',)

@admin.register(CommentArticle)
class CommentArticleAdmin(admin.ModelAdmin):
    list_display=('article', 'body', 'surname', 'firstname', 'middlename', 'is_pub') 
    list_filter = ('article', 'is_pub')

@admin.register(CommentDevelop)
class CommentDevelopAdmin(admin.ModelAdmin):
    list_display=('develop', 'body', 'surname', 'firstname', 'middlename', 'is_pub') 
    list_filter = ('develop', 'is_pub')

