import serial
import time
import numpy as np

arduino_port = "/dev/ttyUSB0"
baud_rate = 9600
filename = "tempSensor.csv"
duration = int(input("Collect data for how many seconds?: "))

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)
    start = time.time()
    print(f"Connected to Arduino on {arduino_port}")

    with open(filename, "w", encoding="utf-8") as file:
        print(f"Exporting data to '{filename}'... Press Ctrl+C to stop")

        while time.time() - start < duration:
            time.sleep(1)
            if ser.in_waiting > 0:
                raw_data = ser.readline()
                decoded_line = raw_data.decode("utf-8").strip()
                temperatures = np.loadtxt(filename)

                if decoded_line:
                    elapsed_seconds = int(time.time() - start)
                    print(f"{elapsed_seconds} Seconds: {decoded_line}")
                    file.write(decoded_line + "\n")
                    file.flush()

            time.sleep(0.01)

except KeyboardInterrupt:
    print("\nData collection stopped by user")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial connection closed")