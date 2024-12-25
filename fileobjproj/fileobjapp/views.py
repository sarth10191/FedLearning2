from django.http import JsonResponse
from .models import Client
from django.core.files import File
from asgiref.sync import sync_to_async
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
MODEL_DIR = "../models/"
os.makedirs(MODEL_DIR, exist_ok=True)

@csrf_exempt
async def RegisterClientView(request):
    if request.method == "POST":
        try:
            client = await sync_to_async(Client.objects.create)(name = request.POST.get("name"))
            return JsonResponse({"message":"Client registered successfully"})
        except Exception as e:
            return JsonResponse({"Error":f"Error registering client{e}"}, status = 500)
    else:
        return JsonResponse({"Error":"Method not allowed"}, status = 500)

@csrf_exempt
async def RecieveFiles(request):
    if request.method == "POST":
        try:
            client = await sync_to_async(Client.objects.get)(name=request.POST.get("name"))
            path = os.path.join(MODEL_DIR, client.name)
            file = request.FILES.get("file")
            with open(path, 'wb') as f:
                content = file.read()
                f.write(content)
            client.filepath = path
            await sync_to_async(client.save)()
            return JsonResponse({"saved_file":"successfilly"}, status=200)
        except Exception as e:
            return JsonResponse({"Error":f"Error saving client. {e}"}, status = 500)
    else:
        return JsonResponse({"Error":"Method not allowed"}, status = 500)