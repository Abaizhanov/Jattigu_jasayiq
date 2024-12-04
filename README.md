1. Installation Steps
Prerequisites:
- Python
- Django
- React.js 
- pip

Step 1: Clone the project repository
git clone https://github.com/akzhyato/Jattigu_jasayiq.git

cd jattigu


Step 2: Install project dependencies. Run the following command to install Python dependencies   requirements.txt.
   pip install -r requirements.txt

For the backend (Django):
1. Navigate to the backend folder:
   cd backend

2. Migrate database
   python manage,py makemigrations
   python manage.py migrate

3.To be able to access the Django admin interface, create a superuser:
   python manage.py createsuperuser

4. Start the Django development server to verify that everything is working:
   python manage.py runserver

For the frontend (React):
1. Navigate to the frontend folder:
   cd frontend

2. Install the required React.js dependencies:
   npm install

3. Start the React development server to verify that everything is working:
   npm start
