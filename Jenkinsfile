pipeline {
    agent any

    environment {
        PROJECT_DIR = 'API_Testing'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                    @echo on
                    cd /d "%WORKSPACE%"
                    if exist "%VENV_DIR%" rd /s /q "%VENV_DIR%"
                    python -m venv "%VENV_DIR%"
                    "%WORKSPACE%\\%VENV_DIR%\\Scripts\\python.exe" -m pip install --upgrade pip
                    "%WORKSPACE%\\%VENV_DIR%\\Scripts\\python.exe" -m pip install -r "%WORKSPACE%\\%PROJECT_DIR%\\requirements.txt"
                    "%WORKSPACE%\\%VENV_DIR%\\Scripts\\python.exe" -m playwright install chromium
                """
            }
        }

        stage('Run API Tests') {
            steps {
                dir(PROJECT_DIR) {
                    bat """
                        @echo on
                        "%WORKSPACE%\\%VENV_DIR%\\Scripts\\python.exe" -m pytest -q
                    """
                }
            }
        }

        stage('Publish Results') {
            steps {
                dir(PROJECT_DIR) {
                    bat """
                        @echo on
                        if exist allure-results (dir allure-results) else (echo No allure-results directory found)
                        if exist reports (dir reports) else (echo No reports directory found)
                    """
                }
                archiveArtifacts artifacts: 'API_Testing/reports/**', fingerprint: true, allowEmptyArchive: true
                archiveArtifacts artifacts: 'API_Testing/allure-results/**', fingerprint: true, allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed. Check test results and logs.'
        }
        success {
            echo 'Build passed successfully.'
        }
    }
}
