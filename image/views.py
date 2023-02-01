from django.shortcuts import render
import os
from django.views import View
from .api_config import generate_image_from_prompt


class LandingPage(View):
    def get(self, request):
        return render(request, 'image/index.html')


class GeneratingImage(View):
    def get(self, request):
        return render(request, 'image/main.html')

    def post(self, request):
        if request.method == 'POST':
            API_KEY = os.getenv('OPENAI_API_KEY')
            prompt = request.POST.get('prompt')
            if prompt:
                image_data = generate_image_from_prompt(prompt, API_KEY)
                if image_data != KeyError:
                    print(image_data)
                    image_url = image_data[0].get("url")
                    return render(request, 'image/main.html', {"image_url": image_url})

                render(request, 'image/index.html')

            return render(request, 'image/index.html')
