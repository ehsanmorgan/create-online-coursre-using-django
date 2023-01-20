from django import forms

from courses.models import course


class postForm(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'