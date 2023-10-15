import subprocess
import re
import os


def run_slither(command):
    try:
        result = subprocess.run(
            command, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command {' '.join(command)} failed with error:\n{e.stderr}"
    except Exception as e:
        return f"An error occurred: {e}"


def process_vulnerabilities(file_name):
    # List of commands to run
    commands = [
        ['solc-select', 'install', '0.8.4'],
        ['solc-select', 'use', '0.8.4'],
        ['slither', file_name, '--checklist']
    ]

    result = ""
    for cmd in commands:
        result += run_slither(cmd)  # Accumulate the Slither output

    # Create the slither_results folder if it doesn't exist
    result_dir = "slither_results"
    os.makedirs(result_dir, exist_ok=True)

    # Save the Slither result to a file in the slither_results folder
    result_file_path = os.path.join(result_dir, "result.md")
    with open(result_file_path, "w") as result_file:
        result_file.write(result)

    # Find and extract lines with "Reference:" and the part after '#' on each line
    vulnerabilitieNames = re.findall(r'Reference:.*?#(.*?)\s', result)
    return vulnerabilitieNames
