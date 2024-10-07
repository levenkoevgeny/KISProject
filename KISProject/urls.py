from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from kis import views as kis_views


router = routers.DefaultRouter()

router.register(r'cadet', kis_views.CadetViewSet)
router.register(r'group', kis_views.GroupViewSet)
router.register(r'rank', kis_views.RankViewSet)
router.register(r'rank-history', kis_views.RankHistoryViewSet)
router.register(r'encouragement-kind', kis_views.EncouragementKindViewSet)
router.register(r'encouragement', kis_views.EncouragementViewSet)
router.register(r'punishment-kind', kis_views.PunishmentKindViewSet)
router.register(r'punishment', kis_views.PunishmentViewSet)
router.register(r'speciality', kis_views.SpecialityViewSet)
router.register(r'subdivision', kis_views.SubdivisionViewSet)


urlpatterns = [
    path('', RedirectView.as_view(url='/api/')),
    path('api/', include(router.urls)),
    # path('', RedirectView.as_view(url="/kis/")),
    path('admin/', admin.site.urls),
    path('kis/', include('kis.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
