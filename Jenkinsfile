pipeline {
  agent any
  stages { 
stage('sam install') {
steps {
sh 'sudo su'
sh 'sudo apt-get update'
sh 'sudo apt-get install -y wget curl zip'
sh 'sudo systemctl start docker'
sh 'sleep 20'
sh 'sudo systemctl status docker'
sh 'docker ps'
sh 'wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip'
sh 'sha256sum aws-sam-cli-linux-x86_64.zip'
sh 'sudo ./sam-installation/install --update'
sh 'sam --version'
}  
} 
stage('aws cli install')
{
steps{
sh 'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'
sh 'sudo ./aws/install --update'
}
}	  

stage('build') 
	  {
            steps {
                sh 'sam build'
		sh 'docker images'
            }
	  }
        stage('package'){
            steps{  
                withCredentials([[
    $class: 'AmazonWebServicesCredentialsBinding',
    credentialsId: "AWS-Access",
    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
]]) {
    sh 'sam package --output-template-file packaged-template.yaml --region us-east-1 --image-repository 940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp'
}
            }
	}
        stage('deploy'){
            steps {  
		withCredentials([[
    $class: 'AmazonWebServicesCredentialsBinding',
    credentialsId: "AWS-Access",
    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
]]) {
	sh 'sam deploy --template-file /var/lib/jenkins/workspace/Test-SAM/packaged-template.yaml --stack-name sam-app --no-confirm-changeset --no-fail-on-empty-changeset'// -t template.yaml --region us-east-1 --capabilities CAPABILITY_IAM --confirm-changeset true'// --resolve-image-repos' //940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp' --s3-bucket sam-jenkins-demo-us-west-2-subhayandpwc //--no-confirm-changeset --no-fail-on-empty-changeset'
             
}
             }
	    }
          }
	}


