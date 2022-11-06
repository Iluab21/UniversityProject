from django.urls import path, include
from rest_framework import permissions
from .views import DirectionApiView, DisciplineApiView, StudyGroupApiView, StudentApiView, get_report, report_status
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="University Cervice API",
      default_version='v1',
      description="",
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)


urlpatterns = [
    path('api/v1/report/', get_report),
    path('api/v1/report-status/', report_status),
    path('api/v1/diretions/', DirectionApiView.as_view()),
    path('api/v1/diretions/<int:id>/', DirectionApiView.as_view()),
    path('api/v1/disciplines/', DisciplineApiView.as_view()),
    path('api/v1/disciplines/<int:id>/', DisciplineApiView.as_view()),
    path('api/v1/studygroups/', StudyGroupApiView.as_view()),
    path('api/v1/studygroups/<int:id>/', StudyGroupApiView.as_view()),
    path('api/v1/students/', StudentApiView.as_view()),
    path('api/v1/students/<int:id>/', StudentApiView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
