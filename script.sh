#!/bin/bash

docker build -t server-http .

# docker tag server-http:latest your-remote-repository/your-app-image:tag
# docker push your-remote-repository/your-app-image:tag

helm install http-server web-server-0.1.0.tgz