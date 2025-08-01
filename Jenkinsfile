pipeline {
    agent any

    //environment {
    //    AWS_REGION = 'us-east-1'
    //    ECR_REPO = 'ai-mock-interviewer-repo'
    //    IMAGE_TAG = 'latest'
    //    SERVICE_NAME = 'ai-mock-interviewer-service'
    //}

    stages {

        stage('Clone GitHub Repo') {
            steps {
                script {
                    echo 'Cloning GitHub repository...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'githb-token', url: 'https://github.com/IamAbhinav01/ai-mock-interviewer.git']])
                }
            }
        }

        stage('Build TailwindCSS') {
            steps {
                sh """
                npm install
                npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify
                """
            }
        }

////        stage('Build, Scan, and Push Docker Image to ECR') {
////            steps {
////                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
////                    script {
////                        def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
////                        def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"
////                        def imageFullTag = "${ecrUrl}:${IMAGE_TAG}"
////
////                        sh """
////                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecrUrl}
////                        docker build -t ${env.ECR_REPO}:${IMAGE_TAG} .
////                        trivy image --severity HIGH,CRITICAL --format json -o trivy-report.json ${env.ECR_REPO}:${IMAGE_TAG} || true
////                        docker tag ${env.ECR_REPO}:${IMAGE_TAG} ${imageFullTag}
////                        docker push ${imageFullTag}
////                        """
////
////                        archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
////                    }
////                }
////            }
////        }
////
////        stage('Deploy to AWS App Runner') {
////            steps {
////                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-token']]) {
////                    script {
////                        def accountId = sh(script: "aws sts get-caller-identity --query Account --output text", returnStdout: true).trim()
////                        def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"
////                        def imageFullTag = "${ecrUrl}:${IMAGE_TAG}"
////
////                        echo "Triggering deployment to AWS App Runner..."
////
////                        sh """
////                        SERVICE_ARN=\$(aws apprunner list-services --query "ServiceSummaryList[?ServiceName=='${SERVICE_NAME}'].ServiceArn" --output text --region ${AWS_REGION})
////                        echo "Found App Runner Service ARN: \$SERVICE_ARN"
////
////                        aws apprunner start-deployment --service-arn \$SERVICE_ARN --region ${AWS_REGION}
////                        """
////                    }
////                }
////            }
////        }
   }
}
