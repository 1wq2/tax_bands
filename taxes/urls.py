from django.urls import include, path
from .import views
from .views import TaxView
app_name = 'taxes'

urlpatterns = [
    path('', TaxView.as_view()),
    # path('', views.TaxesView.as_view(), name='index'),
    # path('upload/', views.upload_file, name='upload'),
    # path('url/', views.get_url_data, name='url'),
    # path('cloud/', views.get_cloud_data, name='cloud'),
    # path('db/', views.get_db_data, name='db'),
    # path('db_calc/', views.handle_db_data, name='db_calc'),
    #path('results/', views.get_results, name='results'),
]
