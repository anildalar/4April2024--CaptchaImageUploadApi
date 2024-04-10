from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this to exempt CSRF token requirement
from .models import Customer

from PIL import Image
import io, base64, os, json

def base64_to_image(base64_string, output_file):
    try:
        # Add padding to the Base64 string if needed
        while len(base64_string) % 4 != 0:
            base64_string += '='
            
            
        print('>>>',base64_string )
        # Assuming base64_str is the string value without 'data:image/jpeg;base64,'
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.urlsafe_b64decode('data'))
    
    except Exception as e:
        print("Error:", e)
        
@csrf_exempt  # Exempt CSRF token requirement for this view
def getBalance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            client_key = data['clientKey']
            if client_key:
                try:
                    customer = Customer.objects.get(client_key=client_key)
                    balance = customer.current_amount_usd
                    response_data = {
                        "errorId": 0,
                        "balance": balance
                    }
                    return JsonResponse(response_data)
                except Customer.DoesNotExist:
                    return JsonResponse({"errorId": 1, "message": "Invalid clientKey"})
            else:
                return JsonResponse({"errorId": 1, "message": "clientKey not provided"})
        except json.JSONDecodeError:
            return JsonResponse({"errorId": 1, "message": "Invalid JSON format"})
    else:
        return JsonResponse({"errorId": 1, "message": "Invalid request method"})


        
@csrf_exempt  # Exempt CSRF token requirement for this view
def createTask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            client_key = data['clientKey']
            if client_key:
                try:
                    base64String = data['task']['body'].split(' ')[1]
                    output_file = "image.jpg"  # Output file name (you can change the extension based on the image format)

                    base64_to_image(base64String, output_file)
                    
                    response_data = {
                        "test": "Done"
                    }
                    return JsonResponse(response_data)
                except Customer.DoesNotExist:
                    return JsonResponse({"errorId": 1, "message": "Invalid clientKey"})
            else:
                return JsonResponse({"errorId": 1, "message": "clientKey not provided"})
        except json.JSONDecodeError:
            return JsonResponse({"errorId": 1, "message": "Invalid JSON format"})
    else:
        return JsonResponse({"errorId": 1, "message": "Invalid request method"})
    pass