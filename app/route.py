from flask import jsonify, request
from flask import Flask

app = Flask(__name__)

@app.route('/signin', methods=['POST'])
def signin():
    # Get the user's credentials from the request
    email = request.form['email']
    password = request.form['password']
    
    # Use Firebase's authentication service to verify the credentials
    user = auth.sign_in_with_email_and_password(email, password)
    
    # If the credentials are valid, return a success message
    return jsonify({'message': 'Sign-in successful!'}), 200
    
@app.route('/signup', methods=['POST'])
def signup():
    # Get the user's information from the request
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Use Firebase's authentication service to create a new user account
    auth.create_user_with_email_and_password(email, password)
    
    # Add the user's information to the database
    db.child('users').push({
        'name': name,
        'email': email
    })
    
    # Return a success message
    return jsonify({'message': 'Sign-up successful!'}), 200



@app.route('/toys', methods=['POST'])
def add_toy():
    # Get the toy's information from the request
    name = request.form['name']
    description = request.form['description']
    condition = request.form['condition']
    organization_id = request.form['organization_id']
    
    # Add the toy to the database
    toy_id = db.child('toys').push({
        'name': name,
        'description': description,
        'condition': condition,
        'organization_id': organization_id
    })
    
    # Return a success message
    return jsonify({'message': 'Toy added successfully!', 'toy_id': toy_id}), 200

@app.route('/toys/<toy_id>', methods=['PUT'])
def update_toy(toy_id):
    # Get the updated toy information from the request
    name = request.form['name']
    description = request.form['description']
    condition = request.form['condition']
    organization_id = request.form['organization_id']
    
    # Update the toy in the database
    db.child('toys').child(toy_id).update({
        'name': name,
        'description': description,
        'condition': condition,
        'organization_id': organization_id
    })
    
    # Return a success message
    return jsonify({'message': 'Toy updated successfully!'}), 200

@app.route('/toys/<toy_id>', methods=['DELETE'])
def delete_toy(toy_id):
    # Delete the toy from the database
    db.child('toys').child(toy_id).remove()
    
    # Return a success message
    return jsonify({'message': 'Toy deleted successfully!'}), 200


@app.route('/toys', methods=['GET'])
def search_toys():
    # Get the search criteria from the request
    location = request.args.get('location')
    age_range = request.args.get('age_range')
    toy_type = request.args.get('toy_type')
    
    # Query the toy database based on the search criteria
    toys = db.child('toys').order_by_child('location').equal_to(location).get()
    
    # Return the search results
    return jsonify({'toys': toys}), 200
