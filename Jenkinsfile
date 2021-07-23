pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        bat(script: 'win.bat', returnStatus: true)
        build(job: 'python_test', quietPeriod: 1)
      }
    }

  }
}