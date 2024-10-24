import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageGenerationSerializer


class GenerateImageView(APIView):
    """
    API View to generate images using the Replicate API.

    This view handles POST requests to generate an image based on a provided prompt.
    """

    def post(self, request):
        """
        Handle POST request for image generation.

        Args:
            request (Request): The incoming request containing the prompt.

        Returns:
            Response: A response containing the image URL or error messages.
        """
        serializer = ImageGenerationSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']

            # Call the Replicate API
            replicate_api_url = "https://api.replicate.com/v1/predictions"
            headers = {
                "Authorization": f"Token YOUR_REPLICATE_API_TOKEN",  # Replace with your actual token
                "Content-Type": "application/json"
            }
            data = {
                "version": "YOUR_MODEL_VERSION",  # Specify the model version
                "input": {
                    "prompt": prompt,
                }
            }

            try:
                response = requests.post(replicate_api_url, json=data, headers=headers)

                if response.status_code == 200:
                    output = response.json()
                    return Response({"image_url": output.get("output")}, status=status.HTTP_200_OK)
                else:
                    return Response(response.json(), status=response.status_code)

            except requests.exceptions.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
