pipeline {
  agent any
  stages {
    stage('push_code') {
      steps {
        bat(script: 'dir/w', returnStatus: true)
        bat(script: 'python -v', returnStatus: true)
      }
    }

    stage('mail') {
      steps {
        mail(subject: 'report', body: 'report', to: 'voicetube21@gmail.com')
      }
    }

  }
}