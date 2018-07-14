from .models import Content, ContentLine
from rest_framework import serializers


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'type')


class ContentLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentLine
        fields = ('content_line', 'content_type', 'content_id', 'id')
