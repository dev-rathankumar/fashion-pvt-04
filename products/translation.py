from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import AttributeValue, Color, Product, ProductAttribute, ReviewRating, SalesPopup, Category, Size, Testimonial, Variants


class SalesPopupTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'location')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'description')


class SizeTranslationOptions(TranslationOptions):
    fields = ('name',)


class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductAttributeTranslationOptions(TranslationOptions):
    fields = ('attribute_name',)


class AttributeValueTranslationOptions(TranslationOptions):
    fields = ('attribute_value',)


class VariantsTranslationOptions(TranslationOptions):
    fields = ('title',)


class ReviewRatingTranslationOptions(TranslationOptions):
    fields = ('subject', 'review')


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('testimonial',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description', 'full_specification')


translator.register(SalesPopup, SalesPopupTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Size, SizeTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(ProductAttribute, ProductAttributeTranslationOptions)
translator.register(AttributeValue, AttributeValueTranslationOptions)
translator.register(Variants, VariantsTranslationOptions)
translator.register(ReviewRating, ReviewRatingTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Product, ProductTranslationOptions)