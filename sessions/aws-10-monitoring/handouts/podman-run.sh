#!/bin/bash

# remove old stuff
set +e # keep running if there are errors
podman stop grafana data_source || echo "no containers to remove"
podman rm grafana data_source || echo "no containers to remove"
set -e

# Remove any previous volumes
podman volume rm $(podman volume ls -qf dangling=true)

# Remove all unused containers, networks, images (both dangling and unused), anonymous volumes
podman system prune -f

# Create bridge network
podman network create monitoring_network

python3 replace_cniVersion.py ~/.config/cni/net.d/databases_network.conflist

# Run grafana container with network alias name "grafana"
podman run -d \
  --name grafana \
  --network monitoring_network \
  -p 3000:3000 \
  -v grafana:/var/lib/grafana \
  docker.io/grafana/grafana:latest

# build data source image containing python code
podman build -t data_source_image .

# Run flask data source container with network alias name "data_source"
podman run -d \
  --name data_source \
  --network monitoring_network \
  -p 5000:5000 \
  -v ./app.py:/app/app.py \
  data_source_image

sleep 2
podman ps -a
