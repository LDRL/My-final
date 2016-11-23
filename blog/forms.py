from django import forms
from .models import Compra, Producto, Persona, Marca,CD

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ('cantidad', 'fecha_compra', 'persona','productos')

    def __init__ (self, *args, **kwargs):
    	super(PeliculaForm, self).__init__(*args, **kwargs)
    	self.fields["productos"].widget = forms.widgets.CheckboxSelectMultiple()
    	self.fields["productos"].queryset = Producto.objects.all()
