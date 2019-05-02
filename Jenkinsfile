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
                env\Scripts\activate
                cd lucasroberto/desafio-indra/Hello-Desafio
                python -m Pyautomators -f json -o .U+005Chello-desafio.json
                '''
            }
        }
    }
}
