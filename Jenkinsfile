pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'py.test 9.py -s  --alluredir C:\\Users\\tobasi\\Downloads\\allure-2.14.0\\allure-2.14.0\\reports', returnStatus: true)
        bat(script: 'exit 0', returnStatus: true)
      }
    }

  }
}