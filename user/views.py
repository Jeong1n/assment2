from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password

from django.views.decorators.csrf import csrf_exempt

from user.serializers import UserSerializer
from .models import User

class SignUpView(APIView):

    permission_class = [permissions.AllowAny]

    def post(self, request):
        # data = json.loads(request.body)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        fullname = request.data.get('fullname', None)
        email = request.data.get('email', None)
        # User.objects.create(email=email, password=password)

        passcode = make_password(password)
        User(username=username, password=passcode, fullname=fullname, email=email).save()

        return Response({"massage": f"회원가입이 완료되었습니다. {username}님 환영합니다!"}, status=status.HTTP_200_OK)

class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    @csrf_exempt
    def get(self, request):
        user = request.user
        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serialized_user_data = UserSerializer(user).data
        
        return Response(serialized_user_data,status=status.HTTP_200_OK)
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)
        
    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!"})