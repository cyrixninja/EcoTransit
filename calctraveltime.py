import requests

# Replace with your Mapbox API key
MAPBOX_API_KEY = 'pk.eyJ1IjoiY3lyaXhuaW5qYTY0IiwiYSI6ImNsbXAwc2I0NTE0MGYyc3IyaDV3bjJ4ZDYifQ.uGw7ZerBPUOu2R6TKGw0FA'

def geocode_location(location_name):
    endpoint = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{location_name}.json'
    
    params = {
        'access_token': MAPBOX_API_KEY,
        'limit': 1,  # Limit the results to one location
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data['features']:
            # Get the coordinates of the first result
            coordinates = data['features'][0]['geometry']['coordinates']
            return tuple(coordinates)
        else:
            print(f"Location '{location_name}' not found.")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
def calculate_travel_time(origin, destination, mode):
    endpoint = f'https://api.mapbox.com/directions/v5/mapbox/{mode}/{origin[0]},{origin[1]};{destination[0]},{destination[1]}'
    
    params = {
        'access_token': MAPBOX_API_KEY,
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the travel time in seconds
        travel_time_seconds = data['routes'][0]['duration']
        
        # Convert travel time to minutes
        travel_time_minutes = travel_time_seconds / 60.0
        
        return travel_time_minutes
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    origin_name = input("Enter the origin location: ")
    destination_name = input("Enter the destination location: ")
    
    origin = geocode_location(origin_name)
    destination = geocode_location(destination_name)
    
    if origin and destination:
        mode = input("Enter the mode of transport (driving, cycling, walking): ").lower()
        
        if mode in ['driving', 'cycling', 'walking']:
            travel_time = calculate_travel_time(origin, destination, mode)
            
            if travel_time is not None:
                print(f"The travel time between {origin_name} and {destination_name} ({mode}) is {travel_time:.2f} minutes.")
        else:
            print("Invalid mode of transport. Please enter 'driving', 'cycling', or 'walking'.")
