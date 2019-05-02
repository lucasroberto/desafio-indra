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
                bat 'pip install python-jenkins'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install virtualenv'
                bat 'virtualenv env'
                bat 'env\Scripts\activate'
                bat 'lucasroberto/desafio-indra/Hello-Desafio'
                bat 'python -m Pyautomators -f json -o ./hello-desafio.json'
            }
        }
    }
}
