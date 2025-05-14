 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.












 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.


 # Consume an OAuth2 Secured Service

Choreo is a platform that allows you to create, deploy, and consume services seamlessly. The Choreo Developer Portal simplifies the process of discovering and using APIs for developers. 

This guide is designed for application developers (internal or external to your organization) who want to consume APIs published in the Developer Portal to build their applications. You will learn how to:

- Discover APIs
- Create an application and generate credentials
- Subscribe to an API
- Consume a published REST API via a web application

## Prerequisites

If you don’t already have a published service to consume, follow the [Develop a Service](../develop-components/develop-services/develop-a-service.md) documentation to publish and deploy a sample REST API.

## Discover APIs

In the Choreo Developer Portal, developers can search for APIs by name. APIs and services created and published through the Choreo Console are visible in the Developer Portal based on their visibility settings:

- **Public**: The API is visible to everyone in the Developer Portal.
- **Private**: The API is visible only to users who sign in to the Developer Portal.
- **Restricted**: The API is visible only to users with specific roles. This allows for fine-grained access control.

To learn more about API visibility, see [Control API Visibility](../api-management/control-api-visibility.md).

The Developer Portal lists APIs by their major version.

![Developer Portal APIs](../assets/img/consume/developer-portal-apis.png)

The API overview page displays subscribed versions of the API along with subscription details such as the application name and creation date.

![API overview](../assets/img/consume/api-overview.png)

!!! tip
    To use an API, it’s recommended to use the latest version. Copy the **Endpoint(s)** value from the API overview page and use it in your client application. This ensures your application always invokes the latest API version.

## Create an application

{% include "../consuming-services/create-an-application.md" %}

## Subscribe to an API

{% include "../consuming-services/create-a-subscription.md" %}

## Consume the API via your web application

To securely invoke the API/service, you need to use your Identity Provider (IdP). Follow these steps:

1. Create a web application in Choreo.
2. Create an OAuth application in the IdP.
3. Configure the web application to authenticate API/service invocations using the IdP.
4. Deploy the web application.

For this guide, you’ll use:
- **WSO2 Asgardeo** as the IdP.
- **[choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end)** as the web application. This is a React SPA that uses Axios to invoke the service. It is configured to work with the **[choreo-samples/reading-list-app/reading-list-service](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-service)**. You can modify this web application to work with your service or deploy the sample service in Choreo.

### Step 1: Create a web application component

!!! info
    You can use your own web application instead of the sample. For this guide, you’ll use the [choreo-samples/reading-list-app/reading-list-front-end](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end).

To host the front-end application in Choreo, create a web application component:

1. In the Choreo Console, select the project for the reading list application from the project list in the header.
2. Click **Create** under the **Component Listing** section.
3. On the **Web Application** card, click **Create**.
4. Enter the following details:

    | **Field**       | **Value**               |
    |-----------------|-------------------------|
    | **Name**        | `Reading List Web App`  |
    | **Description** | `Frontend application for the reading list service` |

5. Click **Next**.
6. Click **Authorize with GitHub** to connect Choreo to your GitHub account.
7. In the **Connect Repository** pane, enter the following:

    | **Field**             | **Value**                               |
    |-----------------------|-----------------------------------------|
    | **GitHub Account**    | Your account                            |
    | **GitHub Repository** | **`choreo-samples`**                    |
    | **Branch**            | **`main`**                              |
    | **Buildpack**         | **React** (since it’s a React app built with Vite) |
    | **Build Context Path**| **`reading-list-app/reading-list-front-end`** |
    | **Build Command**     | **`npm install && npm run build`**      |
    | **Build Output**      | **`dist`**                              |
    | **Node Version**      | **`18`**                                |

8. Click **Create**. This initializes the service with the GitHub repository and takes you to the **Overview** page.

### Step 2: Create an OAuth application in the IdP

To invoke the API/service, you need an access token. Create an OAuth application in the IdP (for example, Asgardeo) with the following settings:

- **Allowed grant types**: Code
- **Public client**: Enable this option.
- **Authorized redirect URLs**: Add the web app URL.
- **Allowed origins**: Add the same URLs as authorized redirect URLs.
- **Access Token**: Set to JWT.

Choreo uses Asgardeo as the default IdP. When you create an application in the Choreo Developer Portal, it automatically creates a corresponding application in Asgardeo. Follow these steps to configure the Asgardeo OAuth application:

1. Sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials as Choreo.
2. Ensure you’re in the same organization used in the Choreo Developer Portal.
3. In the Asgardeo Console, click **Applications** in the left navigation. You’ll see the **readingListApp** created by Choreo.
4. Click the edit icon to edit the application.
5. Go to the **Protocol** tab and make the following changes:
    1. Under **Allowed grant types**, select **Code**.
    2. Select the **Public client** checkbox.
    3. In **Authorized redirect URLs**, enter the web app URL and click **+** to add it.
    4. In **Allowed origins**, add the same URLs.
    5. Under **Access Token**, select **JWT** as the token type.
    6. Click **Update**.

### Step 3: Configure the web application to connect to the IdP and invoke the service

Update the web app configurations to invoke the **Reading List Service** REST API. These configurations are environment-specific. For this guide, we’ll configure the development environment.

!!! note
    The web app reads environment-specific configurations from the `window` object at runtime via the `config.js` file. You’ll mount this file for the development environment. Repeat this process for other environments as needed.

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

To deploy the web application:

1. In the left menu, click **Deploy**.
2. In the **Build Area** card, click **Deploy Manually**. Deployment may take a few minutes.
3. Once deployed, copy the **Web App URL** from the development environment card.
4. Navigate to the web app URL to verify it’s successfully hosted.

That’s it! You can now use a user from your IdP to sign in and invoke the service through your web application.


# Expose a Service as a Managed API

Choreo simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Choreo to expose a service as an API proxy and publish it to the Choreo Developer Portal for application developers to consume.

## Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

## Step 1: Create an API proxy

To create an API proxy, you can either upload an OpenAPI specification or provide an OpenAPI specification URL. In this tutorial, you will use a sample OpenAPI specification URL.

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

    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 3: Test the API proxy

You can test the API proxy in the development environment before promoting it to production. Choreo provides the following options to test your API proxy:
- OpenAPI Console
- cURL

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Choreo automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /pet/findByStatus` method and click **Try it Out** to test it.
4. Select **available** as the status and click **Execute**. You will see a response similar to the following:

    ![API proxy response](../assets/img/tutorials/api-proxy-response.png)

    This indicates that your API proxy is working as expected.

## Step 4: Promote the API proxy to production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 5: Publish the API proxy

1. In the left navigation menu, click **Manage** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Choreo Developer Portal.

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

Now you have successfully created, deployed, tested, and published an API proxy using Choreo.


# Secure an API with Role-Based Access Control

Role-based access control (RBAC) is a flexible and scalable approach to manage access to API resources. In this approach, each user or group is assigned a specific role that determines the permissions granted to perform operations on an API resource.

This tutorial explains how to implement RBAC using Choreo and Asgardeo. It includes a real-world scenario with instructions to create and publish an API proxy component in Choreo and apply role-based access control.

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

Let’s take a look at the steps to implement the scenario described above using Choreo and Asgardeo.

### Prerequisites

- If you're signing in to the Choreo Console for the first time, create an organization:
   1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in using your preferred method.
   2. Enter a unique organization name. For example, `Stark Industries`.
   3. Read and accept the privacy policy and terms of use.
   4. Click **Create**.

This creates the organization and opens the home page of the default project created for you.

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

    ![API resources](../assets/img/tutorials/role-based-auth/api-resources.png)

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

Now, application developers can discover the API, subscribe to it, and invoke it.

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

Now you have gained hands-on experience in implementing role-based access control with Choreo and Asgardeo.












