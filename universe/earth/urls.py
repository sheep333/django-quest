from django.urls import path

from . import views

app_name = 'earth'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_human', views.HumanCreateView.as_view(), name='create_human'),
    path('humans', views.HumanListView.as_view(), name='humans'),
    path('human/<int:pk>', views.HumanDetailView.as_view(), name='detail_human'),
    path('edit_human/<int:pk>', views.HumanUpdateView.as_view(), name='update'),
    # path('', views.index_1, name='index'),
    # path('', views.Index2View.as_view(), name='index'),
    # path('', views.Index3View.as_view(), name='index'),
]
