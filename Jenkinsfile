pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m ensurepip'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}
