from flask import Flask, request, request_started #pip install flask
from flask_restful import Resource, Api, reqparse #pip install Flask-RESTful

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

app = Flask(__name__)
api = Api(app) 

class GetCity(Resource):
    def get(self):
        try:
            lat = request.args.get('lat')
            lng = request.args.get('lng')
            coord = lat + "," + lng
            location = geolocator.reverse(coord, exactly_one=True)
            address = location.raw['address']
            city = address.get('city', '')
            print(city);
            return city
            
        except Exception as e:
            return str(e)
        
api.add_resource(GetCity, '/getCity') 

if __name__ == '__main__':
    app.run(port=3000)  
    print(app.logger.error)

