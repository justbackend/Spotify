from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class QoshiqApi(APIView):
    def get(self, request):
        qoshiq = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QoshiqchiApi(APIView):
    def get(self, request):
        qoshiqchi = Qoshiqchi.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchi, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = QoshiqchiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QoshiqchiOneApi(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Qoshiqchi.objects.get(id=pk).delete()
        return Response("Deleted successfully")


class AlbomApi(APIView):
    def get(self, request):
        albom = Albom.objects.all()
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

