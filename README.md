# Port Scanner

The Port Scanner is a Python program that allows you to scan ports on a specified IP address. It utilizes multi-threading to achieve faster scanning of multiple ports concurrently.

## Prerequisites

- Python 3.x

## Usage

1. **Clone** the repository or **download** the program files.

2. Open a terminal or command prompt and **navigate** to the directory where the program files are located.

3. Run the following command to install the required dependencies (if not already installed):

           pip install -r requirements.txt
        

4. Run the program by executing the following command: 
 
           python port_scanner.py
           

5. You will be prompted to **enter** the IP address you want to scan and the number of ports to scan.

6. The program will start scanning the specified IP address for open ports. The progress and the number of open ports found will be displayed in real-time.

7. Once the scanning is complete, the program will show the IP address and a list of open ports found.

8. You will be given an option to **save** the results to a file. Enter 'Y' to save the results or any other key to continue without saving.

9. If you choose to save the results, a file named "results_[IP address].txt" will be created in the same directory, containing the IP address and the list of open ports.

10. The program supports concurrent scanning with multiple threads. You can adjust the `NUM_THREADS` variable in the program to control the level of concurrency. Higher values may increase the scanning speed but also consume more system resources.

11. Press **Ctrl+C** to stop the scanning process at any time.

## Notes

- The program uses the `socket` module to establish TCP connections with the specified IP address and ports. It checks for open ports and identifies the associated service names.

- The timeout for each port connection attempt is set to 1 second (`sock.settimeout(1)`). You can modify this value in the `scan_port` function if desired.

- The program utilizes multi-threading to scan ports concurrently and improve performance. The number of worker threads can be adjusted by modifying the `NUM_THREADS` variable.

- This program is intended for educational and informational purposes only. Make sure to use it responsibly and respect the security and privacy of others.

- For more information or assistance, refer to the program's source code or contact the author.

          
        
