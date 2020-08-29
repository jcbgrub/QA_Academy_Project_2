#! /bin/bash
ssh sfia-manager << EOF
git clone https://github.com/jcbgrub/SFIA_Project_2.git
cd SFIA_Project_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
# docker stack rm sfia2
docker pull sch0tterfoinfoin/service1:latest
docker pull sch0tterfoinfoin/service2:latest
docker pull sch0tterfoinfoin/service3:latest
docker pull sch0tterfoinfoin/service4:latest
docker stack deploy --compose-file docker-compose.yaml sfia2
docker service ls
cd .. 
sleep 5
rm -r SFIA_Project_2/
EOF