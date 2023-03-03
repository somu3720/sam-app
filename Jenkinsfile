pipeline {
  agent {
          kubernetes { label 'testpod-ubuntu'}
 
         }
  stages { 
       stage('sam install') {
            steps {
                sh 'whoami'
                sh 'apt-get --allow-releaseinfo-change update'
                sh 'apt-get install wget'
                sh 'wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip'
                sh 'sha256sum aws-sam-cli-linux-x86_64.zip'
                sh 'apt-get install unzip'
                sh 'unzip aws-sam-cli-linux-x86_64.zip -d sam-installation'
                sh './sam-installation/install'
                sh 'sam --version'
            }
      }
    
      stage('Docker install') {
                steps {
                    sh 'apt-get install -y apt-transport-https ca-certificates  software-properties-common curl  gnupg2'
                    sh 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -'  
                    sh 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"'
                    sh 'apt-cache policy docker-ce'
                    sh 'groupadd docker'
                    sh 'usermod -aG docker root'
                    sh 'apt-get install -y docker.io'
                    sh 'echo "{    "storage-driver": "aufs" } " >> /etc/docker/daemon.json'
                    sh 'cat /etc/docker/daemon.json'
                    sh 'service docker start'
                    sh 'service docker status'
                    sh 'pwd'
                    sh 'ps -aux | grep dockerd'
                    sh 'docker ps'
                     
                    
 
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
