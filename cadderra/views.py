from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'  # 홈 페이지 템플릿


