pipeline {
    agent { label "windows" }
    stages {
        stage('Clean Workspace') {
            steps {
                KILL = false
                REMOVE = false
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
                REMOVE = true
                bat "docker run -itd -p 3000:3000 --name server server:latest"
                KILL = true
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
            if (env.KILL) {
                bat "docker kill server"
            }
            if (env.REMOVE) {
                bat "docker rm server"
            }
        }
    }    
}
