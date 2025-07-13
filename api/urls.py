from django.urls import path
from .views import WheelSpecCreateView, BogieChecksheetCreateView

urlpatterns = [
    path('forms/wheel-specifications', WheelSpecCreateView.as_view()),
    path('forms/bogie-checksheet', BogieChecksheetCreateView.as_view()),
    
]