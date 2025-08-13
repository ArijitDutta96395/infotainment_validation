import can

# Create virtual CAN bus (separate process)
bus = can.interface.Bus(interface='virtual', channel='test_channel', bitrate=500000)
print("ECU simulation started... Waiting for messages.")

while True:
    msg = bus.recv(timeout=1)
    if msg and msg.arbitration_id == 0x100:
        if msg.data[0] == 0x01:
            response = can.Message(arbitration_id=0x101, data=[0xAA], is_extended_id=False)
            bus.send(response)
            print("ECU: Received BT Connect Request → Sent BT Connected Response")
        else:
            response = can.Message(arbitration_id=0x101, data=[0x00], is_extended_id=False)
            bus.send(response)
            print("ECU: Received Invalid Request → Sent Error Response")
