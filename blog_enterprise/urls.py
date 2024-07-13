from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blog/<slug:slug>', BlogViews.blogs, name='blogs'),
    path('blogs/search/', BlogViews.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
