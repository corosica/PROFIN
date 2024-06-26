from rest_framework import serializers
from .models import Article, Comment,QNAarticle,QNAcomment


from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','nickname')


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content','user_id','created_at','user')

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True,read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class QNAArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = QNAarticle
        fields = ('id', 'title', 'content','user_id','created_at','user')

class QNACommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = QNAcomment
        fields = '__all__'
        read_only_fields = ('article',)

class QNAArticleSerializer(serializers.ModelSerializer):
    comments = QNACommentSerializer(many=True,read_only=True)
    comment_count = serializers.IntegerField(source='comments.count',read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = QNAarticle
        fields = '__all__'