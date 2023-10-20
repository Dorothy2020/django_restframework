from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# decorator
@api_view(['GET', 'POST'])
#Function that get arequest
def drink_list(request):
   if request.method=='GET':
      drinks=Drink.objects.all()
      serializer=DrinkSerializer(drinks,many=True)
      return JsonResponse({"drinks":serializer.data},safe=False)

   if request.method=='POST':
      DrinkSerializer(data=request.data)
      if serializer.is_valid:
          serializer.save()
      return Response(serializer.data,status.Http_201_CREATED)


    # get all the drinks


    #serialize them
    #return json
