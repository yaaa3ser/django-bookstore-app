from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user management
    path("accounts/", include("allauth.urls")),
    # local apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns