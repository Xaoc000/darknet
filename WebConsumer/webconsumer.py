import sys
import os
import math
from iofog_python_sdk.client import IoFogClient, IoFogException
from iofog_python_sdk.iomessage import IoMessage
from iofog_python_sdk.listener import *

class MessageListener(IoFogMessageWsListener):
    def on_receipt(self, message_id, timestamp):
        print('Receipt: {} {}'.format(message_id, timestamp))

    def on_message(self, io_msg):
        # DO THE DECODING THE BYTEARRAY STUFF HERE
        messages = io_msg.contentdata.decode()

        for message in messages:
            bottom_left = message[0]
            top_right = message[1]
            print(bottom_left + "And " + top_right + "\n")

def main():
    try:
        client = IoFogClient()
    except IoFogException as e:
    #client creation failed, e contains description
        print(e)
        return -1

    client.establish_message_ws_connection(MessageListener())