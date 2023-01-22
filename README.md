
# APACHE KAFKA® FOR PYTHON DEVELOPERS

This Repo is a code repo for the python course by Confluent - 
[ APACHE KAFKA® FOR PYTHON DEVELOPERS](https://developer.confluent.io/learn-kafka/kafka-python/intro/)


## What is Kafka?
Apache Kafka is a real-time data streaming technology capable of handling trillions of events per day. Initially conceived as a messaging queue, Kafka is based on an abstraction of a distributed commit log. Since being created and open sourced in 2011, Kafka has since become the industry standard for working with data in motion.

## What is a kafka topic?
Apache Kafka has a dedicated and fundamental unit for Event or Message organization, called Topics. In other words, Kafka Topics are Virtual Groups or Logs that hold messages and events in a logical order, allowing users to send and receive data between Kafka Servers with ease.

When a Producer sends messages or events into a specific Kafka Topic, the topics will append the messages one after another, thereby creating a Log File. Furthermore, producers can Push Messages into the tail of these newly created logs while consumers Pull Messages off from a specific Kafka Topic. 

By creating Kafka Topics, users can perform Logical Segregation between Messages and Events, which works the same as the concept of different tables having different types of data in a database.

In Apache Kafka, you can create any number of topics based on your use cases. However, each topic should have a unique and identifiable name to differentiate it across various Kafka Brokers in a Kafka Cluster

## What is Partitioning in Kafka?
Partitioning takes the single topic log and breaks it into multiple logs, each of which can live on a separate node in the Kafka cluster. This way, the work of storing messages, writing new messages, and processing existing messages can be split among many nodes in the cluster.

## What is a broker?
From a physical infrastructure standpoint, Apache Kafka is composed of a network of machines called brokers. In a contemporary deployment, these may not be separate physical servers but containers running on pods running on virtualized servers running on actual processors in a physical datacenter somewhere. However they are deployed, they are independent machines each running the Kafka broker process. Each broker hosts some set of partitions and handles incoming requests to write new events to those partitions or read events from them. Brokers also handle replication of partitions between each other.

## Replication in Kafka
It would not do if we stored each partition on only one broker. Whether brokers are bare metal servers or managed containers, they and their underlying storage are susceptible to failure, so we need to copy partition data to several other brokers to keep it safe. Those copies are called follower replicas, whereas the main partition is called the leader replica. When you produce data to the leader—in general, reading and writing are done to the leader—the leader and the followers work together to replicate those new writes to the followers.

This happens automatically, and while you can tune some settings in the producer to produce varying levels of durability guarantees, this is not usually a process you have to think about as a developer building systems on Kafka. All you really need to know as a developer is that your data is safe, and that if one node in the cluster dies, another will take over its role.



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](http://infapy.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prashanth-pradeep)
[![GitHub](https://img.shields.io/badge/github-DC6B5D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prashanth-p)

