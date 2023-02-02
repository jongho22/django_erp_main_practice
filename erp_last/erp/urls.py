from django.urls import path,include
from .api.views import ProductViewset,COA_Viewset,UserCreate
from rest_framework.routers import DefaultRouter
from . import views


# COA,, Product API
router = DefaultRouter()
router.register('Product', ProductViewset, basename='Product')
router.register('COA', COA_Viewset, basename='COA')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/acounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/acounts/', include('dj_rest_auth.urls')),
    
    # Home
    path('',views.home),

    # Product
    path('product/',views.product),
    path('product/<str:pk>/',views.productDetail),

    # COA
    path('coa/',views.coa),
    path('coa/<int:pk>/',views.coaDetail),
    
    # 로그인
    path('login/',views.login),
    path('register/',views.register),
]
