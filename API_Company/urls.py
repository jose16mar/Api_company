from django.urls import path
from .views import companyListView, companyListName

urlpatterns = [

    path('company/', companyListView.as_view(), name="company_list"),
    path('company/<int:id>', companyListView.as_view(), name="company"),
    path('company/name/<str:name>', companyListName.as_view(), name="busqueda_name")
]