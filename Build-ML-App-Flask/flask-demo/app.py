from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')  # Renders the home page

# Define the contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data here (e.g., save to a database or send an email)
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Redirect to the thank you page after processing
        return redirect(url_for('thank_you', name=name))
    return render_template('contact.html')  # Renders the contact form page

# Define a thank you route for form submissions
@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thank_you.html', name=name)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
