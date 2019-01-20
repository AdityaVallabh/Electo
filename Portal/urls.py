from django.urls import path
from .views import vote_view, thanks_view

urlpatterns = [
    path('elections/', vote_view, name='elections'),
    path('thanks/', thanks_view, name='thanks'),
]
