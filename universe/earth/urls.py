from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index_1, name='index'),
    # path('', views.Index2View.as_view(), name='index'),
    # path('', views.Index3View.as_view(), name='index'),
]
