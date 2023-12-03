from django import forms
from ..models import RequirementModel

#creating a form
class RequirementGatheringform(forms.ModelForm):
    #create meta class
    class Meta:
        model = RequirementModel
        fields = [
            "Client_name",
            "project_title",
            "start_date",
            "end_date",
            "Client_email",
            "project_Description",
            "project_Technology",
        ]
        