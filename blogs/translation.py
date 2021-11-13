from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'blog_body', 'author')

translator.register(Blog, BlogTranslationOptions)