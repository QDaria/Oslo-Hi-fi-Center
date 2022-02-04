from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id' 'created']

class VoteSerializer(serializers.ModelSerializer):
    #voter = serializers.ReadOnlyField(source='voter.username')
    #voter_id = serializers.ReadOnlyField(source='voter.id')
    #post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Vote
        #fields = ['id', 'voter', 'voter_id', 'post']
        fields = ['id']