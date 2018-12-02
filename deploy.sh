#!/bin/bash

git checkout master
git checkout .
git pull

export PROJECT_ID="$(gcloud config get-value project -q)"

docker build -t gcr.io/${PROJECT_ID}/nginx:latest ./nginx/ -f ./nginx/Dockerfile.live
docker build -t gcr.io/${PROJECT_ID}/nodejs:latest ./nodejs/ -f ./nodejs/Dockerfile
docker build -t gcr.io/${PROJECT_ID}/python:latest ./python/ -f ./python/Dockerfile

docker push gcr.io/${PROJECT_ID}/nginx:latest
docker push gcr.io/${PROJECT_ID}/nodejs:latest
docker push gcr.io/${PROJECT_ID}/python:latest

kubectl apply -f ./nginx/mps-backend-nginx-deployment.yaml
kubectl apply -f ./nodejs/mps-backend-nodejs-deployment.yaml
kubectl apply -f ./python/mps-backend-python-deployment.yaml

kubectl patch deployment mps-backend-nginx -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"
kubectl patch deployment mps-backend-nodejs -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"
kubectl patch deployment mps-backend-python -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"