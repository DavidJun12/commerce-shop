from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#from core.views import index, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #path('',index,name='index'),
    #path('contact/',contact, name='contact'),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
