from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        social_account = self.request.user.socialaccount_set.first()
        user_info = social_account.extra_data if social_account else {}
        provider = social_account.provider if social_account else None
        
        context['user_info'] = user_info
        context['provider'] = provider
        return context
    
class AboutPageView(TemplateView):
    template_name = "about.html"