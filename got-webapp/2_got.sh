# Build your images and push it to dockerhub
# docker build -t [your account]/nameofthisapp .
# docker push [your account]/nameofthisapp
# Run the image on your kube cluster, for eg:
kubectl run got-webapp --image cvugrinec/got-webapp --namespace got-webapp
# Expose as service with public endpoint
kubectl expose deployment got-webapp --namespace got-webapp --port 5000 --target-port 5000 --type LoadBalancer
