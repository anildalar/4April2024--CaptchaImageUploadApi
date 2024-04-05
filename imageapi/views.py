from rest_framework.views import APIView
from rest_framework.response import Response
import os

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
            
            # Return a response indicating that the image was received and stored
            return Response({"message": "Image received and stored"})
        else:
            # If 'captchaImage' is not in the request, return an error response
            return Response({"error": "No image file provided"}, status=400)
