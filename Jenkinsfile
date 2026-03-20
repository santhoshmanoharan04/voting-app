pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-cred-id'
        DOCKERHUB_REPO = 'santhosh0476'
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/santhoshmanoharan04/voting-app.git'
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                docker build -t $DOCKERHUB_REPO/vote-app ./vote
                docker build -t $DOCKERHUB_REPO/worker ./worker
                docker build -t $DOCKERHUB_REPO/result-app ./result
                '''
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "$DOCKERHUB_CREDENTIALS",
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                }
            }
        }

        stage('Push Images') {
            steps {
                sh '''
                docker push $DOCKERHUB_REPO/vote-app
                docker push $DOCKERHUB_REPO/worker
                docker push $DOCKERHUB_REPO/result-app
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
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
