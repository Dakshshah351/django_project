from django import forms
from ..models import pending_projects

#creating a form
class pending_projects(forms.ModelForm):
    #create meta class
    class Meta:
        model = pending_projects
        fields = [
            "id",
            "project_title",
            "Upload_File",
        ]