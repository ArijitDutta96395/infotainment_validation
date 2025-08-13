import can
import time

bus = can.interface.Bus(interface='virtual', channel='test_channel', bitrate=500000)
print("Sending Bluetooth Connect request...")

# Send Positive Request
msg = can.Message(arbitration_id=0x100, data=[0x01], is_extended_id=False)
bus.send(msg)
print("Message Sent: ID=0x100, Data=[01]")
time.sleep(2)

# Send Negative Request
msg = can.Message(arbitration_id=0x100, data=[0xFF], is_extended_id=False)
bus.send(msg)
print("Message Sent: ID=0x100, Data=[FF]")
