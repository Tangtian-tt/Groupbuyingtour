from django.urls import path
from . import views

urlpatterns = [
  path('abroadhome', views.abroadhome,name='abroadhome'),
  path('<int:abroad_id>', views.abroaddetail,name='abroaddetail'),
  path('<int:abroad_id>/createabroadreview',views.createabroadreview, name='createabroadreview'),
  path('review/<int:review_id>', views.updateabroadreview,name='updateabroadreview'),
  path('review/<int:review_id>/delete', views.deleteabroadreview, name='deleteabroadreview'),
]