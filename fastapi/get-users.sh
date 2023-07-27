#!/bin/bash


# Make a GET request to the /users endpoint and capture the HTTP status code and response data
response=$(curl -X GET -w "%{http_code}" http://localhost:9000/users)

# Extract the status code from the response using grep
status_code=$(echo "$response" | grep -oE '[0-9]+$')

# Extract the response data from the response (excluding the status code)
response_data=$(echo "$response" | sed 's/[0-9]\{3\}$//')

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
    echo "Status code: 200 OK"
else
    echo "Status code: $status_code"
    echo "Failed to get a successful response. Exiting."
    exit 1
fi

# Check if the response data is not empty
if [ -z "$response_data" ]; then
    echo "Response data is empty. Exiting."
    exit 1
fi

# If both checks pass, print the response data
echo "Response data:"
echo "$response_data"
echo "TEST PASSED"