## Configure a Custom Domain for Your Organization

Choreo enables you to configure custom domains for your organization, enhancing branding and discoverability. This allows developers to use custom URLs for components like API proxies, services, web applications, and webhooks. The configuration model involves administrators adding custom domains, developers requesting to use them, and administrators approving these requests.

## Choreo custom domain configuration model

Organization administrators can add custom domains, and component developers can request to use these domains for their components. Administrator approval is required for these requests, after which the custom domain becomes available for the component.

## Configure a custom domain for an organization

### Prerequisites

1.  Sign in to the Choreo Console.
2.  Create an organization in Choreo.

### Add a custom domain

To add a custom domain:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **URL Settings** > **Active Domains** and click **+ Add Domains**.
3.  Enter the domain name, select the environment and entity type.
4.  Create a DNS record with your DNS provider, associating the domain name to the generated CNAME target value.
5.  Click **Verify** after creating the CNAME record.
6.  Click **Next** on successful verification.
7.  Select a TLS certificate provider (either import your own or use Let's Encrypt).
8.  Click **Add** to save the custom domain.

The added domain will be listed under the **Active Domains** tab and will be available for the specified entity types in the selected environment. Customizations for the Developer Portal will be applied immediately.

## Configure a custom URL for a component

Developers can request available custom domains to configure custom URLs for components in specific environments.

### Request a custom URL for a component

To request a custom URL:

1.  Sign in to the Choreo Console.
2.  Select the component from the **Component Listing**.
3.  Go to **Settings** > **URL Settings**.
4.  Click the **Edit URL Mapping** icon for the desired environment.
5.  Select a domain in the **URL Settings** dialog and specify the context path for APIs.
6.  Click **Configure**.

The custom URL request will be in **Pending** status until approved.

### Approve a custom URL request

To approve a custom URL mapping:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **URL Settings** > **Pending URL Requests**.
3.  Click the **Approve URL Mapping** icon for the custom URL you want to approve.
4.  Review the details and click **Approve**.

Upon approval, the component's invoke URL will be replaced with the configured custom URL.

# Configure a User Store with the Built-In Identity Provider

Choreo's built-in identity provider (IdP) allows developers to experiment with user authentication and authorization by setting up test users and groups within Choreo. This is not recommended for production use.

## Prerequisites

Administrator rights to your Choreo organization.

## Configure a Choreo built-in IdP user store

To configure a Choreo built-in IdP user store:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Application Security** > **Identity Providers**.
3.  Click **Manage** in the **Choreo Built-in Identity Provider** pane.
4.  Click on a specific environment tab.
5.  Download the sample **User store template file(.csv )**.
6.  Specify user details in the template file and save it.
7.  Select the saved template file and click **Upload**.

# Configure Approvals for Choreo Workflows

Choreo allows configuring approval processes for environment promotion and API subscription workflows, ensuring controlled changes.

## Permissions to review and respond to approval requests

Required permissions for reviewing and responding to approval requests:

*   **Environment promotion**: `WORKFLOW-MANAGEMENT` (Approve component promotion requests), `PROJECT-MANAGEMENT`.
*   **API subscription**: `WORKFLOW-MANAGEMENT` (Approve API subscriptions), `PROJECT-MANAGEMENT`.

## Set up an approval process for a workflow

To set up an approval process:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Workflows**.
3.  Click the edit icon for the desired workflow.
4.  Select roles and assignees to review and respond to workflow approval requests.
5.  Click **Save**.

# Configure Enterprise Login

Choreo allows configuring enterprise login, enabling users from an external identity provider (IdP) to sign in seamlessly.

## Prerequisites

*   A valid email domain for your organization.
*   Access to the Choreo Console via Google, GitHub, or Microsoft account.

## Configure enterprise login for your Choreo organization

To configure enterprise login:

*   Contact Choreo support (`choreo-help@wso2.com`) with your organization name/handle and email domains.
*   Configure the DNS record for your email domain with the provided verification code.

## Bring your own identity to Choreo

Configure a federated enterprise IdP on Asgardeo in the organization provisioned for you.

## Configure role-based access control for enterprise login

To set up role-based access control:

1.  **Configure Asgardeo**:
    *   Configure your IdP as an external IdP in Asgardeo.
    *   Configure the application (**WSO2\_LOGIN\_FOR\_CHOREO\_CONSOLE**) with the IdP and user attributes.
2.  **Map Choreo groups to enterprise IdP groups**:
    *   In the Choreo Console, navigate to **Settings** > **Access Control** > **Groups** > **Manage IdP Group Mapping**.
    *   Map Choreo groups to the corresponding enterprise IdP groups.

# Configure Self-Sign-Up

Choreo enables setting up a self-sign-up page for your Developer Portal, allowing users to access and subscribe to APIs easily.

## Prerequisites

Sign in to the Choreo Console and create an organization.

## Configure Developer Portal self-sign-up

To configure self-sign-up:

1.  Contact Choreo support (`choreo-help@wso2.com`) to configure enterprise IdP for your Developer Portal.
2.  Sign in to Asgardeo using the same credentials as Choreo.
3.  Edit the **WSO2\_LOGIN\_FOR\_CHOREO\_DEV\_PORTAL** application and set the **Access URL** to your Developer Portal URL.
4.  Add user attributes (Email as mandatory, First Name and Last Name as optional).
5.  Configure basic authentication.
6.  Configure self-registration in Asgardeo.

## Manage new users

*   Enable auto-approval or manually approve/reject user accounts in the Choreo Console under **Settings** > **Self Signups**.

# Control Access in the Choreo Console

Choreo allows managing access to projects by restricting access to specific user groups using **Roles**, **Groups**, and **Mapping levels** (**Organization** and **Project**).

## Sample scenario

Grant development access to specific users within the Engineering Project:

1.  **Create a project**: Create a project named `Engineering Project`.
2.  **Create a new group**: Create a group named `Engineering Project Developer`.
3.  **Assign roles to the group**: Assign the **Developer** role to the `Engineering Project Developer` group within the `Engineering Project`.
4.  **Add users to the group**: Invite new users or add existing users to the `Engineering Project Developer` group.

# Control Egress Traffic for Your Organization

Choreo allows managing egress traffic via allow lists or deny lists.

## Configure an egress policy at the organization level

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Egress Control**.
3.  Click **+ Create** and select either **Allow All** or **Deny All**.
4.  Add the required rules for IP ranges or domains.

## Override the organization-level egress policy at the project level

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Egress Control**.
3.  Add or remove project-level rules to further restrict traffic.

# Create API Subscription Plans

API subscription plans control access to APIs by defining rules and limitations.

To create an organization-level subscription plan:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **API Management** > **Subscription Plans**.
3.  Click **+ Add Subscription Plan**.
4.  Enter the appropriate values for each field, including rate limits and burst control.
5.  Click **Create**.

# Customize the Developer Portal

Choreo allows customizing the look and feel of the Developer Portal.

To customize the Developer Portal theme:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **API Management** > **Devportal Theme**.
3.  Customize the **Home** page, color theme, font, header, footer, logos, etc.
4.  Click **Preview** to view changes.
5.  Click **Save** to save changes as a draft theme.
6.  Toggle the **Go Live** switch to apply the changes.

To reset the Developer Portal theme to the default theme, click **Reset to Default**.

# Manage Members of an Organization

Organization administrators can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Review Workflow Approval Requests

Authorized reviewers receive email notifications for workflow approval requests.

To view workflow approval requests:

1.  Sign in to the Choreo Console.
2.  Navigate to **Approvals**.
3.  Click **Review** for a specific request.

To approve or reject a request:

1.  Review the request details.
2.  Click **Approve** or **Reject**.

# Configure Asgardeo as an External Identity Provider (IdP)

To add Asgardeo as an external IdP in Choreo:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Application Security** > **Identity Providers**.
3.  Click **+ Identity Provider** and select **Asgardeo**.
4.  Specify a name and description for the IdP.
5.  Paste the well-known URL from your Asgardeo instance.
6.  Click **Next** and then **Add**.

# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

To add Azure AD as an IdP in Choreo:

1.  Sign in to the Choreo Console.
2.  Navigate to **Settings** > **Application Security** > **Identity Providers**.
3.  Click **+ Identity Provider** and select **Microsoft Entra ID (Azure AD)**.
4.  Provide a name and description for the IdP.
5.  Obtain and provide the `Well-Known URL` of your Azure AD instance.
6.  Review the endpoints and click **Next**.

Okay, here is a summary of the provided content, keeping the headings and minimizing data loss:

# API Rate Limiting

API rate limiting controls the number of requests made to an API to prevent system overload and enhance performance. It ensures API availability, responsiveness, and protection from malicious attacks. You can enable rate limiting via Choreo. API-level rate limiting applies the same request count to all operations, while operation-level allows configuration of different rate limits for each operation. Response headers like `x-ratelimit-limit`, `x-ratelimit-reset`, `x-ratelimit-remaining`, and `x-ratelimit-enforced` are available when rate limiting is enabled.

## Enable rate limiting for an API

To enable rate limiting for an API: 1. Sign in to the Choreo Console. 2. Select the component. 3. Click **Deploy**. 4. Go to the relevant environment card and click the view icon (or settings icon for API Proxy components). 5. Click the settings icon in the **Endpoint Details** pane. 6. Expand the **Rate Limiting** section. 7. Select a **Rate Limiting Level** and click **Apply**.

## API-level rate limiting

API-level rate limiting applies the allocated request count for the specified time unit to all operations in the API.

## Operation-level rate limiting

Operation-level rate limiting allows you to configure different rate-limiting values for each operation. You can use this option to define specific rate-limiting values for critical API operations that require an extra layer of protection.

## Rate-limiting response headers

The following table lists the response headers available when you enable rate limiting for your APIs. You can implement necessary rate-limiting scenarios depending on the response header values.

| **Header Name**  | **Description** |
|------------------|-----------------|
| `x-ratelimit-limit`     | Denotes the request count allocated for the specified time unit.       |
| `x-ratelimit-reset`     | Provides the time remaining to start the next rate-limiting time unit. |
| `x-ratelimit-remaining` | Denotes the remaining request count for the specified time unit.       |
| `x-ratelimit-enforced`  | Visible after exceeding the allocated request count.                   |

# Control API Visibility

APIs in Choreo are public by default, but developers can set visibility to `Private` or `Restricted` to control who can view and modify them.

-   **Public**: Visible to all in the developer portal.
-   **Private**: Visible only to users who sign in.
-   **Restricted**: Visible only to users with specified roles.

## Change API visibility

To change API visibility: 1. Sign in to the Choreo Console. 2. Select the REST API (Service) component. 3. Click **Manage** and then **API Info**. 4. Click the **Developer Portal** tab. 5. Select the desired visibility from the **Visibility** list. 6. Click **Save**. For Restricted visibility, select the visible roles or create new roles.

# Documents

Adding documentation to APIs improves visibility by providing details like descriptions, invocation instructions, limitations, and version history.

## Add documents to an API

To add documentation: 1. Sign in to the Choreo Console. 2. Select the component. 3. Click **Manage** and then **Documents**. 4. Specify a title and content in markdown syntax. 5. Click **Add**. Multiple documents can be added, edited, or deleted.

# Lifecycle Management

API lifecycle management involves distinct states from creation to retirement: `CREATED`, `PRE-RELEASED`, `PUBLISHED`, `BLOCKED`, `DEPRECATED`, and `RETIRED`. Leveraging these states optimizes development and ensures reliable API access.

## API lifecycle states

The following lifecycle states are applicable to APIs in Choreo:

| **API lifecycle state** | **Use case** | **Corresponding action** |
|-----------------------|------------|-----------|
| **CREATED** | The API is created but is not ready for consumption.| The API is not visible to subscribers in the Developer Portal.|
| **PRE-RELEASED** | A prototype is created for early promotion and consumer testing. You can deploy a new API or a new version of an existing API as a prototype to provide subscribers with an early implementation of the API.|The API is published to the Developer Portal as a pre-release.|
| **PUBLISHED** | The API is ready for subscribers to view and subscribe to via the Developer Portal| The API is visible in the Developer Portal and is available for subscription.|
| **BLOCKED** | Access to the API is temporarily blocked.| Runtime calls are blocked, and the API is not visible in the Developer Portal.|
| **DEPRECATED** | The old version of an API is moved to this state when a newer version of the API is PUBLISHED.| The API is deployed and is available to existing subscribers. New subscriptions are disabled. Existing subscribers can continue to use it as usual until the API is retired.|
| **RETIRED** | The API is no longer in use when it is in this state.| The API is unpublished and deleted from the Developer Portal.|

## Manage the lifecycle of an API

To manage the lifecycle: 1. Sign in to the Choreo Console. 2. Select the component. 3. Click **Manage**, then **Lifecycle**. 4. Click on the desired lifecycle state above the transition diagram.

# Rename API Display Name

Choreo allows renaming the API display name for better user-friendliness. By default, the API name follows the format `<component name>-<endpoint name>`.

To rename the API display name: 1. Sign in to the Choreo Console. 2. Select the component. 3. Click **Manage** and then **API Info**. 4. Go to the **Developer Portal** tab. 5. Specify the new name in the **Name** field under **General Details**. 6. Click **Save**.

# OWASP Top 10

This section lists rules enforcing OWASP security guidelines to prevent common vulnerabilities. The rules cover areas such as:

*   Avoiding numeric IDs, HTTP Basic authentication, API keys/credentials in URLs, and insecure authentication schemes.
*   Implementing JWT best practices and using short-lived access tokens.
*   Defining rate limits and Retry-After headers to prevent API overloading.
*   Limiting array, string, and integer sizes to mitigate resource exhaustion.
*   Defining CORS origins and avoiding HTTP schemes for server interactions.
*   Explicitly defining the audience and environment for APIs.
*   Constraining additional/unevaluated properties in JSON schemas.
*   Defining schemas for error responses (429, 401, 500) and carefully restricting strings.
*   Avoiding `eval()` functions and `script` tags in markdown descriptions.

# WSO2 API Design Guidelines

This section details best practices for API design, including:

*   Using `kebab-case` for paths and `snake_case` for parameters.
*   Excluding file extensions and HTTP verbs from paths.
*   Using plural resource names.
*   Avoiding special characters in paths.
*   Ensuring servers have `/api`.

# WSO2 Style Guidelines

These guidelines enforce uniformity in API style, covering:

*   Validating `operationId` for URLs and ensuring path parameter declarations are not empty.
*   Avoiding trailing slashes in paths and using lowercase server URLs.
*   Using OpenAPI 2 host `schemes` to reflect the transfer protocol of the API.
*   Requiring a sibling `items` field for schemas with `type: array`.
*   Including a valid organization URL and email in the `contact` object.
*   Including a `contact` object, a `description` object, and a `license` object in the `info` object.
*   Including a valid URL in the `license` object.
*   Avoiding `eval()` functions and `script` tags in markdown descriptions.
*   Specifying global tags at the root OpenAPI Document level in alphabetical order.
*   Ensuring each operation has a description and an `operationId`.
*   Defining at least one tag for each operation.
*   Specifying a server at the root document level.
*   Ensuring server URLs do not direct to example.com.
*   Providing a description for all `parameter` objects.
*   Defining path parameters on the path level instead of the operation level.

# About API Policies

API policies are units of business logic to modify API invocation flows. They alter `Request`, `Response`, or `Error` flows. Choreo supports inbuilt mediation policies:

*   JSON to XML, XML to JSON
*   Remove/Add Query Parameter
*   Remove/Add/Set Header
*   Rewrite Resource Path
*   Log Message

These policies enable custom transformations without custom code.

# Apply Advanced Settings on Mediation Policies

Advanced settings are available for proxy components with attached mediation policies, including HTTP version, hostname verification, minimum evictable idle time, and detailed access log.

# Attach and Manage Policies

You can attach, rearrange, or swap policies via the Choreo Console. Attaching policies involves deployment initiation and API deployment. The API invocation is modified based on the attached policy. Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. You can also implement API policies as Ballerina projects.

# Assign Subscription Plans to APIs

API subscription plans control access to APIs. You can assign subscription plans to APIs to provide different levels of access based on user needs.

# Subscribe to an API with a Subscription Plan

API consumers can select subscription plans when subscribing to APIs.

I hope this is helpful!

Here's a summary of the provided content, maintaining the original headings for organization and minimizing data loss:

# Configure Mutual TLS Between Components

This section explains how to configure mutual TLS in Choreo to secure communication between components using digital certificates for authentication and encryption. It details the generation of root, client, and server certificates, explains how to read these certificates from components (via file system or environment variables), and provides a link to a sample implementation.  It also notes that TLS can be configured instead of mutual TLS by following the same steps *without* generating a client certificate.

# Pass End-User Attributes to Upstream Services

This section describes how to pass end-user attributes to backend services in Choreo using JWTs. It explains how the JWT is structured, the claims it contains (including examples and descriptions of mandatory/optional claims), and how to enable this feature in the Choreo console. It also covers JWKS support in Choreo for validating the JWT, providing endpoint URLs and a sample response.

# Secure API Access with Asgardeo

This section guides users on integrating Asgardeo with Choreo as an external Identity Provider (IdP) to secure API access. It outlines the steps for assigning scopes to APIs in Choreo, creating APIs and applications in Asgardeo, enabling external IdP authentication in Choreo, and invoking the API with scopes. Prerequisites include configuring Asgardeo as an external IdP, deploying an API in Choreo, and publishing the API.

# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

This section explains how to configure mutual TLS between the Choreo Gateway and a backend service. It details the process of configuring the backend certificate in Choreo, configuring mutual TLS with the backend service (either by generating a key pair through Choreo or using your own certificate pair), associating the certificate with the API, and deploying the API. It also explains how to change the certificate for the production environment.

# Secure Web Applications with Managed Authentication

This section describes how Choreo's managed authentication simplifies adding authentication and authorization to single-page web applications. It details the steps for implementing sign-in and sign-out functionality, obtaining user information claims via cookies or a GET endpoint, invoking APIs, handling session expiry, and setting up a custom error page. It also explains how to enable managed authentication for the component and configure the necessary paths in the Choreo console and how to configure the identity provider (Choreo built-in, Asgardeo or external).

# Test Secure API Access with Choreo Built-In Security Token Service

This section explains how to test secured APIs with permissions using Choreo's built-in authorization. It guides users through assigning scopes, creating roles, assigning permissions, and assigning roles to user groups. It also covers how to test API invocation with managed authentication enabled and disabled, including generating OAuth credentials and retrieving access tokens.

# Choreo Command-Line Interface (CLI) Overview

The Choreo CLI is a command-line tool designed to simplify interactions with Choreo, a comprehensive internal platform-as-a-service. It streamlines the development process, offering benefits such as simplified deployment processes and versatile workflow across frameworks. The CLI supports various component types including Services, Web Applications, Webhooks, Scheduled Tasks, and Manual Tasks.

## Key features of the Choreo CLI

-   **Create and Manage Resources**: Simplifies project and component management.
    -   **Create Builds and Deployments**: Streamlines building and deploying components, allowing for easy promotion to different environments.
-   **Monitor with Logs**: Provides integrated log functionality for effective component monitoring and insights into behavior and performance.

For troubleshooting and FAQs, refer to the Choreo CLI FAQ.

# Get Started with the Choreo CLI

This guide demonstrates how to use the Choreo CLI with a sample to-do app built with Next.js, covering the process of creating, building, deploying, and promoting a web application.

## Prerequisites

Installation involves running a command specific to your OS (Linux, macOS, or Windows) and verifying the installation with `choreo --version`.

## Steps

1.  **Login to Choreo**: Use `choreo login` and follow the console instructions.
2.  **Create a project**: Create a multi-repository project with `choreo create project web-app-project --type=multi-repository`.
3.  **Create a Web Application component**:
    *   Fork the sample to-do app repository.
    *   Create a component with `choreo create component my-web-app --project=web-app-project --type=webApp`.
    *   Provide repository details when prompted, including the repository URL, branch, directory, build-pack (nodejs), language version (20.x.x), and port (8080).
4.  **View component details**: Use `choreo describe component "my-web-app" --project="web-app-project"` to view component information.
5.  **Build the component**: Initiate the build with `choreo create build "my-web-app" --project="web-app-project"`.
    *   **View build status**: Check the status using `choreo describe build <build-id> --project="web-app-project" --component="my-web-app"`.
    *   **View build logs**: Access logs with `choreo logs --type=build --project="web-app-project" --component="my-web-app" --deployment-track="main" --build-id=<build_id>`.
6.  **Deploy to the Development environment**: Deploy with `choreo create deployment "my-web-app" --env=Development --project="web-app-project" --build-id=<build-id>`.
    *   **Verify the deployment**: Retrieve the URL with `choreo describe component "my-web-app" --project="web-app-project"`.
    *   **View runtime logs**: Observe logs with `choreo logs --type component-application --component my-web-app --project web-app-project --env Development --follow`.
7.  **Deploy to the Production environment**: Deploy with `choreo create deployment "my-web-app" --env=Production --project="web-app-project" --build-id=<build-id>`.
    *   **Verify the deployment**: Retrieve the URL with `choreo describe component "my-web-app" --project="web-app-project"`.

To see all available CLI functions, use `choreo --help`.

# Manage Authentication with Personal Access Tokens

Personal Access Tokens (PATs) offer a secure alternative to username/password authentication for the Choreo CLI, enabling granular access management.

## What are personal access tokens?

PATs are unique strings providing an alternative to username and password authentication.

## Sample use cases for personal access tokens

PATs are useful for automated scripting, granular permissions, temporary access, integration with third-party tools and multiple account management.

## Set up personal access tokens

1.  Sign in to the Choreo Console and navigate to Account Settings > Personal Access Tokens.
2.  Click "+ Create New", name the token, define scopes/permissions, and click "Generate".
3.  Copy and store the token securely.

## Use a personal access token with the Choreo CLI

To log in, use `choreo login --with-token` and provide the token via standard input, for example:

```bash
export CHOREO_TOKEN= <YOUR_PERSONAL_ACCESS_TOKEN>
echo "$CHOREO_TOKEN" | choreo login --with-token
```

## Manage and revoke tokens

Manage or revoke tokens via Account Settings > Personal Access Tokens in the Choreo Console.

## Best practices for token management

-   Limit scope
-   Rotate tokens regularly
-   Use secure storage
-   Revoke unused tokens

Okay, here's a summary of the provided content, maintaining the original headings for structure:

# Choreo Marketplace

The Choreo Marketplace facilitates service reuse and sharing within an organization. It allows users to browse, search, and access service definitions, documentation, and usage instructions for services deployed in Choreo. Services are discoverable through search (by name, label, or content) and filtering (by type and network visibility). Exploring a service reveals its overview, API definition, usage instructions, and related documents. Services are automatically added to the Marketplace upon deployment, and their names follow a `component name - endpoint name` convention. The Marketplace displays service versions in major version format and intelligently routes traffic to the latest version within the same major version. Service definitions, visibility, and descriptions are automatically updated during redeployment.

# CI/CD

Choreo provides a CI/CD experience for efficient deployment across multiple environments, where each project has isolated environments with restricted access. It uses a "build once, deploy many" strategy, injecting environment-specific configurations and secrets at runtime, ensuring separation from source code. Build pipelines are auto-generated, creating container images, running security scans, pushing images to a registry, and updating service endpoints. Builds are repeatable from the same code version. Users can manually trigger builds or enable automatic builds on commit.

Deployment can be manual or automatic upon build completion. Choreo uses a setup area to merge the Docker image with environment-independent configurations for the initial deployment. Deployments are immutable, and components can be promoted across environments. Choreo supports environment-independent and environment-specific configurations. Task executions for scheduled and manual tasks can be tracked and monitored. Choreo performs rolling updates for zero-downtime deployments, ensuring health checks before traffic is switched to a new build.

# Component

A component is a single unit of work (microservice, API, task) within a project in Choreo, linked to a directory in a Git repository. It's Choreo's unit of deployment, mapping to a single pod in Kubernetes. Choreo supports different component types, each with unique features.

# Connections

Choreo allows connecting services using Connections, enabling integration with other Choreo services or external resources. Connections provide a Connection ID and parameters, which can be mapped to environment variables. Choreo injects values into these variables at runtime, ensuring loose coupling. Connections can be Project-level (shared across the project) or Component-level (used only by that component).

# Data Planes

Choreo's architecture includes a control plane (SaaS for administration) and data planes (where applications are deployed). There are two types of data planes: cloud data planes (multi-tenant) and private data planes (dedicated infrastructure). Private data planes can be deployed on various cloud providers or on-premises and require Kubernetes, a container registry, a key vault, and a logging service. They communicate outbound with the control plane using TLS. The observability architecture of private data planes emphasizes data privacy by storing logs and data within the data plane. Choreo supports different management models for private data planes, including WSO2 fully managed and customer self-managed options.

# Deployment Tracks

Deployment Tracks in Choreo streamline software component deployments, acting as advanced CI/CD pipelines. They address the challenges of streamlined deployment and efficient API versioning. Deployment tracks are linked to a branch in a GitHub repository or a container registry. The API versioning mechanism in Choreo is based on Semantic Versioning (SemVer) and includes the major and minor versions with the prefix `v`.

# Endpoint

An Endpoint is a network-exposed function within a component (service or integration). Each endpoint can have a service contract (OpenAPI, GraphQL SDL) for exposing it to consumers. Choreo enables API management per endpoint.

# Environments

Choreo offers developers multiple environments (e.g., development, production) within a data plane. Each project is associated with one or more environments. Components can be promoted across environments, with environment-specific configuration values.

# Organization

An organization in Choreo is a logical grouping of users and resources. A first-time user must create an organization and be a member of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a member of that organization. A user cannot create more than one organization. Choreo manages user permissions with groups and roles.

# Project

A project in Choreo is a logical group of related components, representing a single cloud-native application. All components within a project are deployed into a single namespace of a Kubernetes cluster.

# Resource Hierarchy

Choreo's resources are structured in a hierarchy: Data planes connect to organizations and are available for all projects. Environments are provisioned per project, and components are deployed as containers to specified environments. Multiple Kubernetes clusters can be associated with an environment.

# Explore the Demo Organization

The Choreo demo organization offers a read-only view of a fully deployed system, showcasing how Choreo simplifies cloud-native application development, deployment, and management.

## Prerequisites

- New users need to create an organization by signing in to the Choreo Console, providing a unique organization name, and accepting the terms of use.

## Join the demo organization

1.  Sign in to the Choreo Console.
2.  Access the **Organization** list in the header.
3.  Click **Join** next to the **Demo Organization** under **Invited Organizations**.

## Demo organization overview

Joining the demo organization provides access to a read-only sample application for customer rewards management. You can explore:

-   **Projects and components**: Sample projects and their functions.
-   **Component details and architecture**: Configuration details like environment variables and API keys.
-   **Build and deployment pipelines**: Build configurations and deployment history.
-   **Delivery, usage, and observability metrics**: Analysis of metrics and insights.

The [Customer Reward Management System Sample](https://github.com/wso2/choreo-samples/tree/main/customer-reward-management#readme) on GitHub offers more details on architecture and source code.

# Quick Deploy a Sample

Choreo's **Quick Deploy** feature allows one-click deployment of samples for quick exploration and experimentation.

## Prerequisites

- New users need to create an organization and a project by signing in to the Choreo Console, providing a unique organization name, and accepting the terms of use.

## Try out quick deploy

1.  Sign in to the Choreo Console.
2.  Select your project from the **Project** list.
3.  In the project **Overview**, go to **Create from a Sample**.
4.  Click **View All Samples**.
5.  Hover over a sample and click **Quick Deploy**.

## Post-deployment actions

-   **Services**: Test using the **Test Console**.
-   **Web applications**: Open the provided URL.
-   **Manual/Scheduled tasks**: Execute from the **Execute** page. Scheduled tasks' cron schedule is on the **Overview** page.

# Samples Overview

Choreo provides a wide range of samples for exploring platform functionalities.

## Prerequisites

- New users need to create an organization and a project by signing in to the Choreo Console, providing a unique organization name, and accepting the terms of use.

## Explore the Choreo samples collection

1.  Sign in to the Choreo Console.
2.  Select your project from the **Project** list.
3.  In the project **Overview**, go to **Create from a Sample**.
4.  Click **View All Samples**.

Samples can be filtered by:

-   **Buildpack**: Technology used (e.g., Ballerina, NodeJS, Docker).
-   **Component Type**: (e.g., service, web application, tasks).
-   **Tags**: Functionalities or integrations (e.g., REST, HTTP, GraphQL).

Samples can be quick deployed or their source code can be accessed on GitHub.

Here is the summary of the given content:

# Consume an API Key Secured Service

To consume an API secured with an API Key, you need to create an application in the Choreo Developer Portal and generate an API Key.

### Steps to Create an API Key

1.  Navigate to the [Choreo Developer Portal](https://devportal.choreo.dev) and sign in.
2.  Click on **APIs** in the Developer Portal header.
3.  Select the desired API that requires an API Key for access.
4.  This will take you to the API overview page, where you can manage credentials.

You can generate API keys for production and sandbox environments. When generating the API Key, you need to provide a key name, select an application, and choose a subscription policy. Use the generated API Key in the `api-key` header to authenticate API requests.

# Consume a OAuth2 Secured Service

To consume an OAuth2 secured service, you need to create an application, subscribe to the API, and generate an access token.

## Generate an access token via curl

1.  In the [Choreo Developer Portal](https://devportal.choreo.dev) header, click **Applications**.
2.  On the **My Applications** page, click on the application for which you want to generate the token.
3.  In the left navigation menu, click the desired environment under **Credentials**. This opens the **Application Keys** pane for that environment.
4.  Copy the **Consumer key**, **Consumer secret**, and **Token endpoint** values.
5.  Use the following template and replace the placeholders with the values you copied:

    ```bash
    curl -k -X POST <token_endpoint> -d "grant_type=client_credentials" -H "Authorization: Basic <base64encode(consumer-key:consumer-secret)>"
    ```
6.  Run the curl command to generate an access token.

Alternatively, you can generate a test access token via the Developer Portal UI for testing purposes. Use the generated access token in the `Bearer` header when invoking the API.

## Additional Information

*   **API Discovery:** APIs in the Choreo Developer Portal can be searched by name and are categorized by major versions. Visibility settings (Public, Private, Restricted) control access.
*   **Application Creation:** An application in Choreo represents a physical application. Creating an application involves providing a name and description in the Developer Portal.
*   **Key Generation:** Choreo uses OAuth 2.0 for API access. After creating an application, generate environment-specific keys (consumer key and secret). Advanced configurations allow setting grant types, token expiry times, and security options like PKCE.
*   **Subscription Management:** Subscribing to an API covers all minor versions within its major version. Subscriptions ensure secure authentication using application keys.
*   **Access Token Generation:** Access tokens enhance security. Generate them via cURL or the Developer Portal UI.
*   **API Key Management:** API Keys can be regenerated (with a grace period) or deleted via the API's or Application's Credentials section in the Developer Portal.
*   **OAuth 2.0 Grant Types:** Choreo supports various OAuth 2.0 grant types, including Authorization Code, Refresh Token, Client Credentials, Implicit, and Password.
*   **Access Token Revocation:** Revoking JWT access tokens is challenging due to their self-validating nature. Short-lived tokens and regular refreshing are recommended.
*   **Application Sharing:** Choreo allows sharing applications with organization members in read-only mode via the Developer Portal.

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

Okay, here is a summary of the provided content, focusing on minimizing data loss and maintaining the original headings:

# Configure Container Resources, Commands, and Arguments

Choreo allows viewing and editing container configurations for components, including image tags, commit IDs, and resource limits. Each component is limited to a single main container. Resource limits prevent excessive resource consumption.

## Update container configurations

Container configurations can be updated via the Choreo Console by navigating to the **Containers** page under **DevOps** for a selected component.

### Update resource requests and limits

Available in paid plans, resource requests and limits can be adjusted using sliders.

### Set the image pull policy

Image pull policies include:
-   **Always**: Always pull the image.
-   **If Not Present**: Pull only if the image is not in the data plane (recommended).

### Specify container ports

Container Port and Service Port values can be specified, with the Service Port being the exposed port.

### Define a command and arguments for the container

Commands and arguments can override the container's ENTRYPOINT. They specify the ENTRYPOINT array and support variable expansion.

# Configure Storage

Choreo components have a default read-only file system. Volume mounts enable writable storage locations.

## Volume mount types

-   **Empty Directory (In-Memory)**: Fast, temporary, in-memory storage (tmpfs).  Erased on container restart or removal. Available on all data planes.
-   **Empty Directory (Disk)**: Temporary storage on disk. Destroyed on container restart or removal. Only available on private data planes.
-   **Persistent Volume**: Permanent storage. Persists across container restarts or removal. Only available on private data planes.

## Create a temporary storage space for your container

Temporary storage is created using Empty Directory mounts (in-memory or on-disk).

**Steps:** Sign in to Choreo Console -> Component Listing -> DevOps -> Storage -> Create -> Specify Volume Name and select Empty Directory (In-Memory) -> Next -> Specify Mount Path -> Create.

## Create a persistent storage space for your container

Persistent storage is created using Persistent Volume mounts. Available only in private data plane organizations.

**Steps:** Sign in to Choreo Console -> Component Listing -> DevOps -> Storage -> Create -> Specify Volume Name and select Persistent Volume -> Select Storage Class -> Set Storage Capacity -> Select Access Mode -> Next -> Specify Mount Path -> Create.

# Configure VPNs on the Choreo Cloud Data Plane

Choreo enables secure access to private networks using Tailscale, providing a prebuilt Tailscale image component as a forward proxy.

## Configure and use Tailscale to access private network endpoints

Details the steps to create, configure, deploy, and use the Tailscale proxy component in Choreo.

### Prerequisites

Details the prerequisites.

### Step 1: Create the Tailscale proxy

Details how to create a project and the tailscale proxy component.

### Step 2: Configure and deploy the Tailscale proxy

Details configuration and deployment.

### Step 3: Access private network endpoints with the Tailscale proxy

Details how to access private network endpoints with the Tailscale proxy.

## Post-deployment actions

Details the post-deployment actions.

### Handle node key expiry

Details how to handle node key expiry.

### Handle auth key expiry

Details how to handle auth key expiry.

### Update port mapping configurations

Details how to update port mapping configurations.

## Best practices

Details the best practices to follow.

### Configure health checks

Details how to configure health checks.

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA.

## Security best practices

Details the security best practices to follow.

## Troubleshoot issues

Details how to troubleshoot issues.

# Manage Configuration Groups

Choreo allows creating Configuration Groups to manage reusable configurations, comprised of key-value pairs for multiple environments.

## Create a configuration group

To create a new configuration group, follow the steps given in the main document.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given in the main document.

### Edit the configuration group

Details how to edit the configuration group.

## Delete a configuration group

To delete a configuration group, follow the steps given in the main document.

# Manage Configurations and Secrets

Choreo enables managing component configurations and secrets as file mounts or environment variables.

## The difference between configurations and secrets

-   **Secrets:** Write-only, content not retrievable.
-   **Configurations:** Readable and updatable.

## Apply a file mount to your container

Details how to apply a file mount to your container.

## Apply environment variables to your container

Details how to apply environment variables to your container.

## Update an existing configuration or secret

Details how to update existing configurations or secrets.

## Delete an existing configuration or secret

Details how to delete existing configurations or secrets.

## Manage Ballerina configurables

Ballerina configurables can be managed for Ballerina components.

# Manage Continuous Deployment Pipelines

Choreo provides a default CD pipeline, but allows creating custom pipelines to define environment deployment order.

## Create a new continuous deployment pipeline

Details how to create a new continuous deployment pipeline.

## Edit a continuous deployment pipeline

Details how to edit a continuous deployment pipeline.

## Delete a continuous deployment pipeline

Details how to delete a continuous deployment pipeline.

## Add a continuous deployment pipeline to a project

Details how to add a continuous deployment pipeline to a project.

## Remove a continuous deployment pipeline from a project

Details how to remove a continuous deployment pipeline from a project.

## Change default continuous deployment pipeline of a project

Details how to change default continuous deployment pipeline of a project.

# Manage Environments

Choreo provisions development and production environments by default.

## Create a new environment

Details how to create a new environment.

## Delete an environment

Details how to delete an environment.

# Set Up Health Checks

Health checks ensure container health and traffic readiness.

## Liveness probes

Liveness probes restart containers on failure.

## Readiness probes

Readiness probes stop traffic to containers on failure.

## Probe types

Probe types include HTTP GET requests, TCP connection probes, and command execution.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container.

### TCP connection probe

This probe attempts to open a socket to the container on the specified port.

### Execute a command

This probe executes a given script inside the container.

## Configure liveness and readiness probes

Details how to configure liveness and readiness probes on a container.

# View Runtime Details

Choreo allows viewing runtime details of running component replicas.

## Redeploy a release

Resources can be redeployed to a specific environment, triggering a rolling update.

## View running instances

Details each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.

### Observe real-time container logs

Details how to observe real-time container logs.

### View container conditions and events

Details how to view container conditions and events.

# Autoscale Component Replicas

Choreo allows autoscaling component replicas based on resource consumption.

# Autoscale Components with Scale-to-Zero

Choreo offers scale-to-zero for HTTP applications.

## How Scale to Zero works in Choreo

Details how Scale to Zero works in Choreo.

## Enable scale to zero

Details how to enable scale to zero.

## Limitations

Details the limitations of the scale to zero.

## Architecture 

Details the architecture of the scale to zero.

## Troubleshooting

Details how to troubleshoot the scale to zero.

# Manage Configuration Groups

Choreo allows creating Configuration Groups to manage reusable configurations, comprised of key-value pairs for multiple environments.

## Create a configuration group

To create a new configuration group, follow the steps given in the main document.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given in the main document.

### Edit the configuration group

Details how to edit the configuration group.

## Delete a configuration group

To delete a configuration group, follow the steps given in the main document.

# Manage Configurations and Secrets

Choreo enables managing component configurations and secrets as file mounts or environment variables.

## The difference between configurations and secrets

-   **Secrets:** Write-only, content not retrievable.
-   **Configurations:** Readable and updatable.

## Apply a file mount to your container

Details how to apply a file mount to your container.

## Apply environment variables to your container

Details how to apply environment variables to your container.

## Update an existing configuration or secret

Details how to update existing configurations or secrets.

## Delete an existing configuration or secret

Details how to delete existing configurations or secrets.

## Manage Ballerina configurables

Ballerina configurables can be managed for Ballerina components.

# Manage Continuous Deployment Pipelines

Choreo provides a default CD pipeline, but allows creating custom pipelines to define environment deployment order.

## Create a new continuous deployment pipeline

Details how to create a new continuous deployment pipeline.

## Edit a continuous deployment pipeline

Details how to edit a continuous deployment pipeline.

## Delete a continuous deployment pipeline

Details how to delete a continuous deployment pipeline.

## Add a continuous deployment pipeline to a project

Details how to add a continuous deployment pipeline to a project.

## Remove a continuous deployment pipeline from a project

Details how to remove a continuous deployment pipeline from a project.

## Change default continuous deployment pipeline of a project

Details how to change default continuous deployment pipeline of a project.

# Manage Environments

Choreo provisions development and production environments by default.

## Create a new environment

Details how to create a new environment.

## Delete an environment

Details how to delete an environment.

# Set Up Health Checks

Health checks ensure container health and traffic readiness.

## Liveness probes

Liveness probes restart containers on failure.

## Readiness probes

Readiness probes stop traffic to containers on failure.

## Probe types

Probe types include HTTP GET requests, TCP connection probes, and command execution.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container.

### TCP connection probe

This probe attempts to open a socket to the container on the specified port.

### Execute a command

This probe executes a given script inside the container.

## Configure liveness and readiness probes

Details how to configure liveness and readiness probes on a container.

# View Runtime Details

Choreo allows viewing runtime details of running component replicas.

## Redeploy a release

Resources can be redeployed to a specific environment, triggering a rolling update.

## View running instances

Details each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.

### Observe real-time container logs

Details how to observe real-time container logs.

### View container conditions and events

Details how to view container conditions and events.

# Autoscale Component Replicas

Choreo allows autoscaling component replicas based on resource consumption.

# Autoscale Components with Scale-to-Zero

Choreo offers scale-to-zero for HTTP applications.

## How Scale to Zero works in Choreo

Details how Scale to Zero works in Choreo.

## Enable scale to zero

Details how to enable scale to zero.

## Limitations

Details the limitations of the scale to zero.

## Architecture 

Details the architecture of the scale to zero.

## Troubleshooting

Details how to troubleshoot the scale to zero.

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

Okay, here's a summary of the provided content, maintaining the original headings and minimizing data loss:

# Alert Overview

This section describes how to configure alerts for Choreo components to proactively monitor the ecosystem and take corrective actions. Alert setup is available only at the component level.

## Alert Types

Choreo supports the following alert types:

-   Latency alerts
-   Traffic alerts
-   Resource alerts
-   Log alerts
-   Build failure alerts
-   Status code alerts

### Latency Alerts

Notifies when a component's response latency exceeds a threshold. Configurable parameters include Metric (99th, 95th, 90th, or 50th percentile), Threshold (milliseconds), and Period (duration).

### Traffic Alerts

Notifies when a component's request count exceeds a threshold. Configurable parameters include Threshold (requests per minute) and Period (monitoring window).

### Resource Alerts

Notifies when a component's CPU or memory usage exceeds thresholds. Configurable parameters include Metric (CPU or Memory), Threshold (mCPU or MiB), and Period.  CPU is measured in mCPU (milliCPU) and Memory in MiB (Mebibyte).

### Log Alerts

Triggers when a specific phrase appears a certain number of times in component logs within a time window. Configurable parameters include Search Phrase, Count, and Interval.

### Build Failure Alerts

Informs you if a build failure occurs for your component.

### Status Code Alerts

Triggers when a component returns specific HTTP errors. Configurable parameters include Status Code, Count, and Interval. Supported only for API proxy component types.

## Configure Alert

Steps to configure an alert: navigate to the component, click **Observability** and then click **Alerts**, click **Create Alert Rule**, select the alert type, environment, and deployment track/version, configure the fields, specify email recipients, configure advanced parameters (if required), review the explanation, and click **Create**. You can edit, remove, and disable/enable alerts.

## Alert History & Notifications

### View Alert History

Check past triggered alerts in the **Alerts History** pane, filterable by Alert Type, Environment, Deployment Track/Version, and Time Range. API Proxy components show a Version filter and other components display a Deployment Track filter.

### Email Notifications

Alert recipients receive an email with alert details and a link to the Choreo console.

# Generate Custom Reports

Choreo Insights allows generating custom reports with metrics and group-by fields for analysis, supporting overtime charts, pie charts, and tables.

## Metrics

Available metrics include: Successful Hit Count, Response Cache Hits, Request Mediation Latency, Response Mediation Latency, Backend Latency, Total Latency, API Errors, and Target Errors.

## Group-by

Available group-by fields include: API Name, API Version, API Resource Template, API Method, API Creator, Application, Application Owner, Destination, User Agent, and Platform.

Steps to generate a report: click **Custom Reports**, select metrics, select 1-3 group-by fields and their order, set values for each group-by field, and click **Generate**.

## Download Reports

Report data can be downloaded as PDF or CSV files.

# Insights Overview

Choreo provides insights into APIs, including traffic, error rates, and latency, to monitor and optimize API performance.

Key capabilities include: analyzing API traffic, tracking errors, monitoring latency, generating reports, configuring alerts, obtaining granular insights, and drilling down into data.

## View insights

Access usage insights via the Choreo Console under **Insights** > **Usage**.  Permission-based access and data exclusion apply at the organization level.

## Analyze statistics

The **Usage Insights** page offers several subpages:

### Overview

Provides a system status overview, including Total Traffic, Error Request Count, Average Error Rate, 95th Percentile Latency, and an API Request Summary timeline.

### Traffic

Displays information related to API traffic, including API usage, application usage, and resource usage.  Allows filtering by API and Application.

### Errors

Presents information on erroneous API calls, categorized by error type and status code. Allows filtering by API, Category, and Status Code.

### Latency

Shows latency information, including the top 10 slowest APIs and latencies by category (Backend, Request mediation, Response mediation).

### Cache

Displays statistics on response caching efficiency, including Cache Hit Percentage and Latency.

### Devices

Provides information on operating systems and user agents used to invoke APIs.

### Alerts

Shows business alerts issued by Choreo.

### Reports

Allows downloading monthly usage reports, with preconfigured and custom report options.

#### Download custom reports

Custom reports can be generated by selecting APIs, applications, and specifying a time interval.

#### Download pregenerated reports

Pregenerated monthly reports are available for the last three months.

### Geo Map

Presents a geographical representation of API usage by country.  Available for on-premises environments.

# Integrate Choreo with Moesif

This section guides you through integrating Choreo with Moesif, an API analytics and monetization service.

Steps include: generating an API key in Moesif (with separate instructions for new and existing users), configuring Choreo with the Moesif API key, and invoking an API to observe data on the Moesif dashboard.

# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.

# Deploy a Web Application that Consumes a Backend Service

This guide explains how to expose a service endpoint via Choreo, securely consume it from a web application, and use Choreo's managed authentication. The sample web application allows users to sign in, view, add to, and delete books from their reading lists, and sign out. The steps include deploying and testing a service, creating a web application, creating a connection to the service, enabling managed authentication, deploying the web application, and consuming the service. The prerequisite is forking the Choreo sample book list app repository and creating a Choreo organization.

# Prerequisites

A GitHub account is required to fork the Choreo sample book list app repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Connect your sample repository and configure the service

Connect Choreo to your GitHub account and select the forked repository. Configure the `Reading List Service` component by specifying the directory, component type (Service), and buildpack (NodeJS).

# Step 3: Build the service

Navigate to the `Reading List Service` component's overview page, and initiate a build. Monitor the build progress until it completes successfully.

# Step 4: Deploy the service

Deploy the service by configuring the environment and verifying that the network visibility is set to public.

# Step 5: Test the service

Test the service using the OpenAPI Console to ensure the endpoints are working as expected. You can test GET, POST and DELETE methods.

# Step 6: Consume the service

Create a web application component, connect it to the GitHub repository, select React as the buildpack, and configure the build command and path. Then, create a connection between the web application and the deployed service, build the web application component, and configure and deploy the web application, replacing the placeholder service URL in `config.js` with the actual URL. Enable managed authentication and create a test user.

# Step 7: Test the front-end application

Access the front-end application via its web URL, log in with the created credentials, and verify the reading list functionality, including adding and deleting items.

# Deploy Your First Service

This guide provides instructions on how to deploy a service using Choreo, an Internal Developer Platform (IDevP). It involves using a pre-built book list service, building and deploying it using the Node.js buildpack, and testing the service.

# Prerequisites

A GitHub account is required to fork the Choreo sample book list service repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Create a service component

Create a service component, connect it to the GitHub repository, and select NodeJS as the buildpack.

# Step 3: Build and deploy

Build the service component and then deploy it by configuring the environment and reviewing the endpoint details.

# Step 4: Test the service

Test the service using the OpenAPI Console to ensure the endpoints are working as expected.

# Deploy Your First Static Web Application

This guide details how to deploy a static web application using Choreo. The example application is a to-do list where users can add tasks.

# Prerequisites

A GitHub account is required to fork the choreo-sample-todo-list-app repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Create a web application component

Create a web application component, connect it to the GitHub repository, and select NodeJS as the buildpack.

# Step 3: Build your web application

Build the web application component.

# Step 4: Deploy and access your web application

Deploy the web application and verify that it is hosted successfully by accessing the Web App URL.

Here's a summary of the provided content, keeping the headings intact and minimizing data loss:

# Choreo Limitations

This section outlines the limitations of Choreo, specifically concerning API management and the Choreo Cloud Data Plane.

## API management limits

The following table summarizes API management limitations in Choreo:

| Resource                                  | Limit                                                                                               |
| :---------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| Maximum request payload                   | 50 MB                                                                                               |
| URL size                                  | 2 KB                                                                                                |
| Request header                            | Request Headers total: 40 KB, Max Single Request header: 10 KB                                     |
| Total request duration                    | Minimum: 10 seconds, Default: 1 minute, Maximum: 5 minutes                                         |
| Maximum connection duration (WebSocket APIs) | 15 minutes                                                                                        |
| Connection idle timeout (WebSocket APIs)  | 5 minutes                                                                                         |
| Size for API definition (OpenAPI document) | 10 Mb                                                                                               |
| Number of APIs for PDP                    | 1000 API deployments                                                                                |
| Number of APIs per organization (free tier) | 5 APIs for free users                                                                             |
| Number of Developer Portal applications per organization (free tier) | 10 applications for free users                                                                    |

## Choreo cloud data plane limits

The following table summarizes the cloud data plane limitations in Choreo:

| Resource                                                     | Limit                                                                                                                                                                                                                                                                                                                                                                             |
| :----------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Request size limit (including headers, cookies, and payloads) | 256 KB                                                                                                                                                                                                                                                                                                                                                                            |
| Response body size limit                                     | 20 MB                                                                                                                                                                                                                                                                                                                                                                             |
| Number of open ports permitted per web application           | 1 <br/> While it is possible to have multiple ports open for project-level communication within a data plane, incoming internet traffic can only be directed to a single port. This contrasts with Service-type components, which allow for multiple endpoints.                                                                                                            |

# Choreo Platform Service Billing and Upgrades

This section explains how Choreo bills for platform services like databases, caches, and Kafka, and how to upgrade service plans.

## Platform service billing information

*   **Hourly billing:**  You are billed based on the number of hours a resource is active.
*   **Fixed pricing:** Pricing is based on the selected service plan. Choreo does not charge extra for network bandwidth usage.

## Upgrade a service plan

To upgrade a service plan, contact Choreo support.

# Frequently Asked Questions

This section covers frequently asked questions about Choreo.

## General

*   **What is Choreo?** Choreo is an internal developer platform (IDP) for building, deploying, monitoring, and managing cloud-native applications, aiming to enhance developer productivity and innovation.
*   **What is an organization in Choreo?** A logical grouping of users and resources, representing a company, community, or single user. Users can belong to multiple organizations with different roles.
*   **What is a project in Choreo?** A logical grouping of related components providing runtime isolation through namespaces.
*   **What is a component in Choreo?** A workload designed to run on Choreo (integrations, APIs, microservices, jobs, web apps, triggers).
*   **Internal vs. External API:** External APIs are publicly accessible, while internal APIs are only accessible within the same organization.
*   **What is a connector?** Reusable Ballerina packages for connecting to external systems/APIs.
*   **What is a trigger?** Enables users to receive event payloads from external systems.
*   **What is a sample/template?** Prebuilt Ballerina programs for common integration use cases.
*   **What are the support options in Choreo?** Free, basic, and enterprise plans are available.
*   **Log monitoring:** Azure Monitor or similar services can be used with Choreo.
*   **Maximum request payload size:** 50 MB.
*   **Supported source control software:** GitHub, Bitbucket and GitLab.
*   **Undeployed builds retention:** Free tier retains 1 undeployed build, other tiers retain the latest 5.
*   **What is Ballerina?** An open-source programming language designed for the cloud.
*   **What is Asgardeo?** Asgardeo is Choreo’s default IDP.
*   **Region selector:** Available for paid subscriptions in Choreo cloud data plane.
*   **Multiple data planes:** Free-tier users can create components only in the default data plane. Paid subscriptions are required to create components in different data planes.

## Security and data protection

*   **Data management:** Choreo uses WSO2 containers and Kubernetes clusters for scalability, resilience, and security.
*   **WSO2 Subprocessor list:** A detailed list of all subprocessors used by WSO2.
*   **Cloud Security:** WSO2 employs various security controls and design patterns to protect against threats.
*   **Connecting to third-party applications:** Allow requests from Choreo data plane by adding specific data plane IP ranges to your allowlist.

## Data planes

*   **Choreo control plane:** Centralized management component for overseeing and coordinating workloads.
*   **Data plane:** Computing environment for running customer workloads (private or Choreo data plane).
*   **Choreo data plane regions:** US East 2 and North Europe.
*   **Private data plane regions:** Any region where Azure and AWS are available.
*   **Azure AKS requirements for PDP:** Minimum of two (2) workload nodes for high availability.
*   **Control plane and data plane HA:** Designed for high availability using Azure components with a 99.99% availability.

## Environments

*   **Environment creation:** Requires a paid subscription (PAYG or Enterprise).
*   **PAYG environments:** Up to 5 environments.
*   **Enterprise PDP environments:** Unlimited number of environments, but more environments may result in higher infrastructure costs.
*   **Data plane selector:** US & EU data planes are visible only with a paid subscription and projects in both data planes.
*   **Private data plane environments:** You will receive the requested number of environments when establishing your private data plane and can create additional environments as needed.

## Billing and support

*   **Billing questions:** Contact cloud-billing-support@wso2.com.
*   **Developer plan:** Free plan for PoCs with limited transactions, 5 components, and US$1,000/year CDP credits.
*   **Infrastructure cost calculation:** Depends on the workload type and complexity.
*   **Component limitations:** Developer plan allows up to a maximum of five free components and unlimited paid components. PAYG and Enterprise plan allows unlimited paid components.
*   **Bill details:** Components used, infrastructure consumed, support plans, and additional services. Contact choreo-support@wso2.com for clarification.
*   **Enterprise plan support:** Not automatically included, but can be purchased separately.
*   **Enterprise PDP costs:** Basic plan or Enterprise support plan.
*   **PAYG to Enterprise upgrade:** No outage.

## Choreo CLI

*   **Uninstall CLI:** Delete the `.choreo` directory in the home directory of your OS.
*   **Update CLI:** Run the provided curl command.
*   **Supported component types:** Service, Web Application, Webhook, Scheduled Task, Manual Task.
*   **Get command help:** `choreo <command> --help`
*   **Build configurations:** Provided table outlines required build configurations for each component type and buildpack.

## Private Data Plane Management Models

This section outlines the roles and responsibilities for managing Private Data Planes (PDPs) under different models:

*   **WSO2 Fully Managed (Infrastructure and PDP in WSO2 Subscription):** WSO2 is responsible for most tasks including subscription prerequisites, remote access, network and firewall management, infrastructure provisioning, Kubernetes cluster management, choreo system components deployment, monitoring, and security monitoring. The customer is responsible for Choreo application creation/deployment, management, monitoring, and logs.
*   **WSO2 Fully Managed (Infrastructure and PDP in Customer Subscription):**  The customer is responsible for subscription prerequisites and providing remote access. Other responsibilities are shared between WSO2 and the customer.
*   **Customer Self-Managed (WSO2 Provides Installation Script and Updates):** The customer handles most tasks.

## Private Data Plane Security Levels

This section outlines the security features available at different tiers for private data planes:

*   **Basic Tier:** Foundational security features.
*   **Standard Tier:** Includes basic features plus Kubernetes runtime protection and WAF.
*   **Premium Tier:** Includes standard features plus a network firewall.

## Troubleshoot Choreo

This section provides solutions to common problems encountered while using Choreo.

*   **Angular Web App Displays Nginx Welcome Page:** Ensure the build output directory is correctly specified during component creation.
*   **Trivy Scan Error in BYOC:** Fix the identified vulnerability or add a `.trivyignore` file to the Docker build context path.
*   **config.js File Not Properly Mounted:** Add the `config.js` file to the `app/public` directory and reference it in the `index.html` file.
*   **React App Renders Unexpected HTML:** Reference the `config.js` file in the `index.html` file and ensure the path is correct.
*   **Commits Triggering Automatic Build:** Merge commits and commits pushed directly to the branch can trigger a build.
*   **Nginx Welcome Page After Building a Web App:** Check Docker build logs to ensure the correct files are copied during the build process.
*   **Preferred Language Not Available as a Buildpack:** Use the Dockerfile buildpack.
*   **Incorrect Build Command:** Update the build command in the build configurations section on the build page of the component.
*   **Cannot Add Users with Managed Authentication:** Follow the steps to manage users with Choreo's built-in IDP or set up other OpenID Connect (OIDC) supported IDPs.
*   **Tailscale Proxy Issues:**

    *   **Troubleshooting Logs:** View runtime logs of the running container for the Tailscale proxy deployment.
    *   **Authentication Failure:** Re-check the `TS_AUTH_KEY` for misconfiguration, or generate a new key if it has expired.
    *   **Cannot Access Private Endpoints:** Ensure the on-premises setup is properly connected to the Tailscale network, and verify that the IP addresses and ports in the `Config.yaml` and `endpoints.yaml` files are correct.

# Choreo Kubernetes Infrastructure Upgrade Notice

**Upgrade Date: September 4, 2023, from 3:00 a.m. to 6:00 a.m. UTC**

An upgrade to the Choreo Kubernetes infrastructure is scheduled for September 4, 2023.

## Impact on Java-based Components

Java-based components, specifically those using Java Runtime versions older than jdk8u372 or 11.0.16, may experience out-of-memory errors due to increased memory consumption after the upgrade.

## Affected Component Types

The following Choreo component types are affected:

-   Components created using the Ballerina preset.
-   Integration components created using the WSO2 Micro Integrator preset.
-   REST API Proxies that include mediation policies.
-   Components created using the Dockerfile preset that utilize the Java Runtime.

## Action Required

**Recommended action date: Before September 4, 2023, 3:00 a.m. UTC**

To ensure compatibility and a smooth transition, users are advised to take the following actions before the upgrade:

-   **Ballerina or Micro Integrator-based components**: Redeploy components.
-   **REST API Proxy components with mediation policies**: Redeploy components.
-   **Other Java-based containerized components**:
    1.  Upgrade Java version to OpenJDK / HotSpot - jdk8u372, 11.0.16, 15, or later.
    2.  Rebuild the containerized application.
    3.  Redeploy the containerized component.

### Redeploy a component in Choreo

Instructions to redeploy a component:

1.  Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in.
2.  Select component from **Components Listing**.
3.  In the left navigation menu, click **Deploy**.
4.  Deploy component via the **Build Area** card.

Here's a summary of the provided content, maintaining the headings for organization:

# Test APIs with Choreo API Chat

Choreo API Chat simplifies API testing by allowing you to interact with your APIs using natural language. This eliminates the need for manual test scenario creation and concerns about JSON payload accuracy. It supports REST API Proxy and Service components with REST endpoints. You can test APIs by signing into Choreo Console, selecting a component, navigating to the API Chat pane, and entering queries in natural language.

## Prerequisites
- A REST API Proxy component or a Service component that exposes a REST API with a valid OpenAPI specification. 

## Test your APIs
- Sign in to the Choreo Console.
- Select the component you want to test.
- On the left navigation, click **Test** and then click **API Chat**. This opens the **API Chat** pane.
- Enter your query in natural language and execute it. 

# Test APIs with cURL

Choreo allows you to use cURL commands generated by Choreo. To test your API method follow the steps below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Select the component you want to test.
3. Click **Test** in the left navigation menu and then click **cURL**.
4. Select the environment from the drop-down list.
5. Select an appropriate HTTP method from the **Method** list.
6. Add the necessary parameters for the API method in the **Parameters** tab.
7. Add the required header values in the **Headers** tab.
8. Select the message body type to invoke the API method in the **Body** tab.
9. Copy the generated cURL command.
10. Use the copied cURL command via a cURL client to test your API method.

# Test Components with Test Runner

Test Runner simplifies automated testing of components deployed in Choreo, enabling developers to evaluate applications in various setups. Tests can be created using languages like Go, Java, JavaScript, and Python, or by using a Dockerfile with test scripts or Postman Collections.

## Prerequisites
- Create an organization in Choreo Console.
- Fork the Choreo examples repository.

## Create a test runner component using a buildpack

1.  Sign in to the Choreo Console and navigate to the project home page.
2.  Click **+Create** in the **Component Listing** section.
3.  Click the **Test Runner** card.
4.  Connect a Git Repository.
5.  Select a buildpack based on the language of your choice.
6.  Enter a display name, unique name, and description for the test runner component.
7.  Click **Create**. 

## Build and deploy the test runner component to execute the tests

1.  In the left navigation menu, click **Build**.
2.  In the **Builds** pane, click **Build Latest**.
3.  On the left navigation, click **Deploy**.
4.  In the **Set Up** card, click **Deploy** to deploy the test runner component.
5.  Once the deployment is successful, click **Execute** in the left navigation menu.
6.  Select the environment from the environment list and click **Run Now** to trigger a test execution.
7.  Once the execution is completed it is listed on the execution page. 

# Test GraphQL Endpoints via the GraphQL Console

Choreo offers a GraphQL Console for testing GraphQL endpoints of Service components. It uses OAuth 2.0 for security and generates test keys.

1.  Sign in to the [Choreo Console](https://console.choreo.dev/).
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu and then click **Console**.
4.  In the **GraphQL Console** pane, select the environment from the drop-down list.
5.  Select the required endpoint from the **Endpoint** list.
6.  If the **Network Visibilities** of the endpoint contains **Organization**, click on **Generate URL** to generate a temporary test URL that will be active for 15 minutes.
7.  Enter the API path and the query or mutation you want to test.
8.  Click the play icon.

# Test REST Endpoints via the OpenAPI Console

Choreo provides an OpenAPI Console for testing REST endpoints, securing them with OAuth 2.0 and generating test keys.

1.  Go to the [Choreo Console](https://console.choreo.dev/) and log in.
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu, then select **Console**.
4.  In the **OpenAPI Console** pane, select the desired environment from the drop-down menu.
5.  Choose the endpoint you want to test from the **Endpoint** list.
6.  If the **Network Visibility** is set to **Organization**, click **Generate URL** to create a temporary test URL.
7.  Expand the resource you want to test.
8.  Click the **Try it out** button to enable testing.
9.  Provide values for any parameters, if applicable.
10. Click **Execute**.

# Test Websocket Endpoints via the Websocket Console

Choreo offers a WebSocket Console for testing WebSocket endpoints, securing them with OAuth 2.0 and generating test keys.

1.  Go to the [Choreo Console](https://console.choreo.dev/) and log in.
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu, then select **Console**.
4.  In the **WebSocket Console** pane, select the desired environment from the drop-down list.
5.  Choose the endpoint you want to test from the **Endpoint** list.
6.  If the **Network Visibility** is set to **Organization**, click **Generate URL** to create a temporary test URL.
7.  Expand the channel you want to test.
8.  Click **Connect** to establish a connection.
9.  Send and receive messages.

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

