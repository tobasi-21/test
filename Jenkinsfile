pipeline {
  agent any
  stages {
    stage('push_code') {
      parallel {
        stage('push_code') {
          steps {
            bat(script: 'dir/w', returnStatus: true)
          }
        }

        stage('') {
          steps {
            git(url: 'https://@github.com/tobasi-21/test.git', branch: 'tobasi-21 / test', changelog: true)
          }
        }

      }
    }

  }
}