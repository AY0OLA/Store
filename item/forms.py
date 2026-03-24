from django import forms
from .models import Items


INPUT_CLASSESS =  'w-full px-4 py-2 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('Category','name', 'description','price','image')

        widgets = {
            'Category': forms.Select(attrs={
                'class': INPUT_CLASSESS
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': INPUT_CLASSESS
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Item Description',
                'class': INPUT_CLASSESS
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Item Price',
                'class': INPUT_CLASSESS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSESS
            }),
        }
