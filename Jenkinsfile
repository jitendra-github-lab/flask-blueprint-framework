pipeline {
	agent any
	stages {
		stage('One'){
			steps{
				script { 
					CI_COOMIT = git rev-parse HEAD
					echo "TAG ID: ${CI_COOMT}"
				}
			}
		}
	}
}
