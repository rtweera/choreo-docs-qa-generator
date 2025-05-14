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