pipeline {
  agent any
  stages {
    stage('cmd') {
      steps {
        bat(script: 'po45646546', returnStatus: true, label: 'qdqdq')
        emailext(attachLog: true, subject: 'jenkins_report', body: 'build_result', to: 'misawa21@gmail.com', compressLog: true, from: 'voicetube21@gmail.com', attachmentsPattern: 'log')
      }
    }

  }
}