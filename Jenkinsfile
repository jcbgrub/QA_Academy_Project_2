pipeline {
    agent any 
    stages{
        stage('Configure'){
            steps{
                sh './scripts/configure.sh'
            }
        }
        stage('Test'){
            steps{
                sh './scripts/test.sh'
            }
        }
        stage('Build'){
            steps{
                sh './scripts/build.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/deploy.sh'
            }
        }                   
    }
}