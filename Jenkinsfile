pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'pytest', returnStatus: true)
      }
    }

  }
}