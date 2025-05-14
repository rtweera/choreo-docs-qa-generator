     # Configure Mutual TLS Between Components

Mutual transport layer security (mutual TLS) is a protocol that ensures privacy, integrity, and authentication of the data transmitted between two endpoints. In mutual TLS, the client and the server authenticate each other using digital certificates, establishing trust and verifying identities. Upon successful authentication, mutual TLS encrypts the data exchanged between the client and the server, preventing unauthorized access.

In Choreo, you can use mutual TLS to establish secure connections between components within a project.

!!! note
     If mutual TLS is not required, you can configure TLS instead. TLS provides a secure communication channel between a client and server but does not require the client to present a certificate to the server. This results in the absence of mutual authentication between the client and the server. While TLS ensures the confidentiality of data transmitted between the client and server, preventing unauthorized tampering, mutual TLS enhances TLS by introducing client-side authentication and facilitating mutual verification of identities between the client and server. 

     To configure TLS, you can follow the same steps as for mutual TLS as mentioned below, *without having to generate a client certificate*. The client only needs the root certificate to verify the server's identity.

## Generate certificates to establish mutual TLS

- **Root certificate:** Trusted by both the client and the server, this certificate is used to verify the authenticity of other certificates presented during the mutual TLS handshake process and to issue certificates for clients and servers. For a specific project, you can generate a single root certificate using a tool like OpenSSL.

- **Client certificate:** Contains the client’s identity for authentication. The common name (CN) in the certificate identifies the client. The generated client certificate must be signed by the root certificate.

- **Server certificate:** Clients use the server certificate to verify the trustworthiness of the server and establish a secure and authenticated connection. Similar to the client certificates, the server certificate must also be signed by the root certificate. When generating the server certificate, you must specify the server's hostname for the subject alternative name (SAN). You can obtain the hostname for the specific version of a service component from any project endpoint on the **Overview** page.

For example, if your project endpoint is `http://my-service-3781140846:7080/todos`, the hostname will be `my-service-3781140846`.

## Read mutual TLS certificates from your component

The approach to read mutual TLS certificates from a component can vary depending on its implementation. Typically, a component can read the certificate data from the file system or via an environment variable. For detailed instructions on adding environment variables and file mounts to your application, see [Manage Configurations and Secrets](../devops-and-ci-cd/manage-configurations-and-secrets.md).

!!! info
    When you specify a **private key**, ensure you **save it as a secret**.

## Sample for mutual TLS communication

For a sample that demonstrates how you can deploy services that communicate using mutual TLS, see [service-to-service-mtls](https://github.com/wso2/choreo-samples/tree/main/docker-service-to-service-mtls).


# Pass End-User Attributes to Upstream Services

There are scenarios where a backend service needs to apply specific logic or make decisions depending on the user consuming an API. In such scenarios, you must pass end-user attributes to the backend during an API call.

Choreo provides a method to send user information to a backend service through a JSON Web Token (JWT) in an HTTP header of an API request.

## How it works

The backend JWT contains claims transferred between the parties, such as the user and the backend. A claim can be metadata of the request or data about the user. A set of claims is called a dialect, for example, `http://wso2.org/claims`.

For each API request, a digitally signed JWT is carried to the backend service in the following format to ensure that the authenticity of the claims list is verified:

`{token header}.{claims list}.{signature}`

When a request goes through Choreo, the backend JWT is appended as the `X-JWT-Assertion` header in the outgoing message. The backend service fetches the JWT and retrieves the required information about the user, application, or token.

## Claims

Claims are fragments of information included in the JWT. 

The following is a sample claim set added to the end-user token for an access token generated via the authorization code:

!!! tip
    This access token is generated via Asgardeo using the authorization code grant type. Here, the Asgardeo application is configured to include the email claim in the token. 

``` java
{
  "sub": "11f53c32-f8ac-4810-bb79-615b2184baf5",
  "http://wso2.org/claims/apiname": "JWT Test - Endpoint 9090 803",
  "http://wso2.org/claims/applicationtier": "Unlimited",
  "http://wso2.org/claims/version": "1.0.0",
  "http://wso2.org/claims/keytype": "PRODUCTION",
  "iss": "wso2.org/products/am",
  "http://wso2.org/claims/applicationname": "jwtTest2",
  "http://wso2.org/claims/enduserTenantId": "0",
  "http://wso2.org/claims/applicationUUId": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "client_id": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "http://wso2.org/claims/subscriber": "5f4a7105-a889-4f92-9612-eef5bafe4eec",
  "azp": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "org_id": "b554e001-761c-4d3a-a7a6-a61d73d34221",
  "http://wso2.org/claims/tier": "Unlimited",
  "scope": "email openid profile",
  "exp": 1690537362,
  "http://wso2.org/claims/applicationid": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "http://wso2.org/claims/usertype": "Application_User",
  "org_name": "test",
  "iat": 1690533762,
  "email": "testmail@gmail.com",
  "jti": "69558555-d386-4a81-9ca0-0a23f809cd3c",
  "http://wso2.org/claims/apicontext": "/b554e001-761c-4d3a-a7a6-a61d73d34221/swog/jwt-test/endpoint-9090-803/1.0.0"
}
```

The following table describes the information contained in the sample JWT claims set given above:

|             **Claim Name**              |          **Description**           |  **Mandatory/Optional**  |
|-----------------------------------------|------------------------------------|--------------------------|
| `iat`                                   |  The time the token was issued.    |   Mandatory              |
| `jti`                                   |  The unique token identifier.      |   Mandatory              |
| `exp`                                   |  The token expiry time.            |   Mandatory              |
| `iss`                                   |  The issuer of the token.          |   Mandatory              |
| `http://wso2.org/claims/apiname`        |  The name of the API in Choreo.    |   Optional               |
| `http://wso2.org/claims/version`        |  The API version.                  |   Optional               |
| `http://wso2.org/claims/keytype`        |  The environment in Choreo that the API is in (`Development` or `production`).|   Optional |
| `http://wso2.org/claims/apicontext`     |  The API context in Choreo.        |   Optional               |
| `http://wso2.org/claims/subscriber`     |  The subscriber to the API, usually the app developer. |   Optional |
| `http://wso2.org/claims/applicationname`|  The application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationid`  |  The ID of the application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationUUId`|  The UUID of the application.      |   Optional               | 
| `client_id`                             |  The client identifier. This is copied from the original token.             |   Optional |
| `azp`                                   |  The authorized party (the party to which the ID token was issued). This is copied from the original token. |   Optional |
| `org_id`                                |  The organization ID. This is copied from the original token. |   Optional |
| `org_name`                              |  The organization name. This is copied from the original token. |   Optional |
| `http://wso2.org/claims/tier`           |  The tier/price band for the subscription. |   Optional       |
| `scope`                                 |  The scope of the token. This is copied from the original token. |   Optional |              
| `http://wso2.org/claims/usertype`       |  The type of application user whose action invoked the API. |   Optional |
| `email`                                 |  The email address of the user. This is copied from the original token. |   Optional |


!!! note

    The claims that get added to the end-user token can vary depending on the grant type used when generating the access token. For example, if you use the client-credentials grant type to generate the access token, the generated backend JWT would contain the following information:

    ``` java
    { 
      "http://wso2.org/claims/apiname": "DefaultAPI", 
      "http://wso2.org/claims/version": "1.0.0", 
      "http://wso2.org/claims/keytype": "PRODUCTION", 
      "iss": "wso2.org/products/am", 
      "http://wso2.org/claims/enduserTenantId": "0", 
      "exp": 1673245727, 
      "http://wso2.org/claims/usertype": "Application_User", 
      "iat": 1673242127, 
      "jti": "6e3f4392-8bd9-4900-9d08-eaab7429c510", 
      "http://wso2.org/claims/apicontext": "/9e71ab5e-6df5-4727-92d2-80ecf1a6218d/qbky/default/1.0.0" 
    }

    ```

To verify the authenticity of claims in a JWT, the claims must be validated using the public key corresponding to the private key used to sign the JWT.

JSON web key set (JWKS) is a set of keys to validate a JWT. It contains a collection of JSON web keys, which are public keys used to verify the signature of a JWT.

Typically, when a third party (such as an identity provider)issues a JWT and the recipient needs to verify its signature, they can use a JWKS. 
JWKS allows the issuer to rotate keys dynamically rather than hard-coding the public key in the application. The recipient can obtain the public key by accessing the JWKS endpoint.

## JWKS support in Choreo to validate the JWT

Choreo provides an endpoint to specify the public keys for backend JWT validation. Here are the endpoint URLs for the US East and EU regions:

- [https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks)
- [https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks)

!!! note
    For private data planes (PDPs), use the following JWKS endpoint URL template:
    
    `https://<PDP_GATEWAY_DOMAIN>/.wellknown/jwks`

    Be sure to replace `<PDP-GATEWAY-DOMAIN>` with the default domain configured to access the PDP APIs.

The endpoint provides one or more signing keys to validate the JWT.
The JSON web keys have a kid identifier that can be matched with the same property on the JWT to decide which key to use when validating.

The following is a sample JWKS response:

``` java
{
   "keys": [
       {
           "kty": "RSA",
           "e": "AQAB",
           "use": "sig",
           "kid": "ZjcwNmI2ZDJmNWQ0M2I5YzZiYzJmZmM4YjMwMDFlOTA4MGE3ZWZjZTMzNjU3YWU1MzViYjZkOTkzZjYzOGYyNg",
           "alg": "RS256",
           "n": "8vjeHzRhvpfMystncPnLBWy_t5F3eCxbcLbdugWnzfnIgaV6TWnqPBUagJBKpzRZs4A9Qja_ZrSVJjYsbARzCS_qiWp0Cdwkqn6ZCXpmbpfjYnKORq8N8M-zWaSZYbNvWJ5oSO4kH-LKWzODaFebwTJBpsR1vChHH95doxFuUjiZaisVaQgUJ6drRdlDtImp9r9EAX36YROuYFPoEJcvsH4_uuAR6ClJ12RE3M-YN4NTi1waVNvGbz43oNrpPy7SXgpizingxSGMqI6WU2ysRmk_f9ALgiPIpFDpufiCTYaIcRT-YcUyp9nMDlTRskMuD-dQ1sdJOa11P_yMs-glfQ"
       }
   ]
}
```

The following table describes the information contained in the JWKS response:

| **Property** |                                 **Description**                                    |  
|--------------|------------------------------------------------------------------------------------|
| `kty`        |  The cryptographic family to which the key belongs. <br> Choreo only supports RSA. |
| `e`          |  The exponent value of the public key.                                             |
| `use`        |  The purpose of the key. For example, whether it is for signing or encryption.     |
| `kid`        |  The identification parameter to match a specific key.                             |
| `alg`        |  The algorithm to use with the key.                                                |
| `n`          |  The modulus value of the public key.                                              |

## Enable passing end-user attributes to the backend

To enable passing end-user attributes to the backend through API calls via Choreo, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Components Listing** pane, click on the component for which you want to pass end-user attributes to the backend.
3. In the left navigation menu, click **Deploy**.
4. Go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.

    !!! note
         If the component is an API Proxy, go to the **Build Area** card and click **Security Settings**. This opens the **Security Settings** pane.
   
5. Select the **Pass Security Context To Backend** checkbox.
6. Optionally, specify appropriate audience values in the **End User Token Audiences** field. Specifying values restricts the JWT to the respective audiences, enabling the backend service to validate and confirm the intended recipients, including itself.

    !!! note
        The backend JWT does not include the audience field (aud) by default.

7. Click **Apply**.
8. To redeploy the component with the applied setting, go to the **Set Up** card and click **Deploy**.


# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Choreo as an external Identity Provider (IdP). This guide will walk you through setting up Choreo to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

- Assign scopes to an API in Choreo. 
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Choreo and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have a service in Choreo, [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- Deploy and publish your API. 

## Step 1: Assign scopes to an API in Choreo

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Manage** and then **Permissions**.
3. Click **+ Add Permission (Scope)**. 
4. In the **Permission List** pane, enter the permission value and click **+ Add New**.
5. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
6. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
7. Click **Save and Deploy**.
8. In the left navigation, click **Manage** and then **Lifecycle**.
9. Click **Publish** and continue to publish your API to the Choreo Developer Portal. 


## Step 2: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 3: Create an application in Choreo and enable external IdP authentication

Follow the steps below to consume the Choreo API and use an external IdP for authentication:

1. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name and description for the application. 
4. Click **Create**.
5. In the left navigation, under **Credentials** and click **Production**.
6. Select the **Identity Provider** as `Asgardeo`.
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - The Identity Provider dropdown is visible only to organizations where you have configured external IdPs. 

9. In the left navigation menu, click **Subscriptions**.
10. In the **Subscription Management** pane that opens, click **+ Add APIs**.
11. Select the API you assigned scopes to in [step 1](#step-1-assign-scopes-to-an-api-in-choreo) and click **Add**. 

## Step 4: Invoke the Choreo API with scopes

1. On the Choreo Developer Portal, go to your application. 
2. In the left navigation menu, under **Credentials** and click **Production**.
3. Under **Endpoints**, copy the **Token Endpoint** URL. 
4. Obtain an access token by invoking the token endpoint as follows:
   
    !!! note
        - If you are using the production credentials, you need to deploy your component(endpoint) to the production environment by promoting it from the development environment.
        - If you are using the sandbox credentials, you can use the endpoints deployed in the development environment.

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```



5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../testing/test-rest-endpoints-via-the-openapi-console.md) in Choreo by specifying the scope. 



# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

To establish secure communication between the Choreo Gateway and your backend, you can configure mutual TLS.

Mutual TLS authentication involves both the client and server validating each other’s certificates before establishing a connection. The following diagram depicts this scenario:

![Mutual TLS authentication](../assets/img/authentication-and-authorization/mutual-ssl-authentication.png)

## Configure mutual TLS to establish secure connectivity

To establish secure connectivity between the Choreo Gateway and your backend using mutual TLS, you must add the certificate of the backend (server certificate) to Choreo and add the certificate of Choreo (client certificate) as a trusted certificate in the backend.

### Step 1: Configure the backend certificate 

#### Prerequisites

- The endpoint must be protected with TLS. 
- The public certificate of the backend server should be extracted in PEM format and saved on the disk with the `.pem` extension.

To configure the backend certificate, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the API proxy for which you want to configure TLS. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
3. In the left navigation menu, click **Develop** and then click **Endpoints**.
4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
5. Click **Upload Endpoint Certificate**, and select the certificate file that you extracted in the prerequisites section to add it. This adds the certificate to all the environments as the default certificate for the endpoint. You can override this certificate if necessary when you deploy or promote the API.

### Step 2: Configure mutual TLS with the backend service

There are two approaches you can take to configure mutual TLS.

 - Generate a key pair with a self-signed certificate from Choreo, download the public certificate, and subsequently add and configure it in the backend.
 - Upload your own public or private certificate pair to Choreo. Subsequently, add and configure the public certificate of this key pair in your backend.

Follow the step-by-step instructions below depending on how you want to establish mutual TLS with the backend service:

=== "Generate a key pair through Choreo"
    When you follow these steps, Choreo generates a key pair with a self-signed certificate. You can attach this key pair to any API proxy created within the same project.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.    
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Generate new key pair** and specify a value as the common name for the certificate pair. This value will be used to identify the certificate.

        ![Generate new key pair](../assets/img/authentication-and-authorization/generate-new-key-pair.png)
       
    9. Optionally, click **Show advanced options** to expand the section and specify appropriate values for each of the fields.
    10. Click **Generate**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
    
    Now you can associate the certificate with the API and deploy the API.

=== "Use your own certificate pair"
    Here, you can use your own public certificate and private certificate as client certificates.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Use my own key pair**.

        ![Use own key pair](../assets/img/authentication-and-authorization/use-own-key-pair.png)
       
    9. Upload the private key and public certificate in PEM format or copy and paste the content of the private key and public certificate.
    10. Click **Add**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
   
    Now you can associate the certificate with the API and deploy the API.

### Step 3: Associate the certificate with the API

To associate a certificate with the API, follow the steps given below:

1. On the **Endpoints** page, go to the **Existing Certificates** section.
2. Select the certificate you want to associate with the API.

    ![Associate certificate](../assets/img/authentication-and-authorization/associate-certificate.png)

3. Click **Save**.
   
### Step 4: Deploy the API 

To deploy the API, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**.
3. Once the mediation application generation phase is complete, verify the endpoint URL populated for the environment and then click **Save & Deploy**.

Once the deployment is complete, you can [test the API](../testing/test-rest-endpoints-via-the-openapi-console.md). 

## Change the certificate for the production environment

If the API backend changes depending on the environment, the respective certificate must be updated for each environment. 

Here, let's take a look at the steps to update the certificate for the production environment:

1. On the **Deploy** page, go to the **Development** card and click **Promote**.
2. In the **Configurations** pane that opens, click **Endpoint Configuration**. You will see all applicable certificates listed in the **Mutual TLS** list. 
3. Select the certificate applicable to the production environment and click **Promote**. This promotes the component to the production environment with the selected certificate.


# Secure Web Applications with Managed Authentication

The managed authentication capability of Choreo simplifies adding authentication and authorization to a single-page web application.

As a developer, you can easily set up Choreo's managed authentication to seamlessly integrate authentication into your web application. You just need to enable Choreo’s managed authentication, configure the built-in identity provider, and connect to Choreo without having to deal with the complexities of underlying OIDC/OAuth2.0 protocols.

Choreo's managed authentication follows the backend for frontend (BFF) architecture, which is a secure pattern recommended for browser-based applications that utilize OIDC/OAuth2.0 for authentication and authorization. This architecture ensures that OAuth tokens remain secure from browser-side code, making them immune to potential attacks like cross-site scripting (XSS).

!!! note
     Choreo's managed authentication is currently available only for web applications created with **React**, **Angular**, or **Vue.js** buildpacks.

!!! warning
     Managed authentication uses the 'SAMESITE' cookie attribute to prevent CSRF attacks. Therefore, it is recommended to use managed authentication with modern browsers that support the 'SAMESITE' attribute.

## Step 1: Set up managed authentication for your web application

To secure your web application, you must implement authentication and authorization for it. 

To easily set up authentication for your web application with Choreo's managed authentication, follow the steps given below. Before you move on to the next section, see [Develop Web Applications Locally with Choreo’s Managed Authentication](../develop-components/develop-web-applications/develop-web-applications-locally-with-managed-authentication.md) to ensure a seamless authentication experience when developing your web application on your local machine. You can also refer to the [sample React app with managed authentication](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end-with-managed-auth).

### Step 1.1: Implement the sign-in functionality

To allow Choreo to manage the sign-in functionality for your web application, you must implement a sign-in button that redirects users to the `/auth/login` path on click. You can use the following code snippet or any custom button component from a preferred UI component library:

``` javascript
<button onClick={() => {window.location.href="/auth/login"}}>Login</button>
```

This code snippet works as follows:

When a user clicks sign in on your web application, Choreo will redirect the user to the configured identity provider and handle the authentication process, conforming to the OICD/OAuth2.0 protocols. On successful sign-in, Choreo will set the relevant session cookies and redirect the user to the post-sign-in path (default is `/`). The user can then invoke any Choreo-deployed APIs depending on the permission granted.

!!! note
    Refer to [configure the identity provider section](#step-3-configure-the-identity-provider-for-the-web-application) for details on configuring an identity provider for the web application. 

#### Optional: Pass additional query parameters to the identity provider 

If you want to pass additional query parameters to the identity provider, include them in the `/auth/login` request. Choreo appends these parameters to the `authorize` request sent to the identity provider.

For example,

``` javascript
<button onClick={() => {window.location.href="/auth/login?fidp=myfederatedidp"}}>Login</button>
```

### Step 1.2: Obtain user information claims

Choreo's managed authentication allows you to access user information claims that the identity provider returns post-sign-in, either via a cookie or by invoking a GET resource.


#### Obtain user information via the `userinfo` cookie

Upon successful sign-in, Choreo's managed authentication establishes a `userinfo` cookie that is accessible from the post-sign-in path you configured (by default, set to /). This `userinfo` cookie, provided by the identity provider, contains encoded user information claims.

!!! note
    - The `userinfo` cookie is intentionally set to have a short lifespan of only 2 minutes.
    - As a developer, you can decide how to utilize the user information that you retrieve. You must securely store the user information because the stored information can also serve as a means to verify the logged-in state of a user.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice. 

The recommended approach is to retrieve user information from the cookie and subsequently clear the cookie. The following is a sample code snippet that you can include in your post-sign-in path to retrieve user information from the cookie and subsequently clear the cookie:

``` javascript
    import Cookies from 'js-cookie';

    // Read userinfo cookie value.
    const encodedUserInfo = Cookies.get('userinfo')

    // Decode the value. 
    const userInfo = JSON.parse(atob(encodedUserInfo))

    // Store the value in a preferred browser-based storage if needed.

    // Clear the cookie.
    Cookies.remove('userinfo', { path: <post-login-path> })
```
#### Obtain user information via a GET endpoint

Choreo's managed authentication provides the GET endpoint `/auth/userinfo` in addition to the `userinfo` cookie that it sets after successful sign-in. You can use this endpoint to query information about users who have signed in. It also serves as a mechanism to check the state of a user who has signed in.

The following is an example of a request to this endpoint:

``` javascript
const response = await fetch('/auth/userinfo')
```

If a user has signed in, the server sends a `200 OK` response with the user information in JSON format in the response body. However, if the user is not signed in, the server sends a `401 Unauthorized` response.

### Step 1.3: Implement the sign-out functionality

To allow Choreo to manage the sign-out functionality of your web application, you can implement a sign-out button to redirect users to the `/auth/logout` path along with the `session_hint` cookie value on click. You can use the following code snippet or any custom button component from a preferred UI component library:

!!! note
    - It is recommended to clear any user information (if stored) at the time of sign-out.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice.   
    
``` javascript
<button onClick={async () => {
    window.location.href = `/auth/logout?session_hint=${Cookies.get('session_hint')}`;
}}>Logout</button>`
```

When a user clicks the sign-out button, Choreo will clear the session cookies and redirect the users to the OIDC logout endpoint of the configured identity provider (if available).  

### Step 1.4: Invoke APIs

To invoke Choreo APIs within the same organization as your web application, you can use the relative path `/choreo-apis/<api-suffix>`, regardless of whether managed authentication is enabled for the web application or not.

!!! note
    To invoke a Choreo API from a web application, you need to [create a Connection](../develop-components/sharing-and-reusing/create-a-connection.md) from the web application to the Choreo API. 

For example, if the API URL is `https://2d9ec1f6-2f04-4127-974f-0a3b20e97af5-dev.e1-us-east-azure.choreoapis.dev/rbln/item-service/api-e04/1.0.0`, the `<api-suffix>` would be `/rbln/item-service/api-e04/1.0.0`. You can invoke the API using the `/choreo-apis/rbln/item-service/api-e04/1.0.0` relative path from your single-page application.

!!! info
     To copy the exact service URL of a Connection, you can follow the steps given below:
      1. In the Choreo Console, go to the appropriate web application component.
      2. In the left navigation menu, click **Connections** under **Dependencies**.
      3. Click on the required Connection and copy the service URL.

If you enable Choreo's managed authentication, you don't have to manually add any logic to attach an access token to the API call because Choreo APIs accept the cookies set by Choreo's managed authentication. You can directly invoke the API as follows:

```
    const response = await fetch('/choreo-apis/<api-suffix>')
```

If Choreo's managed authentication is disabled, you must ensure that your web application attaches a valid access token to the API call.


### Step 1.5: Handle session expiry

When a user session exceeds the configured session expiry time, it automatically expires. A `401 Unauthorized` response status code for a Choreo API request from a logged-in user indicates that the session may have expired, requiring the user to re-login.

To programmatically handle session expiry and automatically re-login upon receiving a `401 Unauthorized` response from a Choreo API, you can encapsulate the request with re-login logic. The following sample code snippet shows how to wrap GET requests:


``` javascript
    export const performGet = async (url) => {
        try {
            // API call
            return await fetch('/choreo-apis/<api-suffix>');
        } catch (error) {
            if (error instanceof HttpError && error.status === 401) {
                // Re-login
                window.location.href = "/auth/login";
            } else {
                throw error;
            }
        }
    };
```

### Step 1.6: Set up a custom error page

You can set up Choreo's managed authentication to redirect to a customized error page within your web application by defining the error path in the configuration. In the event of an error during a redirection-based process, such as sign in or sign out, Choreo will automatically redirect the user to the designated custom error page.

!!! note
    If you have not configured an error path, Choreo's managed authentication will use its default error page whenever an error occurs.

Choreo's managed authentication will include the following query parameters in the URL when redirecting to the custom error page:

| Parameter      |  Description                                    |
|----------------|-------------------------------------------------|
| code           | A short textual error code indicating the error |
| message        | The description of the error                    |


Now have successfully implemented Choreo's managed authentication for your web application. The next step is to enable managed authentication for the component, and subsequently deploy it.

## Step 2: Enable managed authentication and configure the paths

To ensure that your web application functions seamlessly with managed authentication, it is essential to enable managed authentication for your web application component within Choreo.

You can enable managed authentication for your web application component at the time you deploy the component.

!!! tip
     Managed authentication is enabled by default when you create a web application using **React**, **Angular**, or **Vue.js** buildpacks.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). This opens the project home page.
2. In the **Component Listing** pane, click on the web application for which you want to enable managed authentication.
3. In the left navigation menu, click **Deploy**.
4. In the **Set Up** card, click **Configure & Deploy**.
5. Add the necessary configurations for your component if applicable and click **Next**.
6. Make sure **Managed Authentication with Choreo** toggle is enabled.
7. Specify appropriate values for the following fields:

    | Field            |  Description      | Default value      |
    | ----------------- | ----------------- | ----------------- |
    | Post Login Path   | The relative path that the application will be redirected to on successful sign-in. In your code, you must implement the necessary logic to obtain signed-in user's information from the `userinfo` cookie set by managed authentication. See **Obtain user information via the `userinfo` cookie** section in [Obtain user information claims](#step-12-obtain-user-information-claims). | /                      |
    | Post Logout Path  | The relative path to which Choreo redirects you on successful sign-out.  | /                      |
    | Error Path        | The relative path to which Choreo redirects you when an error occurs during a redirection-based flow (i.e., sign in or sign out). See [Set up a custom error page](#step-16-set-up-a-custom-error-page).             | Built-in error page     |
    | Session Expiry Time | The time in minutes after which the user session expires. For a seamless experience, the session expiry value should match the refresh token expiry time of the OIDC application in your identity provider.               | 10080 Minutes (7 Days)                   |
    | Additional Scopes | All additional scopes required by the web application. The `openid`, `profile`, and `email` scopes are added by default together with the scopes required to invoke subscribed APIs.               | none                   |

    !!! note
         If you need to change these configurations after you deploy the component, you can click **Authentication Settings** on the **Set Up** card, make the necessary changes, and deploy the component once again.

## Step 3: Configure the identity provider for the web application

You can configure your web application to work with the Choreo built-in identity provider, Asgardeo, or any external identity provider which supports OIDC/OAuth2.0 . 

!!! note
    The identity provider configured in this step should contain the users for the web application.

Click the respective tab for details depending on which identity provider you need to configure: 

=== "Configure Choreo built-in identity provider"

     Follow the steps given below to configure the built-in identity provider by generating authentication keys:

    !!! note
         Choreo built-in identity provider is configured by default. Therefore, this step is optional.

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Choreo Built-In Identity Provider**.
     5. Click **Generate Secret**. 

        !!! Note
             If the **Regenerate Secret** button is shown instead of the **Generate Secret** button, it indicates that OAuth keys are already generated for the component for the selected environment.

    !!! tip
        Refer to [Configure a User Store with the Built-In Identity Provider](../../administer/configure-a-user-store-with-built-in-idp/) for details on adding test users in Choreo built-in identity provider.

    !!! tip
        If you need to invoke APIs secured with role-based access control, you can test this within Choreo by creating roles for the application and mapping those roles to relevant permissions (scope) and user groups. For more information, see [create roles and assign permissions](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-2-create-roles-and-assign-permissions) and [assign roles to user groups](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-3-assign-roles-to-user-groups) sections in [Test Secure API Access with Choreo Built-In Security Token Service](../test-secure-api-access-with-choreo-built-in-security-token-service).

=== "Configure Asgardeo"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in Asgardeo**

     1. Sign in to [Asgardeo](https://console.asgardeo.io/).
     2. In the top navigation menu, click the **Organization** list and select your organization.
     3. In the Asgardeo Console left navigation menu, click **Applications**.
     4. Click **+ New Application**.
     5. Click **Standard-Based Application**.
     6. Specify a name for the application and select **OAuth2.0 OpenID Connect** as the protocol.
     7. Click **Register**.
     8. Click the **Protocol** tab and follow these steps:

         1. Select `Code` and `Refresh Token` as the **Allowed grant types**.
         2. Specify the following as **Authorized redirect URLs**:
             - [your-web-application-url]/auth/login/callback
             - [your-web-application-url]/auth/logout/callback
         3. Specify your web application URL under **Allowed origins**.
         4. In the **Access Token** section, select `JWT` as the **Token type**.
         5. Click **Update**. 

            !!! tip
                 If you need to invoke APIs secured with role-based access control, you must create roles in the application and map those roles to relevant permissions (scope). Then those roles should be assigned to user groups. For more information, see the [Asgardeo API authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/).

         6. Copy the **Client ID** and **Client Secret** of the application. You will need to use these values in the next step to link the OIDC/OAuth2.0 application to your Choreo component.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo web application component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Asgardeo - [your-org-name]**.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in Asgardeo. 
     6. Click **Add Keys**.

=== "Configure an external identity provider"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in the external identity provider**

     1. Create an OIDC/OAuth2.0 application in your external identity provider.
     2. Configure the OIDC/OAuth2.0 application as follows:

         1. Set `Code` and `Refresh Token` as allowed grant types.
         2. Add the following as authorized redirect URL.
         3. Specify the following as authorized redirect URLs:
         4. Specify the access token type as JWT.

            !!! tip
                 If you want to invoke APIs secured with role-based access control, you must ensure that users are assigned a role mapping that grants the necessary permission for API invocation. The approach of mapping application roles to users can vary depending on the identity provider.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select your identity provider.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in your external identity provider.
     6. Click **Add Keys**.


# Test Secure API Access with Choreo Built-In Security Token Service

API security can protect APIs from potential threats and vulnerabilities, with authentication and authorization playing key roles. Authentication ensures that only authorized users or applications can access the API. This involves using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization governs the actions permitted for authenticated users or applications within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions.

Choreo simplifies security testing for developers, allowing them to easily test APIs with permissions in non-critical environments. With its integrated security token service, Choreo provides authorization features that generate scopes based on the correlation between scopes, roles, and user groups. Developers can create roles, assign permissions, and set up user-group mappings using Choreo's built-in identity provider (IdP).

This guide walks you through the following steps to test the invocation of secured APIs with permissions using Choreo's built-in authorization capability:

- Assign scopes to an API in Choreo.
- Create roles and assign permissions in Choreo.
- Assign roles to user groups.
- Test the API invocation.
    - When Choreo manages the authentication (i.e., managed authentication enabled).
    - When the application independently handles the authentication (i.e., managed authentication disabled).

## Prerequisites

Before you try out this guide, ensure you have set up the following:

- Configure the Choreo built-in identity provider with users. For step-by-step instructions, see [Configure a User Store with the Built-In Identity Provider](../administer/configure-a-user-store-with-built-in-idp.md).
- Deploy and publish an API via Choreo. If you don't have an existing service in Choreo, you can either [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- A web application for API subscription. If you don't have an application in Choreo, you must [create a web application](../develop-components/develop-web-applications/build-and-deploy-a-single-page-web-application.md)
- Administrator rights in your Choreo organization. You need this access to configure role-group and role-permission mappings.

## Step 1: Assign permissions to an API in Choreo

You can provide fine-grained access control to your API resources with permissions. Follow the steps below to assign permissions to the resources in the API:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Project** list and select the project that contains your component.
3. In the **Component Listing** pane, click on the component for which you want to attach permissions.
4. In the left navigation menu, click **Deploy**.
5. On the **Deploy** page, go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.
6. Go to the **Permissions List** section and click **+ Add Permission(Scope)**.
7. In the **Permissions List** section, enter a permission value and click **+ Add New**.
8. Click the copy icon in front of the added permission to copy the fully qualified name of it. Save this value for future reference.
9. To attach permissions to a resource, click the **Select Permissions** list under the respective resource and select the permissions you want to attach.
10. Click **Apply**.
11. To apply the latest permissions to the deployed component, you must redeploy it. Follow the steps below to redeploy:
    1. Go to the **Set Up** card and click **Configure & Deploy**.
    2. In the **Configurations** pane that opens, click **Next**. This opens the **Endpoint Details** pane.
    3. Click **Deploy**.

12. To publish your API to the Choreo Developer Portal, follow the steps given below:
    1.  In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2.  Click **Publish**.

## Step 2: Create roles and assign permissions

The permissions assigned to your API need to be associated with roles. Follow the steps below to create roles and assign permissions to the roles.

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project that contains your component. 
2. In the left navigation menu, click **Settings**.
3. Click the **Application Security** tab.
4. Click **+ Role**.
5. Specify an appropriate **Role Name** and **Role description**. 
6. Select the permissions you want to assign to the role, and then click **Create**.
  
    !!!tip

            The permissions(scopes) defined for APIs exposed via components in the project and the permissions(scopes) required by connections created for components in the project are listed here. 

## Step 3: Assign roles to user groups

You must assign roles to the user groups defined in your Choreo built-in IdP to ensure that authenticated users can obtain access tokens with the required permissions.

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your component.
2. Click the **Application Security** tab and then click **Role Management**.
  
    !!!tip

            The roles defined within different projects in the organization are listed here.

3. Click **Map Groups** corresponding to a role that you want to assign to a group.
4. Specify a group name and enter to add it. You can add multiple groups if necessary.
5. Click **Save**.

## Step 4: Test the API invocation

To test an API invocation, you must first create a connection to your API. To do this, you must have a web application created. You can use the web application you created while setting up the prerequisites.

To create a connection to the web application, follow the steps given below:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project where you created the web application.
2. On the project home page, click the web application listed under **Component Listing**.
3. In the left navigation menu, click **Dependencies** and then click **Connections**.
4. Create a connection to the API you deployed in [Step 1](#step-1-assign-permissions-to-an-api-in-choreo). 
   
Now you can proceed to deploy the web application.

When deploying, if your web application is a single-page application (SPA), you have the option to allow Choreo to handle authentication on behalf of the application. This approach eliminates the need to incorporate OAuth protocol-specific logic into your application.

### Test the invocation when Choreo-managed authentication is enabled

If managed authentication is enabled for your web application, Choreo automatically handles obtaining the necessary permission for API invocation. This occurs during the request for access tokens, allowing you to seamlessly invoke the subscribed APIs through your web application without additional intervention. 

!!! note
    If you change the permissions of an existing connection or create a new connection with permissions, you must redeploy your web application to ensure proper API invocation with managed authentication.

### Test the invocation when the application manages the authentication

If your application manages authentication independently, follow the steps below to generate the necessary OAuth credentials to obtain access tokens:

1. In the left navigation menu, click **Settings**. This opens the settings of the web application component.
2. Click the **Authentication Keys** tab.
3. Click on an environment tab depending on the environment for which you want to generate credentials.
4. Select **Choreo Built-In Identity Provider** as the identity provider.
5. Click to expand **Advanced Configurations** and make sure the `code` and `refresh` grant types are selected. This is required to obtain access tokens with an authorization code grant.
6. Configure the callback URL of the web application to receive the authorization code.
7. Click **Update Configurations**.
8. Click **Regenerate Secret** and make a note of the client ID and secret that is generated.
9. Retrieve an access token using the authorization code grant, specifying the necessary OAuth scopes (You can see the endpoint details on the right side).
    - When prompted for authentication, enter the credentials of a user within the built-in identity provider (IdP) who possesses the required assigned groups.
    - Navigate through the OAuth flow to obtain the JWT access token.
10. Invoke the subscribed API using the access token.




# Configure Mutual TLS Between Components

Mutual transport layer security (mutual TLS) is a protocol that ensures privacy, integrity, and authentication of the data transmitted between two endpoints. In mutual TLS, the client and the server authenticate each other using digital certificates, establishing trust and verifying identities. Upon successful authentication, mutual TLS encrypts the data exchanged between the client and the server, preventing unauthorized access.

In Choreo, you can use mutual TLS to establish secure connections between components within a project.

!!! note
     If mutual TLS is not required, you can configure TLS instead. TLS provides a secure communication channel between a client and server but does not require the client to present a certificate to the server. This results in the absence of mutual authentication between the client and the server. While TLS ensures the confidentiality of data transmitted between the client and server, preventing unauthorized tampering, mutual TLS enhances TLS by introducing client-side authentication and facilitating mutual verification of identities between the client and server. 

     To configure TLS, you can follow the same steps as for mutual TLS as mentioned below, *without having to generate a client certificate*. The client only needs the root certificate to verify the server's identity.

## Generate certificates to establish mutual TLS

- **Root certificate:** Trusted by both the client and the server, this certificate is used to verify the authenticity of other certificates presented during the mutual TLS handshake process and to issue certificates for clients and servers. For a specific project, you can generate a single root certificate using a tool like OpenSSL.

- **Client certificate:** Contains the client’s identity for authentication. The common name (CN) in the certificate identifies the client. The generated client certificate must be signed by the root certificate.

- **Server certificate:** Clients use the server certificate to verify the trustworthiness of the server and establish a secure and authenticated connection. Similar to the client certificates, the server certificate must also be signed by the root certificate. When generating the server certificate, you must specify the server's hostname for the subject alternative name (SAN). You can obtain the hostname for the specific version of a service component from any project endpoint on the **Overview** page.

For example, if your project endpoint is `http://my-service-3781140846:7080/todos`, the hostname will be `my-service-3781140846`.

## Read mutual TLS certificates from your component

The approach to read mutual TLS certificates from a component can vary depending on its implementation. Typically, a component can read the certificate data from the file system or via an environment variable. For detailed instructions on adding environment variables and file mounts to your application, see [Manage Configurations and Secrets](../devops-and-ci-cd/manage-configurations-and-secrets.md).

!!! info
    When you specify a **private key**, ensure you **save it as a secret**.

## Sample for mutual TLS communication

For a sample that demonstrates how you can deploy services that communicate using mutual TLS, see [service-to-service-mtls](https://github.com/wso2/choreo-samples/tree/main/docker-service-to-service-mtls).


# Pass End-User Attributes to Upstream Services

There are scenarios where a backend service needs to apply specific logic or make decisions depending on the user consuming an API. In such scenarios, you must pass end-user attributes to the backend during an API call.

Choreo provides a method to send user information to a backend service through a JSON Web Token (JWT) in an HTTP header of an API request.

## How it works

The backend JWT contains claims transferred between the parties, such as the user and the backend. A claim can be metadata of the request or data about the user. A set of claims is called a dialect, for example, `http://wso2.org/claims`.

For each API request, a digitally signed JWT is carried to the backend service in the following format to ensure that the authenticity of the claims list is verified:

`{token header}.{claims list}.{signature}`

When a request goes through Choreo, the backend JWT is appended as the `X-JWT-Assertion` header in the outgoing message. The backend service fetches the JWT and retrieves the required information about the user, application, or token.

## Claims

Claims are fragments of information included in the JWT. 

The following is a sample claim set added to the end-user token for an access token generated via the authorization code:

!!! tip
    This access token is generated via Asgardeo using the authorization code grant type. Here, the Asgardeo application is configured to include the email claim in the token. 

``` java
{
  "sub": "11f53c32-f8ac-4810-bb79-615b2184baf5",
  "http://wso2.org/claims/apiname": "JWT Test - Endpoint 9090 803",
  "http://wso2.org/claims/applicationtier": "Unlimited",
  "http://wso2.org/claims/version": "1.0.0",
  "http://wso2.org/claims/keytype": "PRODUCTION",
  "iss": "wso2.org/products/am",
  "http://wso2.org/claims/applicationname": "jwtTest2",
  "http://wso2.org/claims/enduserTenantId": "0",
  "http://wso2.org/claims/applicationUUId": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "client_id": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "http://wso2.org/claims/subscriber": "5f4a7105-a889-4f92-9612-eef5bafe4eec",
  "azp": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "org_id": "b554e001-761c-4d3a-a7a6-a61d73d34221",
  "http://wso2.org/claims/tier": "Unlimited",
  "scope": "email openid profile",
  "exp": 1690537362,
  "http://wso2.org/claims/applicationid": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "http://wso2.org/claims/usertype": "Application_User",
  "org_name": "test",
  "iat": 1690533762,
  "email": "testmail@gmail.com",
  "jti": "69558555-d386-4a81-9ca0-0a23f809cd3c",
  "http://wso2.org/claims/apicontext": "/b554e001-761c-4d3a-a7a6-a61d73d34221/swog/jwt-test/endpoint-9090-803/1.0.0"
}
```

The following table describes the information contained in the sample JWT claims set given above:

|             **Claim Name**              |          **Description**           |  **Mandatory/Optional**  |
|-----------------------------------------|------------------------------------|--------------------------|
| `iat`                                   |  The time the token was issued.    |   Mandatory              |
| `jti`                                   |  The unique token identifier.      |   Mandatory              |
| `exp`                                   |  The token expiry time.            |   Mandatory              |
| `iss`                                   |  The issuer of the token.          |   Mandatory              |
| `http://wso2.org/claims/apiname`        |  The name of the API in Choreo.    |   Optional               |
| `http://wso2.org/claims/version`        |  The API version.                  |   Optional               |
| `http://wso2.org/claims/keytype`        |  The environment in Choreo that the API is in (`Development` or `production`).|   Optional |
| `http://wso2.org/claims/apicontext`     |  The API context in Choreo.        |   Optional               |
| `http://wso2.org/claims/subscriber`     |  The subscriber to the API, usually the app developer. |   Optional |
| `http://wso2.org/claims/applicationname`|  The application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationid`  |  The ID of the application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationUUId`|  The UUID of the application.      |   Optional               | 
| `client_id`                             |  The client identifier. This is copied from the original token.             |   Optional |
| `azp`                                   |  The authorized party (the party to which the ID token was issued). This is copied from the original token. |   Optional |
| `org_id`                                |  The organization ID. This is copied from the original token. |   Optional |
| `org_name`                              |  The organization name. This is copied from the original token. |   Optional |
| `http://wso2.org/claims/tier`           |  The tier/price band for the subscription. |   Optional       |
| `scope`                                 |  The scope of the token. This is copied from the original token. |   Optional |              
| `http://wso2.org/claims/usertype`       |  The type of application user whose action invoked the API. |   Optional |
| `email`                                 |  The email address of the user. This is copied from the original token. |   Optional |


!!! note

    The claims that get added to the end-user token can vary depending on the grant type used when generating the access token. For example, if you use the client-credentials grant type to generate the access token, the generated backend JWT would contain the following information:

    ``` java
    { 
      "http://wso2.org/claims/apiname": "DefaultAPI", 
      "http://wso2.org/claims/version": "1.0.0", 
      "http://wso2.org/claims/keytype": "PRODUCTION", 
      "iss": "wso2.org/products/am", 
      "http://wso2.org/claims/enduserTenantId": "0", 
      "exp": 1673245727, 
      "http://wso2.org/claims/usertype": "Application_User", 
      "iat": 1673242127, 
      "jti": "6e3f4392-8bd9-4900-9d08-eaab7429c510", 
      "http://wso2.org/claims/apicontext": "/9e71ab5e-6df5-4727-92d2-80ecf1a6218d/qbky/default/1.0.0" 
    }

    ```

To verify the authenticity of claims in a JWT, the claims must be validated using the public key corresponding to the private key used to sign the JWT.

JSON web key set (JWKS) is a set of keys to validate a JWT. It contains a collection of JSON web keys, which are public keys used to verify the signature of a JWT.

Typically, when a third party (such as an identity provider)issues a JWT and the recipient needs to verify its signature, they can use a JWKS. 
JWKS allows the issuer to rotate keys dynamically rather than hard-coding the public key in the application. The recipient can obtain the public key by accessing the JWKS endpoint.

## JWKS support in Choreo to validate the JWT

Choreo provides an endpoint to specify the public keys for backend JWT validation. Here are the endpoint URLs for the US East and EU regions:

- [https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks)
- [https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks)

!!! note
    For private data planes (PDPs), use the following JWKS endpoint URL template:
    
    `https://<PDP_GATEWAY_DOMAIN>/.wellknown/jwks`

    Be sure to replace `<PDP-GATEWAY-DOMAIN>` with the default domain configured to access the PDP APIs.

The endpoint provides one or more signing keys to validate the JWT.
The JSON web keys have a kid identifier that can be matched with the same property on the JWT to decide which key to use when validating.

The following is a sample JWKS response:

``` java
{
   "keys": [
       {
           "kty": "RSA",
           "e": "AQAB",
           "use": "sig",
           "kid": "ZjcwNmI2ZDJmNWQ0M2I5YzZiYzJmZmM4YjMwMDFlOTA4MGE3ZWZjZTMzNjU3YWU1MzViYjZkOTkzZjYzOGYyNg",
           "alg": "RS256",
           "n": "8vjeHzRhvpfMystncPnLBWy_t5F3eCxbcLbdugWnzfnIgaV6TWnqPBUagJBKpzRZs4A9Qja_ZrSVJjYsbARzCS_qiWp0Cdwkqn6ZCXpmbpfjYnKORq8N8M-zWaSZYbNvWJ5oSO4kH-LKWzODaFebwTJBpsR1vChHH95doxFuUjiZaisVaQgUJ6drRdlDtImp9r9EAX36YROuYFPoEJcvsH4_uuAR6ClJ12RE3M-YN4NTi1waVNvGbz43oNrpPy7SXgpizingxSGMqI6WU2ysRmk_f9ALgiPIpFDpufiCTYaIcRT-YcUyp9nMDlTRskMuD-dQ1sdJOa11P_yMs-glfQ"
       }
   ]
}
```

The following table describes the information contained in the JWKS response:

| **Property** |                                 **Description**                                    |  
|--------------|------------------------------------------------------------------------------------|
| `kty`        |  The cryptographic family to which the key belongs. <br> Choreo only supports RSA. |
| `e`          |  The exponent value of the public key.                                             |
| `use`        |  The purpose of the key. For example, whether it is for signing or encryption.     |
| `kid`        |  The identification parameter to match a specific key.                             |
| `alg`        |  The algorithm to use with the key.                                                |
| `n`          |  The modulus value of the public key.                                              |

## Enable passing end-user attributes to the backend

To enable passing end-user attributes to the backend through API calls via Choreo, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Components Listing** pane, click on the component for which you want to pass end-user attributes to the backend.
3. In the left navigation menu, click **Deploy**.
4. Go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.

    !!! note
         If the component is an API Proxy, go to the **Build Area** card and click **Security Settings**. This opens the **Security Settings** pane.
   
5. Select the **Pass Security Context To Backend** checkbox.
6. Optionally, specify appropriate audience values in the **End User Token Audiences** field. Specifying values restricts the JWT to the respective audiences, enabling the backend service to validate and confirm the intended recipients, including itself.

    !!! note
        The backend JWT does not include the audience field (aud) by default.

7. Click **Apply**.
8. To redeploy the component with the applied setting, go to the **Set Up** card and click **Deploy**.


# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Choreo as an external Identity Provider (IdP). This guide will walk you through setting up Choreo to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

- Assign scopes to an API in Choreo. 
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Choreo and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have a service in Choreo, [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- Deploy and publish your API. 

## Step 1: Assign scopes to an API in Choreo

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Manage** and then **Permissions**.
3. Click **+ Add Permission (Scope)**. 
4. In the **Permission List** pane, enter the permission value and click **+ Add New**.
5. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
6. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
7. Click **Save and Deploy**.
8. In the left navigation, click **Manage** and then **Lifecycle**.
9. Click **Publish** and continue to publish your API to the Choreo Developer Portal. 


## Step 2: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 3: Create an application in Choreo and enable external IdP authentication

Follow the steps below to consume the Choreo API and use an external IdP for authentication:

1. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name and description for the application. 
4. Click **Create**.
5. In the left navigation, under **Credentials** and click **Production**.
6. Select the **Identity Provider** as `Asgardeo`.
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - The Identity Provider dropdown is visible only to organizations where you have configured external IdPs. 

9. In the left navigation menu, click **Subscriptions**.
10. In the **Subscription Management** pane that opens, click **+ Add APIs**.
11. Select the API you assigned scopes to in [step 1](#step-1-assign-scopes-to-an-api-in-choreo) and click **Add**. 

## Step 4: Invoke the Choreo API with scopes

1. On the Choreo Developer Portal, go to your application. 
2. In the left navigation menu, under **Credentials** and click **Production**.
3. Under **Endpoints**, copy the **Token Endpoint** URL. 
4. Obtain an access token by invoking the token endpoint as follows:
   
    !!! note
        - If you are using the production credentials, you need to deploy your component(endpoint) to the production environment by promoting it from the development environment.
        - If you are using the sandbox credentials, you can use the endpoints deployed in the development environment.

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```



5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../testing/test-rest-endpoints-via-the-openapi-console.md) in Choreo by specifying the scope. 



# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

To establish secure communication between the Choreo Gateway and your backend, you can configure mutual TLS.

Mutual TLS authentication involves both the client and server validating each other’s certificates before establishing a connection. The following diagram depicts this scenario:

![Mutual TLS authentication](../assets/img/authentication-and-authorization/mutual-ssl-authentication.png)

## Configure mutual TLS to establish secure connectivity

To establish secure connectivity between the Choreo Gateway and your backend using mutual TLS, you must add the certificate of the backend (server certificate) to Choreo and add the certificate of Choreo (client certificate) as a trusted certificate in the backend.

### Step 1: Configure the backend certificate 

#### Prerequisites

- The endpoint must be protected with TLS. 
- The public certificate of the backend server should be extracted in PEM format and saved on the disk with the `.pem` extension.

To configure the backend certificate, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the API proxy for which you want to configure TLS. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
3. In the left navigation menu, click **Develop** and then click **Endpoints**.
4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
5. Click **Upload Endpoint Certificate**, and select the certificate file that you extracted in the prerequisites section to add it. This adds the certificate to all the environments as the default certificate for the endpoint. You can override this certificate if necessary when you deploy or promote the API.

### Step 2: Configure mutual TLS with the backend service

There are two approaches you can take to configure mutual TLS.

 - Generate a key pair with a self-signed certificate from Choreo, download the public certificate, and subsequently add and configure it in the backend.
 - Upload your own public or private certificate pair to Choreo. Subsequently, add and configure the public certificate of this key pair in your backend.

Follow the step-by-step instructions below depending on how you want to establish mutual TLS with the backend service:

=== "Generate a key pair through Choreo"
    When you follow these steps, Choreo generates a key pair with a self-signed certificate. You can attach this key pair to any API proxy created within the same project.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.    
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Generate new key pair** and specify a value as the common name for the certificate pair. This value will be used to identify the certificate.

        ![Generate new key pair](../assets/img/authentication-and-authorization/generate-new-key-pair.png)
       
    9. Optionally, click **Show advanced options** to expand the section and specify appropriate values for each of the fields.
    10. Click **Generate**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
    
    Now you can associate the certificate with the API and deploy the API.

=== "Use your own certificate pair"
    Here, you can use your own public certificate and private certificate as client certificates.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Use my own key pair**.

        ![Use own key pair](../assets/img/authentication-and-authorization/use-own-key-pair.png)
       
    9. Upload the private key and public certificate in PEM format or copy and paste the content of the private key and public certificate.
    10. Click **Add**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
   
    Now you can associate the certificate with the API and deploy the API.

### Step 3: Associate the certificate with the API

To associate a certificate with the API, follow the steps given below:

1. On the **Endpoints** page, go to the **Existing Certificates** section.
2. Select the certificate you want to associate with the API.

    ![Associate certificate](../assets/img/authentication-and-authorization/associate-certificate.png)

3. Click **Save**.
   
### Step 4: Deploy the API 

To deploy the API, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**.
3. Once the mediation application generation phase is complete, verify the endpoint URL populated for the environment and then click **Save & Deploy**.

Once the deployment is complete, you can [test the API](../testing/test-rest-endpoints-via-the-openapi-console.md). 

## Change the certificate for the production environment

If the API backend changes depending on the environment, the respective certificate must be updated for each environment. 

Here, let's take a look at the steps to update the certificate for the production environment:

1. On the **Deploy** page, go to the **Development** card and click **Promote**.
2. In the **Configurations** pane that opens, click **Endpoint Configuration**. You will see all applicable certificates listed in the **Mutual TLS** list. 
3. Select the certificate applicable to the production environment and click **Promote**. This promotes the component to the production environment with the selected certificate.


# Secure Web Applications with Managed Authentication

The managed authentication capability of Choreo simplifies adding authentication and authorization to a single-page web application.

As a developer, you can easily set up Choreo's managed authentication to seamlessly integrate authentication into your web application. You just need to enable Choreo’s managed authentication, configure the built-in identity provider, and connect to Choreo without having to deal with the complexities of underlying OIDC/OAuth2.0 protocols.

Choreo's managed authentication follows the backend for frontend (BFF) architecture, which is a secure pattern recommended for browser-based applications that utilize OIDC/OAuth2.0 for authentication and authorization. This architecture ensures that OAuth tokens remain secure from browser-side code, making them immune to potential attacks like cross-site scripting (XSS).

!!! note
     Choreo's managed authentication is currently available only for web applications created with **React**, **Angular**, or **Vue.js** buildpacks.

!!! warning
     Managed authentication uses the 'SAMESITE' cookie attribute to prevent CSRF attacks. Therefore, it is recommended to use managed authentication with modern browsers that support the 'SAMESITE' attribute.

## Step 1: Set up managed authentication for your web application

To secure your web application, you must implement authentication and authorization for it. 

To easily set up authentication for your web application with Choreo's managed authentication, follow the steps given below. Before you move on to the next section, see [Develop Web Applications Locally with Choreo’s Managed Authentication](../develop-components/develop-web-applications/develop-web-applications-locally-with-managed-authentication.md) to ensure a seamless authentication experience when developing your web application on your local machine. You can also refer to the [sample React app with managed authentication](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end-with-managed-auth).

### Step 1.1: Implement the sign-in functionality

To allow Choreo to manage the sign-in functionality for your web application, you must implement a sign-in button that redirects users to the `/auth/login` path on click. You can use the following code snippet or any custom button component from a preferred UI component library:

``` javascript
<button onClick={() => {window.location.href="/auth/login"}}>Login</button>
```

This code snippet works as follows:

When a user clicks sign in on your web application, Choreo will redirect the user to the configured identity provider and handle the authentication process, conforming to the OICD/OAuth2.0 protocols. On successful sign-in, Choreo will set the relevant session cookies and redirect the user to the post-sign-in path (default is `/`). The user can then invoke any Choreo-deployed APIs depending on the permission granted.

!!! note
    Refer to [configure the identity provider section](#step-3-configure-the-identity-provider-for-the-web-application) for details on configuring an identity provider for the web application. 

#### Optional: Pass additional query parameters to the identity provider 

If you want to pass additional query parameters to the identity provider, include them in the `/auth/login` request. Choreo appends these parameters to the `authorize` request sent to the identity provider.

For example,

``` javascript
<button onClick={() => {window.location.href="/auth/login?fidp=myfederatedidp"}}>Login</button>
```

### Step 1.2: Obtain user information claims

Choreo's managed authentication allows you to access user information claims that the identity provider returns post-sign-in, either via a cookie or by invoking a GET resource.


#### Obtain user information via the `userinfo` cookie

Upon successful sign-in, Choreo's managed authentication establishes a `userinfo` cookie that is accessible from the post-sign-in path you configured (by default, set to /). This `userinfo` cookie, provided by the identity provider, contains encoded user information claims.

!!! note
    - The `userinfo` cookie is intentionally set to have a short lifespan of only 2 minutes.
    - As a developer, you can decide how to utilize the user information that you retrieve. You must securely store the user information because the stored information can also serve as a means to verify the logged-in state of a user.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice. 

The recommended approach is to retrieve user information from the cookie and subsequently clear the cookie. The following is a sample code snippet that you can include in your post-sign-in path to retrieve user information from the cookie and subsequently clear the cookie:

``` javascript
    import Cookies from 'js-cookie';

    // Read userinfo cookie value.
    const encodedUserInfo = Cookies.get('userinfo')

    // Decode the value. 
    const userInfo = JSON.parse(atob(encodedUserInfo))

    // Store the value in a preferred browser-based storage if needed.

    // Clear the cookie.
    Cookies.remove('userinfo', { path: <post-login-path> })
```
#### Obtain user information via a GET endpoint

Choreo's managed authentication provides the GET endpoint `/auth/userinfo` in addition to the `userinfo` cookie that it sets after successful sign-in. You can use this endpoint to query information about users who have signed in. It also serves as a mechanism to check the state of a user who has signed in.

The following is an example of a request to this endpoint:

``` javascript
const response = await fetch('/auth/userinfo')
```

If a user has signed in, the server sends a `200 OK` response with the user information in JSON format in the response body. However, if the user is not signed in, the server sends a `401 Unauthorized` response.

### Step 1.3: Implement the sign-out functionality

To allow Choreo to manage the sign-out functionality of your web application, you can implement a sign-out button to redirect users to the `/auth/logout` path along with the `session_hint` cookie value on click. You can use the following code snippet or any custom button component from a preferred UI component library:

!!! note
    - It is recommended to clear any user information (if stored) at the time of sign-out.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice.   
    
``` javascript
<button onClick={async () => {
    window.location.href = `/auth/logout?session_hint=${Cookies.get('session_hint')}`;
}}>Logout</button>`
```

When a user clicks the sign-out button, Choreo will clear the session cookies and redirect the users to the OIDC logout endpoint of the configured identity provider (if available).  

### Step 1.4: Invoke APIs

To invoke Choreo APIs within the same organization as your web application, you can use the relative path `/choreo-apis/<api-suffix>`, regardless of whether managed authentication is enabled for the web application or not.

!!! note
    To invoke a Choreo API from a web application, you need to [create a Connection](../develop-components/sharing-and-reusing/create-a-connection.md) from the web application to the Choreo API. 

For example, if the API URL is `https://2d9ec1f6-2f04-4127-974f-0a3b20e97af5-dev.e1-us-east-azure.choreoapis.dev/rbln/item-service/api-e04/1.0.0`, the `<api-suffix>` would be `/rbln/item-service/api-e04/1.0.0`. You can invoke the API using the `/choreo-apis/rbln/item-service/api-e04/1.0.0` relative path from your single-page application.

!!! info
     To copy the exact service URL of a Connection, you can follow the steps given below:
      1. In the Choreo Console, go to the appropriate web application component.
      2. In the left navigation menu, click **Connections** under **Dependencies**.
      3. Click on the required Connection and copy the service URL.

If you enable Choreo's managed authentication, you don't have to manually add any logic to attach an access token to the API call because Choreo APIs accept the cookies set by Choreo's managed authentication. You can directly invoke the API as follows:

```
    const response = await fetch('/choreo-apis/<api-suffix>')
```

If Choreo's managed authentication is disabled, you must ensure that your web application attaches a valid access token to the API call.


### Step 1.5: Handle session expiry

When a user session exceeds the configured session expiry time, it automatically expires. A `401 Unauthorized` response status code for a Choreo API request from a logged-in user indicates that the session may have expired, requiring the user to re-login.

To programmatically handle session expiry and automatically re-login upon receiving a `401 Unauthorized` response from a Choreo API, you can encapsulate the request with re-login logic. The following sample code snippet shows how to wrap GET requests:


``` javascript
    export const performGet = async (url) => {
        try {
            // API call
            return await fetch('/choreo-apis/<api-suffix>');
        } catch (error) {
            if (error instanceof HttpError && error.status === 401) {
                // Re-login
                window.location.href = "/auth/login";
            } else {
                throw error;
            }
        }
    };
```

### Step 1.6: Set up a custom error page

You can set up Choreo's managed authentication to redirect to a customized error page within your web application by defining the error path in the configuration. In the event of an error during a redirection-based process, such as sign in or sign out, Choreo will automatically redirect the user to the designated custom error page.

!!! note
    If you have not configured an error path, Choreo's managed authentication will use its default error page whenever an error occurs.

Choreo's managed authentication will include the following query parameters in the URL when redirecting to the custom error page:

| Parameter      |  Description                                    |
|----------------|-------------------------------------------------|
| code           | A short textual error code indicating the error |
| message        | The description of the error                    |


Now have successfully implemented Choreo's managed authentication for your web application. The next step is to enable managed authentication for the component, and subsequently deploy it.

## Step 2: Enable managed authentication and configure the paths

To ensure that your web application functions seamlessly with managed authentication, it is essential to enable managed authentication for your web application component within Choreo.

You can enable managed authentication for your web application component at the time you deploy the component.

!!! tip
     Managed authentication is enabled by default when you create a web application using **React**, **Angular**, or **Vue.js** buildpacks.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). This opens the project home page.
2. In the **Component Listing** pane, click on the web application for which you want to enable managed authentication.
3. In the left navigation menu, click **Deploy**.
4. In the **Set Up** card, click **Configure & Deploy**.
5. Add the necessary configurations for your component if applicable and click **Next**.
6. Make sure **Managed Authentication with Choreo** toggle is enabled.
7. Specify appropriate values for the following fields:

    | Field            |  Description      | Default value      |
    | ----------------- | ----------------- | ----------------- |
    | Post Login Path   | The relative path that the application will be redirected to on successful sign-in. In your code, you must implement the necessary logic to obtain signed-in user's information from the `userinfo` cookie set by managed authentication. See **Obtain user information via the `userinfo` cookie** section in [Obtain user information claims](#step-12-obtain-user-information-claims). | /                      |
    | Post Logout Path  | The relative path to which Choreo redirects you on successful sign-out.  | /                      |
    | Error Path        | The relative path to which Choreo redirects you when an error occurs during a redirection-based flow (i.e., sign in or sign out). See [Set up a custom error page](#step-16-set-up-a-custom-error-page).             | Built-in error page     |
    | Session Expiry Time | The time in minutes after which the user session expires. For a seamless experience, the session expiry value should match the refresh token expiry time of the OIDC application in your identity provider.               | 10080 Minutes (7 Days)                   |
    | Additional Scopes | All additional scopes required by the web application. The `openid`, `profile`, and `email` scopes are added by default together with the scopes required to invoke subscribed APIs.               | none                   |

    !!! note
         If you need to change these configurations after you deploy the component, you can click **Authentication Settings** on the **Set Up** card, make the necessary changes, and deploy the component once again.

## Step 3: Configure the identity provider for the web application

You can configure your web application to work with the Choreo built-in identity provider, Asgardeo, or any external identity provider which supports OIDC/OAuth2.0 . 

!!! note
    The identity provider configured in this step should contain the users for the web application.

Click the respective tab for details depending on which identity provider you need to configure: 

=== "Configure Choreo built-in identity provider"

     Follow the steps given below to configure the built-in identity provider by generating authentication keys:

    !!! note
         Choreo built-in identity provider is configured by default. Therefore, this step is optional.

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Choreo Built-In Identity Provider**.
     5. Click **Generate Secret**. 

        !!! Note
             If the **Regenerate Secret** button is shown instead of the **Generate Secret** button, it indicates that OAuth keys are already generated for the component for the selected environment.

    !!! tip
        Refer to [Configure a User Store with the Built-In Identity Provider](../../administer/configure-a-user-store-with-built-in-idp/) for details on adding test users in Choreo built-in identity provider.

    !!! tip
        If you need to invoke APIs secured with role-based access control, you can test this within Choreo by creating roles for the application and mapping those roles to relevant permissions (scope) and user groups. For more information, see [create roles and assign permissions](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-2-create-roles-and-assign-permissions) and [assign roles to user groups](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-3-assign-roles-to-user-groups) sections in [Test Secure API Access with Choreo Built-In Security Token Service](../test-secure-api-access-with-choreo-built-in-security-token-service).

=== "Configure Asgardeo"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in Asgardeo**

     1. Sign in to [Asgardeo](https://console.asgardeo.io/).
     2. In the top navigation menu, click the **Organization** list and select your organization.
     3. In the Asgardeo Console left navigation menu, click **Applications**.
     4. Click **+ New Application**.
     5. Click **Standard-Based Application**.
     6. Specify a name for the application and select **OAuth2.0 OpenID Connect** as the protocol.
     7. Click **Register**.
     8. Click the **Protocol** tab and follow these steps:

         1. Select `Code` and `Refresh Token` as the **Allowed grant types**.
         2. Specify the following as **Authorized redirect URLs**:
             - [your-web-application-url]/auth/login/callback
             - [your-web-application-url]/auth/logout/callback
         3. Specify your web application URL under **Allowed origins**.
         4. In the **Access Token** section, select `JWT` as the **Token type**.
         5. Click **Update**. 

            !!! tip
                 If you need to invoke APIs secured with role-based access control, you must create roles in the application and map those roles to relevant permissions (scope). Then those roles should be assigned to user groups. For more information, see the [Asgardeo API authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/).

         6. Copy the **Client ID** and **Client Secret** of the application. You will need to use these values in the next step to link the OIDC/OAuth2.0 application to your Choreo component.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo web application component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Asgardeo - [your-org-name]**.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in Asgardeo. 
     6. Click **Add Keys**.

=== "Configure an external identity provider"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in the external identity provider**

     1. Create an OIDC/OAuth2.0 application in your external identity provider.
     2. Configure the OIDC/OAuth2.0 application as follows:

         1. Set `Code` and `Refresh Token` as allowed grant types.
         2. Add the following as authorized redirect URL.
         3. Specify the following as authorized redirect URLs:
         4. Specify the access token type as JWT.

            !!! tip
                 If you want to invoke APIs secured with role-based access control, you must ensure that users are assigned a role mapping that grants the necessary permission for API invocation. The approach of mapping application roles to users can vary depending on the identity provider.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select your identity provider.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in your external identity provider.
     6. Click **Add Keys**.


# Test Secure API Access with Choreo Built-In Security Token Service

API security can protect APIs from potential threats and vulnerabilities, with authentication and authorization playing key roles. Authentication ensures that only authorized users or applications can access the API. This involves using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization governs the actions permitted for authenticated users or applications within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions.

Choreo simplifies security testing for developers, allowing them to easily test APIs with permissions in non-critical environments. With its integrated security token service, Choreo provides authorization features that generate scopes based on the correlation between scopes, roles, and user groups. Developers can create roles, assign permissions, and set up user-group mappings using Choreo's built-in identity provider (IdP).

This guide walks you through the following steps to test the invocation of secured APIs with permissions using Choreo's built-in authorization capability:

- Assign scopes to an API in Choreo.
- Create roles and assign permissions in Choreo.
- Assign roles to user groups.
- Test the API invocation.
    - When Choreo manages the authentication (i.e., managed authentication enabled).
    - When the application independently handles the authentication (i.e., managed authentication disabled).

## Prerequisites

Before you try out this guide, ensure you have set up the following:

- Configure the Choreo built-in identity provider with users. For step-by-step instructions, see [Configure a User Store with the Built-In Identity Provider](../administer/configure-a-user-store-with-built-in-idp.md).
- Deploy and publish an API via Choreo. If you don't have an existing service in Choreo, you can either [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- A web application for API subscription. If you don't have an application in Choreo, you must [create a web application](../develop-components/develop-web-applications/build-and-deploy-a-single-page-web-application.md)
- Administrator rights in your Choreo organization. You need this access to configure role-group and role-permission mappings.

## Step 1: Assign permissions to an API in Choreo

You can provide fine-grained access control to your API resources with permissions. Follow the steps below to assign permissions to the resources in the API:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Project** list and select the project that contains your component.
3. In the **Component Listing** pane, click on the component for which you want to attach permissions.
4. In the left navigation menu, click **Deploy**.
5. On the **Deploy** page, go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.
6. Go to the **Permissions List** section and click **+ Add Permission(Scope)**.
7. In the **Permissions List** section, enter a permission value and click **+ Add New**.
8. Click the copy icon in front of the added permission to copy the fully qualified name of it. Save this value for future reference.
9. To attach permissions to a resource, click the **Select Permissions** list under the respective resource and select the permissions you want to attach.
10. Click **Apply**.
11. To apply the latest permissions to the deployed component, you must redeploy it. Follow the steps below to redeploy:
    1. Go to the **Set Up** card and click **Configure & Deploy**.
    2. In the **Configurations** pane that opens, click **Next**. This opens the **Endpoint Details** pane.
    3. Click **Deploy**.

12. To publish your API to the Choreo Developer Portal, follow the steps given below:
    1.  In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2.  Click **Publish**.

## Step 2: Create roles and assign permissions

The permissions assigned to your API need to be associated with roles. Follow the steps below to create roles and assign permissions to the roles.

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project that contains your component. 
2. In the left navigation menu, click **Settings**.
3. Click the **Application Security** tab.
4. Click **+ Role**.
5. Specify an appropriate **Role Name** and **Role description**. 
6. Select the permissions you want to assign to the role, and then click **Create**.
  
    !!!tip

            The permissions(scopes) defined for APIs exposed via components in the project and the permissions(scopes) required by connections created for components in the project are listed here. 

## Step 3: Assign roles to user groups

You must assign roles to the user groups defined in your Choreo built-in IdP to ensure that authenticated users can obtain access tokens with the required permissions.

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your component.
2. Click the **Application Security** tab and then click **Role Management**.
  
    !!!tip

            The roles defined within different projects in the organization are listed here.

3. Click **Map Groups** corresponding to a role that you want to assign to a group.
4. Specify a group name and enter to add it. You can add multiple groups if necessary.
5. Click **Save**.

## Step 4: Test the API invocation

To test an API invocation, you must first create a connection to your API. To do this, you must have a web application created. You can use the web application you created while setting up the prerequisites.

To create a connection to the web application, follow the steps given below:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project where you created the web application.
2. On the project home page, click the web application listed under **Component Listing**.
3. In the left navigation menu, click **Dependencies** and then click **Connections**.
4. Create a connection to the API you deployed in [Step 1](#step-1-assign-permissions-to-an-api-in-choreo). 
   
Now you can proceed to deploy the web application.

When deploying, if your web application is a single-page application (SPA), you have the option to allow Choreo to handle authentication on behalf of the application. This approach eliminates the need to incorporate OAuth protocol-specific logic into your application.

### Test the invocation when Choreo-managed authentication is enabled

If managed authentication is enabled for your web application, Choreo automatically handles obtaining the necessary permission for API invocation. This occurs during the request for access tokens, allowing you to seamlessly invoke the subscribed APIs through your web application without additional intervention. 

!!! note
    If you change the permissions of an existing connection or create a new connection with permissions, you must redeploy your web application to ensure proper API invocation with managed authentication.

### Test the invocation when the application manages the authentication

If your application manages authentication independently, follow the steps below to generate the necessary OAuth credentials to obtain access tokens:

1. In the left navigation menu, click **Settings**. This opens the settings of the web application component.
2. Click the **Authentication Keys** tab.
3. Click on an environment tab depending on the environment for which you want to generate credentials.
4. Select **Choreo Built-In Identity Provider** as the identity provider.
5. Click to expand **Advanced Configurations** and make sure the `code` and `refresh` grant types are selected. This is required to obtain access tokens with an authorization code grant.
6. Configure the callback URL of the web application to receive the authorization code.
7. Click **Update Configurations**.
8. Click **Regenerate Secret** and make a note of the client ID and secret that is generated.
9. Retrieve an access token using the authorization code grant, specifying the necessary OAuth scopes (You can see the endpoint details on the right side).
    - When prompted for authentication, enter the credentials of a user within the built-in identity provider (IdP) who possesses the required assigned groups.
    - Navigate through the OAuth flow to obtain the JWT access token.
10. Invoke the subscribed API using the access token.




# Configure Mutual TLS Between Components

Mutual transport layer security (mutual TLS) is a protocol that ensures privacy, integrity, and authentication of the data transmitted between two endpoints. In mutual TLS, the client and the server authenticate each other using digital certificates, establishing trust and verifying identities. Upon successful authentication, mutual TLS encrypts the data exchanged between the client and the server, preventing unauthorized access.

In Choreo, you can use mutual TLS to establish secure connections between components within a project.

!!! note
     If mutual TLS is not required, you can configure TLS instead. TLS provides a secure communication channel between a client and server but does not require the client to present a certificate to the server. This results in the absence of mutual authentication between the client and the server. While TLS ensures the confidentiality of data transmitted between the client and server, preventing unauthorized tampering, mutual TLS enhances TLS by introducing client-side authentication and facilitating mutual verification of identities between the client and server. 

     To configure TLS, you can follow the same steps as for mutual TLS as mentioned below, *without having to generate a client certificate*. The client only needs the root certificate to verify the server's identity.

## Generate certificates to establish mutual TLS

- **Root certificate:** Trusted by both the client and the server, this certificate is used to verify the authenticity of other certificates presented during the mutual TLS handshake process and to issue certificates for clients and servers. For a specific project, you can generate a single root certificate using a tool like OpenSSL.

- **Client certificate:** Contains the client’s identity for authentication. The common name (CN) in the certificate identifies the client. The generated client certificate must be signed by the root certificate.

- **Server certificate:** Clients use the server certificate to verify the trustworthiness of the server and establish a secure and authenticated connection. Similar to the client certificates, the server certificate must also be signed by the root certificate. When generating the server certificate, you must specify the server's hostname for the subject alternative name (SAN). You can obtain the hostname for the specific version of a service component from any project endpoint on the **Overview** page.

For example, if your project endpoint is `http://my-service-3781140846:7080/todos`, the hostname will be `my-service-3781140846`.

## Read mutual TLS certificates from your component

The approach to read mutual TLS certificates from a component can vary depending on its implementation. Typically, a component can read the certificate data from the file system or via an environment variable. For detailed instructions on adding environment variables and file mounts to your application, see [Manage Configurations and Secrets](../devops-and-ci-cd/manage-configurations-and-secrets.md).

!!! info
    When you specify a **private key**, ensure you **save it as a secret**.

## Sample for mutual TLS communication

For a sample that demonstrates how you can deploy services that communicate using mutual TLS, see [service-to-service-mtls](https://github.com/wso2/choreo-samples/tree/main/docker-service-to-service-mtls).


# Pass End-User Attributes to Upstream Services

There are scenarios where a backend service needs to apply specific logic or make decisions depending on the user consuming an API. In such scenarios, you must pass end-user attributes to the backend during an API call.

Choreo provides a method to send user information to a backend service through a JSON Web Token (JWT) in an HTTP header of an API request.

## How it works

The backend JWT contains claims transferred between the parties, such as the user and the backend. A claim can be metadata of the request or data about the user. A set of claims is called a dialect, for example, `http://wso2.org/claims`.

For each API request, a digitally signed JWT is carried to the backend service in the following format to ensure that the authenticity of the claims list is verified:

`{token header}.{claims list}.{signature}`

When a request goes through Choreo, the backend JWT is appended as the `X-JWT-Assertion` header in the outgoing message. The backend service fetches the JWT and retrieves the required information about the user, application, or token.

## Claims

Claims are fragments of information included in the JWT. 

The following is a sample claim set added to the end-user token for an access token generated via the authorization code:

!!! tip
    This access token is generated via Asgardeo using the authorization code grant type. Here, the Asgardeo application is configured to include the email claim in the token. 

``` java
{
  "sub": "11f53c32-f8ac-4810-bb79-615b2184baf5",
  "http://wso2.org/claims/apiname": "JWT Test - Endpoint 9090 803",
  "http://wso2.org/claims/applicationtier": "Unlimited",
  "http://wso2.org/claims/version": "1.0.0",
  "http://wso2.org/claims/keytype": "PRODUCTION",
  "iss": "wso2.org/products/am",
  "http://wso2.org/claims/applicationname": "jwtTest2",
  "http://wso2.org/claims/enduserTenantId": "0",
  "http://wso2.org/claims/applicationUUId": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "client_id": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "http://wso2.org/claims/subscriber": "5f4a7105-a889-4f92-9612-eef5bafe4eec",
  "azp": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "org_id": "b554e001-761c-4d3a-a7a6-a61d73d34221",
  "http://wso2.org/claims/tier": "Unlimited",
  "scope": "email openid profile",
  "exp": 1690537362,
  "http://wso2.org/claims/applicationid": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "http://wso2.org/claims/usertype": "Application_User",
  "org_name": "test",
  "iat": 1690533762,
  "email": "testmail@gmail.com",
  "jti": "69558555-d386-4a81-9ca0-0a23f809cd3c",
  "http://wso2.org/claims/apicontext": "/b554e001-761c-4d3a-a7a6-a61d73d34221/swog/jwt-test/endpoint-9090-803/1.0.0"
}
```

The following table describes the information contained in the sample JWT claims set given above:

|             **Claim Name**              |          **Description**           |  **Mandatory/Optional**  |
|-----------------------------------------|------------------------------------|--------------------------|
| `iat`                                   |  The time the token was issued.    |   Mandatory              |
| `jti`                                   |  The unique token identifier.      |   Mandatory              |
| `exp`                                   |  The token expiry time.            |   Mandatory              |
| `iss`                                   |  The issuer of the token.          |   Mandatory              |
| `http://wso2.org/claims/apiname`        |  The name of the API in Choreo.    |   Optional               |
| `http://wso2.org/claims/version`        |  The API version.                  |   Optional               |
| `http://wso2.org/claims/keytype`        |  The environment in Choreo that the API is in (`Development` or `production`).|   Optional |
| `http://wso2.org/claims/apicontext`     |  The API context in Choreo.        |   Optional               |
| `http://wso2.org/claims/subscriber`     |  The subscriber to the API, usually the app developer. |   Optional |
| `http://wso2.org/claims/applicationname`|  The application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationid`  |  The ID of the application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationUUId`|  The UUID of the application.      |   Optional               | 
| `client_id`                             |  The client identifier. This is copied from the original token.             |   Optional |
| `azp`                                   |  The authorized party (the party to which the ID token was issued). This is copied from the original token. |   Optional |
| `org_id`                                |  The organization ID. This is copied from the original token. |   Optional |
| `org_name`                              |  The organization name. This is copied from the original token. |   Optional |
| `http://wso2.org/claims/tier`           |  The tier/price band for the subscription. |   Optional       |
| `scope`                                 |  The scope of the token. This is copied from the original token. |   Optional |              
| `http://wso2.org/claims/usertype`       |  The type of application user whose action invoked the API. |   Optional |
| `email`                                 |  The email address of the user. This is copied from the original token. |   Optional |


!!! note

    The claims that get added to the end-user token can vary depending on the grant type used when generating the access token. For example, if you use the client-credentials grant type to generate the access token, the generated backend JWT would contain the following information:

    ``` java
    { 
      "http://wso2.org/claims/apiname": "DefaultAPI", 
      "http://wso2.org/claims/version": "1.0.0", 
      "http://wso2.org/claims/keytype": "PRODUCTION", 
      "iss": "wso2.org/products/am", 
      "http://wso2.org/claims/enduserTenantId": "0", 
      "exp": 1673245727, 
      "http://wso2.org/claims/usertype": "Application_User", 
      "iat": 1673242127, 
      "jti": "6e3f4392-8bd9-4900-9d08-eaab7429c510", 
      "http://wso2.org/claims/apicontext": "/9e71ab5e-6df5-4727-92d2-80ecf1a6218d/qbky/default/1.0.0" 
    }

    ```

To verify the authenticity of claims in a JWT, the claims must be validated using the public key corresponding to the private key used to sign the JWT.

JSON web key set (JWKS) is a set of keys to validate a JWT. It contains a collection of JSON web keys, which are public keys used to verify the signature of a JWT.

Typically, when a third party (such as an identity provider)issues a JWT and the recipient needs to verify its signature, they can use a JWKS. 
JWKS allows the issuer to rotate keys dynamically rather than hard-coding the public key in the application. The recipient can obtain the public key by accessing the JWKS endpoint.

## JWKS support in Choreo to validate the JWT

Choreo provides an endpoint to specify the public keys for backend JWT validation. Here are the endpoint URLs for the US East and EU regions:

- [https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks)
- [https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks)

!!! note
    For private data planes (PDPs), use the following JWKS endpoint URL template:
    
    `https://<PDP_GATEWAY_DOMAIN>/.wellknown/jwks`

    Be sure to replace `<PDP-GATEWAY-DOMAIN>` with the default domain configured to access the PDP APIs.

The endpoint provides one or more signing keys to validate the JWT.
The JSON web keys have a kid identifier that can be matched with the same property on the JWT to decide which key to use when validating.

The following is a sample JWKS response:

``` java
{
   "keys": [
       {
           "kty": "RSA",
           "e": "AQAB",
           "use": "sig",
           "kid": "ZjcwNmI2ZDJmNWQ0M2I5YzZiYzJmZmM4YjMwMDFlOTA4MGE3ZWZjZTMzNjU3YWU1MzViYjZkOTkzZjYzOGYyNg",
           "alg": "RS256",
           "n": "8vjeHzRhvpfMystncPnLBWy_t5F3eCxbcLbdugWnzfnIgaV6TWnqPBUagJBKpzRZs4A9Qja_ZrSVJjYsbARzCS_qiWp0Cdwkqn6ZCXpmbpfjYnKORq8N8M-zWaSZYbNvWJ5oSO4kH-LKWzODaFebwTJBpsR1vChHH95doxFuUjiZaisVaQgUJ6drRdlDtImp9r9EAX36YROuYFPoEJcvsH4_uuAR6ClJ12RE3M-YN4NTi1waVNvGbz43oNrpPy7SXgpizingxSGMqI6WU2ysRmk_f9ALgiPIpFDpufiCTYaIcRT-YcUyp9nMDlTRskMuD-dQ1sdJOa11P_yMs-glfQ"
       }
   ]
}
```

The following table describes the information contained in the JWKS response:

| **Property** |                                 **Description**                                    |  
|--------------|------------------------------------------------------------------------------------|
| `kty`        |  The cryptographic family to which the key belongs. <br> Choreo only supports RSA. |
| `e`          |  The exponent value of the public key.                                             |
| `use`        |  The purpose of the key. For example, whether it is for signing or encryption.     |
| `kid`        |  The identification parameter to match a specific key.                             |
| `alg`        |  The algorithm to use with the key.                                                |
| `n`          |  The modulus value of the public key.                                              |

## Enable passing end-user attributes to the backend

To enable passing end-user attributes to the backend through API calls via Choreo, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Components Listing** pane, click on the component for which you want to pass end-user attributes to the backend.
3. In the left navigation menu, click **Deploy**.
4. Go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.

    !!! note
         If the component is an API Proxy, go to the **Build Area** card and click **Security Settings**. This opens the **Security Settings** pane.
   
5. Select the **Pass Security Context To Backend** checkbox.
6. Optionally, specify appropriate audience values in the **End User Token Audiences** field. Specifying values restricts the JWT to the respective audiences, enabling the backend service to validate and confirm the intended recipients, including itself.

    !!! note
        The backend JWT does not include the audience field (aud) by default.

7. Click **Apply**.
8. To redeploy the component with the applied setting, go to the **Set Up** card and click **Deploy**.


# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Choreo as an external Identity Provider (IdP). This guide will walk you through setting up Choreo to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

- Assign scopes to an API in Choreo. 
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Choreo and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have a service in Choreo, [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- Deploy and publish your API. 

## Step 1: Assign scopes to an API in Choreo

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Manage** and then **Permissions**.
3. Click **+ Add Permission (Scope)**. 
4. In the **Permission List** pane, enter the permission value and click **+ Add New**.
5. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
6. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
7. Click **Save and Deploy**.
8. In the left navigation, click **Manage** and then **Lifecycle**.
9. Click **Publish** and continue to publish your API to the Choreo Developer Portal. 


## Step 2: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 3: Create an application in Choreo and enable external IdP authentication

Follow the steps below to consume the Choreo API and use an external IdP for authentication:

1. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name and description for the application. 
4. Click **Create**.
5. In the left navigation, under **Credentials** and click **Production**.
6. Select the **Identity Provider** as `Asgardeo`.
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - The Identity Provider dropdown is visible only to organizations where you have configured external IdPs. 

9. In the left navigation menu, click **Subscriptions**.
10. In the **Subscription Management** pane that opens, click **+ Add APIs**.
11. Select the API you assigned scopes to in [step 1](#step-1-assign-scopes-to-an-api-in-choreo) and click **Add**. 

## Step 4: Invoke the Choreo API with scopes

1. On the Choreo Developer Portal, go to your application. 
2. In the left navigation menu, under **Credentials** and click **Production**.
3. Under **Endpoints**, copy the **Token Endpoint** URL. 
4. Obtain an access token by invoking the token endpoint as follows:
   
    !!! note
        - If you are using the production credentials, you need to deploy your component(endpoint) to the production environment by promoting it from the development environment.
        - If you are using the sandbox credentials, you can use the endpoints deployed in the development environment.

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```



5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../testing/test-rest-endpoints-via-the-openapi-console.md) in Choreo by specifying the scope. 



# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

To establish secure communication between the Choreo Gateway and your backend, you can configure mutual TLS.

Mutual TLS authentication involves both the client and server validating each other’s certificates before establishing a connection. The following diagram depicts this scenario:

![Mutual TLS authentication](../assets/img/authentication-and-authorization/mutual-ssl-authentication.png)

## Configure mutual TLS to establish secure connectivity

To establish secure connectivity between the Choreo Gateway and your backend using mutual TLS, you must add the certificate of the backend (server certificate) to Choreo and add the certificate of Choreo (client certificate) as a trusted certificate in the backend.

### Step 1: Configure the backend certificate 

#### Prerequisites

- The endpoint must be protected with TLS. 
- The public certificate of the backend server should be extracted in PEM format and saved on the disk with the `.pem` extension.

To configure the backend certificate, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the API proxy for which you want to configure TLS. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
3. In the left navigation menu, click **Develop** and then click **Endpoints**.
4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
5. Click **Upload Endpoint Certificate**, and select the certificate file that you extracted in the prerequisites section to add it. This adds the certificate to all the environments as the default certificate for the endpoint. You can override this certificate if necessary when you deploy or promote the API.

### Step 2: Configure mutual TLS with the backend service

There are two approaches you can take to configure mutual TLS.

 - Generate a key pair with a self-signed certificate from Choreo, download the public certificate, and subsequently add and configure it in the backend.
 - Upload your own public or private certificate pair to Choreo. Subsequently, add and configure the public certificate of this key pair in your backend.

Follow the step-by-step instructions below depending on how you want to establish mutual TLS with the backend service:

=== "Generate a key pair through Choreo"
    When you follow these steps, Choreo generates a key pair with a self-signed certificate. You can attach this key pair to any API proxy created within the same project.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.    
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Generate new key pair** and specify a value as the common name for the certificate pair. This value will be used to identify the certificate.

        ![Generate new key pair](../assets/img/authentication-and-authorization/generate-new-key-pair.png)
       
    9. Optionally, click **Show advanced options** to expand the section and specify appropriate values for each of the fields.
    10. Click **Generate**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
    
    Now you can associate the certificate with the API and deploy the API.

=== "Use your own certificate pair"
    Here, you can use your own public certificate and private certificate as client certificates.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Use my own key pair**.

        ![Use own key pair](../assets/img/authentication-and-authorization/use-own-key-pair.png)
       
    9. Upload the private key and public certificate in PEM format or copy and paste the content of the private key and public certificate.
    10. Click **Add**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
   
    Now you can associate the certificate with the API and deploy the API.

### Step 3: Associate the certificate with the API

To associate a certificate with the API, follow the steps given below:

1. On the **Endpoints** page, go to the **Existing Certificates** section.
2. Select the certificate you want to associate with the API.

    ![Associate certificate](../assets/img/authentication-and-authorization/associate-certificate.png)

3. Click **Save**.
   
### Step 4: Deploy the API 

To deploy the API, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**.
3. Once the mediation application generation phase is complete, verify the endpoint URL populated for the environment and then click **Save & Deploy**.

Once the deployment is complete, you can [test the API](../testing/test-rest-endpoints-via-the-openapi-console.md). 

## Change the certificate for the production environment

If the API backend changes depending on the environment, the respective certificate must be updated for each environment. 

Here, let's take a look at the steps to update the certificate for the production environment:

1. On the **Deploy** page, go to the **Development** card and click **Promote**.
2. In the **Configurations** pane that opens, click **Endpoint Configuration**. You will see all applicable certificates listed in the **Mutual TLS** list. 
3. Select the certificate applicable to the production environment and click **Promote**. This promotes the component to the production environment with the selected certificate.


# Secure Web Applications with Managed Authentication

The managed authentication capability of Choreo simplifies adding authentication and authorization to a single-page web application.

As a developer, you can easily set up Choreo's managed authentication to seamlessly integrate authentication into your web application. You just need to enable Choreo’s managed authentication, configure the built-in identity provider, and connect to Choreo without having to deal with the complexities of underlying OIDC/OAuth2.0 protocols.

Choreo's managed authentication follows the backend for frontend (BFF) architecture, which is a secure pattern recommended for browser-based applications that utilize OIDC/OAuth2.0 for authentication and authorization. This architecture ensures that OAuth tokens remain secure from browser-side code, making them immune to potential attacks like cross-site scripting (XSS).

!!! note
     Choreo's managed authentication is currently available only for web applications created with **React**, **Angular**, or **Vue.js** buildpacks.

!!! warning
     Managed authentication uses the 'SAMESITE' cookie attribute to prevent CSRF attacks. Therefore, it is recommended to use managed authentication with modern browsers that support the 'SAMESITE' attribute.

## Step 1: Set up managed authentication for your web application

To secure your web application, you must implement authentication and authorization for it. 

To easily set up authentication for your web application with Choreo's managed authentication, follow the steps given below. Before you move on to the next section, see [Develop Web Applications Locally with Choreo’s Managed Authentication](../develop-components/develop-web-applications/develop-web-applications-locally-with-managed-authentication.md) to ensure a seamless authentication experience when developing your web application on your local machine. You can also refer to the [sample React app with managed authentication](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end-with-managed-auth).

### Step 1.1: Implement the sign-in functionality

To allow Choreo to manage the sign-in functionality for your web application, you must implement a sign-in button that redirects users to the `/auth/login` path on click. You can use the following code snippet or any custom button component from a preferred UI component library:

``` javascript
<button onClick={() => {window.location.href="/auth/login"}}>Login</button>
```

This code snippet works as follows:

When a user clicks sign in on your web application, Choreo will redirect the user to the configured identity provider and handle the authentication process, conforming to the OICD/OAuth2.0 protocols. On successful sign-in, Choreo will set the relevant session cookies and redirect the user to the post-sign-in path (default is `/`). The user can then invoke any Choreo-deployed APIs depending on the permission granted.

!!! note
    Refer to [configure the identity provider section](#step-3-configure-the-identity-provider-for-the-web-application) for details on configuring an identity provider for the web application. 

#### Optional: Pass additional query parameters to the identity provider 

If you want to pass additional query parameters to the identity provider, include them in the `/auth/login` request. Choreo appends these parameters to the `authorize` request sent to the identity provider.

For example,

``` javascript
<button onClick={() => {window.location.href="/auth/login?fidp=myfederatedidp"}}>Login</button>
```

### Step 1.2: Obtain user information claims

Choreo's managed authentication allows you to access user information claims that the identity provider returns post-sign-in, either via a cookie or by invoking a GET resource.


#### Obtain user information via the `userinfo` cookie

Upon successful sign-in, Choreo's managed authentication establishes a `userinfo` cookie that is accessible from the post-sign-in path you configured (by default, set to /). This `userinfo` cookie, provided by the identity provider, contains encoded user information claims.

!!! note
    - The `userinfo` cookie is intentionally set to have a short lifespan of only 2 minutes.
    - As a developer, you can decide how to utilize the user information that you retrieve. You must securely store the user information because the stored information can also serve as a means to verify the logged-in state of a user.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice. 

The recommended approach is to retrieve user information from the cookie and subsequently clear the cookie. The following is a sample code snippet that you can include in your post-sign-in path to retrieve user information from the cookie and subsequently clear the cookie:

``` javascript
    import Cookies from 'js-cookie';

    // Read userinfo cookie value.
    const encodedUserInfo = Cookies.get('userinfo')

    // Decode the value. 
    const userInfo = JSON.parse(atob(encodedUserInfo))

    // Store the value in a preferred browser-based storage if needed.

    // Clear the cookie.
    Cookies.remove('userinfo', { path: <post-login-path> })
```
#### Obtain user information via a GET endpoint

Choreo's managed authentication provides the GET endpoint `/auth/userinfo` in addition to the `userinfo` cookie that it sets after successful sign-in. You can use this endpoint to query information about users who have signed in. It also serves as a mechanism to check the state of a user who has signed in.

The following is an example of a request to this endpoint:

``` javascript
const response = await fetch('/auth/userinfo')
```

If a user has signed in, the server sends a `200 OK` response with the user information in JSON format in the response body. However, if the user is not signed in, the server sends a `401 Unauthorized` response.

### Step 1.3: Implement the sign-out functionality

To allow Choreo to manage the sign-out functionality of your web application, you can implement a sign-out button to redirect users to the `/auth/logout` path along with the `session_hint` cookie value on click. You can use the following code snippet or any custom button component from a preferred UI component library:

!!! note
    - It is recommended to clear any user information (if stored) at the time of sign-out.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice.   
    
``` javascript
<button onClick={async () => {
    window.location.href = `/auth/logout?session_hint=${Cookies.get('session_hint')}`;
}}>Logout</button>`
```

When a user clicks the sign-out button, Choreo will clear the session cookies and redirect the users to the OIDC logout endpoint of the configured identity provider (if available).  

### Step 1.4: Invoke APIs

To invoke Choreo APIs within the same organization as your web application, you can use the relative path `/choreo-apis/<api-suffix>`, regardless of whether managed authentication is enabled for the web application or not.

!!! note
    To invoke a Choreo API from a web application, you need to [create a Connection](../develop-components/sharing-and-reusing/create-a-connection.md) from the web application to the Choreo API. 

For example, if the API URL is `https://2d9ec1f6-2f04-4127-974f-0a3b20e97af5-dev.e1-us-east-azure.choreoapis.dev/rbln/item-service/api-e04/1.0.0`, the `<api-suffix>` would be `/rbln/item-service/api-e04/1.0.0`. You can invoke the API using the `/choreo-apis/rbln/item-service/api-e04/1.0.0` relative path from your single-page application.

!!! info
     To copy the exact service URL of a Connection, you can follow the steps given below:
      1. In the Choreo Console, go to the appropriate web application component.
      2. In the left navigation menu, click **Connections** under **Dependencies**.
      3. Click on the required Connection and copy the service URL.

If you enable Choreo's managed authentication, you don't have to manually add any logic to attach an access token to the API call because Choreo APIs accept the cookies set by Choreo's managed authentication. You can directly invoke the API as follows:

```
    const response = await fetch('/choreo-apis/<api-suffix>')
```

If Choreo's managed authentication is disabled, you must ensure that your web application attaches a valid access token to the API call.


### Step 1.5: Handle session expiry

When a user session exceeds the configured session expiry time, it automatically expires. A `401 Unauthorized` response status code for a Choreo API request from a logged-in user indicates that the session may have expired, requiring the user to re-login.

To programmatically handle session expiry and automatically re-login upon receiving a `401 Unauthorized` response from a Choreo API, you can encapsulate the request with re-login logic. The following sample code snippet shows how to wrap GET requests:


``` javascript
    export const performGet = async (url) => {
        try {
            // API call
            return await fetch('/choreo-apis/<api-suffix>');
        } catch (error) {
            if (error instanceof HttpError && error.status === 401) {
                // Re-login
                window.location.href = "/auth/login";
            } else {
                throw error;
            }
        }
    };
```

### Step 1.6: Set up a custom error page

You can set up Choreo's managed authentication to redirect to a customized error page within your web application by defining the error path in the configuration. In the event of an error during a redirection-based process, such as sign in or sign out, Choreo will automatically redirect the user to the designated custom error page.

!!! note
    If you have not configured an error path, Choreo's managed authentication will use its default error page whenever an error occurs.

Choreo's managed authentication will include the following query parameters in the URL when redirecting to the custom error page:

| Parameter      |  Description                                    |
|----------------|-------------------------------------------------|
| code           | A short textual error code indicating the error |
| message        | The description of the error                    |


Now have successfully implemented Choreo's managed authentication for your web application. The next step is to enable managed authentication for the component, and subsequently deploy it.

## Step 2: Enable managed authentication and configure the paths

To ensure that your web application functions seamlessly with managed authentication, it is essential to enable managed authentication for your web application component within Choreo.

You can enable managed authentication for your web application component at the time you deploy the component.

!!! tip
     Managed authentication is enabled by default when you create a web application using **React**, **Angular**, or **Vue.js** buildpacks.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). This opens the project home page.
2. In the **Component Listing** pane, click on the web application for which you want to enable managed authentication.
3. In the left navigation menu, click **Deploy**.
4. In the **Set Up** card, click **Configure & Deploy**.
5. Add the necessary configurations for your component if applicable and click **Next**.
6. Make sure **Managed Authentication with Choreo** toggle is enabled.
7. Specify appropriate values for the following fields:

    | Field            |  Description      | Default value      |
    | ----------------- | ----------------- | ----------------- |
    | Post Login Path   | The relative path that the application will be redirected to on successful sign-in. In your code, you must implement the necessary logic to obtain signed-in user's information from the `userinfo` cookie set by managed authentication. See **Obtain user information via the `userinfo` cookie** section in [Obtain user information claims](#step-12-obtain-user-information-claims). | /                      |
    | Post Logout Path  | The relative path to which Choreo redirects you on successful sign-out.  | /                      |
    | Error Path        | The relative path to which Choreo redirects you when an error occurs during a redirection-based flow (i.e., sign in or sign out). See [Set up a custom error page](#step-16-set-up-a-custom-error-page).             | Built-in error page     |
    | Session Expiry Time | The time in minutes after which the user session expires. For a seamless experience, the session expiry value should match the refresh token expiry time of the OIDC application in your identity provider.               | 10080 Minutes (7 Days)                   |
    | Additional Scopes | All additional scopes required by the web application. The `openid`, `profile`, and `email` scopes are added by default together with the scopes required to invoke subscribed APIs.               | none                   |

    !!! note
         If you need to change these configurations after you deploy the component, you can click **Authentication Settings** on the **Set Up** card, make the necessary changes, and deploy the component once again.

## Step 3: Configure the identity provider for the web application

You can configure your web application to work with the Choreo built-in identity provider, Asgardeo, or any external identity provider which supports OIDC/OAuth2.0 . 

!!! note
    The identity provider configured in this step should contain the users for the web application.

Click the respective tab for details depending on which identity provider you need to configure: 

=== "Configure Choreo built-in identity provider"

     Follow the steps given below to configure the built-in identity provider by generating authentication keys:

    !!! note
         Choreo built-in identity provider is configured by default. Therefore, this step is optional.

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Choreo Built-In Identity Provider**.
     5. Click **Generate Secret**. 

        !!! Note
             If the **Regenerate Secret** button is shown instead of the **Generate Secret** button, it indicates that OAuth keys are already generated for the component for the selected environment.

    !!! tip
        Refer to [Configure a User Store with the Built-In Identity Provider](../../administer/configure-a-user-store-with-built-in-idp/) for details on adding test users in Choreo built-in identity provider.

    !!! tip
        If you need to invoke APIs secured with role-based access control, you can test this within Choreo by creating roles for the application and mapping those roles to relevant permissions (scope) and user groups. For more information, see [create roles and assign permissions](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-2-create-roles-and-assign-permissions) and [assign roles to user groups](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-3-assign-roles-to-user-groups) sections in [Test Secure API Access with Choreo Built-In Security Token Service](../test-secure-api-access-with-choreo-built-in-security-token-service).

=== "Configure Asgardeo"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in Asgardeo**

     1. Sign in to [Asgardeo](https://console.asgardeo.io/).
     2. In the top navigation menu, click the **Organization** list and select your organization.
     3. In the Asgardeo Console left navigation menu, click **Applications**.
     4. Click **+ New Application**.
     5. Click **Standard-Based Application**.
     6. Specify a name for the application and select **OAuth2.0 OpenID Connect** as the protocol.
     7. Click **Register**.
     8. Click the **Protocol** tab and follow these steps:

         1. Select `Code` and `Refresh Token` as the **Allowed grant types**.
         2. Specify the following as **Authorized redirect URLs**:
             - [your-web-application-url]/auth/login/callback
             - [your-web-application-url]/auth/logout/callback
         3. Specify your web application URL under **Allowed origins**.
         4. In the **Access Token** section, select `JWT` as the **Token type**.
         5. Click **Update**. 

            !!! tip
                 If you need to invoke APIs secured with role-based access control, you must create roles in the application and map those roles to relevant permissions (scope). Then those roles should be assigned to user groups. For more information, see the [Asgardeo API authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/).

         6. Copy the **Client ID** and **Client Secret** of the application. You will need to use these values in the next step to link the OIDC/OAuth2.0 application to your Choreo component.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo web application component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Asgardeo - [your-org-name]**.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in Asgardeo. 
     6. Click **Add Keys**.

=== "Configure an external identity provider"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in the external identity provider**

     1. Create an OIDC/OAuth2.0 application in your external identity provider.
     2. Configure the OIDC/OAuth2.0 application as follows:

         1. Set `Code` and `Refresh Token` as allowed grant types.
         2. Add the following as authorized redirect URL.
         3. Specify the following as authorized redirect URLs:
         4. Specify the access token type as JWT.

            !!! tip
                 If you want to invoke APIs secured with role-based access control, you must ensure that users are assigned a role mapping that grants the necessary permission for API invocation. The approach of mapping application roles to users can vary depending on the identity provider.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select your identity provider.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in your external identity provider.
     6. Click **Add Keys**.


# Test Secure API Access with Choreo Built-In Security Token Service

API security can protect APIs from potential threats and vulnerabilities, with authentication and authorization playing key roles. Authentication ensures that only authorized users or applications can access the API. This involves using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization governs the actions permitted for authenticated users or applications within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions.

Choreo simplifies security testing for developers, allowing them to easily test APIs with permissions in non-critical environments. With its integrated security token service, Choreo provides authorization features that generate scopes based on the correlation between scopes, roles, and user groups. Developers can create roles, assign permissions, and set up user-group mappings using Choreo's built-in identity provider (IdP).

This guide walks you through the following steps to test the invocation of secured APIs with permissions using Choreo's built-in authorization capability:

- Assign scopes to an API in Choreo.
- Create roles and assign permissions in Choreo.
- Assign roles to user groups.
- Test the API invocation.
    - When Choreo manages the authentication (i.e., managed authentication enabled).
    - When the application independently handles the authentication (i.e., managed authentication disabled).

## Prerequisites

Before you try out this guide, ensure you have set up the following:

- Configure the Choreo built-in identity provider with users. For step-by-step instructions, see [Configure a User Store with the Built-In Identity Provider](../administer/configure-a-user-store-with-built-in-idp.md).
- Deploy and publish an API via Choreo. If you don't have an existing service in Choreo, you can either [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- A web application for API subscription. If you don't have an application in Choreo, you must [create a web application](../develop-components/develop-web-applications/build-and-deploy-a-single-page-web-application.md)
- Administrator rights in your Choreo organization. You need this access to configure role-group and role-permission mappings.

## Step 1: Assign permissions to an API in Choreo

You can provide fine-grained access control to your API resources with permissions. Follow the steps below to assign permissions to the resources in the API:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Project** list and select the project that contains your component.
3. In the **Component Listing** pane, click on the component for which you want to attach permissions.
4. In the left navigation menu, click **Deploy**.
5. On the **Deploy** page, go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.
6. Go to the **Permissions List** section and click **+ Add Permission(Scope)**.
7. In the **Permissions List** section, enter a permission value and click **+ Add New**.
8. Click the copy icon in front of the added permission to copy the fully qualified name of it. Save this value for future reference.
9. To attach permissions to a resource, click the **Select Permissions** list under the respective resource and select the permissions you want to attach.
10. Click **Apply**.
11. To apply the latest permissions to the deployed component, you must redeploy it. Follow the steps below to redeploy:
    1. Go to the **Set Up** card and click **Configure & Deploy**.
    2. In the **Configurations** pane that opens, click **Next**. This opens the **Endpoint Details** pane.
    3. Click **Deploy**.

12. To publish your API to the Choreo Developer Portal, follow the steps given below:
    1.  In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2.  Click **Publish**.

## Step 2: Create roles and assign permissions

The permissions assigned to your API need to be associated with roles. Follow the steps below to create roles and assign permissions to the roles.

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project that contains your component. 
2. In the left navigation menu, click **Settings**.
3. Click the **Application Security** tab.
4. Click **+ Role**.
5. Specify an appropriate **Role Name** and **Role description**. 
6. Select the permissions you want to assign to the role, and then click **Create**.
  
    !!!tip

            The permissions(scopes) defined for APIs exposed via components in the project and the permissions(scopes) required by connections created for components in the project are listed here. 

## Step 3: Assign roles to user groups

You must assign roles to the user groups defined in your Choreo built-in IdP to ensure that authenticated users can obtain access tokens with the required permissions.

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your component.
2. Click the **Application Security** tab and then click **Role Management**.
  
    !!!tip

            The roles defined within different projects in the organization are listed here.

3. Click **Map Groups** corresponding to a role that you want to assign to a group.
4. Specify a group name and enter to add it. You can add multiple groups if necessary.
5. Click **Save**.

## Step 4: Test the API invocation

To test an API invocation, you must first create a connection to your API. To do this, you must have a web application created. You can use the web application you created while setting up the prerequisites.

To create a connection to the web application, follow the steps given below:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project where you created the web application.
2. On the project home page, click the web application listed under **Component Listing**.
3. In the left navigation menu, click **Dependencies** and then click **Connections**.
4. Create a connection to the API you deployed in [Step 1](#step-1-assign-permissions-to-an-api-in-choreo). 
   
Now you can proceed to deploy the web application.

When deploying, if your web application is a single-page application (SPA), you have the option to allow Choreo to handle authentication on behalf of the application. This approach eliminates the need to incorporate OAuth protocol-specific logic into your application.

### Test the invocation when Choreo-managed authentication is enabled

If managed authentication is enabled for your web application, Choreo automatically handles obtaining the necessary permission for API invocation. This occurs during the request for access tokens, allowing you to seamlessly invoke the subscribed APIs through your web application without additional intervention. 

!!! note
    If you change the permissions of an existing connection or create a new connection with permissions, you must redeploy your web application to ensure proper API invocation with managed authentication.

### Test the invocation when the application manages the authentication

If your application manages authentication independently, follow the steps below to generate the necessary OAuth credentials to obtain access tokens:

1. In the left navigation menu, click **Settings**. This opens the settings of the web application component.
2. Click the **Authentication Keys** tab.
3. Click on an environment tab depending on the environment for which you want to generate credentials.
4. Select **Choreo Built-In Identity Provider** as the identity provider.
5. Click to expand **Advanced Configurations** and make sure the `code` and `refresh` grant types are selected. This is required to obtain access tokens with an authorization code grant.
6. Configure the callback URL of the web application to receive the authorization code.
7. Click **Update Configurations**.
8. Click **Regenerate Secret** and make a note of the client ID and secret that is generated.
9. Retrieve an access token using the authorization code grant, specifying the necessary OAuth scopes (You can see the endpoint details on the right side).
    - When prompted for authentication, enter the credentials of a user within the built-in identity provider (IdP) who possesses the required assigned groups.
    - Navigate through the OAuth flow to obtain the JWT access token.
10. Invoke the subscribed API using the access token.




# Configure Mutual TLS Between Components

Mutual transport layer security (mutual TLS) is a protocol that ensures privacy, integrity, and authentication of the data transmitted between two endpoints. In mutual TLS, the client and the server authenticate each other using digital certificates, establishing trust and verifying identities. Upon successful authentication, mutual TLS encrypts the data exchanged between the client and the server, preventing unauthorized access.

In Choreo, you can use mutual TLS to establish secure connections between components within a project.

!!! note
     If mutual TLS is not required, you can configure TLS instead. TLS provides a secure communication channel between a client and server but does not require the client to present a certificate to the server. This results in the absence of mutual authentication between the client and the server. While TLS ensures the confidentiality of data transmitted between the client and server, preventing unauthorized tampering, mutual TLS enhances TLS by introducing client-side authentication and facilitating mutual verification of identities between the client and server. 

     To configure TLS, you can follow the same steps as for mutual TLS as mentioned below, *without having to generate a client certificate*. The client only needs the root certificate to verify the server's identity.

## Generate certificates to establish mutual TLS

- **Root certificate:** Trusted by both the client and the server, this certificate is used to verify the authenticity of other certificates presented during the mutual TLS handshake process and to issue certificates for clients and servers. For a specific project, you can generate a single root certificate using a tool like OpenSSL.

- **Client certificate:** Contains the client’s identity for authentication. The common name (CN) in the certificate identifies the client. The generated client certificate must be signed by the root certificate.

- **Server certificate:** Clients use the server certificate to verify the trustworthiness of the server and establish a secure and authenticated connection. Similar to the client certificates, the server certificate must also be signed by the root certificate. When generating the server certificate, you must specify the server's hostname for the subject alternative name (SAN). You can obtain the hostname for the specific version of a service component from any project endpoint on the **Overview** page.

For example, if your project endpoint is `http://my-service-3781140846:7080/todos`, the hostname will be `my-service-3781140846`.

## Read mutual TLS certificates from your component

The approach to read mutual TLS certificates from a component can vary depending on its implementation. Typically, a component can read the certificate data from the file system or via an environment variable. For detailed instructions on adding environment variables and file mounts to your application, see [Manage Configurations and Secrets](../devops-and-ci-cd/manage-configurations-and-secrets.md).

!!! info
    When you specify a **private key**, ensure you **save it as a secret**.

## Sample for mutual TLS communication

For a sample that demonstrates how you can deploy services that communicate using mutual TLS, see [service-to-service-mtls](https://github.com/wso2/choreo-samples/tree/main/docker-service-to-service-mtls).


# Pass End-User Attributes to Upstream Services

There are scenarios where a backend service needs to apply specific logic or make decisions depending on the user consuming an API. In such scenarios, you must pass end-user attributes to the backend during an API call.

Choreo provides a method to send user information to a backend service through a JSON Web Token (JWT) in an HTTP header of an API request.

## How it works

The backend JWT contains claims transferred between the parties, such as the user and the backend. A claim can be metadata of the request or data about the user. A set of claims is called a dialect, for example, `http://wso2.org/claims`.

For each API request, a digitally signed JWT is carried to the backend service in the following format to ensure that the authenticity of the claims list is verified:

`{token header}.{claims list}.{signature}`

When a request goes through Choreo, the backend JWT is appended as the `X-JWT-Assertion` header in the outgoing message. The backend service fetches the JWT and retrieves the required information about the user, application, or token.

## Claims

Claims are fragments of information included in the JWT. 

The following is a sample claim set added to the end-user token for an access token generated via the authorization code:

!!! tip
    This access token is generated via Asgardeo using the authorization code grant type. Here, the Asgardeo application is configured to include the email claim in the token. 

``` java
{
  "sub": "11f53c32-f8ac-4810-bb79-615b2184baf5",
  "http://wso2.org/claims/apiname": "JWT Test - Endpoint 9090 803",
  "http://wso2.org/claims/applicationtier": "Unlimited",
  "http://wso2.org/claims/version": "1.0.0",
  "http://wso2.org/claims/keytype": "PRODUCTION",
  "iss": "wso2.org/products/am",
  "http://wso2.org/claims/applicationname": "jwtTest2",
  "http://wso2.org/claims/enduserTenantId": "0",
  "http://wso2.org/claims/applicationUUId": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "client_id": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "http://wso2.org/claims/subscriber": "5f4a7105-a889-4f92-9612-eef5bafe4eec",
  "azp": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "org_id": "b554e001-761c-4d3a-a7a6-a61d73d34221",
  "http://wso2.org/claims/tier": "Unlimited",
  "scope": "email openid profile",
  "exp": 1690537362,
  "http://wso2.org/claims/applicationid": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "http://wso2.org/claims/usertype": "Application_User",
  "org_name": "test",
  "iat": 1690533762,
  "email": "testmail@gmail.com",
  "jti": "69558555-d386-4a81-9ca0-0a23f809cd3c",
  "http://wso2.org/claims/apicontext": "/b554e001-761c-4d3a-a7a6-a61d73d34221/swog/jwt-test/endpoint-9090-803/1.0.0"
}
```

The following table describes the information contained in the sample JWT claims set given above:

|             **Claim Name**              |          **Description**           |  **Mandatory/Optional**  |
|-----------------------------------------|------------------------------------|--------------------------|
| `iat`                                   |  The time the token was issued.    |   Mandatory              |
| `jti`                                   |  The unique token identifier.      |   Mandatory              |
| `exp`                                   |  The token expiry time.            |   Mandatory              |
| `iss`                                   |  The issuer of the token.          |   Mandatory              |
| `http://wso2.org/claims/apiname`        |  The name of the API in Choreo.    |   Optional               |
| `http://wso2.org/claims/version`        |  The API version.                  |   Optional               |
| `http://wso2.org/claims/keytype`        |  The environment in Choreo that the API is in (`Development` or `production`).|   Optional |
| `http://wso2.org/claims/apicontext`     |  The API context in Choreo.        |   Optional               |
| `http://wso2.org/claims/subscriber`     |  The subscriber to the API, usually the app developer. |   Optional |
| `http://wso2.org/claims/applicationname`|  The application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationid`  |  The ID of the application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationUUId`|  The UUID of the application.      |   Optional               | 
| `client_id`                             |  The client identifier. This is copied from the original token.             |   Optional |
| `azp`                                   |  The authorized party (the party to which the ID token was issued). This is copied from the original token. |   Optional |
| `org_id`                                |  The organization ID. This is copied from the original token. |   Optional |
| `org_name`                              |  The organization name. This is copied from the original token. |   Optional |
| `http://wso2.org/claims/tier`           |  The tier/price band for the subscription. |   Optional       |
| `scope`                                 |  The scope of the token. This is copied from the original token. |   Optional |              
| `http://wso2.org/claims/usertype`       |  The type of application user whose action invoked the API. |   Optional |
| `email`                                 |  The email address of the user. This is copied from the original token. |   Optional |


!!! note

    The claims that get added to the end-user token can vary depending on the grant type used when generating the access token. For example, if you use the client-credentials grant type to generate the access token, the generated backend JWT would contain the following information:

    ``` java
    { 
      "http://wso2.org/claims/apiname": "DefaultAPI", 
      "http://wso2.org/claims/version": "1.0.0", 
      "http://wso2.org/claims/keytype": "PRODUCTION", 
      "iss": "wso2.org/products/am", 
      "http://wso2.org/claims/enduserTenantId": "0", 
      "exp": 1673245727, 
      "http://wso2.org/claims/usertype": "Application_User", 
      "iat": 1673242127, 
      "jti": "6e3f4392-8bd9-4900-9d08-eaab7429c510", 
      "http://wso2.org/claims/apicontext": "/9e71ab5e-6df5-4727-92d2-80ecf1a6218d/qbky/default/1.0.0" 
    }

    ```

To verify the authenticity of claims in a JWT, the claims must be validated using the public key corresponding to the private key used to sign the JWT.

JSON web key set (JWKS) is a set of keys to validate a JWT. It contains a collection of JSON web keys, which are public keys used to verify the signature of a JWT.

Typically, when a third party (such as an identity provider)issues a JWT and the recipient needs to verify its signature, they can use a JWKS. 
JWKS allows the issuer to rotate keys dynamically rather than hard-coding the public key in the application. The recipient can obtain the public key by accessing the JWKS endpoint.

## JWKS support in Choreo to validate the JWT

Choreo provides an endpoint to specify the public keys for backend JWT validation. Here are the endpoint URLs for the US East and EU regions:

- [https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks)
- [https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks)

!!! note
    For private data planes (PDPs), use the following JWKS endpoint URL template:
    
    `https://<PDP_GATEWAY_DOMAIN>/.wellknown/jwks`

    Be sure to replace `<PDP-GATEWAY-DOMAIN>` with the default domain configured to access the PDP APIs.

The endpoint provides one or more signing keys to validate the JWT.
The JSON web keys have a kid identifier that can be matched with the same property on the JWT to decide which key to use when validating.

The following is a sample JWKS response:

``` java
{
   "keys": [
       {
           "kty": "RSA",
           "e": "AQAB",
           "use": "sig",
           "kid": "ZjcwNmI2ZDJmNWQ0M2I5YzZiYzJmZmM4YjMwMDFlOTA4MGE3ZWZjZTMzNjU3YWU1MzViYjZkOTkzZjYzOGYyNg",
           "alg": "RS256",
           "n": "8vjeHzRhvpfMystncPnLBWy_t5F3eCxbcLbdugWnzfnIgaV6TWnqPBUagJBKpzRZs4A9Qja_ZrSVJjYsbARzCS_qiWp0Cdwkqn6ZCXpmbpfjYnKORq8N8M-zWaSZYbNvWJ5oSO4kH-LKWzODaFebwTJBpsR1vChHH95doxFuUjiZaisVaQgUJ6drRdlDtImp9r9EAX36YROuYFPoEJcvsH4_uuAR6ClJ12RE3M-YN4NTi1waVNvGbz43oNrpPy7SXgpizingxSGMqI6WU2ysRmk_f9ALgiPIpFDpufiCTYaIcRT-YcUyp9nMDlTRskMuD-dQ1sdJOa11P_yMs-glfQ"
       }
   ]
}
```

The following table describes the information contained in the JWKS response:

| **Property** |                                 **Description**                                    |  
|--------------|------------------------------------------------------------------------------------|
| `kty`        |  The cryptographic family to which the key belongs. <br> Choreo only supports RSA. |
| `e`          |  The exponent value of the public key.                                             |
| `use`        |  The purpose of the key. For example, whether it is for signing or encryption.     |
| `kid`        |  The identification parameter to match a specific key.                             |
| `alg`        |  The algorithm to use with the key.                                                |
| `n`          |  The modulus value of the public key.                                              |

## Enable passing end-user attributes to the backend

To enable passing end-user attributes to the backend through API calls via Choreo, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Components Listing** pane, click on the component for which you want to pass end-user attributes to the backend.
3. In the left navigation menu, click **Deploy**.
4. Go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.

    !!! note
         If the component is an API Proxy, go to the **Build Area** card and click **Security Settings**. This opens the **Security Settings** pane.
   
5. Select the **Pass Security Context To Backend** checkbox.
6. Optionally, specify appropriate audience values in the **End User Token Audiences** field. Specifying values restricts the JWT to the respective audiences, enabling the backend service to validate and confirm the intended recipients, including itself.

    !!! note
        The backend JWT does not include the audience field (aud) by default.

7. Click **Apply**.
8. To redeploy the component with the applied setting, go to the **Set Up** card and click **Deploy**.


# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Choreo as an external Identity Provider (IdP). This guide will walk you through setting up Choreo to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

- Assign scopes to an API in Choreo. 
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Choreo and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have a service in Choreo, [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- Deploy and publish your API. 

## Step 1: Assign scopes to an API in Choreo

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Manage** and then **Permissions**.
3. Click **+ Add Permission (Scope)**. 
4. In the **Permission List** pane, enter the permission value and click **+ Add New**.
5. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
6. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
7. Click **Save and Deploy**.
8. In the left navigation, click **Manage** and then **Lifecycle**.
9. Click **Publish** and continue to publish your API to the Choreo Developer Portal. 


## Step 2: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 3: Create an application in Choreo and enable external IdP authentication

Follow the steps below to consume the Choreo API and use an external IdP for authentication:

1. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name and description for the application. 
4. Click **Create**.
5. In the left navigation, under **Credentials** and click **Production**.
6. Select the **Identity Provider** as `Asgardeo`.
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - The Identity Provider dropdown is visible only to organizations where you have configured external IdPs. 

9. In the left navigation menu, click **Subscriptions**.
10. In the **Subscription Management** pane that opens, click **+ Add APIs**.
11. Select the API you assigned scopes to in [step 1](#step-1-assign-scopes-to-an-api-in-choreo) and click **Add**. 

## Step 4: Invoke the Choreo API with scopes

1. On the Choreo Developer Portal, go to your application. 
2. In the left navigation menu, under **Credentials** and click **Production**.
3. Under **Endpoints**, copy the **Token Endpoint** URL. 
4. Obtain an access token by invoking the token endpoint as follows:
   
    !!! note
        - If you are using the production credentials, you need to deploy your component(endpoint) to the production environment by promoting it from the development environment.
        - If you are using the sandbox credentials, you can use the endpoints deployed in the development environment.

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```



5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../testing/test-rest-endpoints-via-the-openapi-console.md) in Choreo by specifying the scope. 



# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

To establish secure communication between the Choreo Gateway and your backend, you can configure mutual TLS.

Mutual TLS authentication involves both the client and server validating each other’s certificates before establishing a connection. The following diagram depicts this scenario:

![Mutual TLS authentication](../assets/img/authentication-and-authorization/mutual-ssl-authentication.png)

## Configure mutual TLS to establish secure connectivity

To establish secure connectivity between the Choreo Gateway and your backend using mutual TLS, you must add the certificate of the backend (server certificate) to Choreo and add the certificate of Choreo (client certificate) as a trusted certificate in the backend.

### Step 1: Configure the backend certificate 

#### Prerequisites

- The endpoint must be protected with TLS. 
- The public certificate of the backend server should be extracted in PEM format and saved on the disk with the `.pem` extension.

To configure the backend certificate, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the API proxy for which you want to configure TLS. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
3. In the left navigation menu, click **Develop** and then click **Endpoints**.
4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
5. Click **Upload Endpoint Certificate**, and select the certificate file that you extracted in the prerequisites section to add it. This adds the certificate to all the environments as the default certificate for the endpoint. You can override this certificate if necessary when you deploy or promote the API.

### Step 2: Configure mutual TLS with the backend service

There are two approaches you can take to configure mutual TLS.

 - Generate a key pair with a self-signed certificate from Choreo, download the public certificate, and subsequently add and configure it in the backend.
 - Upload your own public or private certificate pair to Choreo. Subsequently, add and configure the public certificate of this key pair in your backend.

Follow the step-by-step instructions below depending on how you want to establish mutual TLS with the backend service:

=== "Generate a key pair through Choreo"
    When you follow these steps, Choreo generates a key pair with a self-signed certificate. You can attach this key pair to any API proxy created within the same project.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.    
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Generate new key pair** and specify a value as the common name for the certificate pair. This value will be used to identify the certificate.

        ![Generate new key pair](../assets/img/authentication-and-authorization/generate-new-key-pair.png)
       
    9. Optionally, click **Show advanced options** to expand the section and specify appropriate values for each of the fields.
    10. Click **Generate**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
    
    Now you can associate the certificate with the API and deploy the API.

=== "Use your own certificate pair"
    Here, you can use your own public certificate and private certificate as client certificates.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Use my own key pair**.

        ![Use own key pair](../assets/img/authentication-and-authorization/use-own-key-pair.png)
       
    9. Upload the private key and public certificate in PEM format or copy and paste the content of the private key and public certificate.
    10. Click **Add**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
   
    Now you can associate the certificate with the API and deploy the API.

### Step 3: Associate the certificate with the API

To associate a certificate with the API, follow the steps given below:

1. On the **Endpoints** page, go to the **Existing Certificates** section.
2. Select the certificate you want to associate with the API.

    ![Associate certificate](../assets/img/authentication-and-authorization/associate-certificate.png)

3. Click **Save**.
   
### Step 4: Deploy the API 

To deploy the API, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**.
3. Once the mediation application generation phase is complete, verify the endpoint URL populated for the environment and then click **Save & Deploy**.

Once the deployment is complete, you can [test the API](../testing/test-rest-endpoints-via-the-openapi-console.md). 

## Change the certificate for the production environment

If the API backend changes depending on the environment, the respective certificate must be updated for each environment. 

Here, let's take a look at the steps to update the certificate for the production environment:

1. On the **Deploy** page, go to the **Development** card and click **Promote**.
2. In the **Configurations** pane that opens, click **Endpoint Configuration**. You will see all applicable certificates listed in the **Mutual TLS** list. 
3. Select the certificate applicable to the production environment and click **Promote**. This promotes the component to the production environment with the selected certificate.


# Secure Web Applications with Managed Authentication

The managed authentication capability of Choreo simplifies adding authentication and authorization to a single-page web application.

As a developer, you can easily set up Choreo's managed authentication to seamlessly integrate authentication into your web application. You just need to enable Choreo’s managed authentication, configure the built-in identity provider, and connect to Choreo without having to deal with the complexities of underlying OIDC/OAuth2.0 protocols.

Choreo's managed authentication follows the backend for frontend (BFF) architecture, which is a secure pattern recommended for browser-based applications that utilize OIDC/OAuth2.0 for authentication and authorization. This architecture ensures that OAuth tokens remain secure from browser-side code, making them immune to potential attacks like cross-site scripting (XSS).

!!! note
     Choreo's managed authentication is currently available only for web applications created with **React**, **Angular**, or **Vue.js** buildpacks.

!!! warning
     Managed authentication uses the 'SAMESITE' cookie attribute to prevent CSRF attacks. Therefore, it is recommended to use managed authentication with modern browsers that support the 'SAMESITE' attribute.

## Step 1: Set up managed authentication for your web application

To secure your web application, you must implement authentication and authorization for it. 

To easily set up authentication for your web application with Choreo's managed authentication, follow the steps given below. Before you move on to the next section, see [Develop Web Applications Locally with Choreo’s Managed Authentication](../develop-components/develop-web-applications/develop-web-applications-locally-with-managed-authentication.md) to ensure a seamless authentication experience when developing your web application on your local machine. You can also refer to the [sample React app with managed authentication](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end-with-managed-auth).

### Step 1.1: Implement the sign-in functionality

To allow Choreo to manage the sign-in functionality for your web application, you must implement a sign-in button that redirects users to the `/auth/login` path on click. You can use the following code snippet or any custom button component from a preferred UI component library:

``` javascript
<button onClick={() => {window.location.href="/auth/login"}}>Login</button>
```

This code snippet works as follows:

When a user clicks sign in on your web application, Choreo will redirect the user to the configured identity provider and handle the authentication process, conforming to the OICD/OAuth2.0 protocols. On successful sign-in, Choreo will set the relevant session cookies and redirect the user to the post-sign-in path (default is `/`). The user can then invoke any Choreo-deployed APIs depending on the permission granted.

!!! note
    Refer to [configure the identity provider section](#step-3-configure-the-identity-provider-for-the-web-application) for details on configuring an identity provider for the web application. 

#### Optional: Pass additional query parameters to the identity provider 

If you want to pass additional query parameters to the identity provider, include them in the `/auth/login` request. Choreo appends these parameters to the `authorize` request sent to the identity provider.

For example,

``` javascript
<button onClick={() => {window.location.href="/auth/login?fidp=myfederatedidp"}}>Login</button>
```

### Step 1.2: Obtain user information claims

Choreo's managed authentication allows you to access user information claims that the identity provider returns post-sign-in, either via a cookie or by invoking a GET resource.


#### Obtain user information via the `userinfo` cookie

Upon successful sign-in, Choreo's managed authentication establishes a `userinfo` cookie that is accessible from the post-sign-in path you configured (by default, set to /). This `userinfo` cookie, provided by the identity provider, contains encoded user information claims.

!!! note
    - The `userinfo` cookie is intentionally set to have a short lifespan of only 2 minutes.
    - As a developer, you can decide how to utilize the user information that you retrieve. You must securely store the user information because the stored information can also serve as a means to verify the logged-in state of a user.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice. 

The recommended approach is to retrieve user information from the cookie and subsequently clear the cookie. The following is a sample code snippet that you can include in your post-sign-in path to retrieve user information from the cookie and subsequently clear the cookie:

``` javascript
    import Cookies from 'js-cookie';

    // Read userinfo cookie value.
    const encodedUserInfo = Cookies.get('userinfo')

    // Decode the value. 
    const userInfo = JSON.parse(atob(encodedUserInfo))

    // Store the value in a preferred browser-based storage if needed.

    // Clear the cookie.
    Cookies.remove('userinfo', { path: <post-login-path> })
```
#### Obtain user information via a GET endpoint

Choreo's managed authentication provides the GET endpoint `/auth/userinfo` in addition to the `userinfo` cookie that it sets after successful sign-in. You can use this endpoint to query information about users who have signed in. It also serves as a mechanism to check the state of a user who has signed in.

The following is an example of a request to this endpoint:

``` javascript
const response = await fetch('/auth/userinfo')
```

If a user has signed in, the server sends a `200 OK` response with the user information in JSON format in the response body. However, if the user is not signed in, the server sends a `401 Unauthorized` response.

### Step 1.3: Implement the sign-out functionality

To allow Choreo to manage the sign-out functionality of your web application, you can implement a sign-out button to redirect users to the `/auth/logout` path along with the `session_hint` cookie value on click. You can use the following code snippet or any custom button component from a preferred UI component library:

!!! note
    - It is recommended to clear any user information (if stored) at the time of sign-out.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice.   
    
``` javascript
<button onClick={async () => {
    window.location.href = `/auth/logout?session_hint=${Cookies.get('session_hint')}`;
}}>Logout</button>`
```

When a user clicks the sign-out button, Choreo will clear the session cookies and redirect the users to the OIDC logout endpoint of the configured identity provider (if available).  

### Step 1.4: Invoke APIs

To invoke Choreo APIs within the same organization as your web application, you can use the relative path `/choreo-apis/<api-suffix>`, regardless of whether managed authentication is enabled for the web application or not.

!!! note
    To invoke a Choreo API from a web application, you need to [create a Connection](../develop-components/sharing-and-reusing/create-a-connection.md) from the web application to the Choreo API. 

For example, if the API URL is `https://2d9ec1f6-2f04-4127-974f-0a3b20e97af5-dev.e1-us-east-azure.choreoapis.dev/rbln/item-service/api-e04/1.0.0`, the `<api-suffix>` would be `/rbln/item-service/api-e04/1.0.0`. You can invoke the API using the `/choreo-apis/rbln/item-service/api-e04/1.0.0` relative path from your single-page application.

!!! info
     To copy the exact service URL of a Connection, you can follow the steps given below:
      1. In the Choreo Console, go to the appropriate web application component.
      2. In the left navigation menu, click **Connections** under **Dependencies**.
      3. Click on the required Connection and copy the service URL.

If you enable Choreo's managed authentication, you don't have to manually add any logic to attach an access token to the API call because Choreo APIs accept the cookies set by Choreo's managed authentication. You can directly invoke the API as follows:

```
    const response = await fetch('/choreo-apis/<api-suffix>')
```

If Choreo's managed authentication is disabled, you must ensure that your web application attaches a valid access token to the API call.


### Step 1.5: Handle session expiry

When a user session exceeds the configured session expiry time, it automatically expires. A `401 Unauthorized` response status code for a Choreo API request from a logged-in user indicates that the session may have expired, requiring the user to re-login.

To programmatically handle session expiry and automatically re-login upon receiving a `401 Unauthorized` response from a Choreo API, you can encapsulate the request with re-login logic. The following sample code snippet shows how to wrap GET requests:


``` javascript
    export const performGet = async (url) => {
        try {
            // API call
            return await fetch('/choreo-apis/<api-suffix>');
        } catch (error) {
            if (error instanceof HttpError && error.status === 401) {
                // Re-login
                window.location.href = "/auth/login";
            } else {
                throw error;
            }
        }
    };
```

### Step 1.6: Set up a custom error page

You can set up Choreo's managed authentication to redirect to a customized error page within your web application by defining the error path in the configuration. In the event of an error during a redirection-based process, such as sign in or sign out, Choreo will automatically redirect the user to the designated custom error page.

!!! note
    If you have not configured an error path, Choreo's managed authentication will use its default error page whenever an error occurs.

Choreo's managed authentication will include the following query parameters in the URL when redirecting to the custom error page:

| Parameter      |  Description                                    |
|----------------|-------------------------------------------------|
| code           | A short textual error code indicating the error |
| message        | The description of the error                    |


Now have successfully implemented Choreo's managed authentication for your web application. The next step is to enable managed authentication for the component, and subsequently deploy it.

## Step 2: Enable managed authentication and configure the paths

To ensure that your web application functions seamlessly with managed authentication, it is essential to enable managed authentication for your web application component within Choreo.

You can enable managed authentication for your web application component at the time you deploy the component.

!!! tip
     Managed authentication is enabled by default when you create a web application using **React**, **Angular**, or **Vue.js** buildpacks.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). This opens the project home page.
2. In the **Component Listing** pane, click on the web application for which you want to enable managed authentication.
3. In the left navigation menu, click **Deploy**.
4. In the **Set Up** card, click **Configure & Deploy**.
5. Add the necessary configurations for your component if applicable and click **Next**.
6. Make sure **Managed Authentication with Choreo** toggle is enabled.
7. Specify appropriate values for the following fields:

    | Field            |  Description      | Default value      |
    | ----------------- | ----------------- | ----------------- |
    | Post Login Path   | The relative path that the application will be redirected to on successful sign-in. In your code, you must implement the necessary logic to obtain signed-in user's information from the `userinfo` cookie set by managed authentication. See **Obtain user information via the `userinfo` cookie** section in [Obtain user information claims](#step-12-obtain-user-information-claims). | /                      |
    | Post Logout Path  | The relative path to which Choreo redirects you on successful sign-out.  | /                      |
    | Error Path        | The relative path to which Choreo redirects you when an error occurs during a redirection-based flow (i.e., sign in or sign out). See [Set up a custom error page](#step-16-set-up-a-custom-error-page).             | Built-in error page     |
    | Session Expiry Time | The time in minutes after which the user session expires. For a seamless experience, the session expiry value should match the refresh token expiry time of the OIDC application in your identity provider.               | 10080 Minutes (7 Days)                   |
    | Additional Scopes | All additional scopes required by the web application. The `openid`, `profile`, and `email` scopes are added by default together with the scopes required to invoke subscribed APIs.               | none                   |

    !!! note
         If you need to change these configurations after you deploy the component, you can click **Authentication Settings** on the **Set Up** card, make the necessary changes, and deploy the component once again.

## Step 3: Configure the identity provider for the web application

You can configure your web application to work with the Choreo built-in identity provider, Asgardeo, or any external identity provider which supports OIDC/OAuth2.0 . 

!!! note
    The identity provider configured in this step should contain the users for the web application.

Click the respective tab for details depending on which identity provider you need to configure: 

=== "Configure Choreo built-in identity provider"

     Follow the steps given below to configure the built-in identity provider by generating authentication keys:

    !!! note
         Choreo built-in identity provider is configured by default. Therefore, this step is optional.

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Choreo Built-In Identity Provider**.
     5. Click **Generate Secret**. 

        !!! Note
             If the **Regenerate Secret** button is shown instead of the **Generate Secret** button, it indicates that OAuth keys are already generated for the component for the selected environment.

    !!! tip
        Refer to [Configure a User Store with the Built-In Identity Provider](../../administer/configure-a-user-store-with-built-in-idp/) for details on adding test users in Choreo built-in identity provider.

    !!! tip
        If you need to invoke APIs secured with role-based access control, you can test this within Choreo by creating roles for the application and mapping those roles to relevant permissions (scope) and user groups. For more information, see [create roles and assign permissions](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-2-create-roles-and-assign-permissions) and [assign roles to user groups](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-3-assign-roles-to-user-groups) sections in [Test Secure API Access with Choreo Built-In Security Token Service](../test-secure-api-access-with-choreo-built-in-security-token-service).

=== "Configure Asgardeo"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in Asgardeo**

     1. Sign in to [Asgardeo](https://console.asgardeo.io/).
     2. In the top navigation menu, click the **Organization** list and select your organization.
     3. In the Asgardeo Console left navigation menu, click **Applications**.
     4. Click **+ New Application**.
     5. Click **Standard-Based Application**.
     6. Specify a name for the application and select **OAuth2.0 OpenID Connect** as the protocol.
     7. Click **Register**.
     8. Click the **Protocol** tab and follow these steps:

         1. Select `Code` and `Refresh Token` as the **Allowed grant types**.
         2. Specify the following as **Authorized redirect URLs**:
             - [your-web-application-url]/auth/login/callback
             - [your-web-application-url]/auth/logout/callback
         3. Specify your web application URL under **Allowed origins**.
         4. In the **Access Token** section, select `JWT` as the **Token type**.
         5. Click **Update**. 

            !!! tip
                 If you need to invoke APIs secured with role-based access control, you must create roles in the application and map those roles to relevant permissions (scope). Then those roles should be assigned to user groups. For more information, see the [Asgardeo API authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/).

         6. Copy the **Client ID** and **Client Secret** of the application. You will need to use these values in the next step to link the OIDC/OAuth2.0 application to your Choreo component.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo web application component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Asgardeo - [your-org-name]**.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in Asgardeo. 
     6. Click **Add Keys**.

=== "Configure an external identity provider"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in the external identity provider**

     1. Create an OIDC/OAuth2.0 application in your external identity provider.
     2. Configure the OIDC/OAuth2.0 application as follows:

         1. Set `Code` and `Refresh Token` as allowed grant types.
         2. Add the following as authorized redirect URL.
         3. Specify the following as authorized redirect URLs:
         4. Specify the access token type as JWT.

            !!! tip
                 If you want to invoke APIs secured with role-based access control, you must ensure that users are assigned a role mapping that grants the necessary permission for API invocation. The approach of mapping application roles to users can vary depending on the identity provider.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select your identity provider.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in your external identity provider.
     6. Click **Add Keys**.


# Test Secure API Access with Choreo Built-In Security Token Service

API security can protect APIs from potential threats and vulnerabilities, with authentication and authorization playing key roles. Authentication ensures that only authorized users or applications can access the API. This involves using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization governs the actions permitted for authenticated users or applications within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions.

Choreo simplifies security testing for developers, allowing them to easily test APIs with permissions in non-critical environments. With its integrated security token service, Choreo provides authorization features that generate scopes based on the correlation between scopes, roles, and user groups. Developers can create roles, assign permissions, and set up user-group mappings using Choreo's built-in identity provider (IdP).

This guide walks you through the following steps to test the invocation of secured APIs with permissions using Choreo's built-in authorization capability:

- Assign scopes to an API in Choreo.
- Create roles and assign permissions in Choreo.
- Assign roles to user groups.
- Test the API invocation.
    - When Choreo manages the authentication (i.e., managed authentication enabled).
    - When the application independently handles the authentication (i.e., managed authentication disabled).

## Prerequisites

Before you try out this guide, ensure you have set up the following:

- Configure the Choreo built-in identity provider with users. For step-by-step instructions, see [Configure a User Store with the Built-In Identity Provider](../administer/configure-a-user-store-with-built-in-idp.md).
- Deploy and publish an API via Choreo. If you don't have an existing service in Choreo, you can either [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- A web application for API subscription. If you don't have an application in Choreo, you must [create a web application](../develop-components/develop-web-applications/build-and-deploy-a-single-page-web-application.md)
- Administrator rights in your Choreo organization. You need this access to configure role-group and role-permission mappings.

## Step 1: Assign permissions to an API in Choreo

You can provide fine-grained access control to your API resources with permissions. Follow the steps below to assign permissions to the resources in the API:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Project** list and select the project that contains your component.
3. In the **Component Listing** pane, click on the component for which you want to attach permissions.
4. In the left navigation menu, click **Deploy**.
5. On the **Deploy** page, go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.
6. Go to the **Permissions List** section and click **+ Add Permission(Scope)**.
7. In the **Permissions List** section, enter a permission value and click **+ Add New**.
8. Click the copy icon in front of the added permission to copy the fully qualified name of it. Save this value for future reference.
9. To attach permissions to a resource, click the **Select Permissions** list under the respective resource and select the permissions you want to attach.
10. Click **Apply**.
11. To apply the latest permissions to the deployed component, you must redeploy it. Follow the steps below to redeploy:
    1. Go to the **Set Up** card and click **Configure & Deploy**.
    2. In the **Configurations** pane that opens, click **Next**. This opens the **Endpoint Details** pane.
    3. Click **Deploy**.

12. To publish your API to the Choreo Developer Portal, follow the steps given below:
    1.  In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2.  Click **Publish**.

## Step 2: Create roles and assign permissions

The permissions assigned to your API need to be associated with roles. Follow the steps below to create roles and assign permissions to the roles.

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project that contains your component. 
2. In the left navigation menu, click **Settings**.
3. Click the **Application Security** tab.
4. Click **+ Role**.
5. Specify an appropriate **Role Name** and **Role description**. 
6. Select the permissions you want to assign to the role, and then click **Create**.
  
    !!!tip

            The permissions(scopes) defined for APIs exposed via components in the project and the permissions(scopes) required by connections created for components in the project are listed here. 

## Step 3: Assign roles to user groups

You must assign roles to the user groups defined in your Choreo built-in IdP to ensure that authenticated users can obtain access tokens with the required permissions.

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your component.
2. Click the **Application Security** tab and then click **Role Management**.
  
    !!!tip

            The roles defined within different projects in the organization are listed here.

3. Click **Map Groups** corresponding to a role that you want to assign to a group.
4. Specify a group name and enter to add it. You can add multiple groups if necessary.
5. Click **Save**.

## Step 4: Test the API invocation

To test an API invocation, you must first create a connection to your API. To do this, you must have a web application created. You can use the web application you created while setting up the prerequisites.

To create a connection to the web application, follow the steps given below:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project where you created the web application.
2. On the project home page, click the web application listed under **Component Listing**.
3. In the left navigation menu, click **Dependencies** and then click **Connections**.
4. Create a connection to the API you deployed in [Step 1](#step-1-assign-permissions-to-an-api-in-choreo). 
   
Now you can proceed to deploy the web application.

When deploying, if your web application is a single-page application (SPA), you have the option to allow Choreo to handle authentication on behalf of the application. This approach eliminates the need to incorporate OAuth protocol-specific logic into your application.

### Test the invocation when Choreo-managed authentication is enabled

If managed authentication is enabled for your web application, Choreo automatically handles obtaining the necessary permission for API invocation. This occurs during the request for access tokens, allowing you to seamlessly invoke the subscribed APIs through your web application without additional intervention. 

!!! note
    If you change the permissions of an existing connection or create a new connection with permissions, you must redeploy your web application to ensure proper API invocation with managed authentication.

### Test the invocation when the application manages the authentication

If your application manages authentication independently, follow the steps below to generate the necessary OAuth credentials to obtain access tokens:

1. In the left navigation menu, click **Settings**. This opens the settings of the web application component.
2. Click the **Authentication Keys** tab.
3. Click on an environment tab depending on the environment for which you want to generate credentials.
4. Select **Choreo Built-In Identity Provider** as the identity provider.
5. Click to expand **Advanced Configurations** and make sure the `code` and `refresh` grant types are selected. This is required to obtain access tokens with an authorization code grant.
6. Configure the callback URL of the web application to receive the authorization code.
7. Click **Update Configurations**.
8. Click **Regenerate Secret** and make a note of the client ID and secret that is generated.
9. Retrieve an access token using the authorization code grant, specifying the necessary OAuth scopes (You can see the endpoint details on the right side).
    - When prompted for authentication, enter the credentials of a user within the built-in identity provider (IdP) who possesses the required assigned groups.
    - Navigate through the OAuth flow to obtain the JWT access token.
10. Invoke the subscribed API using the access token.




# Configure Mutual TLS Between Components

Mutual transport layer security (mutual TLS) is a protocol that ensures privacy, integrity, and authentication of the data transmitted between two endpoints. In mutual TLS, the client and the server authenticate each other using digital certificates, establishing trust and verifying identities. Upon successful authentication, mutual TLS encrypts the data exchanged between the client and the server, preventing unauthorized access.

In Choreo, you can use mutual TLS to establish secure connections between components within a project.

!!! note
     If mutual TLS is not required, you can configure TLS instead. TLS provides a secure communication channel between a client and server but does not require the client to present a certificate to the server. This results in the absence of mutual authentication between the client and the server. While TLS ensures the confidentiality of data transmitted between the client and server, preventing unauthorized tampering, mutual TLS enhances TLS by introducing client-side authentication and facilitating mutual verification of identities between the client and server. 

     To configure TLS, you can follow the same steps as for mutual TLS as mentioned below, *without having to generate a client certificate*. The client only needs the root certificate to verify the server's identity.

## Generate certificates to establish mutual TLS

- **Root certificate:** Trusted by both the client and the server, this certificate is used to verify the authenticity of other certificates presented during the mutual TLS handshake process and to issue certificates for clients and servers. For a specific project, you can generate a single root certificate using a tool like OpenSSL.

- **Client certificate:** Contains the client’s identity for authentication. The common name (CN) in the certificate identifies the client. The generated client certificate must be signed by the root certificate.

- **Server certificate:** Clients use the server certificate to verify the trustworthiness of the server and establish a secure and authenticated connection. Similar to the client certificates, the server certificate must also be signed by the root certificate. When generating the server certificate, you must specify the server's hostname for the subject alternative name (SAN). You can obtain the hostname for the specific version of a service component from any project endpoint on the **Overview** page.

For example, if your project endpoint is `http://my-service-3781140846:7080/todos`, the hostname will be `my-service-3781140846`.

## Read mutual TLS certificates from your component

The approach to read mutual TLS certificates from a component can vary depending on its implementation. Typically, a component can read the certificate data from the file system or via an environment variable. For detailed instructions on adding environment variables and file mounts to your application, see [Manage Configurations and Secrets](../devops-and-ci-cd/manage-configurations-and-secrets.md).

!!! info
    When you specify a **private key**, ensure you **save it as a secret**.

## Sample for mutual TLS communication

For a sample that demonstrates how you can deploy services that communicate using mutual TLS, see [service-to-service-mtls](https://github.com/wso2/choreo-samples/tree/main/docker-service-to-service-mtls).


# Pass End-User Attributes to Upstream Services

There are scenarios where a backend service needs to apply specific logic or make decisions depending on the user consuming an API. In such scenarios, you must pass end-user attributes to the backend during an API call.

Choreo provides a method to send user information to a backend service through a JSON Web Token (JWT) in an HTTP header of an API request.

## How it works

The backend JWT contains claims transferred between the parties, such as the user and the backend. A claim can be metadata of the request or data about the user. A set of claims is called a dialect, for example, `http://wso2.org/claims`.

For each API request, a digitally signed JWT is carried to the backend service in the following format to ensure that the authenticity of the claims list is verified:

`{token header}.{claims list}.{signature}`

When a request goes through Choreo, the backend JWT is appended as the `X-JWT-Assertion` header in the outgoing message. The backend service fetches the JWT and retrieves the required information about the user, application, or token.

## Claims

Claims are fragments of information included in the JWT. 

The following is a sample claim set added to the end-user token for an access token generated via the authorization code:

!!! tip
    This access token is generated via Asgardeo using the authorization code grant type. Here, the Asgardeo application is configured to include the email claim in the token. 

``` java
{
  "sub": "11f53c32-f8ac-4810-bb79-615b2184baf5",
  "http://wso2.org/claims/apiname": "JWT Test - Endpoint 9090 803",
  "http://wso2.org/claims/applicationtier": "Unlimited",
  "http://wso2.org/claims/version": "1.0.0",
  "http://wso2.org/claims/keytype": "PRODUCTION",
  "iss": "wso2.org/products/am",
  "http://wso2.org/claims/applicationname": "jwtTest2",
  "http://wso2.org/claims/enduserTenantId": "0",
  "http://wso2.org/claims/applicationUUId": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "client_id": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "http://wso2.org/claims/subscriber": "5f4a7105-a889-4f92-9612-eef5bafe4eec",
  "azp": "IMJB5ZiR1dHQYBdiMIRAGis1WToa",
  "org_id": "b554e001-761c-4d3a-a7a6-a61d73d34221",
  "http://wso2.org/claims/tier": "Unlimited",
  "scope": "email openid profile",
  "exp": 1690537362,
  "http://wso2.org/claims/applicationid": "45101ccb-865f-4f48-b7ac-18e43b07edd3",
  "http://wso2.org/claims/usertype": "Application_User",
  "org_name": "test",
  "iat": 1690533762,
  "email": "testmail@gmail.com",
  "jti": "69558555-d386-4a81-9ca0-0a23f809cd3c",
  "http://wso2.org/claims/apicontext": "/b554e001-761c-4d3a-a7a6-a61d73d34221/swog/jwt-test/endpoint-9090-803/1.0.0"
}
```

The following table describes the information contained in the sample JWT claims set given above:

|             **Claim Name**              |          **Description**           |  **Mandatory/Optional**  |
|-----------------------------------------|------------------------------------|--------------------------|
| `iat`                                   |  The time the token was issued.    |   Mandatory              |
| `jti`                                   |  The unique token identifier.      |   Mandatory              |
| `exp`                                   |  The token expiry time.            |   Mandatory              |
| `iss`                                   |  The issuer of the token.          |   Mandatory              |
| `http://wso2.org/claims/apiname`        |  The name of the API in Choreo.    |   Optional               |
| `http://wso2.org/claims/version`        |  The API version.                  |   Optional               |
| `http://wso2.org/claims/keytype`        |  The environment in Choreo that the API is in (`Development` or `production`).|   Optional |
| `http://wso2.org/claims/apicontext`     |  The API context in Choreo.        |   Optional               |
| `http://wso2.org/claims/subscriber`     |  The subscriber to the API, usually the app developer. |   Optional |
| `http://wso2.org/claims/applicationname`|  The application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationid`  |  The ID of the application through which the API invocation is done. |   Optional |
| `http://wso2.org/claims/applicationUUId`|  The UUID of the application.      |   Optional               | 
| `client_id`                             |  The client identifier. This is copied from the original token.             |   Optional |
| `azp`                                   |  The authorized party (the party to which the ID token was issued). This is copied from the original token. |   Optional |
| `org_id`                                |  The organization ID. This is copied from the original token. |   Optional |
| `org_name`                              |  The organization name. This is copied from the original token. |   Optional |
| `http://wso2.org/claims/tier`           |  The tier/price band for the subscription. |   Optional       |
| `scope`                                 |  The scope of the token. This is copied from the original token. |   Optional |              
| `http://wso2.org/claims/usertype`       |  The type of application user whose action invoked the API. |   Optional |
| `email`                                 |  The email address of the user. This is copied from the original token. |   Optional |


!!! note

    The claims that get added to the end-user token can vary depending on the grant type used when generating the access token. For example, if you use the client-credentials grant type to generate the access token, the generated backend JWT would contain the following information:

    ``` java
    { 
      "http://wso2.org/claims/apiname": "DefaultAPI", 
      "http://wso2.org/claims/version": "1.0.0", 
      "http://wso2.org/claims/keytype": "PRODUCTION", 
      "iss": "wso2.org/products/am", 
      "http://wso2.org/claims/enduserTenantId": "0", 
      "exp": 1673245727, 
      "http://wso2.org/claims/usertype": "Application_User", 
      "iat": 1673242127, 
      "jti": "6e3f4392-8bd9-4900-9d08-eaab7429c510", 
      "http://wso2.org/claims/apicontext": "/9e71ab5e-6df5-4727-92d2-80ecf1a6218d/qbky/default/1.0.0" 
    }

    ```

To verify the authenticity of claims in a JWT, the claims must be validated using the public key corresponding to the private key used to sign the JWT.

JSON web key set (JWKS) is a set of keys to validate a JWT. It contains a collection of JSON web keys, which are public keys used to verify the signature of a JWT.

Typically, when a third party (such as an identity provider)issues a JWT and the recipient needs to verify its signature, they can use a JWKS. 
JWKS allows the issuer to rotate keys dynamically rather than hard-coding the public key in the application. The recipient can obtain the public key by accessing the JWKS endpoint.

## JWKS support in Choreo to validate the JWT

Choreo provides an endpoint to specify the public keys for backend JWT validation. Here are the endpoint URLs for the US East and EU regions:

- [https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-us-east-azure.choreoapis.dev/.wellknown/jwks)
- [https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks](https://gateway.e1-eu-north-azure.choreoapis.dev/.wellknown/jwks)

!!! note
    For private data planes (PDPs), use the following JWKS endpoint URL template:
    
    `https://<PDP_GATEWAY_DOMAIN>/.wellknown/jwks`

    Be sure to replace `<PDP-GATEWAY-DOMAIN>` with the default domain configured to access the PDP APIs.

The endpoint provides one or more signing keys to validate the JWT.
The JSON web keys have a kid identifier that can be matched with the same property on the JWT to decide which key to use when validating.

The following is a sample JWKS response:

``` java
{
   "keys": [
       {
           "kty": "RSA",
           "e": "AQAB",
           "use": "sig",
           "kid": "ZjcwNmI2ZDJmNWQ0M2I5YzZiYzJmZmM4YjMwMDFlOTA4MGE3ZWZjZTMzNjU3YWU1MzViYjZkOTkzZjYzOGYyNg",
           "alg": "RS256",
           "n": "8vjeHzRhvpfMystncPnLBWy_t5F3eCxbcLbdugWnzfnIgaV6TWnqPBUagJBKpzRZs4A9Qja_ZrSVJjYsbARzCS_qiWp0Cdwkqn6ZCXpmbpfjYnKORq8N8M-zWaSZYbNvWJ5oSO4kH-LKWzODaFebwTJBpsR1vChHH95doxFuUjiZaisVaQgUJ6drRdlDtImp9r9EAX36YROuYFPoEJcvsH4_uuAR6ClJ12RE3M-YN4NTi1waVNvGbz43oNrpPy7SXgpizingxSGMqI6WU2ysRmk_f9ALgiPIpFDpufiCTYaIcRT-YcUyp9nMDlTRskMuD-dQ1sdJOa11P_yMs-glfQ"
       }
   ]
}
```

The following table describes the information contained in the JWKS response:

| **Property** |                                 **Description**                                    |  
|--------------|------------------------------------------------------------------------------------|
| `kty`        |  The cryptographic family to which the key belongs. <br> Choreo only supports RSA. |
| `e`          |  The exponent value of the public key.                                             |
| `use`        |  The purpose of the key. For example, whether it is for signing or encryption.     |
| `kid`        |  The identification parameter to match a specific key.                             |
| `alg`        |  The algorithm to use with the key.                                                |
| `n`          |  The modulus value of the public key.                                              |

## Enable passing end-user attributes to the backend

To enable passing end-user attributes to the backend through API calls via Choreo, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Components Listing** pane, click on the component for which you want to pass end-user attributes to the backend.
3. In the left navigation menu, click **Deploy**.
4. Go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.

    !!! note
         If the component is an API Proxy, go to the **Build Area** card and click **Security Settings**. This opens the **Security Settings** pane.
   
5. Select the **Pass Security Context To Backend** checkbox.
6. Optionally, specify appropriate audience values in the **End User Token Audiences** field. Specifying values restricts the JWT to the respective audiences, enabling the backend service to validate and confirm the intended recipients, including itself.

    !!! note
        The backend JWT does not include the audience field (aud) by default.

7. Click **Apply**.
8. To redeploy the component with the applied setting, go to the **Set Up** card and click **Deploy**.


# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Choreo as an external Identity Provider (IdP). This guide will walk you through setting up Choreo to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

- Assign scopes to an API in Choreo. 
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Choreo and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have a service in Choreo, [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- Deploy and publish your API. 

## Step 1: Assign scopes to an API in Choreo

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Manage** and then **Permissions**.
3. Click **+ Add Permission (Scope)**. 
4. In the **Permission List** pane, enter the permission value and click **+ Add New**.
5. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
6. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
7. Click **Save and Deploy**.
8. In the left navigation, click **Manage** and then **Lifecycle**.
9. Click **Publish** and continue to publish your API to the Choreo Developer Portal. 


## Step 2: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 3: Create an application in Choreo and enable external IdP authentication

Follow the steps below to consume the Choreo API and use an external IdP for authentication:

1. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name and description for the application. 
4. Click **Create**.
5. In the left navigation, under **Credentials** and click **Production**.
6. Select the **Identity Provider** as `Asgardeo`.
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - The Identity Provider dropdown is visible only to organizations where you have configured external IdPs. 

9. In the left navigation menu, click **Subscriptions**.
10. In the **Subscription Management** pane that opens, click **+ Add APIs**.
11. Select the API you assigned scopes to in [step 1](#step-1-assign-scopes-to-an-api-in-choreo) and click **Add**. 

## Step 4: Invoke the Choreo API with scopes

1. On the Choreo Developer Portal, go to your application. 
2. In the left navigation menu, under **Credentials** and click **Production**.
3. Under **Endpoints**, copy the **Token Endpoint** URL. 
4. Obtain an access token by invoking the token endpoint as follows:
   
    !!! note
        - If you are using the production credentials, you need to deploy your component(endpoint) to the production environment by promoting it from the development environment.
        - If you are using the sandbox credentials, you can use the endpoints deployed in the development environment.

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```



5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../testing/test-rest-endpoints-via-the-openapi-console.md) in Choreo by specifying the scope. 



# Secure Communication Between the Choreo Gateway and Your Backend with Mutual TLS

To establish secure communication between the Choreo Gateway and your backend, you can configure mutual TLS.

Mutual TLS authentication involves both the client and server validating each other’s certificates before establishing a connection. The following diagram depicts this scenario:

![Mutual TLS authentication](../assets/img/authentication-and-authorization/mutual-ssl-authentication.png)

## Configure mutual TLS to establish secure connectivity

To establish secure connectivity between the Choreo Gateway and your backend using mutual TLS, you must add the certificate of the backend (server certificate) to Choreo and add the certificate of Choreo (client certificate) as a trusted certificate in the backend.

### Step 1: Configure the backend certificate 

#### Prerequisites

- The endpoint must be protected with TLS. 
- The public certificate of the backend server should be extracted in PEM format and saved on the disk with the `.pem` extension.

To configure the backend certificate, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the API proxy for which you want to configure TLS. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
3. In the left navigation menu, click **Develop** and then click **Endpoints**.
4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
5. Click **Upload Endpoint Certificate**, and select the certificate file that you extracted in the prerequisites section to add it. This adds the certificate to all the environments as the default certificate for the endpoint. You can override this certificate if necessary when you deploy or promote the API.

### Step 2: Configure mutual TLS with the backend service

There are two approaches you can take to configure mutual TLS.

 - Generate a key pair with a self-signed certificate from Choreo, download the public certificate, and subsequently add and configure it in the backend.
 - Upload your own public or private certificate pair to Choreo. Subsequently, add and configure the public certificate of this key pair in your backend.

Follow the step-by-step instructions below depending on how you want to establish mutual TLS with the backend service:

=== "Generate a key pair through Choreo"
    When you follow these steps, Choreo generates a key pair with a self-signed certificate. You can attach this key pair to any API proxy created within the same project.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.    
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Generate new key pair** and specify a value as the common name for the certificate pair. This value will be used to identify the certificate.

        ![Generate new key pair](../assets/img/authentication-and-authorization/generate-new-key-pair.png)
       
    9. Optionally, click **Show advanced options** to expand the section and specify appropriate values for each of the fields.
    10. Click **Generate**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
    
    Now you can associate the certificate with the API and deploy the API.

=== "Use your own certificate pair"
    Here, you can use your own public certificate and private certificate as client certificates.

    1. Sign in to the [Choreo Console](https://console.choreo.dev/).
    2. In the **Component Listing** pane, click on the API proxy for which you want to generate a key pair. For instructions on how to create an API proxy component, see [Develop an API Proxy: Step 1](../develop-components/develop-an-api-proxy.md#step-1-create-an-api-proxy).
    3. In the left navigation menu, click **Develop** and then click **Endpoints**.
    4. On the **Endpoints** page, click **Configure** corresponding to the endpoint.
    5. If your backend does not use a CA-signed certificate and you have not already added the backend certificate, click **Upload Endpoint Certificate** and add the backend certificate.
    6. To enable mutual SSL, turn on the **Mutual SSL** toggle.
    7. Click **Add Client Certificate**.
    8. In the **Add Client Certificate Pair** dialog, select **Use my own key pair**.

        ![Use own key pair](../assets/img/authentication-and-authorization/use-own-key-pair.png)
       
    9. Upload the private key and public certificate in PEM format or copy and paste the content of the private key and public certificate.
    10. Click **Add**. This generates the certificate and lists it under **Existing Certificates**.
    11. Click the more options icon corresponding to the certificate and then click **View and Download**.

         ![View and download certificate](../assets/img/authentication-and-authorization/view-and-download.png)
       
        This opens the certificate for you to view and download.

         ![Certificate details](../assets/img/authentication-and-authorization/certificate-details.png)

    12. To download the certificate in PEM format, click **Download**. You can add this certificate as a trusted certificate in the API backend server.
   
    Now you can associate the certificate with the API and deploy the API.

### Step 3: Associate the certificate with the API

To associate a certificate with the API, follow the steps given below:

1. On the **Endpoints** page, go to the **Existing Certificates** section.
2. Select the certificate you want to associate with the API.

    ![Associate certificate](../assets/img/authentication-and-authorization/associate-certificate.png)

3. Click **Save**.
   
### Step 4: Deploy the API 

To deploy the API, follow the steps given below:

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**.
3. Once the mediation application generation phase is complete, verify the endpoint URL populated for the environment and then click **Save & Deploy**.

Once the deployment is complete, you can [test the API](../testing/test-rest-endpoints-via-the-openapi-console.md). 

## Change the certificate for the production environment

If the API backend changes depending on the environment, the respective certificate must be updated for each environment. 

Here, let's take a look at the steps to update the certificate for the production environment:

1. On the **Deploy** page, go to the **Development** card and click **Promote**.
2. In the **Configurations** pane that opens, click **Endpoint Configuration**. You will see all applicable certificates listed in the **Mutual TLS** list. 
3. Select the certificate applicable to the production environment and click **Promote**. This promotes the component to the production environment with the selected certificate.


# Secure Web Applications with Managed Authentication

The managed authentication capability of Choreo simplifies adding authentication and authorization to a single-page web application.

As a developer, you can easily set up Choreo's managed authentication to seamlessly integrate authentication into your web application. You just need to enable Choreo’s managed authentication, configure the built-in identity provider, and connect to Choreo without having to deal with the complexities of underlying OIDC/OAuth2.0 protocols.

Choreo's managed authentication follows the backend for frontend (BFF) architecture, which is a secure pattern recommended for browser-based applications that utilize OIDC/OAuth2.0 for authentication and authorization. This architecture ensures that OAuth tokens remain secure from browser-side code, making them immune to potential attacks like cross-site scripting (XSS).

!!! note
     Choreo's managed authentication is currently available only for web applications created with **React**, **Angular**, or **Vue.js** buildpacks.

!!! warning
     Managed authentication uses the 'SAMESITE' cookie attribute to prevent CSRF attacks. Therefore, it is recommended to use managed authentication with modern browsers that support the 'SAMESITE' attribute.

## Step 1: Set up managed authentication for your web application

To secure your web application, you must implement authentication and authorization for it. 

To easily set up authentication for your web application with Choreo's managed authentication, follow the steps given below. Before you move on to the next section, see [Develop Web Applications Locally with Choreo’s Managed Authentication](../develop-components/develop-web-applications/develop-web-applications-locally-with-managed-authentication.md) to ensure a seamless authentication experience when developing your web application on your local machine. You can also refer to the [sample React app with managed authentication](https://github.com/wso2/choreo-samples/tree/main/reading-list-app/reading-list-front-end-with-managed-auth).

### Step 1.1: Implement the sign-in functionality

To allow Choreo to manage the sign-in functionality for your web application, you must implement a sign-in button that redirects users to the `/auth/login` path on click. You can use the following code snippet or any custom button component from a preferred UI component library:

``` javascript
<button onClick={() => {window.location.href="/auth/login"}}>Login</button>
```

This code snippet works as follows:

When a user clicks sign in on your web application, Choreo will redirect the user to the configured identity provider and handle the authentication process, conforming to the OICD/OAuth2.0 protocols. On successful sign-in, Choreo will set the relevant session cookies and redirect the user to the post-sign-in path (default is `/`). The user can then invoke any Choreo-deployed APIs depending on the permission granted.

!!! note
    Refer to [configure the identity provider section](#step-3-configure-the-identity-provider-for-the-web-application) for details on configuring an identity provider for the web application. 

#### Optional: Pass additional query parameters to the identity provider 

If you want to pass additional query parameters to the identity provider, include them in the `/auth/login` request. Choreo appends these parameters to the `authorize` request sent to the identity provider.

For example,

``` javascript
<button onClick={() => {window.location.href="/auth/login?fidp=myfederatedidp"}}>Login</button>
```

### Step 1.2: Obtain user information claims

Choreo's managed authentication allows you to access user information claims that the identity provider returns post-sign-in, either via a cookie or by invoking a GET resource.


#### Obtain user information via the `userinfo` cookie

Upon successful sign-in, Choreo's managed authentication establishes a `userinfo` cookie that is accessible from the post-sign-in path you configured (by default, set to /). This `userinfo` cookie, provided by the identity provider, contains encoded user information claims.

!!! note
    - The `userinfo` cookie is intentionally set to have a short lifespan of only 2 minutes.
    - As a developer, you can decide how to utilize the user information that you retrieve. You must securely store the user information because the stored information can also serve as a means to verify the logged-in state of a user.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice. 

The recommended approach is to retrieve user information from the cookie and subsequently clear the cookie. The following is a sample code snippet that you can include in your post-sign-in path to retrieve user information from the cookie and subsequently clear the cookie:

``` javascript
    import Cookies from 'js-cookie';

    // Read userinfo cookie value.
    const encodedUserInfo = Cookies.get('userinfo')

    // Decode the value. 
    const userInfo = JSON.parse(atob(encodedUserInfo))

    // Store the value in a preferred browser-based storage if needed.

    // Clear the cookie.
    Cookies.remove('userinfo', { path: <post-login-path> })
```
#### Obtain user information via a GET endpoint

Choreo's managed authentication provides the GET endpoint `/auth/userinfo` in addition to the `userinfo` cookie that it sets after successful sign-in. You can use this endpoint to query information about users who have signed in. It also serves as a mechanism to check the state of a user who has signed in.

The following is an example of a request to this endpoint:

``` javascript
const response = await fetch('/auth/userinfo')
```

If a user has signed in, the server sends a `200 OK` response with the user information in JSON format in the response body. However, if the user is not signed in, the server sends a `401 Unauthorized` response.

### Step 1.3: Implement the sign-out functionality

To allow Choreo to manage the sign-out functionality of your web application, you can implement a sign-out button to redirect users to the `/auth/logout` path along with the `session_hint` cookie value on click. You can use the following code snippet or any custom button component from a preferred UI component library:

!!! note
    - It is recommended to clear any user information (if stored) at the time of sign-out.
    - The following example uses the `js-cookie` library for cookie parsing. You can use any cookie-parsing library of your choice.   
    
``` javascript
<button onClick={async () => {
    window.location.href = `/auth/logout?session_hint=${Cookies.get('session_hint')}`;
}}>Logout</button>`
```

When a user clicks the sign-out button, Choreo will clear the session cookies and redirect the users to the OIDC logout endpoint of the configured identity provider (if available).  

### Step 1.4: Invoke APIs

To invoke Choreo APIs within the same organization as your web application, you can use the relative path `/choreo-apis/<api-suffix>`, regardless of whether managed authentication is enabled for the web application or not.

!!! note
    To invoke a Choreo API from a web application, you need to [create a Connection](../develop-components/sharing-and-reusing/create-a-connection.md) from the web application to the Choreo API. 

For example, if the API URL is `https://2d9ec1f6-2f04-4127-974f-0a3b20e97af5-dev.e1-us-east-azure.choreoapis.dev/rbln/item-service/api-e04/1.0.0`, the `<api-suffix>` would be `/rbln/item-service/api-e04/1.0.0`. You can invoke the API using the `/choreo-apis/rbln/item-service/api-e04/1.0.0` relative path from your single-page application.

!!! info
     To copy the exact service URL of a Connection, you can follow the steps given below:
      1. In the Choreo Console, go to the appropriate web application component.
      2. In the left navigation menu, click **Connections** under **Dependencies**.
      3. Click on the required Connection and copy the service URL.

If you enable Choreo's managed authentication, you don't have to manually add any logic to attach an access token to the API call because Choreo APIs accept the cookies set by Choreo's managed authentication. You can directly invoke the API as follows:

```
    const response = await fetch('/choreo-apis/<api-suffix>')
```

If Choreo's managed authentication is disabled, you must ensure that your web application attaches a valid access token to the API call.


### Step 1.5: Handle session expiry

When a user session exceeds the configured session expiry time, it automatically expires. A `401 Unauthorized` response status code for a Choreo API request from a logged-in user indicates that the session may have expired, requiring the user to re-login.

To programmatically handle session expiry and automatically re-login upon receiving a `401 Unauthorized` response from a Choreo API, you can encapsulate the request with re-login logic. The following sample code snippet shows how to wrap GET requests:


``` javascript
    export const performGet = async (url) => {
        try {
            // API call
            return await fetch('/choreo-apis/<api-suffix>');
        } catch (error) {
            if (error instanceof HttpError && error.status === 401) {
                // Re-login
                window.location.href = "/auth/login";
            } else {
                throw error;
            }
        }
    };
```

### Step 1.6: Set up a custom error page

You can set up Choreo's managed authentication to redirect to a customized error page within your web application by defining the error path in the configuration. In the event of an error during a redirection-based process, such as sign in or sign out, Choreo will automatically redirect the user to the designated custom error page.

!!! note
    If you have not configured an error path, Choreo's managed authentication will use its default error page whenever an error occurs.

Choreo's managed authentication will include the following query parameters in the URL when redirecting to the custom error page:

| Parameter      |  Description                                    |
|----------------|-------------------------------------------------|
| code           | A short textual error code indicating the error |
| message        | The description of the error                    |


Now have successfully implemented Choreo's managed authentication for your web application. The next step is to enable managed authentication for the component, and subsequently deploy it.

## Step 2: Enable managed authentication and configure the paths

To ensure that your web application functions seamlessly with managed authentication, it is essential to enable managed authentication for your web application component within Choreo.

You can enable managed authentication for your web application component at the time you deploy the component.

!!! tip
     Managed authentication is enabled by default when you create a web application using **React**, **Angular**, or **Vue.js** buildpacks.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). This opens the project home page.
2. In the **Component Listing** pane, click on the web application for which you want to enable managed authentication.
3. In the left navigation menu, click **Deploy**.
4. In the **Set Up** card, click **Configure & Deploy**.
5. Add the necessary configurations for your component if applicable and click **Next**.
6. Make sure **Managed Authentication with Choreo** toggle is enabled.
7. Specify appropriate values for the following fields:

    | Field            |  Description      | Default value      |
    | ----------------- | ----------------- | ----------------- |
    | Post Login Path   | The relative path that the application will be redirected to on successful sign-in. In your code, you must implement the necessary logic to obtain signed-in user's information from the `userinfo` cookie set by managed authentication. See **Obtain user information via the `userinfo` cookie** section in [Obtain user information claims](#step-12-obtain-user-information-claims). | /                      |
    | Post Logout Path  | The relative path to which Choreo redirects you on successful sign-out.  | /                      |
    | Error Path        | The relative path to which Choreo redirects you when an error occurs during a redirection-based flow (i.e., sign in or sign out). See [Set up a custom error page](#step-16-set-up-a-custom-error-page).             | Built-in error page     |
    | Session Expiry Time | The time in minutes after which the user session expires. For a seamless experience, the session expiry value should match the refresh token expiry time of the OIDC application in your identity provider.               | 10080 Minutes (7 Days)                   |
    | Additional Scopes | All additional scopes required by the web application. The `openid`, `profile`, and `email` scopes are added by default together with the scopes required to invoke subscribed APIs.               | none                   |

    !!! note
         If you need to change these configurations after you deploy the component, you can click **Authentication Settings** on the **Set Up** card, make the necessary changes, and deploy the component once again.

## Step 3: Configure the identity provider for the web application

You can configure your web application to work with the Choreo built-in identity provider, Asgardeo, or any external identity provider which supports OIDC/OAuth2.0 . 

!!! note
    The identity provider configured in this step should contain the users for the web application.

Click the respective tab for details depending on which identity provider you need to configure: 

=== "Configure Choreo built-in identity provider"

     Follow the steps given below to configure the built-in identity provider by generating authentication keys:

    !!! note
         Choreo built-in identity provider is configured by default. Therefore, this step is optional.

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Choreo Built-In Identity Provider**.
     5. Click **Generate Secret**. 

        !!! Note
             If the **Regenerate Secret** button is shown instead of the **Generate Secret** button, it indicates that OAuth keys are already generated for the component for the selected environment.

    !!! tip
        Refer to [Configure a User Store with the Built-In Identity Provider](../../administer/configure-a-user-store-with-built-in-idp/) for details on adding test users in Choreo built-in identity provider.

    !!! tip
        If you need to invoke APIs secured with role-based access control, you can test this within Choreo by creating roles for the application and mapping those roles to relevant permissions (scope) and user groups. For more information, see [create roles and assign permissions](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-2-create-roles-and-assign-permissions) and [assign roles to user groups](../test-secure-api-access-with-choreo-built-in-security-token-service/#step-3-assign-roles-to-user-groups) sections in [Test Secure API Access with Choreo Built-In Security Token Service](../test-secure-api-access-with-choreo-built-in-security-token-service).

=== "Configure Asgardeo"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in Asgardeo**

     1. Sign in to [Asgardeo](https://console.asgardeo.io/).
     2. In the top navigation menu, click the **Organization** list and select your organization.
     3. In the Asgardeo Console left navigation menu, click **Applications**.
     4. Click **+ New Application**.
     5. Click **Standard-Based Application**.
     6. Specify a name for the application and select **OAuth2.0 OpenID Connect** as the protocol.
     7. Click **Register**.
     8. Click the **Protocol** tab and follow these steps:

         1. Select `Code` and `Refresh Token` as the **Allowed grant types**.
         2. Specify the following as **Authorized redirect URLs**:
             - [your-web-application-url]/auth/login/callback
             - [your-web-application-url]/auth/logout/callback
         3. Specify your web application URL under **Allowed origins**.
         4. In the **Access Token** section, select `JWT` as the **Token type**.
         5. Click **Update**. 

            !!! tip
                 If you need to invoke APIs secured with role-based access control, you must create roles in the application and map those roles to relevant permissions (scope). Then those roles should be assigned to user groups. For more information, see the [Asgardeo API authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/).

         6. Copy the **Client ID** and **Client Secret** of the application. You will need to use these values in the next step to link the OIDC/OAuth2.0 application to your Choreo component.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo web application component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select **Asgardeo - [your-org-name]**.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in Asgardeo. 
     6. Click **Add Keys**.

=== "Configure an external identity provider"

     **Step 3.1: Create and configure an OIDC/OAuth2.0 application in the external identity provider**

     1. Create an OIDC/OAuth2.0 application in your external identity provider.
     2. Configure the OIDC/OAuth2.0 application as follows:

         1. Set `Code` and `Refresh Token` as allowed grant types.
         2. Add the following as authorized redirect URL.
         3. Specify the following as authorized redirect URLs:
         4. Specify the access token type as JWT.

            !!! tip
                 If you want to invoke APIs secured with role-based access control, you must ensure that users are assigned a role mapping that grants the necessary permission for API invocation. The approach of mapping application roles to users can vary depending on the identity provider.

     **Step 3.2: Link the OIDC/OAuth2.0 application to the Choreo component**

     1. In the Choreo Console, go to the component for which you want to manage OAuth keys.
     2. In the left navigation menu, click **Settings**.
     3. Click the **Authentication Keys** tab and then click on the environment for which you want to generate keys.
     4. In the **Identity Provider** list, select your identity provider.
     5. Paste the **Client ID** and **Client Secret** of the OIDC/OAuth2.0 application you created in your external identity provider.
     6. Click **Add Keys**.


# Test Secure API Access with Choreo Built-In Security Token Service

API security can protect APIs from potential threats and vulnerabilities, with authentication and authorization playing key roles. Authentication ensures that only authorized users or applications can access the API. This involves using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization governs the actions permitted for authenticated users or applications within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions.

Choreo simplifies security testing for developers, allowing them to easily test APIs with permissions in non-critical environments. With its integrated security token service, Choreo provides authorization features that generate scopes based on the correlation between scopes, roles, and user groups. Developers can create roles, assign permissions, and set up user-group mappings using Choreo's built-in identity provider (IdP).

This guide walks you through the following steps to test the invocation of secured APIs with permissions using Choreo's built-in authorization capability:

- Assign scopes to an API in Choreo.
- Create roles and assign permissions in Choreo.
- Assign roles to user groups.
- Test the API invocation.
    - When Choreo manages the authentication (i.e., managed authentication enabled).
    - When the application independently handles the authentication (i.e., managed authentication disabled).

## Prerequisites

Before you try out this guide, ensure you have set up the following:

- Configure the Choreo built-in identity provider with users. For step-by-step instructions, see [Configure a User Store with the Built-In Identity Provider](../administer/configure-a-user-store-with-built-in-idp.md).
- Deploy and publish an API via Choreo. If you don't have an existing service in Choreo, you can either [develop a service](../develop-components/develop-services/develop-a-service.md) or an [API Proxy](../develop-components/develop-an-api-proxy.md).
- A web application for API subscription. If you don't have an application in Choreo, you must [create a web application](../develop-components/develop-web-applications/build-and-deploy-a-single-page-web-application.md)
- Administrator rights in your Choreo organization. You need this access to configure role-group and role-permission mappings.

## Step 1: Assign permissions to an API in Choreo

You can provide fine-grained access control to your API resources with permissions. Follow the steps below to assign permissions to the resources in the API:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Project** list and select the project that contains your component.
3. In the **Component Listing** pane, click on the component for which you want to attach permissions.
4. In the left navigation menu, click **Deploy**.
5. On the **Deploy** page, go to the **Set Up** card and click **Endpoint Configurations**. This opens the **Endpoint Configurations** pane.
6. Go to the **Permissions List** section and click **+ Add Permission(Scope)**.
7. In the **Permissions List** section, enter a permission value and click **+ Add New**.
8. Click the copy icon in front of the added permission to copy the fully qualified name of it. Save this value for future reference.
9. To attach permissions to a resource, click the **Select Permissions** list under the respective resource and select the permissions you want to attach.
10. Click **Apply**.
11. To apply the latest permissions to the deployed component, you must redeploy it. Follow the steps below to redeploy:
    1. Go to the **Set Up** card and click **Configure & Deploy**.
    2. In the **Configurations** pane that opens, click **Next**. This opens the **Endpoint Details** pane.
    3. Click **Deploy**.

12. To publish your API to the Choreo Developer Portal, follow the steps given below:
    1.  In the left navigation menu, click **Manage** and then click **Lifecycle**.
    2.  Click **Publish**.

## Step 2: Create roles and assign permissions

The permissions assigned to your API need to be associated with roles. Follow the steps below to create roles and assign permissions to the roles.

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project that contains your component. 
2. In the left navigation menu, click **Settings**.
3. Click the **Application Security** tab.
4. Click **+ Role**.
5. Specify an appropriate **Role Name** and **Role description**. 
6. Select the permissions you want to assign to the role, and then click **Create**.
  
    !!!tip

            The permissions(scopes) defined for APIs exposed via components in the project and the permissions(scopes) required by connections created for components in the project are listed here. 

## Step 3: Assign roles to user groups

You must assign roles to the user groups defined in your Choreo built-in IdP to ensure that authenticated users can obtain access tokens with the required permissions.

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your component.
2. Click the **Application Security** tab and then click **Role Management**.
  
    !!!tip

            The roles defined within different projects in the organization are listed here.

3. Click **Map Groups** corresponding to a role that you want to assign to a group.
4. Specify a group name and enter to add it. You can add multiple groups if necessary.
5. Click **Save**.

## Step 4: Test the API invocation

To test an API invocation, you must first create a connection to your API. To do this, you must have a web application created. You can use the web application you created while setting up the prerequisites.

To create a connection to the web application, follow the steps given below:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the project where you created the web application.
2. On the project home page, click the web application listed under **Component Listing**.
3. In the left navigation menu, click **Dependencies** and then click **Connections**.
4. Create a connection to the API you deployed in [Step 1](#step-1-assign-permissions-to-an-api-in-choreo). 
   
Now you can proceed to deploy the web application.

When deploying, if your web application is a single-page application (SPA), you have the option to allow Choreo to handle authentication on behalf of the application. This approach eliminates the need to incorporate OAuth protocol-specific logic into your application.

### Test the invocation when Choreo-managed authentication is enabled

If managed authentication is enabled for your web application, Choreo automatically handles obtaining the necessary permission for API invocation. This occurs during the request for access tokens, allowing you to seamlessly invoke the subscribed APIs through your web application without additional intervention. 

!!! note
    If you change the permissions of an existing connection or create a new connection with permissions, you must redeploy your web application to ensure proper API invocation with managed authentication.

### Test the invocation when the application manages the authentication

If your application manages authentication independently, follow the steps below to generate the necessary OAuth credentials to obtain access tokens:

1. In the left navigation menu, click **Settings**. This opens the settings of the web application component.
2. Click the **Authentication Keys** tab.
3. Click on an environment tab depending on the environment for which you want to generate credentials.
4. Select **Choreo Built-In Identity Provider** as the identity provider.
5. Click to expand **Advanced Configurations** and make sure the `code` and `refresh` grant types are selected. This is required to obtain access tokens with an authorization code grant.
6. Configure the callback URL of the web application to receive the authorization code.
7. Click **Update Configurations**.
8. Click **Regenerate Secret** and make a note of the client ID and secret that is generated.
9. Retrieve an access token using the authorization code grant, specifying the necessary OAuth scopes (You can see the endpoint details on the right side).
    - When prompted for authentication, enter the credentials of a user within the built-in identity provider (IdP) who possesses the required assigned groups.
    - Navigate through the OAuth flow to obtain the JWT access token.
10. Invoke the subscribed API using the access token.


