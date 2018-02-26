#!/bin/sh

curl --data "present=lahja3" --data send="send" localhost:5000
curl --data "present=" --data send="send" localhost:5000
curl --data "" --data send="send" localhost:5000
