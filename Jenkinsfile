pipeline {
  agent {
          kubernetes { label 'k8s-agent'}
 
         }
  stages { 
stage('sam install') {
steps {
	container('ubuntu'){
sh 'apt-get update'
sh 'apt-get install wget curl zip'
sh 'service docker start'
sh 'sleep 20'
sh 'service docker status'
sh 'docker ps'
sh 'wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip'
sh 'sha256sum aws-sam-cli-linux-x86_64.zip'
sh 'unzip aws-sam-cli-linux-x86_64.zip -d sam-installation'
sh './sam-installation/install'
sh 'sam --version'
}
}  
}        	      
stage('build') 
	  {
            steps {
		    container('ubuntu'){ 
                sh 'sam build'
		sh 'docker images'
            }
	    }
        }
    
        stage('package'){
            steps{
		    container('ubuntu'){    
                sh 'sam package --output-template-file packaged-template.yaml --region us-east-1 --image-repository 940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp'
            }
	    }
        }
        stage('deploy'){
            steps {
		    container('ubuntu'){   
			sh 'sam deploy --template-file /var/lib/jenkins/workspace/Test-SAM/packaged-template.yaml --stack-name sam-app --no-confirm-changeset --no-fail-on-empty-changeset'// -t template.yaml --region us-east-1 --capabilities CAPABILITY_IAM --confirm-changeset true'// --resolve-image-repos' //940810086075.dkr.ecr.us-east-1.amazonaws.com/docker-lambda-testapp' --s3-bucket sam-jenkins-demo-us-west-2-subhayandpwc //--no-confirm-changeset --no-fail-on-empty-changeset'
            }
	    }
        }
    }
}
