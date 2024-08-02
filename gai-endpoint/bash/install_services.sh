#!/bin/bash

# Bash script to install and enable all systemd services from a specified directory
# Defaults to a folder named 'systemd' in the current directory if no arguments are provided

# Set default directory
# Base directory where the folders are located
DEFAULT_DIR="$(pwd)/bash/systemd"

# Check if the correct number of arguments is provided
if [ "$#" -eq 1 ]; then
    SERVICES_DIR=$1
elif [ "$#" -eq 0 ]; then
    SERVICES_DIR=$DEFAULT_DIR
else
    echo "Usage: $0 [/path/to/systemd_services_directory]"
    exit 1
fi

# Check if the directory exists
if [ ! -d "$SERVICES_DIR" ]; then
    echo "Error: Directory '$SERVICES_DIR' not found."
    exit 1
fi

# Loop through all .service files in the specified directory
for SERVICE_FILE in "$SERVICES_DIR"/*.service; do
    # Check if any .service files are found
    if [ ! -e "$SERVICE_FILE" ]; then
        echo "No service files found in '$SERVICES_DIR'."
        exit 1
    fi

    # Copy the service file to the systemd directory
    sudo cp "$SERVICE_FILE" /etc/systemd/system/

    # Get the name of the service
    SERVICE_NAME=$(basename "$SERVICE_FILE")

    # Reload the systemd daemon to recognize the new service
    sudo systemctl daemon-reload

    # Enable the service to start on boot
    sudo systemctl enable "$SERVICE_NAME"

    # Start the service immediately
    sudo systemctl start "$SERVICE_NAME"

    # Restart the service to ensure it's running with the latest changes
    sudo systemctl restart "$SERVICE_NAME"

    # # Print the status of the service
    # sudo systemctl status "$SERVICE_NAME"
done

echo "All services from '$SERVICES_DIR' have been installed and started."
