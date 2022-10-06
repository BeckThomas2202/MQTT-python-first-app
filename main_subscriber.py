"""
This file contains the MQTT subscriber.
"""
import paho.mqtt.client as mqtt

MQTTBROKER = "127.0.0.1"


def on_connect(client, connection_result):
    """
    Callback function for when the client receives a CONNACK response from the server.
    @param client: The client instance for this callback
    @param userdata: The private user data as set in Client() or userdata_set()
    @param flags: Response flags sent by the broker
    @param rc: The connection result
    """

    print("Connected with result code "+str(connection_result))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("TEMPERATURE")


def on_message(message):
    """
    Callback function for when a PUBLISH message is received from the server.
    @param client: The client instance for this callback
    @param userdata: The private user data as set in Client() or userdata_set()
    @param msg: An instance of MQTTMessage.
    """

    print(message.topic+" "+str(message.payload))


def on_disconnect(connection_result):
    """
    Callback function for when the client disconnects from the server.
    """
    if connection_result != 0:
        print("Unexpected disconnection.")


def main():
    """
    Main function that subscribes to a topic.
    """
    client = mqtt.Client("python client")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect(MQTTBROKER, 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a manual interface.
    client.loop_forever()


if __name__ == '__main__':
    main()

# Shell command to publish a message to the broker
# mosquitto_pub -h 127.0.0.1 -m "test message" -t TEMPERATURE
