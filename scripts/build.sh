#! /bin/bash
# docker
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
sudo docker-compose down --rmi all
sudo docker-compose build
sudo docker-compose push
docker login
docker-compose build

# docker push sch0tterfoinfoin/service1:latest
# docker push sch0tterfoinfoin/service2:latest
# docker push sch0tterfoinfoin/service3:latest
# docker push sch0tterfoinfoin/service4:latest