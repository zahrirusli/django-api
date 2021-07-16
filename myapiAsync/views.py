from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from myapiAsync.tasks import add
from myapiAsync.models import Product
from django.shortcuts import render
from celery.result import AsyncResult
from django.views.decorators.http import require_http_methods, require_GET
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from myapi.models import Product
from myapi.serializers import ProductSerializer


@api_view(["GET"])
def get_product_list(request):
    try:
        if request.method == 'GET':
            product = Product.objects.all()
            
            prod_name=request.GET.get('product_name',None)
            if prod_name is not None:
                product = product.filter(product_name__icontains=prod_name)
            prod_serialize = ProductSerializer(product,many=True)
            return JsonResponse(prod_serialize.data,safe=False)
    except:
        return JsonResponse(prod_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])  
def add_product(request):
    print(request.method)
    if request.method == "POST":
        
        prod_data = JSONParser().parse(request)
        print(prod_data)
        add.delay(prod_data=prod_data)
        return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(["DELETE"])        
def delete_all_product(request):
    try:
        if request.method == 'DELETE':
            count = Product.objects.all().delete()
            return JsonResponse({'message': '{} Product were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    except: 
        return JsonResponse(count.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product_detail(request, pk):
    try: 
        products = Product.objects.get(pk=pk) 
        if request.method == 'GET': 
            product_serialize = ProductSerializer(products) 
            return JsonResponse(product_serialize.data) 
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['PUT']) #put & patch
def update_product_detail(request,pk):
    try:
        products = Product.objects.get(pk=pk) 
        if request.method == 'PUT': 
            prod_data = JSONParser().parse(request) 
            product_serialize = ProductSerializer(products, data=prod_data,partial=True) 
            if product_serialize.is_valid(): 
                product_serialize.save() 
                return JsonResponse(product_serialize.data) 
            return JsonResponse(product_serialize.errors, status=status.HTTP_400_BAD_REQUEST) 
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['DELETE'])
def delete_product_by_id(request,pk):        
    try:
        products = Product.objects.get(pk=pk) 
        if request.method == 'DELETE': 
            products.delete() 
            return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND)                
# Create your views here.
