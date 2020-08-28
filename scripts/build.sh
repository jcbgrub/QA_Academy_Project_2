#! /bin/bash
# docker
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
sudo docker-compose down --rmi all
sudo docker-compose build
sudo docker-compose push

