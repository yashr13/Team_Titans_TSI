Traffic Signboard Instructor

Project Description The Traffic Signboard Instructor is a Django-based application designed to recognize and classify traffic signs from uploaded images. The application provides an intuitive interface for users to upload images, view recognized traffic signs, and learn about their meanings. It incorporates user authentication for secure access and includes an admin dashboard for managing users and monitoring system statistics.

Setup Instructions

Step 1: Clone the Repository $ git clone <repository_url> $ cd Traffic-Signboard-Instructor

Step 2: Create and Activate a Virtual Environment On Windows: $ python -m venv venv $ venv\Scripts\activate On macOS/Linux: $ python3 -m venv venv $ source venv/bin/activate

Step 3: Install Dependencies $ pip install -r requirements.txt

Step 4:Set up email settings in info.py EMAIL_USE_TLS = True EMAIL_HOST = 'smtp.gmail.com' EMAIL_HOST_USER= 'your_email' EMAIL_HOST_PASSWORD= 'password' #password generated from security page on manage account section of that email account(search for "App Password" and generate new for your custom app) EMAIL_PORT = 587

Step 5: Run the Server $ python manage.py runserver
