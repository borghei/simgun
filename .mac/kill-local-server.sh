#!/bin/bash

sudo lsof -t -i tcp:8000 | xargs kill -9