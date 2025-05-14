     # Choreo Marketplace

The Choreo Marketplace promotes and facilitates reusing and sharing services. It allows you to share all the services deployed in Choreo.
You can easily browse and search available services within the Marketplace and refer to the service definitions, documentation, instructions on how you can use it, etc. 

![Internal Marketplace](../assets/img/choreo-concepts/marketplace/internal-marketplace.png){.cInlineImage-full}

## Discover services

The Marketplace includes all services deployed in your organization. This may be a large number of services. Therefore, effective discoverability is desirable.

You can use the search or apply various filter criteria to explore the services available.

### Search

The top search bar provides universal searching to find the services. It allows you to search for a text in the following search attributes:

- **Name**: The service name.
- **Label**: The service labels.
- **Content**: The service content: overview, summary, and documentation.
- **All**: All of the above criteria.

### Filter

The Choreo Marketplace provides a filtering capability through the left-hand side filter panel. It allows you to filter with the following filter attributes:

- **Type**: This filter enables you to categorize services based on their type, with two available options: "Internal" and "Third-party". "Internal" refers to services deployed within Choreo, while "Third-party" refers to services running externally to Choreo, independently added to the Marketplace.

- **Network Visibility**: This filter enables you to categorize services based on their network visibility level, with three choices: "Public," "Organization," and "Project".  "Public" filters services exposed publicly, "Organization" represents services exposed across the entire organization, and "Project" represents services exposed at the project level.


## Explore a service 

You can click on the service card to open the detailed view of the service. The detailed service page features the service name, summary, version, labels, and service icon as the header.

Choreo organizes the service content into four tabs. The four tabs contain information as follows: 

- **Overview**: Choreo displays the service overview provided by the service developer. If the service developer has not provided any content at service creation, this section will be disabled. The service developer can provide the overview content via the Manage → Marketplace section of the component.

- **API definition**: Includes the API definition for the service, extracted from the `component.yaml` file in the user repository. If an API definition is not provided, this tab will be empty.

    !!! note
        If you are are currently using the `component-config.yaml` or `endpoints.yaml` configuration files, see the respective [migration guide](../develop-components/manage-component-source-configurations.md#migration-guide) for instructions on migrating to the recommended `component.yaml` configuration file.

- **How to use**: Includes instructions on how to use the selected service. This includes instructions on [creating a connection](../develop-components/sharing-and-reusing/create-a-connection.md).

- **Related documents**: Includes any additional content the user has provided as documents through the Manage -> Marketplace section of the component.

## Add a service to the Choreo Marketplace

You can add services to the Marketplace as Choreo services as follows: 

### Add a Choreo service

In Choreo, a service exposed through the platform is termed a Choreo service, with each service being identifiable by an endpoint within a Choreo service component. The Marketplace showcases a service for each endpoint within a service component.

Upon deployment to the initial environment, services get automatically added to the Marketplace. Choreo effortlessly collects essential details such as component name, endpoint name, description, and service definitions during this deployment, utilizing them to generate the corresponding service entries in the Marketplace.

The service name follows the convention of `component name - endpoint name`, while all other details remain unchanged.

## Service versioning in the Choreo Marketplace

In the Choreo Marketplace, service versions are displayed in their major version format. Each service in the Choreo Marketplace represents the latest version of the service within its major version, following semantic versioning principles.

For example, if a Choreo service has versions `v1.0`, `v1.1`, `v1.2`, and `v2.0`, the Choreo Marketplace displays services with versions `v1` and `v2` representing the latest versions `v1.2` and `v2.0` respectively.

When you deploy a new minor version of a service already deployed in Choreo, the corresponding service in the marketplace automatically updates to reflect the latest version within the same major version.

### Semantic-version-based intelligent routing in the Choreo Marketplace

When you use a service from the Choreo marketplace as a dependency, the dependent service's traffic automatically routes to the latest version of the corresponding service within the same major version. This ensures that your dependencies remain up-to-date without requiring manual updates within a major version.

For example, if you create a connection to connect your Choreo component named `Foo` to a Choreo service named `Bar`, which is currently available in the Choreo Marketplace as version v1, and if the latest version of the service `Bar` within the v1 range is v1.2, the component `Foo` will automatically connect to `Bar` v1.2.  Subsequently, when `Bar` releases version v1.3, traffic from `Foo` will automatically route to `Bar` v1.3.

## Edit services in the Choreo Marketplace

You can edit services in the Choreo Marketplace. During redeployment to any environment, Choreo automatically updates service definitions, visibility, and descriptions.


# CI/CD

Choreo provides a streamlined continuous integration and continuous deployment (CI/CD) experience to deploy applications and services efficiently across multiple environments.

Choreo creates environments for each project, where all components within the project share the environments. An environment is an isolated deployment area with restricted network and resource access. Services deployed in one environment cannot communicate with services deployed in another.

The Choreo cloud data plane provides two default environments (i.e., development and production). However, if you are in a private data plane organization, you can customize and create multiple environments based on your requirements.

Choreo adopts a *build once, deploy many* strategy to manage components across multiple environments. An application is built only once (i.e., per commit if automatic build on commit is enabled or based on the selected commit during a manual build). Then it is promoted to subsequent environments. This allows testing changes in lower, non-production environments like development before promoting the build to production.

Choreo injects configurations and secrets that you maintain at the environment level into components at runtime. This ensures a strict separation of environment-specific configurations from source code. Although configurations can vary across environments, the code and the built container remain unchanged. Configurations and secrets include:

- Resource credentials to a database, cache, or other backing services.
- Credentials to external cloud services such as Amazon S3 or external APIs.

All configurations and secrets are encrypted at rest and in transit and stored in a secure vault. In a private data plane organization, you can store configurations and secrets in your infrastructure.

## Build

Choreo auto-generates build pipelines that may slightly differ depending on the component type you create. Generally, all build pipelines work as follows:

- Builds a container image either from the provided source code or from a given Dockerfile for a specific commit.
- Runs security and vulnerability scans if applicable, depending on the component type.
- Pushes the container image to a container registry. In the cloud data plane, Choreo pushes the image to a Choreo-managed registry. If it is a private data plane organization, Choreo pushes the image to a registry that you own.
- Updates service endpoints and API specifications from the provided repository if applicable.

In addition to these steps, some buildpacks support integrating unit tests into the build pipeline. For more details, see [Integrate Unit Tests into the Build Pipeline](../develop-components/integrate-unit-tests-into-the-build-pipeline.md).

### Repeatable builds

Choreo can replicate builds from an identical code version (Git commit). This means that multiple builds initiated from the same Git commit will generate Docker images with the same behavior.

!!! note
    In the event of multiple builds from the same code version, Choreo preserves only the most recent version of the Docker image created from the particular code version.

### Trigger a build

On the **Build** page, click **Build Latest**. If necessary, you have the option to select a particular commit and build an image.

!!! note
    Admin and Choreo DevOps users can trigger builds using specific tags from the connected Git repository. However, this action bypasses the standard branch-based deployment process and should only be used for critical, time-sensitive scenarios, as it can disrupt deployment track integrity.

If you want to automatically trigger a build with each commit, you can enable **Auto Build on Commit**.

### Build logs

You can view build logs for specific builds on the **Build** page.

To view details of a specific build, click **View Details** corresponding to the build.

## Deployment

Once you build an image in Choreo, you can deploy it via the **Deploy** page. To deploy an image, you can follow one of the approaches given below:

- **Manually deploy**: In the **Deploy** page, go to the **Set Up** card and click **Deploy**.
- **Automatically deploy on build**: In the **Deploy** page, go to the **Set Up** card and enable **Auto Deploy on Build**. This automatically initiates deployment upon the completion of an automatic build.

!!! info
    To enable **Auto Deploy on Build**, you must enable **Auto Build on Commit**. This is because automatic deployment is not necessary or useful in scenarios where automatic build is not enabled.

!!! note
    - You must trigger the first build in a Ballerina component manually to ensure that Choreo applies the required configurations to the development environment. You can enable automatic builds subsequently.
    - Choreo automatically checks the configurable defined in your source code against the configurable values applied in an environment. Choreo requests the configurable values on deployment and promotion. If you have changed the configurables in your Ballerina component, auto-build pipelines can fail as a precaution to avoid a component crash at runtime due to missing configurables.
    - The configurable verifying capability is only available for Ballerina components. For Dockerfile-based components, ensure to manage and update the configurations and secrets in environments ahead of time. You must also ensure backward compatibility between at least one release if you change the configurations.

### Set up area and initial deployment

In the deploy phase, Choreo uses a setup area to merge the Docker image with its environment-independent configurations. Choreo then deploys this composite to the environment. This is known as the initial deployment.

### Immutable deployments

Once Choreo deploys a component with configurations, the configurations become immutable. Any subsequent change results in a new deployment.

### Promote a component to a higher environment

Choreo builds a container once per GitHub commit and then promotes it to subsequent higher environments.

You can go to the **Deploy** page of a component and promote it manually across environments.

## Configurations

Choreo allows you to define both environment-independent configurations and environment-specific configurations.

### Environment-independent configurations

These configurations apply to all environments.

To change environment-independent configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the **Set Up** card, and then trigger a new deployment to the initial environment. From there, you can proceed to promote the component to higher environments.

### Environment-specific configurations

These configurations apply to a particular environment.

To change environment-specific configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the specific environment card, and trigger a new deployment.

To learn more about managing these configurations, see [Configuration Management](https://wso2.com/choreo/docs/choreo-concepts/configuration-management/).

## Task execution

The information on the **Execute** page is only applicable to scheduled and manual task components.

To track and monitor executions associated with a deployed scheduled task or manual task, go to the left navigation menu and click **Execute**.

You can view current and historic execution details along with a quick snapshot of recent activity via the total count of executions within the last 30 days. For each execution, you can view vital details such as the unique execution ID, the time it was triggered, and relevant revision information. Furthermore, you can dive deeper into the details by clicking on a specific execution to access its associated logs. This information enhances transparency, troubleshooting capabilities, and overall execution management, allowing you to easily monitor and analyze workflows.

## Zero-downtime deployments

Choreo performs rolling updates to ensure zero downtime between deployments and promotions.

A new build undergoes a health check before traffic is switched to it from the current build.

If you configure the necessary health checks for a component, it can prevent deploying and promoting unhealthy versions of a component.


﻿# Component

A component within a project represents a single unit of work in a cloud native application. A component is usually a single microservice, API, or job/task. Each component in Choreo is attached to a given directory path in a Git repository which either contains program source code or a Dockerfile with build instructions. A component is Choreo’s unit of deployment. Each component maps to a single pod in the Kubernetes cluster (data plane) at deployment time. Therefore, you can deploy, manage, and scale each component in Choreo independently.

Choreo supports different component types for various use cases. These include component types such as services, API proxies, integrations, web applications, and so on. Each component type hosts unique features based on its characteristics. For example, a scheduled integration component can accept a cron expression as a configuration to schedule an integration job/task.



# Connections

Services can exist in two main forms: standalone and integrated. Connecting services is an integral part in creating integrated solutions. Choreo allows you to connect services using Connections. 

Using Connections, you can integrate the service you intend to deploy on Choreo with other services on Choreo or external resources. Upon creating a connection to a service on Choreo, Choreo provides you a Connection ID along with a set of connection parameters. Thereafter, you have the capability to configure your service to establish a connection using this Connection ID and map connection parameters to environment variable names in your Choreo component. You can read these environment variable names in your service implementation to retrieve the values, to create a programmatic connection to the service you want to consume. 

At runtime, Choreo dynamically injects values into the environment variables based on the configured mapping. This approach ensures that the connection parameter values and the service connection creation remain loosely coupled, providing developers with flexibility and ease of maintenance.

You can add Connections in different visibility levels: Project and Component. The visibility levels are described below:

## Project Connections

Project Connections are Connections you create to connect to services within a particular project. The Connections **can be used by any component within the project**. 

For example, if you want to share a third-party service like Twilio across the project for all the components within that project to reuse, you can create a project connection. Components can refer to Project Connections using the connection ID. 
Project connections created to consume Choreo services under the OAuth security scheme will share the same OAuth application across the project. Any component reusing such a connection will use the same client ID and client secret.

## Component Connections

Component Connections are Connections you define at the component level and **used by only that component**. 

For example, create a component connection if you want to connect a legacy service to a given component. Components can refer to the Component Connection using the connection ID. 
If your component consumes more than one Choreo service, the Component connections created to consume those Choreo services under the OAuth security scheme can share the same OAuth application by sharing the same client ID and secret between all such connections.

Learn how you can [share and reuse services using connections](../develop-components/sharing-and-reusing/create-a-connection.md) in Choreo.


# Data Planes

Choreo's architecture comprises two key components: the control plane and the data plane. The control plane handles essential tasks such as administering organizations, users, and projects. In addition, it also governs the entire journey of application development, from the initial stages of creation, progressing  to deployment, including measures to enforce governance and the provision for observability. The Choreo control plane is a SaaS that manages all cloud data planes and private data planes. It caters to diverse user personas, including CIOs, architects, and developers, as well as DevOps, site reliability engineers, and platform engineers.

The data plane is the environment where user applications are deployed based on configurations set in the control plane. These applications can range from services and web applications to APIs, integrations, and scheduled tasks. The applications can be written in various programming languages, allowing for a polyglot approach. Importantly, all traffic related to the runtime of user applications is restricted to the Choreo data plane, ensuring strict containment of user data within its boundaries.

Choreo's architecture features two distinct data plane types: cloud data planes and private data planes. A cloud data plane utilizes a multi-tenanted infrastructure model for deploying user applications, creating a shared yet secure environment for application runtime. In contrast, a private data plane(PDP) provides dedicated infrastructure for a single organization to run its user applications. This ensures an added layer of privacy and control for organizations with specific requirements.

![Choreo high-level view](../assets/img/choreo-concepts/high-level-view.png)

## Private data planes

### Infrastructure

Choreo private data planes can be deployed with almost all major cloud providers, such as Azure, AWS, and GCP, and are also compatible with on-premises infrastructure.

The essential requirements for a private data plane include upstream-compatible Kubernetes clusters, a container registry, a key vault (secret store), and a logging service or log storage.

![Private data plane architecture](../assets/img/choreo-concepts/private-data-plane-architecture.png)

### System components

Setting up the Choreo PDP system involves using a Helm installation on the Kubernetes infrastructure. 
The following software components are installed during the helm execution:

  - Cilium CNI and service mesh.
  - Choreo API Gateways and related components.
  - Choreo PDP agent.
  - Observability and logging APIs, along with observability agents.
  - Flux controller.

All of these software components receive automatic updates, including security patches and bug fixes through the flux controller connected to the Choreo Update Management System. 

### Connectivity with the control plane

The private data plane requires communication with the Choreo control plane to manage various activities. All these communications are outbound from the private data plane, ensuring that there is no need to open any specific `IP:Port` from its perspective for these interactions. However, if an organization's network restricts all outbound traffic, it is necessary to permit outbound traffic to the public IP range of the Choreo control plane.

The following table outlines the inbound and outbound connections from a private data plane:

<table border=1>
<thead>
<tr>
<th align="left">Data plane component</th>
<th align="left">Endpoint</th>
<th align="left">Direction</th>
<th align="left">Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2>Choreo PDP agent</td>
<td>Choreo control plane (CP) (mizzen server)</td>
<td>Outbound</td>
<td>WSS</td>
</tr>
<tr>
<td>Kubernetes API server</td>
<td>Outbound (cluster internal)</td>
<td>HTTPS, WS</td>
</tr>
<tr>
<td rowspan=2>APIM/local adaptor</td>
<td>Global adaptor</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Azure Service Bus (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td >APIM/Enforcer</td>
<td>Event hub (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td>Choreo secret resolver</td>
<td>Cloud secret store</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Container registry</td>
<td>Container registry (public)</td>
<td>Inbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Container registry</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Certificate manager</td>
<td>Azure DNS service</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>LetsEncrypt</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux source controller</td>
<td>GitHub</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux Helm controller</td>
<td>Choreo container registry</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
</tbody>
</table> 

All communication between the control plane and the private data plane is secured using TLS.

### Observability architecture

The following diagram depicts the architecture overview of Choreo's in-data-plane log and observability in Azure PDP:

![Observability architecture](../assets/img/choreo-concepts/observability-architecture.png)

The private data plane observability architecture is centered around a strong commitment to data privacy and compliance. This is achieved through a strategic decision to retain logs and observability data within the data planes itself. Key aspects of this architecture include:

- **Data storage at source**: Logs and observability data are stored within the data plane itself, enhancing security, simplifying access, and ensuring compliance.
- **Direct browser-to-data-plane interaction**: The Choreo Console in the user's browser directly interacts with APIs in the data plane, reducing potential data routing complexities and ensuring a more secure, direct flow of information.
- **Reduced data exposure points**: Fetching data directly from the data plane's APIs minimizes the number of data transfer points, effectively decreasing the chances of data exposure or interception.
- **Compliance with regulatory standards**: The architecture supports data locality, aligning with global regulatory standards like GDPR and CCPA by keeping data in its original environment.
- **Improved performance and real-time insights**: Direct interaction between the browser and data plane results in faster data retrieval, providing users with immediate insights.
- **User transparency and control**: Users have a clear view of their data's location and access methods, alongside granular control over data access.

### Security

The Choreo private data plane ensures extensive, production-grade security, ranging from infrastructure and architecture to zero-trust network security. All incoming traffic is protected by a firewall and must undergo authentication and authorization via the API Gateway. It also provides end-to-end network traffic encryption using Cilium transparent encryption, ensuring efficient data path encryption.

For details on the private data plane security levels supported in Choreo pricing plans, see [Private Data Plane Security Levels](../references/private-data-plane-security-levels.md).

### Management models

Choreo supports the following management models for private data planes (PDPs), fostering collaboration between WSO2 and customers across diverse scenarios:

  - WSO2 fully managed (infrastructure and PDP in WSO2 subscription) model
  - WSO2 fully managed (infrastructure and PDP in customer subscription) model
  - Customer self-managed (WSO2 provides installation script and updates) model

To explore each management model in detail so that you can make informed decisions depending on the supported cloud-based operations and security, see [Private Data Plane Management Models](../references/private-data-plane-management-models.md).


# Deployment Tracks

Deployment Tracks in Choreo are structured pathways for simplified software component deployment. They act like advanced CI/CD pipelines, ensuring your components reach their destinations seamlessly, whether from source code or prebuilt images. They establish an organized and structured approach that minimizes the chances of errors and challenges that are typically associated with deployment workflows.

## The significance of Deployment Tracks

Deployment Tracks offer practical solutions to enhance the API consumer experience by addressing two critical challenges:

- **Streamlined deployment**: Deployment Tracks serve as well-designed routes for your software components, enhancing the organization and reliability of the deployment process, similar to a well-structured express route.

- **Efficient API versioning**: Especially beneficial for managed APIs, Deployment Tracks provide a straightforward method for creating API versions that seamlessly interact with previous iterations. This simplified version management benefits both API creators and consumers alike.

## Streamlined deployments

For streamlined deployments, Choreo dissects two integral approaches that leverage Deployment Tracks: the comprehensive CI/CD integration and the focused CD-Only strategy.

### CI/CD with Deployment Tracks

A deployment track is linked to a particular branch within a GitHub repository. This connection is useful for handling deployments to various environments. On Choreo's Deploy page, you can easily visualize the deployments to specific environments associated with your selected deployment track. Moreover, the deployment track has a functionality that initiates automatic deployments for the linked branch. When activated, merging a pull request (PR) triggers a deployment to the development environment.

![Deployment tracks - source repo](../assets/img/choreo-concepts/deployment-tracks-source-repo.png){.cInlineImage-half}

### CD-Only strategy with Deployment Tracks

If you're inclined to use your own Continuous Integration (CI) systems and want to harness the deployment track as a Continuous Deployment (CD) pipeline, you can seamlessly link deployment tracks to a container registry repository. This configuration empowers users to effortlessly deploy images sourced directly from the linked container registry repository.

![Deployment tracks - container registry](../assets/img/choreo-concepts/deployment-tracks-container-registry.png){.cInlineImage-half}


## Efficient API versioning

**This section applies to only service components**. When working with service components in Choreo, it is important to have an effective API versioning mechanism. Choreo follows a versioning mechanism based on Semantic Versioning (SemVer) but only includes the major version and minor version with the prefix `v`. 

For example, `v1.2`. 

You can follow the approach given below when you version APIs in Choreo:

  - Increment the major version when you make incompatible API changes.
  - Increment the minor version when you add functionality in a backward-compatible manner.

!!! info "What is Semantic Versioning?"
    Semantic Versioning (SemVer) is a specification that defines how to assign and increment version numbers for software products, including APIs. For more information, see [Semantic Versioning specification](https://semver.org/#semantic-versioning-specification-semver).

One of the primary concerns when dealing with SaaS APIs is to minimize disruption for API consumers while continuously developing and deploying updates.

In compliance with SemVer, changes that don't introduce breaking or additive modifications to the API are categorized as patch updates. Hover, from the perspective of API consumers, these changes should ideally not disrupt their API clients. Typically, API consumers are most concerned with major API version alterations, but there might be instances where minor version changes are communicated to them.

Therefore, in the context of deployment tracks, API developers only need to specify the major and minor versions being delivered from a particular deployment track. This information is treated as the API version attribute of a deployment track. If the publisher requires versioning for internal tracking purposes, this can be accomplished in Git through the use of Git tags, on GitHub with GitHub releases, and so forth.

![Deployment tracks - api versioning](../assets/img/choreo-concepts/deployment-tracks-api-versioning.md.png){.cInlineImage-half}


﻿# Endpoint

An Endpoint is a network-exposed function that resides within a component. In Choreo, service and integration components expose one or more endpoints. Each endpoint in a component can have a service contract (OpenAPI, GraphQL SDL) associated with it. This contract is used to expose the endpoint to consumers. In the absence of a contract, Choreo uses /* exposed on all HTTP verbs as the default contract to expose the service or the integration.

Each endpoint exposed in a component is considered a single API. Therefore, Choreo allows you to do API management per endpoint for a given component. For example, you can perform lifecycle management and configure security settings per endpoint in a given component.


See [Configure Endpoints](../develop-components/configure-endpoints.md) to learn how to configure endpoints when developing components in Choreo. 

# Environments

Choreo offers developers one or more environments to run their applications within a given data plane. By default, the Choreo cloud data plane provides two environments (i.e., development and production). Each project in Choreo is associated with one or more  environments available in the organization. For example, project A may choose to utilize dev, staging, and production environments, while project B may only use development and production environments.

You can promote components within a project across available environments. When you promote a component, its configuration values can be overridden with environment-specific values.

The following diagram illustrates how a component is promoted across environments.

![Choreo environments](../assets/img/choreo-concepts/choreo-environments.png){.cInlineImage-threeQuarter}


﻿# Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization.

## Switch organizations

If you are a member of more than one organization, you can switch from one organization to another when necessary. To do this, select the required organization from the **Organization** list in the Choreo Console header.

{% include "../administer/inviting-members.md" %}

## Manage user permission

Choreo manages user permissions with groups and roles.

### Groups

A group in Choreo is a collection of users, each with one or more roles assigned to them. Users within a group inherit the permissions associated with the roles assigned to that group. For instance, if a user is added to the `API Publisher` group, they will automatically receive the `API Publisher` role.

Choreo comes with predefined groups already configured with specific roles, as follows:

- **API Publisher**: A collection of users who have the API Publisher role.
- **API Subscriber**: A collection of users who have the API Subscriber role.
- **Admin** : A collection of users who have the Admin role.
- **Billing Admin** : A collection of users who have the Billing Admin role.
- **Choreo DevOps** : A collection of users who have the Choreo DevOps role.
- **Developer** : Users who develop, deploy, and manage cloud native applications at scale.
- **External API Subscriber**: A collection of users who have the External API Subscriber role.

When creating a new group to invite members, be sure to assign a role to the group to ensure users have the required permissions.

### Roles

Choreo roles are defined as follows:

- **API Publisher**: An API publisher can discover, create, publish, delete, test, and manage an API.
- **API Subscriber**: An API subscriber is a developer in a particular organization. An API subscriber can subscribe to an application, manage subscriptions, manage applications, generate API keys, and manage API keys.
- **Admin**: An administrator is responsible for all administration tasks, including user management, customizing the Developer Portal, managing projects, enabling analytics, managing domains, etc.
- **Billing Admin**: Is responsible for billing administration that includes viewing tiers, creating and viewing organizations, managing invoices, viewing and creating subscriptions, and viewing and creating payment methods.
- **Choreo DevOps**: A Choreo DevOps user is a user with access to the Choreo DevOps portal, enabling them to actively manage, ensure dependable deployment, and monitor components.
- **Developer** : A user who can develop, deploy, and manage cloud native applications at scale.  
- **External API subscriber**: External API subscribers are API consumers who have access only to the API Developer Portal. They can join an organization with the sole purpose of consuming APIs.
- **Environment Manager (Deprecated)**: Manages deployment environments.

## Organization ID

The Organization ID serves as a unique identifier for each organization. To get the organization ID, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. In the header, click the **Organization** list. This will open the organization level settings page. 
5. Under **Organization** click **Copy ID**.

## Organization Handle

The organization handle is a unique string that directly corresponds to your organization's name. To get the organization handle, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. Under **Organization** click **Copy Handle**.


﻿# Project

A project in Choreo is a logical group of related components that typically represent a single cloud native application. A project consists of one or more components. All components within a project can ideally be (but is not restricted to) in a single GitHub repository under different paths. This is also known as the monorepo architecture.

At deployment time, all components within a given project are deployed into a single namespace of the Kubernetes cluster. Components within a project can be exposed to the public internet, internally to the rest of the organization, or privately within the project only. A project in Choreo is represented as a cell with regard to the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md). The following diagram illustrates a project and how the components within a project are laid out at runtime:

![Project](../assets/img/choreo-concepts/project.png){.cInlineImage-full}








# Resource Hierarchy


The following diagram depicts the high-level resources and their relationships in Choreo.

![Resource hierarchy](../assets/img/choreo-concepts/resource-hierarchy.png){.cInlineImage-full}

## Organizations and data planes

Data planes are connected to the organization and are available for all projects within the organization. When you create an environment in a project, the data plane connected to the organization is linked with an automatically generated Kubernetes namespace.

## Environments and data planes

Choreo allows multiple Kubernetes clusters to be associated with an environment. This enables you to build highly resilient and resource-efficient solutions that utilize multiple clusters. Choreo synchronizes your applications and workloads between associated clusters in an environment, allowing you to perform multi-cluster deployment with a single click.

The following diagram illustrates how multiple clusters associate with different environments:

![Environments and dataplanes](../assets/img/choreo-concepts/environments-and-dataplanes.png){.cInlineImage-full}

!!! info "Note"
    It is not necessary to use a different cluster per environment. You can create multiple environments on the same cluster. The above diagram is an example of a specific solution. Your application architecture may require a different configuration than what is depicted.

## Components and environments

Components belong to a project in Choreo, and environments are provisioned per project. When a component is deployed, it is deployed as a container to the specified environment. Once deployed, you can promote the container image across the environments available in the project.



# Choreo Marketplace

The Choreo Marketplace promotes and facilitates reusing and sharing services. It allows you to share all the services deployed in Choreo.
You can easily browse and search available services within the Marketplace and refer to the service definitions, documentation, instructions on how you can use it, etc. 

![Internal Marketplace](../assets/img/choreo-concepts/marketplace/internal-marketplace.png){.cInlineImage-full}

## Discover services

The Marketplace includes all services deployed in your organization. This may be a large number of services. Therefore, effective discoverability is desirable.

You can use the search or apply various filter criteria to explore the services available.

### Search

The top search bar provides universal searching to find the services. It allows you to search for a text in the following search attributes:

- **Name**: The service name.
- **Label**: The service labels.
- **Content**: The service content: overview, summary, and documentation.
- **All**: All of the above criteria.

### Filter

The Choreo Marketplace provides a filtering capability through the left-hand side filter panel. It allows you to filter with the following filter attributes:

- **Type**: This filter enables you to categorize services based on their type, with two available options: "Internal" and "Third-party". "Internal" refers to services deployed within Choreo, while "Third-party" refers to services running externally to Choreo, independently added to the Marketplace.

- **Network Visibility**: This filter enables you to categorize services based on their network visibility level, with three choices: "Public," "Organization," and "Project".  "Public" filters services exposed publicly, "Organization" represents services exposed across the entire organization, and "Project" represents services exposed at the project level.


## Explore a service 

You can click on the service card to open the detailed view of the service. The detailed service page features the service name, summary, version, labels, and service icon as the header.

Choreo organizes the service content into four tabs. The four tabs contain information as follows: 

- **Overview**: Choreo displays the service overview provided by the service developer. If the service developer has not provided any content at service creation, this section will be disabled. The service developer can provide the overview content via the Manage → Marketplace section of the component.

- **API definition**: Includes the API definition for the service, extracted from the `component.yaml` file in the user repository. If an API definition is not provided, this tab will be empty.

    !!! note
        If you are are currently using the `component-config.yaml` or `endpoints.yaml` configuration files, see the respective [migration guide](../develop-components/manage-component-source-configurations.md#migration-guide) for instructions on migrating to the recommended `component.yaml` configuration file.

- **How to use**: Includes instructions on how to use the selected service. This includes instructions on [creating a connection](../develop-components/sharing-and-reusing/create-a-connection.md).

- **Related documents**: Includes any additional content the user has provided as documents through the Manage -> Marketplace section of the component.

## Add a service to the Choreo Marketplace

You can add services to the Marketplace as Choreo services as follows: 

### Add a Choreo service

In Choreo, a service exposed through the platform is termed a Choreo service, with each service being identifiable by an endpoint within a Choreo service component. The Marketplace showcases a service for each endpoint within a service component.

Upon deployment to the initial environment, services get automatically added to the Marketplace. Choreo effortlessly collects essential details such as component name, endpoint name, description, and service definitions during this deployment, utilizing them to generate the corresponding service entries in the Marketplace.

The service name follows the convention of `component name - endpoint name`, while all other details remain unchanged.

## Service versioning in the Choreo Marketplace

In the Choreo Marketplace, service versions are displayed in their major version format. Each service in the Choreo Marketplace represents the latest version of the service within its major version, following semantic versioning principles.

For example, if a Choreo service has versions `v1.0`, `v1.1`, `v1.2`, and `v2.0`, the Choreo Marketplace displays services with versions `v1` and `v2` representing the latest versions `v1.2` and `v2.0` respectively.

When you deploy a new minor version of a service already deployed in Choreo, the corresponding service in the marketplace automatically updates to reflect the latest version within the same major version.

### Semantic-version-based intelligent routing in the Choreo Marketplace

When you use a service from the Choreo marketplace as a dependency, the dependent service's traffic automatically routes to the latest version of the corresponding service within the same major version. This ensures that your dependencies remain up-to-date without requiring manual updates within a major version.

For example, if you create a connection to connect your Choreo component named `Foo` to a Choreo service named `Bar`, which is currently available in the Choreo Marketplace as version v1, and if the latest version of the service `Bar` within the v1 range is v1.2, the component `Foo` will automatically connect to `Bar` v1.2.  Subsequently, when `Bar` releases version v1.3, traffic from `Foo` will automatically route to `Bar` v1.3.

## Edit services in the Choreo Marketplace

You can edit services in the Choreo Marketplace. During redeployment to any environment, Choreo automatically updates service definitions, visibility, and descriptions.


# CI/CD

Choreo provides a streamlined continuous integration and continuous deployment (CI/CD) experience to deploy applications and services efficiently across multiple environments.

Choreo creates environments for each project, where all components within the project share the environments. An environment is an isolated deployment area with restricted network and resource access. Services deployed in one environment cannot communicate with services deployed in another.

The Choreo cloud data plane provides two default environments (i.e., development and production). However, if you are in a private data plane organization, you can customize and create multiple environments based on your requirements.

Choreo adopts a *build once, deploy many* strategy to manage components across multiple environments. An application is built only once (i.e., per commit if automatic build on commit is enabled or based on the selected commit during a manual build). Then it is promoted to subsequent environments. This allows testing changes in lower, non-production environments like development before promoting the build to production.

Choreo injects configurations and secrets that you maintain at the environment level into components at runtime. This ensures a strict separation of environment-specific configurations from source code. Although configurations can vary across environments, the code and the built container remain unchanged. Configurations and secrets include:

- Resource credentials to a database, cache, or other backing services.
- Credentials to external cloud services such as Amazon S3 or external APIs.

All configurations and secrets are encrypted at rest and in transit and stored in a secure vault. In a private data plane organization, you can store configurations and secrets in your infrastructure.

## Build

Choreo auto-generates build pipelines that may slightly differ depending on the component type you create. Generally, all build pipelines work as follows:

- Builds a container image either from the provided source code or from a given Dockerfile for a specific commit.
- Runs security and vulnerability scans if applicable, depending on the component type.
- Pushes the container image to a container registry. In the cloud data plane, Choreo pushes the image to a Choreo-managed registry. If it is a private data plane organization, Choreo pushes the image to a registry that you own.
- Updates service endpoints and API specifications from the provided repository if applicable.

In addition to these steps, some buildpacks support integrating unit tests into the build pipeline. For more details, see [Integrate Unit Tests into the Build Pipeline](../develop-components/integrate-unit-tests-into-the-build-pipeline.md).

### Repeatable builds

Choreo can replicate builds from an identical code version (Git commit). This means that multiple builds initiated from the same Git commit will generate Docker images with the same behavior.

!!! note
    In the event of multiple builds from the same code version, Choreo preserves only the most recent version of the Docker image created from the particular code version.

### Trigger a build

On the **Build** page, click **Build Latest**. If necessary, you have the option to select a particular commit and build an image.

!!! note
    Admin and Choreo DevOps users can trigger builds using specific tags from the connected Git repository. However, this action bypasses the standard branch-based deployment process and should only be used for critical, time-sensitive scenarios, as it can disrupt deployment track integrity.

If you want to automatically trigger a build with each commit, you can enable **Auto Build on Commit**.

### Build logs

You can view build logs for specific builds on the **Build** page.

To view details of a specific build, click **View Details** corresponding to the build.

## Deployment

Once you build an image in Choreo, you can deploy it via the **Deploy** page. To deploy an image, you can follow one of the approaches given below:

- **Manually deploy**: In the **Deploy** page, go to the **Set Up** card and click **Deploy**.
- **Automatically deploy on build**: In the **Deploy** page, go to the **Set Up** card and enable **Auto Deploy on Build**. This automatically initiates deployment upon the completion of an automatic build.

!!! info
    To enable **Auto Deploy on Build**, you must enable **Auto Build on Commit**. This is because automatic deployment is not necessary or useful in scenarios where automatic build is not enabled.

!!! note
    - You must trigger the first build in a Ballerina component manually to ensure that Choreo applies the required configurations to the development environment. You can enable automatic builds subsequently.
    - Choreo automatically checks the configurable defined in your source code against the configurable values applied in an environment. Choreo requests the configurable values on deployment and promotion. If you have changed the configurables in your Ballerina component, auto-build pipelines can fail as a precaution to avoid a component crash at runtime due to missing configurables.
    - The configurable verifying capability is only available for Ballerina components. For Dockerfile-based components, ensure to manage and update the configurations and secrets in environments ahead of time. You must also ensure backward compatibility between at least one release if you change the configurations.

### Set up area and initial deployment

In the deploy phase, Choreo uses a setup area to merge the Docker image with its environment-independent configurations. Choreo then deploys this composite to the environment. This is known as the initial deployment.

### Immutable deployments

Once Choreo deploys a component with configurations, the configurations become immutable. Any subsequent change results in a new deployment.

### Promote a component to a higher environment

Choreo builds a container once per GitHub commit and then promotes it to subsequent higher environments.

You can go to the **Deploy** page of a component and promote it manually across environments.

## Configurations

Choreo allows you to define both environment-independent configurations and environment-specific configurations.

### Environment-independent configurations

These configurations apply to all environments.

To change environment-independent configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the **Set Up** card, and then trigger a new deployment to the initial environment. From there, you can proceed to promote the component to higher environments.

### Environment-specific configurations

These configurations apply to a particular environment.

To change environment-specific configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the specific environment card, and trigger a new deployment.

To learn more about managing these configurations, see [Configuration Management](https://wso2.com/choreo/docs/choreo-concepts/configuration-management/).

## Task execution

The information on the **Execute** page is only applicable to scheduled and manual task components.

To track and monitor executions associated with a deployed scheduled task or manual task, go to the left navigation menu and click **Execute**.

You can view current and historic execution details along with a quick snapshot of recent activity via the total count of executions within the last 30 days. For each execution, you can view vital details such as the unique execution ID, the time it was triggered, and relevant revision information. Furthermore, you can dive deeper into the details by clicking on a specific execution to access its associated logs. This information enhances transparency, troubleshooting capabilities, and overall execution management, allowing you to easily monitor and analyze workflows.

## Zero-downtime deployments

Choreo performs rolling updates to ensure zero downtime between deployments and promotions.

A new build undergoes a health check before traffic is switched to it from the current build.

If you configure the necessary health checks for a component, it can prevent deploying and promoting unhealthy versions of a component.


﻿# Component

A component within a project represents a single unit of work in a cloud native application. A component is usually a single microservice, API, or job/task. Each component in Choreo is attached to a given directory path in a Git repository which either contains program source code or a Dockerfile with build instructions. A component is Choreo’s unit of deployment. Each component maps to a single pod in the Kubernetes cluster (data plane) at deployment time. Therefore, you can deploy, manage, and scale each component in Choreo independently.

Choreo supports different component types for various use cases. These include component types such as services, API proxies, integrations, web applications, and so on. Each component type hosts unique features based on its characteristics. For example, a scheduled integration component can accept a cron expression as a configuration to schedule an integration job/task.



# Connections

Services can exist in two main forms: standalone and integrated. Connecting services is an integral part in creating integrated solutions. Choreo allows you to connect services using Connections. 

Using Connections, you can integrate the service you intend to deploy on Choreo with other services on Choreo or external resources. Upon creating a connection to a service on Choreo, Choreo provides you a Connection ID along with a set of connection parameters. Thereafter, you have the capability to configure your service to establish a connection using this Connection ID and map connection parameters to environment variable names in your Choreo component. You can read these environment variable names in your service implementation to retrieve the values, to create a programmatic connection to the service you want to consume. 

At runtime, Choreo dynamically injects values into the environment variables based on the configured mapping. This approach ensures that the connection parameter values and the service connection creation remain loosely coupled, providing developers with flexibility and ease of maintenance.

You can add Connections in different visibility levels: Project and Component. The visibility levels are described below:

## Project Connections

Project Connections are Connections you create to connect to services within a particular project. The Connections **can be used by any component within the project**. 

For example, if you want to share a third-party service like Twilio across the project for all the components within that project to reuse, you can create a project connection. Components can refer to Project Connections using the connection ID. 
Project connections created to consume Choreo services under the OAuth security scheme will share the same OAuth application across the project. Any component reusing such a connection will use the same client ID and client secret.

## Component Connections

Component Connections are Connections you define at the component level and **used by only that component**. 

For example, create a component connection if you want to connect a legacy service to a given component. Components can refer to the Component Connection using the connection ID. 
If your component consumes more than one Choreo service, the Component connections created to consume those Choreo services under the OAuth security scheme can share the same OAuth application by sharing the same client ID and secret between all such connections.

Learn how you can [share and reuse services using connections](../develop-components/sharing-and-reusing/create-a-connection.md) in Choreo.


# Data Planes

Choreo's architecture comprises two key components: the control plane and the data plane. The control plane handles essential tasks such as administering organizations, users, and projects. In addition, it also governs the entire journey of application development, from the initial stages of creation, progressing  to deployment, including measures to enforce governance and the provision for observability. The Choreo control plane is a SaaS that manages all cloud data planes and private data planes. It caters to diverse user personas, including CIOs, architects, and developers, as well as DevOps, site reliability engineers, and platform engineers.

The data plane is the environment where user applications are deployed based on configurations set in the control plane. These applications can range from services and web applications to APIs, integrations, and scheduled tasks. The applications can be written in various programming languages, allowing for a polyglot approach. Importantly, all traffic related to the runtime of user applications is restricted to the Choreo data plane, ensuring strict containment of user data within its boundaries.

Choreo's architecture features two distinct data plane types: cloud data planes and private data planes. A cloud data plane utilizes a multi-tenanted infrastructure model for deploying user applications, creating a shared yet secure environment for application runtime. In contrast, a private data plane(PDP) provides dedicated infrastructure for a single organization to run its user applications. This ensures an added layer of privacy and control for organizations with specific requirements.

![Choreo high-level view](../assets/img/choreo-concepts/high-level-view.png)

## Private data planes

### Infrastructure

Choreo private data planes can be deployed with almost all major cloud providers, such as Azure, AWS, and GCP, and are also compatible with on-premises infrastructure.

The essential requirements for a private data plane include upstream-compatible Kubernetes clusters, a container registry, a key vault (secret store), and a logging service or log storage.

![Private data plane architecture](../assets/img/choreo-concepts/private-data-plane-architecture.png)

### System components

Setting up the Choreo PDP system involves using a Helm installation on the Kubernetes infrastructure. 
The following software components are installed during the helm execution:

  - Cilium CNI and service mesh.
  - Choreo API Gateways and related components.
  - Choreo PDP agent.
  - Observability and logging APIs, along with observability agents.
  - Flux controller.

All of these software components receive automatic updates, including security patches and bug fixes through the flux controller connected to the Choreo Update Management System. 

### Connectivity with the control plane

The private data plane requires communication with the Choreo control plane to manage various activities. All these communications are outbound from the private data plane, ensuring that there is no need to open any specific `IP:Port` from its perspective for these interactions. However, if an organization's network restricts all outbound traffic, it is necessary to permit outbound traffic to the public IP range of the Choreo control plane.

The following table outlines the inbound and outbound connections from a private data plane:

<table border=1>
<thead>
<tr>
<th align="left">Data plane component</th>
<th align="left">Endpoint</th>
<th align="left">Direction</th>
<th align="left">Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2>Choreo PDP agent</td>
<td>Choreo control plane (CP) (mizzen server)</td>
<td>Outbound</td>
<td>WSS</td>
</tr>
<tr>
<td>Kubernetes API server</td>
<td>Outbound (cluster internal)</td>
<td>HTTPS, WS</td>
</tr>
<tr>
<td rowspan=2>APIM/local adaptor</td>
<td>Global adaptor</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Azure Service Bus (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td >APIM/Enforcer</td>
<td>Event hub (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td>Choreo secret resolver</td>
<td>Cloud secret store</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Container registry</td>
<td>Container registry (public)</td>
<td>Inbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Container registry</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Certificate manager</td>
<td>Azure DNS service</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>LetsEncrypt</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux source controller</td>
<td>GitHub</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux Helm controller</td>
<td>Choreo container registry</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
</tbody>
</table> 

All communication between the control plane and the private data plane is secured using TLS.

### Observability architecture

The following diagram depicts the architecture overview of Choreo's in-data-plane log and observability in Azure PDP:

![Observability architecture](../assets/img/choreo-concepts/observability-architecture.png)

The private data plane observability architecture is centered around a strong commitment to data privacy and compliance. This is achieved through a strategic decision to retain logs and observability data within the data planes itself. Key aspects of this architecture include:

- **Data storage at source**: Logs and observability data are stored within the data plane itself, enhancing security, simplifying access, and ensuring compliance.
- **Direct browser-to-data-plane interaction**: The Choreo Console in the user's browser directly interacts with APIs in the data plane, reducing potential data routing complexities and ensuring a more secure, direct flow of information.
- **Reduced data exposure points**: Fetching data directly from the data plane's APIs minimizes the number of data transfer points, effectively decreasing the chances of data exposure or interception.
- **Compliance with regulatory standards**: The architecture supports data locality, aligning with global regulatory standards like GDPR and CCPA by keeping data in its original environment.
- **Improved performance and real-time insights**: Direct interaction between the browser and data plane results in faster data retrieval, providing users with immediate insights.
- **User transparency and control**: Users have a clear view of their data's location and access methods, alongside granular control over data access.

### Security

The Choreo private data plane ensures extensive, production-grade security, ranging from infrastructure and architecture to zero-trust network security. All incoming traffic is protected by a firewall and must undergo authentication and authorization via the API Gateway. It also provides end-to-end network traffic encryption using Cilium transparent encryption, ensuring efficient data path encryption.

For details on the private data plane security levels supported in Choreo pricing plans, see [Private Data Plane Security Levels](../references/private-data-plane-security-levels.md).

### Management models

Choreo supports the following management models for private data planes (PDPs), fostering collaboration between WSO2 and customers across diverse scenarios:

  - WSO2 fully managed (infrastructure and PDP in WSO2 subscription) model
  - WSO2 fully managed (infrastructure and PDP in customer subscription) model
  - Customer self-managed (WSO2 provides installation script and updates) model

To explore each management model in detail so that you can make informed decisions depending on the supported cloud-based operations and security, see [Private Data Plane Management Models](../references/private-data-plane-management-models.md).


# Deployment Tracks

Deployment Tracks in Choreo are structured pathways for simplified software component deployment. They act like advanced CI/CD pipelines, ensuring your components reach their destinations seamlessly, whether from source code or prebuilt images. They establish an organized and structured approach that minimizes the chances of errors and challenges that are typically associated with deployment workflows.

## The significance of Deployment Tracks

Deployment Tracks offer practical solutions to enhance the API consumer experience by addressing two critical challenges:

- **Streamlined deployment**: Deployment Tracks serve as well-designed routes for your software components, enhancing the organization and reliability of the deployment process, similar to a well-structured express route.

- **Efficient API versioning**: Especially beneficial for managed APIs, Deployment Tracks provide a straightforward method for creating API versions that seamlessly interact with previous iterations. This simplified version management benefits both API creators and consumers alike.

## Streamlined deployments

For streamlined deployments, Choreo dissects two integral approaches that leverage Deployment Tracks: the comprehensive CI/CD integration and the focused CD-Only strategy.

### CI/CD with Deployment Tracks

A deployment track is linked to a particular branch within a GitHub repository. This connection is useful for handling deployments to various environments. On Choreo's Deploy page, you can easily visualize the deployments to specific environments associated with your selected deployment track. Moreover, the deployment track has a functionality that initiates automatic deployments for the linked branch. When activated, merging a pull request (PR) triggers a deployment to the development environment.

![Deployment tracks - source repo](../assets/img/choreo-concepts/deployment-tracks-source-repo.png){.cInlineImage-half}

### CD-Only strategy with Deployment Tracks

If you're inclined to use your own Continuous Integration (CI) systems and want to harness the deployment track as a Continuous Deployment (CD) pipeline, you can seamlessly link deployment tracks to a container registry repository. This configuration empowers users to effortlessly deploy images sourced directly from the linked container registry repository.

![Deployment tracks - container registry](../assets/img/choreo-concepts/deployment-tracks-container-registry.png){.cInlineImage-half}


## Efficient API versioning

**This section applies to only service components**. When working with service components in Choreo, it is important to have an effective API versioning mechanism. Choreo follows a versioning mechanism based on Semantic Versioning (SemVer) but only includes the major version and minor version with the prefix `v`. 

For example, `v1.2`. 

You can follow the approach given below when you version APIs in Choreo:

  - Increment the major version when you make incompatible API changes.
  - Increment the minor version when you add functionality in a backward-compatible manner.

!!! info "What is Semantic Versioning?"
    Semantic Versioning (SemVer) is a specification that defines how to assign and increment version numbers for software products, including APIs. For more information, see [Semantic Versioning specification](https://semver.org/#semantic-versioning-specification-semver).

One of the primary concerns when dealing with SaaS APIs is to minimize disruption for API consumers while continuously developing and deploying updates.

In compliance with SemVer, changes that don't introduce breaking or additive modifications to the API are categorized as patch updates. Hover, from the perspective of API consumers, these changes should ideally not disrupt their API clients. Typically, API consumers are most concerned with major API version alterations, but there might be instances where minor version changes are communicated to them.

Therefore, in the context of deployment tracks, API developers only need to specify the major and minor versions being delivered from a particular deployment track. This information is treated as the API version attribute of a deployment track. If the publisher requires versioning for internal tracking purposes, this can be accomplished in Git through the use of Git tags, on GitHub with GitHub releases, and so forth.

![Deployment tracks - api versioning](../assets/img/choreo-concepts/deployment-tracks-api-versioning.md.png){.cInlineImage-half}


﻿# Endpoint

An Endpoint is a network-exposed function that resides within a component. In Choreo, service and integration components expose one or more endpoints. Each endpoint in a component can have a service contract (OpenAPI, GraphQL SDL) associated with it. This contract is used to expose the endpoint to consumers. In the absence of a contract, Choreo uses /* exposed on all HTTP verbs as the default contract to expose the service or the integration.

Each endpoint exposed in a component is considered a single API. Therefore, Choreo allows you to do API management per endpoint for a given component. For example, you can perform lifecycle management and configure security settings per endpoint in a given component.


See [Configure Endpoints](../develop-components/configure-endpoints.md) to learn how to configure endpoints when developing components in Choreo. 

# Environments

Choreo offers developers one or more environments to run their applications within a given data plane. By default, the Choreo cloud data plane provides two environments (i.e., development and production). Each project in Choreo is associated with one or more  environments available in the organization. For example, project A may choose to utilize dev, staging, and production environments, while project B may only use development and production environments.

You can promote components within a project across available environments. When you promote a component, its configuration values can be overridden with environment-specific values.

The following diagram illustrates how a component is promoted across environments.

![Choreo environments](../assets/img/choreo-concepts/choreo-environments.png){.cInlineImage-threeQuarter}


﻿# Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization.

## Switch organizations

If you are a member of more than one organization, you can switch from one organization to another when necessary. To do this, select the required organization from the **Organization** list in the Choreo Console header.

{% include "../administer/inviting-members.md" %}

## Manage user permission

Choreo manages user permissions with groups and roles.

### Groups

A group in Choreo is a collection of users, each with one or more roles assigned to them. Users within a group inherit the permissions associated with the roles assigned to that group. For instance, if a user is added to the `API Publisher` group, they will automatically receive the `API Publisher` role.

Choreo comes with predefined groups already configured with specific roles, as follows:

- **API Publisher**: A collection of users who have the API Publisher role.
- **API Subscriber**: A collection of users who have the API Subscriber role.
- **Admin** : A collection of users who have the Admin role.
- **Billing Admin** : A collection of users who have the Billing Admin role.
- **Choreo DevOps** : A collection of users who have the Choreo DevOps role.
- **Developer** : Users who develop, deploy, and manage cloud native applications at scale.
- **External API Subscriber**: A collection of users who have the External API Subscriber role.

When creating a new group to invite members, be sure to assign a role to the group to ensure users have the required permissions.

### Roles

Choreo roles are defined as follows:

- **API Publisher**: An API publisher can discover, create, publish, delete, test, and manage an API.
- **API Subscriber**: An API subscriber is a developer in a particular organization. An API subscriber can subscribe to an application, manage subscriptions, manage applications, generate API keys, and manage API keys.
- **Admin**: An administrator is responsible for all administration tasks, including user management, customizing the Developer Portal, managing projects, enabling analytics, managing domains, etc.
- **Billing Admin**: Is responsible for billing administration that includes viewing tiers, creating and viewing organizations, managing invoices, viewing and creating subscriptions, and viewing and creating payment methods.
- **Choreo DevOps**: A Choreo DevOps user is a user with access to the Choreo DevOps portal, enabling them to actively manage, ensure dependable deployment, and monitor components.
- **Developer** : A user who can develop, deploy, and manage cloud native applications at scale.  
- **External API subscriber**: External API subscribers are API consumers who have access only to the API Developer Portal. They can join an organization with the sole purpose of consuming APIs.
- **Environment Manager (Deprecated)**: Manages deployment environments.

## Organization ID

The Organization ID serves as a unique identifier for each organization. To get the organization ID, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. In the header, click the **Organization** list. This will open the organization level settings page. 
5. Under **Organization** click **Copy ID**.

## Organization Handle

The organization handle is a unique string that directly corresponds to your organization's name. To get the organization handle, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. Under **Organization** click **Copy Handle**.


﻿# Project

A project in Choreo is a logical group of related components that typically represent a single cloud native application. A project consists of one or more components. All components within a project can ideally be (but is not restricted to) in a single GitHub repository under different paths. This is also known as the monorepo architecture.

At deployment time, all components within a given project are deployed into a single namespace of the Kubernetes cluster. Components within a project can be exposed to the public internet, internally to the rest of the organization, or privately within the project only. A project in Choreo is represented as a cell with regard to the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md). The following diagram illustrates a project and how the components within a project are laid out at runtime:

![Project](../assets/img/choreo-concepts/project.png){.cInlineImage-full}








# Resource Hierarchy


The following diagram depicts the high-level resources and their relationships in Choreo.

![Resource hierarchy](../assets/img/choreo-concepts/resource-hierarchy.png){.cInlineImage-full}

## Organizations and data planes

Data planes are connected to the organization and are available for all projects within the organization. When you create an environment in a project, the data plane connected to the organization is linked with an automatically generated Kubernetes namespace.

## Environments and data planes

Choreo allows multiple Kubernetes clusters to be associated with an environment. This enables you to build highly resilient and resource-efficient solutions that utilize multiple clusters. Choreo synchronizes your applications and workloads between associated clusters in an environment, allowing you to perform multi-cluster deployment with a single click.

The following diagram illustrates how multiple clusters associate with different environments:

![Environments and dataplanes](../assets/img/choreo-concepts/environments-and-dataplanes.png){.cInlineImage-full}

!!! info "Note"
    It is not necessary to use a different cluster per environment. You can create multiple environments on the same cluster. The above diagram is an example of a specific solution. Your application architecture may require a different configuration than what is depicted.

## Components and environments

Components belong to a project in Choreo, and environments are provisioned per project. When a component is deployed, it is deployed as a container to the specified environment. Once deployed, you can promote the container image across the environments available in the project.



# Choreo Marketplace

The Choreo Marketplace promotes and facilitates reusing and sharing services. It allows you to share all the services deployed in Choreo.
You can easily browse and search available services within the Marketplace and refer to the service definitions, documentation, instructions on how you can use it, etc. 

![Internal Marketplace](../assets/img/choreo-concepts/marketplace/internal-marketplace.png){.cInlineImage-full}

## Discover services

The Marketplace includes all services deployed in your organization. This may be a large number of services. Therefore, effective discoverability is desirable.

You can use the search or apply various filter criteria to explore the services available.

### Search

The top search bar provides universal searching to find the services. It allows you to search for a text in the following search attributes:

- **Name**: The service name.
- **Label**: The service labels.
- **Content**: The service content: overview, summary, and documentation.
- **All**: All of the above criteria.

### Filter

The Choreo Marketplace provides a filtering capability through the left-hand side filter panel. It allows you to filter with the following filter attributes:

- **Type**: This filter enables you to categorize services based on their type, with two available options: "Internal" and "Third-party". "Internal" refers to services deployed within Choreo, while "Third-party" refers to services running externally to Choreo, independently added to the Marketplace.

- **Network Visibility**: This filter enables you to categorize services based on their network visibility level, with three choices: "Public," "Organization," and "Project".  "Public" filters services exposed publicly, "Organization" represents services exposed across the entire organization, and "Project" represents services exposed at the project level.


## Explore a service 

You can click on the service card to open the detailed view of the service. The detailed service page features the service name, summary, version, labels, and service icon as the header.

Choreo organizes the service content into four tabs. The four tabs contain information as follows: 

- **Overview**: Choreo displays the service overview provided by the service developer. If the service developer has not provided any content at service creation, this section will be disabled. The service developer can provide the overview content via the Manage → Marketplace section of the component.

- **API definition**: Includes the API definition for the service, extracted from the `component.yaml` file in the user repository. If an API definition is not provided, this tab will be empty.

    !!! note
        If you are are currently using the `component-config.yaml` or `endpoints.yaml` configuration files, see the respective [migration guide](../develop-components/manage-component-source-configurations.md#migration-guide) for instructions on migrating to the recommended `component.yaml` configuration file.

- **How to use**: Includes instructions on how to use the selected service. This includes instructions on [creating a connection](../develop-components/sharing-and-reusing/create-a-connection.md).

- **Related documents**: Includes any additional content the user has provided as documents through the Manage -> Marketplace section of the component.

## Add a service to the Choreo Marketplace

You can add services to the Marketplace as Choreo services as follows: 

### Add a Choreo service

In Choreo, a service exposed through the platform is termed a Choreo service, with each service being identifiable by an endpoint within a Choreo service component. The Marketplace showcases a service for each endpoint within a service component.

Upon deployment to the initial environment, services get automatically added to the Marketplace. Choreo effortlessly collects essential details such as component name, endpoint name, description, and service definitions during this deployment, utilizing them to generate the corresponding service entries in the Marketplace.

The service name follows the convention of `component name - endpoint name`, while all other details remain unchanged.

## Service versioning in the Choreo Marketplace

In the Choreo Marketplace, service versions are displayed in their major version format. Each service in the Choreo Marketplace represents the latest version of the service within its major version, following semantic versioning principles.

For example, if a Choreo service has versions `v1.0`, `v1.1`, `v1.2`, and `v2.0`, the Choreo Marketplace displays services with versions `v1` and `v2` representing the latest versions `v1.2` and `v2.0` respectively.

When you deploy a new minor version of a service already deployed in Choreo, the corresponding service in the marketplace automatically updates to reflect the latest version within the same major version.

### Semantic-version-based intelligent routing in the Choreo Marketplace

When you use a service from the Choreo marketplace as a dependency, the dependent service's traffic automatically routes to the latest version of the corresponding service within the same major version. This ensures that your dependencies remain up-to-date without requiring manual updates within a major version.

For example, if you create a connection to connect your Choreo component named `Foo` to a Choreo service named `Bar`, which is currently available in the Choreo Marketplace as version v1, and if the latest version of the service `Bar` within the v1 range is v1.2, the component `Foo` will automatically connect to `Bar` v1.2.  Subsequently, when `Bar` releases version v1.3, traffic from `Foo` will automatically route to `Bar` v1.3.

## Edit services in the Choreo Marketplace

You can edit services in the Choreo Marketplace. During redeployment to any environment, Choreo automatically updates service definitions, visibility, and descriptions.


# CI/CD

Choreo provides a streamlined continuous integration and continuous deployment (CI/CD) experience to deploy applications and services efficiently across multiple environments.

Choreo creates environments for each project, where all components within the project share the environments. An environment is an isolated deployment area with restricted network and resource access. Services deployed in one environment cannot communicate with services deployed in another.

The Choreo cloud data plane provides two default environments (i.e., development and production). However, if you are in a private data plane organization, you can customize and create multiple environments based on your requirements.

Choreo adopts a *build once, deploy many* strategy to manage components across multiple environments. An application is built only once (i.e., per commit if automatic build on commit is enabled or based on the selected commit during a manual build). Then it is promoted to subsequent environments. This allows testing changes in lower, non-production environments like development before promoting the build to production.

Choreo injects configurations and secrets that you maintain at the environment level into components at runtime. This ensures a strict separation of environment-specific configurations from source code. Although configurations can vary across environments, the code and the built container remain unchanged. Configurations and secrets include:

- Resource credentials to a database, cache, or other backing services.
- Credentials to external cloud services such as Amazon S3 or external APIs.

All configurations and secrets are encrypted at rest and in transit and stored in a secure vault. In a private data plane organization, you can store configurations and secrets in your infrastructure.

## Build

Choreo auto-generates build pipelines that may slightly differ depending on the component type you create. Generally, all build pipelines work as follows:

- Builds a container image either from the provided source code or from a given Dockerfile for a specific commit.
- Runs security and vulnerability scans if applicable, depending on the component type.
- Pushes the container image to a container registry. In the cloud data plane, Choreo pushes the image to a Choreo-managed registry. If it is a private data plane organization, Choreo pushes the image to a registry that you own.
- Updates service endpoints and API specifications from the provided repository if applicable.

In addition to these steps, some buildpacks support integrating unit tests into the build pipeline. For more details, see [Integrate Unit Tests into the Build Pipeline](../develop-components/integrate-unit-tests-into-the-build-pipeline.md).

### Repeatable builds

Choreo can replicate builds from an identical code version (Git commit). This means that multiple builds initiated from the same Git commit will generate Docker images with the same behavior.

!!! note
    In the event of multiple builds from the same code version, Choreo preserves only the most recent version of the Docker image created from the particular code version.

### Trigger a build

On the **Build** page, click **Build Latest**. If necessary, you have the option to select a particular commit and build an image.

!!! note
    Admin and Choreo DevOps users can trigger builds using specific tags from the connected Git repository. However, this action bypasses the standard branch-based deployment process and should only be used for critical, time-sensitive scenarios, as it can disrupt deployment track integrity.

If you want to automatically trigger a build with each commit, you can enable **Auto Build on Commit**.

### Build logs

You can view build logs for specific builds on the **Build** page.

To view details of a specific build, click **View Details** corresponding to the build.

## Deployment

Once you build an image in Choreo, you can deploy it via the **Deploy** page. To deploy an image, you can follow one of the approaches given below:

- **Manually deploy**: In the **Deploy** page, go to the **Set Up** card and click **Deploy**.
- **Automatically deploy on build**: In the **Deploy** page, go to the **Set Up** card and enable **Auto Deploy on Build**. This automatically initiates deployment upon the completion of an automatic build.

!!! info
    To enable **Auto Deploy on Build**, you must enable **Auto Build on Commit**. This is because automatic deployment is not necessary or useful in scenarios where automatic build is not enabled.

!!! note
    - You must trigger the first build in a Ballerina component manually to ensure that Choreo applies the required configurations to the development environment. You can enable automatic builds subsequently.
    - Choreo automatically checks the configurable defined in your source code against the configurable values applied in an environment. Choreo requests the configurable values on deployment and promotion. If you have changed the configurables in your Ballerina component, auto-build pipelines can fail as a precaution to avoid a component crash at runtime due to missing configurables.
    - The configurable verifying capability is only available for Ballerina components. For Dockerfile-based components, ensure to manage and update the configurations and secrets in environments ahead of time. You must also ensure backward compatibility between at least one release if you change the configurations.

### Set up area and initial deployment

In the deploy phase, Choreo uses a setup area to merge the Docker image with its environment-independent configurations. Choreo then deploys this composite to the environment. This is known as the initial deployment.

### Immutable deployments

Once Choreo deploys a component with configurations, the configurations become immutable. Any subsequent change results in a new deployment.

### Promote a component to a higher environment

Choreo builds a container once per GitHub commit and then promotes it to subsequent higher environments.

You can go to the **Deploy** page of a component and promote it manually across environments.

## Configurations

Choreo allows you to define both environment-independent configurations and environment-specific configurations.

### Environment-independent configurations

These configurations apply to all environments.

To change environment-independent configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the **Set Up** card, and then trigger a new deployment to the initial environment. From there, you can proceed to promote the component to higher environments.

### Environment-specific configurations

These configurations apply to a particular environment.

To change environment-specific configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the specific environment card, and trigger a new deployment.

To learn more about managing these configurations, see [Configuration Management](https://wso2.com/choreo/docs/choreo-concepts/configuration-management/).

## Task execution

The information on the **Execute** page is only applicable to scheduled and manual task components.

To track and monitor executions associated with a deployed scheduled task or manual task, go to the left navigation menu and click **Execute**.

You can view current and historic execution details along with a quick snapshot of recent activity via the total count of executions within the last 30 days. For each execution, you can view vital details such as the unique execution ID, the time it was triggered, and relevant revision information. Furthermore, you can dive deeper into the details by clicking on a specific execution to access its associated logs. This information enhances transparency, troubleshooting capabilities, and overall execution management, allowing you to easily monitor and analyze workflows.

## Zero-downtime deployments

Choreo performs rolling updates to ensure zero downtime between deployments and promotions.

A new build undergoes a health check before traffic is switched to it from the current build.

If you configure the necessary health checks for a component, it can prevent deploying and promoting unhealthy versions of a component.


﻿# Component

A component within a project represents a single unit of work in a cloud native application. A component is usually a single microservice, API, or job/task. Each component in Choreo is attached to a given directory path in a Git repository which either contains program source code or a Dockerfile with build instructions. A component is Choreo’s unit of deployment. Each component maps to a single pod in the Kubernetes cluster (data plane) at deployment time. Therefore, you can deploy, manage, and scale each component in Choreo independently.

Choreo supports different component types for various use cases. These include component types such as services, API proxies, integrations, web applications, and so on. Each component type hosts unique features based on its characteristics. For example, a scheduled integration component can accept a cron expression as a configuration to schedule an integration job/task.



# Connections

Services can exist in two main forms: standalone and integrated. Connecting services is an integral part in creating integrated solutions. Choreo allows you to connect services using Connections. 

Using Connections, you can integrate the service you intend to deploy on Choreo with other services on Choreo or external resources. Upon creating a connection to a service on Choreo, Choreo provides you a Connection ID along with a set of connection parameters. Thereafter, you have the capability to configure your service to establish a connection using this Connection ID and map connection parameters to environment variable names in your Choreo component. You can read these environment variable names in your service implementation to retrieve the values, to create a programmatic connection to the service you want to consume. 

At runtime, Choreo dynamically injects values into the environment variables based on the configured mapping. This approach ensures that the connection parameter values and the service connection creation remain loosely coupled, providing developers with flexibility and ease of maintenance.

You can add Connections in different visibility levels: Project and Component. The visibility levels are described below:

## Project Connections

Project Connections are Connections you create to connect to services within a particular project. The Connections **can be used by any component within the project**. 

For example, if you want to share a third-party service like Twilio across the project for all the components within that project to reuse, you can create a project connection. Components can refer to Project Connections using the connection ID. 
Project connections created to consume Choreo services under the OAuth security scheme will share the same OAuth application across the project. Any component reusing such a connection will use the same client ID and client secret.

## Component Connections

Component Connections are Connections you define at the component level and **used by only that component**. 

For example, create a component connection if you want to connect a legacy service to a given component. Components can refer to the Component Connection using the connection ID. 
If your component consumes more than one Choreo service, the Component connections created to consume those Choreo services under the OAuth security scheme can share the same OAuth application by sharing the same client ID and secret between all such connections.

Learn how you can [share and reuse services using connections](../develop-components/sharing-and-reusing/create-a-connection.md) in Choreo.


# Data Planes

Choreo's architecture comprises two key components: the control plane and the data plane. The control plane handles essential tasks such as administering organizations, users, and projects. In addition, it also governs the entire journey of application development, from the initial stages of creation, progressing  to deployment, including measures to enforce governance and the provision for observability. The Choreo control plane is a SaaS that manages all cloud data planes and private data planes. It caters to diverse user personas, including CIOs, architects, and developers, as well as DevOps, site reliability engineers, and platform engineers.

The data plane is the environment where user applications are deployed based on configurations set in the control plane. These applications can range from services and web applications to APIs, integrations, and scheduled tasks. The applications can be written in various programming languages, allowing for a polyglot approach. Importantly, all traffic related to the runtime of user applications is restricted to the Choreo data plane, ensuring strict containment of user data within its boundaries.

Choreo's architecture features two distinct data plane types: cloud data planes and private data planes. A cloud data plane utilizes a multi-tenanted infrastructure model for deploying user applications, creating a shared yet secure environment for application runtime. In contrast, a private data plane(PDP) provides dedicated infrastructure for a single organization to run its user applications. This ensures an added layer of privacy and control for organizations with specific requirements.

![Choreo high-level view](../assets/img/choreo-concepts/high-level-view.png)

## Private data planes

### Infrastructure

Choreo private data planes can be deployed with almost all major cloud providers, such as Azure, AWS, and GCP, and are also compatible with on-premises infrastructure.

The essential requirements for a private data plane include upstream-compatible Kubernetes clusters, a container registry, a key vault (secret store), and a logging service or log storage.

![Private data plane architecture](../assets/img/choreo-concepts/private-data-plane-architecture.png)

### System components

Setting up the Choreo PDP system involves using a Helm installation on the Kubernetes infrastructure. 
The following software components are installed during the helm execution:

  - Cilium CNI and service mesh.
  - Choreo API Gateways and related components.
  - Choreo PDP agent.
  - Observability and logging APIs, along with observability agents.
  - Flux controller.

All of these software components receive automatic updates, including security patches and bug fixes through the flux controller connected to the Choreo Update Management System. 

### Connectivity with the control plane

The private data plane requires communication with the Choreo control plane to manage various activities. All these communications are outbound from the private data plane, ensuring that there is no need to open any specific `IP:Port` from its perspective for these interactions. However, if an organization's network restricts all outbound traffic, it is necessary to permit outbound traffic to the public IP range of the Choreo control plane.

The following table outlines the inbound and outbound connections from a private data plane:

<table border=1>
<thead>
<tr>
<th align="left">Data plane component</th>
<th align="left">Endpoint</th>
<th align="left">Direction</th>
<th align="left">Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2>Choreo PDP agent</td>
<td>Choreo control plane (CP) (mizzen server)</td>
<td>Outbound</td>
<td>WSS</td>
</tr>
<tr>
<td>Kubernetes API server</td>
<td>Outbound (cluster internal)</td>
<td>HTTPS, WS</td>
</tr>
<tr>
<td rowspan=2>APIM/local adaptor</td>
<td>Global adaptor</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Azure Service Bus (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td >APIM/Enforcer</td>
<td>Event hub (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td>Choreo secret resolver</td>
<td>Cloud secret store</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Container registry</td>
<td>Container registry (public)</td>
<td>Inbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Container registry</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Certificate manager</td>
<td>Azure DNS service</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>LetsEncrypt</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux source controller</td>
<td>GitHub</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux Helm controller</td>
<td>Choreo container registry</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
</tbody>
</table> 

All communication between the control plane and the private data plane is secured using TLS.

### Observability architecture

The following diagram depicts the architecture overview of Choreo's in-data-plane log and observability in Azure PDP:

![Observability architecture](../assets/img/choreo-concepts/observability-architecture.png)

The private data plane observability architecture is centered around a strong commitment to data privacy and compliance. This is achieved through a strategic decision to retain logs and observability data within the data planes itself. Key aspects of this architecture include:

- **Data storage at source**: Logs and observability data are stored within the data plane itself, enhancing security, simplifying access, and ensuring compliance.
- **Direct browser-to-data-plane interaction**: The Choreo Console in the user's browser directly interacts with APIs in the data plane, reducing potential data routing complexities and ensuring a more secure, direct flow of information.
- **Reduced data exposure points**: Fetching data directly from the data plane's APIs minimizes the number of data transfer points, effectively decreasing the chances of data exposure or interception.
- **Compliance with regulatory standards**: The architecture supports data locality, aligning with global regulatory standards like GDPR and CCPA by keeping data in its original environment.
- **Improved performance and real-time insights**: Direct interaction between the browser and data plane results in faster data retrieval, providing users with immediate insights.
- **User transparency and control**: Users have a clear view of their data's location and access methods, alongside granular control over data access.

### Security

The Choreo private data plane ensures extensive, production-grade security, ranging from infrastructure and architecture to zero-trust network security. All incoming traffic is protected by a firewall and must undergo authentication and authorization via the API Gateway. It also provides end-to-end network traffic encryption using Cilium transparent encryption, ensuring efficient data path encryption.

For details on the private data plane security levels supported in Choreo pricing plans, see [Private Data Plane Security Levels](../references/private-data-plane-security-levels.md).

### Management models

Choreo supports the following management models for private data planes (PDPs), fostering collaboration between WSO2 and customers across diverse scenarios:

  - WSO2 fully managed (infrastructure and PDP in WSO2 subscription) model
  - WSO2 fully managed (infrastructure and PDP in customer subscription) model
  - Customer self-managed (WSO2 provides installation script and updates) model

To explore each management model in detail so that you can make informed decisions depending on the supported cloud-based operations and security, see [Private Data Plane Management Models](../references/private-data-plane-management-models.md).


# Deployment Tracks

Deployment Tracks in Choreo are structured pathways for simplified software component deployment. They act like advanced CI/CD pipelines, ensuring your components reach their destinations seamlessly, whether from source code or prebuilt images. They establish an organized and structured approach that minimizes the chances of errors and challenges that are typically associated with deployment workflows.

## The significance of Deployment Tracks

Deployment Tracks offer practical solutions to enhance the API consumer experience by addressing two critical challenges:

- **Streamlined deployment**: Deployment Tracks serve as well-designed routes for your software components, enhancing the organization and reliability of the deployment process, similar to a well-structured express route.

- **Efficient API versioning**: Especially beneficial for managed APIs, Deployment Tracks provide a straightforward method for creating API versions that seamlessly interact with previous iterations. This simplified version management benefits both API creators and consumers alike.

## Streamlined deployments

For streamlined deployments, Choreo dissects two integral approaches that leverage Deployment Tracks: the comprehensive CI/CD integration and the focused CD-Only strategy.

### CI/CD with Deployment Tracks

A deployment track is linked to a particular branch within a GitHub repository. This connection is useful for handling deployments to various environments. On Choreo's Deploy page, you can easily visualize the deployments to specific environments associated with your selected deployment track. Moreover, the deployment track has a functionality that initiates automatic deployments for the linked branch. When activated, merging a pull request (PR) triggers a deployment to the development environment.

![Deployment tracks - source repo](../assets/img/choreo-concepts/deployment-tracks-source-repo.png){.cInlineImage-half}

### CD-Only strategy with Deployment Tracks

If you're inclined to use your own Continuous Integration (CI) systems and want to harness the deployment track as a Continuous Deployment (CD) pipeline, you can seamlessly link deployment tracks to a container registry repository. This configuration empowers users to effortlessly deploy images sourced directly from the linked container registry repository.

![Deployment tracks - container registry](../assets/img/choreo-concepts/deployment-tracks-container-registry.png){.cInlineImage-half}


## Efficient API versioning

**This section applies to only service components**. When working with service components in Choreo, it is important to have an effective API versioning mechanism. Choreo follows a versioning mechanism based on Semantic Versioning (SemVer) but only includes the major version and minor version with the prefix `v`. 

For example, `v1.2`. 

You can follow the approach given below when you version APIs in Choreo:

  - Increment the major version when you make incompatible API changes.
  - Increment the minor version when you add functionality in a backward-compatible manner.

!!! info "What is Semantic Versioning?"
    Semantic Versioning (SemVer) is a specification that defines how to assign and increment version numbers for software products, including APIs. For more information, see [Semantic Versioning specification](https://semver.org/#semantic-versioning-specification-semver).

One of the primary concerns when dealing with SaaS APIs is to minimize disruption for API consumers while continuously developing and deploying updates.

In compliance with SemVer, changes that don't introduce breaking or additive modifications to the API are categorized as patch updates. Hover, from the perspective of API consumers, these changes should ideally not disrupt their API clients. Typically, API consumers are most concerned with major API version alterations, but there might be instances where minor version changes are communicated to them.

Therefore, in the context of deployment tracks, API developers only need to specify the major and minor versions being delivered from a particular deployment track. This information is treated as the API version attribute of a deployment track. If the publisher requires versioning for internal tracking purposes, this can be accomplished in Git through the use of Git tags, on GitHub with GitHub releases, and so forth.

![Deployment tracks - api versioning](../assets/img/choreo-concepts/deployment-tracks-api-versioning.md.png){.cInlineImage-half}


﻿# Endpoint

An Endpoint is a network-exposed function that resides within a component. In Choreo, service and integration components expose one or more endpoints. Each endpoint in a component can have a service contract (OpenAPI, GraphQL SDL) associated with it. This contract is used to expose the endpoint to consumers. In the absence of a contract, Choreo uses /* exposed on all HTTP verbs as the default contract to expose the service or the integration.

Each endpoint exposed in a component is considered a single API. Therefore, Choreo allows you to do API management per endpoint for a given component. For example, you can perform lifecycle management and configure security settings per endpoint in a given component.


See [Configure Endpoints](../develop-components/configure-endpoints.md) to learn how to configure endpoints when developing components in Choreo. 

# Environments

Choreo offers developers one or more environments to run their applications within a given data plane. By default, the Choreo cloud data plane provides two environments (i.e., development and production). Each project in Choreo is associated with one or more  environments available in the organization. For example, project A may choose to utilize dev, staging, and production environments, while project B may only use development and production environments.

You can promote components within a project across available environments. When you promote a component, its configuration values can be overridden with environment-specific values.

The following diagram illustrates how a component is promoted across environments.

![Choreo environments](../assets/img/choreo-concepts/choreo-environments.png){.cInlineImage-threeQuarter}


﻿# Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization.

## Switch organizations

If you are a member of more than one organization, you can switch from one organization to another when necessary. To do this, select the required organization from the **Organization** list in the Choreo Console header.

{% include "../administer/inviting-members.md" %}

## Manage user permission

Choreo manages user permissions with groups and roles.

### Groups

A group in Choreo is a collection of users, each with one or more roles assigned to them. Users within a group inherit the permissions associated with the roles assigned to that group. For instance, if a user is added to the `API Publisher` group, they will automatically receive the `API Publisher` role.

Choreo comes with predefined groups already configured with specific roles, as follows:

- **API Publisher**: A collection of users who have the API Publisher role.
- **API Subscriber**: A collection of users who have the API Subscriber role.
- **Admin** : A collection of users who have the Admin role.
- **Billing Admin** : A collection of users who have the Billing Admin role.
- **Choreo DevOps** : A collection of users who have the Choreo DevOps role.
- **Developer** : Users who develop, deploy, and manage cloud native applications at scale.
- **External API Subscriber**: A collection of users who have the External API Subscriber role.

When creating a new group to invite members, be sure to assign a role to the group to ensure users have the required permissions.

### Roles

Choreo roles are defined as follows:

- **API Publisher**: An API publisher can discover, create, publish, delete, test, and manage an API.
- **API Subscriber**: An API subscriber is a developer in a particular organization. An API subscriber can subscribe to an application, manage subscriptions, manage applications, generate API keys, and manage API keys.
- **Admin**: An administrator is responsible for all administration tasks, including user management, customizing the Developer Portal, managing projects, enabling analytics, managing domains, etc.
- **Billing Admin**: Is responsible for billing administration that includes viewing tiers, creating and viewing organizations, managing invoices, viewing and creating subscriptions, and viewing and creating payment methods.
- **Choreo DevOps**: A Choreo DevOps user is a user with access to the Choreo DevOps portal, enabling them to actively manage, ensure dependable deployment, and monitor components.
- **Developer** : A user who can develop, deploy, and manage cloud native applications at scale.  
- **External API subscriber**: External API subscribers are API consumers who have access only to the API Developer Portal. They can join an organization with the sole purpose of consuming APIs.
- **Environment Manager (Deprecated)**: Manages deployment environments.

## Organization ID

The Organization ID serves as a unique identifier for each organization. To get the organization ID, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. In the header, click the **Organization** list. This will open the organization level settings page. 
5. Under **Organization** click **Copy ID**.

## Organization Handle

The organization handle is a unique string that directly corresponds to your organization's name. To get the organization handle, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. Under **Organization** click **Copy Handle**.


﻿# Project

A project in Choreo is a logical group of related components that typically represent a single cloud native application. A project consists of one or more components. All components within a project can ideally be (but is not restricted to) in a single GitHub repository under different paths. This is also known as the monorepo architecture.

At deployment time, all components within a given project are deployed into a single namespace of the Kubernetes cluster. Components within a project can be exposed to the public internet, internally to the rest of the organization, or privately within the project only. A project in Choreo is represented as a cell with regard to the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md). The following diagram illustrates a project and how the components within a project are laid out at runtime:

![Project](../assets/img/choreo-concepts/project.png){.cInlineImage-full}








# Resource Hierarchy


The following diagram depicts the high-level resources and their relationships in Choreo.

![Resource hierarchy](../assets/img/choreo-concepts/resource-hierarchy.png){.cInlineImage-full}

## Organizations and data planes

Data planes are connected to the organization and are available for all projects within the organization. When you create an environment in a project, the data plane connected to the organization is linked with an automatically generated Kubernetes namespace.

## Environments and data planes

Choreo allows multiple Kubernetes clusters to be associated with an environment. This enables you to build highly resilient and resource-efficient solutions that utilize multiple clusters. Choreo synchronizes your applications and workloads between associated clusters in an environment, allowing you to perform multi-cluster deployment with a single click.

The following diagram illustrates how multiple clusters associate with different environments:

![Environments and dataplanes](../assets/img/choreo-concepts/environments-and-dataplanes.png){.cInlineImage-full}

!!! info "Note"
    It is not necessary to use a different cluster per environment. You can create multiple environments on the same cluster. The above diagram is an example of a specific solution. Your application architecture may require a different configuration than what is depicted.

## Components and environments

Components belong to a project in Choreo, and environments are provisioned per project. When a component is deployed, it is deployed as a container to the specified environment. Once deployed, you can promote the container image across the environments available in the project.



# Choreo Marketplace

The Choreo Marketplace promotes and facilitates reusing and sharing services. It allows you to share all the services deployed in Choreo.
You can easily browse and search available services within the Marketplace and refer to the service definitions, documentation, instructions on how you can use it, etc. 

![Internal Marketplace](../assets/img/choreo-concepts/marketplace/internal-marketplace.png){.cInlineImage-full}

## Discover services

The Marketplace includes all services deployed in your organization. This may be a large number of services. Therefore, effective discoverability is desirable.

You can use the search or apply various filter criteria to explore the services available.

### Search

The top search bar provides universal searching to find the services. It allows you to search for a text in the following search attributes:

- **Name**: The service name.
- **Label**: The service labels.
- **Content**: The service content: overview, summary, and documentation.
- **All**: All of the above criteria.

### Filter

The Choreo Marketplace provides a filtering capability through the left-hand side filter panel. It allows you to filter with the following filter attributes:

- **Type**: This filter enables you to categorize services based on their type, with two available options: "Internal" and "Third-party". "Internal" refers to services deployed within Choreo, while "Third-party" refers to services running externally to Choreo, independently added to the Marketplace.

- **Network Visibility**: This filter enables you to categorize services based on their network visibility level, with three choices: "Public," "Organization," and "Project".  "Public" filters services exposed publicly, "Organization" represents services exposed across the entire organization, and "Project" represents services exposed at the project level.


## Explore a service 

You can click on the service card to open the detailed view of the service. The detailed service page features the service name, summary, version, labels, and service icon as the header.

Choreo organizes the service content into four tabs. The four tabs contain information as follows: 

- **Overview**: Choreo displays the service overview provided by the service developer. If the service developer has not provided any content at service creation, this section will be disabled. The service developer can provide the overview content via the Manage → Marketplace section of the component.

- **API definition**: Includes the API definition for the service, extracted from the `component.yaml` file in the user repository. If an API definition is not provided, this tab will be empty.

    !!! note
        If you are are currently using the `component-config.yaml` or `endpoints.yaml` configuration files, see the respective [migration guide](../develop-components/manage-component-source-configurations.md#migration-guide) for instructions on migrating to the recommended `component.yaml` configuration file.

- **How to use**: Includes instructions on how to use the selected service. This includes instructions on [creating a connection](../develop-components/sharing-and-reusing/create-a-connection.md).

- **Related documents**: Includes any additional content the user has provided as documents through the Manage -> Marketplace section of the component.

## Add a service to the Choreo Marketplace

You can add services to the Marketplace as Choreo services as follows: 

### Add a Choreo service

In Choreo, a service exposed through the platform is termed a Choreo service, with each service being identifiable by an endpoint within a Choreo service component. The Marketplace showcases a service for each endpoint within a service component.

Upon deployment to the initial environment, services get automatically added to the Marketplace. Choreo effortlessly collects essential details such as component name, endpoint name, description, and service definitions during this deployment, utilizing them to generate the corresponding service entries in the Marketplace.

The service name follows the convention of `component name - endpoint name`, while all other details remain unchanged.

## Service versioning in the Choreo Marketplace

In the Choreo Marketplace, service versions are displayed in their major version format. Each service in the Choreo Marketplace represents the latest version of the service within its major version, following semantic versioning principles.

For example, if a Choreo service has versions `v1.0`, `v1.1`, `v1.2`, and `v2.0`, the Choreo Marketplace displays services with versions `v1` and `v2` representing the latest versions `v1.2` and `v2.0` respectively.

When you deploy a new minor version of a service already deployed in Choreo, the corresponding service in the marketplace automatically updates to reflect the latest version within the same major version.

### Semantic-version-based intelligent routing in the Choreo Marketplace

When you use a service from the Choreo marketplace as a dependency, the dependent service's traffic automatically routes to the latest version of the corresponding service within the same major version. This ensures that your dependencies remain up-to-date without requiring manual updates within a major version.

For example, if you create a connection to connect your Choreo component named `Foo` to a Choreo service named `Bar`, which is currently available in the Choreo Marketplace as version v1, and if the latest version of the service `Bar` within the v1 range is v1.2, the component `Foo` will automatically connect to `Bar` v1.2.  Subsequently, when `Bar` releases version v1.3, traffic from `Foo` will automatically route to `Bar` v1.3.

## Edit services in the Choreo Marketplace

You can edit services in the Choreo Marketplace. During redeployment to any environment, Choreo automatically updates service definitions, visibility, and descriptions.


# CI/CD

Choreo provides a streamlined continuous integration and continuous deployment (CI/CD) experience to deploy applications and services efficiently across multiple environments.

Choreo creates environments for each project, where all components within the project share the environments. An environment is an isolated deployment area with restricted network and resource access. Services deployed in one environment cannot communicate with services deployed in another.

The Choreo cloud data plane provides two default environments (i.e., development and production). However, if you are in a private data plane organization, you can customize and create multiple environments based on your requirements.

Choreo adopts a *build once, deploy many* strategy to manage components across multiple environments. An application is built only once (i.e., per commit if automatic build on commit is enabled or based on the selected commit during a manual build). Then it is promoted to subsequent environments. This allows testing changes in lower, non-production environments like development before promoting the build to production.

Choreo injects configurations and secrets that you maintain at the environment level into components at runtime. This ensures a strict separation of environment-specific configurations from source code. Although configurations can vary across environments, the code and the built container remain unchanged. Configurations and secrets include:

- Resource credentials to a database, cache, or other backing services.
- Credentials to external cloud services such as Amazon S3 or external APIs.

All configurations and secrets are encrypted at rest and in transit and stored in a secure vault. In a private data plane organization, you can store configurations and secrets in your infrastructure.

## Build

Choreo auto-generates build pipelines that may slightly differ depending on the component type you create. Generally, all build pipelines work as follows:

- Builds a container image either from the provided source code or from a given Dockerfile for a specific commit.
- Runs security and vulnerability scans if applicable, depending on the component type.
- Pushes the container image to a container registry. In the cloud data plane, Choreo pushes the image to a Choreo-managed registry. If it is a private data plane organization, Choreo pushes the image to a registry that you own.
- Updates service endpoints and API specifications from the provided repository if applicable.

In addition to these steps, some buildpacks support integrating unit tests into the build pipeline. For more details, see [Integrate Unit Tests into the Build Pipeline](../develop-components/integrate-unit-tests-into-the-build-pipeline.md).

### Repeatable builds

Choreo can replicate builds from an identical code version (Git commit). This means that multiple builds initiated from the same Git commit will generate Docker images with the same behavior.

!!! note
    In the event of multiple builds from the same code version, Choreo preserves only the most recent version of the Docker image created from the particular code version.

### Trigger a build

On the **Build** page, click **Build Latest**. If necessary, you have the option to select a particular commit and build an image.

!!! note
    Admin and Choreo DevOps users can trigger builds using specific tags from the connected Git repository. However, this action bypasses the standard branch-based deployment process and should only be used for critical, time-sensitive scenarios, as it can disrupt deployment track integrity.

If you want to automatically trigger a build with each commit, you can enable **Auto Build on Commit**.

### Build logs

You can view build logs for specific builds on the **Build** page.

To view details of a specific build, click **View Details** corresponding to the build.

## Deployment

Once you build an image in Choreo, you can deploy it via the **Deploy** page. To deploy an image, you can follow one of the approaches given below:

- **Manually deploy**: In the **Deploy** page, go to the **Set Up** card and click **Deploy**.
- **Automatically deploy on build**: In the **Deploy** page, go to the **Set Up** card and enable **Auto Deploy on Build**. This automatically initiates deployment upon the completion of an automatic build.

!!! info
    To enable **Auto Deploy on Build**, you must enable **Auto Build on Commit**. This is because automatic deployment is not necessary or useful in scenarios where automatic build is not enabled.

!!! note
    - You must trigger the first build in a Ballerina component manually to ensure that Choreo applies the required configurations to the development environment. You can enable automatic builds subsequently.
    - Choreo automatically checks the configurable defined in your source code against the configurable values applied in an environment. Choreo requests the configurable values on deployment and promotion. If you have changed the configurables in your Ballerina component, auto-build pipelines can fail as a precaution to avoid a component crash at runtime due to missing configurables.
    - The configurable verifying capability is only available for Ballerina components. For Dockerfile-based components, ensure to manage and update the configurations and secrets in environments ahead of time. You must also ensure backward compatibility between at least one release if you change the configurations.

### Set up area and initial deployment

In the deploy phase, Choreo uses a setup area to merge the Docker image with its environment-independent configurations. Choreo then deploys this composite to the environment. This is known as the initial deployment.

### Immutable deployments

Once Choreo deploys a component with configurations, the configurations become immutable. Any subsequent change results in a new deployment.

### Promote a component to a higher environment

Choreo builds a container once per GitHub commit and then promotes it to subsequent higher environments.

You can go to the **Deploy** page of a component and promote it manually across environments.

## Configurations

Choreo allows you to define both environment-independent configurations and environment-specific configurations.

### Environment-independent configurations

These configurations apply to all environments.

To change environment-independent configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the **Set Up** card, and then trigger a new deployment to the initial environment. From there, you can proceed to promote the component to higher environments.

### Environment-specific configurations

These configurations apply to a particular environment.

To change environment-specific configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the specific environment card, and trigger a new deployment.

To learn more about managing these configurations, see [Configuration Management](https://wso2.com/choreo/docs/choreo-concepts/configuration-management/).

## Task execution

The information on the **Execute** page is only applicable to scheduled and manual task components.

To track and monitor executions associated with a deployed scheduled task or manual task, go to the left navigation menu and click **Execute**.

You can view current and historic execution details along with a quick snapshot of recent activity via the total count of executions within the last 30 days. For each execution, you can view vital details such as the unique execution ID, the time it was triggered, and relevant revision information. Furthermore, you can dive deeper into the details by clicking on a specific execution to access its associated logs. This information enhances transparency, troubleshooting capabilities, and overall execution management, allowing you to easily monitor and analyze workflows.

## Zero-downtime deployments

Choreo performs rolling updates to ensure zero downtime between deployments and promotions.

A new build undergoes a health check before traffic is switched to it from the current build.

If you configure the necessary health checks for a component, it can prevent deploying and promoting unhealthy versions of a component.


﻿# Component

A component within a project represents a single unit of work in a cloud native application. A component is usually a single microservice, API, or job/task. Each component in Choreo is attached to a given directory path in a Git repository which either contains program source code or a Dockerfile with build instructions. A component is Choreo’s unit of deployment. Each component maps to a single pod in the Kubernetes cluster (data plane) at deployment time. Therefore, you can deploy, manage, and scale each component in Choreo independently.

Choreo supports different component types for various use cases. These include component types such as services, API proxies, integrations, web applications, and so on. Each component type hosts unique features based on its characteristics. For example, a scheduled integration component can accept a cron expression as a configuration to schedule an integration job/task.



# Connections

Services can exist in two main forms: standalone and integrated. Connecting services is an integral part in creating integrated solutions. Choreo allows you to connect services using Connections. 

Using Connections, you can integrate the service you intend to deploy on Choreo with other services on Choreo or external resources. Upon creating a connection to a service on Choreo, Choreo provides you a Connection ID along with a set of connection parameters. Thereafter, you have the capability to configure your service to establish a connection using this Connection ID and map connection parameters to environment variable names in your Choreo component. You can read these environment variable names in your service implementation to retrieve the values, to create a programmatic connection to the service you want to consume. 

At runtime, Choreo dynamically injects values into the environment variables based on the configured mapping. This approach ensures that the connection parameter values and the service connection creation remain loosely coupled, providing developers with flexibility and ease of maintenance.

You can add Connections in different visibility levels: Project and Component. The visibility levels are described below:

## Project Connections

Project Connections are Connections you create to connect to services within a particular project. The Connections **can be used by any component within the project**. 

For example, if you want to share a third-party service like Twilio across the project for all the components within that project to reuse, you can create a project connection. Components can refer to Project Connections using the connection ID. 
Project connections created to consume Choreo services under the OAuth security scheme will share the same OAuth application across the project. Any component reusing such a connection will use the same client ID and client secret.

## Component Connections

Component Connections are Connections you define at the component level and **used by only that component**. 

For example, create a component connection if you want to connect a legacy service to a given component. Components can refer to the Component Connection using the connection ID. 
If your component consumes more than one Choreo service, the Component connections created to consume those Choreo services under the OAuth security scheme can share the same OAuth application by sharing the same client ID and secret between all such connections.

Learn how you can [share and reuse services using connections](../develop-components/sharing-and-reusing/create-a-connection.md) in Choreo.


# Data Planes

Choreo's architecture comprises two key components: the control plane and the data plane. The control plane handles essential tasks such as administering organizations, users, and projects. In addition, it also governs the entire journey of application development, from the initial stages of creation, progressing  to deployment, including measures to enforce governance and the provision for observability. The Choreo control plane is a SaaS that manages all cloud data planes and private data planes. It caters to diverse user personas, including CIOs, architects, and developers, as well as DevOps, site reliability engineers, and platform engineers.

The data plane is the environment where user applications are deployed based on configurations set in the control plane. These applications can range from services and web applications to APIs, integrations, and scheduled tasks. The applications can be written in various programming languages, allowing for a polyglot approach. Importantly, all traffic related to the runtime of user applications is restricted to the Choreo data plane, ensuring strict containment of user data within its boundaries.

Choreo's architecture features two distinct data plane types: cloud data planes and private data planes. A cloud data plane utilizes a multi-tenanted infrastructure model for deploying user applications, creating a shared yet secure environment for application runtime. In contrast, a private data plane(PDP) provides dedicated infrastructure for a single organization to run its user applications. This ensures an added layer of privacy and control for organizations with specific requirements.

![Choreo high-level view](../assets/img/choreo-concepts/high-level-view.png)

## Private data planes

### Infrastructure

Choreo private data planes can be deployed with almost all major cloud providers, such as Azure, AWS, and GCP, and are also compatible with on-premises infrastructure.

The essential requirements for a private data plane include upstream-compatible Kubernetes clusters, a container registry, a key vault (secret store), and a logging service or log storage.

![Private data plane architecture](../assets/img/choreo-concepts/private-data-plane-architecture.png)

### System components

Setting up the Choreo PDP system involves using a Helm installation on the Kubernetes infrastructure. 
The following software components are installed during the helm execution:

  - Cilium CNI and service mesh.
  - Choreo API Gateways and related components.
  - Choreo PDP agent.
  - Observability and logging APIs, along with observability agents.
  - Flux controller.

All of these software components receive automatic updates, including security patches and bug fixes through the flux controller connected to the Choreo Update Management System. 

### Connectivity with the control plane

The private data plane requires communication with the Choreo control plane to manage various activities. All these communications are outbound from the private data plane, ensuring that there is no need to open any specific `IP:Port` from its perspective for these interactions. However, if an organization's network restricts all outbound traffic, it is necessary to permit outbound traffic to the public IP range of the Choreo control plane.

The following table outlines the inbound and outbound connections from a private data plane:

<table border=1>
<thead>
<tr>
<th align="left">Data plane component</th>
<th align="left">Endpoint</th>
<th align="left">Direction</th>
<th align="left">Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2>Choreo PDP agent</td>
<td>Choreo control plane (CP) (mizzen server)</td>
<td>Outbound</td>
<td>WSS</td>
</tr>
<tr>
<td>Kubernetes API server</td>
<td>Outbound (cluster internal)</td>
<td>HTTPS, WS</td>
</tr>
<tr>
<td rowspan=2>APIM/local adaptor</td>
<td>Global adaptor</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Azure Service Bus (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td >APIM/Enforcer</td>
<td>Event hub (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td>Choreo secret resolver</td>
<td>Cloud secret store</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Container registry</td>
<td>Container registry (public)</td>
<td>Inbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Container registry</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Certificate manager</td>
<td>Azure DNS service</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>LetsEncrypt</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux source controller</td>
<td>GitHub</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux Helm controller</td>
<td>Choreo container registry</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
</tbody>
</table> 

All communication between the control plane and the private data plane is secured using TLS.

### Observability architecture

The following diagram depicts the architecture overview of Choreo's in-data-plane log and observability in Azure PDP:

![Observability architecture](../assets/img/choreo-concepts/observability-architecture.png)

The private data plane observability architecture is centered around a strong commitment to data privacy and compliance. This is achieved through a strategic decision to retain logs and observability data within the data planes itself. Key aspects of this architecture include:

- **Data storage at source**: Logs and observability data are stored within the data plane itself, enhancing security, simplifying access, and ensuring compliance.
- **Direct browser-to-data-plane interaction**: The Choreo Console in the user's browser directly interacts with APIs in the data plane, reducing potential data routing complexities and ensuring a more secure, direct flow of information.
- **Reduced data exposure points**: Fetching data directly from the data plane's APIs minimizes the number of data transfer points, effectively decreasing the chances of data exposure or interception.
- **Compliance with regulatory standards**: The architecture supports data locality, aligning with global regulatory standards like GDPR and CCPA by keeping data in its original environment.
- **Improved performance and real-time insights**: Direct interaction between the browser and data plane results in faster data retrieval, providing users with immediate insights.
- **User transparency and control**: Users have a clear view of their data's location and access methods, alongside granular control over data access.

### Security

The Choreo private data plane ensures extensive, production-grade security, ranging from infrastructure and architecture to zero-trust network security. All incoming traffic is protected by a firewall and must undergo authentication and authorization via the API Gateway. It also provides end-to-end network traffic encryption using Cilium transparent encryption, ensuring efficient data path encryption.

For details on the private data plane security levels supported in Choreo pricing plans, see [Private Data Plane Security Levels](../references/private-data-plane-security-levels.md).

### Management models

Choreo supports the following management models for private data planes (PDPs), fostering collaboration between WSO2 and customers across diverse scenarios:

  - WSO2 fully managed (infrastructure and PDP in WSO2 subscription) model
  - WSO2 fully managed (infrastructure and PDP in customer subscription) model
  - Customer self-managed (WSO2 provides installation script and updates) model

To explore each management model in detail so that you can make informed decisions depending on the supported cloud-based operations and security, see [Private Data Plane Management Models](../references/private-data-plane-management-models.md).


# Deployment Tracks

Deployment Tracks in Choreo are structured pathways for simplified software component deployment. They act like advanced CI/CD pipelines, ensuring your components reach their destinations seamlessly, whether from source code or prebuilt images. They establish an organized and structured approach that minimizes the chances of errors and challenges that are typically associated with deployment workflows.

## The significance of Deployment Tracks

Deployment Tracks offer practical solutions to enhance the API consumer experience by addressing two critical challenges:

- **Streamlined deployment**: Deployment Tracks serve as well-designed routes for your software components, enhancing the organization and reliability of the deployment process, similar to a well-structured express route.

- **Efficient API versioning**: Especially beneficial for managed APIs, Deployment Tracks provide a straightforward method for creating API versions that seamlessly interact with previous iterations. This simplified version management benefits both API creators and consumers alike.

## Streamlined deployments

For streamlined deployments, Choreo dissects two integral approaches that leverage Deployment Tracks: the comprehensive CI/CD integration and the focused CD-Only strategy.

### CI/CD with Deployment Tracks

A deployment track is linked to a particular branch within a GitHub repository. This connection is useful for handling deployments to various environments. On Choreo's Deploy page, you can easily visualize the deployments to specific environments associated with your selected deployment track. Moreover, the deployment track has a functionality that initiates automatic deployments for the linked branch. When activated, merging a pull request (PR) triggers a deployment to the development environment.

![Deployment tracks - source repo](../assets/img/choreo-concepts/deployment-tracks-source-repo.png){.cInlineImage-half}

### CD-Only strategy with Deployment Tracks

If you're inclined to use your own Continuous Integration (CI) systems and want to harness the deployment track as a Continuous Deployment (CD) pipeline, you can seamlessly link deployment tracks to a container registry repository. This configuration empowers users to effortlessly deploy images sourced directly from the linked container registry repository.

![Deployment tracks - container registry](../assets/img/choreo-concepts/deployment-tracks-container-registry.png){.cInlineImage-half}


## Efficient API versioning

**This section applies to only service components**. When working with service components in Choreo, it is important to have an effective API versioning mechanism. Choreo follows a versioning mechanism based on Semantic Versioning (SemVer) but only includes the major version and minor version with the prefix `v`. 

For example, `v1.2`. 

You can follow the approach given below when you version APIs in Choreo:

  - Increment the major version when you make incompatible API changes.
  - Increment the minor version when you add functionality in a backward-compatible manner.

!!! info "What is Semantic Versioning?"
    Semantic Versioning (SemVer) is a specification that defines how to assign and increment version numbers for software products, including APIs. For more information, see [Semantic Versioning specification](https://semver.org/#semantic-versioning-specification-semver).

One of the primary concerns when dealing with SaaS APIs is to minimize disruption for API consumers while continuously developing and deploying updates.

In compliance with SemVer, changes that don't introduce breaking or additive modifications to the API are categorized as patch updates. Hover, from the perspective of API consumers, these changes should ideally not disrupt their API clients. Typically, API consumers are most concerned with major API version alterations, but there might be instances where minor version changes are communicated to them.

Therefore, in the context of deployment tracks, API developers only need to specify the major and minor versions being delivered from a particular deployment track. This information is treated as the API version attribute of a deployment track. If the publisher requires versioning for internal tracking purposes, this can be accomplished in Git through the use of Git tags, on GitHub with GitHub releases, and so forth.

![Deployment tracks - api versioning](../assets/img/choreo-concepts/deployment-tracks-api-versioning.md.png){.cInlineImage-half}


﻿# Endpoint

An Endpoint is a network-exposed function that resides within a component. In Choreo, service and integration components expose one or more endpoints. Each endpoint in a component can have a service contract (OpenAPI, GraphQL SDL) associated with it. This contract is used to expose the endpoint to consumers. In the absence of a contract, Choreo uses /* exposed on all HTTP verbs as the default contract to expose the service or the integration.

Each endpoint exposed in a component is considered a single API. Therefore, Choreo allows you to do API management per endpoint for a given component. For example, you can perform lifecycle management and configure security settings per endpoint in a given component.


See [Configure Endpoints](../develop-components/configure-endpoints.md) to learn how to configure endpoints when developing components in Choreo. 

# Environments

Choreo offers developers one or more environments to run their applications within a given data plane. By default, the Choreo cloud data plane provides two environments (i.e., development and production). Each project in Choreo is associated with one or more  environments available in the organization. For example, project A may choose to utilize dev, staging, and production environments, while project B may only use development and production environments.

You can promote components within a project across available environments. When you promote a component, its configuration values can be overridden with environment-specific values.

The following diagram illustrates how a component is promoted across environments.

![Choreo environments](../assets/img/choreo-concepts/choreo-environments.png){.cInlineImage-threeQuarter}


﻿# Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization.

## Switch organizations

If you are a member of more than one organization, you can switch from one organization to another when necessary. To do this, select the required organization from the **Organization** list in the Choreo Console header.

{% include "../administer/inviting-members.md" %}

## Manage user permission

Choreo manages user permissions with groups and roles.

### Groups

A group in Choreo is a collection of users, each with one or more roles assigned to them. Users within a group inherit the permissions associated with the roles assigned to that group. For instance, if a user is added to the `API Publisher` group, they will automatically receive the `API Publisher` role.

Choreo comes with predefined groups already configured with specific roles, as follows:

- **API Publisher**: A collection of users who have the API Publisher role.
- **API Subscriber**: A collection of users who have the API Subscriber role.
- **Admin** : A collection of users who have the Admin role.
- **Billing Admin** : A collection of users who have the Billing Admin role.
- **Choreo DevOps** : A collection of users who have the Choreo DevOps role.
- **Developer** : Users who develop, deploy, and manage cloud native applications at scale.
- **External API Subscriber**: A collection of users who have the External API Subscriber role.

When creating a new group to invite members, be sure to assign a role to the group to ensure users have the required permissions.

### Roles

Choreo roles are defined as follows:

- **API Publisher**: An API publisher can discover, create, publish, delete, test, and manage an API.
- **API Subscriber**: An API subscriber is a developer in a particular organization. An API subscriber can subscribe to an application, manage subscriptions, manage applications, generate API keys, and manage API keys.
- **Admin**: An administrator is responsible for all administration tasks, including user management, customizing the Developer Portal, managing projects, enabling analytics, managing domains, etc.
- **Billing Admin**: Is responsible for billing administration that includes viewing tiers, creating and viewing organizations, managing invoices, viewing and creating subscriptions, and viewing and creating payment methods.
- **Choreo DevOps**: A Choreo DevOps user is a user with access to the Choreo DevOps portal, enabling them to actively manage, ensure dependable deployment, and monitor components.
- **Developer** : A user who can develop, deploy, and manage cloud native applications at scale.  
- **External API subscriber**: External API subscribers are API consumers who have access only to the API Developer Portal. They can join an organization with the sole purpose of consuming APIs.
- **Environment Manager (Deprecated)**: Manages deployment environments.

## Organization ID

The Organization ID serves as a unique identifier for each organization. To get the organization ID, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. In the header, click the **Organization** list. This will open the organization level settings page. 
5. Under **Organization** click **Copy ID**.

## Organization Handle

The organization handle is a unique string that directly corresponds to your organization's name. To get the organization handle, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. Under **Organization** click **Copy Handle**.


﻿# Project

A project in Choreo is a logical group of related components that typically represent a single cloud native application. A project consists of one or more components. All components within a project can ideally be (but is not restricted to) in a single GitHub repository under different paths. This is also known as the monorepo architecture.

At deployment time, all components within a given project are deployed into a single namespace of the Kubernetes cluster. Components within a project can be exposed to the public internet, internally to the rest of the organization, or privately within the project only. A project in Choreo is represented as a cell with regard to the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md). The following diagram illustrates a project and how the components within a project are laid out at runtime:

![Project](../assets/img/choreo-concepts/project.png){.cInlineImage-full}








# Resource Hierarchy


The following diagram depicts the high-level resources and their relationships in Choreo.

![Resource hierarchy](../assets/img/choreo-concepts/resource-hierarchy.png){.cInlineImage-full}

## Organizations and data planes

Data planes are connected to the organization and are available for all projects within the organization. When you create an environment in a project, the data plane connected to the organization is linked with an automatically generated Kubernetes namespace.

## Environments and data planes

Choreo allows multiple Kubernetes clusters to be associated with an environment. This enables you to build highly resilient and resource-efficient solutions that utilize multiple clusters. Choreo synchronizes your applications and workloads between associated clusters in an environment, allowing you to perform multi-cluster deployment with a single click.

The following diagram illustrates how multiple clusters associate with different environments:

![Environments and dataplanes](../assets/img/choreo-concepts/environments-and-dataplanes.png){.cInlineImage-full}

!!! info "Note"
    It is not necessary to use a different cluster per environment. You can create multiple environments on the same cluster. The above diagram is an example of a specific solution. Your application architecture may require a different configuration than what is depicted.

## Components and environments

Components belong to a project in Choreo, and environments are provisioned per project. When a component is deployed, it is deployed as a container to the specified environment. Once deployed, you can promote the container image across the environments available in the project.



# Choreo Marketplace

The Choreo Marketplace promotes and facilitates reusing and sharing services. It allows you to share all the services deployed in Choreo.
You can easily browse and search available services within the Marketplace and refer to the service definitions, documentation, instructions on how you can use it, etc. 

![Internal Marketplace](../assets/img/choreo-concepts/marketplace/internal-marketplace.png){.cInlineImage-full}

## Discover services

The Marketplace includes all services deployed in your organization. This may be a large number of services. Therefore, effective discoverability is desirable.

You can use the search or apply various filter criteria to explore the services available.

### Search

The top search bar provides universal searching to find the services. It allows you to search for a text in the following search attributes:

- **Name**: The service name.
- **Label**: The service labels.
- **Content**: The service content: overview, summary, and documentation.
- **All**: All of the above criteria.

### Filter

The Choreo Marketplace provides a filtering capability through the left-hand side filter panel. It allows you to filter with the following filter attributes:

- **Type**: This filter enables you to categorize services based on their type, with two available options: "Internal" and "Third-party". "Internal" refers to services deployed within Choreo, while "Third-party" refers to services running externally to Choreo, independently added to the Marketplace.

- **Network Visibility**: This filter enables you to categorize services based on their network visibility level, with three choices: "Public," "Organization," and "Project".  "Public" filters services exposed publicly, "Organization" represents services exposed across the entire organization, and "Project" represents services exposed at the project level.


## Explore a service 

You can click on the service card to open the detailed view of the service. The detailed service page features the service name, summary, version, labels, and service icon as the header.

Choreo organizes the service content into four tabs. The four tabs contain information as follows: 

- **Overview**: Choreo displays the service overview provided by the service developer. If the service developer has not provided any content at service creation, this section will be disabled. The service developer can provide the overview content via the Manage → Marketplace section of the component.

- **API definition**: Includes the API definition for the service, extracted from the `component.yaml` file in the user repository. If an API definition is not provided, this tab will be empty.

    !!! note
        If you are are currently using the `component-config.yaml` or `endpoints.yaml` configuration files, see the respective [migration guide](../develop-components/manage-component-source-configurations.md#migration-guide) for instructions on migrating to the recommended `component.yaml` configuration file.

- **How to use**: Includes instructions on how to use the selected service. This includes instructions on [creating a connection](../develop-components/sharing-and-reusing/create-a-connection.md).

- **Related documents**: Includes any additional content the user has provided as documents through the Manage -> Marketplace section of the component.

## Add a service to the Choreo Marketplace

You can add services to the Marketplace as Choreo services as follows: 

### Add a Choreo service

In Choreo, a service exposed through the platform is termed a Choreo service, with each service being identifiable by an endpoint within a Choreo service component. The Marketplace showcases a service for each endpoint within a service component.

Upon deployment to the initial environment, services get automatically added to the Marketplace. Choreo effortlessly collects essential details such as component name, endpoint name, description, and service definitions during this deployment, utilizing them to generate the corresponding service entries in the Marketplace.

The service name follows the convention of `component name - endpoint name`, while all other details remain unchanged.

## Service versioning in the Choreo Marketplace

In the Choreo Marketplace, service versions are displayed in their major version format. Each service in the Choreo Marketplace represents the latest version of the service within its major version, following semantic versioning principles.

For example, if a Choreo service has versions `v1.0`, `v1.1`, `v1.2`, and `v2.0`, the Choreo Marketplace displays services with versions `v1` and `v2` representing the latest versions `v1.2` and `v2.0` respectively.

When you deploy a new minor version of a service already deployed in Choreo, the corresponding service in the marketplace automatically updates to reflect the latest version within the same major version.

### Semantic-version-based intelligent routing in the Choreo Marketplace

When you use a service from the Choreo marketplace as a dependency, the dependent service's traffic automatically routes to the latest version of the corresponding service within the same major version. This ensures that your dependencies remain up-to-date without requiring manual updates within a major version.

For example, if you create a connection to connect your Choreo component named `Foo` to a Choreo service named `Bar`, which is currently available in the Choreo Marketplace as version v1, and if the latest version of the service `Bar` within the v1 range is v1.2, the component `Foo` will automatically connect to `Bar` v1.2.  Subsequently, when `Bar` releases version v1.3, traffic from `Foo` will automatically route to `Bar` v1.3.

## Edit services in the Choreo Marketplace

You can edit services in the Choreo Marketplace. During redeployment to any environment, Choreo automatically updates service definitions, visibility, and descriptions.


# CI/CD

Choreo provides a streamlined continuous integration and continuous deployment (CI/CD) experience to deploy applications and services efficiently across multiple environments.

Choreo creates environments for each project, where all components within the project share the environments. An environment is an isolated deployment area with restricted network and resource access. Services deployed in one environment cannot communicate with services deployed in another.

The Choreo cloud data plane provides two default environments (i.e., development and production). However, if you are in a private data plane organization, you can customize and create multiple environments based on your requirements.

Choreo adopts a *build once, deploy many* strategy to manage components across multiple environments. An application is built only once (i.e., per commit if automatic build on commit is enabled or based on the selected commit during a manual build). Then it is promoted to subsequent environments. This allows testing changes in lower, non-production environments like development before promoting the build to production.

Choreo injects configurations and secrets that you maintain at the environment level into components at runtime. This ensures a strict separation of environment-specific configurations from source code. Although configurations can vary across environments, the code and the built container remain unchanged. Configurations and secrets include:

- Resource credentials to a database, cache, or other backing services.
- Credentials to external cloud services such as Amazon S3 or external APIs.

All configurations and secrets are encrypted at rest and in transit and stored in a secure vault. In a private data plane organization, you can store configurations and secrets in your infrastructure.

## Build

Choreo auto-generates build pipelines that may slightly differ depending on the component type you create. Generally, all build pipelines work as follows:

- Builds a container image either from the provided source code or from a given Dockerfile for a specific commit.
- Runs security and vulnerability scans if applicable, depending on the component type.
- Pushes the container image to a container registry. In the cloud data plane, Choreo pushes the image to a Choreo-managed registry. If it is a private data plane organization, Choreo pushes the image to a registry that you own.
- Updates service endpoints and API specifications from the provided repository if applicable.

In addition to these steps, some buildpacks support integrating unit tests into the build pipeline. For more details, see [Integrate Unit Tests into the Build Pipeline](../develop-components/integrate-unit-tests-into-the-build-pipeline.md).

### Repeatable builds

Choreo can replicate builds from an identical code version (Git commit). This means that multiple builds initiated from the same Git commit will generate Docker images with the same behavior.

!!! note
    In the event of multiple builds from the same code version, Choreo preserves only the most recent version of the Docker image created from the particular code version.

### Trigger a build

On the **Build** page, click **Build Latest**. If necessary, you have the option to select a particular commit and build an image.

!!! note
    Admin and Choreo DevOps users can trigger builds using specific tags from the connected Git repository. However, this action bypasses the standard branch-based deployment process and should only be used for critical, time-sensitive scenarios, as it can disrupt deployment track integrity.

If you want to automatically trigger a build with each commit, you can enable **Auto Build on Commit**.

### Build logs

You can view build logs for specific builds on the **Build** page.

To view details of a specific build, click **View Details** corresponding to the build.

## Deployment

Once you build an image in Choreo, you can deploy it via the **Deploy** page. To deploy an image, you can follow one of the approaches given below:

- **Manually deploy**: In the **Deploy** page, go to the **Set Up** card and click **Deploy**.
- **Automatically deploy on build**: In the **Deploy** page, go to the **Set Up** card and enable **Auto Deploy on Build**. This automatically initiates deployment upon the completion of an automatic build.

!!! info
    To enable **Auto Deploy on Build**, you must enable **Auto Build on Commit**. This is because automatic deployment is not necessary or useful in scenarios where automatic build is not enabled.

!!! note
    - You must trigger the first build in a Ballerina component manually to ensure that Choreo applies the required configurations to the development environment. You can enable automatic builds subsequently.
    - Choreo automatically checks the configurable defined in your source code against the configurable values applied in an environment. Choreo requests the configurable values on deployment and promotion. If you have changed the configurables in your Ballerina component, auto-build pipelines can fail as a precaution to avoid a component crash at runtime due to missing configurables.
    - The configurable verifying capability is only available for Ballerina components. For Dockerfile-based components, ensure to manage and update the configurations and secrets in environments ahead of time. You must also ensure backward compatibility between at least one release if you change the configurations.

### Set up area and initial deployment

In the deploy phase, Choreo uses a setup area to merge the Docker image with its environment-independent configurations. Choreo then deploys this composite to the environment. This is known as the initial deployment.

### Immutable deployments

Once Choreo deploys a component with configurations, the configurations become immutable. Any subsequent change results in a new deployment.

### Promote a component to a higher environment

Choreo builds a container once per GitHub commit and then promotes it to subsequent higher environments.

You can go to the **Deploy** page of a component and promote it manually across environments.

## Configurations

Choreo allows you to define both environment-independent configurations and environment-specific configurations.

### Environment-independent configurations

These configurations apply to all environments.

To change environment-independent configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the **Set Up** card, and then trigger a new deployment to the initial environment. From there, you can proceed to promote the component to higher environments.

### Environment-specific configurations

These configurations apply to a particular environment.

To change environment-specific configurations, go to the **Deploy** page of the component, make the necessary configuration changes via the specific environment card, and trigger a new deployment.

To learn more about managing these configurations, see [Configuration Management](https://wso2.com/choreo/docs/choreo-concepts/configuration-management/).

## Task execution

The information on the **Execute** page is only applicable to scheduled and manual task components.

To track and monitor executions associated with a deployed scheduled task or manual task, go to the left navigation menu and click **Execute**.

You can view current and historic execution details along with a quick snapshot of recent activity via the total count of executions within the last 30 days. For each execution, you can view vital details such as the unique execution ID, the time it was triggered, and relevant revision information. Furthermore, you can dive deeper into the details by clicking on a specific execution to access its associated logs. This information enhances transparency, troubleshooting capabilities, and overall execution management, allowing you to easily monitor and analyze workflows.

## Zero-downtime deployments

Choreo performs rolling updates to ensure zero downtime between deployments and promotions.

A new build undergoes a health check before traffic is switched to it from the current build.

If you configure the necessary health checks for a component, it can prevent deploying and promoting unhealthy versions of a component.


﻿# Component

A component within a project represents a single unit of work in a cloud native application. A component is usually a single microservice, API, or job/task. Each component in Choreo is attached to a given directory path in a Git repository which either contains program source code or a Dockerfile with build instructions. A component is Choreo’s unit of deployment. Each component maps to a single pod in the Kubernetes cluster (data plane) at deployment time. Therefore, you can deploy, manage, and scale each component in Choreo independently.

Choreo supports different component types for various use cases. These include component types such as services, API proxies, integrations, web applications, and so on. Each component type hosts unique features based on its characteristics. For example, a scheduled integration component can accept a cron expression as a configuration to schedule an integration job/task.



# Connections

Services can exist in two main forms: standalone and integrated. Connecting services is an integral part in creating integrated solutions. Choreo allows you to connect services using Connections. 

Using Connections, you can integrate the service you intend to deploy on Choreo with other services on Choreo or external resources. Upon creating a connection to a service on Choreo, Choreo provides you a Connection ID along with a set of connection parameters. Thereafter, you have the capability to configure your service to establish a connection using this Connection ID and map connection parameters to environment variable names in your Choreo component. You can read these environment variable names in your service implementation to retrieve the values, to create a programmatic connection to the service you want to consume. 

At runtime, Choreo dynamically injects values into the environment variables based on the configured mapping. This approach ensures that the connection parameter values and the service connection creation remain loosely coupled, providing developers with flexibility and ease of maintenance.

You can add Connections in different visibility levels: Project and Component. The visibility levels are described below:

## Project Connections

Project Connections are Connections you create to connect to services within a particular project. The Connections **can be used by any component within the project**. 

For example, if you want to share a third-party service like Twilio across the project for all the components within that project to reuse, you can create a project connection. Components can refer to Project Connections using the connection ID. 
Project connections created to consume Choreo services under the OAuth security scheme will share the same OAuth application across the project. Any component reusing such a connection will use the same client ID and client secret.

## Component Connections

Component Connections are Connections you define at the component level and **used by only that component**. 

For example, create a component connection if you want to connect a legacy service to a given component. Components can refer to the Component Connection using the connection ID. 
If your component consumes more than one Choreo service, the Component connections created to consume those Choreo services under the OAuth security scheme can share the same OAuth application by sharing the same client ID and secret between all such connections.

Learn how you can [share and reuse services using connections](../develop-components/sharing-and-reusing/create-a-connection.md) in Choreo.


# Data Planes

Choreo's architecture comprises two key components: the control plane and the data plane. The control plane handles essential tasks such as administering organizations, users, and projects. In addition, it also governs the entire journey of application development, from the initial stages of creation, progressing  to deployment, including measures to enforce governance and the provision for observability. The Choreo control plane is a SaaS that manages all cloud data planes and private data planes. It caters to diverse user personas, including CIOs, architects, and developers, as well as DevOps, site reliability engineers, and platform engineers.

The data plane is the environment where user applications are deployed based on configurations set in the control plane. These applications can range from services and web applications to APIs, integrations, and scheduled tasks. The applications can be written in various programming languages, allowing for a polyglot approach. Importantly, all traffic related to the runtime of user applications is restricted to the Choreo data plane, ensuring strict containment of user data within its boundaries.

Choreo's architecture features two distinct data plane types: cloud data planes and private data planes. A cloud data plane utilizes a multi-tenanted infrastructure model for deploying user applications, creating a shared yet secure environment for application runtime. In contrast, a private data plane(PDP) provides dedicated infrastructure for a single organization to run its user applications. This ensures an added layer of privacy and control for organizations with specific requirements.

![Choreo high-level view](../assets/img/choreo-concepts/high-level-view.png)

## Private data planes

### Infrastructure

Choreo private data planes can be deployed with almost all major cloud providers, such as Azure, AWS, and GCP, and are also compatible with on-premises infrastructure.

The essential requirements for a private data plane include upstream-compatible Kubernetes clusters, a container registry, a key vault (secret store), and a logging service or log storage.

![Private data plane architecture](../assets/img/choreo-concepts/private-data-plane-architecture.png)

### System components

Setting up the Choreo PDP system involves using a Helm installation on the Kubernetes infrastructure. 
The following software components are installed during the helm execution:

  - Cilium CNI and service mesh.
  - Choreo API Gateways and related components.
  - Choreo PDP agent.
  - Observability and logging APIs, along with observability agents.
  - Flux controller.

All of these software components receive automatic updates, including security patches and bug fixes through the flux controller connected to the Choreo Update Management System. 

### Connectivity with the control plane

The private data plane requires communication with the Choreo control plane to manage various activities. All these communications are outbound from the private data plane, ensuring that there is no need to open any specific `IP:Port` from its perspective for these interactions. However, if an organization's network restricts all outbound traffic, it is necessary to permit outbound traffic to the public IP range of the Choreo control plane.

The following table outlines the inbound and outbound connections from a private data plane:

<table border=1>
<thead>
<tr>
<th align="left">Data plane component</th>
<th align="left">Endpoint</th>
<th align="left">Direction</th>
<th align="left">Protocol</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan=2>Choreo PDP agent</td>
<td>Choreo control plane (CP) (mizzen server)</td>
<td>Outbound</td>
<td>WSS</td>
</tr>
<tr>
<td>Kubernetes API server</td>
<td>Outbound (cluster internal)</td>
<td>HTTPS, WS</td>
</tr>
<tr>
<td rowspan=2>APIM/local adaptor</td>
<td>Global adaptor</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Azure Service Bus (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td >APIM/Enforcer</td>
<td>Event hub (CP)</td>
<td>Outbound</td>
<td>AMQP</td>
</tr>
<tr>
<td>Choreo secret resolver</td>
<td>Cloud secret store</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Container registry</td>
<td>Container registry (public)</td>
<td>Inbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Container registry</td>
<td>Outbound (VPC internal)</td>
<td>HTTPS</td>
</tr>
<tr>
<td rowspan=2>Certificate manager</td>
<td>Azure DNS service</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>LetsEncrypt</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux source controller</td>
<td>GitHub</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
<tr>
<td>Flux Helm controller</td>
<td>Choreo container registry</td>
<td>Outbound</td>
<td>HTTPS</td>
</tr>
</tbody>
</table> 

All communication between the control plane and the private data plane is secured using TLS.

### Observability architecture

The following diagram depicts the architecture overview of Choreo's in-data-plane log and observability in Azure PDP:

![Observability architecture](../assets/img/choreo-concepts/observability-architecture.png)

The private data plane observability architecture is centered around a strong commitment to data privacy and compliance. This is achieved through a strategic decision to retain logs and observability data within the data planes itself. Key aspects of this architecture include:

- **Data storage at source**: Logs and observability data are stored within the data plane itself, enhancing security, simplifying access, and ensuring compliance.
- **Direct browser-to-data-plane interaction**: The Choreo Console in the user's browser directly interacts with APIs in the data plane, reducing potential data routing complexities and ensuring a more secure, direct flow of information.
- **Reduced data exposure points**: Fetching data directly from the data plane's APIs minimizes the number of data transfer points, effectively decreasing the chances of data exposure or interception.
- **Compliance with regulatory standards**: The architecture supports data locality, aligning with global regulatory standards like GDPR and CCPA by keeping data in its original environment.
- **Improved performance and real-time insights**: Direct interaction between the browser and data plane results in faster data retrieval, providing users with immediate insights.
- **User transparency and control**: Users have a clear view of their data's location and access methods, alongside granular control over data access.

### Security

The Choreo private data plane ensures extensive, production-grade security, ranging from infrastructure and architecture to zero-trust network security. All incoming traffic is protected by a firewall and must undergo authentication and authorization via the API Gateway. It also provides end-to-end network traffic encryption using Cilium transparent encryption, ensuring efficient data path encryption.

For details on the private data plane security levels supported in Choreo pricing plans, see [Private Data Plane Security Levels](../references/private-data-plane-security-levels.md).

### Management models

Choreo supports the following management models for private data planes (PDPs), fostering collaboration between WSO2 and customers across diverse scenarios:

  - WSO2 fully managed (infrastructure and PDP in WSO2 subscription) model
  - WSO2 fully managed (infrastructure and PDP in customer subscription) model
  - Customer self-managed (WSO2 provides installation script and updates) model

To explore each management model in detail so that you can make informed decisions depending on the supported cloud-based operations and security, see [Private Data Plane Management Models](../references/private-data-plane-management-models.md).


# Deployment Tracks

Deployment Tracks in Choreo are structured pathways for simplified software component deployment. They act like advanced CI/CD pipelines, ensuring your components reach their destinations seamlessly, whether from source code or prebuilt images. They establish an organized and structured approach that minimizes the chances of errors and challenges that are typically associated with deployment workflows.

## The significance of Deployment Tracks

Deployment Tracks offer practical solutions to enhance the API consumer experience by addressing two critical challenges:

- **Streamlined deployment**: Deployment Tracks serve as well-designed routes for your software components, enhancing the organization and reliability of the deployment process, similar to a well-structured express route.

- **Efficient API versioning**: Especially beneficial for managed APIs, Deployment Tracks provide a straightforward method for creating API versions that seamlessly interact with previous iterations. This simplified version management benefits both API creators and consumers alike.

## Streamlined deployments

For streamlined deployments, Choreo dissects two integral approaches that leverage Deployment Tracks: the comprehensive CI/CD integration and the focused CD-Only strategy.

### CI/CD with Deployment Tracks

A deployment track is linked to a particular branch within a GitHub repository. This connection is useful for handling deployments to various environments. On Choreo's Deploy page, you can easily visualize the deployments to specific environments associated with your selected deployment track. Moreover, the deployment track has a functionality that initiates automatic deployments for the linked branch. When activated, merging a pull request (PR) triggers a deployment to the development environment.

![Deployment tracks - source repo](../assets/img/choreo-concepts/deployment-tracks-source-repo.png){.cInlineImage-half}

### CD-Only strategy with Deployment Tracks

If you're inclined to use your own Continuous Integration (CI) systems and want to harness the deployment track as a Continuous Deployment (CD) pipeline, you can seamlessly link deployment tracks to a container registry repository. This configuration empowers users to effortlessly deploy images sourced directly from the linked container registry repository.

![Deployment tracks - container registry](../assets/img/choreo-concepts/deployment-tracks-container-registry.png){.cInlineImage-half}


## Efficient API versioning

**This section applies to only service components**. When working with service components in Choreo, it is important to have an effective API versioning mechanism. Choreo follows a versioning mechanism based on Semantic Versioning (SemVer) but only includes the major version and minor version with the prefix `v`. 

For example, `v1.2`. 

You can follow the approach given below when you version APIs in Choreo:

  - Increment the major version when you make incompatible API changes.
  - Increment the minor version when you add functionality in a backward-compatible manner.

!!! info "What is Semantic Versioning?"
    Semantic Versioning (SemVer) is a specification that defines how to assign and increment version numbers for software products, including APIs. For more information, see [Semantic Versioning specification](https://semver.org/#semantic-versioning-specification-semver).

One of the primary concerns when dealing with SaaS APIs is to minimize disruption for API consumers while continuously developing and deploying updates.

In compliance with SemVer, changes that don't introduce breaking or additive modifications to the API are categorized as patch updates. Hover, from the perspective of API consumers, these changes should ideally not disrupt their API clients. Typically, API consumers are most concerned with major API version alterations, but there might be instances where minor version changes are communicated to them.

Therefore, in the context of deployment tracks, API developers only need to specify the major and minor versions being delivered from a particular deployment track. This information is treated as the API version attribute of a deployment track. If the publisher requires versioning for internal tracking purposes, this can be accomplished in Git through the use of Git tags, on GitHub with GitHub releases, and so forth.

![Deployment tracks - api versioning](../assets/img/choreo-concepts/deployment-tracks-api-versioning.md.png){.cInlineImage-half}


﻿# Endpoint

An Endpoint is a network-exposed function that resides within a component. In Choreo, service and integration components expose one or more endpoints. Each endpoint in a component can have a service contract (OpenAPI, GraphQL SDL) associated with it. This contract is used to expose the endpoint to consumers. In the absence of a contract, Choreo uses /* exposed on all HTTP verbs as the default contract to expose the service or the integration.

Each endpoint exposed in a component is considered a single API. Therefore, Choreo allows you to do API management per endpoint for a given component. For example, you can perform lifecycle management and configure security settings per endpoint in a given component.


See [Configure Endpoints](../develop-components/configure-endpoints.md) to learn how to configure endpoints when developing components in Choreo. 

# Environments

Choreo offers developers one or more environments to run their applications within a given data plane. By default, the Choreo cloud data plane provides two environments (i.e., development and production). Each project in Choreo is associated with one or more  environments available in the organization. For example, project A may choose to utilize dev, staging, and production environments, while project B may only use development and production environments.

You can promote components within a project across available environments. When you promote a component, its configuration values can be overridden with environment-specific values.

The following diagram illustrates how a component is promoted across environments.

![Choreo environments](../assets/img/choreo-concepts/choreo-environments.png){.cInlineImage-threeQuarter}


﻿# Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization.

## Switch organizations

If you are a member of more than one organization, you can switch from one organization to another when necessary. To do this, select the required organization from the **Organization** list in the Choreo Console header.

{% include "../administer/inviting-members.md" %}

## Manage user permission

Choreo manages user permissions with groups and roles.

### Groups

A group in Choreo is a collection of users, each with one or more roles assigned to them. Users within a group inherit the permissions associated with the roles assigned to that group. For instance, if a user is added to the `API Publisher` group, they will automatically receive the `API Publisher` role.

Choreo comes with predefined groups already configured with specific roles, as follows:

- **API Publisher**: A collection of users who have the API Publisher role.
- **API Subscriber**: A collection of users who have the API Subscriber role.
- **Admin** : A collection of users who have the Admin role.
- **Billing Admin** : A collection of users who have the Billing Admin role.
- **Choreo DevOps** : A collection of users who have the Choreo DevOps role.
- **Developer** : Users who develop, deploy, and manage cloud native applications at scale.
- **External API Subscriber**: A collection of users who have the External API Subscriber role.

When creating a new group to invite members, be sure to assign a role to the group to ensure users have the required permissions.

### Roles

Choreo roles are defined as follows:

- **API Publisher**: An API publisher can discover, create, publish, delete, test, and manage an API.
- **API Subscriber**: An API subscriber is a developer in a particular organization. An API subscriber can subscribe to an application, manage subscriptions, manage applications, generate API keys, and manage API keys.
- **Admin**: An administrator is responsible for all administration tasks, including user management, customizing the Developer Portal, managing projects, enabling analytics, managing domains, etc.
- **Billing Admin**: Is responsible for billing administration that includes viewing tiers, creating and viewing organizations, managing invoices, viewing and creating subscriptions, and viewing and creating payment methods.
- **Choreo DevOps**: A Choreo DevOps user is a user with access to the Choreo DevOps portal, enabling them to actively manage, ensure dependable deployment, and monitor components.
- **Developer** : A user who can develop, deploy, and manage cloud native applications at scale.  
- **External API subscriber**: External API subscribers are API consumers who have access only to the API Developer Portal. They can join an organization with the sole purpose of consuming APIs.
- **Environment Manager (Deprecated)**: Manages deployment environments.

## Organization ID

The Organization ID serves as a unique identifier for each organization. To get the organization ID, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. In the header, click the **Organization** list. This will open the organization level settings page. 
5. Under **Organization** click **Copy ID**.

## Organization Handle

The organization handle is a unique string that directly corresponds to your organization's name. To get the organization handle, follow the steps below:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the project home page.
2. Click on the **Organization** list on the header and select your organization.
3. In the left navigation, click **Settings**.
4. Under **Organization** click **Copy Handle**.


﻿# Project

A project in Choreo is a logical group of related components that typically represent a single cloud native application. A project consists of one or more components. All components within a project can ideally be (but is not restricted to) in a single GitHub repository under different paths. This is also known as the monorepo architecture.

At deployment time, all components within a given project are deployed into a single namespace of the Kubernetes cluster. Components within a project can be exposed to the public internet, internally to the rest of the organization, or privately within the project only. A project in Choreo is represented as a cell with regard to the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md). The following diagram illustrates a project and how the components within a project are laid out at runtime:

![Project](../assets/img/choreo-concepts/project.png){.cInlineImage-full}








# Resource Hierarchy


The following diagram depicts the high-level resources and their relationships in Choreo.

![Resource hierarchy](../assets/img/choreo-concepts/resource-hierarchy.png){.cInlineImage-full}

## Organizations and data planes

Data planes are connected to the organization and are available for all projects within the organization. When you create an environment in a project, the data plane connected to the organization is linked with an automatically generated Kubernetes namespace.

## Environments and data planes

Choreo allows multiple Kubernetes clusters to be associated with an environment. This enables you to build highly resilient and resource-efficient solutions that utilize multiple clusters. Choreo synchronizes your applications and workloads between associated clusters in an environment, allowing you to perform multi-cluster deployment with a single click.

The following diagram illustrates how multiple clusters associate with different environments:

![Environments and dataplanes](../assets/img/choreo-concepts/environments-and-dataplanes.png){.cInlineImage-full}

!!! info "Note"
    It is not necessary to use a different cluster per environment. You can create multiple environments on the same cluster. The above diagram is an example of a specific solution. Your application architecture may require a different configuration than what is depicted.

## Components and environments

Components belong to a project in Choreo, and environments are provisioned per project. When a component is deployed, it is deployed as a container to the specified environment. Once deployed, you can promote the container image across the environments available in the project.

