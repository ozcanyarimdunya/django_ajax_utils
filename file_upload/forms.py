from django.forms import forms


class FileUploadForm(forms.Form):
    input_file_1 = forms.FileField()
    input_file_2 = forms.FileField()
