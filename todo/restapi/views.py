from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.models import Item
from .serializers import ItemSerializer
from rest_framework import status

class ItemList(APIView):

    def get(self,request,format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        instance = request.data
        
        serializer = ItemSerializer(data=instance)
        if serializer.is_valid():
            saved = serializer.save()
            saved.url = request.build_absolute_uri() + f"/{saved.id}"
            saved.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,format=None):

        count = Item.objects.all().delete()
        return Response({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class ItemDetail(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)