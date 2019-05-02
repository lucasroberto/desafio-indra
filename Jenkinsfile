    stage ('Checkout') {
      deleteDir()
      checkout scm
    }
  
stage 'Build and Archive'
 node('slave') {
    bat 'export virtualenv env'
 }

