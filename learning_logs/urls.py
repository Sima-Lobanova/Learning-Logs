from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    path('new_topic/', views.new_topic, name='new_topic'),

    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]