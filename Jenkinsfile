pipeline {
    agent { node { label 'slave-docker' } }

    stages {
        stage('Docker build') {
            steps {
                sh 'docker build --rm -t itay_alpcon:1.0 .'
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
                    echo "Run the container..."
                    docker run --name AlpCon -v ${WORKSPACE}:/home itay_alpcon:1.0
                    fi
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
                    echo "stoping the container..."
                    sleep 10
                    docker stop AlpCon
                    else
                    echo "Container are stoped :)"
                    fi
                    '''
                }
            }
        }
    }
}
