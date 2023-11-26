import subprocess
import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import socket

import os

from data_specs import *

current_directory = os.get_cwd()
relative_path = 'captured_data'
directory_path = os.path.join(current_directory,relative_path)

# Function to start TShark capture
def start_tshark_capture(port, ip, filename):
    # filter_expression = f"tcp port {port}" # and dst {ip}"
    inter = "eno1"
    filter_expression = f"tcp and dst {ip}"

    tshark_command = [
        "tshark",
        "-i", inter,  # Replace with your network interface
        "-f", filter_expression,
        "-w", filename,
    ]
    subprocess.Popen(tshark_command)

# Function to open a website using Selenium
def open_website(port,url,t):
    # chromedriver_install_loc = "/Users/annaeaton/Downloads/chromedriver-mac-x64-119/chromedriver"
    chromedriver_install_loc = "/users/aceaton/chromedriver"
    # driver = webdriver.Chrome()  # Make sure you have the ChromeDriver executable in your PATH
    options = webdriver.ChromeOptions()
    options.add_argument(f"--remote-debugging-port={port}")
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    driver = webdriver.Chrome(options=options)#,executable_path=chromedriver_install_loc) 
    driver.get(url)
    print(f"got {url}")
    time.sleep(t)  # Wait for 10 seconds (adjust as needed)
    driver.quit()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip


def capture_site(site, number, time):
    # port_to_capture = 80  # Replace with the desired port
    port_to_capture = 8080  # Specify the desired port for TShark and Selenium

    # Get local IP address
    local_ip = get_local_ip()

    site_path = os.path.join(directory_path, str(site))
    if not os.path.exists(site_path):
        # If it doesn't exist, create the directory
        os.makedirs(site_path)
        print(f"Directory '{site_path}' created.")
    filename = relative_path+"/"+str(site)+"/"+str(site)+"_"+str(time)+"_"+str(number)+".pcap"

    # Start TShark capture in the background
    start_tshark_capture(port_to_capture,local_ip,filename)

    # Open the website in Selenium
    open_website(port_to_capture,site,time)

    # Wait for some time (adjust as needed)
    time.sleep(time)

    # Stop TShark capture (you might need to find the correct process ID)
    subprocess.run(["pkill", "tshark"])


def test():
    # specs from data_specs
    for site in websites[:3]:
        print(site)
        for i in range(samples_per_site):
            capture_site(site,i,capture_time)
            print(i)

test()
