# Copyright 2022-2023 The VNET Project Authors. All Rights Reserved.

# SPDX-License-Identifier: MIT

#!/bin/bash

if [ $1 ]; then
  metatoc_webservice_host=$1
else
  metatoc_webservice_host="172.22.50.211"
fi

if [ $2 ]; then
  metatoc_webservice_port=$2
else
  metatoc_webservice_port="5000"
fi

if [ $3 ]; then
  metatoc_nats_host=$3
else
  metatoc_nats_host="172.22.50.211"
fi

metatoc_nats_port="4222"

echo "Check docker..."
docker -v
if [ $? -eq 0 ]; then
  echo "Docker installed!"
else
  echo "Docker uninstalled! Please install it. see https://www.docker.com/"
  exit 0
fi

echo "Check metatoc-client exists..."
metatoc0client_exists=$(docker image ls "meta42/metatoc-client:latest" | wc -l)
if [ $metatoc0client_exists -eq 2 ]; then
  echo "Metatoc-client exists!"
else
#  echo "Make metatoc-client..."
#  docker build --tag metatoc-client:latest ../.
  echo "Pull metatoc-client..."
  docker pull meta42/metatoc-client:latest
fi

echo "Run metatoc-client..."
docker run --rm -ti -v $PWD/../json:/json --env METATOC_WEBSERVICE_ADDRESS=$metatoc_webservice_host:$metatoc_webservice_port --env METATOC_NATS_ADDRESS=$metatoc_nats_host:$metatoc_nats_port meta42/metatoc-client:latest
