from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


db_config = {
    "host": "localhost",      
    "user": "root",           
    "password": "Anil@2003",   
    "database": "hackthon_reg"  
}

def get_db_connection():
    """Helper function to establish a database connection."""
    return mysql.connector.connect(**db_config)

@app.route("/")
def home():
    """Renders the main registration form."""
    return render_template("index.html", error=request.args.get('error'), form_data={})

@app.route("/register", methods=["POST"])
def register():
    """Handles the registration logic, including email existence check."""
    fullname = request.form.get("fullName")
    mail = request.form.get("email")
    team = request.form.get("teamName")
    project = request.form.get("projectIdea")

    conn = None
    cursor = None
    

    form_data = {
        'fullName': fullname,
        'email': mail,
        'teamName': team,
        'projectIdea': project
    }

    try:
        conn = get_db_connection()
        cursor = conn.cursor()


        check_sql = "SELECT email FROM registrations WHERE email = %s"
        cursor.execute(check_sql, (mail,))
        

        if cursor.fetchone():
            error_message = "This email is already registered."
            return render_template("index.html", error=error_message, form_data=form_data)


       
        insert_sql = """
            INSERT INTO registrations (`name`, `email`, `teamname`, `projectIdea`, `mailsent`)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (fullname, mail, team, project, "no")

        cursor.execute(insert_sql, values)
        conn.commit()

        return render_template("success.html", fullname=fullname)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        
        return render_template("index.html", error="An internal error occurred during registration.", form_data=form_data)
        
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    
    app.run(debug=True)
