from django.urls import path
from . import views 

urlpatternsbook = [ 
    path('book/', views.review_book),
]