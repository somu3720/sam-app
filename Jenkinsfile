pipeline {
  agent {
          kubernetes { label 'testpod-ubuntu'}
 
         }
  stages { 
	stage('Environment Setup') { 
steps {
sh 'apt-get --allow-releaseinfo-change update'
sh 'apt-get install -y apt-transport-https software-properties-common gnupg2 wget net-tools unzip lsb-release iptables'
sh 'apt-get install -y ca-certificates curl'
sh 'whoami'
sh 'groupadd docker'
sh 'usermod -aG docker root'
sh 'uname -a'
sh 'lsb_release -cs'
sh 'apt-get list | grep docker-ce'
}
}
stage('Docker install') {
steps {
sh 'wget https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce-cli_19.03.11~3-0~debian-buster_amd64.deb'
sh 'wget https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/containerd.io_1.3.7-1_amd64.deb'
sh 'wget https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce_19.03.11~3-0~debian-buster_amd64.deb'
sh 'dpkg -i containerd.io_1.3.7-1_amd64.deb docker-ce-cli_19.03.11~3-0~debian-buster_amd64.deb'
sh 'dpkg -i docker-ce_19.03.11~3-0~debian-buster_amd64.deb'
sh 'apt-get install -f'
sh 'service start docker'
sh 'docker version'
sh 'docker info'
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
