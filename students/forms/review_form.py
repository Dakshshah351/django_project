from django import forms
from .. models import reviewModel

#creating a form
class review_form(forms.ModelForm):
    #create meta class
    class Meta:
        model = reviewModel
        fields = [
            "description"

        ]
        