from django.contrib import admin
from django.urls import path,include
from home.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Default home page
    path('users/', include('users.urls')),
    path('theses/', include('theses.urls')),
    path('grading/', include('grading.urls')),

]
