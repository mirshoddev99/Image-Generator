# Image Generation Web Application

  A Django based web application to generate images using OpenAI API.

## Features

  Generates images using OpenAI API based on user provided prompt
  Displays the generated image on the web page
  Allows user to input the prompt for the generated image
  Provides options to customize the generated image
  Displays the generated image with download option
  
  
## Requirements

  Python 3.6 or above
  Django 3.1 or above
  Requests 2.24 or above
  OpenAI API Key
  
  
## Installation

  Clone the repository: git clone https://github.com/mirshoddev99/Image-Generator.git
  Navigate to the project directory: cd image-generation-web-app
  Create a virtual environment: python -m venv venv
  Activate the virtual environment: source venv/bin/activate
  Install the required packages: pip install -r requirements.txt
  Create a .env file in the project directory and add the following line: OPENAI_API_KEY=<your_openai_api_key>
  Apply migrations: python manage.py migrate
  Start the development server: python manage.py runserver


## Usage

Visit http://localhost:8000 in your web browser
Input the prompt for the image you want to generate
Customize the image if required
Click on Generate button to generate the image
Download the generated image if required

## Contributions
Contributions are welcome. Please feel free to fork the repository, make changes and create a pull request.
