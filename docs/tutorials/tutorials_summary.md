Here is a summary of the given content, keeping the headings and minimizing data loss:

# Consume an OAuth2 Secured Service

This guide explains how application developers can consume APIs published in the Choreo Developer Portal. It covers discovering APIs, creating applications, generating credentials, subscribing to APIs, and consuming REST APIs via web applications. A prerequisite is having a published service, for which instructions are available in the "Develop a Service" documentation.

## Prerequisites

- If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

The Choreo Developer Portal allows searching for APIs by name. API visibility settings (Public, Private, Restricted) determine who can see them. The portal lists APIs by major version, and the API overview page displays subscribed versions and details. It's recommended to use the latest API version by copying the endpoint value.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

Consuming an API securely requires using an Identity Provider (IdP). The steps involve: creating a web application in Choreo, creating an OAuth application in the IdP, configuring the web application for authentication, and deploying it. This guide uses WSO2 Asgardeo as the IdP and a sample React SPA, choreo-samples/reading-list-app/reading-list-front-end, as the web application.

### Step 1: Create a web application component

Instructions detail creating a web application component in Choreo, connecting it to a GitHub repository (choreo-samples/reading-list-app/reading-list-front-end), and configuring the build process.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Steps are provided to configure the corresponding OAuth application in Asgardeo, including setting allowed grant types, redirect URLs, allowed origins, and access token type.

### Step 3: Configure the web application to connect to the IdP and invoke the service

To configure the front-end application:

1. On the web application component page, click **DevOps** in the left menu, then click **Configs and Secrets**.
2. Click **+ Create**.
3. Select the following options and click **Next**:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **Config Type**       | **Config Map**                          |
    | **Mount Type**        | **File Mount**                          |

4. Specify the following values:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **Config Name**       | **Web App Config**                      |
    | **Mount Path**        | **/usr/share/nginx/html/config.js**     |

5. Copy the following JSON configuration into the text area. Replace the placeholders with the values from earlier steps:

    ```javascript
    window.config = {
        redirectUrl: "<web-app-url>",
        asgardeoClientId: "<asgardeo-client-id>",
        asgardeoBaseUrl: "https://api.asgardeo.io/t/<your-org-name>",
        choreoApiUrl: "<reading-list-service-url>"
    };
    ```

    | **Field**             | **Description**                               |
    |-----------------------|-----------------------------------------------|
    | **redirectUrl**       | The web app URL you copied earlier.           |
    | **asgardeoClientId**  | The **Client ID** from the Asgardeo application. |
    | **asgardeoBaseUrl**   | The IdP API URL with your organization name (e.g., `https://api.asgardeo.io/t/<ORG_NAME>`). |
    | **choreoApiUrl**      | The **Reading List Service** URL from the endpoint table in the overview page. |

6. Click **Create**.

### Step 4: Deploy the web application

Instructions cover deploying the web application manually, obtaining the web app URL, and verifying successful hosting.

# Expose a Service as a Managed API

This tutorial explains how to expose a service as an API proxy using Choreo and publish it to the Choreo Developer Portal.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

## Step 1: Create an API proxy

You can create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. If you already have one or more components in your project, click **+ Create** under **Component Listing**. Otherwise, proceed to the next step.
3. Click the **API Proxy** card.
4. In the **Create an API Proxy** pane, click **Try with sample URL**.
5. Click **Next**.
6. Update the populated API proxy details with the following values:

    !!! info
        The **Name** field must be unique and cannot be changed after creation.

    | **Field**       | **Value**                                   |
    |-----------------|---------------------------------------------|
    | **Display Name**| `Swagger Petstore`                          |
    | **Name**        | `swagger-petstore`                          |
    | **Context**     | `api/v3`                                    |
    | **Version**     | `1.0`                                       |
    | **Target**      | `https://petstore3.swagger.io/api/v3`       |
    | **Access Mode** | **External**: API is publicly accessible    |

7. Click **Create**. This creates the component and takes you to the **Overview** page of the component.

To see the resources of the API proxy, go to the left navigation menu, click **Develop**, and then click **Resources**.

## Step 2: Deploy the API proxy

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**. This opens the **Configure & Deploy** pane.
3. Select **External** to make the API publicly accessible, and then click **Deploy**.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.
2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

## Step 6: Invoke the API

To generate credentials for the published API and invoke it via the Developer Portal, follow these steps:

1. In the **Lifecycle Management** pane, click **Go to DevPortal**. This takes you to the Petstore API published to the Choreo Developer Portal.
2. Generate credentials:
    1. In the Developer Portal left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates new tokens and populates the **Consumer Key** and **Consumer Secret** fields.
3. Invoke the API:
    1. In the Developer Portal left navigation menu, click **Try Out**.
    2. In the **Endpoint** list, select **Development** as the environment to try out the API.
    3. Click **Get Test Key**. This generates an access token.
    4. Expand the `GET /pet/findByStatus` operation and click **Try it out**.
    5. Select **available** as the status and click **Execute**.

# Secure an API with Role-Based Access Control

This tutorial details how to implement Role-Based Access Control (RBAC) for APIs using Choreo and Asgardeo. A scenario involving a user management service is presented, with HR managers having full access and HR officers having limited access.

## Scenario

An organization needs to implement a user management service to keep track of users. The service needs to perform the following operations:

- List existing users
- List a specific user
- Create new users
- Delete a user

There are two types of users in the organization:

- **Human resource manager (HR manager)**: Can perform all operations (list users, list a user, create users, and delete a user).
- **Human resource officer (HR officer)**: Can only list existing users and list a specific user.

## Implement role-based access control with Choreo and Asgardeo

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

### Step 1: Create an API proxy component and deploy it

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. To create an API proxy component, follow the instructions in [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy). This opens the **Resources** pane, where you can define resources for the API proxy.
3. In the **Resources** pane, add the following resources:
    - **GET** `/users`
    - **GET** `/users/{userID}`
    - **POST** `/users`
    - **DELETE** `/users/{userID}`
4. Remove the five default resources that start with `/*` by clicking the delete icon corresponding to each resource.
5. Click **Save**. The API resources will look like this:

6. In the left navigation menu, click **Deploy**.
7. Go to the **Build Area** card and click **Configure & Deploy**.
8. In the **Configure API Access Mode** pane, select **External** to make the API publicly accessible.
9. Click **Deploy**.

### Step 2: Apply permissions to resources and publish the API

1. On the **Deploy** page, go to the **Build Area** card and click **Security Settings**.
2. In the **Security Settings** pane, go to the **Permissions List** section and click **+ Add Permission(Scope)**.
3. Add the following permission values:
    - `get_user_list`
    - `get_user`
    - `create_user`
    - `delete_user`
4. In the **Permissions** section, assign permissions to resources as follows:

    | **Resource**             | **Permission** |
    |--------------------------|----------------|
    | **GET /users**           | `get_user_list`|
    | **GET /users/{userID}**  | `get_user`     |
    | **POST /users**          | `create_user`  |
    | **DELETE /users/{userID}**| `delete_user`  |

5. Click **Apply**.
6. Redeploy the API to apply the latest permissions:
    1. Go to the **Build Area** card and click **Configure & Deploy**.
    2. Select **External** as the access mode and click **Deploy**.
7. Promote the API to production:
    1. In the left navigation menu, click **Deploy**.
    2. Go to the **Development** card and click **Promote**.
    3. In the **Configure & Deploy** pane, click **Next** to promote the API to production.
8. Publish the API:
    1. In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2. In the **Lifecycle Management** pane, click **Publish**. This changes the API status to **Published**.

### Step 3: Subscribe to the published API

1. Go to the [API Developer Portal](https://devportal.choreo.dev/) and click **Applications** on the top menu.
2. Click **+Create**.
3. Enter `User Management App` as the **Application Name** and click **Create**.
4. In the Developer Portal left navigation menu, click **Production** under **Credentials**.
5. Expand **Advanced Configurations** and:
    1. Select **Code** as the grant type.
    2. Enter the hosted URL of the application as the **Callback URL**.
    3. Click **Generate Credentials**.
6. Subscribe to the API:
    1. In the Developer Portal left navigation menu, click **Subscriptions**.
    2. In the **Subscription Management** pane, click **Add APIs**.
    3. In the **Add APIs** list, go to the API you created and click **Add**.

### Step 4: Define roles and assign them to groups

1. In the Developer Portal left navigation menu, click **Production** under **Credentials**.
2. In the **Permissions** section, click **Manage Permissions**. This takes you to the **Roles** tab of the `User Management App` application in Asgardeo.
3. Add the following roles:
    - **admin**: Assign permissions `get_user_list`, `get_user`, `create_user`, and `delete_user`.
    - **user**: Assign permissions `get_user_list` and `get_user`.
4. Create groups and assign roles:
    - **HR-Manager**: Assign the **admin** role.
    - **HR-Officer**: Assign the **user** role.

### Step 5: Define users and assign them to groups

1. Define two users: `Cameron` and `Alex`. For instructions, see [Manage Users](https://wso2.com/asgardeo/docs/guides/users/manage-customers/#onboard-a-user) in the Asgardeo documentation.
2. Assign `Cameron` to the **HR-Manager** group and `Alex` to the **HR-Officer** group. For instructions, see [Assign Groups](https://wso2.com/asgardeo/docs/guides/users/manage-customers/#assign-groups).

### Step 6: Obtain an access token and try out the API

1. Construct the authorization URL as follows:

    ```
    <authorize_URL>?response_type=code&client_id=<clientID>&redirect_uri=<redirect_URL>&scope=<scopes>
    ```

    - Replace `<authorize_URL>` with the **Authorize Endpoint** URL.
    - Replace `<redirect_URL>` with the **Callback URL**.
    - Replace `<scopes>` with the applicable permissions (e.g., `get_user_list get_user` for `Alex`).
    - Replace `<clientID>` with the **Consumer Key**.

2. Open the constructed URL in a web browser and sign in with `Alex`'s credentials. Click **Allow** to approve the consent.
3. Copy the code from the callback URL and use it to replace `<code>` in the following cURL command:

    ```
    curl <token_url> -d "grant_type=authorization_code&code=<code>&redirect_uri=<redirect_uri>" -H "Authorization: Basic <base64(clientId:clientSecret)>"
    ```

    - Replace `<token_url>` with the **Token Endpoint** URL.
    - Replace `<redirect_uri>` with the **Callback URL**.
    - Replace `<base64(clientId:clientSecret)>` with the Base64-encoded value of `clientId:clientSecret`.

4. Extract the access token from the response.
5. Go to the [API Developer Portal](https://devportal.choreo.dev/) and try out the API using the access token. Observe that `Alex` can only access the following resources:
    - **GET /users**
    - **GET /users/{userID}**

    Attempting to access other resources will result in a scope validation error.

    Similarly, if you use `Cameron`'s credentials, you can access all four resources because the token includes all required permissions.