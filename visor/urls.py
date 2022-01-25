from django.urls import path
#from django.conf.urls import handler404

from . import views

app_name = 'visor'
urlpatterns = [
    path('', views.ColegioListView.as_view(), name='index'),
    #path('<int:pk>/<slug:slug>', views.ColegioDetailView.as_view(), name='detalle_colegio'),
    path('<int:pk>/<slug:slug>', views.colegio_detail_view, name='detalle_colegio'),
    path('calendario/<letra>', views.CalendarioListView.as_view(), name='calendario'),
    #path('calendarioB', views.CalendarioBListView.as_view(), name='calendarioB'),
    path('contacto/', views.contacto, name='contacto'),
    path('recibido/', views.mensaje_recibido, name='mensaje_recibido'),
]

#handler404 = 'visor.views.handle_page_not_found'
