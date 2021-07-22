pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'py.test 9.py -s  --alluredir reports', returnStatus: true)
        bat(script: 'exit 0', returnStatus: true)
      }
    }

  }
}