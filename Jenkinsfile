pipeline {
    agent any 
    stages{
        stage('Build'){
            steps{
                sh './scripts/build.sh'
            }        
        }
        stage('Test'){
            steps{
                sh './scripts/test_services.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }
    }
                   
}