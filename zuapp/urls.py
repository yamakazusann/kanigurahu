from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.zentai,name='zentai'),
    path('paretozu_index/',views.paretozu_index,name="paretozu_index"),
    path('paretozu_edit/<int:num>',views.paretozu_edit,name="paretozu_edit"),

    path('oresen_index/',views.oresen_index,name="oresen_index"),
    path('oresen_edit/<int:num>',views.oresen_edit,name="oresen_edit"),

    path('bougurahu_index/',views.bougurahu_index,name="bougurahu_index"),
    path('bougurahu_edit/<int:num>',views.bougurahu_edit,name="bougurahu_edit"),

    path('engurahu_index/',views.engurahu_index,name="engurahu_index"),
    path('engurahu_edit/<int:num>',views.engurahu_edit,name="engurahu_edit"),








    path('plot/',views.get_svg_z,name='plot'),
    path('en/',views.get_svg_e,name='en'),
    path('bou/',views.get_svg_b,name='bou'),
    path('ore/',views.get_svg_o,name='ore'),
]