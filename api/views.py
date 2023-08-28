from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from base.models import Note
from .serializers import NoteSerializer

# GET requests
@api_view(['GET'])
def getData(request, genre):
    paginator = PageNumberPagination()
    paginator.page_size = 5

    if genre == 'general':
        notes = Note.objects.order_by('-date')
    else:
        notes = Note.objects.filter(genre=genre).order_by('-date')
    
    paginated_notes = paginator.paginate_queryset(notes, request)

    serializer = NoteSerializer(paginated_notes, many=True)

    response_data = {'total_rows': notes.count(), 'data': serializer.data}
    return paginator.get_paginated_response(response_data)


# POST requests
@api_view(['POST'])
def addData(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
