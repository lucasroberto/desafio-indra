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
                bat 'virutalenv env'
                bat 'cd env/Scripts/activate'
                bat 'cd lucasroberto/desafio-indra/Hello-Desafio'
                bat 'python -m Pyautomators -f json -o ./hello-desafio.json'
            }
        }
    }
}
