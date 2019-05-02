#!groovy
pipeline{
    agent any
    
    stage 'Build'{
        steps{
            echo 'Building'
            git 'github.com/lucasroberto/desafio-indra'
        }
    }
     stage 'Test'{
        steps{
            bat 'virutalenv env'
            bat 'cd env/Scripts/activate'
            bat 'cd lucasroberto/desafio-indra/Hello-Desafio'
            bat 'python -m Pyautomators -f json -o ./hello-desafio.json'
        }
    }
}
