from django.urls import path
from .views import MealGet, MealGetList, MealOne

urlpatterns = [
    path('', MealGet.as_view()),
    path('<int:pk>', MealGet.as_view()),
    path('meals', MealGetList.as_view()),
    path('meals/<int:pk>', MealOne.as_view()),
]