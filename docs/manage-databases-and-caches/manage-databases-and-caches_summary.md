# Add Choreo-Managed Databases and Caches to the Marketplace

When you create a Choreo-managed database or cache, you can add it to the Marketplace, making it available for consumption through a connection. To do so, you must import at least one credential for it.

## Step 1: Import credentials

To import credentials:

1.  Sign in to the Choreo Console and select your organization.
2.  Navigate to **Dependencies** > **Databases**.
3.  Select the database and expand it, then click **Import Credentials**.
4.  Choose to **Use Created Credentials** (specifying a display name, database credentials, and environment) or **Use Super Admin Credentials** (specifying a display name and environment).
5.  Click **Save**.

You can delete imported credentials to prevent their use when establishing new connections without affecting existing connections.

## Step 2: Add the database or cache to the Marketplace

-   On the **Databases** tab, click **+Add to Marketplace** corresponding to the database you want to add.

Once added, the database can be consumed via a connection. You can remove a database from the Marketplace to prevent new connections without affecting existing ones.

# Choreo-Managed Cache

Fully compatible with legacy Redis® OSS. Choreo-Managed Cache provides fully-managed in-memory NoSQL databases on AWS, Azure, GCP, and Digital Ocean and can be used as a cache, database, streaming engine, or message broker.

## Create a Choreo-Managed Cache

To create a Choreo-Managed Cache:

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Databases**.
3.  Click **+ Create** and select **Choreo-Managed Cache**. Provide a display name for this server and follow the instructions.
4.  Select a cloud provider (AWS, Azure, GCP, or Digital Ocean).
5.  Select a region.
6.  Select a service plan.
7.  Click **Create**.

## Connect to your Choreo-Managed Cache

To connect:

-   Use any legacy Redis® OSS compatible driver.
-   Find connection parameters in the **Overview** section of the Choreo Console. Choreo-Managed Cache enforces TLS.
-   Restrict access to specific IP addresses and CIDR blocks under **Advanced Settings**.

## High availability and automatic backups

High availability and backup retention periods vary by service plan:

| Service plan | High availability                                                                                                  | Backup features                          | Backup history |
| ------------ | -------------------------------------------------------------------------------------------------------------------| ---------------------------------------- | -------------- |
| Hobbyist     | Single-node with limited availability.                                                                             | Single backup only for disaster recovery | None           |
| Startup      | Single-node with limited availability.                                                                             | Single backup only for disaster recovery | 1 day          |
| Business     | Two-node (primary + standby) with higher availability (automatic failover if the primary node fails).              | Automatic backups                        | 3 days         |
| Premium      | Three-node (primary + standby + standby) with highest availability (automatic failover if the primary node fails). | Automatic backups                        | 13 days        |

Production scenarios benefit from service plans with additional data copies, reduced data loss windows, and quicker restoration. Choreo runs full daily backups, encrypts backups at rest, and automatically handles outages.

### Failure recovery

Choreo automatically handles minor failures. Severe failures are addressed by creating a replacement node.

## Limitations

### Connection limits

The number of simultaneous connections depends on the available memory. The maximum number of connections can be estimated using the formula `max_number_of_connections = 4 x m`, where `m` is the memory in megabytes.

### Restricted commands

To maintain stability and security, Choreo restricts certain commands. The following commands are disabled on Choreo:
`bgrewriteaof`, `cluster`, `command`, `debug`, `failover`, `migrate`, `role`, `slaveof`, `acl`, `bgsave`, `config`, `lastsave`, `monitor`, `replicaof`, `save`, `shutdown`.

The following `eval` commands are also disabled: `eval`, `eval_ro`, `evalsha`, `evalsha_ro`, `fcall`, `fcall_ro`, `function`, `script`.

# Choreo-Managed Databases, Vector Databases, and Caches

Choreo enables the creation of fully managed PostgreSQL, MySQL databases, and Choreo-Managed Cache instances on major cloud providers. These services offer persistence and caching for Choreo components, with service plans ranging from development instances to production-grade databases.

!!! info "Note"
     - The capability to create Choreo-managed databases, vector databases, and cache services is available only for paid Choreo users.
     - Billing for these services will be included in your Choreo subscription, with pricing varying based on the service plan of the resources you create.

!!!Tip "Explore the free trial"
    Choreo provides a 7-day free trial for all database types on the 'Hobbyist' service plan, available to free-tier users.

## PostgreSQL on Choreo

PostgreSQL is an open-source object-relational database management system. You can create PostgreSQL databases on Choreo as fully Choreo-managed, flexible SQL databases that are ideal for both structured and unstructured data. If you want to perform an efficient vector similarity search, you can create a PostgreSQL vector database.

-   [Create a PostgreSQL database on Choreo](./choreo-managed-postgresql-databases.md)

## MySQL on Choreo

MySQL is a user-friendly, flexible, open-source relational database management system with a well-established history in the SQL database realm. Choreo allows you to swiftly create fully Choreo-managed MySQL databases, enabling rapid setup and utilization.

-   [Create a MySQL database on Choreo](./choreo-managed-mysql-databases.md)

## Choreo-Managed Cache

A fully-managed cache compatible with legacy Redis® OSS. A versatile, in-memory NoSQL database that serves as a cache, database, streaming engine, and message broker. Choreo-managed Cache allows you to have fully-managed instances that can be swiftly provisioned and integrated into your applications within minutes.

-   [Create a Choreo-managed Cache](./choreo-managed-caches.md)

# Choreo-managed MySQL Databases

MySQL on Choreo offers fully managed, flexible relational databases on AWS, Azure, GCP, and Digital Ocean.

## Create a Choreo-managed MySQL database

To create a Choreo-managed MySQL database:

1.  Select your **Organization**.
2.  Navigate to **Dependencies** > **Databases**.
3.  Click **Create** and select **MySQL**. Provide a display name for this server and follow the instructions.
4.  Select a cloud provider (AWS, Azure, GCP, or Digital Ocean).
5.  Choose the region.
6.  Select the service plan.

## Connect to your Choreo-managed MySQL database

To connect:

-   Use any MySQL driver, ORM, or supported generic SQL library.
-   Find connection parameters in the **Overview** section of the Choreo Console.
-   Restrict access to specific IP addresses and CIDR blocks under **Advanced Settings**.

## High Availability and Automatic Backups

High availability and backup retention periods vary by service plan:

| Service Plan | High Availability                                                  | Backup Retention Time |
|--------------|--------------------------------------------------------------------|-----------------------|
| Hobbyist     | Single-node with limited availability                              | None                  |
| Startup      | Single-node with limited availability                              | 2 days                |
| Business     | Two-node (primary + standby) with higher availability              | 14 days               |
| Premium      | Three-node (primary + standby + standby) with highest availability | 30 days               |

Production scenarios benefit from service plans with additional data copies, reduced data loss windows, and quicker restoration. Choreo runs full daily backups, encrypts backups at rest, and automatically handles outages.

## Connection Limits

The maximum number of simultaneous connections is fixed for each service plan and depends on RAM. An `extra_connection` with a value of `1` is added for system processes for all MySQL databases, regardless of the service plan.

### For plans under 4 GiB RAM

For plans under 4 GiB of RAM, the number of allowed connections is `75` per GiB:

```
max_connections = 75 x RAM + extra_connection
```

### For plans with over 4 GiB RAM:

For plans with 4 GiB or more RAM, the number of allowed connections is `100` per GiB:

```
max_connections = 100 x RAM + extra_connection
```

# Choreo-Managed PostgreSQL Databases and Vector Databases

PostgreSQL on Choreo offers fully Choreo-managed, efficient object-relational databases on AWS, Azure, GCP, and Digital Ocean. Additionally, Choreo allows you to create fully-managed PostgreSQL vector databases if you want to perform efficient vector similarity search.

## Create a Choreo-managed PostgreSQL database

To create a Choreo-managed PostgreSQL database:

1.  Sign in to the Choreo Console.
2.  Select your **Organization**.
3.  Navigate to **Dependencies** > **Databases**.
4.  Click **Create** and select **PostgreSQL**. Provide a display name for this server and follow the instructions.
5.  Select a cloud provider (AWS, Azure, GCP, or Digital Ocean).
6.  Choose the region.
7.  Select the service plan.

## Create a Choreo-managed PostgreSQL vector database

To create a Choreo-managed PostgreSQL vector database:

1.  Sign in to the Choreo Console.
2.  Select your **Organization**.
3.  Navigate to **Dependencies** > **Vector Databases**.
4.  Follow steps 4 onwards in the [Create a Choreo-managed PostgreSQL database](#create-a-choreo-managed-postgresql-database) section.

## Connecting to your Choreo-managed PostgreSQL database

To connect:

-   Use any PostgreSQL driver, ORM, or supported generic SQL library.
-   Find connection parameters in the **Overview** section of the Choreo Console.
-   Restrict access to specific IP addresses and CIDR blocks under **Advanced Settings**.

## High Availability and Automatic Backups

High availability and backup retention periods vary by service plan:

| Service Plan               | High Availability                                                  | Backup Retention Time |
|----------------------------|--------------------------------------------------------------------|-----------------------|
| Hobbyist                   | Single-node with limited availability                              | None                  |
| Startup                    | Single-node with limited availability                              | 2 days                |
| Business                   | Two-node (primary + standby) with higher availability              | 14 days               |
| Premium                    | Three-node (primary + standby + standby) with highest availability | 30 days               |

Service plans with standby nodes are generally recommended for production scenarios for multiple reasons:
- Provides another physical copy of the data in case of hardware, software, or network failures.
- Typically reduces the data loss window in disaster scenarios.
- Provides a quicker time to restore with a controlled failover in case of failures, as the standby is already installed and running.

### Automatic Backups

Choreo runs full backups daily and encrypts backups at rest. Choreo automatically handles outages.

### Failure Recovery

-   **Minor failures**: Choreo automatically handles minor failures.
-   **Severe failures**: Requires more drastic recovery measures. The monitoring infrastructure automatically detects a failing node, both when the node starts reporting issues in the self-diagnostics or when it stops communicating.

## Connection limits

The following connection limits apply to Choreo-managed PostgreSQL databases based on the selected service plan.

| Service Plan               | Max Connections |
|----------------------------|-----------------|
| Hobbyist                   | 25              |
| Startup/Business/Premium-4 | 100             |
| Business-16                | 400             |
| Premium-8                  | 200             |