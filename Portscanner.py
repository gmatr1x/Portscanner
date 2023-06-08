import socket
import threading
import concurrent.futures
import time
import sys
from queue import Queue

# Set the number of threads to control the level of concurrency
NUM_THREADS = 50

# Create a queue to hold the IP addresses and ports to be scanned
scan_queue = Queue()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        result = sock.connect_ex((ip, port))
        if result == 0:
            service_name = socket.getservbyport(port)
            return ip, port, service_name  # Return the open IP address, port, and service name
        sock.close()
    except KeyboardInterrupt:
        print("Port scanning stopped.")
        exit()
    except socket.error:
        pass

def worker():
    while True:
        ip, num_ports = scan_queue.get()
        open_ports = []
        total_ports = num_ports
        scanned_ports = 0

        for port in range(1, num_ports + 1):
            open_port = scan_port(ip, port)
            if open_port is not None:
                ip, port, service_name = open_port
                open_ports.append((port, service_name))
            scanned_ports += 1
            progress = (scanned_ports / total_ports) * 100
            sys.stdout.write(f"\rScanning {ip} | Progress: {progress:.2f}% | Ports found: {len(open_ports)}")
            sys.stdout.flush()

        if open_ports:
            print(f"\n\nIP Address: {ip}")
            print("Open Ports:")
            for port, service_name in open_ports:
                print(f"   Port: {port}\tService: {service_name}")
            print()
            save_results(ip, open_ports)
        scan_queue.task_done()

def save_results(ip, open_ports):
    save_file = input("Enter 'Y' to save the results to a file, or any other key to continue: ")
    if save_file.lower() == 'y':
        file_name = f"results_{ip}.txt"
        with open(file_name, "w") as file:
            file.write(f"IP Address: {ip}\n")
            file.write("Open Ports:\n")
            for port, service_name in open_ports:
                file.write(f"   Port: {port}\tService: {service_name}\n")
        print(f"Results saved to {file_name}")

if __name__ == "__main__":
    ip = input("Enter the IP address to scan: ")
    num_ports = int(input("Enter the number of ports to scan: "))
    scan_queue.put((ip, num_ports))

    print("Starting port scanning...\n")

    start_time = time.time()

    # Create worker threads
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # Wait for all the ports to be scanned
    scan_queue.join()

    elapsed_time = time.time() - start_time
    print(f"\nPort scanning complete. Elapsed time: {elapsed_time:.2f} seconds.")

