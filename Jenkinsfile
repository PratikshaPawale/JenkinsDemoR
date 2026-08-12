pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
        PROJECT_DIR = 'API_Testing'
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    bat '''
                        @echo on
                        where python
                        python --version
                        cd /d "%WORKSPACE%"
                        python -m venv "%VENV_DIR%"
                        "%WORKSPACE%\%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
                        "%WORKSPACE%\%VENV_DIR%\Scripts\python.exe" -m pip install -r "%WORKSPACE%\%PROJECT_DIR%\requirements.txt"
                        "%WORKSPACE%\%VENV_DIR%\Scripts\python.exe" -m playwright install chromium
                    '''
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    bat '''
                        @echo on
                        cd /d "%WORKSPACE%\%PROJECT_DIR%"
                        "%WORKSPACE%\%VENV_DIR%\Scripts\python.exe" -m pytest -q
                    '''
                }
            }
        }

        stage('Publish Results') {
            steps {
                script {
                    bat '''
                        @echo on
                        cd /d "%WORKSPACE%\%PROJECT_DIR%"
                        dir
                        if exist allure-results (dir allure-results) else (echo No allure-results directory found)
                    '''
                }
                archiveArtifacts artifacts: 'API_Testing/reports/**', fingerprint: true, allowEmptyArchive: true
                archiveArtifacts artifacts: 'API_Testing/allure-results/**', fingerprint: true, allowEmptyArchive: true
                publishHTML(target: [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'API_Testing/reports',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
                allure includeProperties: false, jdk: '', results: [[path: 'API_Testing/allure-results']]
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
