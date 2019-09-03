from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import SieradViewSet, UserLoginViewSet, UserRegisterViewSet, UserViewSet, KandangViewSet, LantaiViewSet,SieradViewSet_MI

router = routers.DefaultRouter()
router.register('DailyInput', SieradViewSet)
router.register('User', UserViewSet)
router.register('kandang', KandangViewSet)
router.register('lantai', LantaiViewSet)
router.register('MonthlyInput', SieradViewSet_MI)



urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserViewSet, name='user'),
    path('register/', UserRegisterViewSet.as_view(), name='register'),
    path('login/', UserLoginViewSet.as_view(), name='login'),
    # path('kandang/', KandangViewSet.as_view(), name='kandang'),
]
