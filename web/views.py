from django.views.generic import FormView

from .forms import PDFUploadForm, SaltForm
from .salt import Salt


class IndexView(FormView):
    template_name = 'web/index.html'
    form_class = PDFUploadForm


class SaltView(FormView):
    template_name = 'web/salt.html'
    form_class = SaltForm
    data = None

    def form_valid(self, form):
        salt = Salt(
            salt_key=form.cleaned_data['salt_key'],
            salt_index=form.cleaned_data['salt_index'],
        )

        if self.request.POST.get('action') == 'en':
            self.data = salt.encode(form.cleaned_data['payload'])
        else:
            self.data = salt.decode(form.cleaned_data['payload'])

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data
        return context