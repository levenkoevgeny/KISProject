from django.urls import path
from . import views

app_name = 'kis'

urlpatterns = [
    path('', views.main, name='main'),
    path('cadet/list', views.cadet_list, name='cadet-list'),
    path('cadet/add', views.add_cadet, name='cadet-add'),
    path('cadet/<cadet_pk>/update', views.update_cadet, name='cadet-update'),
    # path('<game_id>/start', views.new_game_start_page, name='new-game-start-page'),
    # path('running', views.game_running, name='game-running'),
    # path('results', views.game_results, name='game-results'),
    # path('game-over', views.game_over, name='game-over'),
]