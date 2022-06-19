from logging import exception
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, Catagorymodel
from permission import RegistedMoreThan3daysUser

class BlogView(APIView):
    permission_classes = [RegistedMoreThan3daysUser]

    def get(self, request):
        articles = Article.objects.filter(author=request.user)
        titles = [ t['title'] for t in articles.values() ]
        return Response({'titles': titles})

    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        catagory = request.data.get('Catagory', '')
        contents = request.data.get('Contents', '')
        

        if len(title) <=5 :
            return Response({"message":"제목은 5글자 이상이여야 합니다."})

        if len(contents) <=20 :
            return Response({"message":"댓글은 20글자 이상이여야 합니다."})

        if catagory:
            catagory = [ Catagorymodel.objects.get(name =name) for name in catagory.split(',') ]
        else:
            return Response({"massage":"카테고리를 지정해주세요."})
        
        new_aitcle = Article.objects.create(user=user,title=title,Contents=contents)
        new_aitcle.Catagory.set(catagory)
        return Response({"messgae":"게시물작성 완료!"})