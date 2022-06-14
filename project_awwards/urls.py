from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from awwards.views import ProjectView,ProfileView,UserView

router = routers.SimpleRouter()
router.register('project',ProjectView)
router.register('profile',ProfileView)
router.register('user',UserView)



urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('',include('awwards.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

