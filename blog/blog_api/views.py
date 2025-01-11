
from blog_app.models import (
    Category,
    HomeSlider,
    FAQ
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    CategorySerializer,
    HomeSliderSerializer,
    FAQSerializer
)
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def api_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        return Response(result.data)
    if request.method == 'POST':
        category = CategorySerializer(data=request.data)
        category.is_valid(raise_exception=True)
        category.save()

        return Response(category.data)



@api_view(['GET', 'PUT', 'DELETE'])
def api_category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        category.delete()

        return Response({'success': True}, status=204)


@api_view(['GET'])
def api_home_slider(request):
    home_slider_items = HomeSlider.objects.all()
    serializer = HomeSliderSerializer(home_slider_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_faq(request):
    faq_items = FAQ.objects.all()
    serializer = FAQSerializer(faq_items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def api_faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'GET':
        serializer = FAQSerializer(faq)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = FAQSerializer(faq, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        faq.delete()
        return Response({'success': True})

