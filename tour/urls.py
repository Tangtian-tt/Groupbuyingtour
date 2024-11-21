from django.urls import path
from . import views

urlpatterns = [
  path('tourhome', views.tourhome,name='tourhome'),
  path('<int:tour_id>', views.tourdetail,name='tourdetail'),
  path('<int:tour_id>/createtourreview',views.createtourreview, name='createtourreview'),
  path('review/<int:review_id>', views.updatetourreview,name='updatetourreview'),
  path('review/<int:review_id>/delete', views.deletetourreview, name='deletetourreview'),
]