from django.urls import path

from channels import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'channels', views.TodoView, 'channels')

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('', views.HomePageView.as_view()),
#     path('links/', views.LinksPageView.as_view()),  # simple view
#     path('getcust/', views.Customers.getCust),      # simple view
#     path('apitest/', views.CalcTest),               # for REST API test
# ]
