from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.forms.models import model_to_dict

from .models import Content
from content.serializers import ContentSerializer


class ContentMultiplyView(APIView):
    def get(self, _):
        all_content = Content.objects.all()
        contents_to_dict = [model_to_dict(content) for content in all_content]

        return Response(contents_to_dict)

    def post(self, request):
        serializer = ContentSerializer(**request.data)

        if serializer.is_valid():
            content_valid = Content.objects.create(**serializer.data)
            content_to_dict = model_to_dict(content_valid)

            return Response(content_to_dict, status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ContentCRUDView(APIView):
    def get(self, _, content_id):
        try:
            content = Content.objects.get(pk=content_id)

        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)

        content_to_dict = model_to_dict(content)

        return Response(content_to_dict)

    def patch(self, request, content_id):
        try:
            content = Content.objects.get(pk=content_id)

        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(content, key, value)

        content.save()
        content_to_dict = model_to_dict(content)

        return Response(content_to_dict)

    def delete(self, _, content_id):
        try:
            content = Content.objects.get(pk=content_id)

        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)

        content.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)


class ContentFilterView(APIView):
    def get(self, request):

        params = request.query_params.get("title")
        print(params)

        contents_match = Content.objects.filter(title__icontains=params)
        contents_to_dict = [model_to_dict(content) for content in contents_match]

        return Response(contents_to_dict)
