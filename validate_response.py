import can

bus = can.interface.Bus(interface='virtual', channel='test_channel', bitrate=500000)
print("Validator started... Listening for ECU response.")

while True:
    msg = bus.recv(timeout=3)
    if msg and msg.arbitration_id == 0x101:
        if msg.data[0] == 0xAA:
            print("PASS: ECU responded with BT Connected [AA]")
        elif msg.data[0] == 0x00:
            print("PASS: ECU responded with Error [00]")
        else:
            print(f"FAIL: ECU responded with unexpected byte [{msg.data[0]:02X}]")
    else:
        print("FAIL: No response received from ECU.")
