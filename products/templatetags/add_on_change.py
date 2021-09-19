from django import template


register = template.Library()


@register.filter(name='add_on_change')
def add_on_change(field, value):
    return field.as_widget(
        attrs={
            "onchange": 'nvpopulatejson({})'.format(value),
            "data-nvid": 'nv{}'.format(value),
        }
    )
