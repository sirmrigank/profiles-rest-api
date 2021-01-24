from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test API view"""

    def get(self, request, format=None):
        """returns a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application',
            'is mapped manually to urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
