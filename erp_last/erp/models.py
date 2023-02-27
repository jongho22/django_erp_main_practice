from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 제품 관리 모델
class Product(models.Model) :
    제품코드 = models.CharField(max_length=20, primary_key=True)
    제품명 = models.CharField(max_length=30)
    포장단위 = models.CharField(max_length=30)
    제약사 = models.CharField(max_length=30)
    보험코드 = models.CharField(max_length=20)
    표준코드 = models.CharField(max_length=20)
    기준가 = models.IntegerField()
    급여 = models.IntegerField()
    구분 = models.CharField(max_length=20)
    성문코드 = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Product"

# COA 관리 모델
class COA (models.Model) :
    코드 = models.IntegerField(primary_key=True)
    계정명 = models.CharField(max_length=30, null=True)
    계정_대분류 =  models.CharField(max_length=20, null=True)
    계정_중분류 = models.CharField(max_length=20, null=True)
    계정_소분류 = models.CharField(max_length=20, null=True)
    재무제표 = models.CharField(max_length=20, null=True)
    비고 = models.TextField(null=True)
    
    class Meta:
        verbose_name_plural = "COA"

# 부서
class Department(models.Model) :
    부서이름 = models.CharField(primary_key=True,max_length=10)

# 재직자 엑셀 업로드
class IncumbentUpdate(models.Model) :
    #no = models.AutoField(db_column='no', primary_key=True)
    upfile = models.FileField(blank=True, null=True, upload_to="uploads")

# 재직자 모델
class Incumbent(models.Model) :
    사번 = models.IntegerField(primary_key=True)
    구분 = models.CharField(max_length=4)
    이름 = models.CharField(max_length=10)
    영문이름 = models.CharField(max_length=20)
    근무지 = models.CharField(max_length=5)
    부서 = models.ForeignKey("Department",related_name="부서",on_delete=models.SET_NULL,db_column="부서",null=True)
    팀 = models.CharField(max_length=5)
    직급 = models.CharField(max_length=5)
    직책 = models.CharField(max_length=5,null=True,blank=True)
    입사일 = models.DateField(null=True,blank=True)
    근속일 = models.IntegerField(blank=True)
    주민등록번호 = models.CharField(max_length=20,null=True,blank=True)
    생년월일 = models.DateField(null=True,blank=True)
    연락처 = models.CharField(max_length=20,null=True,blank=True)
    비상연락망 = models.CharField(max_length=20,null=True,blank=True)
    회사_이메일 = models.EmailField(null=True,blank=True)
    개인_이메일 = models.EmailField(null=True,blank=True)
    주소 = models.TextField(null=True,blank=True)
    최종학력 = models.CharField(max_length=10,null=True,blank=True)
    학위 = models.CharField(max_length=10,null=True,blank=True)
    학교 = models.CharField(max_length=10,null=True,blank=True)
    전공 = models.CharField(max_length=10,null=True,blank=True)
    학점 = models.CharField(max_length=20,null=True,blank=True)
    입사구분 = models.CharField(max_length=10,null=True,blank=True)
    경력사항1 = models.CharField(max_length=10,null=True,blank=True)
    경력사항2 = models.CharField(max_length=10,null=True,blank=True)
    경력사항3 = models.CharField(max_length=10,null=True,blank=True)
    경력사항4 = models.CharField(max_length=10,null=True,blank=True)
    경력사항5 = models.CharField(max_length=10,null=True,blank=True)
    자격사항1 = models.CharField(max_length=10,null=True,blank=True)
    자격사항2 = models.CharField(max_length=10,null=True,blank=True)
    자격사항3 = models.CharField(max_length=10,null=True,blank=True)
    자격사항4 = models.CharField(max_length=10,null=True,blank=True)
    자격사항5 = models.CharField(max_length=10,null=True,blank=True)
    어학사항1 = models.CharField(max_length=10,null=True,blank=True)
    어학사항2 = models.CharField(max_length=10,null=True,blank=True)
    어학사항3 = models.CharField(max_length=10,null=True,blank=True)
    어학사항4 = models.CharField(max_length=10,null=True,blank=True)
    어학사항5 = models.CharField(max_length=10,null=True,blank=True)

# 퇴직자 모델
class Retiree(models.Model) :
    사번 = models.IntegerField(primary_key=True)
    구분 = models.CharField(max_length=4)
    이름 = models.CharField(max_length=10)
    영문이름 = models.CharField(max_length=20)
    근무지 = models.CharField(max_length=5)
    부서 = models.CharField(max_length=10,null=True,blank=True)
    팀 = models.CharField(max_length=5)
    직급 = models.CharField(max_length=5)
    직책 = models.CharField(max_length=5,null=True,blank=True)
    입사일 = models.DateField(null=True,blank=True)
    근속일 = models.IntegerField(blank=True)
    주민등록번호 = models.CharField(max_length=20,null=True,blank=True)
    생년월일 = models.DateField(null=True,blank=True)
    연락처 = models.CharField(max_length=20,null=True,blank=True)
    비상연락망 = models.CharField(max_length=20,null=True,blank=True)
    회사_이메일 = models.EmailField(null=True,blank=True)
    개인_이메일 = models.EmailField(null=True,blank=True)
    주소 = models.TextField(null=True,blank=True)
    최종학력 = models.CharField(max_length=10,null=True,blank=True)
    학위 = models.CharField(max_length=10,null=True,blank=True)
    학교 = models.CharField(max_length=10,null=True,blank=True)
    전공 = models.CharField(max_length=10,null=True,blank=True)
    학점 = models.CharField(max_length=20,null=True,blank=True)
    입사구분 = models.CharField(max_length=10,null=True,blank=True)
    경력사항1 = models.CharField(max_length=10,null=True,blank=True)
    경력사항2 = models.CharField(max_length=10,null=True,blank=True)
    경력사항3 = models.CharField(max_length=10,null=True,blank=True)
    경력사항4 = models.CharField(max_length=10,null=True,blank=True)
    경력사항5 = models.CharField(max_length=10,null=True,blank=True)
    자격사항1 = models.CharField(max_length=10,null=True,blank=True)
    자격사항2 = models.CharField(max_length=10,null=True,blank=True)
    자격사항3 = models.CharField(max_length=10,null=True,blank=True)
    자격사항4 = models.CharField(max_length=10,null=True,blank=True)
    자격사항5 = models.CharField(max_length=10,null=True,blank=True)
    어학사항1 = models.CharField(max_length=10,null=True,blank=True)
    어학사항2 = models.CharField(max_length=10,null=True,blank=True)
    어학사항3 = models.CharField(max_length=10,null=True,blank=True)
    어학사항4 = models.CharField(max_length=10,null=True,blank=True)
    어학사항5 = models.CharField(max_length=10,null=True,blank=True)

# 유저 관리 
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

# 유저 모델
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
