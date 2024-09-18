#!/bin/bash

read -p "Token: " CHAT_TOKEN
read -p "Query: " CHAT_QUERY

curl -X 'POST' \
  'http://localhost:8000/api/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "x-token: $CHAT_TOKEN" \
  -N \
  -d "{ \"query\": \"$CHAT_QUERY\" }"
