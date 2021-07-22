pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'pytest 9.py', returnStatus: true)
        bat(script: 'exit 0', returnStatus: true)
      }
    }

  }
}