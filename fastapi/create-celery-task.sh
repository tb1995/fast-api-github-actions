#!/bin/bash

set -x

echo "Creating celery task"

response=$(curl -X POST -w "%{http_code}" -s -o /dev/null http://localhost:9000/tasks)

echo "Response code: $response"
if [ "$response" -eq 200 ]; then
    echo "Task created successfully"
else
    echo "Task creation failed"
    exit 1
fi

echo "TEST PASSED"