from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
class QoshiqApi(APIView):
    def get(self, request):
        qoshiq = Qoshiq.objects.all()
        nom = request.query_params.get('name')
        janr = request.query_params.get('janr')
        if nom:
            qoshiq = qoshiq.filter(nom__contains=nom)
        if janr:
            qoshiq = qoshiq.filter(janr__contains=janr)
        qoshiq = qoshiq.order_by('davomiylik')
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QoshiqchiApi(APIView):

    def get(self, request):
        qoshiqchi = Qoshiqchi.objects.all()

        qidiruv_soz = request.query_params.get('name')
        davlat = request.query_params.get('davlat')
        if qidiruv_soz:
            qoshiqchi = Qoshiqchi.objects.filter(ism__contains=qidiruv_soz)
        if davlat:
            qoshiqchi = qoshiqchi.filter(davlat=davlat)
        qoshiqchi = qoshiqchi.order_by('tugilgan_yil')
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
        qidiruv_soz = request.query_params.get('name')
        if qidiruv_soz:
            albom = albom.filter(nom__contains=qidiruv_soz)
        albom = albom.order_by('sana')
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QoshiqchilarViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    @action(detail=True)
    def albom(self, request, pk):
        qoshiqchi = self.get_object()
        albom = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data)

class AlbomViewset(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True)
    def qoshiq(self, request, pk):
        albom = self.get_object()
        qoshiq = Qoshiq.objects.filter(albom=albom)
        serializer = QoshiqSerializer(qoshiq, many=True)
        return Response(serializer.data)

class QoshiqViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer


