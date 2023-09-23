import requests

# Replace with your Mapbox API key
MAPBOX_API_KEY = ''

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

def calculate_distance(origin, destination):
    endpoint = f'https://api.mapbox.com/directions/v5/mapbox/driving/{origin[0]},{origin[1]};{destination[0]},{destination[1]}'
    
    params = {
        'access_token': MAPBOX_API_KEY,
    }
    
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the distance in meters
        distance_meters = data['routes'][0]['distance']
        
        # Convert distance to kilometers
        distance_kilometers = distance_meters / 1000.0
        
        return distance_kilometers
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def main(origin,destination):
    start = geocode_location(origin)
    end = geocode_location(destination)
    if origin and destination:
        distance = calculate_distance(start, end)
        
        if distance is not None:
            return distance