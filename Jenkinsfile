pipeline {
   agent { node { label 'slave' } }
   
   stages {
      stage('Docker build') {
        steps {
          sh 'docker build --rm -t AlpCon:1.0 -f /home/itay/docker-PRO/Dockerfile .'
        } 
      }

      stage('Docker run') {
        steps {
	        script {
			sh 'docker run --name AlpCon -v/home/itay/docker-PRO:${WORKSPACE} AlpCon:1.0
			
		    }
		}            
               
     }
	  stage('Chack if run ') {
            steps {
	          script {
		      if ($(docker ps | grep AlpCon) == 'AlpCon') {
			 echo 'container are Running'
			 } else { sh 'docker start AlpCon'
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
       
   }
}
