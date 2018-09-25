#!/bin/bash

# Label all the nodes with beta.kubernetes.io/fluentd-ds-ready=true
for node in $(kubectl get nodes -o json | jq -r '.items[].metadata.name')
do
  kubectl label node $node beta.kubernetes.io/fluentd-ds-ready=true
done

# List all the nodes and their labels
for node in $(kubectl get nodes -o json | jq -r '.items[].metadata.name')
do
  echo node: $node has the following labels: 
  kubectl get node $node -o json | jq -r '.metadata.labels'
done
