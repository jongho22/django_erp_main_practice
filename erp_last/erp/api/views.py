from ..models import Product, COA,User,Department,Incumbent,IncumbentUpdate,Retiree
from .serializers import ProductSerializer,COA_Serializer,UserSerializer,Department_Serializer,Incumbent_Serializer,Incumbent_Upload_Serializer,Retiree_Serializer

from rest_framework import viewsets
from rest_framework import generics

from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 인증 
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# 권한
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
# 유저 확인
#from ..permissions import IsOwenerOrReadOnly

# Create your views here.

# 제품
class ProductViewset(viewsets.ModelViewSet) :
    
    # authentication 추가
    #authentication_classes = [BasicAuthentication,SessionAuthentication]
    
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# COA 
class COA_Viewset(viewsets.ModelViewSet) :

    # authentication 추가
    #authentication_classes = [BasicAuthentication,SessionAuthentication]
    
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = COA.objects.all()
    serializer_class = COA_Serializer

# 부서
class Department_Viewset(viewsets.ModelViewSet) :
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Department.objects.all()
    serializer_class = Department_Serializer


# 재직자
class Incumbent_Viewset(viewsets.ModelViewSet) :
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Incumbent.objects.all()
    serializer_class = Incumbent_Serializer


# 재직자 엑셀 파일을 통한 DB에 입력 구현
class IncumbentUpdate_Viewset(APIView):

    # # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        snippets =IncumbentUpdate.objects.all()
        serializer = Incumbent_Upload_Serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Incumbent_Upload_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("파일을 변환 합니다.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 재직자 업로드 엑셀 파일 디테일 페이지
class IncumbentUpdate_Detail_Viewset(APIView):
    def get_object(self, pk):
        try:
            return IncumbentUpdate.objects.get(pk=pk)
        except IncumbentUpdate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Incumbent_Upload_Serializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Incumbent_Upload_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 퇴직자 
class Retiree_Viewset(viewsets.ModelViewSet):
    # permission 추가
    permission_classes = [permissions.IsAuthenticated]

    queryset = Retiree.objects.all()
    serializer_class = Retiree_Serializer

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer