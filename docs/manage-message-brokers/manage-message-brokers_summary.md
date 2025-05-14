 # Choreo Managed Message Brokers

Choreo allows you to create Apache Kafka services across major cloud providers (AWS, Azure, GCP, and DigitalOcean) as Choreo-managed platform services for your message brokering needs. These fully managed Kafka instances can seamlessly integrate with Choreo components, providing scalable messaging for real-time data pipelines and event-driven applications. Choreo offers multiple Kafka service plans, ranging from lightweight instances for development purposes to production-grade clusters with automatic backups, high-availability multi-nodes, and partitioning.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Apache Kafka on Choreo

Apache Kafka is an open-source platform for real-time event streaming and handling large-scale, event-driven data. You can create Kafka services on Choreo as fully-managed, scalable, message brokers, ideal for handling large volumes of event-driven data.

- [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)


# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics are logical channels used to organize and transfer messages between producers and consumers. They form the core of Kafka's architecture, enabling data streams to be written and read. Kafka topics can also be partitioned to improve scalability and fault tolerance.

To create a Kafka topic, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to create a topic.
5. Click the **Topics** tab.
6. Click **+ Create**.
7. In the **Create Topic** dialog that opens, 
   1. Enter a name for the topic.
   2. To configure advanced settings, click to expand **Advanced Configurations** and apply the required settings. For details, see [Advanced topic configurations](#advanced-topic-configurations).
8. Click **Create**.

### Advanced topic configurations

Choreo allows you to customize settings for Kafka topics, including the number of partitions, replication factor, cleanup policy, retention size (bytes), retention duration (hours), and the minimum number of in-sync replicas.

**Cleanup Policy:**  Determines how messages that reach their retention limit are handled. There are three options:  

- Delete (default): Messages are removed when the retention limit is exceeded. 
- Compact: Retains only the latest record for each unique key, ensuring only the most recent data is kept.  
- Compact and Delete: Combines both approaches, where old records are deleted based on retention limits, but the latest record for each key is retained.

**Replication:** Sets the number of partition copies to ensure data durability. The default is 3.

**Partitions:** Defines the number of segments the topic should be divided into for parallel processing. The default is 1 partition.

**Retention Bytes:** Sets the maximum size of retained messages. Older messages are discarded on reaching this limit. The default is unlimited (-1).

**Retention Hours:** Defines the retention period for messages before deletion. The default is 168 hours (7 days).

**Min In-Sync Replicas:** Specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. The default is 2.

## Manage service users and access control lists

Choreo-managed Kafka services use access control lists (ACLs) and user definitions to control access to topics. You can manage users and ACL entries from the corresponding tabs on the Kafka service details page.

### Manage users

To manage users for a Choreo-managed Kafka service, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to manage users.
5. Click the **Users** tab.
6. Click **+ Add User**, specify a username, and then click **Add**.

By default, new users do not have any permissions. You can grant necessary permissions to users through access control lists (ACLs).

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

 - Username: The username.
 - Topic: The associated Kafka topic to grant access to the user.
 - Permission: The permission to grant the user. 

To add an ACL entry, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to add an ACL entry.
5. Click the **Access Control List** tab.
6. Click **+ Add Entry**, select a username, topic, and permission.
7. Click **Add**.


# Create Choreo-Managed Kafka Services

Kafka on Choreo offers fully managed, distributed message broker services across AWS, Azure, GCP, and DigitalOcean. These services are designed to handle high-throughput, fault-tolerant data streaming use cases such as real-time analytics, event sourcing, and log aggregation.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Create a Choreo-managed Kafka service

Follow the steps below to create a Choreo-managed Kafka service:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. Click **+ Create**.
5. Specify a display name for the Kafka service and click **Next**.
6. Select your preferred cloud provider from AWS, Azure, GCP, or Digital Ocean.
    - The cloud provider provisions the computing and storage infrastructure for your Kafka service.
    - There is no functional difference between Kafka services across providers except for variations in service plans and associated costs.
7. Select a region for your Kafka service.
    - Available regions depend on the selected cloud provider. Choreo currently supports US, EU, and AU regions across all providers.
8. Select a service plan.
    - Service plans differ based on the allocation of CPU, memory (RAM), and storage for your Kafka server, as well as backup retention periods and high-availability options suited for production environments.
9. Click **Create**. This creates the Kafka service and takes you to the **Overview** tab on the service details page.

## Connect to your Choreo-managed Kafka service

To connect to your Choreo-managed Kafka service, use the connection parameters from the **Overview** tab on the service details page. Choreo secures Kafka connections via client certificate authentication.

![Kafka service overview ](../assets/img/platform-services/kafka-service-overview.png)

To use the Kafka service with producer and consumer applications, you must configure them with the provided credentials and connection parameters.

By default, Kafka services accept traffic from the internet. However, if you want to restrict access to specific IP addresses or CIDR blocks, you can configure the necessary advanced settings.

To use the Kafka service in producer and consumer applications, you must add the required parameters as configurations and secrets in Choreo. You can obtain the parameter values from the **Overview** tab on the service details page and include key configurations such as the access key, access certificate, CA certificate, and service URI. Ensure you [create a topic](./configure-a-kafka-service.md#create-a-kafka-topic) before producing or consuming Kafka messages. If a topic already exists, you can proceed.

### Set up configurations and secrets

Follow these steps to set up required configurations and secrets:

1. Create two Choreo components. One for the producer and another for the consumer application. For a producer and consumer implementation in [Go](https://go.dev/), see [sample implementation](#sample-implementation)
2. Define the required [configurations and secrets](https://wso2.com/choreo/docs/devops-and-ci-cd/manage-configurations-and-secrets/) at the component level for each.
   You can configure the `service.key`, `service.cert`, and `ca.pem` using file mounts. The following [sample implementation](#sample-implementation) uses a file mount for the CA certificate. You can follow the same approach for the other files.

    ![Set CA certificate](../assets/img/platform-services/set-ca-certificate.png)

3. Set other configurations, such as `TOPIC_NAME` and `SERVICE_URI` as environment variables. You can define these as shown in the following [sample implementation](#sample-implementation).

    ![Set environment variables](../assets/img/platform-services/set-environment-variables.png)

### Sample implementation

=== "Producer"
    

            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaProducer initializes and returns a Kafka producer.
            func setupKafkaProducer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Writer {
                return kafka.NewWriter(kafka.WriterConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // sendMessages sends a specified number of messages to the Kafka topic.
            func sendMessages(producer *kafka.Writer, count int) {
                for i := 0; i < count; i++ {
                    message := fmt.Sprintf("Hello from Go using SSL %d!", i+1)
                    err := producer.WriteMessages(context.Background(), kafka.Message{Value: []byte(message)})
                    if err != nil {
                        log.Printf("failed to send message: %v", err)
                    } else {
                        log.Printf("message sent: %s", message)
                    }
                    time.Sleep(time.Second)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka producer
                producer := setupKafkaProducer(dialer, serviceURI, topicName)
                defer func() {
                    if err := producer.Close(); err != nil {
                        log.Printf("failed to close producer: %v", err)
                    }
                }()

                // Send messages
                sendMessages(producer, 100)
            }


=== "Consumer"
        
    
            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaConsumer initializes and returns a Kafka consumer.
            func setupKafkaConsumer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Reader {
                return kafka.NewReader(kafka.ReaderConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // consumeMessages continuously reads messages from the Kafka topic.
            func consumeMessages(consumer *kafka.Reader) {
                for {
                    msg, err := consumer.ReadMessage(context.Background())
                    if err != nil {
                        log.Printf("could not read message: %v", err)
                        continue
                    }
                    log.Printf("received: %s", msg.Value)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka consumer
                consumer := setupKafkaConsumer(dialer, serviceURI, topicName)
                defer func() {
                    if err := consumer.Close(); err != nil {
                        log.Printf("failed to close consumer: %v", err)
                    }
                }()

                // Consume messages
                consumeMessages(consumer)
            }


 # Choreo Managed Message Brokers

Choreo allows you to create Apache Kafka services across major cloud providers (AWS, Azure, GCP, and DigitalOcean) as Choreo-managed platform services for your message brokering needs. These fully managed Kafka instances can seamlessly integrate with Choreo components, providing scalable messaging for real-time data pipelines and event-driven applications. Choreo offers multiple Kafka service plans, ranging from lightweight instances for development purposes to production-grade clusters with automatic backups, high-availability multi-nodes, and partitioning.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Apache Kafka on Choreo

Apache Kafka is an open-source platform for real-time event streaming and handling large-scale, event-driven data. You can create Kafka services on Choreo as fully-managed, scalable, message brokers, ideal for handling large volumes of event-driven data.

- [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)


# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics are logical channels used to organize and transfer messages between producers and consumers. They form the core of Kafka's architecture, enabling data streams to be written and read. Kafka topics can also be partitioned to improve scalability and fault tolerance.

To create a Kafka topic, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to create a topic.
5. Click the **Topics** tab.
6. Click **+ Create**.
7. In the **Create Topic** dialog that opens, 
   1. Enter a name for the topic.
   2. To configure advanced settings, click to expand **Advanced Configurations** and apply the required settings. For details, see [Advanced topic configurations](#advanced-topic-configurations).
8. Click **Create**.

### Advanced topic configurations

Choreo allows you to customize settings for Kafka topics, including the number of partitions, replication factor, cleanup policy, retention size (bytes), retention duration (hours), and the minimum number of in-sync replicas.

**Cleanup Policy:**  Determines how messages that reach their retention limit are handled. There are three options:  

- Delete (default): Messages are removed when the retention limit is exceeded. 
- Compact: Retains only the latest record for each unique key, ensuring only the most recent data is kept.  
- Compact and Delete: Combines both approaches, where old records are deleted based on retention limits, but the latest record for each key is retained.

**Replication:** Sets the number of partition copies to ensure data durability. The default is 3.

**Partitions:** Defines the number of segments the topic should be divided into for parallel processing. The default is 1 partition.

**Retention Bytes:** Sets the maximum size of retained messages. Older messages are discarded on reaching this limit. The default is unlimited (-1).

**Retention Hours:** Defines the retention period for messages before deletion. The default is 168 hours (7 days).

**Min In-Sync Replicas:** Specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. The default is 2.

## Manage service users and access control lists

Choreo-managed Kafka services use access control lists (ACLs) and user definitions to control access to topics. You can manage users and ACL entries from the corresponding tabs on the Kafka service details page.

### Manage users

To manage users for a Choreo-managed Kafka service, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to manage users.
5. Click the **Users** tab.
6. Click **+ Add User**, specify a username, and then click **Add**.

By default, new users do not have any permissions. You can grant necessary permissions to users through access control lists (ACLs).

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

 - Username: The username.
 - Topic: The associated Kafka topic to grant access to the user.
 - Permission: The permission to grant the user. 

To add an ACL entry, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to add an ACL entry.
5. Click the **Access Control List** tab.
6. Click **+ Add Entry**, select a username, topic, and permission.
7. Click **Add**.


# Create Choreo-Managed Kafka Services

Kafka on Choreo offers fully managed, distributed message broker services across AWS, Azure, GCP, and DigitalOcean. These services are designed to handle high-throughput, fault-tolerant data streaming use cases such as real-time analytics, event sourcing, and log aggregation.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Create a Choreo-managed Kafka service

Follow the steps below to create a Choreo-managed Kafka service:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. Click **+ Create**.
5. Specify a display name for the Kafka service and click **Next**.
6. Select your preferred cloud provider from AWS, Azure, GCP, or Digital Ocean.
    - The cloud provider provisions the computing and storage infrastructure for your Kafka service.
    - There is no functional difference between Kafka services across providers except for variations in service plans and associated costs.
7. Select a region for your Kafka service.
    - Available regions depend on the selected cloud provider. Choreo currently supports US, EU, and AU regions across all providers.
8. Select a service plan.
    - Service plans differ based on the allocation of CPU, memory (RAM), and storage for your Kafka server, as well as backup retention periods and high-availability options suited for production environments.
9. Click **Create**. This creates the Kafka service and takes you to the **Overview** tab on the service details page.

## Connect to your Choreo-managed Kafka service

To connect to your Choreo-managed Kafka service, use the connection parameters from the **Overview** tab on the service details page. Choreo secures Kafka connections via client certificate authentication.

![Kafka service overview ](../assets/img/platform-services/kafka-service-overview.png)

To use the Kafka service with producer and consumer applications, you must configure them with the provided credentials and connection parameters.

By default, Kafka services accept traffic from the internet. However, if you want to restrict access to specific IP addresses or CIDR blocks, you can configure the necessary advanced settings.

To use the Kafka service in producer and consumer applications, you must add the required parameters as configurations and secrets in Choreo. You can obtain the parameter values from the **Overview** tab on the service details page and include key configurations such as the access key, access certificate, CA certificate, and service URI. Ensure you [create a topic](./configure-a-kafka-service.md#create-a-kafka-topic) before producing or consuming Kafka messages. If a topic already exists, you can proceed.

### Set up configurations and secrets

Follow these steps to set up required configurations and secrets:

1. Create two Choreo components. One for the producer and another for the consumer application. For a producer and consumer implementation in [Go](https://go.dev/), see [sample implementation](#sample-implementation)
2. Define the required [configurations and secrets](https://wso2.com/choreo/docs/devops-and-ci-cd/manage-configurations-and-secrets/) at the component level for each.
   You can configure the `service.key`, `service.cert`, and `ca.pem` using file mounts. The following [sample implementation](#sample-implementation) uses a file mount for the CA certificate. You can follow the same approach for the other files.

    ![Set CA certificate](../assets/img/platform-services/set-ca-certificate.png)

3. Set other configurations, such as `TOPIC_NAME` and `SERVICE_URI` as environment variables. You can define these as shown in the following [sample implementation](#sample-implementation).

    ![Set environment variables](../assets/img/platform-services/set-environment-variables.png)

### Sample implementation

=== "Producer"
    

            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaProducer initializes and returns a Kafka producer.
            func setupKafkaProducer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Writer {
                return kafka.NewWriter(kafka.WriterConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // sendMessages sends a specified number of messages to the Kafka topic.
            func sendMessages(producer *kafka.Writer, count int) {
                for i := 0; i < count; i++ {
                    message := fmt.Sprintf("Hello from Go using SSL %d!", i+1)
                    err := producer.WriteMessages(context.Background(), kafka.Message{Value: []byte(message)})
                    if err != nil {
                        log.Printf("failed to send message: %v", err)
                    } else {
                        log.Printf("message sent: %s", message)
                    }
                    time.Sleep(time.Second)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka producer
                producer := setupKafkaProducer(dialer, serviceURI, topicName)
                defer func() {
                    if err := producer.Close(); err != nil {
                        log.Printf("failed to close producer: %v", err)
                    }
                }()

                // Send messages
                sendMessages(producer, 100)
            }


=== "Consumer"
        
    
            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaConsumer initializes and returns a Kafka consumer.
            func setupKafkaConsumer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Reader {
                return kafka.NewReader(kafka.ReaderConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // consumeMessages continuously reads messages from the Kafka topic.
            func consumeMessages(consumer *kafka.Reader) {
                for {
                    msg, err := consumer.ReadMessage(context.Background())
                    if err != nil {
                        log.Printf("could not read message: %v", err)
                        continue
                    }
                    log.Printf("received: %s", msg.Value)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka consumer
                consumer := setupKafkaConsumer(dialer, serviceURI, topicName)
                defer func() {
                    if err := consumer.Close(); err != nil {
                        log.Printf("failed to close consumer: %v", err)
                    }
                }()

                // Consume messages
                consumeMessages(consumer)
            }


 # Choreo Managed Message Brokers

Choreo allows you to create Apache Kafka services across major cloud providers (AWS, Azure, GCP, and DigitalOcean) as Choreo-managed platform services for your message brokering needs. These fully managed Kafka instances can seamlessly integrate with Choreo components, providing scalable messaging for real-time data pipelines and event-driven applications. Choreo offers multiple Kafka service plans, ranging from lightweight instances for development purposes to production-grade clusters with automatic backups, high-availability multi-nodes, and partitioning.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Apache Kafka on Choreo

Apache Kafka is an open-source platform for real-time event streaming and handling large-scale, event-driven data. You can create Kafka services on Choreo as fully-managed, scalable, message brokers, ideal for handling large volumes of event-driven data.

- [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)


# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics are logical channels used to organize and transfer messages between producers and consumers. They form the core of Kafka's architecture, enabling data streams to be written and read. Kafka topics can also be partitioned to improve scalability and fault tolerance.

To create a Kafka topic, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to create a topic.
5. Click the **Topics** tab.
6. Click **+ Create**.
7. In the **Create Topic** dialog that opens, 
   1. Enter a name for the topic.
   2. To configure advanced settings, click to expand **Advanced Configurations** and apply the required settings. For details, see [Advanced topic configurations](#advanced-topic-configurations).
8. Click **Create**.

### Advanced topic configurations

Choreo allows you to customize settings for Kafka topics, including the number of partitions, replication factor, cleanup policy, retention size (bytes), retention duration (hours), and the minimum number of in-sync replicas.

**Cleanup Policy:**  Determines how messages that reach their retention limit are handled. There are three options:  

- Delete (default): Messages are removed when the retention limit is exceeded. 
- Compact: Retains only the latest record for each unique key, ensuring only the most recent data is kept.  
- Compact and Delete: Combines both approaches, where old records are deleted based on retention limits, but the latest record for each key is retained.

**Replication:** Sets the number of partition copies to ensure data durability. The default is 3.

**Partitions:** Defines the number of segments the topic should be divided into for parallel processing. The default is 1 partition.

**Retention Bytes:** Sets the maximum size of retained messages. Older messages are discarded on reaching this limit. The default is unlimited (-1).

**Retention Hours:** Defines the retention period for messages before deletion. The default is 168 hours (7 days).

**Min In-Sync Replicas:** Specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. The default is 2.

## Manage service users and access control lists

Choreo-managed Kafka services use access control lists (ACLs) and user definitions to control access to topics. You can manage users and ACL entries from the corresponding tabs on the Kafka service details page.

### Manage users

To manage users for a Choreo-managed Kafka service, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to manage users.
5. Click the **Users** tab.
6. Click **+ Add User**, specify a username, and then click **Add**.

By default, new users do not have any permissions. You can grant necessary permissions to users through access control lists (ACLs).

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

 - Username: The username.
 - Topic: The associated Kafka topic to grant access to the user.
 - Permission: The permission to grant the user. 

To add an ACL entry, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to add an ACL entry.
5. Click the **Access Control List** tab.
6. Click **+ Add Entry**, select a username, topic, and permission.
7. Click **Add**.


# Create Choreo-Managed Kafka Services

Kafka on Choreo offers fully managed, distributed message broker services across AWS, Azure, GCP, and DigitalOcean. These services are designed to handle high-throughput, fault-tolerant data streaming use cases such as real-time analytics, event sourcing, and log aggregation.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Create a Choreo-managed Kafka service

Follow the steps below to create a Choreo-managed Kafka service:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. Click **+ Create**.
5. Specify a display name for the Kafka service and click **Next**.
6. Select your preferred cloud provider from AWS, Azure, GCP, or Digital Ocean.
    - The cloud provider provisions the computing and storage infrastructure for your Kafka service.
    - There is no functional difference between Kafka services across providers except for variations in service plans and associated costs.
7. Select a region for your Kafka service.
    - Available regions depend on the selected cloud provider. Choreo currently supports US, EU, and AU regions across all providers.
8. Select a service plan.
    - Service plans differ based on the allocation of CPU, memory (RAM), and storage for your Kafka server, as well as backup retention periods and high-availability options suited for production environments.
9. Click **Create**. This creates the Kafka service and takes you to the **Overview** tab on the service details page.

## Connect to your Choreo-managed Kafka service

To connect to your Choreo-managed Kafka service, use the connection parameters from the **Overview** tab on the service details page. Choreo secures Kafka connections via client certificate authentication.

![Kafka service overview ](../assets/img/platform-services/kafka-service-overview.png)

To use the Kafka service with producer and consumer applications, you must configure them with the provided credentials and connection parameters.

By default, Kafka services accept traffic from the internet. However, if you want to restrict access to specific IP addresses or CIDR blocks, you can configure the necessary advanced settings.

To use the Kafka service in producer and consumer applications, you must add the required parameters as configurations and secrets in Choreo. You can obtain the parameter values from the **Overview** tab on the service details page and include key configurations such as the access key, access certificate, CA certificate, and service URI. Ensure you [create a topic](./configure-a-kafka-service.md#create-a-kafka-topic) before producing or consuming Kafka messages. If a topic already exists, you can proceed.

### Set up configurations and secrets

Follow these steps to set up required configurations and secrets:

1. Create two Choreo components. One for the producer and another for the consumer application. For a producer and consumer implementation in [Go](https://go.dev/), see [sample implementation](#sample-implementation)
2. Define the required [configurations and secrets](https://wso2.com/choreo/docs/devops-and-ci-cd/manage-configurations-and-secrets/) at the component level for each.
   You can configure the `service.key`, `service.cert`, and `ca.pem` using file mounts. The following [sample implementation](#sample-implementation) uses a file mount for the CA certificate. You can follow the same approach for the other files.

    ![Set CA certificate](../assets/img/platform-services/set-ca-certificate.png)

3. Set other configurations, such as `TOPIC_NAME` and `SERVICE_URI` as environment variables. You can define these as shown in the following [sample implementation](#sample-implementation).

    ![Set environment variables](../assets/img/platform-services/set-environment-variables.png)

### Sample implementation

=== "Producer"
    

            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaProducer initializes and returns a Kafka producer.
            func setupKafkaProducer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Writer {
                return kafka.NewWriter(kafka.WriterConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // sendMessages sends a specified number of messages to the Kafka topic.
            func sendMessages(producer *kafka.Writer, count int) {
                for i := 0; i < count; i++ {
                    message := fmt.Sprintf("Hello from Go using SSL %d!", i+1)
                    err := producer.WriteMessages(context.Background(), kafka.Message{Value: []byte(message)})
                    if err != nil {
                        log.Printf("failed to send message: %v", err)
                    } else {
                        log.Printf("message sent: %s", message)
                    }
                    time.Sleep(time.Second)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka producer
                producer := setupKafkaProducer(dialer, serviceURI, topicName)
                defer func() {
                    if err := producer.Close(); err != nil {
                        log.Printf("failed to close producer: %v", err)
                    }
                }()

                // Send messages
                sendMessages(producer, 100)
            }


=== "Consumer"
        
    
            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaConsumer initializes and returns a Kafka consumer.
            func setupKafkaConsumer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Reader {
                return kafka.NewReader(kafka.ReaderConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // consumeMessages continuously reads messages from the Kafka topic.
            func consumeMessages(consumer *kafka.Reader) {
                for {
                    msg, err := consumer.ReadMessage(context.Background())
                    if err != nil {
                        log.Printf("could not read message: %v", err)
                        continue
                    }
                    log.Printf("received: %s", msg.Value)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka consumer
                consumer := setupKafkaConsumer(dialer, serviceURI, topicName)
                defer func() {
                    if err := consumer.Close(); err != nil {
                        log.Printf("failed to close consumer: %v", err)
                    }
                }()

                // Consume messages
                consumeMessages(consumer)
            }


 # Choreo Managed Message Brokers

Choreo allows you to create Apache Kafka services across major cloud providers (AWS, Azure, GCP, and DigitalOcean) as Choreo-managed platform services for your message brokering needs. These fully managed Kafka instances can seamlessly integrate with Choreo components, providing scalable messaging for real-time data pipelines and event-driven applications. Choreo offers multiple Kafka service plans, ranging from lightweight instances for development purposes to production-grade clusters with automatic backups, high-availability multi-nodes, and partitioning.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Apache Kafka on Choreo

Apache Kafka is an open-source platform for real-time event streaming and handling large-scale, event-driven data. You can create Kafka services on Choreo as fully-managed, scalable, message brokers, ideal for handling large volumes of event-driven data.

- [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)


# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics are logical channels used to organize and transfer messages between producers and consumers. They form the core of Kafka's architecture, enabling data streams to be written and read. Kafka topics can also be partitioned to improve scalability and fault tolerance.

To create a Kafka topic, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to create a topic.
5. Click the **Topics** tab.
6. Click **+ Create**.
7. In the **Create Topic** dialog that opens, 
   1. Enter a name for the topic.
   2. To configure advanced settings, click to expand **Advanced Configurations** and apply the required settings. For details, see [Advanced topic configurations](#advanced-topic-configurations).
8. Click **Create**.

### Advanced topic configurations

Choreo allows you to customize settings for Kafka topics, including the number of partitions, replication factor, cleanup policy, retention size (bytes), retention duration (hours), and the minimum number of in-sync replicas.

**Cleanup Policy:**  Determines how messages that reach their retention limit are handled. There are three options:  

- Delete (default): Messages are removed when the retention limit is exceeded. 
- Compact: Retains only the latest record for each unique key, ensuring only the most recent data is kept.  
- Compact and Delete: Combines both approaches, where old records are deleted based on retention limits, but the latest record for each key is retained.

**Replication:** Sets the number of partition copies to ensure data durability. The default is 3.

**Partitions:** Defines the number of segments the topic should be divided into for parallel processing. The default is 1 partition.

**Retention Bytes:** Sets the maximum size of retained messages. Older messages are discarded on reaching this limit. The default is unlimited (-1).

**Retention Hours:** Defines the retention period for messages before deletion. The default is 168 hours (7 days).

**Min In-Sync Replicas:** Specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. The default is 2.

## Manage service users and access control lists

Choreo-managed Kafka services use access control lists (ACLs) and user definitions to control access to topics. You can manage users and ACL entries from the corresponding tabs on the Kafka service details page.

### Manage users

To manage users for a Choreo-managed Kafka service, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to manage users.
5. Click the **Users** tab.
6. Click **+ Add User**, specify a username, and then click **Add**.

By default, new users do not have any permissions. You can grant necessary permissions to users through access control lists (ACLs).

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

 - Username: The username.
 - Topic: The associated Kafka topic to grant access to the user.
 - Permission: The permission to grant the user. 

To add an ACL entry, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to add an ACL entry.
5. Click the **Access Control List** tab.
6. Click **+ Add Entry**, select a username, topic, and permission.
7. Click **Add**.


# Create Choreo-Managed Kafka Services

Kafka on Choreo offers fully managed, distributed message broker services across AWS, Azure, GCP, and DigitalOcean. These services are designed to handle high-throughput, fault-tolerant data streaming use cases such as real-time analytics, event sourcing, and log aggregation.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Create a Choreo-managed Kafka service

Follow the steps below to create a Choreo-managed Kafka service:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. Click **+ Create**.
5. Specify a display name for the Kafka service and click **Next**.
6. Select your preferred cloud provider from AWS, Azure, GCP, or Digital Ocean.
    - The cloud provider provisions the computing and storage infrastructure for your Kafka service.
    - There is no functional difference between Kafka services across providers except for variations in service plans and associated costs.
7. Select a region for your Kafka service.
    - Available regions depend on the selected cloud provider. Choreo currently supports US, EU, and AU regions across all providers.
8. Select a service plan.
    - Service plans differ based on the allocation of CPU, memory (RAM), and storage for your Kafka server, as well as backup retention periods and high-availability options suited for production environments.
9. Click **Create**. This creates the Kafka service and takes you to the **Overview** tab on the service details page.

## Connect to your Choreo-managed Kafka service

To connect to your Choreo-managed Kafka service, use the connection parameters from the **Overview** tab on the service details page. Choreo secures Kafka connections via client certificate authentication.

![Kafka service overview ](../assets/img/platform-services/kafka-service-overview.png)

To use the Kafka service with producer and consumer applications, you must configure them with the provided credentials and connection parameters.

By default, Kafka services accept traffic from the internet. However, if you want to restrict access to specific IP addresses or CIDR blocks, you can configure the necessary advanced settings.

To use the Kafka service in producer and consumer applications, you must add the required parameters as configurations and secrets in Choreo. You can obtain the parameter values from the **Overview** tab on the service details page and include key configurations such as the access key, access certificate, CA certificate, and service URI. Ensure you [create a topic](./configure-a-kafka-service.md#create-a-kafka-topic) before producing or consuming Kafka messages. If a topic already exists, you can proceed.

### Set up configurations and secrets

Follow these steps to set up required configurations and secrets:

1. Create two Choreo components. One for the producer and another for the consumer application. For a producer and consumer implementation in [Go](https://go.dev/), see [sample implementation](#sample-implementation)
2. Define the required [configurations and secrets](https://wso2.com/choreo/docs/devops-and-ci-cd/manage-configurations-and-secrets/) at the component level for each.
   You can configure the `service.key`, `service.cert`, and `ca.pem` using file mounts. The following [sample implementation](#sample-implementation) uses a file mount for the CA certificate. You can follow the same approach for the other files.

    ![Set CA certificate](../assets/img/platform-services/set-ca-certificate.png)

3. Set other configurations, such as `TOPIC_NAME` and `SERVICE_URI` as environment variables. You can define these as shown in the following [sample implementation](#sample-implementation).

    ![Set environment variables](../assets/img/platform-services/set-environment-variables.png)

### Sample implementation

=== "Producer"
    

            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaProducer initializes and returns a Kafka producer.
            func setupKafkaProducer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Writer {
                return kafka.NewWriter(kafka.WriterConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // sendMessages sends a specified number of messages to the Kafka topic.
            func sendMessages(producer *kafka.Writer, count int) {
                for i := 0; i < count; i++ {
                    message := fmt.Sprintf("Hello from Go using SSL %d!", i+1)
                    err := producer.WriteMessages(context.Background(), kafka.Message{Value: []byte(message)})
                    if err != nil {
                        log.Printf("failed to send message: %v", err)
                    } else {
                        log.Printf("message sent: %s", message)
                    }
                    time.Sleep(time.Second)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka producer
                producer := setupKafkaProducer(dialer, serviceURI, topicName)
                defer func() {
                    if err := producer.Close(); err != nil {
                        log.Printf("failed to close producer: %v", err)
                    }
                }()

                // Send messages
                sendMessages(producer, 100)
            }


=== "Consumer"
        
    
            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaConsumer initializes and returns a Kafka consumer.
            func setupKafkaConsumer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Reader {
                return kafka.NewReader(kafka.ReaderConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // consumeMessages continuously reads messages from the Kafka topic.
            func consumeMessages(consumer *kafka.Reader) {
                for {
                    msg, err := consumer.ReadMessage(context.Background())
                    if err != nil {
                        log.Printf("could not read message: %v", err)
                        continue
                    }
                    log.Printf("received: %s", msg.Value)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka consumer
                consumer := setupKafkaConsumer(dialer, serviceURI, topicName)
                defer func() {
                    if err := consumer.Close(); err != nil {
                        log.Printf("failed to close consumer: %v", err)
                    }
                }()

                // Consume messages
                consumeMessages(consumer)
            }


 # Choreo Managed Message Brokers

Choreo allows you to create Apache Kafka services across major cloud providers (AWS, Azure, GCP, and DigitalOcean) as Choreo-managed platform services for your message brokering needs. These fully managed Kafka instances can seamlessly integrate with Choreo components, providing scalable messaging for real-time data pipelines and event-driven applications. Choreo offers multiple Kafka service plans, ranging from lightweight instances for development purposes to production-grade clusters with automatic backups, high-availability multi-nodes, and partitioning.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Apache Kafka on Choreo

Apache Kafka is an open-source platform for real-time event streaming and handling large-scale, event-driven data. You can create Kafka services on Choreo as fully-managed, scalable, message brokers, ideal for handling large volumes of event-driven data.

- [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)


# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics are logical channels used to organize and transfer messages between producers and consumers. They form the core of Kafka's architecture, enabling data streams to be written and read. Kafka topics can also be partitioned to improve scalability and fault tolerance.

To create a Kafka topic, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to create a topic.
5. Click the **Topics** tab.
6. Click **+ Create**.
7. In the **Create Topic** dialog that opens, 
   1. Enter a name for the topic.
   2. To configure advanced settings, click to expand **Advanced Configurations** and apply the required settings. For details, see [Advanced topic configurations](#advanced-topic-configurations).
8. Click **Create**.

### Advanced topic configurations

Choreo allows you to customize settings for Kafka topics, including the number of partitions, replication factor, cleanup policy, retention size (bytes), retention duration (hours), and the minimum number of in-sync replicas.

**Cleanup Policy:**  Determines how messages that reach their retention limit are handled. There are three options:  

- Delete (default): Messages are removed when the retention limit is exceeded. 
- Compact: Retains only the latest record for each unique key, ensuring only the most recent data is kept.  
- Compact and Delete: Combines both approaches, where old records are deleted based on retention limits, but the latest record for each key is retained.

**Replication:** Sets the number of partition copies to ensure data durability. The default is 3.

**Partitions:** Defines the number of segments the topic should be divided into for parallel processing. The default is 1 partition.

**Retention Bytes:** Sets the maximum size of retained messages. Older messages are discarded on reaching this limit. The default is unlimited (-1).

**Retention Hours:** Defines the retention period for messages before deletion. The default is 168 hours (7 days).

**Min In-Sync Replicas:** Specifies the minimum number of replicas that must acknowledge a write for it to be considered successful. The default is 2.

## Manage service users and access control lists

Choreo-managed Kafka services use access control lists (ACLs) and user definitions to control access to topics. You can manage users and ACL entries from the corresponding tabs on the Kafka service details page.

### Manage users

To manage users for a Choreo-managed Kafka service, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to manage users.
5. Click the **Users** tab.
6. Click **+ Add User**, specify a username, and then click **Add**.

By default, new users do not have any permissions. You can grant necessary permissions to users through access control lists (ACLs).

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

 - Username: The username.
 - Topic: The associated Kafka topic to grant access to the user.
 - Permission: The permission to grant the user. 

To add an ACL entry, follow these steps:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. In the **Message Brokers** list, click the Kafka service for which you want to add an ACL entry.
5. Click the **Access Control List** tab.
6. Click **+ Add Entry**, select a username, topic, and permission.
7. Click **Add**.


# Create Choreo-Managed Kafka Services

Kafka on Choreo offers fully managed, distributed message broker services across AWS, Azure, GCP, and DigitalOcean. These services are designed to handle high-throughput, fault-tolerant data streaming use cases such as real-time analytics, event sourcing, and log aggregation.

!!! info "Note"
     - Kafka service creation is available only for paid Choreo users.
     - Kafka service billing will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create. For more details, see [Choreo Platform Services Billing](../references/choreo-platform-services-billing-and-upgrades.md#platform-service-billing-information).

## Create a Choreo-managed Kafka service

Follow the steps below to create a Choreo-managed Kafka service:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the header, click the **Organization** list. This opens the organization home page.
3. In the left navigation menu, click **Dependencies** and then click **Message Brokers**.
4. Click **+ Create**.
5. Specify a display name for the Kafka service and click **Next**.
6. Select your preferred cloud provider from AWS, Azure, GCP, or Digital Ocean.
    - The cloud provider provisions the computing and storage infrastructure for your Kafka service.
    - There is no functional difference between Kafka services across providers except for variations in service plans and associated costs.
7. Select a region for your Kafka service.
    - Available regions depend on the selected cloud provider. Choreo currently supports US, EU, and AU regions across all providers.
8. Select a service plan.
    - Service plans differ based on the allocation of CPU, memory (RAM), and storage for your Kafka server, as well as backup retention periods and high-availability options suited for production environments.
9. Click **Create**. This creates the Kafka service and takes you to the **Overview** tab on the service details page.

## Connect to your Choreo-managed Kafka service

To connect to your Choreo-managed Kafka service, use the connection parameters from the **Overview** tab on the service details page. Choreo secures Kafka connections via client certificate authentication.

![Kafka service overview ](../assets/img/platform-services/kafka-service-overview.png)

To use the Kafka service with producer and consumer applications, you must configure them with the provided credentials and connection parameters.

By default, Kafka services accept traffic from the internet. However, if you want to restrict access to specific IP addresses or CIDR blocks, you can configure the necessary advanced settings.

To use the Kafka service in producer and consumer applications, you must add the required parameters as configurations and secrets in Choreo. You can obtain the parameter values from the **Overview** tab on the service details page and include key configurations such as the access key, access certificate, CA certificate, and service URI. Ensure you [create a topic](./configure-a-kafka-service.md#create-a-kafka-topic) before producing or consuming Kafka messages. If a topic already exists, you can proceed.

### Set up configurations and secrets

Follow these steps to set up required configurations and secrets:

1. Create two Choreo components. One for the producer and another for the consumer application. For a producer and consumer implementation in [Go](https://go.dev/), see [sample implementation](#sample-implementation)
2. Define the required [configurations and secrets](https://wso2.com/choreo/docs/devops-and-ci-cd/manage-configurations-and-secrets/) at the component level for each.
   You can configure the `service.key`, `service.cert`, and `ca.pem` using file mounts. The following [sample implementation](#sample-implementation) uses a file mount for the CA certificate. You can follow the same approach for the other files.

    ![Set CA certificate](../assets/img/platform-services/set-ca-certificate.png)

3. Set other configurations, such as `TOPIC_NAME` and `SERVICE_URI` as environment variables. You can define these as shown in the following [sample implementation](#sample-implementation).

    ![Set environment variables](../assets/img/platform-services/set-environment-variables.png)

### Sample implementation

=== "Producer"
    

            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaProducer initializes and returns a Kafka producer.
            func setupKafkaProducer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Writer {
                return kafka.NewWriter(kafka.WriterConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // sendMessages sends a specified number of messages to the Kafka topic.
            func sendMessages(producer *kafka.Writer, count int) {
                for i := 0; i < count; i++ {
                    message := fmt.Sprintf("Hello from Go using SSL %d!", i+1)
                    err := producer.WriteMessages(context.Background(), kafka.Message{Value: []byte(message)})
                    if err != nil {
                        log.Printf("failed to send message: %v", err)
                    } else {
                        log.Printf("message sent: %s", message)
                    }
                    time.Sleep(time.Second)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka producer
                producer := setupKafkaProducer(dialer, serviceURI, topicName)
                defer func() {
                    if err := producer.Close(); err != nil {
                        log.Printf("failed to close producer: %v", err)
                    }
                }()

                // Send messages
                sendMessages(producer, 100)
            }


=== "Consumer"
        
    
            package main

            import (
                "context"
                "crypto/tls"
                "crypto/x509"
                "fmt"
                "log"
                "os"
                "time"

                "github.com/segmentio/kafka-go"
            )

            // loadPEMFromFile reads a PEM file from the specified file path.
            func loadPEMFromFile(filePath string) ([]byte, error) {
                data, err := os.ReadFile(filePath)
                if err != nil {
                    return nil, fmt.Errorf("failed to read file %s: %w", filePath, err)
                }
                return data, nil
            }

            // loadCertificates loads the necessary certificates for TLS configuration.
            func loadCertificates() (tls.Certificate, *x509.CertPool, error) {
                serviceCert, err := loadPEMFromFile("/service.cert")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service cert: %v", err)
                }

                serviceKey, err := loadPEMFromFile("/service.key")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load service key: %v", err)
                }

                caCert, err := loadPEMFromFile("/ca.pem")
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load ca cert: %v", err)
                }

                keypair, err := tls.X509KeyPair(serviceCert, serviceKey)
                if err != nil {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to load key and cert: %v", err)
                }

                caCertPool := x509.NewCertPool()
                if !caCertPool.AppendCertsFromPEM(caCert) {
                    return tls.Certificate{}, nil, fmt.Errorf("failed to append ca cert")
                }

                return keypair, caCertPool, nil
            }

            // createKafkaDialer initializes a Kafka dialer with the provided certificates and CA pool.
            func createKafkaDialer(keypair tls.Certificate, caCertPool *x509.CertPool) *kafka.Dialer {
                return &kafka.Dialer{
                    Timeout:   10 * time.Second,
                    DualStack: true,
                    TLS: &tls.Config{
                        Certificates: []tls.Certificate{keypair},
                        RootCAs:      caCertPool,
                    },
                }
            }

            // setupKafkaConsumer initializes and returns a Kafka consumer.
            func setupKafkaConsumer(dialer *kafka.Dialer, serviceURI, topicName string) *kafka.Reader {
                return kafka.NewReader(kafka.ReaderConfig{
                    Brokers: []string{serviceURI},
                    Topic:   topicName,
                    Dialer:  dialer,
                })
            }

            // consumeMessages continuously reads messages from the Kafka topic.
            func consumeMessages(consumer *kafka.Reader) {
                for {
                    msg, err := consumer.ReadMessage(context.Background())
                    if err != nil {
                        log.Printf("could not read message: %v", err)
                        continue
                    }
                    log.Printf("received: %s", msg.Value)
                }
            }

            func main() {
                // Load environment variables
                serviceURI := os.Getenv("SERVICE_URI")
                if serviceURI == "" {
                    log.Fatalln("service uri is not set")
                }

                topicName := os.Getenv("TOPIC_NAME")
                if topicName == "" {
                    log.Fatalln("topic name is not set")
                }

                // Load certificates and configure TLS
                keypair, caCertPool, err := loadCertificates()
                if err != nil {
                    log.Fatalf("failed to load certificates: %v", err)
                }

                // Create Kafka dialer
                dialer := createKafkaDialer(keypair, caCertPool)

                // Set up Kafka consumer
                consumer := setupKafkaConsumer(dialer, serviceURI, topicName)
                defer func() {
                    if err := consumer.Close(); err != nil {
                        log.Printf("failed to close consumer: %v", err)
                    }
                }()

                // Consume messages
                consumeMessages(consumer)
            }


# Monitor a Kafka Service

You can monitor the health and performance of your Kafka services via the service metrics and service logs.  

## Service metrics

Service metrics provide real-time insights into the performance of your Kafka service.

To view service metrics for a Kafka service, go to the **Metrics** tab on the service details page.

The service metrics include the following:

- **CPU Usage %**: Displays the percentage of CPU resources consumed by the service.
- **Disk Usage %**: Represents the percentage of disk space utilized by the service.
- **Disk IO Reads**: Displays the input/output operations per second (IOPS) for disk reads.
- **Disk IO Writes**: Displays the input/output operations per second (IOPS) for disk writes.
- **Load Average**: Displays the 5-minute average CPU load, indicating the system's computational load.
- **Memory Available %**: Represents the percentage of memory resources utilized by the service.
- **Network Received**: Indicates the volume of network traffic received by the service in bytes per second.
- **Network Sent**: Indicates the amount of network traffic transmitted by the service in bytes per second.

## Service logs

Service logs provide a detailed record of Kafka service activity, such as producer and consumer operations, connection statuses, and error reports. These logs are essential for troubleshooting issues and analyzing message flow. Logs are retained for up to 4 days.

To view Choreo-managed Kafka service logs, go to the **Logs** tab on the service details page.




# Monitor a Kafka Service

You can monitor the health and performance of your Kafka services via the service metrics and service logs.  

## Service metrics

Service metrics provide real-time insights into the performance of your Kafka service.

To view service metrics for a Kafka service, go to the **Metrics** tab on the service details page.

The service metrics include the following:

- **CPU Usage %**: Displays the percentage of CPU resources consumed by the service.
- **Disk Usage %**: Represents the percentage of disk space utilized by the service.
- **Disk IO Reads**: Displays the input/output operations per second (IOPS) for disk reads.
- **Disk IO Writes**: Displays the input/output operations per second (IOPS) for disk writes.
- **Load Average**: Displays the 5-minute average CPU load, indicating the system's computational load.
- **Memory Available %**: Represents the percentage of memory resources utilized by the service.
- **Network Received**: Indicates the volume of network traffic received by the service in bytes per second.
- **Network Sent**: Indicates the amount of network traffic transmitted by the service in bytes per second.

## Service logs

Service logs provide a detailed record of Kafka service activity, such as producer and consumer operations, connection statuses, and error reports. These logs are essential for troubleshooting issues and analyzing message flow. Logs are retained for up to 4 days.

To view Choreo-managed Kafka service logs, go to the **Logs** tab on the service details page.




# Monitor a Kafka Service

You can monitor the health and performance of your Kafka services via the service metrics and service logs.  

## Service metrics

Service metrics provide real-time insights into the performance of your Kafka service.

To view service metrics for a Kafka service, go to the **Metrics** tab on the service details page.

The service metrics include the following:

- **CPU Usage %**: Displays the percentage of CPU resources consumed by the service.
- **Disk Usage %**: Represents the percentage of disk space utilized by the service.
- **Disk IO Reads**: Displays the input/output operations per second (IOPS) for disk reads.
- **Disk IO Writes**: Displays the input/output operations per second (IOPS) for disk writes.
- **Load Average**: Displays the 5-minute average CPU load, indicating the system's computational load.
- **Memory Available %**: Represents the percentage of memory resources utilized by the service.
- **Network Received**: Indicates the volume of network traffic received by the service in bytes per second.
- **Network Sent**: Indicates the amount of network traffic transmitted by the service in bytes per second.

## Service logs

Service logs provide a detailed record of Kafka service activity, such as producer and consumer operations, connection statuses, and error reports. These logs are essential for troubleshooting issues and analyzing message flow. Logs are retained for up to 4 days.

To view Choreo-managed Kafka service logs, go to the **Logs** tab on the service details page.




# Monitor a Kafka Service

You can monitor the health and performance of your Kafka services via the service metrics and service logs.  

## Service metrics

Service metrics provide real-time insights into the performance of your Kafka service.

To view service metrics for a Kafka service, go to the **Metrics** tab on the service details page.

The service metrics include the following:

- **CPU Usage %**: Displays the percentage of CPU resources consumed by the service.
- **Disk Usage %**: Represents the percentage of disk space utilized by the service.
- **Disk IO Reads**: Displays the input/output operations per second (IOPS) for disk reads.
- **Disk IO Writes**: Displays the input/output operations per second (IOPS) for disk writes.
- **Load Average**: Displays the 5-minute average CPU load, indicating the system's computational load.
- **Memory Available %**: Represents the percentage of memory resources utilized by the service.
- **Network Received**: Indicates the volume of network traffic received by the service in bytes per second.
- **Network Sent**: Indicates the amount of network traffic transmitted by the service in bytes per second.

## Service logs

Service logs provide a detailed record of Kafka service activity, such as producer and consumer operations, connection statuses, and error reports. These logs are essential for troubleshooting issues and analyzing message flow. Logs are retained for up to 4 days.

To view Choreo-managed Kafka service logs, go to the **Logs** tab on the service details page.




# Monitor a Kafka Service

You can monitor the health and performance of your Kafka services via the service metrics and service logs.  

## Service metrics

Service metrics provide real-time insights into the performance of your Kafka service.

To view service metrics for a Kafka service, go to the **Metrics** tab on the service details page.

The service metrics include the following:

- **CPU Usage %**: Displays the percentage of CPU resources consumed by the service.
- **Disk Usage %**: Represents the percentage of disk space utilized by the service.
- **Disk IO Reads**: Displays the input/output operations per second (IOPS) for disk reads.
- **Disk IO Writes**: Displays the input/output operations per second (IOPS) for disk writes.
- **Load Average**: Displays the 5-minute average CPU load, indicating the system's computational load.
- **Memory Available %**: Represents the percentage of memory resources utilized by the service.
- **Network Received**: Indicates the volume of network traffic received by the service in bytes per second.
- **Network Sent**: Indicates the amount of network traffic transmitted by the service in bytes per second.

## Service logs

Service logs provide a detailed record of Kafka service activity, such as producer and consumer operations, connection statuses, and error reports. These logs are essential for troubleshooting issues and analyzing message flow. Logs are retained for up to 4 days.

To view Choreo-managed Kafka service logs, go to the **Logs** tab on the service details page.


