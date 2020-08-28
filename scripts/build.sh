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
sudo docker push sch0tterfoinfoin/service1:latest
docker push sch0tterfoinfoin/service2:latest
docker push sch0tterfoinfoin/service3:latest
docker push sch0tterfoinfoin/service4:latest