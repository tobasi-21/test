pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        bat 'py.test 9.py -s  -v --alluredir  reports'
      }
    }

  }
}