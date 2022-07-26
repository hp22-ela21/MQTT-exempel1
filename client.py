#!/usr/bin/python3

##########################################################################################
# client.py: Example of MQTT publish, where data entered by the user is published to a
#            specified topic at host "broker.hivemq.com".
##########################################################################################
import paho.mqtt.client as mqtt

def main():
   """
   main: Connecting a client to host "broker.hivemq.com", then publishing messages
         entered by the user to topic "python/mqtt/topics/topic1". If the user enters
         a blink line, the client is disconnected and the program terminates.
   """
   client = mqtt.Client()
   client.connect(host = "broker.hivemq.com", port = 1883)
   if (not client.is_connected()):
      client.reconnect()
   client.loop_start()
   while True:
      print("Enter a message to publish or a blank line to finish:")
      message = readline()
      if (message):
         client_publish(client, "python/mqtt/topics/topic1", message)
      else:
         client.loop_stop()
         client.disconnect()
         break
   print("Bye!\n")
   return

def readline():
   """
   readline: Returing a line of text read from the terminal.
   """
   s = input()
   print()
   return s

def client_publish(client, topic, message, qos = 1):
   """
   client_publish: Publishing a message to specified topic. A thread is
   """   
   msg = client.publish(topic = topic, payload = message, qos = qos)
   msg.wait_for_publish()
   print("Message " + str(message) + " published!\n")
   return

# Calling the main function to start the program if this is the startup file:
if __name__ == "__main__":
   main()