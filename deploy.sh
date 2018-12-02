#!/bin/bash

git checkout master
git checkout .
git pull

export PROJECT_ID="$(gcloud config get-value project -q)"

docker build -t gcr.io/${PROJECT_ID}/nginx:latest ./mps-project2-backend/nginx/ -f ./mps-project2-backend/nginx/Dockerfile.live
docker build -t gcr.io/${PROJECT_ID}/nodejs:latest ./mps-project2-backend/nodejs/ -f ./mps-project2-backend/nodejs/Dockerfile
docker build -t gcr.io/${PROJECT_ID}/python:latest ./mps-project2-backend/python/ -f ./mps-project2-backend/python/Dockerfile

docker push gcr.io/${PROJECT_ID}/nginx:latest
docker push gcr.io/${PROJECT_ID}/nodejs:latest
docker push gcr.io/${PROJECT_ID}/python:latest

kubectl apply -f ./mps-project2-backend/nginx/mps-backend-nginx-deployment.yaml
kubectl apply -f ./mps-project2-backend/nodejs/mps-backend-nodejs-deployment.yaml
kubectl apply -f ./mps-project2-backend/python/mps-backend-python-deployment.yaml

kubectl patch deployment mps-backend-nginx -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"
kubectl patch deployment mps-backend-nodejs -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"
kubectl patch deployment mps-backend-python -p "{\"spec\":{\"template\":{\"metadata\":{\"labels\":{\"date\":\"`date +'%s'`\"}}}}}"