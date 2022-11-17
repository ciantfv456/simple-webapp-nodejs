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
    }
}
