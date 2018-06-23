# Ride-my-Way API

Ride-my App is a carpooling application that provides drivers with the ability to create ride offers 
and passengers to join available ride offers.
 
## Endpoints 
HTTP Method|End point |Action
-----------|----------|--------------|------
GET| /api/v1/rides   | Fetch all ride offers
GET | /api/v1/rides/<_id> | Fetch a single ride offer
POST | /api/v1/rides | Create a ride offer
POST | /api/v1/rides/<_id>/requests  | Make a request to join a ride


## Requirements
- Python 3.6.5
- Flask framework
## Testing frame
- nosetests

## Running the application
- Use Postman to test the endpoints
