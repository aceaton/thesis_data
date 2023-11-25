import os
import pyshark
import matplotlib.pyplot as plt
from datetime import datetime

# Specify the directory containing the PCAP files
pcap_directory = './pcaps/'

# Create a function to plot packet time distribution and save it
def plot_packet_time_distribution(pcap_file):

    # Open the PCAP file using pyshark
    capture = pyshark.FileCapture(pcap_file, keep_packets=False)

    # Initialize a list to collect packet timestamps
    packet_times = []

    # Iterate through packets and collect their timestamps
    for packet in capture:
        # timestamp = datetime.fromtimestamp(float(packet.sniff_time))
        packet_times.append(float(packet.sniff_time.timestamp()))
    
# # Extract timestamps from packets
# for packet in cap:
#     timestamps.append(float(packet.sniff_time.timestamp()))

    # Create a histogram of packet timestamps
    plt.hist(packet_times, bins=50)
    plt.title(f'Packet Time Distribution for {pcap_file}')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Create a folder with the same name as the PCAP file
    pcap_file_name = os.path.splitext(os.path.basename(pcap_file))[0]
    output_folder = os.path.join(pcap_directory, 'time_graphs')
    os.makedirs(output_folder, exist_ok=True)

    # Save the plot in the folder
    plot_file_name = os.path.join(output_folder, f'{pcap_file_name}.png')
    plt.savefig(plot_file_name)
    plt.close()

# Iterate through PCAP files in the directory
# for root, _, files in os.walk(pcap_directory):
#     for file in files:
#         if file.endswith('.pcap'):
#             pcap_file_path = os.path.join(root, file)
#             print(pcap_file_path)
#             plot_packet_time_distribution(pcap_file_path)
#             print(f'Processed: {pcap_file_path}')
