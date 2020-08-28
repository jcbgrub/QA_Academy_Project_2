#! /bin/bash
ssh sfia-manager << EOF
ls
pwd
whoami
cd SFIA_Project_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF