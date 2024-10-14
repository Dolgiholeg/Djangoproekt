from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Main_page.as_view()),
    path('1/', views.fud_view, name='fud_view'),
    path('2/', views.fud_page_view, name='fud_page_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
