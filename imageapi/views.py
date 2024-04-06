from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CaptchaTask
from rest_framework.views import APIView
from rest_framework.response import Response


import uuid
import threading
import time
import os



@csrf_exempt
def get_captcha_task(request, task_id):
    if request.method == 'GET':
        try:
            captcha_task = CaptchaTask.objects.get(task_id=task_id)
            return JsonResponse({'status': captcha_task.status, 'result': '123'}) # captcha_task.result
        except CaptchaTask.DoesNotExist:
            return JsonResponse({'error': 'Task not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    
def process_captcha_task(captcha_task, captcha_data):
    time.sleep(10)  # Simulating 10 seconds of processing time
    
    captcha_task.status = 'completed'
    captcha_task.result = f"Predicted captcha: 123"  # Reversed captcha as an example
    captcha_task.save()
        
class CaptchaImageView(APIView): 
    def post(self, request, *args, **kwargs):
        # Check if the 'captchaImage' file is included in the request
        if 'captchaImage' in request.FILES:
            # Retrieve the image file from the request
            image_file = request.FILES['captchaImage']
            
            # Specify the directory where you want to save the image
            upload_dir = 'uploads'
            # Create the directory if it doesn't exist
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            
            # Construct the file path to save the image
            file_path = os.path.join(upload_dir, image_file.name)
            
            # Open a new file in write binary mode
            with open(file_path, 'wb') as destination:
                # Iterate through the chunks of the uploaded file
                for chunk in image_file.chunks():
                    # Write each chunk to the destination file
                    destination.write(chunk)
            
            task_id = str(uuid.uuid4())
        
            captcha_task = CaptchaTask.objects.create(task_id=task_id, status='processing')
            captcha_data=''
            threading.Thread(target=process_captcha_task, args=(captcha_task, captcha_data)).start()
            
            
            #return JsonResponse({'task_id': task_id}, status=202)
            # Return a response indicating that the image was received and stored
            return Response({
                                "message": "Image received and stored",
                                "task_id": task_id,
                            })
        else:
            # If 'captchaImage' is not in the request, return an error response
            return Response({"error": "No image file provided"}, status=400)
