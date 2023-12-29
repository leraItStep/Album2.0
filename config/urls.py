
from django.contrib import admin
from django.urls import path, include

from catalog import views as catalog_views
from profiles import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_views.index, name='home'),
    path('catalog/', include('catalog.urls')),
    path('profile/', include('profiles.urls')),
    path('login/', profile_views.login_user, name='login'),
    path('logout/', profile_views.logout_user, name='logout'),
    path('register/', profile_views.register_user, name='register'),
    path('search/', catalog_views.search_result, name='search_result'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#handler404 = catalog_views.pageNotFound