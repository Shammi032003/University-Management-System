from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import pymysql
import secrets

app = Flask(__name__, static_folder='static')
app.secret_key = secrets.token_hex(32)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="univ"
)

def execute_user_query(user_id, query_name):
    cursor = db.cursor()
    query = "SELECT query_text FROM UserQueries WHERE user_id = %s AND query_name = %s"
    cursor.execute(query, (user_id, query_name))
    query_text = cursor.fetchone()

    if query_text:
        print("Retrieved Query Text:", query_text[0])
        cursor.execute(query_text[0])  # Execute the retrieved query text
        data = cursor.fetchall()
        cursor.close()
        print("Data fetched from database:", data)
        return data
    else:
        cursor.close()
        return None

# Define the function to get the current user's ID
def get_current_user_id():
    if 'username' in session:
        cursor = db.cursor()
        query = "SELECT id FROM users WHERE username = %s"
        cursor.execute(query, (session['username'],))
        user_id = cursor.fetchone()
        cursor.close()
        if user_id:
            return user_id[0]
    return None

def validate_login(username, password):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = validate_login(username, password)
        if user:
            session['username'] = user[1]  # Store username in the session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid login credentials"  # You can customize this message

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/attendance')
def attendance():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"  # Handle the case where user is not found

        query_name = 'Attendance Percentage'  # Change this accordingly    
        attendance_data = execute_user_query(current_user_id, query_name)
        
        return render_template('attendance.html', attendance_data=attendance_data)
    return redirect(url_for('login'))



@app.route('/exam_results')
def exam_results():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"  # Handle the case where user is not found

        query_name = 'Exam Result'  # Change this accordingly
        exam_data = execute_user_query(current_user_id, query_name)  # Change variable name to exam_results_data
        return render_template('exam_results.html', exam_data=exam_data)  # Change variable name to exam_results_data

    return redirect(url_for('login'))

@app.route('/student_details')
def student_details():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"  # Handle the case where user is not found
        
        query_name = 'Student Details'
        print(f"Query Name: {query_name}, User ID: {current_user_id}")
        
        student_data = execute_user_query(current_user_id, query_name)
        print("Data from execute_user_query:", student_data)
        
        return render_template('student_details.html', student_data=student_data)
    return redirect(url_for('login'))

@app.route('/enrolled_courses')
def enrolled_courses():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"  # Handle the case where user is not found
        
        query_name = 'Enrolled Courses'
        print(f"Query Name: {query_name}, User ID: {current_user_id}")
        
        courses_data = execute_user_query(current_user_id, query_name)
        print("Data from execute_user_query:", courses_data)
        
        return render_template('enrolled_courses.html', courses_data=courses_data)
    return redirect(url_for('login'))

@app.route('/timetable')
def timetable():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"  # Handle the case where user is not found
        
        query_name = 'Timetable'
        print(f"Query Name: {query_name}, User ID: {current_user_id}")
        
        timetable_data = execute_user_query(current_user_id, query_name)
        print("Data from execute_user_query:", timetable_data)
        
        return render_template('timetable.html', timetable_data=timetable_data)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/triggers')
def triggers():
    if 'username' in session:
        current_user_id = get_current_user_id()
        if current_user_id is None:
            return "User not found"

        # Fetch deleted attendance records for the current user from the "user_query" table
        cursor = db.cursor()
        query = "SELECT query_text FROM UserQueries WHERE user_id = %s AND query_name = 'Attendance Deleted'"
        cursor.execute(query, (current_user_id,))
        deleted_attendance_data = cursor.fetchall()
        cursor.close()

        return render_template('trigger.html', deleted_attendance_data=deleted_attendance_data)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)






















INSERT INTO Attendance (student_id, course_id, attended_classes, total_classes)
VALUES
    (1, 2, 28, 30);

DELETE FROM Attendance WHERE student_id = 1 AND course_id = 2;
