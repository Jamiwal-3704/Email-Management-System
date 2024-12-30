from flask import Flask, render_template, request, redirect, url_for, session
from utils.email_handler import send_email, receive_emails
from utils.nlp_processor import generate_response
from models.database import get_templates, save_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home page
@app.route('/')
def home():
    return render_template('login.html')

# Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Get email content from form
        email_content = request.form['email_content']
        # Generate AI-based response
        ai_response = generate_response(email_content)
        return render_template('dashboard.html', ai_response=ai_response)
    return render_template('dashboard.html')

# Manage templates
@app.route('/templates', methods=['GET', 'POST'])
def templates():
    if request.method == 'POST':
        new_template = request.form['template']
        save_template(new_template)
    templates = get_templates()
    return render_template('templates.html', templates=templates)

if __name__ == '__main__':
    app.run(debug=True)
