from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.models import Plant
from .forms import PlantForm


def main(request):
    plants = Plant.objects.all()
    return TemplateResponse(request, 'core/list.html', context={'plants': plants})


class PlantCreateView(CreateView):
    model = Plant
    template_name = 'core/form.html'
    form_class = PlantForm
    success_url = reverse_lazy('core:list')
