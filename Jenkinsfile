pipeline {
   agent any
   
   stages {
      stage('Clone Sources') {
        steps {
          checkout scm
        } 
      }

      stage('ALL') {
          steps {
	        script {
			sh 'echo "You are in>>> ${WORKSPACE}"'
			sh 'echo "Your name is>>> ${USER}"'
	 	    if (env.LANGUAGE == 'ALL') {
                	echo 'All languages are choosen'
                	echo  'Running C++ code'
                	sh 'cat C.c'
                	echo 'Running Python code'
                	sh 'cat PYTHON.py'
                	echo 'Running Bash script'
                	sh 'cat BASH.sh'
	            }
		    }
		}            
               
    }
	  stage('C') {
            steps {
	          script {
		      if (env.LANGUAGE == 'C') {
			echo 'C language are Running'
                	echo  'Running C++ code'
                	sh 'cat C.c'              
	     	       }
		    }
		}                 
    }
	  stage('Bash') {
            steps {
	       script {
	    	   if (env.LANGUAGE == 'BASH') {
	                echo 'Bash script are Running'
                	echo  'Running Bash script'
                	sh 'cat BASH.sh'
			    }
	    	}
        }
    }
         stage('Python') { 
            steps {
	        
		script {
		      if (env.LANGUAGE == 'PYTHON') {
		      	echo 'Python language are Running'
                      	echo  'Python code are Running'
			sh "cat PYTHON.py"
	
           	      }
	         }
            }   
        } 
	  
    }
}
