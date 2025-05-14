Here's a summary of the provided content, maintaining the original headings for organization:

# Choreo Managed Message Brokers

Choreo provides Apache Kafka services across AWS, Azure, GCP, and DigitalOcean as managed platform services. These Kafka instances integrate with Choreo components, offering scalable messaging. Service plans range from lightweight to production-grade, with features like automatic backups and high availability. Kafka service creation is available for paid users only and will be included in your Choreo subscription.

## Apache Kafka on Choreo

Kafka on Choreo allows you to create fully-managed, scalable message brokers suitable for handling large volumes of event-driven data.

-   [Create a Choreo-managed Kafka service](./create-choreo-managed-kafka-services.md)

# Configure a Kafka Service

After creating a Kafka service, you can create topics, configure advanced settings, and manage access to ensure secure and efficient message processing.

## Create a Kafka topic

Kafka topics organize messages between producers and consumers and can be partitioned for scalability. To create a topic:

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Message Brokers**.
3.  Select the desired Kafka service.
4.  Click the **Topics** tab and then **+ Create**.
5.  Enter a topic name and configure advanced settings if needed.
6.  Click **Create**.

### Advanced topic configurations

Customizable settings include:

*   **Cleanup Policy:** Delete, Compact, or Compact and Delete.
*   **Replication:** Number of partition copies (default is 3).
*   **Partitions:** Number of segments (default is 1).
*   **Retention Bytes:** Maximum size of retained messages (default is unlimited).
*   **Retention Hours:** Retention period (default is 168 hours).
*   **Min In-Sync Replicas:** Minimum replicas for write acknowledgment (default is 2).

## Manage service users and access control lists

Control access to topics using ACLs and user definitions.

### Manage users

To manage users:

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Message Brokers**.
3.  Select the desired Kafka service.
4.  Click the **Users** tab.
5.  Click **+ Add User**, specify a username, and click **Add**.

New users have no permissions by default.

### Configure access control lists (ACLs)

An ACL entry defines access permission for a user. Each entry includes:

*   Username
*   Topic
*   Permission

To add an ACL entry:

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Message Brokers**.
3.  Select the desired Kafka service.
4.  Click the **Access Control List** tab.
5.  Click **+ Add Entry**, select a username, topic, and permission.
6.  Click **Add**.

# Create Choreo-Managed Kafka Services

Kafka on Choreo provides fully managed message broker services for high-throughput data streaming.

## Create a Choreo-managed Kafka service

To create a service:

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Message Brokers**.
3.  Click **+ Create**.
4.  Specify a display name and click **Next**.
5.  Select a cloud provider (AWS, Azure, GCP, or DigitalOcean).
6.  Select a region.
7.  Select a service plan based on CPU, memory, and storage needs.
8.  Click **Create**.

## Connect to your Choreo-managed Kafka service

Use connection parameters from the **Overview** tab, which secures connections via client certificate authentication. Configure producer/consumer applications with the provided credentials. You can restrict access to specific IP addresses.

### Set up configurations and secrets

1.  Create two Choreo components (producer and consumer).
2.  Define configurations and secrets at the component level, using file mounts for `service.key`, `service.cert`, and `ca.pem`.
3.  Set other configurations (e.g., `TOPIC_NAME`, `SERVICE_URI`) as environment variables.

### Sample implementation

Sample Go implementations for producers and consumers are provided.

# Monitor a Kafka Service

Monitor service health and performance using metrics and logs.

## Service metrics

View real-time performance insights on the **Metrics** tab, including:

*   CPU Usage %
*   Disk Usage %
*   Disk IO Reads/Writes
*   Load Average
*   Memory Available %
*   Network Received/Sent

## Service logs

Access detailed records of Kafka activity on the **Logs** tab, which are retained for up to 4 days.