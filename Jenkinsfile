pipeline {

    agent any 

    stages {

        stage('build') {

            steps {

                sh 'sam build'

            }

        }

        stage('deploy'){

            steps {

                sh 'sam deploy --stack-name sam-app -t template.yaml --resolve-s3 --region us-east-1 --capabilities CAPABILITY_IAM --confirm-changeset true --resolve-image-repos' //940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp' --s3-bucket sam-jenkins-demo-us-west-2-subhayandpwc //--no-confirm-changeset --no-fail-on-empty-changeset'

            }

        }

    }

}
