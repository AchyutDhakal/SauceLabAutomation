pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest'
            }
        }
    }
}