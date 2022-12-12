from rest_framework.serializers import ModelSerializer
from .models import Comment,Rating


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

