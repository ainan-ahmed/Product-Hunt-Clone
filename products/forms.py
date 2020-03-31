from django import forms
from .models import Product,Category
class ProductCreateForm(forms.ModelForm):
    category  = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Product
        fields = {'title','image','icon','body','category'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'input--style-5'}),
            'body':forms.Textarea(attrs={'class':'input--style-5','col':40,'row':20})
        }
        

    