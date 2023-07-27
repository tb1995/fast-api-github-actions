#!/bin/bash

set -x

echo "starting smoke test"

container_id=$(docker ps -qf "name=fast")

if [ -z "$container_id" ]; then
    echo "fastapi container is not running"
    exit 1
fi

echo "Fastapi running with the ID: $container_id"

# get the importer container's ip addr
# container_ip=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container_id)

# get the importer container's port
container_port=$(docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}}{{(index $conf 0).HostPort}}{{end}}' $container_id)

echo "Container running on Port: $container_port"

# hit the task status endpoint, as it returns a 200 status code regardless of ID
# response=$(wget --server-response --method=GET --no-check-certificate "http://localhost:9000/api/v1/imports/1" 2>&1)
response=$(curl -s -o /dev/null -w "%{http_code}" -X GET --insecure "http://localhost:9000/")

echo "Response code: $response"
if [ "$response" -eq 200 ]; then
    echo "Fastapi container running successfully"
else
    echo "Fastapi container smoke test failed"
    exit 1
fi

