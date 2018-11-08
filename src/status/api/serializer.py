from rest_framework import serializers

from status.models import Status

"""
Serializers -> JSON
Serializers -> validate
"""




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            print("Content None")
            content = None
        image = data.get('image',None)
        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required!')
        return data
