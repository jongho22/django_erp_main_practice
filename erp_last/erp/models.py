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
