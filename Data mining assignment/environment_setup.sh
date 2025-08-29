#!/bin/bash

# Required Python version
REQUIRED_PYTHON_VERSION="3.12.6"

# Check if python or python3 is available and get the version
PYTHON_VERSION=$(command -v python &>/dev/null && python --version 2>&1 | awk '{print $2}' || python3 --version 2>&1 | awk '{print $2}')

if [ -z "$PYTHON_VERSION" ]; then
    echo "Error: Python is not installed."
    exit 1
fi

if [ "$PYTHON_VERSION" != "$REQUIRED_PYTHON_VERSION" ]; then
    echo "Warning: Python version mismatch. Required: $REQUIRED_PYTHON_VERSION, Found: $PYTHON_VERSION"
else
    echo "Python version matches: $PYTHON_VERSION"
fi

# List of required Python libraries with specific versions
REQUIRED_LIBRARIES=(
    "numpy"
    "pandas"
    "scipy"
    "statsmodels"
    "tabular"
    "matplotlib"
    "pickleshare==0.7.5"
)

# Install each library
for LIBRARY in "${REQUIRED_LIBRARIES[@]}"; do
    pip install "$LIBRARY"
    if [ $? -ne 0 ]; then
        echo "Error installing $LIBRARY"
        exit 1
    fi
done

echo "All required libraries have been installed successfully."
