pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'py.test 9.py -s  -v --alluredir  reports && exit 0', returnStatus: true)
      }
    }

  }
}