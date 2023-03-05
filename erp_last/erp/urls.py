from django.urls import path,include
from .api.views import ProductViewset,COA_Viewset,UserCreate,Department_Viewset,Incumbent_Viewset,IncumbentUpdate_Viewset,IncumbentUpdate_Detail_Viewset
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls.static import static
from django.conf import settings


# COA,, Product API
router = DefaultRouter()
router.register('Product', ProductViewset, basename='Product')
router.register('COA', COA_Viewset, basename='COA')
router.register('Department',Department_Viewset,basename='Department')
router.register('Incumbent',Incumbent_Viewset,basename='Incumbent')
#router.register('IncumbentUpdate',IncumbentUpdate_Viewset, basename='IncumbentUpdate')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/acounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/acounts/', include('dj_rest_auth.urls')),
    
    path('api/IncumbentUpdate/', IncumbentUpdate_Viewset.as_view()),
    path('api/IncumbentUpdate/<int:pk>/', IncumbentUpdate_Detail_Viewset.as_view()),

    # Home
    path('',views.home),

    # Product
    path('product/',views.product),
    path('product/<str:pk>/',views.productDetail),

    # COA
    path('coa/',views.coa),
    path('coa/<int:pk>/',views.coaDetail),

    # 재직자
    path('incumbent/',views.incumbent),
    path('incumbent/<int:pk>/',views.incumbentDetail),
    path('incumbent_upload/',views.incumbent_upload),
    
    # 퇴직자
    path('retiree/',views.retiree),
    #path('retiree/<int:pk>/',views.retiree),

    # 로그인
    path('login/',views.login),
    path('register/',views.register),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
