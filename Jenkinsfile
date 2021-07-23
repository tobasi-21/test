pipeline {
  agent any
  stages {
<<<<<<< HEAD
<<<<<<< HEAD
    stage('') {
=======
    stage('checkout') {
>>>>>>> 1138ffb (Added Jenkinsfile)
      steps {
        bat(script: 'dir/w', returnStatus: true)
=======
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
<<<<<<< HEAD
>>>>>>> 01982bcc694fbd5c429b0b1cdf33718a78ad878b
=======
>>>>>>> 1138ffb (Added Jenkinsfile)
      }
    }

  }
}