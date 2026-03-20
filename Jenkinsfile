pipeline{
    agent any
    environment{
    DOCKERHUB_CREDENTIALS = 'dockerhub-cred-id'
        DOCKERHUB_REPO = 'santhosh0476'
    }
    stages{
        stage('clone repo'){
            steps{
               git branch: 'main', url: 'https://github.com/santhoshmanoharan04/voting-app.git'
            }
        }
        stage('build image'){
            steps{
                sh '''
                docker build -t santhosh0476/vote-app ./vote
                docker build -t santhosh0476/worker ./worker
                docker build -t santhosh0476/result-app ./result
                '''
            }
        }
        stage('login to docker'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: "$DOCKERHUB_CREDENTIALS",
                    usernameVariable: 'santhosh0476',
                    passwordVariable: 'praba200404'

                )]){
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }

            }
        }
        stage('push image'){
            steps{
                sh '''
                docker push santhosh0476/vote-app
                docker push santhosh0476/worker
                docker push santhosh0476/result-app
                '''
            }
        }
        stage('Deploy to Kubernetes'){
           steps{
            sh 'kubectl apply -f k8s/'
           }
        }
    }
    post {
        success {
            echo '✅ Deployment Successful 🚀'
        }
        failure {
            echo '❌ Deployment Failed'
        }
    }

}
