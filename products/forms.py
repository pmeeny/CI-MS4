from django import forms
from django.forms import Textarea
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    """
    Represents a form for product rating and comments
    """
    class Meta:
        """
        Fields and types for product rating and comments form.
        """
        model = Review
        fields = (
            'product_rating',
            'review_text',
        )

        widgets = {
            'product_rating': forms.Select(attrs={'id': 'product_rating'}),
            'review_text': Textarea(attrs={'rows': 3}),
        }
