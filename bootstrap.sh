#!/bin/bash


#bring up docker
registry_url=http://localhost:8081

docker-compose up -d

#wait until schema registry is rdy
until [[ "`docker inspect kafka-ssl-example_schema-registry_1 -f {{.State.Running}}`"=="true" ]]; do
    echo 'Waiting for schema registry...'
    sleep 0.5;
done;

registry_response=$(curl --write-out %{http_code} --silent --output /dev/null $registry_url)
until [[ "$registry_response" == "200" ]]; do
    echo $registry_response
    echo 'waiting for healthy schema reg..'
    sleep 1
    registry_response=$(curl --write-out %{http_code} --silent --output /dev/null $registry_url)
done

#register schema
echo 'Registering schema.....\n'
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json"  \
 --data-binary "@data/schema.avsc" \
$registry_url/subjects/test.topic-value/versions
echo 'Done.\n'


