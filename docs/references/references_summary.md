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