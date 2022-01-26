from django.views.generic import TemplateView
from .models import CompanyInfo

class HomeView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = CompanyInfo.objects.all().first()
        return context
    
