# Full-Stack-Hackthon-Registration

This project is a robust, full-stack registration system for a hackathon, combining a Python Flask web application for user interface and data persistence, and a UiPath Robotic Process Automation (RPA) bot for automated, real-time email confirmations.

## ✨ Features

* **Responsive Registration Form:** User-friendly form built with HTML and **Tailwind CSS**.
* **Backend Validation:** Checks the database for existing emails to prevent duplicate registrations.
* **Database Integration:** Stores registration data (name, email, teamname, projectIdea) in a **MySQL** database.
* **Persistent Input:** Form fields retain user input upon error, providing a better user experience.
* **RPA Automation:** A **UiPath** process automatically queries the database, sends personalized confirmation emails via **SMTP** for new registrations, and updates the `mailsent` status to prevent duplicate emails.
* **Personalized Confirmation:** The confirmation email includes the student's name, team, and registration ID.

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Web Backend** | Python (Flask) | Handles routing and database interaction. |
| **Web Frontend** | HTML, Tailwind CSS | UI/UX for the registration form. |
| **Database** | MySQL | Stores registration data in the `registrations` table. |
| **Automation** | UiPath Studio, SMTP | Connects to DB, iterates through new users, and sends emails. |

---

## ⚙️ Setup and Installation

### A. Web Application & Database Setup

1.  **MySQL Database:**
    * Create a database named `hackthon_reg` (or update `db_config` in `app.py`).
    * Create a table named `registrations` with the following structure. **Note:** The `mailsent` column is crucial for the RPA process.
        ```sql
        CREATE TABLE registrations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            teamname VARCHAR(255),
            projectIdea TEXT,
            mailsent VARCHAR(10) DEFAULT 'no'
        );
        ```
    * Update the database connection details in `app.py`:
        ```python
        db_config = {
            "host": "localhost",      
            "user": "root",           
            "password": "YOUR_DB_PASSWORD",   # <-- Update this
            "database": "hackthon_reg"  
        }
        ```

2.  **Python Environment:**
    * Install the required Python packages:
        ```bash
        pip install Flask mysql-connector-python
        ```
    * Run the Flask application:
        ```bash
        python app.py
        ```
    The registration form will be accessible at `http://127.0.0.1:5000/`.

### B. UiPath RPA Automation Setup

This process automates sending confirmation emails.

1.  **Open UiPath Project:** Open the project located in the `uipath-rpa-process/` folder in UiPath Studio.
2.  **Database Connection:**
    * Open `uipath-rpa-process/Main.xaml`.
    * Verify/Update the `DatabaseConnect` activity in the `Main Sequence` with the correct DSN (for ODBC) or connection string, username, and password. The current connection uses `Dsn=Hackthon_db;uid=root;pwd=Anil@2003`.
3.  **Email Configuration:**
    * Update the `Send SMTP Email` activity with your organization's SMTP credentials.
    * **Current Settings:** The bot is configured to use GMail's SMTP server:
        * **Email:** `anianni9164@gmail.com`
        * **Password:** `evxt qdff tfnm vwpm` (App Password)
        * **Server/Port:** `smtp.gmail.com:465` with SSL enabled
4.  **Running the Bot:**
    * Run the `Main.xaml` sequence. The bot will check for new registrations (`mailsent = 'no'`) and process them.
    * This bot should be scheduled to run at regular intervals (e.g., every 5 minutes) via **UiPath Orchestrator** or a local scheduler to ensure real-time confirmations.

---

## 📸 Screenshots

*(Add your images here using standard Markdown format, referencing the `images` folder)*

```markdown
| Registration Form | Success Page |
| :---: | :---: |
| ![Registration Form](images/form.png) | ![Success Page](images/success.png) |
