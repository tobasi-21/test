pipeline {
  agent any
  stages {
    stage('run') {
      steps {
        build(job: 'python_test', quietPeriod: 1)
      }
    }

  }
}