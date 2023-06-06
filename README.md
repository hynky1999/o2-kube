# How to run it
1. I built the images and pushed them to my dockerhub repository (no need to do it again).
2. Run `kind create cluster --config cluster_definition.yaml` to create the cluster.
3. Run `kubectl apply -f app_deployment.yaml` to deploy the app.
4. Run `kubectl apply -f api_deployment.yaml` to deploy the api.
5. Go to localhost:80/showtime to see the time quried from the api.


# Cluster
I used kind as a cluster provider. It is a simple and easy to use tool to create a kubernetes cluster.

## Cluster definition
A cluster is defined in cluster_definition.yaml
3 workers and 1 master are defined in the cluster, workers are split into 2 groups, based on labels(frontend and backend).
Lastly, we also forward localhost:80 -> frontend:30080, so that we can access the app from outside the cluster.


## Depolyments
Deployments are defined in app_deployment.yaml and api_deployment.yaml.
The api_deployment is set to run on backend nodes, and the app_deployment is set to run on frontend nodes.
We use 4 and 2 replicas for api and app respectively.

Both deployment pull images from my respository on dockerhub. The images were built based on api_app/frontend_app folders.


## Services
Services are defined in app_service.yaml and api_service.yaml.
The app has a nodeport service (30080), so that we can access it from outside the cluster.
The api has a clusterIP service (5000), so that app can access it from inside the cluster.


# Questions
## Basic parts of a Kubernetes cluster:

1. Master Node
Includes components like the API server, controller manager, scheduler, and key-value store (etcd).
2. Worker Nodes: Where the pods are deployed and executed. Each node runs the Kubernetes runtime components, such as kubelet (orchestration of pods on node), container runtime, and kube-proxy (network routing).
3. Pods: The basic deployable units. It can encapuslate one or more containers and shared resources, such as network and storage.
Services: Defines a stable network endpoint to access a group of pods. There are 4 most common types of services: ClusterIP, NodePort, LoadBalancer, and Ingress.
4. ReplicaSets/Deployments: Manage the lifecycle of pods, ensuring a desired number of replicas are running and automatically scaling up or down based on defined criteria.
5. Persistent Volumes: Provides persistent storage for stateful applications in the cluster.
6. Deployments: Manage the lifecycle of pods, ensuring a desired number of replicas are running and automatically scaling up or down based on defined criteria.


## Differences between Kubernetes and Red Hat OpenShift:
Frankly I have never used Red Hat OpenShift, so I will just list the differences I found online.

- Kubernets is free, while Red Hat OpenShift is a commercial product.
- Kubernetes is easier to use, while Red Hat OpenShift is more opinionated.
- Openshift also include components for CI/CD as Source-to-Image (S2I) for building container images, integrated developer workflows, and a web console with extended management capabilities.

## Deployment of an application from a repository to a Kubernetes cluster:
1. First build a container image of the application and push it to a container registry (e.g., Docker Hub, etc.).
2. Trigger `kubectl set image deployment/<deployment-name> <container-name>=<new-image>` to update the image of the deployment.
3. Deployment will create a new ReplicaSet with the new image and gradually terminate the old pods (rolling update), or terminate all old pods and create new pods with the new image (recreate).
4. We can monitor the progress of the rolling update using `kubectl rollout status <deployment-name>`.

We could also change the deployment definition file and apply it using `kubectl apply -f <deployment-definition-file>`. However, that is a bit harder to automate.
I hope I understood the problem correctly, which means that when we start to deploy we already have a deployment definition file and running pods.
If not, the process is very similar, build images -> define deployment.yaml -> apply deployment.yaml.


## Rolling update process in Kubernetes:
I have already described it in the previous question, but I will repeat it here.
1. First build a container image of the application and push it to a container registry (e.g., Docker Hub, etc.).
2. Trigger `kubectl set image deployment/<deployment-name> <container-name>=<new-image>` to update the image of the deployment.
3. Deployment will create a new ReplicaSet with the new image and gradually terminate the old pods (rolling update), or terminate all old pods and create new pods with the new image (recreate).
4. We can monitor the progress of the rolling update using `kubectl rollout status <deployment-name>`.




