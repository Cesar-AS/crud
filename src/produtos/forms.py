from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):


    class Meta:
        model = Produto
        fields = ['descricao', 'categoria', 'preco', 'quantidade']
        widgets = {
            'descricao': forms.TextInput(attrs={'class':'input', 'placeholder':'descricao'}),
            'categoria': forms.TextInput(attrs={'class':'input', 'placeholder':'categoria'}),
            'preco': forms.TextInput(attrs={'class':'input', 'placeholder':'preco'}),
            'quantidade': forms.TextInput(attrs={'class':'input', 'placeholder':'quantidade'})
        }
