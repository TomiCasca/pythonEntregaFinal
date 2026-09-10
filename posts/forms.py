from django import forms
from posts.models import Posteo

# v1
# class FormularioCrearPosteo(forms.Form):
#     titulo = forms.CharField(max_length=200)
#     autor = forms.CharField(max_length=50)
#     contenido = forms.CharField(widget=forms.Textarea)

# v2
# class FormularioCrearPosteo(forms.ModelForm):
    
#     class Meta():
#         model = Posteo
#         fields = "__all__"
#         # fields = ['titulo', 'autor', 'contenido']
        
# class FormularioEditarPosteo(forms.ModelForm):
    
#     class Meta():
#         model = Posteo
#         fields = "__all__"


# v3
class FormularioBasePosteo(forms.ModelForm):
    
    class Meta():
        model = Posteo
        fields = "__all__"
    
    
class FormularioCrearPosteo(FormularioBasePosteo): ...


class FormularioEditarPosteo(FormularioBasePosteo): ...