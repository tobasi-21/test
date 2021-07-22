pipeline {
  agent any
  stages {
    stage('cmd') {
      steps {
        bat(script: 'po', returnStatus: true, returnStdout: true)
      }
    }

  }
}