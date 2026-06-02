pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/akashar13/ai-tutor-app.git'
            }
        }
       
        stage('Setup Python') {
            steps {
                bat '"C:\\Users\\Akash AR\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Python app build completed'
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }
    }
}
