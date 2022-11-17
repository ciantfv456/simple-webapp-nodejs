pipeline {
    agent { label "windows" }
    environment {
        env.KILL = false
        env.REMOVE = false
    }
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
                echo "${name}"
            }
        }
        stage('Build Docker') {
            steps {
                bat "docker build . -t server:latest"
            }
        }
        
        stage('Run Docker') {
            environment {
                env.REMOVE = true
            }
            steps {                
                bat "docker run -itd -p 3000:3000 --name server server:latest"                
            }               
        }
        
        stage('run tests') {
            environment {
                env.KILL = true
            }
            steps {
                bat "curl http://localhost:3000/"
                bat "python test.py"
            }   
        }
    }
    post { 
        always {          
            script {
                if (env.KILL == true) {
                    bat "docker kill server"
                }
                if (env.REMOVE == true) {
                    bat "docker rm server"
                }                         
            }
        }    
    }
}
