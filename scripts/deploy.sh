#! /bin/bash
ssh sfia-manager << EOF
sudo chmod 666 /var/run/docker.sock
cd SFIA-PROJECT_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF