from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from file_upload.forms import FileUploadForm


class IndexView(View):
    def get(self, request):
        form = FileUploadForm()
        ctx = {
            "form": form
        }
        return render(request, 'index.html', ctx)

    def post(self, request):
        print(request.FILES)
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_1 = request.FILES['input_file_1']
            file_2 = request.FILES['input_file_2']

            return JsonResponse({"file_1": str(file_1), 'file_2': str(file_2)})
        else:
            return JsonResponse({"message": "form is not valid and file is not uploaded"})
