##Adaptation of code to django 2.0:
# "from django.conf.urls import include , url" replaced by "from django.urls import path"
# "url(r'^" replaced by "path('"

from django.urls import path
from django.conf import settings

from . import views
from django.conf.urls.static import static
from .views import pIDWebView,FileDeleteView
#,FileListView

urlpatterns = [
     path('', views.index, name='index'),
     #path('pIDWeb', views.pIDWeb, name='pIDWeb'),
     path('pIDWeb',pIDWebView.as_view(),name="run-job"),
     path('delete/<int:pk>', FileDeleteView.as_view(), name='upload-delete'),
     #path('view', FileListView.as_view(), name='upload-view'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
