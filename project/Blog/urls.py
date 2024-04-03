from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from home import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.blogs),
    path('blog/<slug:slug>/', views.post, name='blogpost'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('search/', views.search_view, name='search'),
    path('add_blogs/', views.add_blogs, name='add_blogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)