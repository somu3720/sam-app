pipeline {
  agent any
  stages { 
stage('sam install') {
steps {
sh 'sudo --u'
sh 'apt update'
sh 'apt install wget curl zip'
sh 'systemctl start docker'
sh 'sleep 20'
sh 'service status docker'
sh 'docker ps'
sh 'wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip'
sh 'sha256sum aws-sam-cli-linux-x86_64.zip'
sh 'unzip aws-sam-cli-linux-x86_64.zip -d sam-installation'
sh './sam-installation/install'
sh 'sam --version'
}  
} 
stage('aws cli install')
{
steps{
sh 'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'
sh 'unzip awscliv2.zip'
sh './aws/install'
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


