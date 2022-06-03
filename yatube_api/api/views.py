from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404

from api.permissions import IsAuthorOrReadOnly
from posts.models import Post, Group
from api.serializers import (PostSerializer, GroupSerializer,
                             CommentSerializer,
                             FollowSerializer
                             )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
