# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Define API to manage a GET request
@api_view(['GET'])
def getRequest(request):
    # Define response
    response = JsonResponse(
        {
            'message': 'Welcome to the ECC-Worflow Catalog-API!'
        }, 
        status=200)
    return response