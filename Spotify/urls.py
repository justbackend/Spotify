from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music.views import *
router = DefaultRouter()
router.register('qoshiqchilarv', QoshiqchilarViewSet)
router.register('albomview', AlbomViewset)
router.register('qoshiqview', QoshiqViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('albom/', AlbomApi.as_view()),
    path('qoshiq/', QoshiqApi.as_view()),
    path('qoshiqchi/', QoshiqchiApi.as_view()),
    path('qoshiqchi/<int:pk>/', QoshiqchiOneApi.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


