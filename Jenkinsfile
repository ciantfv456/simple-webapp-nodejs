pipeline {
    agent { label "windows" }
    def killContainer = false
    def removeContainer = false
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
        stage('Say My Name') {
            steps {
                echo $name
            }
        }
        stage('Build Docker') {
            steps {
                bat "docker build . -t server:latest"
            }
        }
        stage('Run Docker') {
            steps {
                removeContainer = true
                bat "docker run -itd -p 3000:3000 --name server server:latest"
                killContainer = true
            }   
        }
        stage('run tests') {
            steps {
                bat "curl http://localhost:3000/"
                bat "python test.py"
            }   
        }
    }
    post { 
        always { 
            if (killContainer) {
                bat "docker kill server"
            }
            if (removeContainer) {
                bat "docker rm server"
            }
        }
    }    
}
