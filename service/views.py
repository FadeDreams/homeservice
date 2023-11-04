from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from .serializers import ServiceSerializer
from .models import Service

from django.shortcuts import get_object_or_404
from .filters import ServicesFilter

# Create your views here.

@api_view(['GET'])
def getAllServices(request):
    filterset = ServicesFilter(request.GET, queryset=Service.objects.all().order_by('id'))
    count = filterset.qs.count()
    resPerPage = 3
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = ServiceSerializer(queryset, many=True)
    return Response({
        "count": count,
        "resPerPage": resPerPage,
        'services': serializer.data
        })


@api_view(['GET'])
def getService(request, pk):
    service = get_object_or_404(Service, id=pk)
    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def newService(request):
    data = request.data

    service = Service.objects.create(**data)

    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateService(request, pk):
    service = get_object_or_404(Service, id=pk)

    service.title = request.data['title']
    service.description = request.data['description']
    service.email = request.data['email']
    service.address = request.data['address']
    service.serviceType = request.data['serviceType']
    service.education = request.data['education']
    service.industry = request.data['industry']
    service.experience = request.data['experience']
    service.salary = request.data['salary']
    service.positions = request.data['positions']
    service.company = request.data['company']

    service.save()

    serializer = ServiceSerializer(service, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteService(request, pk):
    service = get_object_or_404(Service, id=pk)

    service.delete()

    return Response({ 'message': 'Service is Deleted.' }, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(request, topic):

    args = { 'title__icontains': topic }
    services = Service.objects.filter(**args)

    if len(services) == 0:
        return Response({ 'message': 'Not stats found for {topic}'.format(topic=topic) })

    
    stats = services.aggregate(
        total_services = Count('title'),
        avg_positions = Avg('positions'),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Max('salary')
    )

    return Response(stats)

