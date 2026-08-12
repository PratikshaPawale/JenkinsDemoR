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
                    sh '''
                        python3 --version
                        cd "$WORKSPACE/$PROJECT_DIR"
                        python3 -m venv "$WORKSPACE/$VENV_DIR"
                        . "$WORKSPACE/$VENV_DIR/bin/activate"
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    sh '''
                        cd "$WORKSPACE/$PROJECT_DIR"
                        . "$WORKSPACE/$VENV_DIR/bin/activate"
                        pytest -q
                    '''
                }
            }
        }

        stage('Publish Results') {
            steps {
                script {
                    sh '''
                        cd "$WORKSPACE/$PROJECT_DIR"
                        ls -la
                        ls -la allure-results || true
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
