# Nearby Hotels API using Django 
 API web application to show list of hotels given a location and coordinates 

#Getting Started
### setting up virtual environment
1. open cmd or terminal, run this command if you don't have virtual environment on your machine > pip install virtualenv
2. create a virtual environment > virtualenv env
3. Activate the virtual environment
Windows: env\Scripts\activate
Linux / OSX: source/bin/activate

### Seeting up Local Server
1. Firstly, clone or download the github repository > https://github.com/gyrationtechs/nearhotel.git
2. I am assume you are familiar with working with virtual environment and command prompt
3. to clone the repository run this command > 'git clone https://github.com/gyrationtechs/nearhotel.git'
4. initialize a virtual environment on the repository you created, activate the virtual environment
5. run the command to install all library used >  pip install -r requirements.txt
6. run the command > python manage.py migrate (to create database tables)
7. Before running > python manage.py runserver read the API Docs
8. Rename the .env-example file to .env and replace the API_KEY Variable with the key gotten from the here API

## API DOCS
1. This project uses Here API for geocoding, near places, and mapView, to access the API you will need to provide an API_KEY on the .env file.
2. Go to > https://developer.here.com and sign up for a free developer account, create a project and navigate to your dashboard
3. Open the service you created and click on Create API_KEY, copy the key and paste the code in the .env file, replace YOUR_API_KEY with the value from the here dashboard

### Testing the Application Locally
1. Once all configurations are set, you can run the command > python manage.py runserver
2. By default, you access the web app through > localhost:8000

### Remote host
1. The web application is hosted remotely on heroku and can be accessed through the link below
Demo: https://nearbyhotel.herokuapp.com
