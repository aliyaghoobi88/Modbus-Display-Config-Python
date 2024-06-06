import tkinter as tk
from tkinter import ttk, messagebox
from serial.tools import list_ports
import minimalmodbus

# Constants
MAX_CHAR_LIMIT = 11
baud_rates = [1200,2400,4800,9600]

# Global variables
modbus_instrument = None

def update_led_status():
    global modbus_instrument
    if modbus_instrument:
        try:
            up_key_value = modbus_instrument.read_register(39)
            down_key_value = modbus_instrument.read_register(40)
            enter_key_value = modbus_instrument.read_register(41)

            led1_color = "green" if up_key_value == 1 else "red"
            led2_color = "green" if down_key_value == 1 else "red"
            led3_color = "green" if enter_key_value == 1 else "red"

            led1.config(bg=led1_color)
            led2.config(bg=led2_color)
            led3.config(bg=led3_color)
        except Exception as e:
            print(f"Failed to update LED status: {e}")
    else:
        print("Modbus instrument is not initialized")
    
    # Schedule the next update after 1000 milliseconds (1 second)
    root.after(1000, update_led_status)

# Start the periodic update of LED status

def change_modbus_config():
    baud_rate_index = dbox_Baud.current()
    modbus_id = tbx_Mdbusid.get()

    try:
        if modbus_instrument:
            modbus_instrument.write_register(37, baud_rate_index)
            modbus_instrument.write_register(36, int(modbus_id))
            modbus_instrument.write_register(38, 1)
            messagebox.showinfo("Success", "Modbus configuration updated. Parameters saved.")
        else:
            messagebox.showerror("Error", "Modbus instrument is not initialized")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to change Modbus config: {e}")
        
def connect_to_modbus():
    global modbus_instrument
    selected_port = dbox_Comname.get()
    modbus_id = tbx_Mdbusid.get()
    baud_rate = dbox_Baud.get()

    if not modbus_id:
        messagebox.showerror("Error", "Modbus ID is empty")
        return

    try:
        modbus_instrument = minimalmodbus.Instrument(selected_port, int(modbus_id))
        modbus_instrument.serial.baudrate = int(baud_rate)
        modbus_instrument.serial.timeout = 1
        print(f"Connected to Modbus device on {selected_port} (ID: {modbus_id})")
    except Exception as e:
        print(f"Failed to connect to Modbus device: {e}")

def disconnect_from_modbus():
    global modbus_instrument
    modbus_instrument = None
    print("Disconnected from Modbus device")

def send_to_holding_registers():
    if not modbus_instrument:
        messagebox.showerror("Error", "Not connected to Modbus device")
        return

    line1_value = tbx_line1.get()
    line2_value = tbx_line2.get()
    line3_value = tbx_line3.get()

    if len(line1_value) > MAX_CHAR_LIMIT:
        messagebox.showwarning("Warning", f"Line1 exceeded {MAX_CHAR_LIMIT} characters limit")
    if len(line2_value) > MAX_CHAR_LIMIT:
        messagebox.showwarning("Warning", f"Line2 exceeded {MAX_CHAR_LIMIT} characters limit")
    if len(line3_value) > MAX_CHAR_LIMIT:
        messagebox.showwarning("Warning", f"Line3 exceeded {MAX_CHAR_LIMIT} characters limit")

    try:
        for i, char in enumerate(line1_value[:MAX_CHAR_LIMIT]):
            modbus_instrument.write_register(i, ord(char))
        for i, char in enumerate(line2_value[:MAX_CHAR_LIMIT], MAX_CHAR_LIMIT):
            modbus_instrument.write_register(i, ord(char))
        for i, char in enumerate(line3_value[:MAX_CHAR_LIMIT], MAX_CHAR_LIMIT * 2):
            modbus_instrument.write_register(i, ord(char))
        print("Values sent to holding registers")
    except Exception as e:
        print(f"Failed to send values to holding registers: {e}")

def buzzer_on():
    try:
        modbus_instrument.write_register(42, 2)
        print("Buzzer ON")
    except Exception as e:
        print(f"Failed to turn ON buzzer: {e}")

def buzzer_off():
    try:
        modbus_instrument.write_register(42, 3)
        print("Buzzer OFF")
    except Exception as e:
        print(f"Failed to turn OFF buzzer: {e}")

def beep():
    try:
        modbus_instrument.write_register(42, 1)
        print("Beep")
    except Exception as e:
        print(f"Failed to beep: {e}")

def populate_com_ports():
    com_ports = [port.device for port in list_ports.comports()]
    dbox_Comname['values'] = com_ports
    if com_ports:
        dbox_Comname.current(0)

def populate_baud_rates():
    dbox_Baud['values'] = baud_rates
    dbox_Baud.current(0)


def change_modbus_config():
    # Retrieve the selected baud rate index from the combo box
    baud_rate_index = dbox_Baudnew.current()
    
    # Retrieve the Modbus ID from the entry widget
    modbus_id = tbx_Mdbusidnew.get()

    try:
        # Check if the Modbus instrument is initialized
        if modbus_instrument:
            # Write the baud rate index to holding register 37
            modbus_instrument.write_register(37, baud_rate_index)
            
            # Write the Modbus ID to holding register 36
            modbus_instrument.write_register(36, int(modbus_id))
            
            # Write 1 to holding register 38 to save the parameters
            modbus_instrument.write_register(38, 1)
            
            # Show a success message box
            messagebox.showinfo("Success", "Modbus configuration updated. Parameters saved.")
        else:
            # Show an error message box if the Modbus instrument is not initialized
            messagebox.showerror("Error", "Modbus instrument is not initialized")
    except Exception as e:
        # Show an error message box if there's an exception
        messagebox.showerror("Error", f"Failed to change Modbus config: {e}")
def ack_up():
    global modbus_instrument
    if modbus_instrument:
        try:
            modbus_instrument.write_register(39, 0)
            print("ACK for UP Key")
        except Exception as e:
            print(f"Failed to send ACK for UP Key: {e}")
    else:
        print("Modbus instrument is not initialized")

def ack_down():
    global modbus_instrument
    if modbus_instrument:
        try:
            modbus_instrument.write_register(40, 0)
            print("ACK for DOWN Key")
        except Exception as e:
            print(f"Failed to send ACK for DOWN Key: {e}")
    else:
        print("Modbus instrument is not initialized")

def ack_enter():
    global modbus_instrument
    if modbus_instrument:
        try:
            modbus_instrument.write_register(41, 0)
            print("ACK for ENTER Key")
        except Exception as e:
            print(f"Failed to send ACK for ENTER Key: {e}")
    else:
        print("Modbus instrument is not initialized")


# GUI setup
root = tk.Tk()
root.title("Modbus RTU Display ")

# Connect and Disconnect buttons
btn_connect = tk.Button(root, text="Connect", command=connect_to_modbus)
btn_connect.grid(row=0, column=0, padx=10, pady=10)
btn_disconnect = tk.Button(root, text="Disconnect", command=disconnect_from_modbus)
btn_disconnect.grid(row=0, column=1, padx=10, pady=10)

# Port and Baud Rate dropdowns
label_port = tk.Label(root, text="Port")
label_port.grid(row=1, column=0, padx=10)
dbox_Comname = ttk.Combobox(root)
dbox_Comname.grid(row=1, column=1, padx=10)

label_baud_rate = tk.Label(root, text="Baud Rate")
label_baud_rate.grid(row=2, column=0, padx=10)
dbox_Baud = ttk.Combobox(root)
dbox_Baud.grid(row=2, column=1, padx=10)

# Modbus ID textbox
label_modbus_id = tk.Label(root, text="Modbus ID")
label_modbus_id.grid(row=3, column=0, padx=10)
tbx_Mdbusid = tk.Entry(root)
tbx_Mdbusid.grid(row=3, column=1, padx=10)

ttk.Separator(root, orient="horizontal").grid(row=4, columnspan=4, sticky="ew", padx=10, pady=10)
# Line textboxes
label_line1 = tk.Label(root, text="Line1")
label_line1.grid(row=5, column=0, padx=10, pady=10)
tbx_line1 = tk.Entry(root)
tbx_line1.grid(row=5, column=1, padx=10, pady=10)

label_line2 = tk.Label(root, text="Line2")
label_line2.grid(row=6, column=0, padx=10, pady=10)
tbx_line2 = tk.Entry(root)
tbx_line2.grid(row=6, column=1, padx=10, pady=10)

label_line3 = tk.Label(root, text="Line3")
label_line3.grid(row=7, column=0, padx=10, pady=10)
tbx_line3 = tk.Entry(root)
tbx_line3.grid(row=7, column=1, padx=10, pady=10)

# Send to Holding Registers button
btn_send_to_holding_registers = tk.Button(root, text="Send to Holding Registers", command=send_to_holding_registers)
btn_send_to_holding_registers.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

ttk.Separator(root, orient="horizontal").grid(row=9, columnspan=4, sticky="ew", padx=10, pady=10)


# Buzzer controls
btn_buzzer_on = tk.Button(root, text="Buzzer ON", command=buzzer_on)
btn_buzzer_on.grid(row=10, column=0, padx=10, pady=10)

btn_buzzer_off = tk.Button(root, text="Buzzer OFF", command=buzzer_off)
btn_buzzer_off.grid(row=10, column=1, padx=10, pady=10)

btn_beep = tk.Button(root, text="Beep", command=beep)
btn_beep.grid(row=10, column=2, padx=10, pady=10)


ttk.Separator(root, orient="horizontal").grid(row=11, columnspan=4, sticky="ew", padx=10, pady=10)

# LED indicators (Squares)
led1 = tk.Label(root, bg="red", width=3, height=1)
led1.grid(row=12, column=0, padx=5, pady=5)

led2 = tk.Label(root, bg="red", width=3, height=1)
led2.grid(row=12, column=1, padx=5, pady=5)

led3 = tk.Label(root, bg="red", width=3, height=1)
led3.grid(row=12, column=2, padx=5, pady=5)

# ACK buttons
btn_ack_up = tk.Button(root, text="ACK", command=ack_up)
btn_ack_up.grid(row=13, column=0, padx=5, pady=5)

btn_ack_down = tk.Button(root, text="ACK", command=ack_down)
btn_ack_down.grid(row=13, column=1, padx=5, pady=5)

btn_ack_enter = tk.Button(root, text="ACK", command=ack_enter)
btn_ack_enter.grid(row=13, column=2, padx=5, pady=5)


ttk.Separator(root, orient="horizontal").grid(row=14, columnspan=3, sticky="ew", padx=10, pady=10)

# Label for "Change Modbus Config"
label_change_config = tk.Label(root, text="Change Modbus Config")
label_change_config.grid(row=15, column=1, pady=5)

# Combo box for baud rate
label_baud_ratenew = tk.Label(root, text="Baud Rate")
label_baud_ratenew.grid(row=16, column=0, padx=10, pady=5)


dbox_Baudnew = ttk.Combobox(root, values=[1200,2400, 4800, 9600, 115200])
dbox_Baudnew.grid(row=16, column=1, padx=10, pady=5)
dbox_Baudnew.current(2)  # Set default value to 9600

# Modbus ID textbox
label_modbus_idNEW = tk.Label(root, text="Modbus ID")
label_modbus_idNEW.grid(row=17, column=0, padx=10, pady=5)
tbx_Mdbusidnew = tk.Entry(root)
tbx_Mdbusidnew.grid(row=17, column=1, padx=10, pady=5)

btn_change_param = tk.Button(root, text="Change Param", command=change_modbus_config)
btn_change_param.grid(row=18, columnspan=2, pady=10)

populate_com_ports()
populate_baud_rates()
update_led_status()
root.mainloop()

