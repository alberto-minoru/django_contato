import json
import urllib
from decouple import config
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContatoForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContatoPageView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def form_valid(self, form):

        # Início da validação do reCAPTCHA
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': config('GOOGLE_RECAPTCHA_SECRET_KEY'),
            'response': recaptcha_response,
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        # Fim da validação do reCAPTCHA

        if result['success']:
            form.send_mail()
            messages.success(self.request, 'E-mail enviado com sucesso!')
            return super(ContatoPageView, self).form_valid(form)
        else:
            messages.error(self.request, 'Captcha inválido. Por favor tente novamente.')
            return super(ContatoPageView, self).form_invalid(form)
