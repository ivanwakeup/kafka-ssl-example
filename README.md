# kafka-ssl-example
A example repository to show how to produce and consume to kafka over an SSL connection

This repository contains generated keystore and truststore .jks files intended for example use only, please don't use these files
in your production environment!! You should obviously be generating your own keystore for both clients and brokers in production.


To get up and running, do the following:

1. run bootstrap.sh, which will bring up your docker containers and register a test message schema (found in data/schema.avsc)
2. example certificates/keystores/truststores are provided for java clients to enable ssl consumption. use the kafka-cli to try out using the consumer.



tips:

you can make adjustments to the docker-compose.yml to change your broker config. by default, the brokers listen on both PLAINTEXT (9092) and SSL (9093) channels.
