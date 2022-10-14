from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index),
    path('grid',views.bGrid),
    path('bootstrap',views.bbootstrap) ,
    path('new',views.new) ,
    path('baabtra',views.baabtra)

]

 