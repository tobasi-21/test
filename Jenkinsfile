pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        bat(script: 'exit 0', returnStatus: true)
      }
    }

    stage('test') {
      steps {
        bat(script: 'py.test 9.py -s  -v --alluredir  reports', returnStatus: true)
      }
    }

    stage('QA check') {
      steps {
        input(message: 'Is ok?', ok: 'go~!!', submitter: 'admin')
      }
    }

  }
}