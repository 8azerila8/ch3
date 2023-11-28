from django.urls import path
from .views import HomePageView, AboutPageView, CategoryView,GameView

urlpatterns = [
    path("games/",GameView.as_view(), name= "games"),
    path("about/",AboutPageView.as_view(), name= "about"),
    path("",HomePageView.as_view(), name= "home" ),
    path("category/", CategoryView.as_view(), name= 'category'),
]