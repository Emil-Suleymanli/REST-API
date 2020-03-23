import json
import flask
#importing objects from the Flask model
from flask import Flask, jsonify, request

#define the app
app = Flask(__name__)

#data
cities = [{'name' : 'wakaw'}, {'name' : 'laval'}, {'name' : 'serres'}, {'name' : 'glenelg'}, {'name' : 'ottawa'}, {'name' : 'toronto'}]

#Function to define whether the message is palindrome

#reverse the message
def reverse(message): 
    return message[::-1] 
#determine whether palindrome
def palindrome(message): 
    reversed = reverse(message) 
    if (message == reversed): 
        return True
    return False

#index
@app.route('/', methods=['GET'])
def project():
	return 'Cloud Audition Project'

#Retrieve all the messages (cities)
@app.route('/cities', methods=['GET'])
def get_all_cities():
	return jsonify({'cities' : cities})


#Retrieve the specific city name and define if it is palindrome
@app.route('/cities/<string:name>', methods=['GET'])
def get_selected_city(name):
	selected_city = [city for city in cities if city['name'] == name][0]
	return jsonify({'city' : selected_city}, {'Is the message palindrome?' : palindrome(selected_city['name'])})


#Create the message (add a city)
@app.route('/cities', methods=['POST'])
def add_city():
	new_city = {'name' : request.json['name']}
	cities.append(new_city)
	return jsonify({'cities' : cities})


#Update the message (change the city to a different one)
@app.route('/cities/<string:name>', methods=['PUT'])
def edit_city(name):
	selected_city = [city for city in cities if city['name'] == name]
	selected_city[0]['name'] = request.json['name']
	return jsonify({'city' : selected_city[0]})


#Delete the message (delete the selected city)
@app.route('/cities/<string:name>', methods=['DELETE'])
def delete_city(name):
	selected_city = [city for city in cities if city['name'] == name]
	cities.remove(selected_city[0])
	return jsonify({'cities' : cities})

#run the app
if __name__ == '__main__':
#running on port 8080 and in debug mode
	app.run(debug=True, port=8080)