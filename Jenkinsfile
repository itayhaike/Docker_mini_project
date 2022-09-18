pipeline {
   agent { node { label 'slave' } }
   
   stages {
      stage('Docker build') {
        steps {
          sh 'docker build --name AlpCon .'
        } 
      }

      stage('Docker run') {
        steps {
	        script { 
					if ($(docker ps) | grep AlpCon) {
					echo 'container are Running'
					} elif ($(docker ps -a | grep AlpCon)) {
					echo 'Container are down, start it...'
					 sh 'docker start AlpCon'
					} else { sh 'docker run --rm --name AlpCon -v ${WORKSPACE}:/home AlpCon' }
		    }  
		}            
               
      }
	  stage('Chack if run ') {
            steps {
	          script {
		      if ($(docker ps | grep AlpCon)) {
			     echo 'container are Running'
				 sleep 10 // seconds
				 sh 'docker stop AlpCon'
			 } else { echo 'Container are stoped' }
			 
	        }             
           }
	  }	   
	  
   }
}
