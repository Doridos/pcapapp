# PCAPNG Comment Tool ⚙️

This tool allows you to add and read comments in PCAPNG files. It provides a simple command-line interface for interacting with PCAPNG files.

## Features ✨

- **Add Comments**: Insert comments into specific packet within a PCAPNG file.
  - Note: When adding a comment a new PCAPNG file will be created with the comment.
- **Read Comments**: Extract comments from specific packet within a PCAPNG file.

## Requirements 📦

- Python 3.10+
- `scapy` library

## Installation 🛠️

1. Clone the repository:
    ```sh
    git clone git@github.com:Doridos/pcapapp.git
    cd pcapapp
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage 🚀

Run the script using Python:

```sh
python pcapng.py
```

### Options

1. **Add a comment to a PCAPNG file**:
    - Choose option `1`.
    - Enter the details in the format: `input_file;comment;packet_number`.

2. **Read a comment from a PCAPNG file**:
    - Choose option `2`.
    - Enter the details in the format: `input_file;packet_number`.

3. **Close the program**:
    - Choose option `q`.

### Example

For example usage there is test.pcapng file in the repository.

**Adding a comment**:
```sh
Choose an option:
1 -> Add a comment to a PCAPNG file.
2 -> Read a comment from a PCAPNG file.
q -> Close program.
Enter your choice (1 or 2 or q): 1
Enter the details in this format (semicolon-separated):
input_file;comment;packet_number
Enter details: test.pcapng;This is a test comment;3
```

**Reading a comment**:
```sh
Choose an option:
1 -> Add a comment to a PCAPNG file.
2 -> Read a comment from a PCAPNG file.
q -> Close program.
Enter your choice (1 or 2 or q): 2
Enter the details in this format (semicolon-separated):
input_file;packet_number
Enter details: test.pcapng;3
Packet Information:
{
    "packet_number": 3,
    "comment": "This is a test comment"
}
```
