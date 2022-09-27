from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.forms.models import model_to_dict

from .models import Content
from content.serializers import ContentSerializer


class ContentMultiplyView(APIView):
    def get(self, _):
        all_content = Content.objects.all()
        content_to_dict = [model_to_dict(content) for content in all_content]

        return Response(content_to_dict)

    def post(self, request):
        serializer = ContentSerializer(**request.data)

        if serializer.is_valid():
            content_valid = Content.objects.create(**serializer.data)
            content_to_dict = model_to_dict(content_valid)

            return Response(content_to_dict, status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
