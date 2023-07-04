from .serializer import *
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from blog.models import Article
from rest_framework.views import APIView
from rest_framework import status

class ArticleListView(APIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser ,)
    def get(self , request):
        query = Article.objects.filter(is_public=True)
        serializer = ArticleSerializer(query , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)