from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CategoryView(TemplateView):
    template_name = "category.html"

class GameView(TemplateView):
    template_name = "games.html"

