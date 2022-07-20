from django.contrib import admin
from django.urls import path,include 
from review import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('users/',include('user.urls')),
    path('reviews/', include('review.urls'))
]
