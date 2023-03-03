pipeline {
  agent {
          kubernetes { label 'testpod-ubuntu'}
 
         }
  stages { 
	stage('Environment Setup') { 
steps {
sh 'apt-get --allow-releaseinfo-change update'
sh 'apt-get install -y apt-transport-https software-properties-common gnupg2 wget net-tools unzip lsb-release'
sh 'apt-get install -y ca-certificates curl'
sh 'whoami'
sh 'groupadd docker'
sh 'usermod -aG docker root'
sh 'uname -a'
sh 'lsb_release -cs'	
}
}
stage('Docker install') {
steps {
sh 'mkdir -m 0755 -p /etc/apt/keyrings'
sh 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg'
sh 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null'	
sh 'chmod a+r /etc/apt/keyrings/docker.gpg'
sh 'apt-cache madison docker-ce'
}
}
stage('sam install') {
steps {
sh 'wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip'
sh 'sha256sum aws-sam-cli-linux-x86_64.zip'
sh 'unzip aws-sam-cli-linux-x86_64.zip -d sam-installation'
sh './sam-installation/install'
sh 'sam --version'
}
}  
         	      
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
