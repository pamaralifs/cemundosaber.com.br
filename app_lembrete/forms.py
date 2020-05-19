# Módulo forms.py criado para implementar filtro na view ListView
from django import forms
from .models import Lembrete

class LembreteForm1Filtro(forms.Form):
    search = forms.CharField(label='Título', required=False, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id':'id_search'}))
    # O id css/html já é padrão id_nomecampo, mesmo se omitir
    # O input html será disabled, mas via javascript inline no template, será habilitado ou não
    class Meta:
        model = Lembrete
        fields = ['id','titulo','arquivo','visivel']

class LembreteFormCreateUpdate(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','columns':'10'}))
    
    class Meta:
        fields = ['id','titulo','conteudo','visivel']
        model = Lembrete
        #exclude = ['id']