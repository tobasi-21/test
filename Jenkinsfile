pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat(script: 'exit 0', returnStatus: true)
      }
    }

    stage('test') {
      steps {
        build(job: 'python_test', propagate: true)
      }
    }

    stage('qa') {
      steps {
        input(message: 'Is ok', ok: 'go~!!', submitter: 'admin')
      }
    }

  }
}