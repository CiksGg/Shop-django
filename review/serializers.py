from rest_framework.serializers import ModelSerializer
from .models import Comment,Rating


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')  # получаем запрос из view
        attrs['author'] = request.user
        return attrs
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep['product']
        rep['author'] = instance.author.email
        return rep

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')  # получаем запрос из view
        attrs['author'] = request.user
        return attrs

