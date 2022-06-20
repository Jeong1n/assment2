from rest_framework import serializers
from user.models import User, UserProfile
from blog.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "Comment"

class ArticleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Article
        fields = ["title"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article_set = ArticleSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = User 
        fields = ["username","article_set","comment_set","userprofile"]

