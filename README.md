# Nautobot Demo

This project demonstrates integration with [Nautobot](https://github.com/nautobot/nautobot) using Python, Ansible, and Nornir. It includes scripts and playbooks to interact with Nautobot's API and inventory.

## Contents

- `pynautobot-test.py`: Example Python script using `pynautobot` to query devices and locations from Nautobot.
- `ansible-test.yml`: Ansible playbook to retrieve and display devices from Nautobot.
- `nornir-test.py`: Example Python script using Nornir with Nautobot as the inventory source.
- `local.env`: Example environment variable file for storing Nautobot credentials and URL.

## Setup

1. **Clone the repository**  
    Navigate to the project directory:
    ```bash
    git clone <repo-url>
    cd nautobot-demo
    ```

2. **Create and activate a virtual environment**  
    (Linux example):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**  
    Install required Python packages and Ansible collections:
    ```bash
    pip install ansible ansible-dev-tools ansible-pylibssh napalm netutils pynautobot
    ansible-galaxy collection install networktocode.nautobot napalm.napalm
    ansible --version
    ```

4. **Configure environment variables**  
    Edit `local.env` with your Nautobot URL and API token:
    ```bash
    export NAUTOBOT_URL=https://your-nautobot-url
    export NAUTOBOT_TOKEN=your-nautobot-token
    ```

5. **Source the environment variables**  
    Before running scripts or playbooks:
    ```bash
    source local.env
    ```

## Usage

- **Python scripts**  
  Run the scripts after sourcing `local.env`:
  ```bash
  python pynautobot-test.py
  python nornir-test.py
  ```

- **Ansible playbook**  
  Run the playbook after sourcing `local.env`:
  ```bash
  ansible-playbook ansible-test.yml
  ```

## Requirements

- Python 3.x
- [pynautobot](https://pynautobot.readthedocs.io/)
- [Nornir](https://nornir.tech/)
- [Ansible](https://www.ansible.com/)
- Nautobot instance with API access

## Notes

- Do **not** commit sensitive information such as tokens or passwords.
- The `.gitignore` file excludes logs, environment files, and backup directories.

---
This project is for demonstration and educational purposes.