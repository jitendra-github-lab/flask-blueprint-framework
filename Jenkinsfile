pipeline {
	agent any
	stages {
		stage('One'){
			steps{
				script { 
				 CI_COOMIT = git tag -f -m "Test tag" -a %Tag_Name% %SHA%
				 bat("echo" CI_COOMIT)
				}
			}
		}
	}
}
