pipeline {
    agent { label "windows" }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Git Pull') {
            steps {
                git 'https://github.com/ciantfv456/simple-webapp-nodejs.git'
            }
        }
        stage('Build') {
            steps {
                bat "npm install"
            }
        }
        stage('Run Tests') {
            steps {
                bat "npm test"
            }
        }
        stage('Build Docker') {
            steps {
                bat "docker build . -t server:latest"
            }
        }
        stage('Run Docker') {
            steps {
                bat "docker run -itd -p 3000:3000 --name node-server server:latest"
            }   
        }
        stage('CURL') {
            steps {
                bat "curl http://localhost:3000/"
            }   
        }
        stage('Kill Docker') {
            steps {
                bat "docker kill node-server"
                bat "docker rm node-server"
            }   
        }        
    }
}
