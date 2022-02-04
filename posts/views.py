from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Post
from .serializers import PostSerializer, VoteSerializer
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class VoteCreate(generics.CreateAPIView):
    #queryset = Post.objects.all()
    serializer_class = VoteSerializer
    permissions_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        #queryset = super(VoteCreate, self).get_queryset()
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        #return queryset.filter(poster=self.request.user)
        return Vote.objects.filter(voter=user, post=post)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise serializers.ValidationError("You have already voted for this post")
        serializer.save(poster=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))