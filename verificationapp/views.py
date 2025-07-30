from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from .serializers import  NationalIdSerializer


class ValidationView(APIView):

    permission_classes = [HasAPIKey]

    def post(self, request):
        national_id = request.data.get("national_id")
        if not national_id:
            return Response({"error": "national_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NationalIdSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.save()
            return Response({'valid'  :validated_data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

