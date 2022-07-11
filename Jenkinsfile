pipeline {
	agent any
	stages {
		stage('One'){
			steps{
				script { 
					CI_COMMIT = sh(returnStdout: true, script: "git tag --points-at HEAD")
					echo "TAG ID: ${CI_COMMIT}"
				}
			}
		}
	}
}
