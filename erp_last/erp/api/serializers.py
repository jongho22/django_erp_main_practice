from ..models import Product, COA, User
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer) :
    #user = serializers.ReadOnlyField(source = 'user.nickname')
    
    class Meta :
        model = Product
        fields = ['제품코드','제품명','포장단위','제약사','보험코드','표준코드','기준가','급여','구분','성문코드']
    
class COA_Serializer(serializers.ModelSerializer) :
    #user = serializers.ReadOnlyField(source = 'user.nickname')

    class Meta :
        model = COA
        fields = ['코드','계정명','계정_대분류','계정_중분류','계정_소분류','계정_소분류','재무제표','비고']

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'email', 'name', 'password']