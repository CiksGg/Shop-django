from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer,RatingSerializer
from .models import Comment,Rating
from .permissions import IsAuthorOrReadOnly
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

# class RatingViewSet(ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     permission_classes = [IsAuthorOrReadOnly]

class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self,request):
        user = request.user
        ser = RatingSerializer(data=request.data, context = {'request':request})
        ser.is_valid(raise_exception=True)
        product_id = request.data.get('product')
        if Rating.objects.filter(author = user, product__id = product_id ).exists():
            rating = Rating.objects.get(author = user, product__id = product_id)
            rating.value = request.data.get('value')
            rating.save()
        else:
            # Rating.objects.create(user)
            ser.save()
        return Response(status=201)

