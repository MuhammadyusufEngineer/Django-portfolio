from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, upload_image

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/upload-image/', upload_image),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)