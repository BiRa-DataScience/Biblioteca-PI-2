from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class TermsView(TemplateView):
    template_name = 'terms.html'


class ArticleView(TemplateView):
    template_name = 'article.html'


class LoginView(TemplateView):
    template_name = 'login.html'