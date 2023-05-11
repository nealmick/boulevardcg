from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Article




#Test input
'''
{
    "title": "test",
    "content": "test"
}
'''

#Articles List View
#/articles/
@api_view(['GET','POST'])
def articles(request):
    if request.method == "POST":
        print('post')
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
        return Response({'message': 'Article created successfully.', 'id': instance.id}, status=201)
  

    if request.method == "GET":
        qs = Article.objects.all().order_by('-id')
        return get_paginated_queryset_response(qs,request)
    
            
    return Response({'test':'hello'},200)


#Article Detail View
#/articles/<int:ArticlePK>
@api_view(['GET','PUT','DELETE'])
def articleDetail(request, ArticlePK):
    try:
        article = Article.objects.get(pk=ArticlePK)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)







#get paginated response from qs
def get_paginated_queryset_response(qs,request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    paginated_qs = paginator.paginate_queryset(qs,request)
    serializer = ArticleSerializer(paginated_qs, many=True, context={"request":request}) 
    return paginator.get_paginated_response(serializer.data)
