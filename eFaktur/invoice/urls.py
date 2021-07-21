from django.urls import path
from .views import GetCommercialRelationship, VerifyCompany

urlpatterns = [
    path('verify/<str:company_name>/', VerifyCompany.as_view()),
    path('relationship/<str:first_company>/<str:second_company>',
         GetCommercialRelationship.as_view())
]
