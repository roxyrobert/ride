

total_rides = []

class Rides:
    def __init__(self,route,driver,fare):
        '''rides class'''
        self._id = 0
        self.route = route
        self.driver = driver
        self.fare = fare       
        self.total_rides = []

    def get_id(self):
        return self._id
    
    def get_route(self):
        return self.route

    def get_driver(self):
        return self.driver
    
    def get_fare(self):
        return self.fare
    
    def add_ride(self):
        '''create a new_ride'''

        _id = len(total_rides)
        self._id = _id + 1

        new_ride = {
            '_id':self._id,
            'route':self.route,
            'driver': self.driver,
            'fare':self.fare
        }

        total_rides.append(new_ride)
        return new_ride

    @staticmethod
    def get_a_specific_ride(_id):
        
        _id = int(_id) 
        if len(total_rides) > 0 and _id <= len(total_rides):
            ride_data = {
                '_id': total_rides[_id-1]['_id'],
                'route': total_rides[_id-1]['route'],
                'driver': total_rides[_id-1]['driver'],
                'fare': total_rides[_id-1]['fare'],
            }
            return ride_data


ride_requests = []

class RideRequests:
    def __init__(self,username,contact):
        self.request_id = 0
        self.username = username
        self.contact = contact
        self.ride_requests = []
    
    def get_request_id(self):
        return self.request_id
    
    def get_username(self):
        return self.username
    
    def get_contact(self):
        return self.contact
    
    def join_ride(self):
        '''request to join a ride'''

        request_id = len(ride_requests)
        self.request_id = request_id + 1

        request_ride = {
            'request_id':self.request_id,
            'username':self.username,
            'contact': self.contact
        }

        ride_requests.append(request_ride)
        return request_ride

users = []

class Users():
    def __init__(self, username, email, pwd_hash, contact, role):
        self.user_id = 0
        self.username = username
        self.email = email
        self.pwd_hash = pwd_hash
        self.contact = contact
        self.role = role
        self.users = []
    
    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_pwd_hash(self):
        return self.pwd_hash

    def get_contact(self):
        return self.contact

    def get_role(self):
        return self.role

    def add_user(self):
        '''add a new user to users list'''
        user_id = len(users)
        self.user_id = user_id + 1
        
        new_user = {
            'user_id':self.user_id,
            'username':self.username,
            'email': self.email,
            'pwd_hash':self.pwd_hash,
            'contact':self.contact,
            'role':self.role
        }
        users.append(new_user)
        return new_user

    def encode_auth_token(self, user_id):
        # """
        # Generates the Auth Token
        # :return: string
        # """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET'),
                algorithm='HS256'
            )
        except Exception as e:
            return e