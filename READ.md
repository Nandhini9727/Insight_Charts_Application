# Dashboard page project

# Project Overview
This project aims to build a versatile dashboard page that showcases a variety of charts, such as candlestick, line, bar, and pie charts. The dashboard’s backend is powered by Django and Django Rest Framework (DRF), which work together to create REST API endpoints. These endpoints handle requests from the frontend and provide the chart data needed for display. The frontend of the application is crafted with Next.js, ensuring that users experience a responsive and interactive interface.

# Backend
The backend is built with Django, which manages the overall application, and DRF, which is used to create the RESTful APIs. These APIs are crucial as they deliver the chart data to the frontend. Here’s what’s included in the backend setup:

API Endpoints: These endpoints deliver data in JSON format for different types of charts (candlestick, line, bar, and pie).
CORS Configuration: This setup allows the frontend (which may run on a different server or port) to access the backend APIs without any issues.

# Frontend
The frontend is developed using Next.js, a popular React framework that supports server-side rendering and is easy to work with. It communicates with the Django backend through API calls and displays the chart data in various formats. Key aspects of the frontend include:

Chart Components: These are built with libraries like Highcharts and Chart.js to render different types of charts.
Data Fetching: The frontend makes HTTP requests using 'axios' library to retrieve data from the backend.
Responsive Design: The dashboard is designed to be user-friendly and functional on various devices and screen sizes.

## Procedure to setup and run Backend
1) Under backend project folder create a virutual environment
2) 'python -m venv env'
3) Move to project level directory and activate virtual environment - 'env\Scripts\activate'
5) Install Django - 'pip install Django'
6) Install Django Rest Framework -  'pip install django_rest_framework'
6) Intstall CORS Header - 'pip install django-cors-headers'
7) Start Django project - 'django-admin startproject chart'
8) Start Django App - 'python manage.py startapp chart_api'
9) Add 'rest_framework','corsheaders' and 'chart_api' to INSTALLED APPS in settings.py under project directory
10) Add CORS handiling to middleware - 'corsheaders.middleware.CorsMiddleware'
11) Configure CORS header - CORS_ALLOW_ALL_ORIGINS = True
12) Run python 'python manage.py migrate' to migrate default Django tables
13) Confirgure urls.py under project level directory to handle the URL endpoint - ''
14) Confirgure urls.py under app level directory to handle the URL endpoint - '/api/candlestick-data/' , '/api/line-chart-data/','/api/bar-chart-data/','/api/pie-chart-data/'
15) Configure views.py under app level directory to render appropirate JSON response based the API end point
16) Configure tests.py under app level directory to unit test different components of views.py 
17) Run 'python manage.py test' for testing
18) Run 'python manage.py runserver' for staring the development server
19) Open the development server with URL - 'http://127.0.0.1:8000/'
20) Add the end point below to above URL to get the JSON response of required chart data 

#REST API ENDPOINTS
Candlestick Data: GET /api/candlestick-data/
Line Chart Data: GET /api/line-chart-data/
Bar Chart Data: GET /api/bar-chart-data/
Pie Chart Data: GET /api/pie-chart-data/

# Procedure to setup and run Frontend
1) Install Node.js and npm
2) Create Next.js project - 'npx create-next-app@latest chartfrontendapp'
3) Move into project folder - 'cd chartfrontendapp'
4) Install required dependencies and HTTP request - 'npm install highcharts highcharts-react-official react-chartjs-2 chart.js axios'
5) Create folder named dashboard under app directory
6) Create page.js under dashboard folder
7) Configure page.js to display data fetched from backend and utilize libararies for charts installed to create and display charts 
8) Start Next.js development server - 'npm run dev'
9) Open the server with URL - 'http://localhost:3000/dashboard'

# Libraries and Tools used:
# Backend
1) Django: A Python framework for building web apps.
2) Django Rest Framework (DRF): A toolkit for creating REST APIs.
3) django-cors-headers: Manages CORS to allow frontend-backend communication across different domains.

# Frontend
1) Next.js: A React framework that supports server-side rendering and improves performance and SEO.
2) Highcharts: A library for creating interactive and high-performance charts, including candlestick charts.
3) Highcharts React: Makes it easier to use Highcharts in React apps.
4) react-chartjs-2: Simplifies using Chart.js in React applications.
5) Axios: A tool for making HTTP requests to fetch data from the backend.
6) Chart.js: A library for creating various charts like line, bar, and pie charts.

# Development Tools
1) Python: Used for backend development with Django.
2) Node.js: Executes JavaScript and manages frontend dependencies.
3) npm: Manages JavaScript libraries and tools.
4) VS Code: A code editor with extensions for managing and editing code.











