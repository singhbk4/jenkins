pipeline {
  agent any
  stages {
    stage ('DataUpdate') {
      steps {
        script {
                sh 'cte.py'
        }
      }
    }
     stage ('build') {
      steps {
        script {
                sh 'main_script.py'
            }
          }
        }
      }
    }
