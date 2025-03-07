from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import ReactSerializer
from rest_framework.response import Response

class ReactView(APIView):
    def get(self, request):
        output = [{"model": output.model, "accuracy": output.accuracy, "cost_in": output.cost_in, "cost_out": output.cost_out, "latency": output.latency}
                  
                  for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # Save the data to the database
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)