from decouple import config
from django import forms
from django.core.mail.message import EmailMessage
from datetime import datetime


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=10)
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'{nome} - {email}\nEntrou em contato em: {data}\n\nAssunto:\n{assunto}\n\nMensagem:\n{mensagem}'

        mail = EmailMessage(
            subject='Contato feito pelo site',
            body=conteudo,
            from_email=config('DEFAULT_FROM_EMAIL'),
            to=[config('TO_EMAIL'), ],
            headers={
                'Reply-To': email
            }
        )
        mail.send()
