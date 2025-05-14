 # Consume an API Key Secured Service

{% include "discovering-an-api-devportal.md" %}

## Creating an API Key

To consume an API secured with an API Key, an API Key is required. To obtain an API Key, an application must first be created in the Choreo Developer Portal. This application represents a physical entity (such as a mobile app, web app, or device) and serves as the means to subscribe to APIs under a defined usage policy. The API Key is associated with a specific application, and an application can be created during the API Key generation process if needed.

---

### Steps to Create an API Key

1. Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2. Click on **APIs** in the Developer Portal header.
3. Select the desired API that requires an API Key for access.
4. This will take you to the API overview page, where you can manage credentials.

#### Generating Environment-Specific API Keys.

Choreo allows you to generate API keys for production and sandbox environments.

!!! note
    Access to production endpoints may be restricted based on your user role. Ensure you have the required permissions before generating production keys.

Follow these steps to generate an API Key:

1. In the left navigation menu, select the desired environment under **Credentials**. The **API Keys** pane for the chosen environment will open.
2. If any API keys already exist, they will be listed here.
3. Click **Generate API Key** and configure the following options:
    - **Key Name**: Provide a suitable name for the API key.
    - **Application**: Select an existing application or create a new one.
    - **Subscription Policy**: Choose an appropriate subscription policy.
4. Click **Generate**. The newly created API Key will be displayed.


!!! note
    If the selected application is already subscribed to the chosen API, the subscription selection step will be skipped.
    If the selected API has multiple endpoints, an endpoint needs to be selected during API key generation.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.choreoapis.dev/greet"
```

For managing API keys, see [Manage API Keys](./manage-api-keys.md)

# Consume a OAuth2 Secured Service

{% include "discovering-an-api-devportal.md" %}

## Create an application

{% include "create-an-application.md" %}

## Subscribe to an API

{% include "create-a-subscription.md" %}

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.

## Consume an API

Use this generated access token to authenticate API requests by including it in the `Bearer` header when invoking the API.

Example:
    
```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" -X GET "https://my-sample-api.choreoapis.dev/greet"  
```

!!! note
    The name of the Authorization header may vary depending on the API provider’s configuration. Always refer to the API’s Swagger (OpenAPI) definition for the correct header format.


 # Consume an API Key Secured Service

{% include "discovering-an-api-devportal.md" %}

## Creating an API Key

To consume an API secured with an API Key, an API Key is required. To obtain an API Key, an application must first be created in the Choreo Developer Portal. This application represents a physical entity (such as a mobile app, web app, or device) and serves as the means to subscribe to APIs under a defined usage policy. The API Key is associated with a specific application, and an application can be created during the API Key generation process if needed.

---

### Steps to Create an API Key

1. Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2. Click on **APIs** in the Developer Portal header.
3. Select the desired API that requires an API Key for access.
4. This will take you to the API overview page, where you can manage credentials.

#### Generating Environment-Specific API Keys.

Choreo allows you to generate API keys for production and sandbox environments.

!!! note
    Access to production endpoints may be restricted based on your user role. Ensure you have the required permissions before generating production keys.

Follow these steps to generate an API Key:

1. In the left navigation menu, select the desired environment under **Credentials**. The **API Keys** pane for the chosen environment will open.
2. If any API keys already exist, they will be listed here.
3. Click **Generate API Key** and configure the following options:
    - **Key Name**: Provide a suitable name for the API key.
    - **Application**: Select an existing application or create a new one.
    - **Subscription Policy**: Choose an appropriate subscription policy.
4. Click **Generate**. The newly created API Key will be displayed.


!!! note
    If the selected application is already subscribed to the chosen API, the subscription selection step will be skipped.
    If the selected API has multiple endpoints, an endpoint needs to be selected during API key generation.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.choreoapis.dev/greet"
```

For managing API keys, see [Manage API Keys](./manage-api-keys.md)

# Consume a OAuth2 Secured Service

{% include "discovering-an-api-devportal.md" %}

## Create an application

{% include "create-an-application.md" %}

## Subscribe to an API

{% include "create-a-subscription.md" %}

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.

## Consume an API

Use this generated access token to authenticate API requests by including it in the `Bearer` header when invoking the API.

Example:
    
```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" -X GET "https://my-sample-api.choreoapis.dev/greet"  
```

!!! note
    The name of the Authorization header may vary depending on the API provider’s configuration. Always refer to the API’s Swagger (OpenAPI) definition for the correct header format.


 # Consume an API Key Secured Service

{% include "discovering-an-api-devportal.md" %}

## Creating an API Key

To consume an API secured with an API Key, an API Key is required. To obtain an API Key, an application must first be created in the Choreo Developer Portal. This application represents a physical entity (such as a mobile app, web app, or device) and serves as the means to subscribe to APIs under a defined usage policy. The API Key is associated with a specific application, and an application can be created during the API Key generation process if needed.

---

### Steps to Create an API Key

1. Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2. Click on **APIs** in the Developer Portal header.
3. Select the desired API that requires an API Key for access.
4. This will take you to the API overview page, where you can manage credentials.

#### Generating Environment-Specific API Keys.

Choreo allows you to generate API keys for production and sandbox environments.

!!! note
    Access to production endpoints may be restricted based on your user role. Ensure you have the required permissions before generating production keys.

Follow these steps to generate an API Key:

1. In the left navigation menu, select the desired environment under **Credentials**. The **API Keys** pane for the chosen environment will open.
2. If any API keys already exist, they will be listed here.
3. Click **Generate API Key** and configure the following options:
    - **Key Name**: Provide a suitable name for the API key.
    - **Application**: Select an existing application or create a new one.
    - **Subscription Policy**: Choose an appropriate subscription policy.
4. Click **Generate**. The newly created API Key will be displayed.


!!! note
    If the selected application is already subscribed to the chosen API, the subscription selection step will be skipped.
    If the selected API has multiple endpoints, an endpoint needs to be selected during API key generation.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.choreoapis.dev/greet"
```

For managing API keys, see [Manage API Keys](./manage-api-keys.md)

# Consume a OAuth2 Secured Service

{% include "discovering-an-api-devportal.md" %}

## Create an application

{% include "create-an-application.md" %}

## Subscribe to an API

{% include "create-a-subscription.md" %}

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.

## Consume an API

Use this generated access token to authenticate API requests by including it in the `Bearer` header when invoking the API.

Example:
    
```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" -X GET "https://my-sample-api.choreoapis.dev/greet"  
```

!!! note
    The name of the Authorization header may vary depending on the API provider’s configuration. Always refer to the API’s Swagger (OpenAPI) definition for the correct header format.


 # Consume an API Key Secured Service

{% include "discovering-an-api-devportal.md" %}

## Creating an API Key

To consume an API secured with an API Key, an API Key is required. To obtain an API Key, an application must first be created in the Choreo Developer Portal. This application represents a physical entity (such as a mobile app, web app, or device) and serves as the means to subscribe to APIs under a defined usage policy. The API Key is associated with a specific application, and an application can be created during the API Key generation process if needed.

---

### Steps to Create an API Key

1. Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2. Click on **APIs** in the Developer Portal header.
3. Select the desired API that requires an API Key for access.
4. This will take you to the API overview page, where you can manage credentials.

#### Generating Environment-Specific API Keys.

Choreo allows you to generate API keys for production and sandbox environments.

!!! note
    Access to production endpoints may be restricted based on your user role. Ensure you have the required permissions before generating production keys.

Follow these steps to generate an API Key:

1. In the left navigation menu, select the desired environment under **Credentials**. The **API Keys** pane for the chosen environment will open.
2. If any API keys already exist, they will be listed here.
3. Click **Generate API Key** and configure the following options:
    - **Key Name**: Provide a suitable name for the API key.
    - **Application**: Select an existing application or create a new one.
    - **Subscription Policy**: Choose an appropriate subscription policy.
4. Click **Generate**. The newly created API Key will be displayed.


!!! note
    If the selected application is already subscribed to the chosen API, the subscription selection step will be skipped.
    If the selected API has multiple endpoints, an endpoint needs to be selected during API key generation.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.choreoapis.dev/greet"
```

For managing API keys, see [Manage API Keys](./manage-api-keys.md)

# Consume a OAuth2 Secured Service

{% include "discovering-an-api-devportal.md" %}

## Create an application

{% include "create-an-application.md" %}

## Subscribe to an API

{% include "create-a-subscription.md" %}

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.

## Consume an API

Use this generated access token to authenticate API requests by including it in the `Bearer` header when invoking the API.

Example:
    
```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" -X GET "https://my-sample-api.choreoapis.dev/greet"  
```

!!! note
    The name of the Authorization header may vary depending on the API provider’s configuration. Always refer to the API’s Swagger (OpenAPI) definition for the correct header format.


 # Consume an API Key Secured Service

{% include "discovering-an-api-devportal.md" %}

## Creating an API Key

To consume an API secured with an API Key, an API Key is required. To obtain an API Key, an application must first be created in the Choreo Developer Portal. This application represents a physical entity (such as a mobile app, web app, or device) and serves as the means to subscribe to APIs under a defined usage policy. The API Key is associated with a specific application, and an application can be created during the API Key generation process if needed.

---

### Steps to Create an API Key

1. Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2. Click on **APIs** in the Developer Portal header.
3. Select the desired API that requires an API Key for access.
4. This will take you to the API overview page, where you can manage credentials.

#### Generating Environment-Specific API Keys.

Choreo allows you to generate API keys for production and sandbox environments.

!!! note
    Access to production endpoints may be restricted based on your user role. Ensure you have the required permissions before generating production keys.

Follow these steps to generate an API Key:

1. In the left navigation menu, select the desired environment under **Credentials**. The **API Keys** pane for the chosen environment will open.
2. If any API keys already exist, they will be listed here.
3. Click **Generate API Key** and configure the following options:
    - **Key Name**: Provide a suitable name for the API key.
    - **Application**: Select an existing application or create a new one.
    - **Subscription Policy**: Choose an appropriate subscription policy.
4. Click **Generate**. The newly created API Key will be displayed.


!!! note
    If the selected application is already subscribed to the chosen API, the subscription selection step will be skipped.
    If the selected API has multiple endpoints, an endpoint needs to be selected during API key generation.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.choreoapis.dev/greet"
```

For managing API keys, see [Manage API Keys](./manage-api-keys.md)

# Consume a OAuth2 Secured Service

{% include "discovering-an-api-devportal.md" %}

## Create an application

{% include "create-an-application.md" %}

## Subscribe to an API

{% include "create-a-subscription.md" %}

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.

## Consume an API

Use this generated access token to authenticate API requests by including it in the `Bearer` header when invoking the API.

Example:
    
```bash
curl -H "Authorization: Bearer <YOUR_ACCESS_TOKEN>" -X GET "https://my-sample-api.choreoapis.dev/greet"  
```

!!! note
    The name of the Authorization header may vary depending on the API provider’s configuration. Always refer to the API’s Swagger (OpenAPI) definition for the correct header format.



To use a published API in your application, you must subscribe to it. When you subscribe to an API, your subscription covers all minor versions within the API's major version.

The subscription process ensures secure authentication of API requests using application keys. While you can generate credentials for an API without subscribing to an application, this approach limits advanced configuration options such as access token expiry time, revoke token expiry time, ID token expiry time, and enabling access to the API without a secret. Generating keys directly in the API is suitable for testing or short-term use but is not recommended for long-term production usage.

To subscribe to an API via an application, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. To navigate to applications, in the Developer Portal header, click **Applications**.

3. On the **My Applications** page, click on the application you want to use to subscribe to an API.

4. In the left navigation menu, click **Subscriptions**.

5. In the **Subscription Management** pane, click **+ Add APIs**.

6. Click **Add** to subscribe to an API. You can subscribe to one or more APIs based on your requirements.

    !!! tip
        When a new minor version of an API is published, the major version-based invocation URL automatically routes to the latest minor version within the subscribed API's major version. This ensures that existing client applications continue to function without disruption while benefiting from improvements or additions in the newer minor version.

    ![Add APIs](../assets/img/consume/add-apis.png)

Once you subscribe to an API, you can invoke it using the application keys.



An application in Choreo is a logical representation of a physical application, such as a mobile app, web app, or device. To consume an API in Choreo, you need to create an application that maps to your physical application and subscribe to the required API under a usage policy plan. This plan provides a usage quota. A single application can have multiple API subscriptions. Using the consumer key and consumer secret, you can generate an access token to invoke all APIs subscribed to the same application.

This guide walks you through the steps to create an application in Choreo.

## Step 1: Create an application

To create an application in the Choreo Developer Portal, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. In the Developer Portal header, click **Applications** and then click **+Create**.

3. Enter application details. Provide a name and description for your application.

4. Click **Create**.

This creates the application and opens the **Application Overview** page. Here, you can view details such as the token type, workflow status, and the application owner.

## Step 2: Generate keys

Choreo uses OAuth 2.0 bearer token-based authentication for API access. An API access token is a string passed as an HTTP header in API requests to authenticate access.

Once you create an application, you can generate credentials for it. Choreo provides a consumer key and consumer secret when you generate credentials for the first time. The consumer key acts as the unique identifier for the application and is used for authentication.

### Generate environment-specific keys and tokens

You can generate keys and tokens to invoke production and non-production endpoints separately.

!!! info "Note"
    Access to production endpoints depends on your role. If you have the necessary permissions, you can generate keys and tokens for production endpoints.

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Expand **Advanced configurations** and review the following options:
    - **Grant types**: Select the grant types to use when generating the access token.
    - **Public client**: Enable **Allow authentication without the client secret** if your application is a public client (e.g., a browser or mobile app).
    - **PKCE for enhanced security**: Set to **Mandatory** if you want the application to send a code challenge in the authorization request and a code verifier in the token request. Asgardeo supports SHA-256 and plain.
    - **Application access token expiry time**: Set the access token expiry time in seconds.
    - **Refresh token expiry time**: Set the refresh token expiry time in seconds.
    - **ID token expiry time**: Set the ID token expiry time in seconds.

5. Click **Generate Credentials**. The **Application Keys** pane will display the consumer key and consumer secret.

You can use the consumer key and consumer secret to generate an API access token by invoking the token endpoint. You can also revoke the access token by invoking the revoke endpoint.

To generate a test token for testing purposes, click **Generate Token** and copy the displayed token. Alternatively, click **cURL** to copy the generated cURL command and obtain a test token using a cURL client.

!!! warning
    Do not use the test token in your production environment.


Choreo is a powerful platform that enables developers to create, deploy, and consume services efficiently. The Choreo Developer Portal simplifies API discovery and usage, allowing developers to integrate APIs seamlessly into their applications.

This guide is intended for application developers (both internal and external) who wish to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

---

## Prerequisites

Before proceeding, ensure you have access to a published service to consume. If you do not have one, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) guide to create and deploy a sample REST API.

---

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: Visible to all users in the Developer Portal.
- **Private**: Accessible only to signed-in users.
- **Restricted**: Available to users with specific roles, enabling granular access control.

For more details, refer to [Control API Visibility](../api-management/control-api-visibility.md).

### Viewing Available APIs

The Developer Portal lists APIs categorized by their major versions. The API overview page displays:

- Subscribed versions of the API
- Subscription details (e.g., application name and creation date)

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

### Selecting the Correct API Version

> **Tip:** It is recommended to use the latest version of an API. Copy the **Endpoint(s)** from the API overview page and integrate it into your client application to ensure compatibility with the most recent updates.

---

# Generate an Access Token

Using access tokens for request authorization enhances security by preventing certain types of denial-of-service (DoS) attacks on published APIs. API consumers generate access tokens to access APIs, including them as string values in HTTP header requests.

When you register an application in the Developer Portal, you can generate a consumer key and consumer secret. These credentials represent the application's identity. The consumer key acts as the unique identifier for the application, similar to a username, and is used to authenticate API requests. Choreo issues an access token for the application based on the consumer key.

This guide walks you through the steps to generate an access token for your application in Choreo.

## Prerequisites

Before proceeding, ensure you have the following:

1. An application in the [Choreo Developer Portal](https://devportal.choreo.dev). If you don’t have one, [create a new application](https://wso2.com/choreo/docs/consuming-services/manage-application/#step-1-create-an-application).
2. [Generate keys for the application](https://wso2.com/choreo/docs/consuming-services/create-an-application/#step-2-generate-keys).
3. [Subscribe APIs to the application](https://wso2.com/choreo/docs/consuming-services/create-a-subscription/#manage-subscriptions).

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.


# Manage API Keys

To access a published API secured with an API Key, you need to generate a dedicated API Key for that specific API. This key acts as a unique identifier, enabling authorized usage while maintaining security and control over how the API is consumed.  

Once created, API Keys can be managed through two locations within the Choreo Developer Portal:

- **Credentials section of the API**: This section provides an overview of all API Keys associated with the specific API, enabling API owners to monitor and manage access.
- **Credentials section of the Application**: This section allows application owners to view and manage all API Keys linked to their application, ensuring they have control over API subscriptions and access.

From these sections, you can perform various API Key management actions, such as regenerating and deleting.

## API Key Regeneration

API Key regeneration allows you to obtain a new secret key for an existing API Key while ensuring minimal disruption to service. When an API Key is regenerated, a new secret key is generated, and the existing key remains valid for a grace period of one hour before being revoked. This ensures that applications have sufficient time to update their credentials without experiencing service interruptions.

!!! warning
    Ensure that all applications using the existing API Key are updated with the newly generated key within the grace period to prevent any disruptions in API invocations.

## API Key Deletion

API Keys can be deleted when they are no longer needed. Deleting an API Key immediately revokes its access, preventing further use of the key for API invocations. This action is irreversible and should be performed with caution, as any application relying on the deleted API Key will lose access to the API immediately.

# Manage Applications

{% include "create-an-application.md" %}

## Grant types

Choreo uses OAuth 2.0 for authentication. In OAuth 2.0, grant types are methods that allow client applications to obtain an access token. The type of grant used depends on the resource owner, the application type, and the trust relationship between the authorization server and the resource owner.

### Authorization code grant

The Authorization Code flow is a secure way for a client application to obtain an access token without exposing the user's credentials. The user authenticates with the authorization server, which issues an authorization code. This code is then exchanged for an access token.

This method protects user credentials and prevents them from being compromised by malicious client applications.

### Refresh token grant

A refresh token allows you to obtain a new access token when the current one expires or when a new token is needed. The refresh token grant type is used for this purpose. Refresh tokens are optional and, if issued, are included in the response along with the access token. You can use the refresh token to request a new access token from the authorization server. Choreo's default authorization server, Asgardeo, issues refresh tokens for all grant types except the **Client Credentials** grant type, as recommended by the OAuth 2.0 specification.

!!! note
    - Treat refresh tokens as securely as access tokens.
    - No user interaction is required to obtain a new access token using the Refresh Token grant type.

### Client credentials grant

The Client Credentials flow allows client applications to obtain an access token without user authentication. This is useful when the client application needs to access its own resources, such as data storage or APIs, but does not require access to user data. Ensure that client credentials are kept secure, as anyone with these credentials can obtain access tokens and access the client's resources.

### Implicit grant

The Implicit Grant flow allows a client application to obtain an access token directly from the authorization server without an intermediate authorization code exchange. This flow is commonly used in browser-based applications.

However, the access token is exposed in the browser's URL fragment, making it vulnerable to attacks like cross-site scripting (XSS). As a result, this flow is not recommended for applications requiring high security.

### Password grant

The Password Grant flow allows a client application to obtain an access token by directly providing the user's username and password to the authorization server. This method is less secure than other grant types because the client application handles and transmits the user's credentials.

This grant type is typically used in highly trusted client applications where user experience is prioritized over security. It is not recommended for public-facing applications or scenarios involving sensitive data.

## Revoke access tokens

Revoking JWT access tokens can be challenging because they are self-validating. Once issued, a token contains all the information needed to validate its authenticity without requiring server-side lookups.

It is recommended to set an expiry time of no more than 900 seconds.

In traditional session-based authentication, the server can revoke a session by invalidating its session ID. However, JWTs do not rely on a central authority to track valid or invalid tokens. Revoking a JWT requires techniques like denylists or allowlists, which can complicate the authentication process and may not always be foolproof.

To address these challenges, use short-lived JWT access tokens and refresh them regularly. This reduces the risk of unauthorized access if a token is stolen or leaked. Additionally, implementing strong encryption and secure token storage can further enhance JWT-based authentication security.

By default, the Choreo Developer Portal sets the token lifespan to 15 minutes (900 seconds). Application developers can increase this time if necessary, but it is recommended to keep it as short as possible.

# Manage Subscriptions

{% include "create-a-subscription.md" %}


# Share Applications

Choreo's application-sharing feature allows you to share your applications with members within your organization. This promotes collaboration when multiple members need to work on the same application.

Follow these steps to share an application with members of your organization:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev/) and click the **Applications** tab.

2. On the **Applications** page, click on the application you want to share.

3. On the **Application Overview** page, click the **Share** button on the right side.

4. In the **Share Application** dialog, enter the email addresses of the members you want to share the application with.

    !!! note
        You must type an email address and press **Enter** to add it.

5. Click **Confirm**. The application will be shared in read-only mode with the specified members.

To view the members with whom the application is shared, go to the **Application Overview** page and check the email addresses listed in the **Shared with** field.





To use a published API in your application, you must subscribe to it. When you subscribe to an API, your subscription covers all minor versions within the API's major version.

The subscription process ensures secure authentication of API requests using application keys. While you can generate credentials for an API without subscribing to an application, this approach limits advanced configuration options such as access token expiry time, revoke token expiry time, ID token expiry time, and enabling access to the API without a secret. Generating keys directly in the API is suitable for testing or short-term use but is not recommended for long-term production usage.

To subscribe to an API via an application, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. To navigate to applications, in the Developer Portal header, click **Applications**.

3. On the **My Applications** page, click on the application you want to use to subscribe to an API.

4. In the left navigation menu, click **Subscriptions**.

5. In the **Subscription Management** pane, click **+ Add APIs**.

6. Click **Add** to subscribe to an API. You can subscribe to one or more APIs based on your requirements.

    !!! tip
        When a new minor version of an API is published, the major version-based invocation URL automatically routes to the latest minor version within the subscribed API's major version. This ensures that existing client applications continue to function without disruption while benefiting from improvements or additions in the newer minor version.

    ![Add APIs](../assets/img/consume/add-apis.png)

Once you subscribe to an API, you can invoke it using the application keys.



An application in Choreo is a logical representation of a physical application, such as a mobile app, web app, or device. To consume an API in Choreo, you need to create an application that maps to your physical application and subscribe to the required API under a usage policy plan. This plan provides a usage quota. A single application can have multiple API subscriptions. Using the consumer key and consumer secret, you can generate an access token to invoke all APIs subscribed to the same application.

This guide walks you through the steps to create an application in Choreo.

## Step 1: Create an application

To create an application in the Choreo Developer Portal, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. In the Developer Portal header, click **Applications** and then click **+Create**.

3. Enter application details. Provide a name and description for your application.

4. Click **Create**.

This creates the application and opens the **Application Overview** page. Here, you can view details such as the token type, workflow status, and the application owner.

## Step 2: Generate keys

Choreo uses OAuth 2.0 bearer token-based authentication for API access. An API access token is a string passed as an HTTP header in API requests to authenticate access.

Once you create an application, you can generate credentials for it. Choreo provides a consumer key and consumer secret when you generate credentials for the first time. The consumer key acts as the unique identifier for the application and is used for authentication.

### Generate environment-specific keys and tokens

You can generate keys and tokens to invoke production and non-production endpoints separately.

!!! info "Note"
    Access to production endpoints depends on your role. If you have the necessary permissions, you can generate keys and tokens for production endpoints.

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Expand **Advanced configurations** and review the following options:
    - **Grant types**: Select the grant types to use when generating the access token.
    - **Public client**: Enable **Allow authentication without the client secret** if your application is a public client (e.g., a browser or mobile app).
    - **PKCE for enhanced security**: Set to **Mandatory** if you want the application to send a code challenge in the authorization request and a code verifier in the token request. Asgardeo supports SHA-256 and plain.
    - **Application access token expiry time**: Set the access token expiry time in seconds.
    - **Refresh token expiry time**: Set the refresh token expiry time in seconds.
    - **ID token expiry time**: Set the ID token expiry time in seconds.

5. Click **Generate Credentials**. The **Application Keys** pane will display the consumer key and consumer secret.

You can use the consumer key and consumer secret to generate an API access token by invoking the token endpoint. You can also revoke the access token by invoking the revoke endpoint.

To generate a test token for testing purposes, click **Generate Token** and copy the displayed token. Alternatively, click **cURL** to copy the generated cURL command and obtain a test token using a cURL client.

!!! warning
    Do not use the test token in your production environment.


Choreo is a powerful platform that enables developers to create, deploy, and consume services efficiently. The Choreo Developer Portal simplifies API discovery and usage, allowing developers to integrate APIs seamlessly into their applications.

This guide is intended for application developers (both internal and external) who wish to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

---

## Prerequisites

Before proceeding, ensure you have access to a published service to consume. If you do not have one, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) guide to create and deploy a sample REST API.

---

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: Visible to all users in the Developer Portal.
- **Private**: Accessible only to signed-in users.
- **Restricted**: Available to users with specific roles, enabling granular access control.

For more details, refer to [Control API Visibility](../api-management/control-api-visibility.md).

### Viewing Available APIs

The Developer Portal lists APIs categorized by their major versions. The API overview page displays:

- Subscribed versions of the API
- Subscription details (e.g., application name and creation date)

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

### Selecting the Correct API Version

> **Tip:** It is recommended to use the latest version of an API. Copy the **Endpoint(s)** from the API overview page and integrate it into your client application to ensure compatibility with the most recent updates.

---

# Generate an Access Token

Using access tokens for request authorization enhances security by preventing certain types of denial-of-service (DoS) attacks on published APIs. API consumers generate access tokens to access APIs, including them as string values in HTTP header requests.

When you register an application in the Developer Portal, you can generate a consumer key and consumer secret. These credentials represent the application's identity. The consumer key acts as the unique identifier for the application, similar to a username, and is used to authenticate API requests. Choreo issues an access token for the application based on the consumer key.

This guide walks you through the steps to generate an access token for your application in Choreo.

## Prerequisites

Before proceeding, ensure you have the following:

1. An application in the [Choreo Developer Portal](https://devportal.choreo.dev). If you don’t have one, [create a new application](https://wso2.com/choreo/docs/consuming-services/manage-application/#step-1-create-an-application).
2. [Generate keys for the application](https://wso2.com/choreo/docs/consuming-services/create-an-application/#step-2-generate-keys).
3. [Subscribe APIs to the application](https://wso2.com/choreo/docs/consuming-services/create-a-subscription/#manage-subscriptions).

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.


# Manage API Keys

To access a published API secured with an API Key, you need to generate a dedicated API Key for that specific API. This key acts as a unique identifier, enabling authorized usage while maintaining security and control over how the API is consumed.  

Once created, API Keys can be managed through two locations within the Choreo Developer Portal:

- **Credentials section of the API**: This section provides an overview of all API Keys associated with the specific API, enabling API owners to monitor and manage access.
- **Credentials section of the Application**: This section allows application owners to view and manage all API Keys linked to their application, ensuring they have control over API subscriptions and access.

From these sections, you can perform various API Key management actions, such as regenerating and deleting.

## API Key Regeneration

API Key regeneration allows you to obtain a new secret key for an existing API Key while ensuring minimal disruption to service. When an API Key is regenerated, a new secret key is generated, and the existing key remains valid for a grace period of one hour before being revoked. This ensures that applications have sufficient time to update their credentials without experiencing service interruptions.

!!! warning
    Ensure that all applications using the existing API Key are updated with the newly generated key within the grace period to prevent any disruptions in API invocations.

## API Key Deletion

API Keys can be deleted when they are no longer needed. Deleting an API Key immediately revokes its access, preventing further use of the key for API invocations. This action is irreversible and should be performed with caution, as any application relying on the deleted API Key will lose access to the API immediately.

# Manage Applications

{% include "create-an-application.md" %}

## Grant types

Choreo uses OAuth 2.0 for authentication. In OAuth 2.0, grant types are methods that allow client applications to obtain an access token. The type of grant used depends on the resource owner, the application type, and the trust relationship between the authorization server and the resource owner.

### Authorization code grant

The Authorization Code flow is a secure way for a client application to obtain an access token without exposing the user's credentials. The user authenticates with the authorization server, which issues an authorization code. This code is then exchanged for an access token.

This method protects user credentials and prevents them from being compromised by malicious client applications.

### Refresh token grant

A refresh token allows you to obtain a new access token when the current one expires or when a new token is needed. The refresh token grant type is used for this purpose. Refresh tokens are optional and, if issued, are included in the response along with the access token. You can use the refresh token to request a new access token from the authorization server. Choreo's default authorization server, Asgardeo, issues refresh tokens for all grant types except the **Client Credentials** grant type, as recommended by the OAuth 2.0 specification.

!!! note
    - Treat refresh tokens as securely as access tokens.
    - No user interaction is required to obtain a new access token using the Refresh Token grant type.

### Client credentials grant

The Client Credentials flow allows client applications to obtain an access token without user authentication. This is useful when the client application needs to access its own resources, such as data storage or APIs, but does not require access to user data. Ensure that client credentials are kept secure, as anyone with these credentials can obtain access tokens and access the client's resources.

### Implicit grant

The Implicit Grant flow allows a client application to obtain an access token directly from the authorization server without an intermediate authorization code exchange. This flow is commonly used in browser-based applications.

However, the access token is exposed in the browser's URL fragment, making it vulnerable to attacks like cross-site scripting (XSS). As a result, this flow is not recommended for applications requiring high security.

### Password grant

The Password Grant flow allows a client application to obtain an access token by directly providing the user's username and password to the authorization server. This method is less secure than other grant types because the client application handles and transmits the user's credentials.

This grant type is typically used in highly trusted client applications where user experience is prioritized over security. It is not recommended for public-facing applications or scenarios involving sensitive data.

## Revoke access tokens

Revoking JWT access tokens can be challenging because they are self-validating. Once issued, a token contains all the information needed to validate its authenticity without requiring server-side lookups.

It is recommended to set an expiry time of no more than 900 seconds.

In traditional session-based authentication, the server can revoke a session by invalidating its session ID. However, JWTs do not rely on a central authority to track valid or invalid tokens. Revoking a JWT requires techniques like denylists or allowlists, which can complicate the authentication process and may not always be foolproof.

To address these challenges, use short-lived JWT access tokens and refresh them regularly. This reduces the risk of unauthorized access if a token is stolen or leaked. Additionally, implementing strong encryption and secure token storage can further enhance JWT-based authentication security.

By default, the Choreo Developer Portal sets the token lifespan to 15 minutes (900 seconds). Application developers can increase this time if necessary, but it is recommended to keep it as short as possible.

# Manage Subscriptions

{% include "create-a-subscription.md" %}


# Share Applications

Choreo's application-sharing feature allows you to share your applications with members within your organization. This promotes collaboration when multiple members need to work on the same application.

Follow these steps to share an application with members of your organization:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev/) and click the **Applications** tab.

2. On the **Applications** page, click on the application you want to share.

3. On the **Application Overview** page, click the **Share** button on the right side.

4. In the **Share Application** dialog, enter the email addresses of the members you want to share the application with.

    !!! note
        You must type an email address and press **Enter** to add it.

5. Click **Confirm**. The application will be shared in read-only mode with the specified members.

To view the members with whom the application is shared, go to the **Application Overview** page and check the email addresses listed in the **Shared with** field.





To use a published API in your application, you must subscribe to it. When you subscribe to an API, your subscription covers all minor versions within the API's major version.

The subscription process ensures secure authentication of API requests using application keys. While you can generate credentials for an API without subscribing to an application, this approach limits advanced configuration options such as access token expiry time, revoke token expiry time, ID token expiry time, and enabling access to the API without a secret. Generating keys directly in the API is suitable for testing or short-term use but is not recommended for long-term production usage.

To subscribe to an API via an application, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. To navigate to applications, in the Developer Portal header, click **Applications**.

3. On the **My Applications** page, click on the application you want to use to subscribe to an API.

4. In the left navigation menu, click **Subscriptions**.

5. In the **Subscription Management** pane, click **+ Add APIs**.

6. Click **Add** to subscribe to an API. You can subscribe to one or more APIs based on your requirements.

    !!! tip
        When a new minor version of an API is published, the major version-based invocation URL automatically routes to the latest minor version within the subscribed API's major version. This ensures that existing client applications continue to function without disruption while benefiting from improvements or additions in the newer minor version.

    ![Add APIs](../assets/img/consume/add-apis.png)

Once you subscribe to an API, you can invoke it using the application keys.



An application in Choreo is a logical representation of a physical application, such as a mobile app, web app, or device. To consume an API in Choreo, you need to create an application that maps to your physical application and subscribe to the required API under a usage policy plan. This plan provides a usage quota. A single application can have multiple API subscriptions. Using the consumer key and consumer secret, you can generate an access token to invoke all APIs subscribed to the same application.

This guide walks you through the steps to create an application in Choreo.

## Step 1: Create an application

To create an application in the Choreo Developer Portal, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. In the Developer Portal header, click **Applications** and then click **+Create**.

3. Enter application details. Provide a name and description for your application.

4. Click **Create**.

This creates the application and opens the **Application Overview** page. Here, you can view details such as the token type, workflow status, and the application owner.

## Step 2: Generate keys

Choreo uses OAuth 2.0 bearer token-based authentication for API access. An API access token is a string passed as an HTTP header in API requests to authenticate access.

Once you create an application, you can generate credentials for it. Choreo provides a consumer key and consumer secret when you generate credentials for the first time. The consumer key acts as the unique identifier for the application and is used for authentication.

### Generate environment-specific keys and tokens

You can generate keys and tokens to invoke production and non-production endpoints separately.

!!! info "Note"
    Access to production endpoints depends on your role. If you have the necessary permissions, you can generate keys and tokens for production endpoints.

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Expand **Advanced configurations** and review the following options:
    - **Grant types**: Select the grant types to use when generating the access token.
    - **Public client**: Enable **Allow authentication without the client secret** if your application is a public client (e.g., a browser or mobile app).
    - **PKCE for enhanced security**: Set to **Mandatory** if you want the application to send a code challenge in the authorization request and a code verifier in the token request. Asgardeo supports SHA-256 and plain.
    - **Application access token expiry time**: Set the access token expiry time in seconds.
    - **Refresh token expiry time**: Set the refresh token expiry time in seconds.
    - **ID token expiry time**: Set the ID token expiry time in seconds.

5. Click **Generate Credentials**. The **Application Keys** pane will display the consumer key and consumer secret.

You can use the consumer key and consumer secret to generate an API access token by invoking the token endpoint. You can also revoke the access token by invoking the revoke endpoint.

To generate a test token for testing purposes, click **Generate Token** and copy the displayed token. Alternatively, click **cURL** to copy the generated cURL command and obtain a test token using a cURL client.

!!! warning
    Do not use the test token in your production environment.


Choreo is a powerful platform that enables developers to create, deploy, and consume services efficiently. The Choreo Developer Portal simplifies API discovery and usage, allowing developers to integrate APIs seamlessly into their applications.

This guide is intended for application developers (both internal and external) who wish to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

---

## Prerequisites

Before proceeding, ensure you have access to a published service to consume. If you do not have one, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) guide to create and deploy a sample REST API.

---

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: Visible to all users in the Developer Portal.
- **Private**: Accessible only to signed-in users.
- **Restricted**: Available to users with specific roles, enabling granular access control.

For more details, refer to [Control API Visibility](../api-management/control-api-visibility.md).

### Viewing Available APIs

The Developer Portal lists APIs categorized by their major versions. The API overview page displays:

- Subscribed versions of the API
- Subscription details (e.g., application name and creation date)

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

### Selecting the Correct API Version

> **Tip:** It is recommended to use the latest version of an API. Copy the **Endpoint(s)** from the API overview page and integrate it into your client application to ensure compatibility with the most recent updates.

---

# Generate an Access Token

Using access tokens for request authorization enhances security by preventing certain types of denial-of-service (DoS) attacks on published APIs. API consumers generate access tokens to access APIs, including them as string values in HTTP header requests.

When you register an application in the Developer Portal, you can generate a consumer key and consumer secret. These credentials represent the application's identity. The consumer key acts as the unique identifier for the application, similar to a username, and is used to authenticate API requests. Choreo issues an access token for the application based on the consumer key.

This guide walks you through the steps to generate an access token for your application in Choreo.

## Prerequisites

Before proceeding, ensure you have the following:

1. An application in the [Choreo Developer Portal](https://devportal.choreo.dev). If you don’t have one, [create a new application](https://wso2.com/choreo/docs/consuming-services/manage-application/#step-1-create-an-application).
2. [Generate keys for the application](https://wso2.com/choreo/docs/consuming-services/create-an-application/#step-2-generate-keys).
3. [Subscribe APIs to the application](https://wso2.com/choreo/docs/consuming-services/create-a-subscription/#manage-subscriptions).

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.


# Manage API Keys

To access a published API secured with an API Key, you need to generate a dedicated API Key for that specific API. This key acts as a unique identifier, enabling authorized usage while maintaining security and control over how the API is consumed.  

Once created, API Keys can be managed through two locations within the Choreo Developer Portal:

- **Credentials section of the API**: This section provides an overview of all API Keys associated with the specific API, enabling API owners to monitor and manage access.
- **Credentials section of the Application**: This section allows application owners to view and manage all API Keys linked to their application, ensuring they have control over API subscriptions and access.

From these sections, you can perform various API Key management actions, such as regenerating and deleting.

## API Key Regeneration

API Key regeneration allows you to obtain a new secret key for an existing API Key while ensuring minimal disruption to service. When an API Key is regenerated, a new secret key is generated, and the existing key remains valid for a grace period of one hour before being revoked. This ensures that applications have sufficient time to update their credentials without experiencing service interruptions.

!!! warning
    Ensure that all applications using the existing API Key are updated with the newly generated key within the grace period to prevent any disruptions in API invocations.

## API Key Deletion

API Keys can be deleted when they are no longer needed. Deleting an API Key immediately revokes its access, preventing further use of the key for API invocations. This action is irreversible and should be performed with caution, as any application relying on the deleted API Key will lose access to the API immediately.

# Manage Applications

{% include "create-an-application.md" %}

## Grant types

Choreo uses OAuth 2.0 for authentication. In OAuth 2.0, grant types are methods that allow client applications to obtain an access token. The type of grant used depends on the resource owner, the application type, and the trust relationship between the authorization server and the resource owner.

### Authorization code grant

The Authorization Code flow is a secure way for a client application to obtain an access token without exposing the user's credentials. The user authenticates with the authorization server, which issues an authorization code. This code is then exchanged for an access token.

This method protects user credentials and prevents them from being compromised by malicious client applications.

### Refresh token grant

A refresh token allows you to obtain a new access token when the current one expires or when a new token is needed. The refresh token grant type is used for this purpose. Refresh tokens are optional and, if issued, are included in the response along with the access token. You can use the refresh token to request a new access token from the authorization server. Choreo's default authorization server, Asgardeo, issues refresh tokens for all grant types except the **Client Credentials** grant type, as recommended by the OAuth 2.0 specification.

!!! note
    - Treat refresh tokens as securely as access tokens.
    - No user interaction is required to obtain a new access token using the Refresh Token grant type.

### Client credentials grant

The Client Credentials flow allows client applications to obtain an access token without user authentication. This is useful when the client application needs to access its own resources, such as data storage or APIs, but does not require access to user data. Ensure that client credentials are kept secure, as anyone with these credentials can obtain access tokens and access the client's resources.

### Implicit grant

The Implicit Grant flow allows a client application to obtain an access token directly from the authorization server without an intermediate authorization code exchange. This flow is commonly used in browser-based applications.

However, the access token is exposed in the browser's URL fragment, making it vulnerable to attacks like cross-site scripting (XSS). As a result, this flow is not recommended for applications requiring high security.

### Password grant

The Password Grant flow allows a client application to obtain an access token by directly providing the user's username and password to the authorization server. This method is less secure than other grant types because the client application handles and transmits the user's credentials.

This grant type is typically used in highly trusted client applications where user experience is prioritized over security. It is not recommended for public-facing applications or scenarios involving sensitive data.

## Revoke access tokens

Revoking JWT access tokens can be challenging because they are self-validating. Once issued, a token contains all the information needed to validate its authenticity without requiring server-side lookups.

It is recommended to set an expiry time of no more than 900 seconds.

In traditional session-based authentication, the server can revoke a session by invalidating its session ID. However, JWTs do not rely on a central authority to track valid or invalid tokens. Revoking a JWT requires techniques like denylists or allowlists, which can complicate the authentication process and may not always be foolproof.

To address these challenges, use short-lived JWT access tokens and refresh them regularly. This reduces the risk of unauthorized access if a token is stolen or leaked. Additionally, implementing strong encryption and secure token storage can further enhance JWT-based authentication security.

By default, the Choreo Developer Portal sets the token lifespan to 15 minutes (900 seconds). Application developers can increase this time if necessary, but it is recommended to keep it as short as possible.

# Manage Subscriptions

{% include "create-a-subscription.md" %}


# Share Applications

Choreo's application-sharing feature allows you to share your applications with members within your organization. This promotes collaboration when multiple members need to work on the same application.

Follow these steps to share an application with members of your organization:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev/) and click the **Applications** tab.

2. On the **Applications** page, click on the application you want to share.

3. On the **Application Overview** page, click the **Share** button on the right side.

4. In the **Share Application** dialog, enter the email addresses of the members you want to share the application with.

    !!! note
        You must type an email address and press **Enter** to add it.

5. Click **Confirm**. The application will be shared in read-only mode with the specified members.

To view the members with whom the application is shared, go to the **Application Overview** page and check the email addresses listed in the **Shared with** field.





To use a published API in your application, you must subscribe to it. When you subscribe to an API, your subscription covers all minor versions within the API's major version.

The subscription process ensures secure authentication of API requests using application keys. While you can generate credentials for an API without subscribing to an application, this approach limits advanced configuration options such as access token expiry time, revoke token expiry time, ID token expiry time, and enabling access to the API without a secret. Generating keys directly in the API is suitable for testing or short-term use but is not recommended for long-term production usage.

To subscribe to an API via an application, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. To navigate to applications, in the Developer Portal header, click **Applications**.

3. On the **My Applications** page, click on the application you want to use to subscribe to an API.

4. In the left navigation menu, click **Subscriptions**.

5. In the **Subscription Management** pane, click **+ Add APIs**.

6. Click **Add** to subscribe to an API. You can subscribe to one or more APIs based on your requirements.

    !!! tip
        When a new minor version of an API is published, the major version-based invocation URL automatically routes to the latest minor version within the subscribed API's major version. This ensures that existing client applications continue to function without disruption while benefiting from improvements or additions in the newer minor version.

    ![Add APIs](../assets/img/consume/add-apis.png)

Once you subscribe to an API, you can invoke it using the application keys.



An application in Choreo is a logical representation of a physical application, such as a mobile app, web app, or device. To consume an API in Choreo, you need to create an application that maps to your physical application and subscribe to the required API under a usage policy plan. This plan provides a usage quota. A single application can have multiple API subscriptions. Using the consumer key and consumer secret, you can generate an access token to invoke all APIs subscribed to the same application.

This guide walks you through the steps to create an application in Choreo.

## Step 1: Create an application

To create an application in the Choreo Developer Portal, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. In the Developer Portal header, click **Applications** and then click **+Create**.

3. Enter application details. Provide a name and description for your application.

4. Click **Create**.

This creates the application and opens the **Application Overview** page. Here, you can view details such as the token type, workflow status, and the application owner.

## Step 2: Generate keys

Choreo uses OAuth 2.0 bearer token-based authentication for API access. An API access token is a string passed as an HTTP header in API requests to authenticate access.

Once you create an application, you can generate credentials for it. Choreo provides a consumer key and consumer secret when you generate credentials for the first time. The consumer key acts as the unique identifier for the application and is used for authentication.

### Generate environment-specific keys and tokens

You can generate keys and tokens to invoke production and non-production endpoints separately.

!!! info "Note"
    Access to production endpoints depends on your role. If you have the necessary permissions, you can generate keys and tokens for production endpoints.

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Expand **Advanced configurations** and review the following options:
    - **Grant types**: Select the grant types to use when generating the access token.
    - **Public client**: Enable **Allow authentication without the client secret** if your application is a public client (e.g., a browser or mobile app).
    - **PKCE for enhanced security**: Set to **Mandatory** if you want the application to send a code challenge in the authorization request and a code verifier in the token request. Asgardeo supports SHA-256 and plain.
    - **Application access token expiry time**: Set the access token expiry time in seconds.
    - **Refresh token expiry time**: Set the refresh token expiry time in seconds.
    - **ID token expiry time**: Set the ID token expiry time in seconds.

5. Click **Generate Credentials**. The **Application Keys** pane will display the consumer key and consumer secret.

You can use the consumer key and consumer secret to generate an API access token by invoking the token endpoint. You can also revoke the access token by invoking the revoke endpoint.

To generate a test token for testing purposes, click **Generate Token** and copy the displayed token. Alternatively, click **cURL** to copy the generated cURL command and obtain a test token using a cURL client.

!!! warning
    Do not use the test token in your production environment.


Choreo is a powerful platform that enables developers to create, deploy, and consume services efficiently. The Choreo Developer Portal simplifies API discovery and usage, allowing developers to integrate APIs seamlessly into their applications.

This guide is intended for application developers (both internal and external) who wish to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

---

## Prerequisites

Before proceeding, ensure you have access to a published service to consume. If you do not have one, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) guide to create and deploy a sample REST API.

---

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: Visible to all users in the Developer Portal.
- **Private**: Accessible only to signed-in users.
- **Restricted**: Available to users with specific roles, enabling granular access control.

For more details, refer to [Control API Visibility](../api-management/control-api-visibility.md).

### Viewing Available APIs

The Developer Portal lists APIs categorized by their major versions. The API overview page displays:

- Subscribed versions of the API
- Subscription details (e.g., application name and creation date)

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

### Selecting the Correct API Version

> **Tip:** It is recommended to use the latest version of an API. Copy the **Endpoint(s)** from the API overview page and integrate it into your client application to ensure compatibility with the most recent updates.

---

# Generate an Access Token

Using access tokens for request authorization enhances security by preventing certain types of denial-of-service (DoS) attacks on published APIs. API consumers generate access tokens to access APIs, including them as string values in HTTP header requests.

When you register an application in the Developer Portal, you can generate a consumer key and consumer secret. These credentials represent the application's identity. The consumer key acts as the unique identifier for the application, similar to a username, and is used to authenticate API requests. Choreo issues an access token for the application based on the consumer key.

This guide walks you through the steps to generate an access token for your application in Choreo.

## Prerequisites

Before proceeding, ensure you have the following:

1. An application in the [Choreo Developer Portal](https://devportal.choreo.dev). If you don’t have one, [create a new application](https://wso2.com/choreo/docs/consuming-services/manage-application/#step-1-create-an-application).
2. [Generate keys for the application](https://wso2.com/choreo/docs/consuming-services/create-an-application/#step-2-generate-keys).
3. [Subscribe APIs to the application](https://wso2.com/choreo/docs/consuming-services/create-a-subscription/#manage-subscriptions).

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.


# Manage API Keys

To access a published API secured with an API Key, you need to generate a dedicated API Key for that specific API. This key acts as a unique identifier, enabling authorized usage while maintaining security and control over how the API is consumed.  

Once created, API Keys can be managed through two locations within the Choreo Developer Portal:

- **Credentials section of the API**: This section provides an overview of all API Keys associated with the specific API, enabling API owners to monitor and manage access.
- **Credentials section of the Application**: This section allows application owners to view and manage all API Keys linked to their application, ensuring they have control over API subscriptions and access.

From these sections, you can perform various API Key management actions, such as regenerating and deleting.

## API Key Regeneration

API Key regeneration allows you to obtain a new secret key for an existing API Key while ensuring minimal disruption to service. When an API Key is regenerated, a new secret key is generated, and the existing key remains valid for a grace period of one hour before being revoked. This ensures that applications have sufficient time to update their credentials without experiencing service interruptions.

!!! warning
    Ensure that all applications using the existing API Key are updated with the newly generated key within the grace period to prevent any disruptions in API invocations.

## API Key Deletion

API Keys can be deleted when they are no longer needed. Deleting an API Key immediately revokes its access, preventing further use of the key for API invocations. This action is irreversible and should be performed with caution, as any application relying on the deleted API Key will lose access to the API immediately.

# Manage Applications

{% include "create-an-application.md" %}

## Grant types

Choreo uses OAuth 2.0 for authentication. In OAuth 2.0, grant types are methods that allow client applications to obtain an access token. The type of grant used depends on the resource owner, the application type, and the trust relationship between the authorization server and the resource owner.

### Authorization code grant

The Authorization Code flow is a secure way for a client application to obtain an access token without exposing the user's credentials. The user authenticates with the authorization server, which issues an authorization code. This code is then exchanged for an access token.

This method protects user credentials and prevents them from being compromised by malicious client applications.

### Refresh token grant

A refresh token allows you to obtain a new access token when the current one expires or when a new token is needed. The refresh token grant type is used for this purpose. Refresh tokens are optional and, if issued, are included in the response along with the access token. You can use the refresh token to request a new access token from the authorization server. Choreo's default authorization server, Asgardeo, issues refresh tokens for all grant types except the **Client Credentials** grant type, as recommended by the OAuth 2.0 specification.

!!! note
    - Treat refresh tokens as securely as access tokens.
    - No user interaction is required to obtain a new access token using the Refresh Token grant type.

### Client credentials grant

The Client Credentials flow allows client applications to obtain an access token without user authentication. This is useful when the client application needs to access its own resources, such as data storage or APIs, but does not require access to user data. Ensure that client credentials are kept secure, as anyone with these credentials can obtain access tokens and access the client's resources.

### Implicit grant

The Implicit Grant flow allows a client application to obtain an access token directly from the authorization server without an intermediate authorization code exchange. This flow is commonly used in browser-based applications.

However, the access token is exposed in the browser's URL fragment, making it vulnerable to attacks like cross-site scripting (XSS). As a result, this flow is not recommended for applications requiring high security.

### Password grant

The Password Grant flow allows a client application to obtain an access token by directly providing the user's username and password to the authorization server. This method is less secure than other grant types because the client application handles and transmits the user's credentials.

This grant type is typically used in highly trusted client applications where user experience is prioritized over security. It is not recommended for public-facing applications or scenarios involving sensitive data.

## Revoke access tokens

Revoking JWT access tokens can be challenging because they are self-validating. Once issued, a token contains all the information needed to validate its authenticity without requiring server-side lookups.

It is recommended to set an expiry time of no more than 900 seconds.

In traditional session-based authentication, the server can revoke a session by invalidating its session ID. However, JWTs do not rely on a central authority to track valid or invalid tokens. Revoking a JWT requires techniques like denylists or allowlists, which can complicate the authentication process and may not always be foolproof.

To address these challenges, use short-lived JWT access tokens and refresh them regularly. This reduces the risk of unauthorized access if a token is stolen or leaked. Additionally, implementing strong encryption and secure token storage can further enhance JWT-based authentication security.

By default, the Choreo Developer Portal sets the token lifespan to 15 minutes (900 seconds). Application developers can increase this time if necessary, but it is recommended to keep it as short as possible.

# Manage Subscriptions

{% include "create-a-subscription.md" %}


# Share Applications

Choreo's application-sharing feature allows you to share your applications with members within your organization. This promotes collaboration when multiple members need to work on the same application.

Follow these steps to share an application with members of your organization:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev/) and click the **Applications** tab.

2. On the **Applications** page, click on the application you want to share.

3. On the **Application Overview** page, click the **Share** button on the right side.

4. In the **Share Application** dialog, enter the email addresses of the members you want to share the application with.

    !!! note
        You must type an email address and press **Enter** to add it.

5. Click **Confirm**. The application will be shared in read-only mode with the specified members.

To view the members with whom the application is shared, go to the **Application Overview** page and check the email addresses listed in the **Shared with** field.





To use a published API in your application, you must subscribe to it. When you subscribe to an API, your subscription covers all minor versions within the API's major version.

The subscription process ensures secure authentication of API requests using application keys. While you can generate credentials for an API without subscribing to an application, this approach limits advanced configuration options such as access token expiry time, revoke token expiry time, ID token expiry time, and enabling access to the API without a secret. Generating keys directly in the API is suitable for testing or short-term use but is not recommended for long-term production usage.

To subscribe to an API via an application, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. To navigate to applications, in the Developer Portal header, click **Applications**.

3. On the **My Applications** page, click on the application you want to use to subscribe to an API.

4. In the left navigation menu, click **Subscriptions**.

5. In the **Subscription Management** pane, click **+ Add APIs**.

6. Click **Add** to subscribe to an API. You can subscribe to one or more APIs based on your requirements.

    !!! tip
        When a new minor version of an API is published, the major version-based invocation URL automatically routes to the latest minor version within the subscribed API's major version. This ensures that existing client applications continue to function without disruption while benefiting from improvements or additions in the newer minor version.

    ![Add APIs](../assets/img/consume/add-apis.png)

Once you subscribe to an API, you can invoke it using the application keys.



An application in Choreo is a logical representation of a physical application, such as a mobile app, web app, or device. To consume an API in Choreo, you need to create an application that maps to your physical application and subscribe to the required API under a usage policy plan. This plan provides a usage quota. A single application can have multiple API subscriptions. Using the consumer key and consumer secret, you can generate an access token to invoke all APIs subscribed to the same application.

This guide walks you through the steps to create an application in Choreo.

## Step 1: Create an application

To create an application in the Choreo Developer Portal, follow these steps:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.

2. In the Developer Portal header, click **Applications** and then click **+Create**.

3. Enter application details. Provide a name and description for your application.

4. Click **Create**.

This creates the application and opens the **Application Overview** page. Here, you can view details such as the token type, workflow status, and the application owner.

## Step 2: Generate keys

Choreo uses OAuth 2.0 bearer token-based authentication for API access. An API access token is a string passed as an HTTP header in API requests to authenticate access.

Once you create an application, you can generate credentials for it. Choreo provides a consumer key and consumer secret when you generate credentials for the first time. The consumer key acts as the unique identifier for the application and is used for authentication.

### Generate environment-specific keys and tokens

You can generate keys and tokens to invoke production and non-production endpoints separately.

!!! info "Note"
    Access to production endpoints depends on your role. If you have the necessary permissions, you can generate keys and tokens for production endpoints.

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Expand **Advanced configurations** and review the following options:
    - **Grant types**: Select the grant types to use when generating the access token.
    - **Public client**: Enable **Allow authentication without the client secret** if your application is a public client (e.g., a browser or mobile app).
    - **PKCE for enhanced security**: Set to **Mandatory** if you want the application to send a code challenge in the authorization request and a code verifier in the token request. Asgardeo supports SHA-256 and plain.
    - **Application access token expiry time**: Set the access token expiry time in seconds.
    - **Refresh token expiry time**: Set the refresh token expiry time in seconds.
    - **ID token expiry time**: Set the ID token expiry time in seconds.

5. Click **Generate Credentials**. The **Application Keys** pane will display the consumer key and consumer secret.

You can use the consumer key and consumer secret to generate an API access token by invoking the token endpoint. You can also revoke the access token by invoking the revoke endpoint.

To generate a test token for testing purposes, click **Generate Token** and copy the displayed token. Alternatively, click **cURL** to copy the generated cURL command and obtain a test token using a cURL client.

!!! warning
    Do not use the test token in your production environment.


Choreo is a powerful platform that enables developers to create, deploy, and consume services efficiently. The Choreo Developer Portal simplifies API discovery and usage, allowing developers to integrate APIs seamlessly into their applications.

This guide is intended for application developers (both internal and external) who wish to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

---

## Prerequisites

Before proceeding, ensure you have access to a published service to consume. If you do not have one, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) guide to create and deploy a sample REST API.

---

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: Visible to all users in the Developer Portal.
- **Private**: Accessible only to signed-in users.
- **Restricted**: Available to users with specific roles, enabling granular access control.

For more details, refer to [Control API Visibility](../api-management/control-api-visibility.md).

### Viewing Available APIs

The Developer Portal lists APIs categorized by their major versions. The API overview page displays:

- Subscribed versions of the API
- Subscription details (e.g., application name and creation date)

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

### Selecting the Correct API Version

> **Tip:** It is recommended to use the latest version of an API. Copy the **Endpoint(s)** from the API overview page and integrate it into your client application to ensure compatibility with the most recent updates.

---

# Generate an Access Token

Using access tokens for request authorization enhances security by preventing certain types of denial-of-service (DoS) attacks on published APIs. API consumers generate access tokens to access APIs, including them as string values in HTTP header requests.

When you register an application in the Developer Portal, you can generate a consumer key and consumer secret. These credentials represent the application's identity. The consumer key acts as the unique identifier for the application, similar to a username, and is used to authenticate API requests. Choreo issues an access token for the application based on the consumer key.

This guide walks you through the steps to generate an access token for your application in Choreo.

## Prerequisites

Before proceeding, ensure you have the following:

1. An application in the [Choreo Developer Portal](https://devportal.choreo.dev). If you don’t have one, [create a new application](https://wso2.com/choreo/docs/consuming-services/manage-application/#step-1-create-an-application).
2. [Generate keys for the application](https://wso2.com/choreo/docs/consuming-services/create-an-application/#step-2-generate-keys).
3. [Subscribe APIs to the application](https://wso2.com/choreo/docs/consuming-services/create-a-subscription/#manage-subscriptions).

## Generate an access token via curl

Follow these steps to generate an access token for your application using cURL:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate the token.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.

5. Use the following template and replace the placeholders with the values you copied:

    === "Format"
    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```

6. Run the curl command to generate an access token.

## Generate an access token via the Developer Portal UI (for testing)

To generate an access token for **testing purposes**, follow these steps:

1. In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.

2. On the **My Applications** page, click on the application for which you want to generate keys and tokens.

3. In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.

4. Click **Generate Token** to create a test access token.


# Manage API Keys

To access a published API secured with an API Key, you need to generate a dedicated API Key for that specific API. This key acts as a unique identifier, enabling authorized usage while maintaining security and control over how the API is consumed.  

Once created, API Keys can be managed through two locations within the Choreo Developer Portal:

- **Credentials section of the API**: This section provides an overview of all API Keys associated with the specific API, enabling API owners to monitor and manage access.
- **Credentials section of the Application**: This section allows application owners to view and manage all API Keys linked to their application, ensuring they have control over API subscriptions and access.

From these sections, you can perform various API Key management actions, such as regenerating and deleting.

## API Key Regeneration

API Key regeneration allows you to obtain a new secret key for an existing API Key while ensuring minimal disruption to service. When an API Key is regenerated, a new secret key is generated, and the existing key remains valid for a grace period of one hour before being revoked. This ensures that applications have sufficient time to update their credentials without experiencing service interruptions.

!!! warning
    Ensure that all applications using the existing API Key are updated with the newly generated key within the grace period to prevent any disruptions in API invocations.

## API Key Deletion

API Keys can be deleted when they are no longer needed. Deleting an API Key immediately revokes its access, preventing further use of the key for API invocations. This action is irreversible and should be performed with caution, as any application relying on the deleted API Key will lose access to the API immediately.

# Manage Applications

{% include "create-an-application.md" %}

## Grant types

Choreo uses OAuth 2.0 for authentication. In OAuth 2.0, grant types are methods that allow client applications to obtain an access token. The type of grant used depends on the resource owner, the application type, and the trust relationship between the authorization server and the resource owner.

### Authorization code grant

The Authorization Code flow is a secure way for a client application to obtain an access token without exposing the user's credentials. The user authenticates with the authorization server, which issues an authorization code. This code is then exchanged for an access token.

This method protects user credentials and prevents them from being compromised by malicious client applications.

### Refresh token grant

A refresh token allows you to obtain a new access token when the current one expires or when a new token is needed. The refresh token grant type is used for this purpose. Refresh tokens are optional and, if issued, are included in the response along with the access token. You can use the refresh token to request a new access token from the authorization server. Choreo's default authorization server, Asgardeo, issues refresh tokens for all grant types except the **Client Credentials** grant type, as recommended by the OAuth 2.0 specification.

!!! note
    - Treat refresh tokens as securely as access tokens.
    - No user interaction is required to obtain a new access token using the Refresh Token grant type.

### Client credentials grant

The Client Credentials flow allows client applications to obtain an access token without user authentication. This is useful when the client application needs to access its own resources, such as data storage or APIs, but does not require access to user data. Ensure that client credentials are kept secure, as anyone with these credentials can obtain access tokens and access the client's resources.

### Implicit grant

The Implicit Grant flow allows a client application to obtain an access token directly from the authorization server without an intermediate authorization code exchange. This flow is commonly used in browser-based applications.

However, the access token is exposed in the browser's URL fragment, making it vulnerable to attacks like cross-site scripting (XSS). As a result, this flow is not recommended for applications requiring high security.

### Password grant

The Password Grant flow allows a client application to obtain an access token by directly providing the user's username and password to the authorization server. This method is less secure than other grant types because the client application handles and transmits the user's credentials.

This grant type is typically used in highly trusted client applications where user experience is prioritized over security. It is not recommended for public-facing applications or scenarios involving sensitive data.

## Revoke access tokens

Revoking JWT access tokens can be challenging because they are self-validating. Once issued, a token contains all the information needed to validate its authenticity without requiring server-side lookups.

It is recommended to set an expiry time of no more than 900 seconds.

In traditional session-based authentication, the server can revoke a session by invalidating its session ID. However, JWTs do not rely on a central authority to track valid or invalid tokens. Revoking a JWT requires techniques like denylists or allowlists, which can complicate the authentication process and may not always be foolproof.

To address these challenges, use short-lived JWT access tokens and refresh them regularly. This reduces the risk of unauthorized access if a token is stolen or leaked. Additionally, implementing strong encryption and secure token storage can further enhance JWT-based authentication security.

By default, the Choreo Developer Portal sets the token lifespan to 15 minutes (900 seconds). Application developers can increase this time if necessary, but it is recommended to keep it as short as possible.

# Manage Subscriptions

{% include "create-a-subscription.md" %}


# Share Applications

Choreo's application-sharing feature allows you to share your applications with members within your organization. This promotes collaboration when multiple members need to work on the same application.

Follow these steps to share an application with members of your organization:

1. Go to the [Choreo Developer Portal](https://devportal.choreo.dev/) and click the **Applications** tab.

2. On the **Applications** page, click on the application you want to share.

3. On the **Application Overview** page, click the **Share** button on the right side.

4. In the **Share Application** dialog, enter the email addresses of the members you want to share the application with.

    !!! note
        You must type an email address and press **Enter** to add it.

5. Click **Confirm**. The application will be shared in read-only mode with the specified members.

To view the members with whom the application is shared, go to the **Application Overview** page and check the email addresses listed in the **Shared with** field.


