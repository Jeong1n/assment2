from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import product
from datetime import datetime
from permission import IsAdminOrIsAuthenticatedReadOnly
from .serializers import ProductSerializer
# Create your views here.
# sample request.data
class productView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get(self, request):
        today = datetime.now()
        products = product.objects.filter(
            Q(start_date__lte=today, end_date__gte=today, is_activate=True) |
            Q(user=request.user)
            )
        return Response(ProductSerializer(products, many=True).data,status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        request.data['user'] = request.user.id
        # title = request.data.get('title', '')
        # image = request.data.get('image', '')
        # Contents = request.data.get('Contents', '')
        if user.is_anonymous:
            return Response({"error": "로그인 후 이용해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        
        # 기본적인 사용 방법은 validator, creater와 다르지 않다.
        # update를 해줄 경우 obj, data(수정할 dict)를 입력한다.
        # partial=True로 설정해 주면 일부 필드만 입력해도 에러가 발생하지 않는다.
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            product_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, obj_id):
        Product = product.objects.get(id=obj_id)
        
        # title = request.data.get('title', '')
        # image = request.data.get('image', '')
        # Contents = request.data.get('Contents', '')
      
          
        # 기본적인 사용 방법은 validator, creater와 다르지 않다.
        # update를 해줄 경우 obj, data(수정할 dict)를 입력한다.
        # partial=True로 설정해 주면 일부 필드만 입력해도 에러가 발생하지 않는다.
        product_serializer = ProductSerializer(Product,data=request.data,partial=True)
        if product_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            product_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
