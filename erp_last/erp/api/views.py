from ..models import Product, COA,User,Department,Incumbent,IncumbentUpdate
from .serializers import ProductSerializer,COA_Serializer,UserSerializer,Department_Serializer,Incumbent_Serializer,Incumbent_Upload_Serializer

from rest_framework import viewsets
from rest_framework import generics

from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django_filters.rest_framework import DjangoFilterBackend,FilterSet,CharFilter,NumberFilter,BooleanFilter
from rest_framework.filters import SearchFilter,OrderingFilter

from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework.viewsets import ReadOnlyModelViewSet

import pandas as pd

from ..models import Incumbent

import psycopg2
from sqlalchemy import create_engine

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

    # 모델에서 가져오기
    queryset = Incumbent.objects.all()
    serializer_class = Incumbent_Serializer
    
    # 필터
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['사번','구분','이름','영문이름','근무지','부서','팀','직급','직책','입사일','근속일','주민등록번호','생년월일','연락처','비상연락망','회사_이메일','개인_이메일','주소','최종학력','학위','학교','전공','학점','입사구분','경력사항1','경력사항2','경력사항3','경력사항4','경력사항5','자격사항1','자격사항2','자격사항3','자격사항4','자격사항5','어학사항1','어학사항2','어학사항3','어학사항4','어학사항5','퇴직여부']
    # 검색 (foreign key는 제거되야 함)
    search_fields = ['사번','구분','이름','영문이름','근무지','팀','직급','직책','입사일','근속일','주민등록번호','생년월일','연락처','비상연락망','회사_이메일','개인_이메일','주소','최종학력','학위','학교','전공','학점','입사구분','경력사항1','경력사항2','경력사항3','경력사항4','경력사항5','자격사항1','자격사항2','자격사항3','자격사항4','자격사항5','어학사항1','어학사항2','어학사항3','어학사항4','어학사항5','퇴직여부']
    # 정렬
    ordering_fields = ['사번','이름','영문이름']
    ordering = ['사번']

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

            file_name = str(request.data.get('upfile'))
            print(file_name)
            
            pd_data = pd.read_csv(f'./media/uploads/{file_name}',encoding="CP949")
            conn = psycopg2.connect(database="erp_database", user="postgres", password="1234", host="localhost", port="")
            #print(conn)
            cur = conn.cursor()
            #cur.execute("SELECT * FROM erp_incumbent;")
            #rows = cur.fetchall()
            #for row in rows:
            #    print(row)
            engine = create_engine('postgresql://erp_database:1234@localhost:/erp_database')
            pd_data('erp_incumbent', engine, if_exists='append', index=False)

            conn.close()

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

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer