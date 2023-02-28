pipeline {
    agent kubernetes
    stages {
        stage('build') {
            steps {
                sh 'sam build'
            }
        }
        stage('package'){
            steps{
                sh 'sam package --output-template-file packaged-template.yaml --image-repository 940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp'
            }
        }
        stage('deploy'){
            steps {
                sh 'sam deploy --template-file /var/lib/jenkins/workspace/AWS-SAM/packaged-template.yaml --stack-name sam-app --no-confirm-changeset --no-fail-on-empty-changeset'// -t template.yaml --region us-east-1 --capabilities CAPABILITY_IAM --confirm-changeset true'// --resolve-image-repos' //940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp' --s3-bucket sam-jenkins-demo-us-west-2-subhayandpwc //--no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }
    }
}
