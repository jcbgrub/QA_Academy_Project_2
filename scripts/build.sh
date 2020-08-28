#!/bin/sh
# make sure ~/.local/bin exists and is on your PATH
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
# install ansible with pip
pip3 install --user ansible
ansible-playbook -i inventory ansible/playbook.yaml
# docker
sudo docker-compose down --rmi all
sudo docker-compose build
sudo docker-compose push