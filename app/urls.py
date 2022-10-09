from django.urls import path
from django.conf.urls.static import static
from app.views import IndexListView, CompleteListView, LinkDeleteView, StartDownload
from django.conf import settings



urlpatterns = [
    path('', IndexListView.as_view(), name = 'search'),
    path('/completed', CompleteListView.as_view(), name = 'complete'),
    path('delete/<int:id>/', LinkDeleteView, name = 'link_delete'),
    path('start/<int:id>/', StartDownload, name = 'start'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)