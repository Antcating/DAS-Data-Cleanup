# DAS-Febus-Cleanup

This project is a Python script designed to clean up old files from a specified directory. It is an addition for the project DAS-Febus-Concat and specifically written to work with it.

## Table of Contents
- [DAS-Febus-Cleanup](#das-febus-cleanup)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
      - [Python](#python)
      - [Bash](#bash)
      - [Systemd Service and Timer](#systemd-service-and-timer)

## Description

The script scans each directory within a specified path. If a directory is older than 3 days and contains a file named ".completed", the script deletes the directory and its contents. If a directory is not old enough or does not contain the ".completed" file, it is skipped. A warning is issued if the ".completed" file is not found.



## Getting Started

### Installation

To use this script, follow the steps below:

1. Clone the repository to your local machine:
    ```shell
    git clone https://github.com/Antcating/DAS-Febus-Cleanup.git
    ```

2. Navigate to the project directory:
    ```shell
    cd DAS-Febus-Cleanup
    ```

3. Create and activate a virtual environment:
    ```shell
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

### Usage

1. Open the `config.py` file and set the `LOCAL_PATH` variable to the directory you want to clean up.

#### Python

2. Activate a virtual environment:
    ```shell
    source .venv/bin/activate
    ```

3. Run the script:
    ```shell
    python3 main.py
    ```

#### Bash

2. You can run the script using the `clean.sh` bash file. Set the `PROJECT_PATH` variable in `clean.sh` to the absolute PATH to this project, and then execute the bash file:
    ```shell
    bash clean.sh
    ```

#### Systemd Service and Timer

2. Alternatively, you can use the systemd service and timer provided in the `systemd` directory of this project. Follow these steps:

   - Copy the `FebusCleanDaily.service` and `FebusCleanDaily.timer` files to the appropriate systemd directory (e.g., `/etc/systemd/system/`).
   - Edit the `FebusCleanDaily.service` file and set the `ExecStart` path to the absolute path of the `clean.sh` script.
   - Edit the `FebusCleanDaily.timer` file and set the desired interval for running the cleanup script.
   - Enable and start the timer:
     ```shell
     sudo systemctl enable cleanup.timer
     sudo systemctl start cleanup.timer
     ```

   The systemd timer will automatically execute the cleanup script at the specified interval.
