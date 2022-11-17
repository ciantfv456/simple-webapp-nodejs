@Library('my-library@main') _
pipeline {
    agent { label "windows" }
    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    KILL = "false"
                    REMOVE = "false"
                }
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
                script {
                    ciConfig = readYaml(text: libraryResource('environments.yml'))    
                }
                echo "${name}"                
                echo "${ciConfig.buildImage}"
            }
        }
        stage('Build Docker') {
            steps {
                dockerBuild(context: '.', tag: 'latest')
            }
        }
        
        stage('Run Docker') {
            steps {          
                script {
                    REMOVE = "true"
                }                
                bat "docker run -itd -p 3000:3000 --name server server:latest"                
                script {
                    KILL = "true"
                }    
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
            script {
                if (KILL == "true") {
                    bat "docker kill server"
                }
                if (REMOVE == "true") {
                    bat "docker rm server"
                }                         
            }
        }    
    }
}
