 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).



# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.




 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).


 # Configure Container Resources, Commands, and Arguments

In Choreo, you can view detailed information about the container that comprises a component, such as its image tag, the corresponding commit ID, any imposed resource usage limits, and so on. 

Each component in Choreo is limited to a single main container.

![Container details](../assets/img/devops-and-ci-cd/containers/containers-view.png){.cInlineImage-full}

!!! info "Resource Limits"
    Resource limits ensure that a single component does not take up more resources than it requires, which can affect other workloads on the data plane. If a process exceeds the allocated memory limit, the corresponding container will be forcefully shut down and restarted. If the process exceeds the allocated CPU limit, it gets throttled and can result in significant latencies in compute and I/O operations.

Choreo allows you to edit the default container configuration depending on your requirement.

## Update container configurations

Follow these steps to update container configurations:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to edit container configurations.
3. In the left navigation menu, click **DevOps** and then click **Containers**.
4. On the **Containers** page, click **Edit** to update the corresponding container configuration.
5. Apply the necessary changes and click **Save**.

    ![Edit container configurations](../assets/img/devops-and-ci-cd/containers/edit-container-form.png){.cInlineImage-full}

The following topics walk you through the container configuration changes you can apply.

### Update resource requests and limits

!!! info "Note"
    The capability to update resource requests and limits is only available in paid pricing plans.

To update resource requests and limits, move the corresponding slider to a required position. A resource request cannot be less than its corresponding limit.


### Set the image pull policy

You can select one of the following options as the image pull policy.

- **Always**: The image is always pulled from the container registry, even if a matching tag is already present in the data plane.
- **If Not Present** - The image is pulled from the container registry only if a matching image is not present in the data plane.

    !!! tip

          The recommended option is **If Not Present**.


### Specify container ports

You can specify appropriate values for the **Container Port** and **Service Port**. The **Service Port** is the port exposed outside of the container to your project-scoped endpoint. If you do not know the value to specify as the **Service Port**, specify the **Container Port** value in both fields.

!!! tip

      You do not need to configure port values manually for Ballerina components. The capability to edit port values is primarily for containerized/Dockerfile-based components. 


You can also select an appropriate **Protocol**. 

### Define a command and arguments for the container

You can define a command and arguments for a container when you want to provide or override the `ENTRYPOINT` of a container. For example, in a scenario where you want to run legacy or third-party applications, you would want to provide or override the `ENTRYPOINT` of a container.

![Container command and arguments example](../assets/img/devops-and-ci-cd/containers/example-container-cmd-and-args.png){.cInlineImage-half}

When you define a command and arguments, 

- It specifies the `ENTRYPOINT` array and it is not executed within a shell. 
- Variable references `$(VAR_NAME)` are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged.
- `$$` are reduced to `$`, which allows escaping the `$(VAR_NAME)` syntax. This means that `"$$(VAR_NAME)"` produces the string literal `"$(VAR_NAME)"`. 
- Escaped references are never expanded, regardless of whether the variable exists or not. 

The `ENTRYPOINT` of the container image is used if you do not define a command and arguments for the container.


# Configure Storage

All components you create in Choreo have a default **read-only file system**, which you cannot access or write to from your applications.

Volume mounts allow you to create either temporary or persisted writable file system storage locations for your applications.

## Volume mount types

| Type                              | Description                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Empty Directory (In-Memory)       | A fast, temporary in-memory (tmpfs) storage location. This volume gets erased when you restart or remove the attached container. *Available on all data planes.*    |
| Empty Directory (Disk)            | A temporary storage location on disk. This volume gets destroyed when you restart or remove the attached container. *Only available on private data planes.*        |
| Persistent Volume                 | A permanent storage location. This volume persists even if you restart or remove the attached container. *Only available on private data planes.*                   |

!!! tip 
    All components have a writable location in the `/tmp` directory at the time of component creation. You can also configure other writable locations if required.


## Create a temporary storage space for your container

Empty directory (in-memory or on-disk) mounts allow you to create temporary file systems that your application can read from and write to. This option provides a convenient way to create a *scratch space* to write files temporarily before storing them in a more permanent storage location such as a cloud-backed storage bucket.
For example, unzipping a file, temporarily writing results from a memory-intensive operation to disk, a temporary local cache, etc. 
However, it is important to note that these volumes destroy when you restart or update a container because the volumes are attached to the lifetime of a container.

Follow these steps to create a temporary storage space for your container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a temporary storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Empty Directory (In-Memory)**.

   ![Create temporary storage](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-1.png){.cInlineImage-full}

6. Click **Next**.

    !!! warning "In-memory (tmpfs) storage uses up container memory"
        Storage capacity for this type of volume will count against the container's memory limit.<br/>
        Uncontrolled writes to this location may starve your application process of memory and can result in the container getting killed and restarted if the memory limits exceed.

7. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

    ![Specify mount details](../assets/img/devops-and-ci-cd/storage/create-emptydir-step-2.png){.cInlineImage-full}

8. Click **Create**. This applies the volume mount immediately to your container and triggers a rolling restart.

## Create a persistent storage space for your container

Follow these steps to create a persistent storage space for your container:

!!! info "Note"

       Persistent volume options are only available in private data plane organizations.


1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to create a persistent storage.
3. In the left navigation menu, click **DevOps** and then click **Storage**.
4. Click **+ Create**.
5. In the **Create a Volume Mount** pane, specify a name for the volume and select **Persistent Volume**.
6. Select a **Storage Class**.
7. Move the **Storage Capacity** slider to set the required capacity.
8. Select an appropriate **Access Mode**. 

    !!! tip "Check and specify an access mode supported by the storage class"
        - You must check the cloud provider documentation to select an appropriate access mode that the storage class supports. Choreo does not verify whether the storage class supports the access mode you select.
        - If the storage class does not support the access mode you select, it can result in a runtime mount error.

    ![Create persistent storage](../assets/img/devops-and-ci-cd/storage/create-pv.png){.cInlineImage-full}

9. Click **Next**.
10. To add a mount location, specify a **Mount Path** and click **Add mount**.
  
    !!!tip

          - You can add multiple mount locations to a volume.
          - Mount paths should be *absolute file paths* and will be available to your application to read/write from.

11. Click **Create**. This applies the volume immediately to your container.


# Configure VPNs on the Choreo Cloud Data Plane

Secure access to private networks from the Choreo cloud data plane is an essential use case for cloud data plane users. 

Choreo allows this secure connection using [Tailscale](https://tailscale.com/). For this, Choreo provides a prebuilt Tailscale image component that can act as a forward proxy, which you can deploy in your Choreo project as a service. This service allows you to forward traffic to your external networks via Tailscale’s peer-to-peer [WireGuard](https://tailscale.com/kb/1035/wireguard) network.

The following diagram illustrates the high-level deployment architecture of the Tailscale pre-installed forward proxy:

![Deployment architecture](../assets/img/devops-and-ci-cd/tailscale/deployment-architecture.png)

Let's take a look at the specifics of each part to understand the deployment architecture.

- **Choreo project**

    In Choreo, a project groups various components. For more information on what a project in Choreo is, see the documentation on [Project](../choreo-concepts/project.md).

- **Tailscale proxy**

    This acts as the Tailscale pre-installed forward proxy, facilitating secure peer-to-peer WireGuard connections from the Choreo cloud data plane to private networks. It includes a [Tailscale Daemon](https://tailscale.com/kb/1278/tailscaled), [SOCKS5 proxy](https://tailscale.com/kb/1112/userspace-networking#socks5-vs-http), and a configurable TCP forwarder.

    - **Tailscale daemon**

        This is the core component of Tailscale. It is a software service that provides secure network connectivity and private networking solutions. For more details see the [Tailscale documentation](https://tailscale.com/kb/1278/tailscaled).

    - **SOCKS5 proxy**

        This uses Tailscale’s [userspace networking](https://tailscale.com/kb/1112/userspace-networking) mode, rather than the kernel mode. Therefore, the inbuilt SOCKS5 proxy handles the forwarded traffic and directs it through the Tailscale network.

    - **TCP forwarder**

        Forwards inbound TCP (transmission control protocol) traffic from the Tailscale proxy container’s network interface to the SOCKS5 proxy, ensuring it reaches its destination via the secured WireGuard tunnel.

- **User applications and the Choreo API gateway**

    User applications within the same namespace (project) can use the Kubernetes service created to front the Tailscale proxy, for connecting to the corresponding private endpoints. You can either expose this service within the organization via the internal API gateway or expose it to the public via the external API gateway. For more details, see the documentation on [Choreo endpoints](../develop-components/configure-endpoints.md).

<hr>

Now that you understand the deployment architecture, let’s explore how you can use Tailscale to secure connections to your private networks.

## Configure and use Tailscale to access private network endpoints

This section walks you through the steps to create, configure, deploy, and use the Tailscale proxy component. 
  
![Tailscale proxy deployment](../assets/img/devops-and-ci-cd/tailscale/tailscale-proxy-deployment.png)

Let's get started.

### Prerequisites

- Understand the basics of [how Tailscale works](https://tailscale.com/blog/how-tailscale-works).
- Have a Tailscale account (Tailnet). There are multiple plans available for you to set up your Tailscale network. For details, see [Tailscale plans](https://tailscale.com/pricing).
- Install Tailscale and connect your private data center or server to it, so that your private services are accessible via your Tailscale network. To quickly get started with Tailscale, see the [Tailscale quickstart](https://tailscale.com/kb/1017/install).
- If you are signing in to the Choreo Console for the first time, create an organization as follows:

    1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

### Step 1: Create the Tailscale proxy

#### Step 1.1: Create a project 

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Tailscale Proxy Project            |
    | **Name**                 | tailscale-proxy-project            |
    | **Project Description**  | My Tailscale project               |

4. Click **Create**. This creates the project and takes you to the project home page.

#### Step 1.2: Create the Tailscale proxy component

1. On the project home page, click **Service** under **Create a Component**.
2. Click the **Container Registry** from the **Connect a Docker Image** section
3. In the **Container Registry** list, select **Choreo Samples Registry**.
4. Click the **Tailscale Proxy** card.
5. Enter a display name, component name, and a description for the service. For this guide, let's enter the following values:

    |Field                 |     Value                |
    |----------------------|--------------------------|
    |Component Display Name| Tailscale proxy          |
    |Component Name        | tailscale-proxy          |
    |Description           | Tailscale proxy component|

6. Click **Create**.

Now you have successfully created the Tailscale proxy. You can proceed to configure and deploy it.

### Step 2: Configure and deploy the Tailscale proxy

Here, you will add the required volume mounts, set the Tailscale authentication key, configure the TCP forwarder, configure endpoints, and deploy the Tailscale proxy. Follow the steps given below:

#### Step 2.1: Add required volume mounts

Tailscale requires the following volume mounts for its operations:

 - `/var/run/tailscale`
 - `/.local`

To create the volume mounts, follow the step-by-step instructions in [Configure Storage](../devops-and-ci-cd/configure-storage.md). 

#### Step 2.2: Configure and deploy the component

To configure and deploy the component, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. On the **Build Area** card, click **Configure &  Deploy**.
3. In the **Environment Configurations** pane that opens, click **+ Add** and add the `TS_AUTH_KEY` environment variable as a secret. To add the environment variable, you must obtain an authentication key from your Tailscale network. For details on how to obtain an authentication key from your Tailscale network, see [Auth keys](https://tailscale.com/kb/1085/auth-keys) in the Tailscale documentation.

    !!! info "Note"
        The authentication keys obtained from your Tailscale network have an expiration date and require periodic rotation. To avoid manual rotation, you can generate non-expiring authentication keys using OAuth clients. For details, see [Generating long-lived auth keys](https://tailscale.com/kb/1215/oauth-clients#generating-long-lived-auth-keys) in the Tailscale documentation.
        
        Follow these steps if you want to add an OAuth client secret to the Tailscale proxy component instead of the `TS_AUTH_KEY` environment variable as a secret:

         1. Define a tag named `choreo-vpn` in your Tailscale ACLs. For details, see [Define a tag](https://tailscale.com/kb/1068/tags#define-a-tag) in the Tailscale documentation.
         2. Create an [OAuth client](https://tailscale.com/kb/1215/oauth-clients) with the following scope, ensuring it is assigned to the `choreo-vpn` tag:
             - Keys → Auth Keys → write
         3. Generate the OAuth client and copy the client secret.
         4. Set the client secret as an environment variable named `OAUTH_CLIENT_SECRET`.

4. Click **Next**.
5. In the **File Mount** pane that opens, click **+ Add**.
6. To mount a configuration file to the Tailscale proxy component and specify the port mapping for the TCP forward proxy running there, do the following:
    1. Specify `/config.yaml` as the **Mount Path**.
    2. Specify the following in the sample configuration file:
       ```
       portMappings:
           8080: "100.108.78.93:8090"
           8081: "100.108.78.93:1433"
       ```

        !!! note
            In this sample configuration, the TCP traffic arriving at port 8080 on your Tailscale proxy will be forwarded to port 8090 on the node with IP address 100.108.78.93 in your Tailscale network. Similarly, port 8081 will map to the corresponding address. You can find the IP addresses of your nodes on the [Tailscale machines](https://login.tailscale.com/admin/machines) page in your Tailscale network's admin console or via the Tailscale clients running on your machine.

7. Click **Next**.
8. In the **Endpoints** pane that opens, click **+ Add** and edit the `endpoints.yaml` configuration to expose your Tailscale proxy as a service. The following is a sample `endpoints.yaml` configuration you can use:

    !!! note
        The sample `endpoints.yaml` file given below defines two project-level endpoints. These endpoints can be used by other components within the same project to access the services. If you want to directly expose your private endpoint via the Choreo gateway either with the **Public** or **Organization** visibility, you can set the `networkVisibility` property of the endpoint to `Public` or `Organization`.

    ``` yaml

    version: 0.1
    endpoints:
      - name: Private HTTP service
        port: 8080
        type: REST
        networkVisibility: Project
        context: /
      - name: Private DB service
        port: 8081
        type: TCP
        networkVisibility: Project
        context: /

    ```

9. Click **Save**.
10. Click **Next** and then click **Deploy**.

    !!! note
        Deploying the component may take a while. You can track the progress by observing the logs. Once the deployment is complete, the build status changes to **Active** on the **Development** environment card.

When the component is deployed, you can observe a new node connected to your Tailscale network. To view this, go to the [Tailscale machines](https://login.tailscale.com/admin/machines) page of your Tailscale coordination server.

### Step 3: Access private network endpoints with the Tailscale proxy

Now you have successfully deployed the Tailscale proxy in your project and it is connected to your Tailnet. You can proceed to use the Tailscale proxy to provision access for other components to securely access private network endpoints.

You can [configure endpoints](https://wso2.com/choreo/docs/develop-components/configure-endpoints/#learn-the-endpointsyaml-file) of the Tailscale proxy to use it for various aspects within Choreo.

## Post-deployment actions

### Handle node key expiry

Tailscale nodes have a default [node key](https://tailscale.com/kb/1010/node-keys) expiry time of 180 days. Nodes require re-authentication after key expiry to avoid connection losses and application downtime. There is an option to disable node key expiry if necessary. For more details, see [Node key expiry documentation](https://tailscale.com/kb/1028/key-expiry).

### Handle auth key expiry

[Auth keys](https://tailscale.com/kb/1085/auth-keys) are used to register new nodes into your Tailscale network. The default [expiry time for auth keys](https://tailscale.com/kb/1085/auth-keys#key-expiry) is 90 days, but nodes remain connected even after auth key expiry. This becomes an issue only if the Tailscale Proxy component is redeployed or restarted.

### Update port mapping configurations

If you want to add a new private endpoint to your network and access it via the same Tailscale proxy within Choreo, you must add a new port mapping entry in the port mapping configuration of your Tailscale proxy deployment.

## Best practices

### Configure health checks

Since the Tailscale proxy acts as a forward proxy, it is important to configure health checks. You can use one of the open ports of the TCP forwarder as a health endpoint. For details on how to set up health probes in Choreo, see [Set up health checks](./set-up-health-checks.md).

### Use Tailscale ACLs
You can use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to precisely manage permission for users and devices on your Tailnet.

### Disable scale-to-zero for the Tailscale proxy
It is recommended to disable [Scale-to-Zero](./autoscale/autoscale-components-with-scale-to-zero.md) for the Tailscale proxy because it acts as a forward proxy and should always be up and running to make consistent connections with the Tailscale VPN mesh.
If you enable Scale-to-Zero, you may experience service downtime.

### Run multiple replicas with HPA (horizontal pod autoscaler) 
To achieve high availability and resiliency for the Tailscale proxy, you must run multiple replicas with HPA. To configure multiple replicas for the Tailscale proxy component, go to the **Scaling** page under **DevOps**. For more details, see [Autoscale component replicas](./autoscale/autoscale-component-replicas.md)

## Security best practices

Before deploying the Tailscale proxy in production environments, it is recommended to follow the Tailscale [production best practices](https://tailscale.com/kb/1300/production-best-practices) and [security best practices](https://tailscale.com/kb/1196/security-hardening).

!!! Note
     Choreo blocks incoming connections from other nodes in your Tailnet to the Tailscale proxy to prevent access to your project’s namespace in the Choreo cloud data plane. 

## Troubleshoot issues

For assistance in resolving common Tailscale proxy issues, see [Troubleshoot Tailscale proxy issues](../references/troubleshoot-choreo.md#troubleshoot-tailscale-proxy-issues).



# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.





# Manage Configuration Groups

Choreo allows you to create Configuration Groups to efficiently manage reusable configurations across components within your organization. A Configuration Group is a collection of key-value pairs, where values can be defined for multiple environments. This feature ensures consistency and simplifies the management of configurations across environments.

Configuration groups can be defined at organization level and link to components at deployment time. Once linked, Choreo automatically resolves and mounts the configurations to the respective environments on deployment. You can either link a configuration group to inject the configurations as environment variables or file mounts.

!!!important
    - All configuration group values are encrypted and stored in environment-specific key vaults.
    - Management of configuration groups is restricted to users with Choreo Admin, DevOps, and Platform Engineer roles.
    - Developers can discover configuration groups available within the organization via the **Choreo Internal Marketplace**.

## Create a configuration group

To create a new configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**.
3. On the **Configuration Groups** page, click **Create** and specify the following details to create a new configuration group:
   
    - **Name**: A name for the configuration group (Unique within the organization).
    - **Description**: A description for the configuration group (Optional).
    - **Define Keys**: Define the keys for the configuration group.

        - Configuration keys uniquely identify values in a configuration group. You can map these keys to environment variables or file mounts during deployment. Each key must be unique within the group.

    - **Assign Values**: Define values by environment for the keys defined.

        - By default, all the environments are grouped together allowing you to manage configuration smoothly. You can separate and manage configuration values for each environment as needed.

    - **Create**: Click **Create** to create the configuration group. 
    
4. Now you can link this configuration group to any component within the organization.

!!!note
    - Configuration groups created will be listed in the **Choreo Internal Marketplace**, improving visibility and discoverability for developers.
    - All configuration groups will also be listed in the component deployment drawers, allowing developers to easily link them during deployment.

## Link and use configuration groups

The configuration groups created at organization level can be linked to any component within the organization. A configuration group can be linked as **Environment Variables** or **File Mounts** at deployment time.

Linking a configuration group will inject the values defined in the group during deployment. The values are mapped to environment variable names or file names based on the keys defined in the configuration group. If needed, you can customize the environment variable name or file name by updating the mapping at deployment.

To link a configuration group to a component, follow the steps given below:

1. Navigate to the component you want to link the configuration group.
2. On the **Deploy** page, click **Configure & Deploy**, this will open the configuration and deployment wizard.
3. In the wizard, link the configuration groups as **Environment Variables** or **File Mounts**, based on your requirements.

    === "Environment Variables"

        - Choose the configuration group you want to link to the component.
        - Click **Link** to link the configuration group to the component.

    === "File Mounts"

        - Choose the configuration group you want to link to the component.
        - Specify the **Mount Path** to mount the configuration files.
            
            !!!note
                All configurations within the selected configuration group will be mounted as individual files to the specified mount path/directory.

        - Click **Link** to link the configuration group to the component.

4. Complete the deployment wizard by providing the required details and click **Deploy** to deploy the component with the updated configurations.

## View & edit a configuration group

To view & edit a configuration group, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, select the desired configuration group to view.

    !!!note
        - Only non-sensitive configuration values are displayed in the view mode.
        - Updating the configuration group will not affect the current deployment; changes will be applied when the component is redeployed.

### Edit the configuration group

Configuration keys and values within a configuration group can be modified, and these changes will take effect when the components using the configuration group are redeployed.

To edit the configuration group definition, click **Edit the Configuration Group** and make the necessary updates:

- Add or remove configuration keys.
- Update the configuration group's display name and description.

To edit the configuration values, click the edit icon in the corresponding set of environments and modify the required details:

- Update configuration values.
- Add a new set of configuration values.
- Add or remove environments from an existing set.

!!! warning
    - **Adding a new environment:** Non-sensitive configuration values will be copied to the new environment, but sensitive values will not be. As a result, sensitive values will be cleared across all environments in the set. **New values must be provided for sensitive configurations.**
    - **Removing an environment:** All configuration values for the removed environment will be deleted.

## Delete a configuration group

To delete a configuration group, follow the steps given below:

!!! warning
    Deleting a configuration group is a permanent, non-reversible action. Ensure that the configuration group is not linked to any component before deleting it.

1. In the [Choreo Console](https://console.choreo.dev/), go to the top navigation menu. Click **Organization** and select your organization.
2. In the left navigation menu, click **DevOps** and then click **Configuration Groups**. 
3. In the **Configuration Groups** list, click the delete icon next to the configuration group you want to delete. This will display a confirmation dialog with details about the impact of the deletion.
4. Review the details, then type the configuration group name to confirm the deletion.
5. Click **Delete**.


# Manage Configurations and Secrets

Choreo allows you to easily manage and version your component's configurations and secrets as **file mounts** or **environment variables**.

!!! info "Note"
    All configurations and secrets applied to a Choreo component are stored in an encrypted secret vault in the cloud data plane, which is managed by WSO2.
    If you are on a private data plane, the configurations and secrets are stored in an Azure key vault or AWS secret manager attached to your data plane in your cloud environment.

## The difference between configurations and secrets

Choreo considers all configurations and secrets to be sensitive content when storing them, but gives you the option to choose between secret or configuration when you create a file mount or an environment variable.

- **Secrets** are write-only. Once you create a secret, you cannot see or retrieve its content via the Choreo Console. However, you can overwrite the existing content at any time.
- **Configurations** can be read and updated via the Choreo Console after you create them.
  
    !!!info "Note"

          If you want to include sensitive data such as database passwords, cloud credentials, service accounts, and so on, the recommended approach is to use a secret instead of a configuration.

## Apply a file mount to your container

Follow these steps to apply a file mount to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **File Mount**.
6. If you want to create the file mount as a secret, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create the file mount as a secret, you will not be able to read the file content after you create the file mount.

7. In the **Display Name** field, specify a name for the file mount.
  
    !!!tip

        The display name does not affect the file mount or its content. It is only a reference to identify the configuration or secret you create.

8. In the **File Mount Path** field, specify where to mount the file inside the container. Use an absolute file path with the file name and extension if applicable.
  
    !!!tip

        The file name in the mount path does not need to match the configuration name or the name of the file you upload.

9. Upload a configuration file or copy and paste the configuration content into the editor.

10. Click **Create**.
  
    !!!info "Note"
           
        Configurations and secrets are applied immediately to your environment on creation. To ensure that the container reflects the new content, your existing running replicas undergo a rolling restart.

## Apply environment variables to your container

Follow these steps to apply environment variables to a component you have created:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to define configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click **+ Create**.
5. In the **Create a Config or Secret** pane, click **Environment Variables**.
6. If you want to create the environment variable values as secrets, select **Mark as a Secret**. Otherwise, proceed to the next step.
    
    !!!info "Note"
           
        If you create environment variables as secrets, you will not be able to read the values you set for the environment variables after you create them.

7. In the **Display Name** field, specify a name to identify the configuration or secret.

    !!!tip

        The display name you specify does not affect the environment variables you set. It is only a reference to identify the configuration or secret you create.

8. Under **Add Environment Variables**, specify the necessary environment variables as key-value pairs. You can click **Add Item** to add any number of environment variables.

9. Click **Create**.
   
## Update an existing configuration or secret

Follow these steps to update a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to update configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the edit icon corresponding to the configuration or secret you want to update.
5. Apply the necessary changes and click **Save**.

## Delete an existing configuration or secret

Follow these steps to delete a configuration or secret you have defined:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to delete configurations and secrets.
3. In the left navigation menu, click **DevOps** and then click **Configs & Secrets**.
4. Click the delete icon corresponding to the configuration or secret you want to delete.
5. Enter the name of the configuration or secret to confirm deletion.
6. Click **Delete**.

## Manage Ballerina configurables

Choreo manages the [Ballerina configurables](https://ballerina.io/learn/by-example/configurable-variables/) for the Ballerina components you create.

When you deploy or promote a Ballerina application, you can modify the Ballerina configurables via the **Deploy** page.
  
!!!tip

      You can use configurables instead of environment variables to add file mounts to a Ballerina component.
      Environment variables are primarily for components written in other languages.


# Manage Continuous Deployment Pipelines

By default, all the organizations in Choreo are provisioned with a default continuous deployment pipeline.

Environments within an organization are applied to projects in the order specified by the continuous deployment pipeline. The organization's default continuous deployment pipeline is applied to all the projects. You can create additional pipelines and customize the sequence in which environments are applied in projects.

## Create a new continuous deployment pipeline

### Prerequisites

- To create a new continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. On the **CD Pipelines** page, click **+ Create Pipeline** and specify the following details required to create a new pipeline:
   
    - **Name**: A display name for the new pipeline.
    - **Mark as Default**: Select if you want to assign this new pipeline as the default pipeline for all new projects.
5. Click **+ Add Environment** and add required environments for the pipeline according to the preferred environment sequence.
6. Click **Create**.

## Edit a continuous deployment pipeline

### Prerequisites

- To edit a continuous deployment pipeline in an organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To edit a pipeline, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
4. Click the edit icon corresponding to the pipeline you want to edit.
5. Update the pipeline name, mark the pipeline as default, and change the sequence of environments.
6. Click **Update**.


## Delete a continuous deployment pipeline

To delete a pipeline, follow the steps given below:

!!! warning
    Continuous deployment pipeline deletion is a permanent, non-reversible operation.

!!! info "Note"
        The **default** continuous deployment pipeline of the organization cannot be deleted.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **CD Pipelines**. 
4. Click the delete icon corresponding to the pipeline you want to delete. This displays a confirmation dialog with details on the impact of deletion.

    !!! info "Note"
        If the pipeline is utilized by one or more projects, deletion will not be permitted. To proceed with deleting such a pipeline, you must first remove it from every project that is currently using it.

5. Review the details, then type the pipeline name to confirm the deletion.
6. Click **Delete**.


## Add a continuous deployment pipeline to a project

### Prerequisites

- To add a continuous deployment pipeline to a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To add a pipeline to a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to add the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **+ Add** and select the pipelines you want to add to the project.
6. Click **Add**.


## Remove a continuous deployment pipeline from a project

### Prerequisites

- To remove a continuous deployment pipeline from a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To remove a pipeline from a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to remove the pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Remove** corresponding to the pipeline you want to remove from the project. This displays a confirmation dialog with details on the impact of deletion.
6. Review the details, then type the pipeline name to confirm the deletion.
7. Click **Remove**.

## Change default continuous deployment pipeline of a project

### Prerequisites

- To change the default continuous deployment pipeline of a project, you must have the `ENVIRONMENT-MANAGEMENT` or `PROJECT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles and `PROJECT-MANAGEMENT` permission is granted to Admin, Choreo DevOps, and Project Admin roles.

To change the default pipeline of a project, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. Click the project you want to change the default pipeline.
4. In the left navigation menu, click **DevOps** and then click **CD Pipelines**.
5. Click **Set as Default** corresponding to the pipeline you want to set as the default pipeline for the project. This displays a confirmation dialog that details the impact of setting the new pipeline as the project default.
6. Click **Confirm**.

    !!! info "Note"
        The **default** continuous deployment pipeline is configured separately at both the organization and project levels. When a project is created, it inherits the organization's **default** pipeline. The project's **default** pipeline then defines the default promotion order for its components on the Deploy page.


# Manage Environments

By default, all projects created in the cloud data planes (irrespective of the data plane region) are provisioned with two environments (i.e., development and production).

The environments are listed in the order of deployment and promotion. The initial deployment takes place in the first environment and you can proceed to promote a component to subsequent environments.

## Create a new environment

### Prerequisites

- To create a new environment in a private data plane organization, you must have the `ENVIRONMENT-MANAGEMENT` permission. By default, `ENVIRONMENT-MANAGEMENT` permission is granted to Admin, Choreo Platform Engineer and Choreo DevOps roles.

To create a new environment, follow the steps given below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**.
4. On the **Environments** page, click **Create** and specify the following details to create a new environment:
   
    - **Name**: A display name for the new environment.
    - **Data Plane** - The data plane to create the new environment.

        !!!tip
            The **Data Plane** list displays all the private data planes registered under your organization. 

    - **DNS Prefix**: A DNS prefix to identify the exposed APIs in the environment. Here, the base domain depends on the custom domain attached to the API gateways provisioned on the selected data plane.
    - **Mark environment as a Production environment**: Select if you want this environment to be a production environment.
  
        !!!tip
            In Choreo, you can have multiple non-production and production environments. To work in a production environment, you must have privileged permissions to access and deploy to production environments.

## Delete an environment

To delete an environment, follow the steps given below:

!!! warning
    Environment deletion is a permanent, non-reversible operation.

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. Then select your organization.
3. In the left navigation menu, click **DevOps** and then click **Environments**. 
4. In the **Environments** list, click the delete icon corresponding to the environment you want to delete. This displays a confirmation dialog with details on the impact of deletion.
5. Review the details, then type the environment name to confirm the deletion.
6. Click **Delete**.


# Set Up Health Checks

Health checks ensure that a running container is always healthy and ready to serve traffic.

## Liveness probes

Liveness probes run periodically on your container and restart if the probe fails.
This allows the container to self-heal in scenarios where the application may have crashed or become unresponsive.

## Readiness probes

Similar to liveness probes, readiness probes run periodically throughout the lifecycle of a container.
However, unlike liveness probes, these probes do not restart the container if the probe fails. Instead, they stop the container from receiving network traffic.

!!! warning "Readiness probes on single replicas"
    You must be mindful when you configure readiness probes on a single-running replica. If the readiness probe fails, your application stops receiving traffic  because there is only one active replica. The application may not recover unless the liveness probe fails and restarts the container.

## Probe types

You can configure the following probe types for both readiness and liveness probes.

### HTTP `GET` request

This probe sends an HTTP `GET` request to a specified port and path on the container. A response status code in the range of 200-399 indicates that the request is a success.

Depending on your requirement, you can configure additional HTTP headers.

The recommended approach is to create a `/healthz` or `/health` endpoint in your service for this purpose.

![HTTP GET probe](../assets/img/devops-and-ci-cd/healthchecks/http-get-probe.png){.cInlineImage-half}

### TCP connection probe

This probe attempts to open a socket to the container on the specified port. If it cannot establish a TCP connection, it becomes a failure.

### Execute a command

This probe executes a given script inside the container. A non-zero return from the command is considered a failure.

For example, `["cat", "/tmp/healthy"]` is considered healthy if the file `/tmp/healthy` is present. If not, it becomes a failure (non-zero exit code).
In such scenarios, the application is responsible for writing and maintaining this file in the specified location.

## Configure liveness and readiness probes

Follow these steps to configure liveness and readiness probes on a container:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to configure liveness and readiness probes.
3. In the left navigation menu, click **DevOps** and then click **Health Checks**.
4. On the **Health Checks** page, click **+ Create**.
5. Configure the liveness probe depending on your requirement.

    ![Configure probe](../assets/img/devops-and-ci-cd/healthchecks/confgure-probes.png){.cInlineImage-full}

6. Click **Save**.
7. Configure the readiness probe depending on your requirement.
8. Click **Save**.
  
    !!!info "Note"

          You can update or remove a probe at any time.

Follow these steps to ensure that the container works as expected:

1. In the left navigation menu, click **Runtime** under **DevOps**.
2. On the **Runtime** page, check the details to confirm that the container works as expected. If the container does not start, check the **events and conditions** to see if any of the probes are causing the container to fail.


# View Runtime Details

In Choreo, you can view details about running replicas of a component in a specific environment (i.e., Development or Production).

To view the runtime details of a component, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to view runtime details.
3. In the left navigation menu, click **DevOps** and then click **Runtime**. This opens the **Runtime** page populated with data retrieved from the underlying Choreo data plane.

![Runtime details](../assets/img/devops-and-ci-cd/runtime/runtime-view.png){.cInlineImage-full}

The runtime details you can see here are analogous to a *zoomed-in* view of a specific environment on the **Deploy** page.

The following topics walk you through the specific details you can view and actions you can perform via the **Runtime** page.

## Redeploy a release

On the **Runtime** page, you can click **Redeploy Release** to immediately redeploy all resources, including configurations and secrets, to a specific environment. This triggers a rolling update to sync all the latest changes to the data plane.

!!! info "What is a release?"
    A release in Choreo uniquely identifies an underlying deployment of a component to an environment for a given version. For example, if you deploy a component to two environments across two versions, the component will have four active releases.

The capability to redeploy a release also allows you to quickly restart all the running replicas of a component in a specific environment.

## View running instances

The running instances you see on the **Runtime** page provide insights into the active replicas of your component in the selected environment.

- You can view details of each active replica and its associated real-time CPU and memory usage, status, restarts, and the time of the last activity.
- If you want to see the real-time logs and information on conditions and events of a replica, click the menu icon of the replica and then click **Real-time Logs** or **Conditions & Events** depending on what you need to view. These options provide insights that help to diagnose issues in deployments.

    ![Running instances](../assets/img/devops-and-ci-cd/runtime/running-instaces.png){.cInlineImage-full}

    !!! info "Note"
        - All metrics such as the total and replica-level CPU and memory usage displayed on the **Runtime** page are real-time data and are instantaneous representations of a component's current state. 
        - You can take a look at the observability metrics of a component to see historical data and usage trends.

### Observe real-time container logs

Unlike the logs available in the **Observability Metrics** of a component, these logs are fetched in real-time from the data plane and are not historical. Therefore, you can only see logs of active containers and the last shutdown container.

![Real-time container logs](../assets/img/devops-and-ci-cd/runtime/realtime-container-logs.png){.cInlineImage-full}

- **Display Previous Logs:** Enable to retrieve logs from the last shutdown/crashed/restarted container of an instance.
- **Since Seconds**: Specify the duration in seconds to fetch corresponding logs.  
- **Filter Logs**: Enable to filter and displays matching log lines. This is a fuzzy string search.

### View container conditions and events

Conditions and events provide information necessary to troubleshoot failing deployments. 

![Container conditions and events](../assets/img/devops-and-ci-cd/runtime/container-conditions-and-events.png){.cInlineImage-full}

If a component is not behaving as expected and you cannot detect any issues via the application logs, these events can provide necessary debugging information, such as the following:

- Failing health checks (liveness and readiness probes).
- Missing or invalid configuration/secret mounts.
- Missing or invalid storage volume mounts.
- Scheduling issues in the underlying data plane.


# Autoscale Component Replicas

Choreo allows you to automatically scale your component replicas up or down in number based on resource consumption to ensure high availability.

!!! info "Note"
    Autoscaling capabilities are only available in paid plans for private data plane organizations.
    In the free tier, components run in a single-replica, low-availability mode.

![Scale component replicas](../../assets/img/devops-and-ci-cd/scaling/scaling-view.png){.cInlineImage-full}

The following parameters allow you to scale component replicas:

- **Min replicas**: The minimum number of replicas to run at any given time. It is recommended to keep the value at a minimum of `2`.
- **Max replicas**: The maximum number of replicas to scale up to. In the cloud data plane, this is restricted to a maximum of `5`. There is no restriction on the value in private data planes.
- **CPU Threshold**: The average CPU utilization across all running replicas. If the CPU utilization across all active instances reaches the threshold, the number of active replicas automatically scales up until the average CPU utilization falls below the threshold.
- **Memory Threshold**: The average memory usage across all running replicas. Like the **CPU Threshold**, if all active instances reach the memory threshold, the number of active replicas automatically scales up until the average memory usage falls below the threshold.

!!! tip
    If you update a scaling parameter, it may not immediately reflect in the Choreo Console because the change can take some time to propagate.

!!! info "Run a fixed number of replicas"
    If you want to run exactly `3` replicas for a component, you must set the minimum and maximum replicas to `3`.

!!! warning "Scale to zero"
    - Although it is possible to set the minimum number of replicas to `0`, your component does not scale to zero automatically during low usage. It can only go down to `1` replica.
    - Setting both the minimum and maximum replicas to `0` suspends the deployment.


# Autoscale Components with Scale-to-Zero

Choreo provides the scale-to-zero capability for HTTP applications you deploy in the data plane. This lets you run your components in a serverless mode.

Scale to zero is very useful in lower environments, where you can significantly reduce infrastructure costs by scaling down idle workloads. In production environments, you can also use scale-to-zero capability if your application's behavior aligns with this feature behavior. In the paid tier, if you want to run your application with more guaranteed high availability, it is recommended to choose HPA (Horizontal Pod Autoscaler) scaling method and configure a minimum replica count of 2 or higher.

## How Scale to Zero works in Choreo

!!! info
    For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default.

When Scale to Zero is enabled, your apps will automatically scale down to zero unless they receive HTTP traffic. When the application receives an HTTP request, your workload quickly scales up from zero to handle the request. When a new request is received by the deployment, the deployment will scale up to one replica and serve the request. When the deployment remains idle for a set period (approximately 5 minutes), it will automatically scale back to zero until a new request is received.

When Scale to Zero is enabled, you can set the maximum number of replicas for deployments with this capability. Choreo dynamically scales deployments up to meet high HTTP traffic demand, up to the specified number of replicas. If the pending requests surpass the defined threshold under **Number of pending requests to spawn a new pod**, Choreo automatically adds a new replica to handle the increased load.

![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-view.png){.cInlineImage-full}

## Enable scale to zero

For service components and web-apps you create after February 23, 2024, Choreo enables the scale-to-zero feature by default. When deploying or promoting the component, the deployment will automatically scale-to-zero.
Upon the next request to the deployed service, a replica will be created to serve the request.

!!! note  
    - For the services which contain at least one endpoint with the network visibility as **Project**, Choreo will not automatically scale-to-zero those components when you deploy or promote them.
    - HTTP services that run on a port other than the below list of ports will not automatically scale-to-zero your component when deploying or promoting: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290.


To enable scale-to-zero for service components created before February 23, 2024, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component you want to scale-to-zero. 
3. Make sure the component is deployed to an environment and is ready to receive traffic.
4. In the left navigation menu, click **DevOps** and then click **Scaling**.

    - **If you are a free user**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Free User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/free-user-scaling-view.png){.cInlineImage-full}

    - **If you are a paid user or you are running your applications in your own private data plane**, you will see a view similar to the one below. You can click the **scale-to-zero** card to enable scale-to-zero for your component.

        ![Paid User - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/paid-user-scaling-view.png){.cInlineImage-full}

    !!! note 
         The scale-to-zero service should start within 60 seconds. If it doesn’t, the gateway will timeout the request.

You can independently scale Choreo components in both the **Development** and **Production** environments. The deployment card indicates the scaling status of each environment. To configure the scale-to-zero feature for a specific environment, click on the **scale-to-zero** link, which redirects to the **Devops** → **Scaling** page.

![Deploy View - Scale to Zero](../../assets/img/devops-and-ci-cd/scaling/scale-to-zero-in-deploy-view.png){.cInlineImage-full}

When you turn on the scale-to-zero for your application, the minimum replicas for your app will be set to zero. However, you can still select an appropriate maximum number of replicas.

## Limitations

- The scale-to-zero feature currently exclusively supports web applications and HTTP services. TCP and HTTPS services are not supported to be scaled to zero.
- To scale to zero, your HTTP service must run on one of the specified ports: 5000, 6000, 7000, 8000, 9000, 7070 to 7079, 8080 to 8089, and 9090 to 9099 or 8290. If you have an endpoint in your component running in any other port, your component will not automatically scale-to-zero when deploying or promoting. Also, if you try to switch to the “scale-to-zero” option in the “Devops” → “Scaling” view, it will fail.
- Scheduled tasks and manually triggered components cannot connect to a service on a project scope if scale-to-zero is enabled. Attempting to do so results in the following error:

    `Host not found, not forwarding request.`

    To allow a task-type component to invoke a project-level service, set it to HPA mode if you are on a paid plan, or to no scaling if you are on the Developer plan.

## Architecture 

When your Choreo application scales down to zero, an intermediary proxy service intercepts incoming requests. If a request is directed at your application, this service initiates a scale-up. Requests are held in the proxy's queue until your application becomes active. After scaling up, the proxy forwards the queued requests to your application.

If your application remains without HTTP traffic for an extended period (default idle time is 5 minutes), it will be scaled down to zero until more HTTP requests arrive. Conversely, if there's a surge in HTTP traffic to your scaled-up application, Choreo will further increase its scale to manage the demand. Choreo considers adding additional replicas if the number of queued requests surpasses the 'Target Pending Requests' threshold, which is set to 100 by default. You can adjust this threshold in the user interface.

!!! note 
    The initial request after a long period of inactivity experiences a delay because the application must first scale up from zero. If your API operates in a service-chain sequence (e.g., service-1 activates service-2, which in turn calls service-3), this waiting time may extend further. If your application or its chain takes a considerable time to scale up, be aware that the first request might face a timeout.

## Troubleshooting

When Choreo enables scale-to-zero by default, it will configure the readiness probe with some default values. However, in some cases, you may observe that your first request responds with a 503 status code. To overcome these behaviors, fine-tune the readiness probe in the **DevOps** → **Health Checks** view to match your application's needs.


