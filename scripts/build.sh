#! /bin/bash
# docker
sudo chmod 666 /var/run/docker.sock
# export SECRET_KEY=${SECRET_KEY} 
# export DATABASE_URI=${DATABASE_URI}

docker-compose down --rmi all
docker-compose build
docker login 
docker-compose push

# docker push sch0tterfoinfoin/service1:latest
# docker push sch0tterfoinfoin/service2:latest
# docker push sch0tterfoinfoin/service3:latest
# docker push sch0tterfoinfoin/service4:latest