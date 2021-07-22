pipeline {
  agent any
  stages {
    stage('push_code') {
      steps {
        bat(script: 'dir/w', returnStatus: true)
        bat(script: 'python -v', returnStatus: true)
      }
    }

  }
}