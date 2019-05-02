#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/lucasroberto/desafio-indra'
            }
        }
        stage ("Test"){
            steps{
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
                bat '''
                cd hello-desafio
                python -m Pyautomators -f json -o .//hello-desafio.json
                '''
                bat '''
                cd desafio2
                python -m Pyautomators -f json -o .//desafio2.json
                '''
                bat '''
                cd enviar
                python -m Pyautomators -f json -o .//enviar.json
                '''
            }
        }
    }
}
