# Django main imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# Django Rest Framework imports
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
# My imports
from micros import views as micros_views
from users import views as user_views


router = routers.DefaultRouter()
router.register('maindesc', micros_views.MainfooddescSearchView)
router.register('adddesc', micros_views.AddfooddescSearchView)
router.register('weights', micros_views.FoodweightsSearchView)
router.register('portiondesc', micros_views.FoodportiondescSearchView)
router.register('nutvalabb', micros_views.FnddsnutvalAbbrevSearchView)
router.register('nutdesc', micros_views.NutdescSearchView)

router.register('users', user_views.UserViewSet)
router.register('groups', user_views.GroupViewSet)
router.register('profile', user_views.ProfileSearchView)
router.register('userweight', user_views.WeightSearchView)
router.register('meals', user_views.MealSearchView)
router.register('mealfoods', user_views.FoodSearchView)
router.register('crudmealfoods', user_views.FoodCRUDView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('users.urls')),
    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
