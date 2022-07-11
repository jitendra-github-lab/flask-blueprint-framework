pipeline {
	agent any
	stages {
		stage('Stage-One'){
			steps{
				script { 
					CI_COMMIT = sh(script: "git rev-parse HEAD", returnStdout: true).trim()
					echo "TAG ID: ${CI_COMMIT}"
				}
			}
		}
	}
}
