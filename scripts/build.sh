#! /bin/bash
# docker
# sudo chmod 666 /var/run/docker.sock
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI}
export TEST_SECRET_KEY=${TEST_SECRET_KEY} 
export TEST_DATABASE_URI=${TEST_DATABASE_URI}

docker-compose down --rmi all
docker-compose build
sudo docker login 
docker-compose push
