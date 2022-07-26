#!/usr/bin/python3 

##########################################################################################
# server.py: Example of MQTT subscription, where received data from multiple topics at
#            host "broker.hivemq.com" is printed in the terminal.
##########################################################################################
import paho.mqtt.client as mqtt 

def client_on_connect(client, data, flags, result_code):
   """
   client_on_connect: Printing status after connection attempt, indicated via the result code,
                      where result_code != 0 indicates an error.
   """
   if (result_code):
      print("Could not connect to host " + str(client._host) + "!\n")
   else:
      print("Successfully connected to host " + str(client._host) + "!\n")
   return

def client_on_disconnect(client, data, flags, result_code):
   """
   client_on_disconnect: Printing status after disconnection, indicated via the result code,
                         where result_code != 0 indicates unexpected disconnection.
   """
   if (result_code):
      print("Unexpected disconnection from host " + str(client._host) + "!\n")
   else:
      print("Disconnected from host " + str(client._host) + "!\n")
   return

def client_on_message(client, data, message):
   """
   client_on_message: Printing latest received message and the the topic it originates from.
   """
   print("Received message from topic " + str(message.topic) + ": ", end = "")
   print(message.payload.decode("utf-8"), end = "\n")
   return

def main():
   """
   main: Connecting a client to host "broker.hivemq.com", using a wildcard to subscribe 
         to every topic in "python/mqtt/topics". Function pointers are used to print
         status during connection and disconnection and printing received messages.
         A thread is started to receive messages and call the correct callback function
         by calling method loop_start. A while loop is used to run the program continuously.
         This while loop could be skipped by calling method loop_forever instead of
         loop_start.
   """
   client = mqtt.Client()
   client.on_connect = client_on_connect
   client.on_disconnect = client_on_disconnect
   client.on_message = client_on_message
   client.connect(host = "broker.hivemq.com", port = 1883)
   if not client.is_connected():
      client.reconnect()
   client.subscribe(topic = "python/mqtt/topics/#", qos = 1)
   client.loop_start()
   while True:
      pass
   return

# Calling the main function to start the program if this is the startup file:
if __name__ == "__main__":
   main()