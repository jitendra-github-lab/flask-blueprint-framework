pipeline {
	agent any
	stages {
		stage('One'){
			steps{
				script { 
				 CI_COOMIT = sh(script: 'git rev-parse --short HEAD', returnStdout: true)? trim()
				 echo "${CI_COOMIT}"
				}
			}
		}
		
	}
}