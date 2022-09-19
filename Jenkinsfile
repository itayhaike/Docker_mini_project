pipeline {
   agent { node { label 'slave-docker' } }
   
   stages {
      stage('Docker build') {
        steps {
          sh 'docker build -t itay_alpcon:1.0 .'
        } 
      }
	  
      stage('Docker run') {
        steps {
	        script { 
				sh '''
				if (echo $(docker ps) | grep AlpCon); then
					echo "container are Running :)"
				elif (echo $(docker ps -a) | grep AlpCon); then
					echo "Container is down, starting it...."
					docker start AlpCon
				else 
					docker run --rm --name AlpCon -v ${WORKSPACE}:/home AlpCon
		      		'''
			}
		}            
      }
	  
	  stage('Chack if run ') {
            steps {
	          script {
			  sh '''
		      if (echo $(docker ps | grep AlpCon); then
			     echo "container are Running"
				 sleep 10
				 docker stop AlpCon
			  else 
				 echo "Container are stoped"
	         }   
	   }
        }
    }	     
}
