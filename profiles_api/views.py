from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView (APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview=[
        'uses HTTP methods as function (get,post,patch,delete)',
        'Is similar to traditional Django view',
        'Is mapped Manually to urls'
        ]

        return Response({"message":'hello','an_apiview':an_apiview})
