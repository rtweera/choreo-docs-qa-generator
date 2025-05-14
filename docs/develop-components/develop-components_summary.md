# Develop Components

This document provides guides for developing various types of components in Choreo.

## Bring Your Own Image (BYOI)

Choreo allows deploying and managing prebuilt container images from external registries as components, offering flexibility in managing container images. This feature is available on private data planes (PDPs) for Service, Web Application, Scheduled Task, and Manual Task components.

### Prerequisites

- A container registry.
- An image in the registry.
- (Optional) An external build/CI pipeline.

Choreo cannot create images from source code or initiate new deployments automatically. However, deployments can be triggered via a webhook.

### Step 1: Register a container registry

Establish a connection between your container registry and Choreo by providing registry details and authentication information. Choreo uses these credentials to facilitate your data plane's ability to retrieve images without pulling them into the control plane.

**Authentication types**:
- Public (anonymous) access
- Basic authentication
- Docker config
- Vendor-specific authentication

### Step 2: Create a component in Choreo

Create a component, select the **Container Registry** as the source, choose the registered registry, and enter the image URL.

### Step 3: Deploy the component in Choreo

Deploy the component by updating the image and setting network visibility. You can update the image tag or URL during deployment.

### Step 4: Expose service endpoints

For service components, define endpoints by editing the `endpoints.yaml` file or uploading API specification/schema files.

### Auto-deploy images with an external CI/build pipeline

Integrate your CI pipelines to trigger deployments on Choreo using webhooks.

## Configure Endpoints

Services and integrations are exposed through endpoints, which define port binding, protocol, network visibility, and schema. Endpoints can be configured using the Choreo Console or a `component.yaml` file. They can also be exposed as managed APIs for secure and controlled access.

## Deploy a Containerized Application

Choreo supports deploying containerized applications for various component types using Dockerfiles.

### Connect your repository to Choreo

Authorize the Choreo Apps GitHub application for repository access. Alternatively, you can connect a public repository without authorization.

### Deploy the containerized component

Choreo applies deployment configurations based on the component type. You can run unit tests in the build pipeline by adding the relevant commands to the Dockerfile.

### Application configurations

Provide necessary configurations in the **Configs & Secrets** section, choosing between ConfigMaps and Secrets for storing data and specifying how to mount them (environment variables or file mounts).

### Deployment configurations

Configure deployment settings such as scaling, resource limits, and health checks.

### Build, deploy, and promote

Build and deploy manually, with the option for auto-deploy on commit. Choreo performs security vulnerability scans during the build process.

## Deploy an Application with Buildpacks

Choreo supports deploying applications with buildpacks for various component types. Buildpacks convert source code into container images without requiring a Dockerfile.

### Buildpacks
Choreo uses Google Buildpacks as default buildpacks for Java, Go, NodeJS, Python, PHP, and Ruby and its own buildpacks for Ballerina and WSO2 MI.

### Develop a component

Follow the guidelines based on your language, including the use of a `Procfile` to customize the container's entry point.

### Configure build-time environment variables

Configure environment variables for the build process using the **Build Configurations Editor**.

## Develop a Webhook

Choreo enables developers to design high-quality webhooks. A sample scenario is to notify software engineers via email whenever someone creates a GitHub issue with the `bug` label.

### Prerequisites

- Create an organization.
- Fork the Choreo samples repository.

### Step 1: Create a webhook component

Create a Webhook component and authorize with GitHub to connect Choreo to your GitHub account.

### Step 2: Deploy

Deploy the webhook to the development environment and set the webhook secret and email address.

### Step 3: Connect the webhook to the GitHub repository

Connect the webhook to the GitHub repository by specifying the invoke URL and setting up the events to trigger the webhook.

### Step 4: Test

Test the webhook by creating a GitHub issue with the `Bug` label in the repository.

### Step 5: Promote

Promote the webhook to the Production environment.

## Develop an External Consumer

An external consumer in Choreo is any client that can interact with services deployed in Choreo, as an entity hosted outside of the Choreo infrastructure.

### Prerequisites

- Create an organization.

### Step 1: Create an external consumer component

Create an external consumer component.

### Step 2: Manage authentication for the external consumer

You can configure the external consumer to work with the Choreo built-in identity provider or any external identity provider that supports OIDC/OAuth 2.0.

### Step 3: Connect the external consumer to a service deployed in Choreo

To establish connections from the external consumer to services deployed in Choreo, you can create connections.

## Develop Components Using VS Code

The [Choreo VS Code extension](https://marketplace.visualstudio.com/items?itemName=WSO2.choreo) provides comprehensive component management capabilities to streamline local development within Choreo.

### Prerequisites

1. [Visual Studio Code](https://code.visualstudio.com/download) installed with the [Choreo extension](https://marketplace.visualstudio.com/items?itemName=WSO2.choreo) version **2.0.0** or later.

2. A locally cloned GitHub repository to create new components or link to existing Choreo components.

3. [Git](https://git-scm.com) version 2.0.0 or later.

### Get started

To use the capabilities of the Choreo extension in the VS Code editor, you need an active [Choreo account](https://wso2.com/choreo/pricing/). If you already have an account, follow these steps to set up the extension:

1. Install the [Choreo VS Code extension](https://marketplace.visualstudio.com/items?itemName=WSO2.choreo) and wait for activation. On successful activation, the Choreo extension opens in the VS Code editor. 
2. Sign in to Choreo using one of the following methods:
    - In the Choreo activity pane, click **Sign In**.
    - Use the `Sign In` command provided by the Choreo extension.

    This redirects you to an external URI to complete the authentication process. On successful sign-in, the Choreo activity pane displays your account details along with any components detected within the VS Code workspace.

### Create a new component

1. Open the source code directory where you want to build, deploy, and manage components using Choreo.
2. Create a new component using one of the following methods:
    - In the Choreo activity pane, click **Create Component**.
    - Use the `Create New Component` command provided by the Choreo extension.

3. If the Choreo extension cannot determine the project context of the opened workspace, it prompts you to select the organization and the project to which the new component belongs.
4. Specify component details such as the name, type, buildpack, etc.

    On successful creation, the component details view opens, and the Choreo activity pane displays the new component.
     
    !!! tip
        Once the component is created, a `.choreo/context.yaml` file is generated in the root of the Git repository. For more details, see [Understand the project context](#understand-the-project-context).

The component details view allows you to manage your component by performing various actions such as the following:

 - Triggering builds for selected commits.
 - Viewing lists of builds and statuses.
 - Diagnosing build failures with build logs.
 - Deploying builds in available environments.
 - Accessing runtime logs and deployed component URLs.
 - Invoking deployed service endpoints.

### Understand the project context

Context files contain metadata related to the project, allowing the extension to establish an association between local directories and Choreo projects. These files, such as the `context.yaml`file, resides in the `/.choreo` directory within the root of the Git repository.

The Choreo extension scans the root of the opened Git repository to find the `context.yaml` file and lists the components of the associated project. This allows you to easily open and manage the components they are developing within the VS Code workspace.

A `context.yaml` file can contain multiple projects, whereas, a workspace opened via VS Code can have multiple `context.yaml` files with different project associations. In such cases, VS Code allows you to switch between these projects, add new project associations, or remove existing ones, allowing you as a developer to focus on components of a particular project at a time.

You can decide whether to commit the `context.yaml` file to the Git repository. Committing this file enables other team members working on the same repository to have a seamless developer experience with Choreo.

If the `context.yaml` file for a particular project is not committed to the Git repository or is unavailable for other reasons, you can easily regenerate it using one of the following methods:

 - In the Choreo activity pane, click **Link Directory**.
 - Use the `Link Directory` command provided by the Choreo extension.

### Discover additional features

To access a range of functionalities provided by the Choreo extension, open the VS Code command palette and type `Choreo`.

### Troubleshoot issues

To troubleshoot Choreo extension issues, follow these steps:

1. To open the **OUTPUT** pane, go to the VS Code editor main menu, click **View**, and then click **Output**.

2. Select **Choreo** from the drop-down menu on the right-hand side to view the Choreo output for troubleshooting.

### Get help

For assistance with the Choreo VS Code extension, create [GitHub issues](https://github.com/wso2/choreo-vscode/issues).

## Develop Components With Git

Choreo enables you to develop components by connecting your GitHub, Bitbucket, or GitLab repository. You have the flexibility to either connect an existing repository or start with an empty repository and commit the source code later. By integrating your repositories with Choreo, you can automate tasks and optimize workflows across multiple systems, all within the Choreo platform.  Choreo currently supports GitHub, Bitbucket, and GitLab as Git providers. 

Key benefits of this capability include:

  - **Code sharing without duplication**: Use submodules to maintain shared libraries across multiple projects, ensuring a single source of truth.
  - **Efficient third-party library management**: Manage third-party libraries as submodules to update them independently and track changes easily, avoiding direct code integration.

### Connect a Git repository to Choreo

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. Click the **Credentials** tab. 
5. Click **+Add Credentials** to configure the Git repository connection.
6. Enter a **Credential Name**, select the Git provider, and enter the **Personal Access Token** you obtained from the Git provider.
7. Click **Save**.  

### Authorize GitHub with Choreo 

Authorizing Choreo as a GitHub application grants Choreo permissions to perform actions on your behalf within the repository, including:

|Permission   | Read| Write| Description                                                           |
|-------------|-----|------|-----------------------------------------------------------------------|
|Issues       | Y   | N    | Read component ID label to filter the pull requests                   |
|Metadata     | Y   | N    | List repositories                                                     |
|Contents     | Y   | Y    | List branches and create a branch to commit sample code               |
|Pull Request | Y   | Y    | Create a pull request if you start with a Choreo sample               |
|Webhooks     | Y   | Y    | Trigger automatic deployment and configuration generation             |

### Add Git submodules to a project

Choreo provides [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) support when you connect your GitHub repository to Choreo. This allows you to manage and include external repositories effectively within Choreo build pipelines. 

For example, when you [work with the Micro Integrator (MI) runtime in Choreo](./work-with-the-micro-integrator-runtime-in-choreo.md), you can use Git submodules to reuse MI templates and sequences across components without duplication.

To enable this feature, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click the component for which you want to pull the latest versions of Git submodules.
3. In the left navigation menu, click **Build**.
4. On the **Build** page, click to edit **Build Configurations**.
5. Turn on the **Pull Latest Submodules** toggle.

#### Automatically pull latest versions of Git submodules

Choreo lets you automatically pull the latest versions of Git submodules from their respective repositories. 

!!! note 
    Choreo currently supports this feature only for components where the buildpack is **WSO2 MI**.

If you rebuild a previously built commit and it doesn’t reflect the latest changes, follow these steps to ensure the changes are applied to the deployed environment:

1. In the Choreo Console left navigation menu, click **DevOps**, then click **Containers**.
2. Click **Edit** to update the container settings.
3. Select **Always** as the **Image Pull Policy**.
4. Click **Save Changes**.

### Authorize Bitbucket with Choreo

Authorizing using a personal access token (PAT) from Bitbucket grants Choreo the following permissions to perform the respective actions on your behalf within the repository.

|Permission    | Read| Write| Description                                                        |
|--------------|-----|------|--------------------------------------------------------------------|
|Account       | Y   | N    | Get user information and workspace details                         |
|Repositories  | Y   | Y    | List branches and create a branch to commit sample code            |
|Pull Requests | Y   | Y    | Create a pull request if you start with a Choreo sample            |
|Webhooks      | Y   | Y    | Trigger automatic deployment and configuration generation          |

### Authorize self-managed GitLab with Choreo

Authorizing using a personal access token (PAT) obtained from your GitLab self-managed server grants Choreo the following permissions to perform the respective actions on your behalf within the repository.

|Permission    | Description                                                                         |
|--------------|-------------------------------------------------------------------------------------|
|API           | Grants full read/write access to the API, covering all groups and projects, as well as read/write access to the repository.|


 # Bring Your Own Image (BYOI)

Choreo allows you to deploy and manage prebuilt container images from external container registries as Choreo components. This enables you to deploy and effectively manage your container images within the Choreo environment.

!!! info
    This feature is currently only available on [private data planes (PDPs)](../choreo-concepts/data-planes.md#private-data-planes) for the following component types:

    - Service
    - Web Application
    - Scheduled Task
    - Manual Task


## Prerequisites

Before you try out this guide, ensure you have the following:

- **A container registry**: Ensure you have a container registry containing the images you want to deploy. Choreo is compatible with various container registries, including but not limited to GCR (Google Container Registry), ACR (Azure Container Registry), GitHub Container Registry, and Docker Hub.

- **An image in the registry**: You need an image ready for deployment.

- **(Optional) An external build/CI pipeline**:  This is to initiate automatic deployments during the build process outside of Choreo.

When using a container registry to deploy a component, Choreo cannot create an image from the source code (Git) or initiate a new deployment when a new image is ready. However, you can use your existing build process to trigger a deployment on Choreo by sending an HTTP POST request to a webhook with the new image details.

This feature is currently only available on private data planes (PDPs). You can find this option under **Deploy an image from a container registry** in the **Select Source** step during component creation for service components, web applications, scheduled tasks, and manual tasks.

## Step 1: Register a container registry

To get started, establish a connection between your container registry and Choreo. 

!!! Info
    When you use your Choreo credentials, Choreo does not *pull* your images into its control plane. Instead, it functions as an orchestrator, facilitating your data plane's ability to retrieve images from an external container registry. Choreo passes on these credentials to the data plane for authentication and access.

To register your container registry, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization settings page. 
4. Click the **Credentials** tab and then click the **Container Registries** tab. 
5. Click **+Add Registry** to configure the Git repository connection.
6. Specify a **Registry Display Name**.
7. Select the **Authentication Type**. Fill in the required information depending on your authentication type. For details on each authentication type, see [Authentication types](#authentication-types).
8. Click **Save**.

### Authentication types

Choreo provides the following authentication options:  

#### Public (anonymous) access
    
You can use this option to establish a connection with a container registry that permits unrestricted public or anonymous access (for example, Public Docker Hub). In this case, only the registry host information is necessary.

For example, the following are the Docker Hub registry hosts for reference:

| Vendor                           | Registry host                |
|----------------------------------|------------------------------|
|Docker Hub (public repositories)  | `registry.hub.docker.com`    |
|Docker Hub (private repositories) | `registry.docker.com`        |

\* If necessary, you can use other mirrors instead of the above.

#### Basic authentication

To use basic authentication to authenticate to the container registry, you must provide the username and password.

#### Docker config

You can provide a Docker config in JSON format to authenticate to the container registry. This option only allows you to register one container registry. That is, it **only allows a single registry under `auths`**.

You must provide the credentials directly within the configuration. Choreo cannot utilize references to executable authentication plugins.

Sample Docker config format:

```json
    {
    "auths": {
        "index.docker.io/v1/": {
        "auth": "c3R...zE2"
        }
    }
    }
```

#### Vendor-specific authentication

This option is specifically for private data planes, where your cloud provider manages authentication at the Kubernetes level. Choreo requires knowledge of the registry host because the data plane already possesses implicit (preconfigured) access to the registry.

Follow the guidelines below based on your container registry:

=== "ACR"
    **Azure Container Registry** 

    Recommended authentication options:

    * [**Service principal-based basic authentication**](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal)

    * **Vendor-specific authentication on Azure private data planes**
        
        Contact Choreo support to enable infrastructure-level private access to your registry from your Azure private data plane on AKS. If you are on a self-managed PDP on Azure, follow [this guide](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?toc=%2Fazure%2Fcontainer-registry%2Ftoc.json&bc=%2Fazure%2Fcontainer-registry%2Fbreadcrumb%2Ftoc.json&tabs=azure-cli).

=== "GAR"
    **Google Artifact Registry**

    Recommended authentication options:

    * [**Service account-based basic authentication**](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling#key)

        Use the service account key in JSON format ([`_json_key`](https://cloud.google.com/artifact-registry/docs/docker/authentication#:~:text=of%20the%20following%3A-,_json_key,-if%20you%20are)) as the username and specify the minified JSON contents of the service account key as the password.

         You can use `jq` as follows to minify the service account JSON key file:

         `jq -c . <service-account.json>`

    * **Vendor-specific authentication on GCP private data planes**

        Contact Choreo support to enable infrastructure-level private access to your registry from your GCP private data plane on GKE. If you are on a self-managed PDP on GCP, see [https://cloud.google.com/artifact-registry/docs/access-control#grant-project](https://cloud.google.com/artifact-registry/docs/access-control#grant-project).

=== "AWS ECR"
    **Elastic Container Registry**

    ECR does not allow the creation of static access passwords for basic authentication. The passwords (that is, access tokens) provided by AWS are only valid for 10 hours and must be manually regenerated. However, when an ECR is attached to an EKS cluster at an infrastructure level, this limitation does not apply because the authentication is handled by AWS internally. For details, see [https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html).

    Choreo recommends using ECR when you are exclusively on an AWS private data plane using the vendor-specific authentication option. Contact Choreo support to enable a private connection between your ECR and the underlying EKS clusters on your data plane. If you are on a self-managed PDP, you can follow [this guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_EKS.html).    

=== "Docker Hub (Private)"

    Recommended authentication options:

    * **Basic authentication**

          Use your Docker Hub username/password or an access token. You can generate an access token from your Docker Hub account settings and use it in place of the password. For details, see [https://docs.docker.com/docker-hub/access-tokens/](https://docs.docker.com/docker-hub/access-tokens/).

    * **Docker config**

          Sign in to the Docker CLI and copy the contents of the docker config JSON. Note that external credential stores and multiple repositories within the same config object are not supported. For more information, see [https://docs.docker.com/engine/reference/commandline/login/](https://docs.docker.com/engine/reference/commandline/login/).

=== "GHCR"
    **GitHub Container Registry**

    Recommended authentication option:

    * **Basic authentication using a PAT token**

          Create a personal access token (PAT) and use it in place of the password. You cannot use your own GitHub password. You must provide a [PAT token](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-with-a-personal-access-token-classicn).
  
## Step 2: Create a component in Choreo

1. In the left navigation, click **Overview** and select your project. Alternatively, select your project from the **Project** list in the Choreo Console header. 
2. Under **Component Listing** click **+ Create**.
3. Select your component type (BYOI is only available for Service, Web Application, Scheduled Task, or Manual Task components). 
4. From the Create Component pane, select the **Container Registry** under the **Connect a Docker Image** section.
5. Under **Deploy an image from Container Registry/Docker Hub**, select the container registry you have registered in [Step 1](#step-1-register-a-container-registry).
6. Enter the full image URL. The image URL format in general is as follows:
   `[container-registry-host]/[repository-name]/[image-name]:[tag]`

    !!! tip
        When a public image from Docker Hub lacks a specified repository name, it typically defaults to `/library/`. For example, you can access the public Nginx image `https://hub.docker.com/_/nginx` as `registry.hub.docker.com/library/nginx:1.25`.

7. Enter a display name, a unique name, and a description for the component.
    
    !!! info
         In the **Component Name** field, you must specify a name to uniquely identify the component in various contexts. The value is editable only at the time you create the component. You cannot change the name after you create the component.


## Step 3: Deploy the component in Choreo

To deploy the component and bring your image to Choreo, follow the steps given below: 

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Update Image & Deploy**. 
3. In the **Endpoint** pane that opens, you can see the endpoint ready to be deployed. Click the edit icon next to the endpoint name. Optionally, you can define the endpoints for your service when you manually deploy the service. For more information, see [Expose service endpoints](#step-4-expose-service-endpoints).
4. Change the **Network Visibility** to **Public**. This setting securely exposes the endpoint for consumption.
5. Click **Update**.

    !!! info
         In this example, you deploy a Ballerina service as a REST endpoint. Therefore, Choreo generated the REST endpoint automatically. If you deploy a non-Ballerina service, you must manually add the REST endpoint and set the network visibility to **Public**.

6. Select your update image option. Refer to the update options listed below.

    You have the capability of updating the image when you are deploying the component in Choreo in one of the following three ways:

    | Option                   |Description                                                                                             |
    |--------------------------|--------------------------------------------------------------------------------------------------------|
    | **Update Image Tag**     | This option allows you to update the tag of the image.                                                 |
    | **Update Image URL**     | With this option, you can change the image name, tag, and the image repository of the image URL.|
    | **Previous Images**      | This option allows you to select a previous image and redeploy the image.                               |

7. Click **Deploy**. This deploys the service to the development environment.

## Step 4: Expose service endpoints 

!!! info
    This section only applies to service components.

After creating a service component in Choreo, you have the option to define the endpoints for your service when manually deploying a new image.

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Update Image & Deploy**. 
3. In the **Endpoint** pane that opens, optionally, you can define the endpoints for your service when you manually deploy the service. 
4. Click  **Create/Update Endpoints**.
5. Under the **Edit endpoints.yaml** section, you can edit the endpoints YAML file in the provided editor. 
   Alternatively, you can upload the associated API specification/schema files (OpenAPI/GraphQL schemas). Instead of specifying the file path, you can also reference this file in the `endpoints.yaml` file by its file name, similar to the Git-based Choreo components. The endpoints template follows the standard definitions for defining endpoints in Choreo. For more details, see [Configure Endpoints](../develop-components/configure-endpoints.md).

## Auto-deploy images in Choreo with an external CI/build pipeline

Choreo does not have automatic detection and deployment for newly added images or tags in the linked container registry. To overcome this limitation, Choreo allows you to integrate your own CI pipelines and initiate deployments manually. This approach enables you to use your existing CI setup or build a pipeline for image creation and pushing. You can then trigger automatic deployments using a webhook.

Follow the steps below to configure your CI/build pipeline:

1. Build and push the container image associated with a Choreo component to your container registry.
2. In the left navigation menu, click **DevOps** and then click **External CI**.
3. Generate a token for your CI pipeline from the **Manage Tokens** section. 

    !!! note
        - The tokens are bound to a specific component.
        - It is recommended to reference the token from a secure location available to your CI pipeline. For example, use a GitHub secret if you are using GitHub Actions.

4. To trigger an automatic deployment to your development environment, you can initiate an HTTP POST request to the Choreo webhook endpoint with the updated image details. Alternatively, you can use the provided Webhook snippets. This action will seamlessly deploy the image to the development environment.



Services and integrations are exposed to other services, integrations, or applications through endpoints. A service or an integration can expose multiple endpoints, each representing a unique entry point into the service. For example, a service may expose a REST API endpoint and a GraphQL endpoint, each providing different ways to interact with the service. Endpoints provide specific details for how the service or the integration can be consumed. For instance, the port number, protocol, and the schema such as open API specification (OAS) or GraphQL schema. By defining these details, endpoints make it possible for other services, integrations, and applications to discover and interact with the service in a standardized way.

Choreo defines endpoints by combining port binding, protocol, endpoint name, network visibility, endpoint schema, and additional protocol-related fields. The following table describes each attribute of an endpoint.

| Field | Description |
| ----- | ----------- |
| Name | A unique identifier for the endpoint within the service component. |
| Port | The network port on which the endpoint is accessible. |
| Type | The endpoint protocol. Supported protocols: REST, GraphQL, gRPC, WS, UDP, and TCP. |
| Network Visibility | Determines the level of visibility of an endpoint. Possible values are: <ul><li>Project: Allows components within the same project to access the endpoint.</li><li>Organization: Allows any component within the same organization to access the endpoint but restricts access to components outside the organization.</li><li>Public: Allows any client to access the endpoint, regardless of location or organization.</li></ul> |
| Schema | Specifies the structure and format of the data exchanged through the endpoint. |
| Context (HTTP and GraphQL only) | A context path that you add to the endpoint's URL for routing purposes. |

## Configure endpoints
The method of defining endpoints depends on the buildpack.

* For `Ballerina` and `WSO2 MI` buildpacks, Choreo automatically detects the endpoint details for REST APIs.
* For all other buildpacks (Java, Python, NodeJS, Ruby, PHP, Go, Dockerfile, etc.), you can configure endpoints in one of the following ways:
  
    * **Using the Choreo Console**: If a `component.yaml` file is not present, you can define a basic endpoint configuration during component creation.
    * **Using the component.yaml file**: You can manually configure endpoint details by defining them in a `component.yaml` file, placing it inside the `.choreo` directory at the build context path, and committing it to the source repository.

You can override UI-defined and auto-generated endpoints by providing a `component.yaml` file in the `.choreo` directory, which will take priority over other configurations.

To learn about the `component.yaml` file, see [Overview of the component.yaml file](../develop-components/manage-component-source-configurations.md#overview-of-the-componentyaml-file).
!!! note
    Automatic endpoint generation is not supported for dynamic endpoint parameters such as variable ports. Therefore, you must use an `component.yaml` file to define dynamic endpoint parameters.

To learn about the `component.yaml` file, see [Overview of the component.yaml file](../develop-components/manage-component-source-configurations.md#overview-of-the-componentyaml-file).

## Expose endpoints as managed APIs

Exposing endpoints as managed APIs is crucial to ensure secure and controlled access to the services being exposed. When a user wants to expose their written service to the outside world or to the organization at large, there is an inherent security risk involved. To mitigate this risk, the Choreo platform is built with an internal (access within the organization only) or external (publicly accessible) gateway that is protected with Choreo API management making the services secure by design.

!!! note
    This feature is not available for gRPC, UDP, and TCP endpoints.

If you want to expose an endpoint as a managed API in Choreo, you need to set the network visibility to either Organization or Public. This allows the endpoint to be exposed through the Choreo API Gateway, which provides a number of benefits, including:

* Expose APIs to external and internal consumers
* Full lifecycle API Management
* API throttling
* Secure APIs with industry-standard authorization flows
* API analytics and monitoring

Once you deploy the service component, Choreo will expose the endpoint as a managed API through the Choreo API Gateway. You can then use the full lifecycle API management features provided by Choreo to test, deploy, maintain, monitor, and manage your API using the API management features.

## Understand the default component URL

The default URL of a component corresponds to the default endpoint of the component and is structured as follows:

`<domain>/<project-name>/<component-name>`

This URL does not include the default endpoint name. For all other endpoints, the URL structure includes the endpoint name, as follows:

`<domain>/<project-name>/<component-name>/<endpoint-name>`

If a component has multiple endpoints, Choreo allows you to change the endpoint corresponding to the default component URL. For a component with a single endpoint, the default URL automatically corresponds to that endpoint.

### Change the default endpoint of a component

To change the default endpoint of a component, follow the steps given below:

!!! note
     - You cannot change the default endpoint if it has associated published APIs. You must go to the **Lifecycle** page and unpublish the relevant APIs before updating the default endpoint. For instructions on unpublishing an API, see [Lifecycle Management](https://wso2.com/choreo/docs/api-management/lifecycle-management/).
     - Choreo does not allow you to change the default endpoint of a component if you create multiple deployment tracks within its current major version, or promote the component beyond its initial environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to change the default endpoint.
3. In the left navigation menu, click **Deploy**.
4. On the **Deploy** page, go to the **Set Up** card and click **Configure & Deploy**.
5. In the **Environment Configurations** pane that opens, click **Next**.
6. In the **File Mount** pane that opens, click **Next**.
7. In the **Endpoint Details** pane that opens, click the **Default Endpoint** list, select the endpoint you want to set as the default endpoint, and then click **Update**.
8. Click **Deploy**. This deploys the component with the selected endpoint as the default, and the default URL will now correspond to this endpoint.  

### Edit a UI-Defined Endpoint
If you defined an endpoint during component creation, you can edit it later by following these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update the endpoint.
3. In the left navigation menu, click **Deploy**.
4. On the **Deploy** page, go to the **Set Up** card and click **Configure & Deploy**.
5. In the **Environment Configurations** pane that opens, click **Next**.
6. In the **File Mount** pane that opens, click **Next**.
7. In the **Endpoint Details** pane that opens, locate the endpoint you want to edit.
8. Click the **Edit** icon next to the endpoint, modify the editable fields, and click **Update**.
9. Click **Deploy** to apply the changes.

!!! note
     If you commit a `component.yaml` file, build the component, and proceed with deployment, the endpoints will be generated from the `component.yaml` file and will take priority. In this case, the endpoint cannot be edited through the UI. To modify the endpoint, you must update the`component.yaml` file.


# Configure Endpoints
{% include "configure-endpoints-body.md" %}

# Deploy a Containerized Application 

Using Choreo, you can easily deploy applications written in different language frameworks (such as Java, Go, NodeJS