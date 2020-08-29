#! /bin/bash
ssh sfia-manager << EOF
git clone https://github.com/jcbgrub/SFIA_Project_2.git
cd SFIA_Project_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
# docker stack rm sfia2
docker stack deploy --compose-file docker-compose.yaml sfia2
docker service ls
cd .. 
sleep 5
rm -r SFIA_Project_2/
EOF