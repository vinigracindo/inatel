from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
         redirect_authenticated_user=True),
         name='login'),
    path('core/', include('core.urls', namespace='core')),
    path('weather/', include('weather.urls', namespace='weather')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('admin/', admin.site.urls),
]

# Serving static and media files for development enviroment
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
