from django.urls import path
from .views import *
urlpatterns = [
   path('resource-type/',ResourceTypeView.as_view({'get':'list','post':'create'})),
   path('resource-type/<int:pk>/',ResourceTypeView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
   path('department/',DepartmentView.as_view({'get':'list','post':'create'})),
   path('department/<int:pk>/',DepartmentView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
   # path('resource/',ResourceView.as_view({'get':'list','post':'create'})),
   # path('resource/<int:pk>/',ResourceView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

   path('resource/',ResourceView.as_view()),

   path('vendor/',VendorView.as_view({'get':'list','post':'create'})),
   path('vendor/<int:pk>/',VendorView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
   path('purchase/',PurchaseView.as_view({'get':'list','post':'create'})),
   path('purchase/<int:pk>/',PurchaseView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]
