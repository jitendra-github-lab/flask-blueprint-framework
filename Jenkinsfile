pipeline {
	agent any
	stages {
		stage('One'){
			steps{
				script { 
				 CI_COOMIT = git rev-parse HEAD
				 bat("echo" CI_COOMIT)
				}
			}
		}
	}
}
