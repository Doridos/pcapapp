import os
import json
import sys

from datetime import datetime
from scapy.all import PcapNgReader, PcapNgWriter

def add_comment_to_pcapng(file_path, comment, packet_number):
    """
    Adds a comment to a specific packet in a PCAPNG file in-place.

    Args:
        file_path (str): Path to the PCAPNG file.
        comment (str): Text of the comment to add.
        packet_number (int): Index of the packet to add the comment to (1-based index).
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_base, file_ext = os.path.splitext(file_path)

        output_file = f"{file_base}_modified_{current_time}{file_ext}"

        with PcapNgReader(file_path) as reader, PcapNgWriter(output_file) as writer:
            packets = list(reader)
            if packet_number > len(packets) or packet_number < 1:
                os.remove(output_file)
                return print("Error: Packet number out of range")
            for i, packet in enumerate(packets):
                if i+1 == packet_number:
                    packet.comment = comment
                writer.write(packet)

        print(f"Comment added to packet {packet_number} and saved to {output_file}.")

    except Exception as e:
        print(f"Error adding comment: {e}")


def read_comment_from_pcapng(input_file, packet_number):
    """
    Reads a comment from a specific packet in a PCAPNG file.

    Args:
        input_file (str): Path to the PCAPNG file.
        packet_number (int): Index of the packet to read the comment from (1-based index).

    Returns:
        str: JSON text containing the packet number and comment.
    """
    try:
        with PcapNgReader(input_file) as reader:
            packets = list(reader)

        if packet_number > len(packets) or packet_number < 1:
            return  "\n" + json.dumps({"error": "Packet number out of range"}) + "\n"

        packet = packets[packet_number - 1]
        comment_bytes = getattr(packet, "comment", None)
        if comment_bytes:
            comment = comment_bytes.decode('utf-8')
        else:
            comment = ""

        result = {
            "packet_number": packet_number,
            "comment": comment,
        }
        return "\n" + json.dumps(result, indent=4) + "\n"
    except Exception as e:
        return json.dumps({"error": str(e)})

def main():
    """
    Main function to control user input and flow for reading or adding comments to PCAPNG files.
    """
    print("Choose an option:")
    print("1 -> Add a comment to a PCAPNG file.")
    print("2 -> Read a comment from a PCAPNG file.")
    print("q -> Close program.")
    choice = input("Enter your choice (1 or 2 o q): ").strip()

    if choice == "1":
        print("Enter the details in this format (semicolon-separated):")
        print("input_file;comment;packet_number")
        user_input = input("Enter details: ").strip()
        try:
            input_file, comment, packet_number = user_input.split(";")
            packet_number = int(packet_number)
            add_comment_to_pcapng(input_file, comment, packet_number)

        except ValueError:
            print("Invalid input. Please ensure the details are correctly formatted.", file=sys.stderr)

    elif choice == "2":
        print("Enter the details in this format (semicolon-separated):")
        print("input_file;packet_number")
        user_input = input("Enter details: ").strip()
        try:
            input_file, packet_number = user_input.split(";")
            packet_number = int(packet_number)
            result_json = read_comment_from_pcapng(input_file, packet_number)
            print("Packet Information:")
            print(result_json)
        except ValueError:
            print("Invalid input. Please ensure the details are correctly formatted.", file=sys.stderr)

    elif choice == "q":
        exit()
    else:
        print("Invalid choice. Please enter 1 or 2 or q.", file=sys.stderr)

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    main()

