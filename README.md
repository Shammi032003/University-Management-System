# University Management System

This Flask application serves as a simple University Management System, allowing users to log in, view various aspects of their academic information, and perform actions such as checking attendance, viewing exam results, and accessing course details.

Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/university-management-system.git
cd university-management-system
Database Setup:

Set up a MySQL database named univ.
Execute the SQL queries provided in the script or import the provided database dump file into your MySQL server.
Run the Flask Application:

bash
Copy code
python app.py
The application will run on http://localhost:5000/.

Login:

Access the application through your web browser.
Log in with your credentials.
Dashboard:

After logging in, you will be redirected to the dashboard.
From the dashboard, you can navigate to different sections such as Attendance, Exam Results, Student Details, Enrolled Courses, Timetable, and Triggers.
Logout:

Click on the logout link to log out from the application.
Structure
app.py: Contains the Flask application and routes.
templates/: Directory containing HTML templates for the application's frontend.
static/: Directory containing static files such as CSS, JavaScript, and images.
database.sql: SQL queries to create the necessary database tables.
haarcascade_frontalface_default.xml: Haarcascade file for face detection.
model.h5: Pre-trained Keras model for emotion detection.
p2.csv: CSV file containing motivational quotes for different emotions.
Routes
/: Home route. Redirects to the login page if the user is not logged in; otherwise, redirects to the dashboard.
/login: Login page. Handles user authentication.
/dashboard: Dashboard page. Displays various sections and links to navigate through the application.
/attendance: Attendance page. Displays attendance data.
/exam_results: Exam Results page. Displays exam results data.
/student_details: Student Details page. Displays student details data.
/enrolled_courses: Enrolled Courses page. Displays enrolled courses data.
/timetable: Timetable page. Displays timetable data.
/logout: Logout route. Logs out the user and redirects to the login page.
/triggers: Triggers page. Displays triggers data.
Database Schema
The database schema includes tables such as users, Attendance, and UserQueries.

Contributing
## Requirements

To run this project, you'll need the following:
- Python 3
- Flask
- pymysql

You can install the required packages using pip:
```bash
pip install Flask pymysql
