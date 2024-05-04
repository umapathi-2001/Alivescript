import os
import requests
import time

# Get deployment ID from environment variable
deployment_id = os.getenv('DEPLOYMENT_ID')
if not deployment_id:
    print("Error: DEPLOYMENT_ID environment variable is not set.")
    exit(1)

# Construct service URL using deployment ID
service_url = f'https://{deployment_id}.zeabur.com'

# Get interval time from environment variable (default to 60 seconds if not set)
request_interval = int(os.getenv('REQUEST_INTERVAL', 60))

def keep_alive():
    while True:
        try:
            response = requests.get(service_url)
            if response.status_code == 200:
                print(f"Request sent successfully to {service_url}")
            else:
                print(f"Failed to send request to {service_url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred while sending request to {service_url}: {e}")
        
        time.sleep(request_interval)

if __name__ == "__main__":
    keep_alive()
