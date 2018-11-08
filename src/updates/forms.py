from django import forms

from .models import Update as UpdateModel

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        print("Clean method")
        content = data.get('content', None)
        if content == "":
            print("Content None")
            content = None
        image = data.get('image',None)
        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required!')
        return super().clean(*args, **kwargs)
