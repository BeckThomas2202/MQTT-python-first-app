"""
This file is part of the `mqtt` project.
It contains the the MQTT publisher.
"""
import time
from paho.mqtt import publish

MQTTBROKER = "127.0.0.1"


def main():
    """
    Main function that publishes a message to the broker.
    """
    while True:
        time.sleep(1)
        publish.single("TEMPERATURE", "test message", hostname=MQTTBROKER)


if __name__ == '__main__':
    main()
