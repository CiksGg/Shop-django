from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer,RatingSerializer
from .models import Comment,Rating
from .permissions import IsAuthorOrReadOnly


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthorOrReadOnly]

