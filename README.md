# Modbus RTU Display Control Panel

This project provides a graphical user interface (GUI) for interacting with a Modbus RTU device using the Tkinter library in Python. The application allows users to connect to a Modbus device via a serial port, configure communication parameters, send data to holding registers, control a buzzer, and monitor the status of various keys and LEDs.

![Gui](https://github.com/aliyaghoobi88/Modbus-Display-Config-Python/assets/4157568/5035c415-7207-4e48-8b2f-188114011fc2)
![Mrtu-gui](https://github.com/aliyaghoobi88/Modbus-Display-Config-Python/assets/4157568/aeb194c5-e747-4731-b1dc-952f355bdc06)

## Features

- **Connect/Disconnect to Modbus Device**: Connect or disconnect to a Modbus RTU device via a selected serial port and baud rate.
- **Send Data to Holding Registers**: Send up to three lines of text to the device's holding registers.
- **Buzzer Control**: Turn the buzzer on, off, or make it beep.
- **LED Status Monitoring**: Monitor the status of three LEDs which represent the state of UP, DOWN, and ENTER keys.
- **ACK Keys**: Acknowledge the pressing of UP, DOWN, and ENTER keys.
- **Modbus Configuration**: Change the Modbus device's communication parameters including baud rate and Modbus ID.

## Requirements
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aliyaghoobi88/Modbus-Display-Config-Python.git
   cd Modbus-Display-Config-Python
   ```

2. Install the required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python modbus_gui.py
   ```

2. **Connect to Modbus Device**:
   - Select the appropriate serial port and baud rate from the dropdown menus.
   - Enter the Modbus ID.
   - Click on the `Connect` button.

3. **Send Data to Holding Registers**:
   - Enter text in the Line1, Line2, and Line3 fields (up to 11 characters each).
   - Click the `Send to Holding Registers` button.

4. **Control the Buzzer**:
   - Use the `Buzzer ON`, `Buzzer OFF`, and `Beep` buttons to control the buzzer.

5. **Monitor and Acknowledge Keys**:
   - The LED indicators will show the status of the UP, DOWN, and ENTER keys (green for pressed, red for not pressed).
   - Click the `ACK` buttons to acknowledge key presses.

6. **Change Modbus Configuration**:
   - Select a new baud rate and Modbus ID.
   - Click the `Change Param` button to apply the new configuration.

## GUI Layout

- **Top Section**: Connect/Disconnect controls.
- **Middle Section**: Text input for Line1, Line2, Line3 and sending to holding registers.
- **Lower Section**: Buzzer controls, LED indicators, and ACK buttons.
- **Bottom Section**: Modbus configuration controls.

## Acknowledgments

This project leverages the following libraries:
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- [pyserial](https://pyserial.readthedocs.io/en/latest/) for serial communication.
- [minimalmodbus](https://minimalmodbus.readthedocs.io/en/stable/) for Modbus RTU communication.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your improvements or bug fixes.
