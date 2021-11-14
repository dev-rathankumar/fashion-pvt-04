from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Blog, Comment


class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'description')


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'blog_body')


class CommentTranslationOptions(TranslationOptions):
    fields = ('comment_body',)



translator.register(Blog, BlogTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Comment, CommentTranslationOptions)