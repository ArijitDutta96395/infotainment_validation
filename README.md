# Infotainment ECU Validation Framework

A comprehensive testing framework for validating infotainment Electronic Control Unit (ECU) communication protocols through simulated CAN bus interactions.

## Overview

This project provides a virtual CAN bus simulation environment for testing infotainment ECU responses without requiring actual hardware. The framework validates ECU communication protocols, response patterns, and error handling mechanisms.

## Project Structure

```
infotainment_validation/
├── can_simulation.py          # Main ECU simulation script
├── send_message.py            # Message transmission utilities
├── receive_message.py         # Message reception utilities
├── validate_response.py       # Response validation logic
├── can_log.txt               # CAN communication logs
├── Infotainment_CAN_Test_Plan.xlsx    # Test planning document
├── Infotainment_CAN_Test_Report.docx  # Test execution report
└── README.md                 # This file
```

## Features

- **Virtual CAN Bus Simulation**: Complete ECU response simulation without hardware dependencies
- **Automated Test Execution**: Built-in test cases for positive and negative scenarios
- **Response Validation**: Automatic validation of ECU responses against expected values
- **Comprehensive Logging**: Detailed logging of all CAN bus interactions
- **Error Handling**: Robust error detection and reporting mechanisms

## ECU Response Logic

The simulated ECU responds to specific data bytes with predefined responses:

| Request Data Byte | ECU Response | Description |
|------------------|--------------|-------------|
| 0x01 | 0xAA | BT Connect Request → BT Connected Response |
| Any other value | 0x00 | Invalid Request → Error Response |

## Usage

### Running the Simulation

Execute the main simulation script:

```bash
python can_simulation.py
```

### Expected Output

```
Virtual CAN bus started...

--- Starting Infotainment ECU Validation ---

Tester: Sent Request ID=0x100, Data=[0x01]
ECU: Received BT Connect Request → Sent BT Connected Response
Validator: PASS → ECU responded with expected byte [0xAA]

Tester: Sent Request ID=0x100, Data=[0xFF]
ECU: Received Invalid Request → Sent Error Response
Validator: PASS → ECU responded with expected byte [0x00]

--- Test Execution Complete ---
```

## Test Cases

### Positive Test Case
- **Test ID**: TC001
- **Request**: 0x01 (BT Connect Request)
- **Expected Response**: 0xAA (BT Connected Response)
- **Purpose**: Validates successful BT connection establishment

### Negative Test Case
- **Test ID**: TC002
- **Request**: 0xFF (Invalid Request)
- **Expected Response**: 0x00 (Error Response)
- **Purpose**: Validates proper error handling for invalid requests

## File Descriptions

### can_simulation.py
Main simulation script containing:
- ECU response logic implementation
- Test case execution framework
- Result validation and reporting

### send_message.py
Handles message transmission to the virtual CAN bus including:
- Message formatting
- Transmission timing
- Error handling for send operations

### receive_message.py
Manages message reception from the virtual CAN bus including:
- Message parsing
- Response extraction
- Timeout handling

### validate_response.py
Provides response validation functionality:
- Expected vs actual response comparison
- Pass/fail determination
- Detailed validation reporting

## Test Documentation

### Test Plan (Infotainment_CAN_Test_Plan.xlsx)
- Comprehensive test strategy
- Test case definitions
- Pass/fail criteria
- Resource requirements

### Test Report (Infotainment_CAN_Test_Report.docx)
- Test execution results
- Detailed findings
- Recommendations
- Compliance status

## Logging

All CAN bus interactions are logged to `can_log.txt` with timestamps for:
- Message transmission events
- ECU response events
- Validation results
- Error conditions

## Extending the Framework

### Adding New Test Cases

1. Define test case parameters in `can_simulation.py`
2. Update expected response mapping
3. Add validation logic in `validate_response.py`
4. Document in test plan and report

### Adding New ECU Responses

1. Modify the `ecu_response` function in `can_simulation.py`
2. Update response mapping documentation
3. Add corresponding test cases

## Requirements

- Python 3.6 or higher
- No additional dependencies required

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Update documentation
5. Submit a pull request

## License

This project is proprietary software developed for infotainment system validation purposes.

## Support

For technical support or questions regarding this validation framework, please contact the infotainment validation team.
