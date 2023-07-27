#!/bin/bash

set -x

echo "Inserting users"

response=$(curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe"}'  -w "%{http_code}" -s -o /dev/null http://localhost:9000/users)

echo "Response code: $response"
if [ "$response" -eq 200 ]; then
    echo "User created successfully"
else
    echo "Failed to create user"
    exit 1
fi

echo "TEST PASSED"