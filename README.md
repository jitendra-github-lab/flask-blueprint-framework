Follow the below steps to setup and run application

* Pre-requisite
	1. Install python >= 3.8 
	2. Install cookiecutter using below command 
		* pip install cookiecutter
		
* Build New Project
	1. Download/Git clone cookiecutter template from - https://github.com/jitendra-github-lab/flask-blueprint-framework.git
	2. Entered into flask-blueprint-framework folder and execute below command to create new project 
	   provide all the required input (Note: In case of blank input it will take default as input)
		* cookiecutter ds-arch-type
	
	3. Open PyCharm editor and Open newly created project
	4. Open Terminal and install all the required libraries using below command 
		* pip install .  
		#(Note: Dot is representing setup.py file)
		
	5. Set environment variable (For logger and configuration files)
		* environment variable name will be : <project_name>__config
		* Path : <Full path till project config directory>
		#(Example: C:\base-drectory\cookicutter-template\jeetprd\app\config\)
	
* Run and Test Project
	* Run
		1. Open Terminal in PyCharm
		2. Execute command 
			* flask run 
			(Note: It will execute and run application on ip:port http://localhost:5000)
		
	* Test
		1. Go to app-test folder and run test
		2. Go to browser and provide URL to run as Swagger API (http://localhost:5000/api/swagger)
	

Test Fork
