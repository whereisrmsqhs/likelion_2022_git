from django.contrib import admin
from django.urls import path
from studyapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('modelform', views.modelform, name='modelform'),

    path('detail/<int:post_id>', views.detail, name='detail'),

    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)