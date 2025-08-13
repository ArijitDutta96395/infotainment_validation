import time

print("Virtual CAN bus started...")

# --- ECU Response Logic (no actual CAN bus needed) ---
def ecu_response(data_byte):
    if data_byte == 0x01:
        print("ECU: Received BT Connect Request → Sent BT Connected Response")
        return 0xAA
    else:
        print("ECU: Received Invalid Request → Sent Error Response")
        return 0x00

# --- Send + Validate together ---
def run_test_case(test_data, expected_response):
    print(f"Tester: Sent Request ID=0x100, Data=[{test_data:02X}]")
    resp = ecu_response(test_data)
    if resp == expected_response:
        print(f"Validator: PASS → ECU responded with expected byte [{expected_response:02X}]")
    else:
        print(f"Validator: FAIL → Expected [{expected_response:02X}], got [{resp:02X}]")

print("\n--- Starting Infotainment ECU Validation ---\n")
run_test_case(0x01, 0xAA)  # Positive case
time.sleep(1)
run_test_case(0xFF, 0x00)  # Negative case
print("\n--- Test Execution Complete ---")
