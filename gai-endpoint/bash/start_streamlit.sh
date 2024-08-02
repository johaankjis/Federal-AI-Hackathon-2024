#!/bin/bash

# Usage function
usage() {
  echo "Usage: $0 -d <project_dir> -a <application_path> -p <port> -u <url_path>"
  exit 1
}

# Parse command-line arguments
while getopts ":d:a:p:u:" opt; do
  case $opt in
    d) PROJECT_DIR="$OPTARG"
    ;;
    a) APPLICATION_PATH="$OPTARG"
    ;;
    p) PORT="$OPTARG"
    ;;
    u) URL_PATH="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
        usage
    ;;
  esac
done

# Check if all arguments are provided
if [ -z "$PROJECT_DIR" ] || [ -z "$APPLICATION_PATH" ] || [ -z "$PORT" ] || [ -z "$URL_PATH" ]; then
    usage
fi

# Resolve the full path to the application
FULL_APPLICATION_PATH="$PROJECT_DIR/$APPLICATION_PATH"

# Get the Python executable from pipenv
PYTHON_EXEC_PATH=$(which python)

echo "PROJECT_DIR $PROJECT_DIR"
echo "APPLICATION_PATH $FULL_APPLICATION_PATH"
echo "PORT $PORT"
echo "URL_PATH $URL_PATH"
echo "PYTHON_EXEC_PATH $PYTHON_EXEC_PATH"

export PYTHONPATH=$PYTHONPATH:$PROJECT_DIR



START_COMMAND="streamlit run $FULL_APPLICATION_PATH --server.port $PORT --browser.gatherUsageStats false --server.baseUrlPath $URL_PATH --ui.hideTopBar false"



bash -c "$START_COMMAND"

