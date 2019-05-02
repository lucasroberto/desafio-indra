    stage ('Checkout') {
      deleteDir()
      checkout scm
    }
stage ('Build and Archive'){
    sh 'virtualenv env; cd env/Scripts/activate ; python -m Pyautomators '
    step([$class: Artifacts , artifacts: 'desafio-indra/build/outputs/apk/desaio-indra.apk'])
}
