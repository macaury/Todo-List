from django import forms

from .models import Tarefas

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas

        fields = ('titulo','categoria','status','descricao')
    
    
    
class Novo_user(forms.ModelForm):
    nome = forms.CharField(max_length=40,label='Seu nome')
    sobrenome = forms.CharField(max_length=40,label="Sobrenome")
    genero = 'menino' # botar opçãoes | choices
    
    email = forms.EmailInput()
    telefone = forms.NumberInput()
    
    organizacao = '1234HPF'
    
    def validacao_campo(self):
        return 1

    def envio_codigo(self):
        # whatsapp | Email
        return 2       
    
    def validacao_organizacao(self):
        return 3
    