# Creating namespace
kubectl create ns got-webapp
# Creating deployment
kubectl run redis --image redis --namespace got-webapp
# Exposing deployment as service
kubectl expose deployment redis --namespace got-webapp --port 6379

