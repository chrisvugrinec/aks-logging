
# Create Namaspace
kubectl create ns efk-demo

# Create Storage Account, needed for Storage Class if using Azure File
# az group create -l westeurope -n efk-demo
# az storage account create -g efk-demo -n efkstorage


# Creating Storage Class
kubectl create -f efk-demo/es-storageclass-manageddisk.yaml 

# Create deployment using Statefull Set
kubectl create -f efk-demo/es-statefulset.yaml

# Expose the service
kubectl create -f efk-demo/es-service.yaml
