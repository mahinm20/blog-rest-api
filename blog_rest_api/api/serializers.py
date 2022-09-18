from enum import auto
from django.contrib.auth.models import User,Group
from api.models import Author,Blog,Comment
from rest_framework import serializers,permissions

class CommentSerializer(serializers.ModelSerializer):
    commentor = serializers.CharField(source="commentor.username",read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id','commentor','post','body']


class UserSerializers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    

    class Meta:
        model = User
        fields = ['id','username','email','comments']


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

#         return user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'




class BlogSerializer(serializers.ModelSerializer):
    writer = serializers.CharField(source="writer.author_name")
    #comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True,read_only=True)

    def create(self,validated_data):
        name = validated_data['writer']['author_name']
        title = validated_data['title']
        body = validated_data['body']
        upvote =validated_data['upvote']
        downvote = validated_data['downvote']
        name_instance,created= Author.objects.get_or_create(author_name=name)
        blog_instance = Blog.objects.create(title=title,body=body,upvote=upvote,downvote=downvote,writer=name_instance)
        blog_instance.save()
        return blog_instance

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)    
        instance.body = validated_data.get('body',instance.body)
        instance.upvote = validated_data.get('upvote',instance.upvote)
        instance.downvote = validated_data.get('downvote',instance.downvote)
        new_name=(validated_data['writer']['author_name'])
        old_name = Author.objects.get(author_name=instance.writer)
        old_name.author_name = new_name
        old_name.save()
        instance.save()
        return instance



    class Meta:
        model = Blog
        fields = ['id','title','body','upvote','downvote','writer','comments']


