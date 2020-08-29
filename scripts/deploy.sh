#! /bin/bash
# SSH to the manager, clone GIT hub, export environment variables, deploy docker stock and remove git repo afterwards
ssh sfia-manager << EOF
pwd
git clone https://github.com/jcbgrub/SFIA_Project_2.git
cd SFIA_Project_2/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
docker service ls
cd .. 
rm -r SFIA_Project_2/
EOF