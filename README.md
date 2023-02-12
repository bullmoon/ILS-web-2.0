# Application "ILS copper binding v2

This is a demo version of real application.

## Code for app

The current version of the app is built using Python, with the Flask web framework, and is served by NGINX acting as a reverse proxy server.

## Public code to GitHub

<https://github.com/bullmoon/ILS-web-2.0>

## Build image

The script for building a Docker image, named "dockerimagebuild.sh", is located in the "tools/Docker" directory.

## Public image to DockerHub

<https://hub.docker.com/repository/docker/bullhorn/ils2>

## Jenkins pipeline for building Docker image

<https://github.com/bullmoon/ILS-web-2.0/blob/main/tools/Jenkins/BuildImage/Jenkinsfile>

## Configure webhook

In brief, when we commit our changes, GitHub will trigger Jenkins and the Pipeline will be initiated.
**GitHub->repository->Settings->Webhooks->->Add webhook**

1) **Payload URL**: <https://jenkins.blablabla.com:8080/github-webhook/>
2) **Content type**: application/json
3) **Secret**: leave the field empty
4) **Which events would you like to trigger this webhook?**: choose "Let me select individual events" and check Pull "Requests" and "Pushes". make sure that the ‘Active’ option is checked and click on "Add webhook"
**Jenkins->Job->Configure->Build triggers->"GitHub hook trigger for GITScm polling"**

## Create a Kubernetes configuration

## Deploy and run app in Kubernetes cluster

## Configure GitHub webhooks to trigger Jenkins builds

## Configure Jenkins for publishing Docker images to DockerHub

## Configure Jenkins for communication with the Kubernetes cluster

## Configure Jenkins for manual deployment of the app to the Production environment
