pipeline {
    agent { any { image 'public.ecr.aws/lambda/python:3.9' } }
    stages {
        stage('build') {
            steps {
                sh 'sam build'
                sh 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}
