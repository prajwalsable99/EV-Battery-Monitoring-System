import os
from google.cloud import pubsub_v1
import json
import time
from BatteryDataSensorApi import generate_correlated_ev_data

# change path of json file according to your pc
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\\Users\\PS001028870\Documents\\Python Course\battery-project\battery-project-435805-c2b0ec6d08b9.json"


PROJECT_ID="battery-project-435805"
TOPIC="ev-battery-topic"


# Initialize Pub/Sub client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC)


def publish_message(project_id, topic_id, message_data):
    # Create a Publisher client
    publisher = pubsub_v1.PublisherClient()
    
    # Define the topic path
    topic_path = publisher.topic_path(project_id, topic_id)
    
    # Convert message data to JSON string and encode to bytes
    message_data_json = json.dumps(message_data)
    message_data_bytes = message_data_json.encode('utf-8')

    try:
        # Publish the message
        future = publisher.publish(topic_path, message_data_bytes)
        # Wait for the result and print message ID
        print(f"Published message ID: {future.result()}")
    except GoogleAPIError as e:
        print(f"An error occurred: {e}")

# Define the message as a dictionary
message_data={
  "timestamp": "2024-09-24 16:38:00",
  "vehicleid": 1111,
  "voltage": 200.5,
  "current": 150.0,
  "temperature": 45.3,
  "stateofcharge": 85.0,
  "poweroutput": 75.0

}

publish_message(PROJECT_ID, TOPIC, message_data)

entries=1
c=0
while (c<entries):
    messages_data =generate_correlated_ev_data(vehicle_ids=[1,2,3,4,5]) 
    for message_data in messages_data:

        # Publish the message
        publish_message(PROJECT_ID, TOPIC, message_data)
        print("data==>",message_data)
    c=c+1
    time.sleep(60)

