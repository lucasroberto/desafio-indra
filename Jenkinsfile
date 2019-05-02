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
            sh 'virutalenv env'
            sh 'cd env/Scripts/activate'
            sh 'cd lucasroberto/desafio-indra/Hello-Desafio'
            sh 'python -m Pyautomators -f json -o ./hello-desafio.json'
        }
    }
}
