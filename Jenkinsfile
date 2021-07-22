pipeline {
  agent any
  stages {
    stage('push_code') {
      steps {
        bat(script: 'dir/w', returnStatus: true)
        bat(script: 'python -v', returnStatus: true)
      }
    }

    stage('send ') {
      steps {
        mail(subject: 'report', body: 'test', from: 'jenkins', to: 'misawa21@gmail.com')
      }
    }

  }
}