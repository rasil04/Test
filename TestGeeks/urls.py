from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from TestGeeks import settings
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.TaskListAPIView.as_view()),
    path('api/tasks/<int:id>/', views.TaskDetailAPIView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
