from django.urls import path
from .views import NewsList, Search  # импортируем наше представление

urlpatterns = [
    # Path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    path('search', Search.as_view()),
    path('', Search.as_view())
]
