from flask import Flask, request, render_template, redirect

app = Flask(__name__)

database= {}

@app.route('/')
def hi():
    return "hi welcome"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Retrieve data from the form
        key = request.form.get('key')
        value = request.form.get('value')

        # Create a new entry in the dictionary
        database[key] = value

        # Redirect to a success page or display a success message
        return "Entry created successfully!"
    
    return render_template('create.html')
 

@app.route('/read')
def read():
    # Display the current state of the dictionary
    return render_template('read.html', database=database)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Retrieve data from the form
        key = request.form.get('key')
        value = request.form.get('value')

        # Update the value of an existing entry
        if key in database:
            database[key] = value

        # Redirect to the read route
        return redirect('/read')

    # If it's a GET request, display the update form
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # Retrieve data from the form
        key = request.form.get('key')

        # Delete an existing entry from the dictionary
        if key in database:
            del database[key]

        # Redirect to the read route
        return redirect('/read')

    # If it's a GET request, display the delete form
    return render_template('delete.html')


if __name__ == "__main__":
    app.run()