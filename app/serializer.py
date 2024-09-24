# Serializers are used to convert complex data types, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['model', 'accuracy', 'cost_in', 'cost_out', 'latency']