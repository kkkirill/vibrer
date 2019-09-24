from django.urls import include, path
from rest_framework import routers

from apps.media.routers import router as me_router
from apps.user import urls as user_urls
from apps.user.routers import router as us_router


class ApiRouter(routers.DefaultRouter):

    def extend(self, router):
        self.registry.extend(router.registry)


router = ApiRouter()
router.extend(me_router)
router.extend(us_router)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('auth/', include(user_urls)),
]
