Rick and Morty Devops project by igor

Directory structure:
--------------------

devops_project/
│
├── Step1/
│   ├── rick_and_morty.py
│   ├── rick_and_morty_characters.csv
│   └── ...
│
├── Step2/
│   ├── Dockerfile
│   ├── requirements.txt  
│   ├── rick_and_morty.py  
│   └── ...
│
├── Step3/
│   ├── yamls/
│   │   ├── deployment.yml
│   │   ├── service.yml
│   │   ├── ingress.yml
│   │   └── ...
│   └── ...
│
├── Step4/
│   ├── rick_and_morty_chart
│   │   ├── charts/
│   │   │   └── ...
│   │   ├── templates/
│   │   │   ├── tests/
│   │   │   ├── ├── test-connection.yaml
│   │   │   │   └── ...
│   │   │   ├── _helpers.tpl
│   │   │   ├── deployment.yaml
│   │   │   ├── hpa.yaml
│   │   │   ├── ingress.yaml
│   │   │   ├── NOTES.txt
│   │   │   ├── service.yaml
│   │   │   ├── serviceaccount.yaml
│   │   │   └── ...
│   │   ├── .helmignore
│   │   ├── Chart.yaml
│   │   ├── Values.yaml
│   │   └── ...
│   └── ...
│
└── Step5/
    ├── .github/
    │   │   ├── workflows/
    │   │   │   ├── kubernetes.yaml
    │   │   │   └── ...
    │   │   └── ...   
    ├── charts/
    │   └── ...
    ├── templates/
    │   ├── tests/
    │   │   ├── ├── test-connection.yaml
    │   │   │   └── ...
    │   │   ├── _helpers.tpl
    │   │   ├── deployment.yaml
    │   │   ├── hpa.yaml
    │   │   ├── ingress.yaml
    │   │   ├── NOTES.txt
    │   │   ├── service.yaml
    │   │   ├── serviceaccount.yaml
    │   │   └── ...
    │   └── ...
    ├── .helmignore
    ├── Chart.yaml
    ├── values.yaml
    └── ...

Step 1
------

About:

This Python script retrieves information about alive human characters from the Rick and Morty API and saves their names, origin locations, and images to a CSV file.

Usage:

1. Make sure you have Python installed on your system.
2. Install the requests library (pip install requests).
3. Install the flask library (pip install flask).
4. Run the script (python rick_and_morty.py).
5. Check the generated rick_and_morty_characters.csv file in the same directory for the results.

Step 2
------

About:

This Python Flask application deploys on docker and fetches alive human characters from the Rick and Morty API and provides endpoints to retrieve this data as JSON and perform a health check.

Usage:

1. Make sure you have Python installed on your system.
2. Make sure you have docker installed on your system.
3. Clone the repository (`git clone https://github.com/IgornDevOps/devops_project.git`).
4. Enter the folder containing the files (`cd /devops_project/Step2`).
5. Build the Docker image (`docker build -t rick_and_morty .`).
6. run the Docker container (`docker run -itdp 5000:5000 rick_and_morty`).
7. Check the generated rick_and_morty_characters.csv file in the same directory for the results.
8. Health Check by running 'curl http://localhost:5000/healthcheck'.
9. Retrieve list of characters by running 'curl http://localhost:5000/characters'.

Step 3
------

About:

This code deploys the Rick and Morty application on Kubernetes.

Usage:

1. Make sure you have Minikube installed on your system.
2. Make sure you have Docker installed on your system.
3. Clone the repository (`git clone https://github.com/IgornDevOps/devops_project.git`).
4. Enter the folder containing the files (`cd /devops_project/Step3`).
5. Build the Docker image (`docker build -t rick_and_morty .`).
6. run (`kubectl apply -f deployment.yaml
         kubectl apply -f service.yaml
         kubectl apply -f ingress.yaml
         minikube addons enable ingress`).
7. Run (`minikube service rick-and-morty-service`) this provides url to access endpoints.
8. Health Check by running 'curl 192.168.59.100:31983/healthcheck' and type in the info from the previous step (ip and port).
7. Retrieve list of characters by running 'curl 192.168.59.100:31983/characters' and type in the info from the previous step (ip and port).


Step 4
------

About: 

This code deploys the Rick and Morty application on Kubernetes with the use of Helm.

Usage:

1. Clone the repository (`git clone https://github.com/IgornDevOps/devops_project.git`).
2. Enter the folder containing the files (`cd /devops_project/Step4/rick_and_morty_chart`).
3. Install the helm chart (` helm install rick-morty-api . --values values.yaml`)
4. To access endpoints run (`minikube service rick-and-morty-service`) this provides url to access endpoints.
5. Health Check by running 'curl 192.168.59.100:31983/healthcheck'(provide coordinates from previous step) and type in the info from the previous step (ip and port).
6. Retrieve list of characters by running 'curl 192.168.59.100:31983/characters' and type in the info from the previous step (ip and port).


Step5
------

About:

This code deploys the Rick and Morty application workflow on Github-Actions with the use of Helm and Kubernetes.

Workflow steps:
1. Set up Docker buildx.
2. Set up Helm.
3. Set up Minikube.
4. Start Minikube.
5. Check out the repository for deployment.
6. Deploy the application to Minikube using Helm .
7. Wait for the deployment to be ready.
8. Retrieve the service URL and target port for testing.
9. Run tests against the deployed application to ensure its functionality.

Usage:

1. Clone the repo with git clone (`git clone https://github.com/IgornDevOps/devops_project.git`).
2. Upload repo to your github with git init,git add .,git commit -m "describe commit",git push.
3. Github actions will run automatically on push trigger.
4. You can see the endpoints in the actions workflows under build>run tests.