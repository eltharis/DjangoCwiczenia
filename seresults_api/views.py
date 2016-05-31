from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seresults.models import SearchRequest
from seresults_api.serializers import UserSerializer, SearchRequestSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = get_user_model().objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


class SearchRequestViewSet(viewsets.ModelViewSet):
    queryset = SearchRequest.objects.all()
    serializer_class = SearchRequestSerializer
