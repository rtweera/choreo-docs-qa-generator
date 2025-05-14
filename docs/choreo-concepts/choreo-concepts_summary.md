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