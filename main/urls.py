from django.urls import path
from .views import HomeView, CreateSavingView, DetailSavingView, UpdateSavingVIew, DeleteSavingView
from . import services
app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('create/',CreateSavingView.as_view(), name='create' ),
    path('detail/<slug:slug>', DetailSavingView.as_view(), name='detail_saving'),
    path('update/<slug:slug>', UpdateSavingVIew.as_view(), name='update'),
    path('detail/<slug:slug>/download-xlsx', services.convert_saving_log_to_excel, name='export_to_excel' ),
    path('delete/<slug:slug>',DeleteSavingView.as_view(), name='delete' )
    
]
