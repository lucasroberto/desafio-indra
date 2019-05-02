pipeline{
    agent any
    
    stages('Build'){
        steps{
            echo 'Building'
            git 'https://github.com/lucasroberto/desafio-indra'
        }
    }
    stages('Test'){
        steps{
            sh 'virutalenv env'
            sh 'cd env/Scripts/activate'
            sh 'cd lucasroberto/desafio-indra/Hello-Desafio'
            sh 'python -m Pyautomators -f json -o .\hello-desafio.json'
        }
    }
