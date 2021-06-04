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
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(ContatoPageView, self).form_valid(form)
