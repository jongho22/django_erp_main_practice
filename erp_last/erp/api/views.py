from ..models import Product, COA,User,Department,Incumbent
from .serializers import ProductSerializer,COA_Serializer,UserSerializer,Department_Serializer,Incumbent_Serializer

from rest_framework import viewsets
from rest_framework import generics

from rest_framework import permissions
# 인증 
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# 권한
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
# 유저 확인
#from ..permissions import IsOwenerOrReadOnly

# Create your views here.
class ProductViewset(viewsets.ModelViewSet) :
    
    # authentication 추가
    #authentication_classes = [BasicAuthentication,SessionAuthentication]
    
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class COA_Viewset(viewsets.ModelViewSet) :

    # authentication 추가
    #authentication_classes = [BasicAuthentication,SessionAuthentication]
    
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = COA.objects.all()
    serializer_class = COA_Serializer

class Department_Viewset(viewsets.ModelViewSet) :
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Department.objects.all()
    serializer_class = Department_Serializer

class Incumbent_Viewset(viewsets.ModelViewSet) :
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Incumbent.objects.all()
    serializer_class = Incumbent_Serializer

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer