"""
MQTT IoT Communication Module - Cloud Data Transmission

Handles publishing drone telemetry and sensor data to MQTT broker
for cloud storage and remote monitoring.

Author: Your Name
Date: June 2026
"""

import logging
import json
import paho.mqtt.client as mqtt
import threading
from datetime import datetime

logger = logging.getLogger(__name__)


class MQTTClient:
    """
    MQTT client for IoT communication.
    
    Publishes:
    - drone/telemetry - Drone state (position, velocity, battery)
    - drone/sensors - Environmental sensor data
    - drone/status - Flight status
    
    Subscribes to:
    - drone/commands - Ground station commands
    """
    
    def __init__(self, broker_address="localhost", broker_port=1883, client_id="drone_001"):
        """
        Initialize MQTT client.
        
        Args:
            broker_address (str): MQTT broker hostname/IP
            broker_port (int): MQTT broker port
            client_id (str): Unique client identifier
        """
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.client_id = client_id
        self.connected = False
        
        # Create MQTT client
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_message = self._on_message
        
        logger.info(f"MQTT client initialized: {client_id}")
    
    def connect(self):
        """Connect to MQTT broker."""
        try:
            logger.info(f"Connecting to MQTT broker at {self.broker_address}:{self.broker_port}...")
            self.client.connect(self.broker_address, self.broker_port, keepalive=60)
            self.client.loop_start()  # Start background thread
            logger.info("✓ MQTT connection initiated")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            logger.warning("Running without MQTT connectivity")
            return False
    
    def _on_connect(self, client, userdata, flags, rc):
        """MQTT connection callback."""
        if rc == 0:
            self.connected = True
            logger.info("✓ Connected to MQTT broker")
            # Subscribe to command topic
            self.client.subscribe("drone/commands")
        else:
            logger.error(f"Connection failed with code {rc}")
    
    def _on_disconnect(self, client, userdata, rc):
        """MQTT disconnection callback."""
        self.connected = False
        if rc != 0:
            logger.warning(f"Unexpected disconnection (code {rc})")
    
    def _on_message(self, client, userdata, msg):
        """MQTT message received callback."""
        logger.info(f"Command received: {msg.topic} -> {msg.payload.decode()}")
    
    def publish_telemetry(self, vehicle_state):
        """
        Publish drone telemetry data.
        
        Args:
            vehicle_state (dict): Vehicle state dictionary from DroneController.get_vehicle_state()
        """
        if not self.connected:
            logger.debug("MQTT not connected, skipping telemetry publish")
            return
        
        telemetry = {
            'timestamp': datetime.now().isoformat(),
            'mode': vehicle_state['mode'],
            'armed': vehicle_state['armed'],
            'location': vehicle_state['location'],
            'velocity': vehicle_state['velocity'],
            'battery': vehicle_state['battery'],
        }
        
        try:
            self.client.publish(
                "drone/telemetry",
                json.dumps(telemetry),
                qos=1
            )
            logger.debug("Telemetry published")
        except Exception as e:
            logger.error(f"Failed to publish telemetry: {e}")
    
    def publish_sensor_data(self, sensor_data):
        """
        Publish environmental sensor data.
        
        Args:
            sensor_data (EnvironmentalData): Sensor data from EnvironmentalSensor
        """
        if not self.connected:
            logger.debug("MQTT not connected, skipping sensor data publish")
            return
        
        try:
            self.client.publish(
                "drone/sensors",
                json.dumps(sensor_data.to_dict()),
                qos=1
            )
            logger.debug("Sensor data published")
        except Exception as e:
            logger.error(f"Failed to publish sensor data: {e}")
    
    def publish_status(self, status_message):
        """
        Publish flight status message.
        
        Args:
            status_message (str): Status message
        """
        if not self.connected:
            logger.debug("MQTT not connected, skipping status publish")
            return
        
        status = {
            'timestamp': datetime.now().isoformat(),
            'message': status_message,
        }
        
        try:
            self.client.publish(
                "drone/status",
                json.dumps(status),
                qos=1
            )
            logger.info(f"Status published: {status_message}")
        except Exception as e:
            logger.error(f"Failed to publish status: {e}")
    
    def disconnect(self):
        """Disconnect from MQTT broker."""
        if self.connected:
            logger.info("Disconnecting from MQTT broker...")
            self.client.loop_stop()
            self.client.disconnect()
            self.connected = False
            logger.info("✓ Disconnected")


def main():
    """Example usage of MQTT client."""
    
    # Create MQTT client (will fail if broker not running, which is OK for demo)
    mqtt_client = MQTTClient(broker_address="localhost")
    mqtt_client.connect()
    
    # Simulate some data
    test_telemetry = {
        'mode': 'GUIDED',
        'armed': True,
        'location': {
            'lat': 54.7753,
            'lon': -1.5473,
            'alt': 100.0,
            'relative_alt': 50.0,
        },
        'velocity': [1.0, 1.0, 0.5],
        'battery': {
            'voltage': 11.5,
            'current': 10.0,
            'level': 75,
        }
    }
    
    mqtt_client.publish_telemetry(test_telemetry)
    mqtt_client.publish_status("Test flight initiated")
    
    mqtt_client.disconnect()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
