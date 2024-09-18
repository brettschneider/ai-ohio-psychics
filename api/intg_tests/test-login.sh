#!/bin/bash

read -p "Username: " LOGIN_USERNAME
read -p "Password: " LOGIN_PASSWORD

curl -X 'POST' \
  'http://localhost:8000/api/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -N \
  -d "{ \"username\": \"$LOGIN_USERNAME\", \"password\": \"$LOGIN_PASSWORD\" }"
