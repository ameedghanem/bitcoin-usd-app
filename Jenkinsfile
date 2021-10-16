pipeline{


	// this code is based on https://medium.com/codex/how-to-push-a-docker-image-to-docker-hub-using-jenkins-487fb1fcbe25
	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('DockerHub')
	}

	stages {

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker tag bitcoin-app $DOCKERHUB_CREDENTIALS_USR/bitcoin-app'
				sh 'docker push $DOCKERHUB_CREDENTIALS_USR/bitcoin-app'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}