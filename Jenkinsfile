pipeline {
	agent any
	stages {
		stage('Stage-One'){
			steps{
				script { 
					CI_COMMIT = sh(script: "git tag --points-at HEAD", returnStdout: true).trim()
					echo "TAG ID: ${CI_COMMIT}"
				}
			}
		}
	}
}
