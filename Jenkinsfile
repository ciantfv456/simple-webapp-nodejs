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
        script {
            try {
                stage('Run Docker') {
                    steps {
                        bat "docker run -itd -p 3000:3000 --name server server:latest"
                    }   
                }
                stage('CURL') {
                    steps {
                        bat "curl http://localhost:3000/"
                    }   
                }
            }
            finally {
                stage('Kill Docker') {
                    steps {
                        bat "docker kill server"
                        bat "docker rm server"
                    }   
                }        
            }
        }
    }
}
