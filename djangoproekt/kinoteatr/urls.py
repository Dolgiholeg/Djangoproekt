from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.start_page_view, name='start'),
    path('main/', views.main_page_view, name='main'),
    path('1/', views.fud_view, name='fud_view'),
    path('2/', views.today_view, name='today_view'),
    path('3/', views.multfilm_view, name='multfilm_view'),
    path('4/', views.film1_view, name='film1_view'),
    path('5/', views.film2_view, name='film2_view'),
    path('comments/', views.comment_view, name='comments'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
