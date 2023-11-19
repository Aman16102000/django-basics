#!/usr/bin/env groovy

pipeline {

    agent {
        docker{
            image 'ubuntu'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'df -h'
            }
        }
        
    }
}