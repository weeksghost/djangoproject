from django.forms.models import BaseInlineFormSet


class OrderedFormSet(BaseInlineFormSet):
    def get_queryset(self):
        return super(OrderedFormSet, self).get_queryset().order_by('order')
