from rest_framework import serializers
from user.models import User, UserProfile
from blog.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    
    class Meta:
        model = Article
        fields = ["Catagory","comment_set"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "introduction"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = ArticleSerializer(many=True)
    class Meta:
        model = User 
        fields = ["username","userprofile","article_set"]

