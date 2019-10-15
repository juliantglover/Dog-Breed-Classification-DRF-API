from rest_framework import serializers

class Image(serializers.Serializer):
    image = serializers.ImageField()

class Result(serializers.Serializer):
    prediction  = serializers.IntegerField()
    results  = serializers.ListField(child=serializers.ListField(child=serializers.IntegerField()))