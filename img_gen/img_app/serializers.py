from rest_framework import serializers


class ImageGenerationSerializer(serializers.Serializer):
    """
    Serializer for validating image generation requests.

    Attributes:
        prompt (str): A text prompt to generate the image.
    """
    prompt = serializers.CharField(max_length=255)
