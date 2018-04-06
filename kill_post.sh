#!/usr/bin/env bash
sudo kill -9 $(lsof -t -i:8000)