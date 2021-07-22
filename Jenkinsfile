pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'pytest 9.py exit 0', returnStatus: true)
      }
    }

  }
}