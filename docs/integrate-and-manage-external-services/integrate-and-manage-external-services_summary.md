# Integrate and Manage Generative AI Services

Generative AI (GenAI) services use machine learning models to generate original content. Choreo allows seamless integration with GenAI services.

## Register a GenAI service

Registering a GenAI service in Choreo makes it available in the Internal Marketplace for consumption via a Connection. Registration can occur at the organization or project level.

### Prerequisites

Before registering, obtain the API key, service URL, and other necessary parameters from the service provider.

### Step 1: Select a service provider

1.  Sign in to the Choreo Console.
2.  Select the organization or project.
3.  Navigate to **Dependencies** > **GenAI Services**.
4.  Click **+ Register**.
5.  Select a service provider.
6.  Click **Next**.

### Step 2: Provide service details

1.  Enter the service's **Name**, **Version**, and **Service URL**.
2.  Click **Next**.

### Step 3: Add configurations

1.  Enter the service's configuration details.
2.  Click **Register**.

## Discover GenAI services

Registered GenAI services are discoverable in the Internal Marketplace for consumption via a Connection.

## Manage GenAI services

GenAI services are listed in the **GenAI Services** list.

### View or update GenAI service details

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **GenAI Services**.
3.  Click on a service to view or update:

    *   **General Details**: Displays service metadata.
    *   **Service Definition**: Displays the service definition; update it by uploading a new file.

### Add a GenAI service to the Internal Marketplace

1.  Navigate to **Dependencies** > **GenAI Services**.
2.  Click on the service.
3.  Click **Add to Marketplace**.

### Remove a GenAI service from the Internal Marketplace

1.  Navigate to **Dependencies** > **GenAI Services**.
2.  Click on the service.
3.  Click **Remove from Marketplace**.

# Integrate and Manage Third-Party Services

Third-party services are external applications or APIs that enhance your system.

## Register a third-party service in Choreo

Registering a third-party service in Choreo makes it available in the Internal Marketplace for consumption via a Connection. Registration can occur at the organization or project level.

Choreo supports the registration of REST APIs, GraphQL APIs, Asynchronous APIs, SOAP, and gRPC services.

### Prerequisites

Before registering, obtain the API specification, service URL, and other necessary parameters from the service provider.

### Step 1: Provide basic details

1.  Sign in to the Choreo Console.
2.  Select the organization or project.
3.  Navigate to **Dependencies** > **Third-Party Services**.
4.  Click **+ Register**.
5.  Enter the service's **Name** and **Version**.
6.  Upload the service definition file.
7.  Verify the **Service Type**.
8.  Click **Define Endpoints**.

### Step 2: Define service endpoints

1.  Under **Define New Endpoint**, enter a **Name** and the **Endpoint URL**.
2.  Under **Additional Parameters**, add any other required parameters, marking sensitive ones as **Secret**.
3.  Select the environments where the endpoint should be accessible.
4.  Click **OK**.
5.  Add more endpoints if needed.
6.  Click **Register**.

## Discover third-party services

Registered third-party services are discoverable in the Internal Marketplace for consumption via a Connection.

## Manage third-party services

Third-party services are listed in the **Third-Party Services** list.

### View or update third-party service details

1.  Sign in to the Choreo Console.
2.  Navigate to **Dependencies** > **Third-Party Services**.
3.  Click on a service to view or update:

    *   **General Details**: Displays service metadata.
    *   **Service Definition**: Displays the service definition; update it by uploading a new file.
    *   **Endpoints**: Displays service endpoint details; add, modify, or delete endpoints.

### Add a third-party service to the Internal Marketplace

1.  Navigate to **Dependencies** > **Third-Party Services**.
2.  Click on the service.
3.  Click **Add to Marketplace**.

### Remove a third-party service from the Internal Marketplace

1.  Navigate to **Dependencies** > **Third-Party Services**.
2.  Click on the service.
3.  Click **Remove from Marketplace**.