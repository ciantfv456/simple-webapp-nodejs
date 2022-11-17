pipeline {
    agent { label "windows" }
    environment {
        KILL = false
        REMOVE = false
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
                echo $name
            }
        }
        stage('Build Docker') {
            steps {
                bat "docker build . -t server:latest"
            }
        }
        
        stage('Run Docker') {
            environment {
                REMOVE = true
            }
            steps {                
                bat "docker run -itd -p 3000:3000 --name server server:latest"                
            }   
            environment {
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
        when {
          expression {
            env.KILL == true 
          }
        }
        steps {
            bat "docker kill server"
        }
        when {
          expression {
            env.KILL == true 
          }
        }
        steps {            
            bat "docker rm server"
        }
    }    
}
