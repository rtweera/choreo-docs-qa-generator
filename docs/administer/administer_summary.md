     # Configure a Custom Domain for Your Organization

A custom domain is essential for effective branding, discoverability, and credibility of a website. Choreo allows you to easily configure custom domains for your organization, enabling developers to utilize it to configure custom URLs for their components such as API proxies, services, web applications, and webhooks.

This section provides an overview of Choreo’s custom domain configuration model and guides you through configuring a custom domain for your organization. It also walks you through utilizing a custom domain to configure a custom URL for a component.

## Choreo custom domain configuration model

Choreo allows organization administrators to add custom domains for their organizations. When an administrator adds custom domains to an organization, component developers can submit requests to utilize the custom domains for their respective components. These requests require approval from the organization administrator. Upon approval, the custom domain and the relevant URL customization become available to the component.

## Configure a custom domain for an organization

### Prerequisites

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Create an organization in Choreo.
    
    ![Create an organization in Choreo](../assets/img/administer/create-choreo-organization.png)

### Add a custom domain

To add a custom domain for your organization, follow the steps given below:

!!! info "Note"
     To add a custom domain, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Active Domains** tab.
5. Click **+ Add Domains**. 
6. In the **Add a Custom Domain** pane, do the following:
    1. Enter your domain name.
    2. Select the environment to apply the domain name.
    3. Select the entity type to apply the domain name.

        !!! tip
             In this context:

              - The **API** entity type represents Choreo components exposed via an endpoint, including API Proxy, Service, and Webhook components.
              - The **Web App** entity type represents the Web Application component.
       
 7. Take a look at the generated CNAME target value displayed and create a DNS record associating the domain name to the CNAME target value with your DNS provider.
    
    ![CNAME target value](../assets/img/administer/configure-domain/cname-target-value.png)

    !!! info
          When you select **Developer Portal** as the type, the environment is not applicable, and the CNAME alias will be displayed as follows:
           ![Developer Portal CNAME target value](../assets/img/administer/configure-domain/developer-portal-cname-target-value.png)

 8. Once the CNAME type DNS record is created, click **Verify**.

    !!! info "Note"
          If the CNAME mapping is correct, the verification completes successfully. It can take some time for the configured CNAME mapping to be globally available.

 9. On successful verification of the custom domain, click **Next**.
 10. Select a TLS certificate provider depending on your preference. You can either import the TLS certificates you created for the custom domain or click **Let's Encrypt** to allow Choreo to generate and manage the certificates for you.

    !!! note "If you want to import your own certificate, it should adhere to specific guidelines"
          - TLS certificate guidelines:
             - It should be issued by a certificate authority (CA) and should contain the domain's public key along with additional information such as the domain name, the company that owns the domain, the certificate's expiration date, and the digital signature of the issuing CA.
             - It should be an X509 certificate.
             - It should be in the PEM format.
             - It should be issued directly or through a wildcard entry for the provided custom URL. For example,
                - For direct issuance, the SSL file must include the exact domain name. For example, if the domain is `apis.choreo.dev`, the SSL file must include `apis.choreo.com`.
                - For wildcard entries, the SSL file should use a wildcard notation to cover all subdomains under the provided URL. For example, if the CNAME is `apis.choreo.dev`, the SSL file should use `*.choreo.dev`.
          - TLS key file guidelines:
             - It should be in the PEM format.
             - It must be encrypted using RSA encryption.
          - Certificate chain file guidelines:
             - The chain file, which is essential for some clients to verify the authenticity of a server's SSL/TLS certificate, should contain your domain's SSL/TLS certificate (optional, as this can be provided via the certificate itself) and one or more intermediate certificates in the correct order, leading back to a root certificate. 
             - All certificates in the chain should be X509 certificates in PEM format.
               <details><summary>For step-by-step instructions on constructing a certificate chain with a root certificate, click here</summary>
               To construct a certificate chain with a root certificate, you must organize and combine the certificates in the correct sequence. A typical certificate chain consists of the following:
                 - **Root certificate**: The trusted self-signed certificate issued by the certificate authority (CA).
                 - **Intermediate certificates** (if any): Certificates issued by the root CA to subordinate CAs.
                 - **Leaf certificate**: Your end-entity certificate issued by the CA. This is an optional certificate that may be included within the chain or provided separately.<br><br>
                Follow these steps to construct the certificate chain:
                    1. Obtain and organize your certificates in the correct order:
                        - **Leaf certificate**: The public certificate issued by the CA. This is optional and may be included within the chain or provided separately.
                        - **Intermediate certificates**: Obtain these from the CA, if applicable.
                        - **Root certificate**: Obtain this from the CA.  If it is self-signed, it serves as the trust anchor.
                    2. Combine the certificates into a single file in the following order:
                        - Leaf certificate: This is your public certificate issued by the CA.
                        - Intermediate certificates if applicable: Include these in the correct hierarchical order.
                        - Root certificate: Include this at the end of the file.<br><br>
                        Use a text editor or a command-line tool to concatenate the certificates into one file, ensuring each certificate begins and ends with the proper markers. Also make sure the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers appear on a new line:
                    ```
                     -----BEGIN CERTIFICATE-----
                     <Leaf Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Intermediate Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Root Certificate Content>
                     -----END CERTIFICATE-----
                    ```
                    3. Save the concatenated file. You can save it with a name such as `certificate_chain.pem`.
                    4. Use the following command to verify that your certificate chain is constructed correctly:
                    ```
                    openssl verify -CAfile <root_or_bundle_cert>.pem certificate_chain.pem
                    ```
                    Replace `<root_or_bundle_cert>.pem` with the path to your root certificate or a bundle containing both the root and intermediate certificates.
                    5. Once the certificate chain is verified, upload it via the Choreo Console:
                        ![Upload certificate chain](../assets/img/administer/configure-domain/upload-certificate-chain.png)
                        - If the constructed chain includes the leaf certificate, follow these steps:
                            - Upload the constructed certificate chain in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Do not upload a certificate chain file, as it is already included in the TLS certificate.
                        - If the constructed chain does not include the leaf certificate, follow these steps:
                            - Upload the leaf certificate in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Upload the constructed certificate chain in the **Certificate Chain File** field.
 
     To proceed with this step in this guide, click **Let's Encrypt**.

 11. To save the custom domain, click **Add**.
 
Now, you have successfully added a custom domain for your organization.

You can see the added custom domain listed in the **Active Domains** tab under the URL **Settings** tab.
    
 ![Active domains](../assets/img/administer/configure-domain/active-domains.png)

The custom domain you added will be available to the entity types in the specified environment. You can request the custom domain when configuring a custom URL for a component.

!!! info "Note"
     If you add a custom domain for the **Developer Portal** type, the customization is applied immediately, and you can access the organization’s Developer Portal via the added domain.

If you want to view the entity types that use a particular custom domain, click the specific custom domain listed in the **Active Domains** tab under **URL Settings**.
 
## Configure a custom URL for a component

When an organization administrator adds custom domains for specific environments, developers can request any available custom domain to configure a custom URL for a component in a specific environment.

### Request a custom URL for a component

To request a custom URL for your component, follow the steps given below:

!!! info "Note"
     Before you request a custom domain for a specific environment, ensure that the component is deployed to that environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to customize the URL.
3. In the left navigation menu, click **Settings**. This opens the component-level settings page.
4. Click the **URL Settings** tab. This displays the active deployments of the component across different environments and indicates whether a custom URL is configured. If an active custom domain is available to configure a custom URL for a component in a specific environment, the **Edit URL Mapping** icon in the corresponding **Action** column becomes enabled.
    
    ![Active deployments](../assets/img/administer/configure-domain/active-deployments.png)

5. To configure a custom URL for a component in a specific environment, click the **Edit URL Mapping** icon under the **Action** column corresponding to the respective environment. This opens the **URL Settings** dialog, where you can specify values to request for a custom URL.
    
    ![URL settings](../assets/img/administer/configure-domain/url-settings.png)

6. In the **URL Settings** dialog, select a domain to configure a custom URL.

    !!! tip
          - The **Domain** drop-down lists the available domains for the component. You can  request for any listed domain.
          - If you want to request a custom URL for an API, you must specify an appropriate context path in the **Path** field. The **Path** field displays the default context path for the API. You can edit the path depending on your preference. 

7. Click **Configure**. This creates the custom URL mapping, which you can see under the **URL Settings** tab.  The custom URL request will be in the **Pending** status until an organization administrator approves the request.
    
    ![Pending custom URL request](../assets/img/administer/configure-domain/pending-custom-url-request.png)

### Approve a custom URL request

When a developer requests a custom URL, the request will be listed in the organization-level settings page under the **URL Settings** tab.

To approve a custom URL mapping, follow the steps given below:

!!! info "Note"
     To approve custom URL requests, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Pending URL Requests** tab. You will see all the pending URL mapping requests sent by developers.
    
    ![Pending URL requests](../assets/img/administer/configure-domain/pending-url-requests.png)


5. Go to the custom URL you want to approve and click the corresponding **Approve URL Mapping** icon under the **Action** column.
6. Review the details and click **Approve**.
   
   Once approved, the invoke URL of the component gets replaced with the configured custom URL.
    
   ![Custom URL](../assets/img/administer/configure-domain/custom-url.png)

   Now you have successfully utilized the configured custom domain to set up a custom URL for a component.


# Configure a User Store with the Built-In Identity Provider

Developers looking to experiment with a complete application development process that includes user authentication and authorization can utilize Choreo's built-in identity provider (IdP). Choreo's built-in identity provider allows you to seamlessly test your application's authentication by setting up test users and groups within Choreo. 

!!! note
     Although the built-in IdP facilitates user management support, it is limited to adding users with attributes and groups. Therefore, the built-in IdP user management capabilities are not recommended for use in production.

## Prerequisites

Before you try out the steps in this guide, be sure you have administrator rights to your Choreo organization. This permission is essential to configure a user store with the built-in IdP.

## Configure a Choreo built-in IdP user store

Follow the steps given below to configure a Choreo built-in IdP user store for an environment:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Organization** list and then click on your organization.
3. In the left navigation menu, click **Settings**. This takes you to your organization settings.
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. On the **Identity Providers** tab, click **Manage** in the **Choreo Built-in Identity Provider** pane.
6. In the Manage IdP pane, click on a specific environment tab depending on where you want to configure the built-in IdP user store.
7. You can download the sample **User store template file(.csv )** from the **User Store** section. The template file content is similar to the following:

   ```csv
   username,password,groups,first_name,last_name,email
   "demouser","password1","[manager, engineering]","John","Doe","john@acme.org"
   ```

!!! note
     The provided template file includes a sample user with associated attributes. To add new users, insert additional rows in the `.csv` file. To include more user attributes, add columns as required in the `.csv` file.
   
8. Specify appropriate user details in the template file and save it.
9. Select the template file that you saved and click **Upload**. A successful upload creates the user store and displays the configured users in the **Users** section.


# Configure Approvals for Choreo Workflows

Choreo allows you to configure approval processes for specific workflows within the platform. An approval process for a workflow ensures that critical or sensitive changes are properly managed and controlled.

Choreo currently allows you to configure approvals for environment promotion and API subscription workflows.

Configuring approvals for environment promotion allows authorized users to control components being promoted to a critical/production environment. 

Configuring approvals for the API subscription workflow allows you to create subscription plans that require approval before being activated. This feature allows you to control access to APIs by requiring administrative review and authorization of subscriptions before they become active.

## Permissions to review and respond to approval requests

Click the respective tab for details on permissions depending on the workflow for which you want to configure approvals:

=== "Environment promotion"

     To review and respond to environment promotion approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**: 
          - Approve component promotion requests: Grants access to review and approve the promotion of components to critical environments.
      - **PROJECT-MANAGEMENT**: Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

=== "API subscription"

     To review and respond to API subscription approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**:
          - Approve API subscriptions: Grants access to review and approve API subscription workflow requests.
      - **PROJECT-MANAGEMENT**: 
          Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

## Set up an approval process for a workflow

To set up an approval process for a workflow, follow these steps:

!!! note
     - You must have administrator privileges in Choreo to configure workflow approvals.
     - Administrators can designate specific roles and assignees to review and respond to requests associated with each workflow.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Workflows** tab.
5. Click the edit icon corresponding to the workflow for which you want to configure an approval.
6. In the **Configure Workflow** dialog that opens, select roles and assignees to review and respond to workflow approval requests.

    - In the **Roles** field, select one or more roles depending on your preference. Any user assigned to these roles can review and respond to requests.
    - In the **Assignees** field, select specific users who can review and approve workflow requests. Assignees can be any Choreo user, even if they are not assigned to a selected role.

    !!! info "Important"
         Currently, there is no validation to ensure that the specified roles and assignees have the necessary permissions to review and respond to requests. If the [required permissions](#permissions-to-review-and-respond-to-approval-requests) are not correctly configured, some users may receive email notifications but will be unable to review the requests.
         
7. Click **Save**. This configures and enables the approval process for the workflow.

Once you enable the approval process for a workflow, see the following details on how to submit a request for approval and the approval process. Click the respective tab depending on the workflow for which you enabled the approval process:  

=== "Environment promotion"

     Once you configure an approval process for environment promotion, developers must [submit a request for approval to use the workflow](../develop-components/submit-and-manage-workflow-approval-requests.md). An authorized assignee must then [review and approve the request](./review-workflow-approval-requests.md) for a developer to proceed with the task related to the workflow.

=== "API subscription"

     Once you configure an approval process for API subscription, administrators can select the **Approval required** checkbox to create or update subscription plans to require approval. For details, see [Create API Subscription Plans](../administer/create-api-subscription-plans.md). API consumers using these plans must request approval to proceed. For details, see step 7 in [Subscribe to an API with a Subscription Plan](../api-management/manage-api-traffic/subscribe-to-an-api-with-a-subscription-plan.md). An authorized approver must then [review and approve the request](./review-workflow-approval-requests.md) before the subscription is granted.


# Configure Enterprise Login

With Choreo, you can configure enterprise login to allow users from an external identity provider (IdP) to sign in to Choreo seamlessly without changing their credentials.

This guide walks you through the steps to configure enterprise login for your organization in Choreo. 


## Prerequisites 

Before you proceed with the configuration, set up the following:

- A valid email domain for your organization.
- Access the Choreo Console at https://console.choreo.dev/ via your Google, GitHub, or Microsoft account. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries". 

## Configure enterprise login for your Choreo organization

To configure enterprise login for your Choreo organization, follow the steps given below:

 - **If you already have a support account with us**, send us your organization name/handle and the email domains specific to your organization through our support portal. 

 - **If you do not have a support account with us yet**, send an email to `choreo-help@wso2.com` requesting to enable enterprise login for your organization. 
      
    !!! tip
        Ensure you include the following information in the request:

         - Organization name or handle. For example, “Stark Industries” or “starkindustries”.
         - Email domains specific to your organization. For example, “@stark.com”, “@starkindustries.com”, and “@stark.eu.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise login
        
        Hi CS team,

        I need to configure enterprise login for my organization. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries
          - Email domains specific to my organization: “@stark.com”, “@starkindustries.com”, and “@stark.eu”

        Thank you.

    The Choreo support team will perform the necessary configurations and respond to you with a verification code. You must sign in to your domain host account and configure the DNS record for your email domain with the following values:

    | **Field**                          | **Value**                                      |
    |------------------------------------|------------------------------------------------|
    | **Name/Host/Alias**                | Specify `@` or leave it blank                  |
    | **Time to Live (TTL)**             | Keep the default value or use `86400`          |
    | **Value/Answer/Destination**       | wso2-domain-verification:<`verification_code`> |


Now, you are ready to bring your own identity to Choreo.

## Bring your own identity to Choreo

When you create an organization in Choreo, an organization with the same name is provisioned for you in Asgardeo. To bring your own identity to Choreo, you must configure a federated enterprise IdP on Asgardeo in the organization that is provisioned for you.

Follow the steps given below to configure the federated IdP:

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. To configure a federated enterprise identity provider for your Asgardeo organization, follow the steps in [Asgardeo documentation - Add Standard-Based Login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/).
3. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
4. Click on the application to edit it.
5. Click the **Sign-in Method** tab. You can observe the configured connection.

Now, users in your enterprise IdP can sign in to the Choreo Console using their enterprise IDs.

## Configure role-based access control for enterprise login

To streamline the enterprise login process and grant appropriate permission, Choreo provides the flexibility to configure role-based access control for users who reside in an external IdP. 

To set up role-based access control for enterprise login within Choreo, follow the steps given below:

### Prerequisites

Before you proceed with the configuration, make sure you complete the following:

1. Configure enterprise login for your organization. For instructions, see [Configure enterprise login for your Choreo organization](#configure-enterprise-login-for-your-choreo-organization). 
2. Ensure your enterprise identity provider includes the group/role attributes in tokens it sends to Asgardeo via the respective protocol.
3. Be sure you have administrator privileges in Choreo.

### Step 1: Configure Asgardeo

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. [Configure your IdP as an external IdP in Asgardeo](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/). Depending on your IdP, you can select OpenID Connect or SAML as the protocol between Asgardeo and your IdP.

    !!! note
        If you are using OpenID Connect, configure the requested scopes accordingly for Asgardeo to get the relevant group/role details from the external IdP.

3. To configure the application, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
    2. Click on the application to edit it.
    3. Click the **Sign-in Method** tab.
    4. Configure the IdP for login depending on the protocol you selected:
        - For OpenID Connect, follow the instructions in [Enable the OIDC IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-oidc-idp-login/#enable-the-oidc-idp-for-login).
        - For SAML, follow the instructions in [Enable the SAML IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-saml-idp-login/#enable-the-saml-idp-for-login).
            
    5. Click the **User Attributes** tab.
    6. Select the **Groups** attribute and click the arrow to expand the section. Then, select the **Requested** checkbox.
    7. Click **Update**.

4. To add the user attributes as OpenID Connect scopes, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **New Attribute** and select the **Groups** attribute.
    4. Click **Save** and then click **Save Changes**.

### Step 2: Map Choreo groups to enterprise IdP groups via the Choreo Console 

!!! note
    
    Before you map Choreo groups to enterprise IdP groups, ensure you meet the following criteria:

    - Asgardeo is your key manager.
    - You have permission to perform actions of the organization administrator role.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. This takes you to the organization's home page.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. In the **Access Control** tab, click **Groups**. 
5. Click **Manage IdP Group Mapping**.
    ![Group mapping](../assets/img/administer/enterprise-login/group-mapping.png)

6. Click the edit icon corresponding to the Choreo group you want to map to the enterprise IdP group.
7. In the **IdP Group Name** field, specify the exact name you configured in the enterprise IdP and enter to add it.
   
    !!! tip
        If there is a change to the IdP group mapping, it takes effect from the next login session onwards. 

8. Click **Save**. 

By following these steps, you have successfully configured role-based access control for enterprise login in Choreo, allowing users from the external IdP to have the appropriate permission.


# Configure Self-Sign-Up

With Choreo, you can set up a self-sign-up page for your Developer Portal. The self-sign-up page allows users to easily access your Developer Portal and subscribe to APIs. When you configure self-sign-up, users can create their accounts and access your Developer Portal without any manual intervention from you.

This page walks you through the steps to configure self-sign-up for your Developer Portal.

## Prerequisites

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using your Google, GitHub, or Microsoft account.
2. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries".


## Configure Developer Portal self-sign-up

To configure self-sign-up, follow the steps given below:

1. Send an email to <choreo-help@wso2.com> requesting to configure enterprise IdP for the Developer Portal of your organization. 

    !!! tip
        Ensure you include the organization name or handle in the request.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise IdP for Developer Portal
        
        Hi CS team,

        I need to configure enterprise IdP for my organization’s Developer Portal to enable self-sign-up. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries

        Thank you

    The Choreo support team will perform the necessary configurations and respond to your request.

2. When you receive a response, sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials that you used to sign in to Choreo.
3. In the Asgardeo Console, click **View all applications**.

    ![View all applications](../assets/img/administer/self-sign-up/view-all-applications.png)

    You will see an application named **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL**. 

    ![Applications](../assets/img/administer/self-sign-up/application.png)

4. Click on the application to edit it and enter your organization’s Developer Portal URL as the **Access URL** of the application. For example, `https://devportal.choreo.dev/starkindustries`.
5. Click **Update**.
6. To add user attributes, follow these steps:

    !!! info "Note"
          If you have enabled enterprise login and you want to add the **Groups** attribute during self-sign-up configuration, avoid making it mandatory. This ensures proper access control and prevents unauthorized privileges. If you make the **Groups** attribute mandatory, it allows self-signed-up users to specify a group and assume roles associated with it.

    1. Click the **User Attributes** tab.
    2. To add the email as a mandatory user attribute, select **Email** and click the arrow to expand the section. Then, select the **Requested** and **Mandatory** checkboxes.

        ![Email attribute](../assets/img/administer/self-sign-up/email-attribute.png)

    3. To add the first name and last name as optional attributes, select **Profile** and click the arrow to expand the section. Then, select the **Requested** checkbox for the **First Name** and the **Last Name** attributes.

        ![Profile attribute](../assets/img/administer/self-sign-up/profile-attribute.png)

    4. Click **Update**.

7. To add the user attributes as OpenID Connect scopes, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **+ New Attribute**.
    4. Select **Email**, **First Name**, and **Last Name** as the attributes to associate with the OpenID scope.
    5. Click **Save** and then click **Save Changes**.

        ![Save attributes as scopes](../assets/img/administer/self-sign-up/save-attributes-as-scopes.png)

8. To configure basic authentication as the sign-in method, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Applications**.
    2. In the **Applications** pane, click the **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL** application to edit it.
    3. Click the **Sign-in Method** tab and then click **Start with default configuration**.

        ![Add sign-in method](../assets/img/administer/self-sign-up/add-sign-in-method.png)

    4. Click **Update**.

9.  To configure self-registration, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Self Registration**.
    2. In the **Self Registration** pane, click **Configure**.
    3. To enable self-registration, turn on the toggle.
    4. Select **Account verification**. This displays a confirmation message to enable account verification. 
    5. Click **Continue**.
    6. Specify an appropriate value in the **Account verification link expiry time** field.
    7. Click **Update**. 
     
        ![Configure self-registration](../assets/img/administer/self-sign-up/configure-self-registration.png)

Once you complete these steps, you will see a sign up link similar to the following in your Developer Portal:

![Sign-up](../assets/img/administer/self-sign-up/sign-up.png){.cInlineImage-half}
 
Users can click **LOGIN/SIGN UP** and then click **Create an account** to sign up to access your Developer Portal.

![Create an account](../assets/img/administer/self-sign-up/create-an-account.png)

## Manage new users

To manage users who want to access your Developer Portal via self-sign-up, you have two possible approaches:

- Enable auto-approval for new user registrations: This approach automates the user approval process.  When you enable auto-approval, each user who creates an account and signs up to your Developer Portal can access it by default.
- Manually approve or reject user accounts: This allows you to review the list of user registrations and manually approve or reject each registration as needed.

### Enable auto-approval for new user registrations

To automatically approve each new user account registered on your Developer Portal, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**.
4. To enable auto-approval, turn on the toggle.

Once you enable auto-approval, users can sign in to your Developer Portal and view your APIs and applications immediately after creating an account.

### Manually approve or reject user accounts

If you have not enabled auto-approval, you can manually approve or reject new user registrations. Once a user creates an account, Choreo sends an email to ask the user to confirm the account. To manually approve or reject user accounts, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**. You will see the user accounts listed for approval.
4. To approve a user account, click **Approve**. To reject an account, click **Reject**.

    - If you approve an account, the user will receive an email confirming the approval.
    - If you reject an account, the user will receive an email mentioning that their account is rejected. 

        !!! info "Note"
               A rejected user cannot sign up to your Developer Portal using the same account again.


# Control Access in the Choreo Console

In the Choreo Console, you have the ability to manage access to projects and the actions that can be performed within them. Administrators have the capability to restrict project access to specific user groups. This feature is useful when you need certain user groups to have access to particular projects or for a set of projects.

Choreo uses **Roles**, **Groups**, and a **Mapping level** to control access to the Choreo Console as follows: 

- **Role** : Role is a collection of permissions. Choreo has a predefined set of roles with permissions assigned to them. [Learn more](../choreo-concepts/organization.md#roles)
- **Group** : Group is a collection of users. A user group requires a role or multiple roles to be assigned to it so that the users in those groups get the relevant permissions via the assigned roles. [Learn more](../choreo-concepts/organization.md#groups)

- **Mapping level** : A mapping level defines the extent at which a role-group mapping can be done. Choreo has two defined resource levels.
    - **Organization** : You can assign a role to a group or associate a group with a role within the organization. This ensures that    
                         all users in a group inherit the permissions granted by that role across all organizational resources.
                         For example, if a user has edit_project permission at the organization mapping level, that user can edit all the projects in the organization.
    - **Project** : You can assign a role to a group or associate a group with a role within a specific project resource. This ensures 
                    that users in the group inherit the permissions granted by that role only within the context of the specified project.
                    For example, If a user has edit_project permission at the project mapping level, that user can only edit the specified project.


In Choreo, authorization operates by assigning a role to a group at a specified level. The level at which the role is assigned determines the extent of permissions granted to users.

!!! warning "Important"
    Avoid assigning multiple roles to a single user across different projects or levels (organization and project). Such assignments can grant users unintended permission to some projects, allowing them to perform tasks they shouldn't have access to. Therefore, it is recommended to assign only one role to a user across projects or levels to ensure proper access control.

!!! info
    In Choreo, organization-level permissions take precedence over project-level permissions.

To elaborate further, refer to the following diagram. 

The following diagram depicts a role-group assignment at a specific resource level. In the diagram, an admin user has assigned the Developer role to all members of the Engineering group within the Engineering Project. This grants users in the Engineering group the ability to perform all actions allowed by the Developer role within the Engineering Project.

![Console access control](../assets/img/administer/access-control-to-console.png)

## Sample scenario

Now that you understand the basic concepts of access control within the Choreo Console, let’s try out a sample scenario to manage access within a project. 

Assume you are overseeing the Engineering Project within your organization and you need to grant development access to specific users solely within this project. Here's a step-by-step guide on how to achieve this:

### Step 1: Create a project

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | `Engineering Project`              |
    | **Name**                 | `engineering-project`              |
    | **Project Description**  | `My sample project`                |

4. Click **Create**. This creates the project and takes you to the project home page.

### Step 2: Create a new group

Follow the steps given below to create a group with the name `Engineering Project Developer`:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. Click **+ Create Group**.
5. Enter a group name and group description. You can enter the values given below:

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Group Name**           | `Engineering Project Developer`    |
    | **Group Description**    | `Users with development access within the engineering project`|

6. Click **Create**.

### Step 3: Assign roles to the group

Follow the steps given below to assign the **Developer** role to the **Engineering Project Developer** group that you created:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the **Engineering Project** that you created.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. On the **Groups** tab, search for the **Engineering Project Developer** group and click the corresponding edit icon.
5. Click **+Add Roles**. 
6. In the **Add Roles to Group in Project** dialog that opens, click the **Roles** list and select **Developer**.
7. Click **Add**. This assigns the **Developer** role to the group. You should see the mapping level as **Project (Engineering Project)** as follows, indicating the scope of the mapping:

    ![Mapping level](../assets/img/administer/mapping-level.png)

   This means that you have granted developer access to users in the Engineering Project Developer group in the scope of the Engineering Project. 

Now that you have set up access control, you can proceed to add users to the new group.

### Step 4: Add users to the group

There are two approaches you can follow to add users to the group.

#### Add a new user as a project developer 

Follow the steps given below to add a new user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Click **+Invite Users**.
5. In the **Invite Users** dialog,
   1. Specify the email addresses of the users in the **Emails** field.
   2. Click the **Groups** list and select **Engineering Project Developer**.
6. Click **Invite**.

#### Add an existing user as a project developer 

Follow the steps given below to add an existing user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Search for the existing user you want to add to the **Engineering Project Developer** group.
5. Click the edit icon corresponding to the user.
6. Click **+Assign Groups**.
7. In the **Add Groups to User** dialog, click the **Groups** list and select **Engineering Project Developer**.
8. Click **Add**.

!!! tip
     Make sure to remove the user from any other groups to avoid granting organization-level access unintentionally.


!!! note
     - Existing groups are already mapped to similar roles at the organization level. Therefore, adding users to those groups or keeping users in them, will give organization-level access to the users.
     - When users are added to the **Engineering Project Developer** group, they will only have developer access to the **Engineering Project**.
     - You can invite new users or add existing users to new groups within the Engineering Project, and based on their requirements, assign roles like Developer, API Publisher, etc.

Now you have successfully set up access control within your project.


# Control Egress Traffic for Your Organization

In Choreo, you can manage egress traffic originating from your applications by setting up an allow list or deny list. By default, egress traffic is allowed to any destination unless specifically restricted.

## Configure an egress policy at the organization level

To configure an egress policy at the organization level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Egress Control** tab.
5. Click **+ Create** to add a new egress policy.
6. Select the type of egress control to apply and add the required rules:

    - **Allow All**: Allows all egress traffic by default. You can selectively block traffic to specific IP ranges.
    - **Deny All**: Blocks all egress traffic by default. You can selectively allow traffic to specific IP ranges or domains.

        !!! note

             - Once you select an egress control type and create a rule, you cannot change the type. To change the type, you must delete existing rules.
             - Egress rules you add can disrupt your application if they block traffic to required destinations. Ensure you add rules appropriately to prevent such disruptions.
             - If you use the **Deny All** type, be sure to add Choreo-managed database hosts to the allowed list.
             - Egress policies apply across all environments in an organization.
             - Egress policies do not apply to API proxies.

    ![Configure an organization-level egress policy](../assets/img/administer/configure-an-organization-level-egress-policy.png)

## Override the organization-level egress policy at the project level

An egress policy set at the project level can override the organization-level policy, depending on the egress control type you select.

To override the organization-level egress policy at the project level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Project** list and select your project.
3. In the left navigation menu, click **Settings**. This opens the project-level settings page.
4. Click the **Egress Control** tab. You will see that the organization-level egress policy is enforced by default.
5. Add required project-level rules to further restrict egress traffic.

    - If the **Allow All** egress control type is selected at the organization level, you can add project-level deny rules to further restrict traffic.
    - If the **Deny All** egress control type is selected at the organization level, you can remove allow rules inherited from the organization level to further restrict traffic.

    ![Add project-level rules](../assets/img/administer/add-project-level-rules.png)


# Create API Subscription Plans

API subscription plans are essential to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security. With the option to set rate limits and burst control, subscription plans allow API providers to manage traffic, prevent misuse, and offer tiered service levels. Organizations can implement subscription plans to provide varying levels of API access, accommodating different user needs and business models, while ensuring optimal performance and security. 

In Choreo, users with the administrator role can create, update, and delete subscription plans at the organization level. 

!!! tip
    Deleting a subscription plan is only possible if there are no active subscriptions associated with it.  

To create an organization-level subscription plan, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **API Management** tab and then click **Subscription Plans**.
5. Click **+ Add Subscription Plan**.
6. In the **Create Subscription Plan** pane, enter the appropriate values for each field:
    
    !!! note
         - In the **Name** field, you must specify a name to uniquely identify the subscription plan in various contexts. The value is editable only at the time you create the subscription plan. You cannot change the name after you create it.
         - The **Stop on Quota Reach** checkbox is selected by default when creating a subscription plan. When selected, requests return an HTTP 429 response if the request count exceeds the limit. If you clear the checkbox, requests are allowed even if the quota is exceeded.
         - Burst control protects your backend from sudden request spikes and manages API usage. It’s especially useful for subscription plans where the request count is enforced over a long period, to prevent consumers from using their entire quota too quickly. Ensure you select the **Burst Control** checkbox when the **Request Count Time Unit** is selected as **Hour** or **Day**.
         - Select the **Approval required** checkbox if subscription requests made to this plan require administrator or API publisher approval to activate the plan. This allows for manual review and approval of a subscription before granting API access.
  
    ![Create subscription plan](../assets/img/administer/create-subscription-plan.png)

7. Click **Create**. This creates the subscription plan and lists it under **Subscription Plans**.

After creating subscription plans, users with the API publisher role can [assign subscription plans to APIs](../api-management/manage-api-traffic/assign-subscription-plans-to-apis.md). API consumers can then choose the appropriate subscription plan during the subscription process depending on their requirements.


# Customize the Developer Portal

The Developer Portal allows API consumers to find and consume APIs with ease. You can change the look and feel of your Developer Portal by changing the theme to match your brand. Doing so will help you give a better developer experience to your users.

To customize the Developer Portal theme, follow the steps given below:

!!! Note
    - To customize the Developer Portal theme for an organization, you need to be an admin user of that organization.
    - You cannot undo a change and restore or revert to a previous version of the theme. However, you can reset it to the default theme.

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google/ GitHub/ Microsoft account.


2. In the left pane, click **Settings**.

4. In the header, click the **Organization** list. This will open the organization level settings page. 

5. In the **API Management** tab, click **Devportal Theme**.

    ![Access Devportal theme](../assets/img/administer/devportal-theme/access-devportal-theme.png){.cInlineImage-threeQuarter}

    Once you access the theme, you can customize the **Home** page, color theme, font, header and footer, logos, etc., by expanding the relevant sections.

6. Make a change to the theme. For example, let's change the title on the **Home** page and the color theme. 

    1. To update the title on the **Home** page, expand the **Home Page** section, and in the **Title** field, change the default text (for example, to `Try our APIs!`).
   
    2. To update the color theme, expand the **Color Palette** section, and change the colors as required (for example, change the background color to `#C3C5CD` and the primary color of the buttons to `#086634`).
   
    3. Click **Preview** to view a preview of the Developer Portal with the changes you made. Based on the changes given in the examples, the preview appears as follows.

         ![Preview of customization](../assets/img/administer/devportal-theme/preview-of-customization.png){.cInlineImage-threeQuarter}
   
    4. Click **Save** to save your changes as a draft theme.
    
    5. To apply the changes to the Developer Portal, toggle the **Go Live** switch. To confirm that you want to go live with the changes, click **Enable** in the message that appears.
    	
7. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).

The **Home** page will appear as it did in the preview.

## Reset the Developer Portal theme

To reset the Developer Portal theme to the default theme, follow the steps given below:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google, GitHub, or Microsoft account.

2. In the left pane, click **Settings**.

3. In the header, click the **Organization** list. This will open the organization level settings page. 

4. In the **Organization** tab, click **Devportal Theme**, and then click **Reset to Default**.



## Inviting users

An organization administrator can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Manage Members of an Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a user of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a user of that organization.

{% include "inviting-members.md" %}

## Manage user permission

For details on how Choreo manages user permission, see [Manage user permission](../choreo-concepts/organization.md#manage-user-permission).


# Review Workflow Approval Requests

In Choreo, administrators can [configure approvals for workflows](./configure-approvals-for-choreo-workflows.md) and assign specific users as approvers.

If you are assigned as an authorized reviewer for a particular workflow approval request, you will receive an email notification when a [request is submitted for approval](../develop-components/submit-and-manage-workflow-approval-requests.md). The email includes a summary of the request and a link to the **Approvals** page in the Choreo Console, where you can review the details and either approve or reject the request.

!!! note
     - Workflow approvals are managed at the project level. If a role with the necessary permissions is assigned in a project context, only members of the user group bound to that role within the specific project will receive notifications for requests made in that project. For example, if you are assigned the Project Admin role (which includes the necessary permissions) for project A, you will only be notified of workflow requests within project A.
     - Users with organization-level permissions will receive notifications for all workflow requests across any project in the organization.

Other approvers within your organization will also receive notifications for workflow requests and may review a request before you. If a request has already been reviewed, it will appear under the **Past** tab on the **Approvals** page.

Approval requests are submitted on behalf of the team. Once approved, any authorized team member can execute the task. For certain tasks, execution may occur automatically upon approval.

## View workflow approval requests

To view workflow approval requests assigned to you, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Approvals**. This opens the **Approvals** page where you can see all approval requests assigned to you. The **Pending** tab lists requests that are yet to be reviewed. The **Past** tab displays requests already reviewed by you or other approvers, as well as requests canceled by the requester.
4. To view details of a specific request, click **Review** corresponding to it.

## Approve or reject an approval request

To approve or reject a request, follow these steps:

1. Follow the instructions in the [View workflow approval requests](#view-workflow-approval-requests) section above to see details of the workflow you want to review.
   Alternatively, click the Choreo Console link in the approval request email notification you received. This takes you to the request details in the Choreo Console.
2. Review the request and click **Approve** or **Reject** based on your decision.



# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Choreo, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Choreo, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Add Asgardeo as an external IdP in Choreo

Follow the steps below to add Asgardeo as an external IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list.

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Choreo.


# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

In organizations leveraging Microsoft Azure Active Directory (Azure AD) for identity and access management (IAM), integrating it with Choreo offers powerful API access control. This control hinges on the use of API scopes. That is, it enables the restriction of access to a designated group of users. This document guide you step-by-step to configure Azure AD as your external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- An Azure Active Directory account:  If you don’t already have one,  setup an Azure Active Directory account at [https://azure.microsoft.com/en-gb/](https://azure.microsoft.com/en-gb/).
- Administrator rights to your Choreo organization: You need this to configure the Azure AD account in your organization.

## Add Azure Active Directory as an external IdP in Choreo

Follow the steps below to add Azure AD as an IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Microsoft Entra ID (Azure AD)** as the Identity Provider. 
6. Provide a name and a description for the IdP. 
7. To obtain the `Well-Known URL` of your Azure AD instance, on your Azure account, under **Azure Active Directory** go to **App registrations**, and then **Endpoints**. Copy the URI under`OpenID Connect metadata document`.
    
    !!! info
        - In azure, there are two versions of access tokens available. By default, the IDP applications you create use the v1 access token. Therefore, if you intend to use the v1 access token, when providing the `Well-Known URL`, omit the v2.0 path segment from the URL. [Learn more](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats)
        For example, convert `https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration`-> `https://login.microsoftonline.com/<tenant-id>/.well-known/openid-configuration`
        - If you intend to work with v2.0, then the IDP application's manifest should be changed as explained in the [access tokendocumentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats). 
        
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Review the endpoints and click **Next**.




# Configure a Custom Domain for Your Organization

A custom domain is essential for effective branding, discoverability, and credibility of a website. Choreo allows you to easily configure custom domains for your organization, enabling developers to utilize it to configure custom URLs for their components such as API proxies, services, web applications, and webhooks.

This section provides an overview of Choreo’s custom domain configuration model and guides you through configuring a custom domain for your organization. It also walks you through utilizing a custom domain to configure a custom URL for a component.

## Choreo custom domain configuration model

Choreo allows organization administrators to add custom domains for their organizations. When an administrator adds custom domains to an organization, component developers can submit requests to utilize the custom domains for their respective components. These requests require approval from the organization administrator. Upon approval, the custom domain and the relevant URL customization become available to the component.

## Configure a custom domain for an organization

### Prerequisites

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Create an organization in Choreo.
    
    ![Create an organization in Choreo](../assets/img/administer/create-choreo-organization.png)

### Add a custom domain

To add a custom domain for your organization, follow the steps given below:

!!! info "Note"
     To add a custom domain, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Active Domains** tab.
5. Click **+ Add Domains**. 
6. In the **Add a Custom Domain** pane, do the following:
    1. Enter your domain name.
    2. Select the environment to apply the domain name.
    3. Select the entity type to apply the domain name.

        !!! tip
             In this context:

              - The **API** entity type represents Choreo components exposed via an endpoint, including API Proxy, Service, and Webhook components.
              - The **Web App** entity type represents the Web Application component.
       
 7. Take a look at the generated CNAME target value displayed and create a DNS record associating the domain name to the CNAME target value with your DNS provider.
    
    ![CNAME target value](../assets/img/administer/configure-domain/cname-target-value.png)

    !!! info
          When you select **Developer Portal** as the type, the environment is not applicable, and the CNAME alias will be displayed as follows:
           ![Developer Portal CNAME target value](../assets/img/administer/configure-domain/developer-portal-cname-target-value.png)

 8. Once the CNAME type DNS record is created, click **Verify**.

    !!! info "Note"
          If the CNAME mapping is correct, the verification completes successfully. It can take some time for the configured CNAME mapping to be globally available.

 9. On successful verification of the custom domain, click **Next**.
 10. Select a TLS certificate provider depending on your preference. You can either import the TLS certificates you created for the custom domain or click **Let's Encrypt** to allow Choreo to generate and manage the certificates for you.

    !!! note "If you want to import your own certificate, it should adhere to specific guidelines"
          - TLS certificate guidelines:
             - It should be issued by a certificate authority (CA) and should contain the domain's public key along with additional information such as the domain name, the company that owns the domain, the certificate's expiration date, and the digital signature of the issuing CA.
             - It should be an X509 certificate.
             - It should be in the PEM format.
             - It should be issued directly or through a wildcard entry for the provided custom URL. For example,
                - For direct issuance, the SSL file must include the exact domain name. For example, if the domain is `apis.choreo.dev`, the SSL file must include `apis.choreo.com`.
                - For wildcard entries, the SSL file should use a wildcard notation to cover all subdomains under the provided URL. For example, if the CNAME is `apis.choreo.dev`, the SSL file should use `*.choreo.dev`.
          - TLS key file guidelines:
             - It should be in the PEM format.
             - It must be encrypted using RSA encryption.
          - Certificate chain file guidelines:
             - The chain file, which is essential for some clients to verify the authenticity of a server's SSL/TLS certificate, should contain your domain's SSL/TLS certificate (optional, as this can be provided via the certificate itself) and one or more intermediate certificates in the correct order, leading back to a root certificate. 
             - All certificates in the chain should be X509 certificates in PEM format.
               <details><summary>For step-by-step instructions on constructing a certificate chain with a root certificate, click here</summary>
               To construct a certificate chain with a root certificate, you must organize and combine the certificates in the correct sequence. A typical certificate chain consists of the following:
                 - **Root certificate**: The trusted self-signed certificate issued by the certificate authority (CA).
                 - **Intermediate certificates** (if any): Certificates issued by the root CA to subordinate CAs.
                 - **Leaf certificate**: Your end-entity certificate issued by the CA. This is an optional certificate that may be included within the chain or provided separately.<br><br>
                Follow these steps to construct the certificate chain:
                    1. Obtain and organize your certificates in the correct order:
                        - **Leaf certificate**: The public certificate issued by the CA. This is optional and may be included within the chain or provided separately.
                        - **Intermediate certificates**: Obtain these from the CA, if applicable.
                        - **Root certificate**: Obtain this from the CA.  If it is self-signed, it serves as the trust anchor.
                    2. Combine the certificates into a single file in the following order:
                        - Leaf certificate: This is your public certificate issued by the CA.
                        - Intermediate certificates if applicable: Include these in the correct hierarchical order.
                        - Root certificate: Include this at the end of the file.<br><br>
                        Use a text editor or a command-line tool to concatenate the certificates into one file, ensuring each certificate begins and ends with the proper markers. Also make sure the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers appear on a new line:
                    ```
                     -----BEGIN CERTIFICATE-----
                     <Leaf Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Intermediate Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Root Certificate Content>
                     -----END CERTIFICATE-----
                    ```
                    3. Save the concatenated file. You can save it with a name such as `certificate_chain.pem`.
                    4. Use the following command to verify that your certificate chain is constructed correctly:
                    ```
                    openssl verify -CAfile <root_or_bundle_cert>.pem certificate_chain.pem
                    ```
                    Replace `<root_or_bundle_cert>.pem` with the path to your root certificate or a bundle containing both the root and intermediate certificates.
                    5. Once the certificate chain is verified, upload it via the Choreo Console:
                        ![Upload certificate chain](../assets/img/administer/configure-domain/upload-certificate-chain.png)
                        - If the constructed chain includes the leaf certificate, follow these steps:
                            - Upload the constructed certificate chain in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Do not upload a certificate chain file, as it is already included in the TLS certificate.
                        - If the constructed chain does not include the leaf certificate, follow these steps:
                            - Upload the leaf certificate in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Upload the constructed certificate chain in the **Certificate Chain File** field.
 
     To proceed with this step in this guide, click **Let's Encrypt**.

 11. To save the custom domain, click **Add**.
 
Now, you have successfully added a custom domain for your organization.

You can see the added custom domain listed in the **Active Domains** tab under the URL **Settings** tab.
    
 ![Active domains](../assets/img/administer/configure-domain/active-domains.png)

The custom domain you added will be available to the entity types in the specified environment. You can request the custom domain when configuring a custom URL for a component.

!!! info "Note"
     If you add a custom domain for the **Developer Portal** type, the customization is applied immediately, and you can access the organization’s Developer Portal via the added domain.

If you want to view the entity types that use a particular custom domain, click the specific custom domain listed in the **Active Domains** tab under **URL Settings**.
 
## Configure a custom URL for a component

When an organization administrator adds custom domains for specific environments, developers can request any available custom domain to configure a custom URL for a component in a specific environment.

### Request a custom URL for a component

To request a custom URL for your component, follow the steps given below:

!!! info "Note"
     Before you request a custom domain for a specific environment, ensure that the component is deployed to that environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to customize the URL.
3. In the left navigation menu, click **Settings**. This opens the component-level settings page.
4. Click the **URL Settings** tab. This displays the active deployments of the component across different environments and indicates whether a custom URL is configured. If an active custom domain is available to configure a custom URL for a component in a specific environment, the **Edit URL Mapping** icon in the corresponding **Action** column becomes enabled.
    
    ![Active deployments](../assets/img/administer/configure-domain/active-deployments.png)

5. To configure a custom URL for a component in a specific environment, click the **Edit URL Mapping** icon under the **Action** column corresponding to the respective environment. This opens the **URL Settings** dialog, where you can specify values to request for a custom URL.
    
    ![URL settings](../assets/img/administer/configure-domain/url-settings.png)

6. In the **URL Settings** dialog, select a domain to configure a custom URL.

    !!! tip
          - The **Domain** drop-down lists the available domains for the component. You can  request for any listed domain.
          - If you want to request a custom URL for an API, you must specify an appropriate context path in the **Path** field. The **Path** field displays the default context path for the API. You can edit the path depending on your preference. 

7. Click **Configure**. This creates the custom URL mapping, which you can see under the **URL Settings** tab.  The custom URL request will be in the **Pending** status until an organization administrator approves the request.
    
    ![Pending custom URL request](../assets/img/administer/configure-domain/pending-custom-url-request.png)

### Approve a custom URL request

When a developer requests a custom URL, the request will be listed in the organization-level settings page under the **URL Settings** tab.

To approve a custom URL mapping, follow the steps given below:

!!! info "Note"
     To approve custom URL requests, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Pending URL Requests** tab. You will see all the pending URL mapping requests sent by developers.
    
    ![Pending URL requests](../assets/img/administer/configure-domain/pending-url-requests.png)


5. Go to the custom URL you want to approve and click the corresponding **Approve URL Mapping** icon under the **Action** column.
6. Review the details and click **Approve**.
   
   Once approved, the invoke URL of the component gets replaced with the configured custom URL.
    
   ![Custom URL](../assets/img/administer/configure-domain/custom-url.png)

   Now you have successfully utilized the configured custom domain to set up a custom URL for a component.


# Configure a User Store with the Built-In Identity Provider

Developers looking to experiment with a complete application development process that includes user authentication and authorization can utilize Choreo's built-in identity provider (IdP). Choreo's built-in identity provider allows you to seamlessly test your application's authentication by setting up test users and groups within Choreo. 

!!! note
     Although the built-in IdP facilitates user management support, it is limited to adding users with attributes and groups. Therefore, the built-in IdP user management capabilities are not recommended for use in production.

## Prerequisites

Before you try out the steps in this guide, be sure you have administrator rights to your Choreo organization. This permission is essential to configure a user store with the built-in IdP.

## Configure a Choreo built-in IdP user store

Follow the steps given below to configure a Choreo built-in IdP user store for an environment:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Organization** list and then click on your organization.
3. In the left navigation menu, click **Settings**. This takes you to your organization settings.
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. On the **Identity Providers** tab, click **Manage** in the **Choreo Built-in Identity Provider** pane.
6. In the Manage IdP pane, click on a specific environment tab depending on where you want to configure the built-in IdP user store.
7. You can download the sample **User store template file(.csv )** from the **User Store** section. The template file content is similar to the following:

   ```csv
   username,password,groups,first_name,last_name,email
   "demouser","password1","[manager, engineering]","John","Doe","john@acme.org"
   ```

!!! note
     The provided template file includes a sample user with associated attributes. To add new users, insert additional rows in the `.csv` file. To include more user attributes, add columns as required in the `.csv` file.
   
8. Specify appropriate user details in the template file and save it.
9. Select the template file that you saved and click **Upload**. A successful upload creates the user store and displays the configured users in the **Users** section.


# Configure Approvals for Choreo Workflows

Choreo allows you to configure approval processes for specific workflows within the platform. An approval process for a workflow ensures that critical or sensitive changes are properly managed and controlled.

Choreo currently allows you to configure approvals for environment promotion and API subscription workflows.

Configuring approvals for environment promotion allows authorized users to control components being promoted to a critical/production environment. 

Configuring approvals for the API subscription workflow allows you to create subscription plans that require approval before being activated. This feature allows you to control access to APIs by requiring administrative review and authorization of subscriptions before they become active.

## Permissions to review and respond to approval requests

Click the respective tab for details on permissions depending on the workflow for which you want to configure approvals:

=== "Environment promotion"

     To review and respond to environment promotion approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**: 
          - Approve component promotion requests: Grants access to review and approve the promotion of components to critical environments.
      - **PROJECT-MANAGEMENT**: Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

=== "API subscription"

     To review and respond to API subscription approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**:
          - Approve API subscriptions: Grants access to review and approve API subscription workflow requests.
      - **PROJECT-MANAGEMENT**: 
          Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

## Set up an approval process for a workflow

To set up an approval process for a workflow, follow these steps:

!!! note
     - You must have administrator privileges in Choreo to configure workflow approvals.
     - Administrators can designate specific roles and assignees to review and respond to requests associated with each workflow.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Workflows** tab.
5. Click the edit icon corresponding to the workflow for which you want to configure an approval.
6. In the **Configure Workflow** dialog that opens, select roles and assignees to review and respond to workflow approval requests.

    - In the **Roles** field, select one or more roles depending on your preference. Any user assigned to these roles can review and respond to requests.
    - In the **Assignees** field, select specific users who can review and approve workflow requests. Assignees can be any Choreo user, even if they are not assigned to a selected role.

    !!! info "Important"
         Currently, there is no validation to ensure that the specified roles and assignees have the necessary permissions to review and respond to requests. If the [required permissions](#permissions-to-review-and-respond-to-approval-requests) are not correctly configured, some users may receive email notifications but will be unable to review the requests.
         
7. Click **Save**. This configures and enables the approval process for the workflow.

Once you enable the approval process for a workflow, see the following details on how to submit a request for approval and the approval process. Click the respective tab depending on the workflow for which you enabled the approval process:  

=== "Environment promotion"

     Once you configure an approval process for environment promotion, developers must [submit a request for approval to use the workflow](../develop-components/submit-and-manage-workflow-approval-requests.md). An authorized assignee must then [review and approve the request](./review-workflow-approval-requests.md) for a developer to proceed with the task related to the workflow.

=== "API subscription"

     Once you configure an approval process for API subscription, administrators can select the **Approval required** checkbox to create or update subscription plans to require approval. For details, see [Create API Subscription Plans](../administer/create-api-subscription-plans.md). API consumers using these plans must request approval to proceed. For details, see step 7 in [Subscribe to an API with a Subscription Plan](../api-management/manage-api-traffic/subscribe-to-an-api-with-a-subscription-plan.md). An authorized approver must then [review and approve the request](./review-workflow-approval-requests.md) before the subscription is granted.


# Configure Enterprise Login

With Choreo, you can configure enterprise login to allow users from an external identity provider (IdP) to sign in to Choreo seamlessly without changing their credentials.

This guide walks you through the steps to configure enterprise login for your organization in Choreo. 


## Prerequisites 

Before you proceed with the configuration, set up the following:

- A valid email domain for your organization.
- Access the Choreo Console at https://console.choreo.dev/ via your Google, GitHub, or Microsoft account. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries". 

## Configure enterprise login for your Choreo organization

To configure enterprise login for your Choreo organization, follow the steps given below:

 - **If you already have a support account with us**, send us your organization name/handle and the email domains specific to your organization through our support portal. 

 - **If you do not have a support account with us yet**, send an email to `choreo-help@wso2.com` requesting to enable enterprise login for your organization. 
      
    !!! tip
        Ensure you include the following information in the request:

         - Organization name or handle. For example, “Stark Industries” or “starkindustries”.
         - Email domains specific to your organization. For example, “@stark.com”, “@starkindustries.com”, and “@stark.eu.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise login
        
        Hi CS team,

        I need to configure enterprise login for my organization. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries
          - Email domains specific to my organization: “@stark.com”, “@starkindustries.com”, and “@stark.eu”

        Thank you.

    The Choreo support team will perform the necessary configurations and respond to you with a verification code. You must sign in to your domain host account and configure the DNS record for your email domain with the following values:

    | **Field**                          | **Value**                                      |
    |------------------------------------|------------------------------------------------|
    | **Name/Host/Alias**                | Specify `@` or leave it blank                  |
    | **Time to Live (TTL)**             | Keep the default value or use `86400`          |
    | **Value/Answer/Destination**       | wso2-domain-verification:<`verification_code`> |


Now, you are ready to bring your own identity to Choreo.

## Bring your own identity to Choreo

When you create an organization in Choreo, an organization with the same name is provisioned for you in Asgardeo. To bring your own identity to Choreo, you must configure a federated enterprise IdP on Asgardeo in the organization that is provisioned for you.

Follow the steps given below to configure the federated IdP:

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. To configure a federated enterprise identity provider for your Asgardeo organization, follow the steps in [Asgardeo documentation - Add Standard-Based Login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/).
3. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
4. Click on the application to edit it.
5. Click the **Sign-in Method** tab. You can observe the configured connection.

Now, users in your enterprise IdP can sign in to the Choreo Console using their enterprise IDs.

## Configure role-based access control for enterprise login

To streamline the enterprise login process and grant appropriate permission, Choreo provides the flexibility to configure role-based access control for users who reside in an external IdP. 

To set up role-based access control for enterprise login within Choreo, follow the steps given below:

### Prerequisites

Before you proceed with the configuration, make sure you complete the following:

1. Configure enterprise login for your organization. For instructions, see [Configure enterprise login for your Choreo organization](#configure-enterprise-login-for-your-choreo-organization). 
2. Ensure your enterprise identity provider includes the group/role attributes in tokens it sends to Asgardeo via the respective protocol.
3. Be sure you have administrator privileges in Choreo.

### Step 1: Configure Asgardeo

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. [Configure your IdP as an external IdP in Asgardeo](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/). Depending on your IdP, you can select OpenID Connect or SAML as the protocol between Asgardeo and your IdP.

    !!! note
        If you are using OpenID Connect, configure the requested scopes accordingly for Asgardeo to get the relevant group/role details from the external IdP.

3. To configure the application, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
    2. Click on the application to edit it.
    3. Click the **Sign-in Method** tab.
    4. Configure the IdP for login depending on the protocol you selected:
        - For OpenID Connect, follow the instructions in [Enable the OIDC IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-oidc-idp-login/#enable-the-oidc-idp-for-login).
        - For SAML, follow the instructions in [Enable the SAML IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-saml-idp-login/#enable-the-saml-idp-for-login).
            
    5. Click the **User Attributes** tab.
    6. Select the **Groups** attribute and click the arrow to expand the section. Then, select the **Requested** checkbox.
    7. Click **Update**.

4. To add the user attributes as OpenID Connect scopes, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **New Attribute** and select the **Groups** attribute.
    4. Click **Save** and then click **Save Changes**.

### Step 2: Map Choreo groups to enterprise IdP groups via the Choreo Console 

!!! note
    
    Before you map Choreo groups to enterprise IdP groups, ensure you meet the following criteria:

    - Asgardeo is your key manager.
    - You have permission to perform actions of the organization administrator role.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. This takes you to the organization's home page.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. In the **Access Control** tab, click **Groups**. 
5. Click **Manage IdP Group Mapping**.
    ![Group mapping](../assets/img/administer/enterprise-login/group-mapping.png)

6. Click the edit icon corresponding to the Choreo group you want to map to the enterprise IdP group.
7. In the **IdP Group Name** field, specify the exact name you configured in the enterprise IdP and enter to add it.
   
    !!! tip
        If there is a change to the IdP group mapping, it takes effect from the next login session onwards. 

8. Click **Save**. 

By following these steps, you have successfully configured role-based access control for enterprise login in Choreo, allowing users from the external IdP to have the appropriate permission.


# Configure Self-Sign-Up

With Choreo, you can set up a self-sign-up page for your Developer Portal. The self-sign-up page allows users to easily access your Developer Portal and subscribe to APIs. When you configure self-sign-up, users can create their accounts and access your Developer Portal without any manual intervention from you.

This page walks you through the steps to configure self-sign-up for your Developer Portal.

## Prerequisites

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using your Google, GitHub, or Microsoft account.
2. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries".


## Configure Developer Portal self-sign-up

To configure self-sign-up, follow the steps given below:

1. Send an email to <choreo-help@wso2.com> requesting to configure enterprise IdP for the Developer Portal of your organization. 

    !!! tip
        Ensure you include the organization name or handle in the request.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise IdP for Developer Portal
        
        Hi CS team,

        I need to configure enterprise IdP for my organization’s Developer Portal to enable self-sign-up. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries

        Thank you

    The Choreo support team will perform the necessary configurations and respond to your request.

2. When you receive a response, sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials that you used to sign in to Choreo.
3. In the Asgardeo Console, click **View all applications**.

    ![View all applications](../assets/img/administer/self-sign-up/view-all-applications.png)

    You will see an application named **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL**. 

    ![Applications](../assets/img/administer/self-sign-up/application.png)

4. Click on the application to edit it and enter your organization’s Developer Portal URL as the **Access URL** of the application. For example, `https://devportal.choreo.dev/starkindustries`.
5. Click **Update**.
6. To add user attributes, follow these steps:

    !!! info "Note"
          If you have enabled enterprise login and you want to add the **Groups** attribute during self-sign-up configuration, avoid making it mandatory. This ensures proper access control and prevents unauthorized privileges. If you make the **Groups** attribute mandatory, it allows self-signed-up users to specify a group and assume roles associated with it.

    1. Click the **User Attributes** tab.
    2. To add the email as a mandatory user attribute, select **Email** and click the arrow to expand the section. Then, select the **Requested** and **Mandatory** checkboxes.

        ![Email attribute](../assets/img/administer/self-sign-up/email-attribute.png)

    3. To add the first name and last name as optional attributes, select **Profile** and click the arrow to expand the section. Then, select the **Requested** checkbox for the **First Name** and the **Last Name** attributes.

        ![Profile attribute](../assets/img/administer/self-sign-up/profile-attribute.png)

    4. Click **Update**.

7. To add the user attributes as OpenID Connect scopes, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **+ New Attribute**.
    4. Select **Email**, **First Name**, and **Last Name** as the attributes to associate with the OpenID scope.
    5. Click **Save** and then click **Save Changes**.

        ![Save attributes as scopes](../assets/img/administer/self-sign-up/save-attributes-as-scopes.png)

8. To configure basic authentication as the sign-in method, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Applications**.
    2. In the **Applications** pane, click the **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL** application to edit it.
    3. Click the **Sign-in Method** tab and then click **Start with default configuration**.

        ![Add sign-in method](../assets/img/administer/self-sign-up/add-sign-in-method.png)

    4. Click **Update**.

9.  To configure self-registration, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Self Registration**.
    2. In the **Self Registration** pane, click **Configure**.
    3. To enable self-registration, turn on the toggle.
    4. Select **Account verification**. This displays a confirmation message to enable account verification. 
    5. Click **Continue**.
    6. Specify an appropriate value in the **Account verification link expiry time** field.
    7. Click **Update**. 
     
        ![Configure self-registration](../assets/img/administer/self-sign-up/configure-self-registration.png)

Once you complete these steps, you will see a sign up link similar to the following in your Developer Portal:

![Sign-up](../assets/img/administer/self-sign-up/sign-up.png){.cInlineImage-half}
 
Users can click **LOGIN/SIGN UP** and then click **Create an account** to sign up to access your Developer Portal.

![Create an account](../assets/img/administer/self-sign-up/create-an-account.png)

## Manage new users

To manage users who want to access your Developer Portal via self-sign-up, you have two possible approaches:

- Enable auto-approval for new user registrations: This approach automates the user approval process.  When you enable auto-approval, each user who creates an account and signs up to your Developer Portal can access it by default.
- Manually approve or reject user accounts: This allows you to review the list of user registrations and manually approve or reject each registration as needed.

### Enable auto-approval for new user registrations

To automatically approve each new user account registered on your Developer Portal, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**.
4. To enable auto-approval, turn on the toggle.

Once you enable auto-approval, users can sign in to your Developer Portal and view your APIs and applications immediately after creating an account.

### Manually approve or reject user accounts

If you have not enabled auto-approval, you can manually approve or reject new user registrations. Once a user creates an account, Choreo sends an email to ask the user to confirm the account. To manually approve or reject user accounts, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**. You will see the user accounts listed for approval.
4. To approve a user account, click **Approve**. To reject an account, click **Reject**.

    - If you approve an account, the user will receive an email confirming the approval.
    - If you reject an account, the user will receive an email mentioning that their account is rejected. 

        !!! info "Note"
               A rejected user cannot sign up to your Developer Portal using the same account again.


# Control Access in the Choreo Console

In the Choreo Console, you have the ability to manage access to projects and the actions that can be performed within them. Administrators have the capability to restrict project access to specific user groups. This feature is useful when you need certain user groups to have access to particular projects or for a set of projects.

Choreo uses **Roles**, **Groups**, and a **Mapping level** to control access to the Choreo Console as follows: 

- **Role** : Role is a collection of permissions. Choreo has a predefined set of roles with permissions assigned to them. [Learn more](../choreo-concepts/organization.md#roles)
- **Group** : Group is a collection of users. A user group requires a role or multiple roles to be assigned to it so that the users in those groups get the relevant permissions via the assigned roles. [Learn more](../choreo-concepts/organization.md#groups)

- **Mapping level** : A mapping level defines the extent at which a role-group mapping can be done. Choreo has two defined resource levels.
    - **Organization** : You can assign a role to a group or associate a group with a role within the organization. This ensures that    
                         all users in a group inherit the permissions granted by that role across all organizational resources.
                         For example, if a user has edit_project permission at the organization mapping level, that user can edit all the projects in the organization.
    - **Project** : You can assign a role to a group or associate a group with a role within a specific project resource. This ensures 
                    that users in the group inherit the permissions granted by that role only within the context of the specified project.
                    For example, If a user has edit_project permission at the project mapping level, that user can only edit the specified project.


In Choreo, authorization operates by assigning a role to a group at a specified level. The level at which the role is assigned determines the extent of permissions granted to users.

!!! warning "Important"
    Avoid assigning multiple roles to a single user across different projects or levels (organization and project). Such assignments can grant users unintended permission to some projects, allowing them to perform tasks they shouldn't have access to. Therefore, it is recommended to assign only one role to a user across projects or levels to ensure proper access control.

!!! info
    In Choreo, organization-level permissions take precedence over project-level permissions.

To elaborate further, refer to the following diagram. 

The following diagram depicts a role-group assignment at a specific resource level. In the diagram, an admin user has assigned the Developer role to all members of the Engineering group within the Engineering Project. This grants users in the Engineering group the ability to perform all actions allowed by the Developer role within the Engineering Project.

![Console access control](../assets/img/administer/access-control-to-console.png)

## Sample scenario

Now that you understand the basic concepts of access control within the Choreo Console, let’s try out a sample scenario to manage access within a project. 

Assume you are overseeing the Engineering Project within your organization and you need to grant development access to specific users solely within this project. Here's a step-by-step guide on how to achieve this:

### Step 1: Create a project

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | `Engineering Project`              |
    | **Name**                 | `engineering-project`              |
    | **Project Description**  | `My sample project`                |

4. Click **Create**. This creates the project and takes you to the project home page.

### Step 2: Create a new group

Follow the steps given below to create a group with the name `Engineering Project Developer`:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. Click **+ Create Group**.
5. Enter a group name and group description. You can enter the values given below:

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Group Name**           | `Engineering Project Developer`    |
    | **Group Description**    | `Users with development access within the engineering project`|

6. Click **Create**.

### Step 3: Assign roles to the group

Follow the steps given below to assign the **Developer** role to the **Engineering Project Developer** group that you created:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the **Engineering Project** that you created.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. On the **Groups** tab, search for the **Engineering Project Developer** group and click the corresponding edit icon.
5. Click **+Add Roles**. 
6. In the **Add Roles to Group in Project** dialog that opens, click the **Roles** list and select **Developer**.
7. Click **Add**. This assigns the **Developer** role to the group. You should see the mapping level as **Project (Engineering Project)** as follows, indicating the scope of the mapping:

    ![Mapping level](../assets/img/administer/mapping-level.png)

   This means that you have granted developer access to users in the Engineering Project Developer group in the scope of the Engineering Project. 

Now that you have set up access control, you can proceed to add users to the new group.

### Step 4: Add users to the group

There are two approaches you can follow to add users to the group.

#### Add a new user as a project developer 

Follow the steps given below to add a new user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Click **+Invite Users**.
5. In the **Invite Users** dialog,
   1. Specify the email addresses of the users in the **Emails** field.
   2. Click the **Groups** list and select **Engineering Project Developer**.
6. Click **Invite**.

#### Add an existing user as a project developer 

Follow the steps given below to add an existing user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Search for the existing user you want to add to the **Engineering Project Developer** group.
5. Click the edit icon corresponding to the user.
6. Click **+Assign Groups**.
7. In the **Add Groups to User** dialog, click the **Groups** list and select **Engineering Project Developer**.
8. Click **Add**.

!!! tip
     Make sure to remove the user from any other groups to avoid granting organization-level access unintentionally.


!!! note
     - Existing groups are already mapped to similar roles at the organization level. Therefore, adding users to those groups or keeping users in them, will give organization-level access to the users.
     - When users are added to the **Engineering Project Developer** group, they will only have developer access to the **Engineering Project**.
     - You can invite new users or add existing users to new groups within the Engineering Project, and based on their requirements, assign roles like Developer, API Publisher, etc.

Now you have successfully set up access control within your project.


# Control Egress Traffic for Your Organization

In Choreo, you can manage egress traffic originating from your applications by setting up an allow list or deny list. By default, egress traffic is allowed to any destination unless specifically restricted.

## Configure an egress policy at the organization level

To configure an egress policy at the organization level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Egress Control** tab.
5. Click **+ Create** to add a new egress policy.
6. Select the type of egress control to apply and add the required rules:

    - **Allow All**: Allows all egress traffic by default. You can selectively block traffic to specific IP ranges.
    - **Deny All**: Blocks all egress traffic by default. You can selectively allow traffic to specific IP ranges or domains.

        !!! note

             - Once you select an egress control type and create a rule, you cannot change the type. To change the type, you must delete existing rules.
             - Egress rules you add can disrupt your application if they block traffic to required destinations. Ensure you add rules appropriately to prevent such disruptions.
             - If you use the **Deny All** type, be sure to add Choreo-managed database hosts to the allowed list.
             - Egress policies apply across all environments in an organization.
             - Egress policies do not apply to API proxies.

    ![Configure an organization-level egress policy](../assets/img/administer/configure-an-organization-level-egress-policy.png)

## Override the organization-level egress policy at the project level

An egress policy set at the project level can override the organization-level policy, depending on the egress control type you select.

To override the organization-level egress policy at the project level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Project** list and select your project.
3. In the left navigation menu, click **Settings**. This opens the project-level settings page.
4. Click the **Egress Control** tab. You will see that the organization-level egress policy is enforced by default.
5. Add required project-level rules to further restrict egress traffic.

    - If the **Allow All** egress control type is selected at the organization level, you can add project-level deny rules to further restrict traffic.
    - If the **Deny All** egress control type is selected at the organization level, you can remove allow rules inherited from the organization level to further restrict traffic.

    ![Add project-level rules](../assets/img/administer/add-project-level-rules.png)


# Create API Subscription Plans

API subscription plans are essential to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security. With the option to set rate limits and burst control, subscription plans allow API providers to manage traffic, prevent misuse, and offer tiered service levels. Organizations can implement subscription plans to provide varying levels of API access, accommodating different user needs and business models, while ensuring optimal performance and security. 

In Choreo, users with the administrator role can create, update, and delete subscription plans at the organization level. 

!!! tip
    Deleting a subscription plan is only possible if there are no active subscriptions associated with it.  

To create an organization-level subscription plan, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **API Management** tab and then click **Subscription Plans**.
5. Click **+ Add Subscription Plan**.
6. In the **Create Subscription Plan** pane, enter the appropriate values for each field:
    
    !!! note
         - In the **Name** field, you must specify a name to uniquely identify the subscription plan in various contexts. The value is editable only at the time you create the subscription plan. You cannot change the name after you create it.
         - The **Stop on Quota Reach** checkbox is selected by default when creating a subscription plan. When selected, requests return an HTTP 429 response if the request count exceeds the limit. If you clear the checkbox, requests are allowed even if the quota is exceeded.
         - Burst control protects your backend from sudden request spikes and manages API usage. It’s especially useful for subscription plans where the request count is enforced over a long period, to prevent consumers from using their entire quota too quickly. Ensure you select the **Burst Control** checkbox when the **Request Count Time Unit** is selected as **Hour** or **Day**.
         - Select the **Approval required** checkbox if subscription requests made to this plan require administrator or API publisher approval to activate the plan. This allows for manual review and approval of a subscription before granting API access.
  
    ![Create subscription plan](../assets/img/administer/create-subscription-plan.png)

7. Click **Create**. This creates the subscription plan and lists it under **Subscription Plans**.

After creating subscription plans, users with the API publisher role can [assign subscription plans to APIs](../api-management/manage-api-traffic/assign-subscription-plans-to-apis.md). API consumers can then choose the appropriate subscription plan during the subscription process depending on their requirements.


# Customize the Developer Portal

The Developer Portal allows API consumers to find and consume APIs with ease. You can change the look and feel of your Developer Portal by changing the theme to match your brand. Doing so will help you give a better developer experience to your users.

To customize the Developer Portal theme, follow the steps given below:

!!! Note
    - To customize the Developer Portal theme for an organization, you need to be an admin user of that organization.
    - You cannot undo a change and restore or revert to a previous version of the theme. However, you can reset it to the default theme.

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google/ GitHub/ Microsoft account.


2. In the left pane, click **Settings**.

4. In the header, click the **Organization** list. This will open the organization level settings page. 

5. In the **API Management** tab, click **Devportal Theme**.

    ![Access Devportal theme](../assets/img/administer/devportal-theme/access-devportal-theme.png){.cInlineImage-threeQuarter}

    Once you access the theme, you can customize the **Home** page, color theme, font, header and footer, logos, etc., by expanding the relevant sections.

6. Make a change to the theme. For example, let's change the title on the **Home** page and the color theme. 

    1. To update the title on the **Home** page, expand the **Home Page** section, and in the **Title** field, change the default text (for example, to `Try our APIs!`).
   
    2. To update the color theme, expand the **Color Palette** section, and change the colors as required (for example, change the background color to `#C3C5CD` and the primary color of the buttons to `#086634`).
   
    3. Click **Preview** to view a preview of the Developer Portal with the changes you made. Based on the changes given in the examples, the preview appears as follows.

         ![Preview of customization](../assets/img/administer/devportal-theme/preview-of-customization.png){.cInlineImage-threeQuarter}
   
    4. Click **Save** to save your changes as a draft theme.
    
    5. To apply the changes to the Developer Portal, toggle the **Go Live** switch. To confirm that you want to go live with the changes, click **Enable** in the message that appears.
    	
7. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).

The **Home** page will appear as it did in the preview.

## Reset the Developer Portal theme

To reset the Developer Portal theme to the default theme, follow the steps given below:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google, GitHub, or Microsoft account.

2. In the left pane, click **Settings**.

3. In the header, click the **Organization** list. This will open the organization level settings page. 

4. In the **Organization** tab, click **Devportal Theme**, and then click **Reset to Default**.



## Inviting users

An organization administrator can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Manage Members of an Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a user of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a user of that organization.

{% include "inviting-members.md" %}

## Manage user permission

For details on how Choreo manages user permission, see [Manage user permission](../choreo-concepts/organization.md#manage-user-permission).


# Review Workflow Approval Requests

In Choreo, administrators can [configure approvals for workflows](./configure-approvals-for-choreo-workflows.md) and assign specific users as approvers.

If you are assigned as an authorized reviewer for a particular workflow approval request, you will receive an email notification when a [request is submitted for approval](../develop-components/submit-and-manage-workflow-approval-requests.md). The email includes a summary of the request and a link to the **Approvals** page in the Choreo Console, where you can review the details and either approve or reject the request.

!!! note
     - Workflow approvals are managed at the project level. If a role with the necessary permissions is assigned in a project context, only members of the user group bound to that role within the specific project will receive notifications for requests made in that project. For example, if you are assigned the Project Admin role (which includes the necessary permissions) for project A, you will only be notified of workflow requests within project A.
     - Users with organization-level permissions will receive notifications for all workflow requests across any project in the organization.

Other approvers within your organization will also receive notifications for workflow requests and may review a request before you. If a request has already been reviewed, it will appear under the **Past** tab on the **Approvals** page.

Approval requests are submitted on behalf of the team. Once approved, any authorized team member can execute the task. For certain tasks, execution may occur automatically upon approval.

## View workflow approval requests

To view workflow approval requests assigned to you, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Approvals**. This opens the **Approvals** page where you can see all approval requests assigned to you. The **Pending** tab lists requests that are yet to be reviewed. The **Past** tab displays requests already reviewed by you or other approvers, as well as requests canceled by the requester.
4. To view details of a specific request, click **Review** corresponding to it.

## Approve or reject an approval request

To approve or reject a request, follow these steps:

1. Follow the instructions in the [View workflow approval requests](#view-workflow-approval-requests) section above to see details of the workflow you want to review.
   Alternatively, click the Choreo Console link in the approval request email notification you received. This takes you to the request details in the Choreo Console.
2. Review the request and click **Approve** or **Reject** based on your decision.



# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Choreo, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Choreo, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Add Asgardeo as an external IdP in Choreo

Follow the steps below to add Asgardeo as an external IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list.

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Choreo.


# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

In organizations leveraging Microsoft Azure Active Directory (Azure AD) for identity and access management (IAM), integrating it with Choreo offers powerful API access control. This control hinges on the use of API scopes. That is, it enables the restriction of access to a designated group of users. This document guide you step-by-step to configure Azure AD as your external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- An Azure Active Directory account:  If you don’t already have one,  setup an Azure Active Directory account at [https://azure.microsoft.com/en-gb/](https://azure.microsoft.com/en-gb/).
- Administrator rights to your Choreo organization: You need this to configure the Azure AD account in your organization.

## Add Azure Active Directory as an external IdP in Choreo

Follow the steps below to add Azure AD as an IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Microsoft Entra ID (Azure AD)** as the Identity Provider. 
6. Provide a name and a description for the IdP. 
7. To obtain the `Well-Known URL` of your Azure AD instance, on your Azure account, under **Azure Active Directory** go to **App registrations**, and then **Endpoints**. Copy the URI under`OpenID Connect metadata document`.
    
    !!! info
        - In azure, there are two versions of access tokens available. By default, the IDP applications you create use the v1 access token. Therefore, if you intend to use the v1 access token, when providing the `Well-Known URL`, omit the v2.0 path segment from the URL. [Learn more](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats)
        For example, convert `https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration`-> `https://login.microsoftonline.com/<tenant-id>/.well-known/openid-configuration`
        - If you intend to work with v2.0, then the IDP application's manifest should be changed as explained in the [access tokendocumentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats). 
        
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Review the endpoints and click **Next**.




# Configure a Custom Domain for Your Organization

A custom domain is essential for effective branding, discoverability, and credibility of a website. Choreo allows you to easily configure custom domains for your organization, enabling developers to utilize it to configure custom URLs for their components such as API proxies, services, web applications, and webhooks.

This section provides an overview of Choreo’s custom domain configuration model and guides you through configuring a custom domain for your organization. It also walks you through utilizing a custom domain to configure a custom URL for a component.

## Choreo custom domain configuration model

Choreo allows organization administrators to add custom domains for their organizations. When an administrator adds custom domains to an organization, component developers can submit requests to utilize the custom domains for their respective components. These requests require approval from the organization administrator. Upon approval, the custom domain and the relevant URL customization become available to the component.

## Configure a custom domain for an organization

### Prerequisites

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Create an organization in Choreo.
    
    ![Create an organization in Choreo](../assets/img/administer/create-choreo-organization.png)

### Add a custom domain

To add a custom domain for your organization, follow the steps given below:

!!! info "Note"
     To add a custom domain, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Active Domains** tab.
5. Click **+ Add Domains**. 
6. In the **Add a Custom Domain** pane, do the following:
    1. Enter your domain name.
    2. Select the environment to apply the domain name.
    3. Select the entity type to apply the domain name.

        !!! tip
             In this context:

              - The **API** entity type represents Choreo components exposed via an endpoint, including API Proxy, Service, and Webhook components.
              - The **Web App** entity type represents the Web Application component.
       
 7. Take a look at the generated CNAME target value displayed and create a DNS record associating the domain name to the CNAME target value with your DNS provider.
    
    ![CNAME target value](../assets/img/administer/configure-domain/cname-target-value.png)

    !!! info
          When you select **Developer Portal** as the type, the environment is not applicable, and the CNAME alias will be displayed as follows:
           ![Developer Portal CNAME target value](../assets/img/administer/configure-domain/developer-portal-cname-target-value.png)

 8. Once the CNAME type DNS record is created, click **Verify**.

    !!! info "Note"
          If the CNAME mapping is correct, the verification completes successfully. It can take some time for the configured CNAME mapping to be globally available.

 9. On successful verification of the custom domain, click **Next**.
 10. Select a TLS certificate provider depending on your preference. You can either import the TLS certificates you created for the custom domain or click **Let's Encrypt** to allow Choreo to generate and manage the certificates for you.

    !!! note "If you want to import your own certificate, it should adhere to specific guidelines"
          - TLS certificate guidelines:
             - It should be issued by a certificate authority (CA) and should contain the domain's public key along with additional information such as the domain name, the company that owns the domain, the certificate's expiration date, and the digital signature of the issuing CA.
             - It should be an X509 certificate.
             - It should be in the PEM format.
             - It should be issued directly or through a wildcard entry for the provided custom URL. For example,
                - For direct issuance, the SSL file must include the exact domain name. For example, if the domain is `apis.choreo.dev`, the SSL file must include `apis.choreo.com`.
                - For wildcard entries, the SSL file should use a wildcard notation to cover all subdomains under the provided URL. For example, if the CNAME is `apis.choreo.dev`, the SSL file should use `*.choreo.dev`.
          - TLS key file guidelines:
             - It should be in the PEM format.
             - It must be encrypted using RSA encryption.
          - Certificate chain file guidelines:
             - The chain file, which is essential for some clients to verify the authenticity of a server's SSL/TLS certificate, should contain your domain's SSL/TLS certificate (optional, as this can be provided via the certificate itself) and one or more intermediate certificates in the correct order, leading back to a root certificate. 
             - All certificates in the chain should be X509 certificates in PEM format.
               <details><summary>For step-by-step instructions on constructing a certificate chain with a root certificate, click here</summary>
               To construct a certificate chain with a root certificate, you must organize and combine the certificates in the correct sequence. A typical certificate chain consists of the following:
                 - **Root certificate**: The trusted self-signed certificate issued by the certificate authority (CA).
                 - **Intermediate certificates** (if any): Certificates issued by the root CA to subordinate CAs.
                 - **Leaf certificate**: Your end-entity certificate issued by the CA. This is an optional certificate that may be included within the chain or provided separately.<br><br>
                Follow these steps to construct the certificate chain:
                    1. Obtain and organize your certificates in the correct order:
                        - **Leaf certificate**: The public certificate issued by the CA. This is optional and may be included within the chain or provided separately.
                        - **Intermediate certificates**: Obtain these from the CA, if applicable.
                        - **Root certificate**: Obtain this from the CA.  If it is self-signed, it serves as the trust anchor.
                    2. Combine the certificates into a single file in the following order:
                        - Leaf certificate: This is your public certificate issued by the CA.
                        - Intermediate certificates if applicable: Include these in the correct hierarchical order.
                        - Root certificate: Include this at the end of the file.<br><br>
                        Use a text editor or a command-line tool to concatenate the certificates into one file, ensuring each certificate begins and ends with the proper markers. Also make sure the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers appear on a new line:
                    ```
                     -----BEGIN CERTIFICATE-----
                     <Leaf Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Intermediate Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Root Certificate Content>
                     -----END CERTIFICATE-----
                    ```
                    3. Save the concatenated file. You can save it with a name such as `certificate_chain.pem`.
                    4. Use the following command to verify that your certificate chain is constructed correctly:
                    ```
                    openssl verify -CAfile <root_or_bundle_cert>.pem certificate_chain.pem
                    ```
                    Replace `<root_or_bundle_cert>.pem` with the path to your root certificate or a bundle containing both the root and intermediate certificates.
                    5. Once the certificate chain is verified, upload it via the Choreo Console:
                        ![Upload certificate chain](../assets/img/administer/configure-domain/upload-certificate-chain.png)
                        - If the constructed chain includes the leaf certificate, follow these steps:
                            - Upload the constructed certificate chain in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Do not upload a certificate chain file, as it is already included in the TLS certificate.
                        - If the constructed chain does not include the leaf certificate, follow these steps:
                            - Upload the leaf certificate in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Upload the constructed certificate chain in the **Certificate Chain File** field.
 
     To proceed with this step in this guide, click **Let's Encrypt**.

 11. To save the custom domain, click **Add**.
 
Now, you have successfully added a custom domain for your organization.

You can see the added custom domain listed in the **Active Domains** tab under the URL **Settings** tab.
    
 ![Active domains](../assets/img/administer/configure-domain/active-domains.png)

The custom domain you added will be available to the entity types in the specified environment. You can request the custom domain when configuring a custom URL for a component.

!!! info "Note"
     If you add a custom domain for the **Developer Portal** type, the customization is applied immediately, and you can access the organization’s Developer Portal via the added domain.

If you want to view the entity types that use a particular custom domain, click the specific custom domain listed in the **Active Domains** tab under **URL Settings**.
 
## Configure a custom URL for a component

When an organization administrator adds custom domains for specific environments, developers can request any available custom domain to configure a custom URL for a component in a specific environment.

### Request a custom URL for a component

To request a custom URL for your component, follow the steps given below:

!!! info "Note"
     Before you request a custom domain for a specific environment, ensure that the component is deployed to that environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to customize the URL.
3. In the left navigation menu, click **Settings**. This opens the component-level settings page.
4. Click the **URL Settings** tab. This displays the active deployments of the component across different environments and indicates whether a custom URL is configured. If an active custom domain is available to configure a custom URL for a component in a specific environment, the **Edit URL Mapping** icon in the corresponding **Action** column becomes enabled.
    
    ![Active deployments](../assets/img/administer/configure-domain/active-deployments.png)

5. To configure a custom URL for a component in a specific environment, click the **Edit URL Mapping** icon under the **Action** column corresponding to the respective environment. This opens the **URL Settings** dialog, where you can specify values to request for a custom URL.
    
    ![URL settings](../assets/img/administer/configure-domain/url-settings.png)

6. In the **URL Settings** dialog, select a domain to configure a custom URL.

    !!! tip
          - The **Domain** drop-down lists the available domains for the component. You can  request for any listed domain.
          - If you want to request a custom URL for an API, you must specify an appropriate context path in the **Path** field. The **Path** field displays the default context path for the API. You can edit the path depending on your preference. 

7. Click **Configure**. This creates the custom URL mapping, which you can see under the **URL Settings** tab.  The custom URL request will be in the **Pending** status until an organization administrator approves the request.
    
    ![Pending custom URL request](../assets/img/administer/configure-domain/pending-custom-url-request.png)

### Approve a custom URL request

When a developer requests a custom URL, the request will be listed in the organization-level settings page under the **URL Settings** tab.

To approve a custom URL mapping, follow the steps given below:

!!! info "Note"
     To approve custom URL requests, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Pending URL Requests** tab. You will see all the pending URL mapping requests sent by developers.
    
    ![Pending URL requests](../assets/img/administer/configure-domain/pending-url-requests.png)


5. Go to the custom URL you want to approve and click the corresponding **Approve URL Mapping** icon under the **Action** column.
6. Review the details and click **Approve**.
   
   Once approved, the invoke URL of the component gets replaced with the configured custom URL.
    
   ![Custom URL](../assets/img/administer/configure-domain/custom-url.png)

   Now you have successfully utilized the configured custom domain to set up a custom URL for a component.


# Configure a User Store with the Built-In Identity Provider

Developers looking to experiment with a complete application development process that includes user authentication and authorization can utilize Choreo's built-in identity provider (IdP). Choreo's built-in identity provider allows you to seamlessly test your application's authentication by setting up test users and groups within Choreo. 

!!! note
     Although the built-in IdP facilitates user management support, it is limited to adding users with attributes and groups. Therefore, the built-in IdP user management capabilities are not recommended for use in production.

## Prerequisites

Before you try out the steps in this guide, be sure you have administrator rights to your Choreo organization. This permission is essential to configure a user store with the built-in IdP.

## Configure a Choreo built-in IdP user store

Follow the steps given below to configure a Choreo built-in IdP user store for an environment:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Organization** list and then click on your organization.
3. In the left navigation menu, click **Settings**. This takes you to your organization settings.
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. On the **Identity Providers** tab, click **Manage** in the **Choreo Built-in Identity Provider** pane.
6. In the Manage IdP pane, click on a specific environment tab depending on where you want to configure the built-in IdP user store.
7. You can download the sample **User store template file(.csv )** from the **User Store** section. The template file content is similar to the following:

   ```csv
   username,password,groups,first_name,last_name,email
   "demouser","password1","[manager, engineering]","John","Doe","john@acme.org"
   ```

!!! note
     The provided template file includes a sample user with associated attributes. To add new users, insert additional rows in the `.csv` file. To include more user attributes, add columns as required in the `.csv` file.
   
8. Specify appropriate user details in the template file and save it.
9. Select the template file that you saved and click **Upload**. A successful upload creates the user store and displays the configured users in the **Users** section.


# Configure Approvals for Choreo Workflows

Choreo allows you to configure approval processes for specific workflows within the platform. An approval process for a workflow ensures that critical or sensitive changes are properly managed and controlled.

Choreo currently allows you to configure approvals for environment promotion and API subscription workflows.

Configuring approvals for environment promotion allows authorized users to control components being promoted to a critical/production environment. 

Configuring approvals for the API subscription workflow allows you to create subscription plans that require approval before being activated. This feature allows you to control access to APIs by requiring administrative review and authorization of subscriptions before they become active.

## Permissions to review and respond to approval requests

Click the respective tab for details on permissions depending on the workflow for which you want to configure approvals:

=== "Environment promotion"

     To review and respond to environment promotion approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**: 
          - Approve component promotion requests: Grants access to review and approve the promotion of components to critical environments.
      - **PROJECT-MANAGEMENT**: Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

=== "API subscription"

     To review and respond to API subscription approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**:
          - Approve API subscriptions: Grants access to review and approve API subscription workflow requests.
      - **PROJECT-MANAGEMENT**: 
          Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

## Set up an approval process for a workflow

To set up an approval process for a workflow, follow these steps:

!!! note
     - You must have administrator privileges in Choreo to configure workflow approvals.
     - Administrators can designate specific roles and assignees to review and respond to requests associated with each workflow.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Workflows** tab.
5. Click the edit icon corresponding to the workflow for which you want to configure an approval.
6. In the **Configure Workflow** dialog that opens, select roles and assignees to review and respond to workflow approval requests.

    - In the **Roles** field, select one or more roles depending on your preference. Any user assigned to these roles can review and respond to requests.
    - In the **Assignees** field, select specific users who can review and approve workflow requests. Assignees can be any Choreo user, even if they are not assigned to a selected role.

    !!! info "Important"
         Currently, there is no validation to ensure that the specified roles and assignees have the necessary permissions to review and respond to requests. If the [required permissions](#permissions-to-review-and-respond-to-approval-requests) are not correctly configured, some users may receive email notifications but will be unable to review the requests.
         
7. Click **Save**. This configures and enables the approval process for the workflow.

Once you enable the approval process for a workflow, see the following details on how to submit a request for approval and the approval process. Click the respective tab depending on the workflow for which you enabled the approval process:  

=== "Environment promotion"

     Once you configure an approval process for environment promotion, developers must [submit a request for approval to use the workflow](../develop-components/submit-and-manage-workflow-approval-requests.md). An authorized assignee must then [review and approve the request](./review-workflow-approval-requests.md) for a developer to proceed with the task related to the workflow.

=== "API subscription"

     Once you configure an approval process for API subscription, administrators can select the **Approval required** checkbox to create or update subscription plans to require approval. For details, see [Create API Subscription Plans](../administer/create-api-subscription-plans.md). API consumers using these plans must request approval to proceed. For details, see step 7 in [Subscribe to an API with a Subscription Plan](../api-management/manage-api-traffic/subscribe-to-an-api-with-a-subscription-plan.md). An authorized approver must then [review and approve the request](./review-workflow-approval-requests.md) before the subscription is granted.


# Configure Enterprise Login

With Choreo, you can configure enterprise login to allow users from an external identity provider (IdP) to sign in to Choreo seamlessly without changing their credentials.

This guide walks you through the steps to configure enterprise login for your organization in Choreo. 


## Prerequisites 

Before you proceed with the configuration, set up the following:

- A valid email domain for your organization.
- Access the Choreo Console at https://console.choreo.dev/ via your Google, GitHub, or Microsoft account. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries". 

## Configure enterprise login for your Choreo organization

To configure enterprise login for your Choreo organization, follow the steps given below:

 - **If you already have a support account with us**, send us your organization name/handle and the email domains specific to your organization through our support portal. 

 - **If you do not have a support account with us yet**, send an email to `choreo-help@wso2.com` requesting to enable enterprise login for your organization. 
      
    !!! tip
        Ensure you include the following information in the request:

         - Organization name or handle. For example, “Stark Industries” or “starkindustries”.
         - Email domains specific to your organization. For example, “@stark.com”, “@starkindustries.com”, and “@stark.eu.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise login
        
        Hi CS team,

        I need to configure enterprise login for my organization. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries
          - Email domains specific to my organization: “@stark.com”, “@starkindustries.com”, and “@stark.eu”

        Thank you.

    The Choreo support team will perform the necessary configurations and respond to you with a verification code. You must sign in to your domain host account and configure the DNS record for your email domain with the following values:

    | **Field**                          | **Value**                                      |
    |------------------------------------|------------------------------------------------|
    | **Name/Host/Alias**                | Specify `@` or leave it blank                  |
    | **Time to Live (TTL)**             | Keep the default value or use `86400`          |
    | **Value/Answer/Destination**       | wso2-domain-verification:<`verification_code`> |


Now, you are ready to bring your own identity to Choreo.

## Bring your own identity to Choreo

When you create an organization in Choreo, an organization with the same name is provisioned for you in Asgardeo. To bring your own identity to Choreo, you must configure a federated enterprise IdP on Asgardeo in the organization that is provisioned for you.

Follow the steps given below to configure the federated IdP:

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. To configure a federated enterprise identity provider for your Asgardeo organization, follow the steps in [Asgardeo documentation - Add Standard-Based Login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/).
3. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
4. Click on the application to edit it.
5. Click the **Sign-in Method** tab. You can observe the configured connection.

Now, users in your enterprise IdP can sign in to the Choreo Console using their enterprise IDs.

## Configure role-based access control for enterprise login

To streamline the enterprise login process and grant appropriate permission, Choreo provides the flexibility to configure role-based access control for users who reside in an external IdP. 

To set up role-based access control for enterprise login within Choreo, follow the steps given below:

### Prerequisites

Before you proceed with the configuration, make sure you complete the following:

1. Configure enterprise login for your organization. For instructions, see [Configure enterprise login for your Choreo organization](#configure-enterprise-login-for-your-choreo-organization). 
2. Ensure your enterprise identity provider includes the group/role attributes in tokens it sends to Asgardeo via the respective protocol.
3. Be sure you have administrator privileges in Choreo.

### Step 1: Configure Asgardeo

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. [Configure your IdP as an external IdP in Asgardeo](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/). Depending on your IdP, you can select OpenID Connect or SAML as the protocol between Asgardeo and your IdP.

    !!! note
        If you are using OpenID Connect, configure the requested scopes accordingly for Asgardeo to get the relevant group/role details from the external IdP.

3. To configure the application, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
    2. Click on the application to edit it.
    3. Click the **Sign-in Method** tab.
    4. Configure the IdP for login depending on the protocol you selected:
        - For OpenID Connect, follow the instructions in [Enable the OIDC IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-oidc-idp-login/#enable-the-oidc-idp-for-login).
        - For SAML, follow the instructions in [Enable the SAML IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-saml-idp-login/#enable-the-saml-idp-for-login).
            
    5. Click the **User Attributes** tab.
    6. Select the **Groups** attribute and click the arrow to expand the section. Then, select the **Requested** checkbox.
    7. Click **Update**.

4. To add the user attributes as OpenID Connect scopes, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **New Attribute** and select the **Groups** attribute.
    4. Click **Save** and then click **Save Changes**.

### Step 2: Map Choreo groups to enterprise IdP groups via the Choreo Console 

!!! note
    
    Before you map Choreo groups to enterprise IdP groups, ensure you meet the following criteria:

    - Asgardeo is your key manager.
    - You have permission to perform actions of the organization administrator role.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. This takes you to the organization's home page.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. In the **Access Control** tab, click **Groups**. 
5. Click **Manage IdP Group Mapping**.
    ![Group mapping](../assets/img/administer/enterprise-login/group-mapping.png)

6. Click the edit icon corresponding to the Choreo group you want to map to the enterprise IdP group.
7. In the **IdP Group Name** field, specify the exact name you configured in the enterprise IdP and enter to add it.
   
    !!! tip
        If there is a change to the IdP group mapping, it takes effect from the next login session onwards. 

8. Click **Save**. 

By following these steps, you have successfully configured role-based access control for enterprise login in Choreo, allowing users from the external IdP to have the appropriate permission.


# Configure Self-Sign-Up

With Choreo, you can set up a self-sign-up page for your Developer Portal. The self-sign-up page allows users to easily access your Developer Portal and subscribe to APIs. When you configure self-sign-up, users can create their accounts and access your Developer Portal without any manual intervention from you.

This page walks you through the steps to configure self-sign-up for your Developer Portal.

## Prerequisites

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using your Google, GitHub, or Microsoft account.
2. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries".


## Configure Developer Portal self-sign-up

To configure self-sign-up, follow the steps given below:

1. Send an email to <choreo-help@wso2.com> requesting to configure enterprise IdP for the Developer Portal of your organization. 

    !!! tip
        Ensure you include the organization name or handle in the request.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise IdP for Developer Portal
        
        Hi CS team,

        I need to configure enterprise IdP for my organization’s Developer Portal to enable self-sign-up. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries

        Thank you

    The Choreo support team will perform the necessary configurations and respond to your request.

2. When you receive a response, sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials that you used to sign in to Choreo.
3. In the Asgardeo Console, click **View all applications**.

    ![View all applications](../assets/img/administer/self-sign-up/view-all-applications.png)

    You will see an application named **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL**. 

    ![Applications](../assets/img/administer/self-sign-up/application.png)

4. Click on the application to edit it and enter your organization’s Developer Portal URL as the **Access URL** of the application. For example, `https://devportal.choreo.dev/starkindustries`.
5. Click **Update**.
6. To add user attributes, follow these steps:

    !!! info "Note"
          If you have enabled enterprise login and you want to add the **Groups** attribute during self-sign-up configuration, avoid making it mandatory. This ensures proper access control and prevents unauthorized privileges. If you make the **Groups** attribute mandatory, it allows self-signed-up users to specify a group and assume roles associated with it.

    1. Click the **User Attributes** tab.
    2. To add the email as a mandatory user attribute, select **Email** and click the arrow to expand the section. Then, select the **Requested** and **Mandatory** checkboxes.

        ![Email attribute](../assets/img/administer/self-sign-up/email-attribute.png)

    3. To add the first name and last name as optional attributes, select **Profile** and click the arrow to expand the section. Then, select the **Requested** checkbox for the **First Name** and the **Last Name** attributes.

        ![Profile attribute](../assets/img/administer/self-sign-up/profile-attribute.png)

    4. Click **Update**.

7. To add the user attributes as OpenID Connect scopes, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **+ New Attribute**.
    4. Select **Email**, **First Name**, and **Last Name** as the attributes to associate with the OpenID scope.
    5. Click **Save** and then click **Save Changes**.

        ![Save attributes as scopes](../assets/img/administer/self-sign-up/save-attributes-as-scopes.png)

8. To configure basic authentication as the sign-in method, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Applications**.
    2. In the **Applications** pane, click the **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL** application to edit it.
    3. Click the **Sign-in Method** tab and then click **Start with default configuration**.

        ![Add sign-in method](../assets/img/administer/self-sign-up/add-sign-in-method.png)

    4. Click **Update**.

9.  To configure self-registration, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Self Registration**.
    2. In the **Self Registration** pane, click **Configure**.
    3. To enable self-registration, turn on the toggle.
    4. Select **Account verification**. This displays a confirmation message to enable account verification. 
    5. Click **Continue**.
    6. Specify an appropriate value in the **Account verification link expiry time** field.
    7. Click **Update**. 
     
        ![Configure self-registration](../assets/img/administer/self-sign-up/configure-self-registration.png)

Once you complete these steps, you will see a sign up link similar to the following in your Developer Portal:

![Sign-up](../assets/img/administer/self-sign-up/sign-up.png){.cInlineImage-half}
 
Users can click **LOGIN/SIGN UP** and then click **Create an account** to sign up to access your Developer Portal.

![Create an account](../assets/img/administer/self-sign-up/create-an-account.png)

## Manage new users

To manage users who want to access your Developer Portal via self-sign-up, you have two possible approaches:

- Enable auto-approval for new user registrations: This approach automates the user approval process.  When you enable auto-approval, each user who creates an account and signs up to your Developer Portal can access it by default.
- Manually approve or reject user accounts: This allows you to review the list of user registrations and manually approve or reject each registration as needed.

### Enable auto-approval for new user registrations

To automatically approve each new user account registered on your Developer Portal, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**.
4. To enable auto-approval, turn on the toggle.

Once you enable auto-approval, users can sign in to your Developer Portal and view your APIs and applications immediately after creating an account.

### Manually approve or reject user accounts

If you have not enabled auto-approval, you can manually approve or reject new user registrations. Once a user creates an account, Choreo sends an email to ask the user to confirm the account. To manually approve or reject user accounts, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**. You will see the user accounts listed for approval.
4. To approve a user account, click **Approve**. To reject an account, click **Reject**.

    - If you approve an account, the user will receive an email confirming the approval.
    - If you reject an account, the user will receive an email mentioning that their account is rejected. 

        !!! info "Note"
               A rejected user cannot sign up to your Developer Portal using the same account again.


# Control Access in the Choreo Console

In the Choreo Console, you have the ability to manage access to projects and the actions that can be performed within them. Administrators have the capability to restrict project access to specific user groups. This feature is useful when you need certain user groups to have access to particular projects or for a set of projects.

Choreo uses **Roles**, **Groups**, and a **Mapping level** to control access to the Choreo Console as follows: 

- **Role** : Role is a collection of permissions. Choreo has a predefined set of roles with permissions assigned to them. [Learn more](../choreo-concepts/organization.md#roles)
- **Group** : Group is a collection of users. A user group requires a role or multiple roles to be assigned to it so that the users in those groups get the relevant permissions via the assigned roles. [Learn more](../choreo-concepts/organization.md#groups)

- **Mapping level** : A mapping level defines the extent at which a role-group mapping can be done. Choreo has two defined resource levels.
    - **Organization** : You can assign a role to a group or associate a group with a role within the organization. This ensures that    
                         all users in a group inherit the permissions granted by that role across all organizational resources.
                         For example, if a user has edit_project permission at the organization mapping level, that user can edit all the projects in the organization.
    - **Project** : You can assign a role to a group or associate a group with a role within a specific project resource. This ensures 
                    that users in the group inherit the permissions granted by that role only within the context of the specified project.
                    For example, If a user has edit_project permission at the project mapping level, that user can only edit the specified project.


In Choreo, authorization operates by assigning a role to a group at a specified level. The level at which the role is assigned determines the extent of permissions granted to users.

!!! warning "Important"
    Avoid assigning multiple roles to a single user across different projects or levels (organization and project). Such assignments can grant users unintended permission to some projects, allowing them to perform tasks they shouldn't have access to. Therefore, it is recommended to assign only one role to a user across projects or levels to ensure proper access control.

!!! info
    In Choreo, organization-level permissions take precedence over project-level permissions.

To elaborate further, refer to the following diagram. 

The following diagram depicts a role-group assignment at a specific resource level. In the diagram, an admin user has assigned the Developer role to all members of the Engineering group within the Engineering Project. This grants users in the Engineering group the ability to perform all actions allowed by the Developer role within the Engineering Project.

![Console access control](../assets/img/administer/access-control-to-console.png)

## Sample scenario

Now that you understand the basic concepts of access control within the Choreo Console, let’s try out a sample scenario to manage access within a project. 

Assume you are overseeing the Engineering Project within your organization and you need to grant development access to specific users solely within this project. Here's a step-by-step guide on how to achieve this:

### Step 1: Create a project

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | `Engineering Project`              |
    | **Name**                 | `engineering-project`              |
    | **Project Description**  | `My sample project`                |

4. Click **Create**. This creates the project and takes you to the project home page.

### Step 2: Create a new group

Follow the steps given below to create a group with the name `Engineering Project Developer`:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. Click **+ Create Group**.
5. Enter a group name and group description. You can enter the values given below:

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Group Name**           | `Engineering Project Developer`    |
    | **Group Description**    | `Users with development access within the engineering project`|

6. Click **Create**.

### Step 3: Assign roles to the group

Follow the steps given below to assign the **Developer** role to the **Engineering Project Developer** group that you created:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the **Engineering Project** that you created.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. On the **Groups** tab, search for the **Engineering Project Developer** group and click the corresponding edit icon.
5. Click **+Add Roles**. 
6. In the **Add Roles to Group in Project** dialog that opens, click the **Roles** list and select **Developer**.
7. Click **Add**. This assigns the **Developer** role to the group. You should see the mapping level as **Project (Engineering Project)** as follows, indicating the scope of the mapping:

    ![Mapping level](../assets/img/administer/mapping-level.png)

   This means that you have granted developer access to users in the Engineering Project Developer group in the scope of the Engineering Project. 

Now that you have set up access control, you can proceed to add users to the new group.

### Step 4: Add users to the group

There are two approaches you can follow to add users to the group.

#### Add a new user as a project developer 

Follow the steps given below to add a new user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Click **+Invite Users**.
5. In the **Invite Users** dialog,
   1. Specify the email addresses of the users in the **Emails** field.
   2. Click the **Groups** list and select **Engineering Project Developer**.
6. Click **Invite**.

#### Add an existing user as a project developer 

Follow the steps given below to add an existing user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Search for the existing user you want to add to the **Engineering Project Developer** group.
5. Click the edit icon corresponding to the user.
6. Click **+Assign Groups**.
7. In the **Add Groups to User** dialog, click the **Groups** list and select **Engineering Project Developer**.
8. Click **Add**.

!!! tip
     Make sure to remove the user from any other groups to avoid granting organization-level access unintentionally.


!!! note
     - Existing groups are already mapped to similar roles at the organization level. Therefore, adding users to those groups or keeping users in them, will give organization-level access to the users.
     - When users are added to the **Engineering Project Developer** group, they will only have developer access to the **Engineering Project**.
     - You can invite new users or add existing users to new groups within the Engineering Project, and based on their requirements, assign roles like Developer, API Publisher, etc.

Now you have successfully set up access control within your project.


# Control Egress Traffic for Your Organization

In Choreo, you can manage egress traffic originating from your applications by setting up an allow list or deny list. By default, egress traffic is allowed to any destination unless specifically restricted.

## Configure an egress policy at the organization level

To configure an egress policy at the organization level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Egress Control** tab.
5. Click **+ Create** to add a new egress policy.
6. Select the type of egress control to apply and add the required rules:

    - **Allow All**: Allows all egress traffic by default. You can selectively block traffic to specific IP ranges.
    - **Deny All**: Blocks all egress traffic by default. You can selectively allow traffic to specific IP ranges or domains.

        !!! note

             - Once you select an egress control type and create a rule, you cannot change the type. To change the type, you must delete existing rules.
             - Egress rules you add can disrupt your application if they block traffic to required destinations. Ensure you add rules appropriately to prevent such disruptions.
             - If you use the **Deny All** type, be sure to add Choreo-managed database hosts to the allowed list.
             - Egress policies apply across all environments in an organization.
             - Egress policies do not apply to API proxies.

    ![Configure an organization-level egress policy](../assets/img/administer/configure-an-organization-level-egress-policy.png)

## Override the organization-level egress policy at the project level

An egress policy set at the project level can override the organization-level policy, depending on the egress control type you select.

To override the organization-level egress policy at the project level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Project** list and select your project.
3. In the left navigation menu, click **Settings**. This opens the project-level settings page.
4. Click the **Egress Control** tab. You will see that the organization-level egress policy is enforced by default.
5. Add required project-level rules to further restrict egress traffic.

    - If the **Allow All** egress control type is selected at the organization level, you can add project-level deny rules to further restrict traffic.
    - If the **Deny All** egress control type is selected at the organization level, you can remove allow rules inherited from the organization level to further restrict traffic.

    ![Add project-level rules](../assets/img/administer/add-project-level-rules.png)


# Create API Subscription Plans

API subscription plans are essential to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security. With the option to set rate limits and burst control, subscription plans allow API providers to manage traffic, prevent misuse, and offer tiered service levels. Organizations can implement subscription plans to provide varying levels of API access, accommodating different user needs and business models, while ensuring optimal performance and security. 

In Choreo, users with the administrator role can create, update, and delete subscription plans at the organization level. 

!!! tip
    Deleting a subscription plan is only possible if there are no active subscriptions associated with it.  

To create an organization-level subscription plan, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **API Management** tab and then click **Subscription Plans**.
5. Click **+ Add Subscription Plan**.
6. In the **Create Subscription Plan** pane, enter the appropriate values for each field:
    
    !!! note
         - In the **Name** field, you must specify a name to uniquely identify the subscription plan in various contexts. The value is editable only at the time you create the subscription plan. You cannot change the name after you create it.
         - The **Stop on Quota Reach** checkbox is selected by default when creating a subscription plan. When selected, requests return an HTTP 429 response if the request count exceeds the limit. If you clear the checkbox, requests are allowed even if the quota is exceeded.
         - Burst control protects your backend from sudden request spikes and manages API usage. It’s especially useful for subscription plans where the request count is enforced over a long period, to prevent consumers from using their entire quota too quickly. Ensure you select the **Burst Control** checkbox when the **Request Count Time Unit** is selected as **Hour** or **Day**.
         - Select the **Approval required** checkbox if subscription requests made to this plan require administrator or API publisher approval to activate the plan. This allows for manual review and approval of a subscription before granting API access.
  
    ![Create subscription plan](../assets/img/administer/create-subscription-plan.png)

7. Click **Create**. This creates the subscription plan and lists it under **Subscription Plans**.

After creating subscription plans, users with the API publisher role can [assign subscription plans to APIs](../api-management/manage-api-traffic/assign-subscription-plans-to-apis.md). API consumers can then choose the appropriate subscription plan during the subscription process depending on their requirements.


# Customize the Developer Portal

The Developer Portal allows API consumers to find and consume APIs with ease. You can change the look and feel of your Developer Portal by changing the theme to match your brand. Doing so will help you give a better developer experience to your users.

To customize the Developer Portal theme, follow the steps given below:

!!! Note
    - To customize the Developer Portal theme for an organization, you need to be an admin user of that organization.
    - You cannot undo a change and restore or revert to a previous version of the theme. However, you can reset it to the default theme.

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google/ GitHub/ Microsoft account.


2. In the left pane, click **Settings**.

4. In the header, click the **Organization** list. This will open the organization level settings page. 

5. In the **API Management** tab, click **Devportal Theme**.

    ![Access Devportal theme](../assets/img/administer/devportal-theme/access-devportal-theme.png){.cInlineImage-threeQuarter}

    Once you access the theme, you can customize the **Home** page, color theme, font, header and footer, logos, etc., by expanding the relevant sections.

6. Make a change to the theme. For example, let's change the title on the **Home** page and the color theme. 

    1. To update the title on the **Home** page, expand the **Home Page** section, and in the **Title** field, change the default text (for example, to `Try our APIs!`).
   
    2. To update the color theme, expand the **Color Palette** section, and change the colors as required (for example, change the background color to `#C3C5CD` and the primary color of the buttons to `#086634`).
   
    3. Click **Preview** to view a preview of the Developer Portal with the changes you made. Based on the changes given in the examples, the preview appears as follows.

         ![Preview of customization](../assets/img/administer/devportal-theme/preview-of-customization.png){.cInlineImage-threeQuarter}
   
    4. Click **Save** to save your changes as a draft theme.
    
    5. To apply the changes to the Developer Portal, toggle the **Go Live** switch. To confirm that you want to go live with the changes, click **Enable** in the message that appears.
    	
7. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).

The **Home** page will appear as it did in the preview.

## Reset the Developer Portal theme

To reset the Developer Portal theme to the default theme, follow the steps given below:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google, GitHub, or Microsoft account.

2. In the left pane, click **Settings**.

3. In the header, click the **Organization** list. This will open the organization level settings page. 

4. In the **Organization** tab, click **Devportal Theme**, and then click **Reset to Default**.



## Inviting users

An organization administrator can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Manage Members of an Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a user of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a user of that organization.

{% include "inviting-members.md" %}

## Manage user permission

For details on how Choreo manages user permission, see [Manage user permission](../choreo-concepts/organization.md#manage-user-permission).


# Review Workflow Approval Requests

In Choreo, administrators can [configure approvals for workflows](./configure-approvals-for-choreo-workflows.md) and assign specific users as approvers.

If you are assigned as an authorized reviewer for a particular workflow approval request, you will receive an email notification when a [request is submitted for approval](../develop-components/submit-and-manage-workflow-approval-requests.md). The email includes a summary of the request and a link to the **Approvals** page in the Choreo Console, where you can review the details and either approve or reject the request.

!!! note
     - Workflow approvals are managed at the project level. If a role with the necessary permissions is assigned in a project context, only members of the user group bound to that role within the specific project will receive notifications for requests made in that project. For example, if you are assigned the Project Admin role (which includes the necessary permissions) for project A, you will only be notified of workflow requests within project A.
     - Users with organization-level permissions will receive notifications for all workflow requests across any project in the organization.

Other approvers within your organization will also receive notifications for workflow requests and may review a request before you. If a request has already been reviewed, it will appear under the **Past** tab on the **Approvals** page.

Approval requests are submitted on behalf of the team. Once approved, any authorized team member can execute the task. For certain tasks, execution may occur automatically upon approval.

## View workflow approval requests

To view workflow approval requests assigned to you, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Approvals**. This opens the **Approvals** page where you can see all approval requests assigned to you. The **Pending** tab lists requests that are yet to be reviewed. The **Past** tab displays requests already reviewed by you or other approvers, as well as requests canceled by the requester.
4. To view details of a specific request, click **Review** corresponding to it.

## Approve or reject an approval request

To approve or reject a request, follow these steps:

1. Follow the instructions in the [View workflow approval requests](#view-workflow-approval-requests) section above to see details of the workflow you want to review.
   Alternatively, click the Choreo Console link in the approval request email notification you received. This takes you to the request details in the Choreo Console.
2. Review the request and click **Approve** or **Reject** based on your decision.



# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Choreo, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Choreo, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Add Asgardeo as an external IdP in Choreo

Follow the steps below to add Asgardeo as an external IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list.

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Choreo.


# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

In organizations leveraging Microsoft Azure Active Directory (Azure AD) for identity and access management (IAM), integrating it with Choreo offers powerful API access control. This control hinges on the use of API scopes. That is, it enables the restriction of access to a designated group of users. This document guide you step-by-step to configure Azure AD as your external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- An Azure Active Directory account:  If you don’t already have one,  setup an Azure Active Directory account at [https://azure.microsoft.com/en-gb/](https://azure.microsoft.com/en-gb/).
- Administrator rights to your Choreo organization: You need this to configure the Azure AD account in your organization.

## Add Azure Active Directory as an external IdP in Choreo

Follow the steps below to add Azure AD as an IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Microsoft Entra ID (Azure AD)** as the Identity Provider. 
6. Provide a name and a description for the IdP. 
7. To obtain the `Well-Known URL` of your Azure AD instance, on your Azure account, under **Azure Active Directory** go to **App registrations**, and then **Endpoints**. Copy the URI under`OpenID Connect metadata document`.
    
    !!! info
        - In azure, there are two versions of access tokens available. By default, the IDP applications you create use the v1 access token. Therefore, if you intend to use the v1 access token, when providing the `Well-Known URL`, omit the v2.0 path segment from the URL. [Learn more](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats)
        For example, convert `https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration`-> `https://login.microsoftonline.com/<tenant-id>/.well-known/openid-configuration`
        - If you intend to work with v2.0, then the IDP application's manifest should be changed as explained in the [access tokendocumentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats). 
        
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Review the endpoints and click **Next**.




# Configure a Custom Domain for Your Organization

A custom domain is essential for effective branding, discoverability, and credibility of a website. Choreo allows you to easily configure custom domains for your organization, enabling developers to utilize it to configure custom URLs for their components such as API proxies, services, web applications, and webhooks.

This section provides an overview of Choreo’s custom domain configuration model and guides you through configuring a custom domain for your organization. It also walks you through utilizing a custom domain to configure a custom URL for a component.

## Choreo custom domain configuration model

Choreo allows organization administrators to add custom domains for their organizations. When an administrator adds custom domains to an organization, component developers can submit requests to utilize the custom domains for their respective components. These requests require approval from the organization administrator. Upon approval, the custom domain and the relevant URL customization become available to the component.

## Configure a custom domain for an organization

### Prerequisites

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Create an organization in Choreo.
    
    ![Create an organization in Choreo](../assets/img/administer/create-choreo-organization.png)

### Add a custom domain

To add a custom domain for your organization, follow the steps given below:

!!! info "Note"
     To add a custom domain, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Active Domains** tab.
5. Click **+ Add Domains**. 
6. In the **Add a Custom Domain** pane, do the following:
    1. Enter your domain name.
    2. Select the environment to apply the domain name.
    3. Select the entity type to apply the domain name.

        !!! tip
             In this context:

              - The **API** entity type represents Choreo components exposed via an endpoint, including API Proxy, Service, and Webhook components.
              - The **Web App** entity type represents the Web Application component.
       
 7. Take a look at the generated CNAME target value displayed and create a DNS record associating the domain name to the CNAME target value with your DNS provider.
    
    ![CNAME target value](../assets/img/administer/configure-domain/cname-target-value.png)

    !!! info
          When you select **Developer Portal** as the type, the environment is not applicable, and the CNAME alias will be displayed as follows:
           ![Developer Portal CNAME target value](../assets/img/administer/configure-domain/developer-portal-cname-target-value.png)

 8. Once the CNAME type DNS record is created, click **Verify**.

    !!! info "Note"
          If the CNAME mapping is correct, the verification completes successfully. It can take some time for the configured CNAME mapping to be globally available.

 9. On successful verification of the custom domain, click **Next**.
 10. Select a TLS certificate provider depending on your preference. You can either import the TLS certificates you created for the custom domain or click **Let's Encrypt** to allow Choreo to generate and manage the certificates for you.

    !!! note "If you want to import your own certificate, it should adhere to specific guidelines"
          - TLS certificate guidelines:
             - It should be issued by a certificate authority (CA) and should contain the domain's public key along with additional information such as the domain name, the company that owns the domain, the certificate's expiration date, and the digital signature of the issuing CA.
             - It should be an X509 certificate.
             - It should be in the PEM format.
             - It should be issued directly or through a wildcard entry for the provided custom URL. For example,
                - For direct issuance, the SSL file must include the exact domain name. For example, if the domain is `apis.choreo.dev`, the SSL file must include `apis.choreo.com`.
                - For wildcard entries, the SSL file should use a wildcard notation to cover all subdomains under the provided URL. For example, if the CNAME is `apis.choreo.dev`, the SSL file should use `*.choreo.dev`.
          - TLS key file guidelines:
             - It should be in the PEM format.
             - It must be encrypted using RSA encryption.
          - Certificate chain file guidelines:
             - The chain file, which is essential for some clients to verify the authenticity of a server's SSL/TLS certificate, should contain your domain's SSL/TLS certificate (optional, as this can be provided via the certificate itself) and one or more intermediate certificates in the correct order, leading back to a root certificate. 
             - All certificates in the chain should be X509 certificates in PEM format.
               <details><summary>For step-by-step instructions on constructing a certificate chain with a root certificate, click here</summary>
               To construct a certificate chain with a root certificate, you must organize and combine the certificates in the correct sequence. A typical certificate chain consists of the following:
                 - **Root certificate**: The trusted self-signed certificate issued by the certificate authority (CA).
                 - **Intermediate certificates** (if any): Certificates issued by the root CA to subordinate CAs.
                 - **Leaf certificate**: Your end-entity certificate issued by the CA. This is an optional certificate that may be included within the chain or provided separately.<br><br>
                Follow these steps to construct the certificate chain:
                    1. Obtain and organize your certificates in the correct order:
                        - **Leaf certificate**: The public certificate issued by the CA. This is optional and may be included within the chain or provided separately.
                        - **Intermediate certificates**: Obtain these from the CA, if applicable.
                        - **Root certificate**: Obtain this from the CA.  If it is self-signed, it serves as the trust anchor.
                    2. Combine the certificates into a single file in the following order:
                        - Leaf certificate: This is your public certificate issued by the CA.
                        - Intermediate certificates if applicable: Include these in the correct hierarchical order.
                        - Root certificate: Include this at the end of the file.<br><br>
                        Use a text editor or a command-line tool to concatenate the certificates into one file, ensuring each certificate begins and ends with the proper markers. Also make sure the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers appear on a new line:
                    ```
                     -----BEGIN CERTIFICATE-----
                     <Leaf Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Intermediate Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Root Certificate Content>
                     -----END CERTIFICATE-----
                    ```
                    3. Save the concatenated file. You can save it with a name such as `certificate_chain.pem`.
                    4. Use the following command to verify that your certificate chain is constructed correctly:
                    ```
                    openssl verify -CAfile <root_or_bundle_cert>.pem certificate_chain.pem
                    ```
                    Replace `<root_or_bundle_cert>.pem` with the path to your root certificate or a bundle containing both the root and intermediate certificates.
                    5. Once the certificate chain is verified, upload it via the Choreo Console:
                        ![Upload certificate chain](../assets/img/administer/configure-domain/upload-certificate-chain.png)
                        - If the constructed chain includes the leaf certificate, follow these steps:
                            - Upload the constructed certificate chain in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Do not upload a certificate chain file, as it is already included in the TLS certificate.
                        - If the constructed chain does not include the leaf certificate, follow these steps:
                            - Upload the leaf certificate in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Upload the constructed certificate chain in the **Certificate Chain File** field.
 
     To proceed with this step in this guide, click **Let's Encrypt**.

 11. To save the custom domain, click **Add**.
 
Now, you have successfully added a custom domain for your organization.

You can see the added custom domain listed in the **Active Domains** tab under the URL **Settings** tab.
    
 ![Active domains](../assets/img/administer/configure-domain/active-domains.png)

The custom domain you added will be available to the entity types in the specified environment. You can request the custom domain when configuring a custom URL for a component.

!!! info "Note"
     If you add a custom domain for the **Developer Portal** type, the customization is applied immediately, and you can access the organization’s Developer Portal via the added domain.

If you want to view the entity types that use a particular custom domain, click the specific custom domain listed in the **Active Domains** tab under **URL Settings**.
 
## Configure a custom URL for a component

When an organization administrator adds custom domains for specific environments, developers can request any available custom domain to configure a custom URL for a component in a specific environment.

### Request a custom URL for a component

To request a custom URL for your component, follow the steps given below:

!!! info "Note"
     Before you request a custom domain for a specific environment, ensure that the component is deployed to that environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to customize the URL.
3. In the left navigation menu, click **Settings**. This opens the component-level settings page.
4. Click the **URL Settings** tab. This displays the active deployments of the component across different environments and indicates whether a custom URL is configured. If an active custom domain is available to configure a custom URL for a component in a specific environment, the **Edit URL Mapping** icon in the corresponding **Action** column becomes enabled.
    
    ![Active deployments](../assets/img/administer/configure-domain/active-deployments.png)

5. To configure a custom URL for a component in a specific environment, click the **Edit URL Mapping** icon under the **Action** column corresponding to the respective environment. This opens the **URL Settings** dialog, where you can specify values to request for a custom URL.
    
    ![URL settings](../assets/img/administer/configure-domain/url-settings.png)

6. In the **URL Settings** dialog, select a domain to configure a custom URL.

    !!! tip
          - The **Domain** drop-down lists the available domains for the component. You can  request for any listed domain.
          - If you want to request a custom URL for an API, you must specify an appropriate context path in the **Path** field. The **Path** field displays the default context path for the API. You can edit the path depending on your preference. 

7. Click **Configure**. This creates the custom URL mapping, which you can see under the **URL Settings** tab.  The custom URL request will be in the **Pending** status until an organization administrator approves the request.
    
    ![Pending custom URL request](../assets/img/administer/configure-domain/pending-custom-url-request.png)

### Approve a custom URL request

When a developer requests a custom URL, the request will be listed in the organization-level settings page under the **URL Settings** tab.

To approve a custom URL mapping, follow the steps given below:

!!! info "Note"
     To approve custom URL requests, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Pending URL Requests** tab. You will see all the pending URL mapping requests sent by developers.
    
    ![Pending URL requests](../assets/img/administer/configure-domain/pending-url-requests.png)


5. Go to the custom URL you want to approve and click the corresponding **Approve URL Mapping** icon under the **Action** column.
6. Review the details and click **Approve**.
   
   Once approved, the invoke URL of the component gets replaced with the configured custom URL.
    
   ![Custom URL](../assets/img/administer/configure-domain/custom-url.png)

   Now you have successfully utilized the configured custom domain to set up a custom URL for a component.


# Configure a User Store with the Built-In Identity Provider

Developers looking to experiment with a complete application development process that includes user authentication and authorization can utilize Choreo's built-in identity provider (IdP). Choreo's built-in identity provider allows you to seamlessly test your application's authentication by setting up test users and groups within Choreo. 

!!! note
     Although the built-in IdP facilitates user management support, it is limited to adding users with attributes and groups. Therefore, the built-in IdP user management capabilities are not recommended for use in production.

## Prerequisites

Before you try out the steps in this guide, be sure you have administrator rights to your Choreo organization. This permission is essential to configure a user store with the built-in IdP.

## Configure a Choreo built-in IdP user store

Follow the steps given below to configure a Choreo built-in IdP user store for an environment:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Organization** list and then click on your organization.
3. In the left navigation menu, click **Settings**. This takes you to your organization settings.
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. On the **Identity Providers** tab, click **Manage** in the **Choreo Built-in Identity Provider** pane.
6. In the Manage IdP pane, click on a specific environment tab depending on where you want to configure the built-in IdP user store.
7. You can download the sample **User store template file(.csv )** from the **User Store** section. The template file content is similar to the following:

   ```csv
   username,password,groups,first_name,last_name,email
   "demouser","password1","[manager, engineering]","John","Doe","john@acme.org"
   ```

!!! note
     The provided template file includes a sample user with associated attributes. To add new users, insert additional rows in the `.csv` file. To include more user attributes, add columns as required in the `.csv` file.
   
8. Specify appropriate user details in the template file and save it.
9. Select the template file that you saved and click **Upload**. A successful upload creates the user store and displays the configured users in the **Users** section.


# Configure Approvals for Choreo Workflows

Choreo allows you to configure approval processes for specific workflows within the platform. An approval process for a workflow ensures that critical or sensitive changes are properly managed and controlled.

Choreo currently allows you to configure approvals for environment promotion and API subscription workflows.

Configuring approvals for environment promotion allows authorized users to control components being promoted to a critical/production environment. 

Configuring approvals for the API subscription workflow allows you to create subscription plans that require approval before being activated. This feature allows you to control access to APIs by requiring administrative review and authorization of subscriptions before they become active.

## Permissions to review and respond to approval requests

Click the respective tab for details on permissions depending on the workflow for which you want to configure approvals:

=== "Environment promotion"

     To review and respond to environment promotion approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**: 
          - Approve component promotion requests: Grants access to review and approve the promotion of components to critical environments.
      - **PROJECT-MANAGEMENT**: Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

=== "API subscription"

     To review and respond to API subscription approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**:
          - Approve API subscriptions: Grants access to review and approve API subscription workflow requests.
      - **PROJECT-MANAGEMENT**: 
          Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

## Set up an approval process for a workflow

To set up an approval process for a workflow, follow these steps:

!!! note
     - You must have administrator privileges in Choreo to configure workflow approvals.
     - Administrators can designate specific roles and assignees to review and respond to requests associated with each workflow.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Workflows** tab.
5. Click the edit icon corresponding to the workflow for which you want to configure an approval.
6. In the **Configure Workflow** dialog that opens, select roles and assignees to review and respond to workflow approval requests.

    - In the **Roles** field, select one or more roles depending on your preference. Any user assigned to these roles can review and respond to requests.
    - In the **Assignees** field, select specific users who can review and approve workflow requests. Assignees can be any Choreo user, even if they are not assigned to a selected role.

    !!! info "Important"
         Currently, there is no validation to ensure that the specified roles and assignees have the necessary permissions to review and respond to requests. If the [required permissions](#permissions-to-review-and-respond-to-approval-requests) are not correctly configured, some users may receive email notifications but will be unable to review the requests.
         
7. Click **Save**. This configures and enables the approval process for the workflow.

Once you enable the approval process for a workflow, see the following details on how to submit a request for approval and the approval process. Click the respective tab depending on the workflow for which you enabled the approval process:  

=== "Environment promotion"

     Once you configure an approval process for environment promotion, developers must [submit a request for approval to use the workflow](../develop-components/submit-and-manage-workflow-approval-requests.md). An authorized assignee must then [review and approve the request](./review-workflow-approval-requests.md) for a developer to proceed with the task related to the workflow.

=== "API subscription"

     Once you configure an approval process for API subscription, administrators can select the **Approval required** checkbox to create or update subscription plans to require approval. For details, see [Create API Subscription Plans](../administer/create-api-subscription-plans.md). API consumers using these plans must request approval to proceed. For details, see step 7 in [Subscribe to an API with a Subscription Plan](../api-management/manage-api-traffic/subscribe-to-an-api-with-a-subscription-plan.md). An authorized approver must then [review and approve the request](./review-workflow-approval-requests.md) before the subscription is granted.


# Configure Enterprise Login

With Choreo, you can configure enterprise login to allow users from an external identity provider (IdP) to sign in to Choreo seamlessly without changing their credentials.

This guide walks you through the steps to configure enterprise login for your organization in Choreo. 


## Prerequisites 

Before you proceed with the configuration, set up the following:

- A valid email domain for your organization.
- Access the Choreo Console at https://console.choreo.dev/ via your Google, GitHub, or Microsoft account. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries". 

## Configure enterprise login for your Choreo organization

To configure enterprise login for your Choreo organization, follow the steps given below:

 - **If you already have a support account with us**, send us your organization name/handle and the email domains specific to your organization through our support portal. 

 - **If you do not have a support account with us yet**, send an email to `choreo-help@wso2.com` requesting to enable enterprise login for your organization. 
      
    !!! tip
        Ensure you include the following information in the request:

         - Organization name or handle. For example, “Stark Industries” or “starkindustries”.
         - Email domains specific to your organization. For example, “@stark.com”, “@starkindustries.com”, and “@stark.eu.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise login
        
        Hi CS team,

        I need to configure enterprise login for my organization. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries
          - Email domains specific to my organization: “@stark.com”, “@starkindustries.com”, and “@stark.eu”

        Thank you.

    The Choreo support team will perform the necessary configurations and respond to you with a verification code. You must sign in to your domain host account and configure the DNS record for your email domain with the following values:

    | **Field**                          | **Value**                                      |
    |------------------------------------|------------------------------------------------|
    | **Name/Host/Alias**                | Specify `@` or leave it blank                  |
    | **Time to Live (TTL)**             | Keep the default value or use `86400`          |
    | **Value/Answer/Destination**       | wso2-domain-verification:<`verification_code`> |


Now, you are ready to bring your own identity to Choreo.

## Bring your own identity to Choreo

When you create an organization in Choreo, an organization with the same name is provisioned for you in Asgardeo. To bring your own identity to Choreo, you must configure a federated enterprise IdP on Asgardeo in the organization that is provisioned for you.

Follow the steps given below to configure the federated IdP:

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. To configure a federated enterprise identity provider for your Asgardeo organization, follow the steps in [Asgardeo documentation - Add Standard-Based Login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/).
3. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
4. Click on the application to edit it.
5. Click the **Sign-in Method** tab. You can observe the configured connection.

Now, users in your enterprise IdP can sign in to the Choreo Console using their enterprise IDs.

## Configure role-based access control for enterprise login

To streamline the enterprise login process and grant appropriate permission, Choreo provides the flexibility to configure role-based access control for users who reside in an external IdP. 

To set up role-based access control for enterprise login within Choreo, follow the steps given below:

### Prerequisites

Before you proceed with the configuration, make sure you complete the following:

1. Configure enterprise login for your organization. For instructions, see [Configure enterprise login for your Choreo organization](#configure-enterprise-login-for-your-choreo-organization). 
2. Ensure your enterprise identity provider includes the group/role attributes in tokens it sends to Asgardeo via the respective protocol.
3. Be sure you have administrator privileges in Choreo.

### Step 1: Configure Asgardeo

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. [Configure your IdP as an external IdP in Asgardeo](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/). Depending on your IdP, you can select OpenID Connect or SAML as the protocol between Asgardeo and your IdP.

    !!! note
        If you are using OpenID Connect, configure the requested scopes accordingly for Asgardeo to get the relevant group/role details from the external IdP.

3. To configure the application, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
    2. Click on the application to edit it.
    3. Click the **Sign-in Method** tab.
    4. Configure the IdP for login depending on the protocol you selected:
        - For OpenID Connect, follow the instructions in [Enable the OIDC IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-oidc-idp-login/#enable-the-oidc-idp-for-login).
        - For SAML, follow the instructions in [Enable the SAML IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-saml-idp-login/#enable-the-saml-idp-for-login).
            
    5. Click the **User Attributes** tab.
    6. Select the **Groups** attribute and click the arrow to expand the section. Then, select the **Requested** checkbox.
    7. Click **Update**.

4. To add the user attributes as OpenID Connect scopes, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **New Attribute** and select the **Groups** attribute.
    4. Click **Save** and then click **Save Changes**.

### Step 2: Map Choreo groups to enterprise IdP groups via the Choreo Console 

!!! note
    
    Before you map Choreo groups to enterprise IdP groups, ensure you meet the following criteria:

    - Asgardeo is your key manager.
    - You have permission to perform actions of the organization administrator role.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. This takes you to the organization's home page.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. In the **Access Control** tab, click **Groups**. 
5. Click **Manage IdP Group Mapping**.
    ![Group mapping](../assets/img/administer/enterprise-login/group-mapping.png)

6. Click the edit icon corresponding to the Choreo group you want to map to the enterprise IdP group.
7. In the **IdP Group Name** field, specify the exact name you configured in the enterprise IdP and enter to add it.
   
    !!! tip
        If there is a change to the IdP group mapping, it takes effect from the next login session onwards. 

8. Click **Save**. 

By following these steps, you have successfully configured role-based access control for enterprise login in Choreo, allowing users from the external IdP to have the appropriate permission.


# Configure Self-Sign-Up

With Choreo, you can set up a self-sign-up page for your Developer Portal. The self-sign-up page allows users to easily access your Developer Portal and subscribe to APIs. When you configure self-sign-up, users can create their accounts and access your Developer Portal without any manual intervention from you.

This page walks you through the steps to configure self-sign-up for your Developer Portal.

## Prerequisites

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using your Google, GitHub, or Microsoft account.
2. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries".


## Configure Developer Portal self-sign-up

To configure self-sign-up, follow the steps given below:

1. Send an email to <choreo-help@wso2.com> requesting to configure enterprise IdP for the Developer Portal of your organization. 

    !!! tip
        Ensure you include the organization name or handle in the request.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise IdP for Developer Portal
        
        Hi CS team,

        I need to configure enterprise IdP for my organization’s Developer Portal to enable self-sign-up. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries

        Thank you

    The Choreo support team will perform the necessary configurations and respond to your request.

2. When you receive a response, sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials that you used to sign in to Choreo.
3. In the Asgardeo Console, click **View all applications**.

    ![View all applications](../assets/img/administer/self-sign-up/view-all-applications.png)

    You will see an application named **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL**. 

    ![Applications](../assets/img/administer/self-sign-up/application.png)

4. Click on the application to edit it and enter your organization’s Developer Portal URL as the **Access URL** of the application. For example, `https://devportal.choreo.dev/starkindustries`.
5. Click **Update**.
6. To add user attributes, follow these steps:

    !!! info "Note"
          If you have enabled enterprise login and you want to add the **Groups** attribute during self-sign-up configuration, avoid making it mandatory. This ensures proper access control and prevents unauthorized privileges. If you make the **Groups** attribute mandatory, it allows self-signed-up users to specify a group and assume roles associated with it.

    1. Click the **User Attributes** tab.
    2. To add the email as a mandatory user attribute, select **Email** and click the arrow to expand the section. Then, select the **Requested** and **Mandatory** checkboxes.

        ![Email attribute](../assets/img/administer/self-sign-up/email-attribute.png)

    3. To add the first name and last name as optional attributes, select **Profile** and click the arrow to expand the section. Then, select the **Requested** checkbox for the **First Name** and the **Last Name** attributes.

        ![Profile attribute](../assets/img/administer/self-sign-up/profile-attribute.png)

    4. Click **Update**.

7. To add the user attributes as OpenID Connect scopes, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **+ New Attribute**.
    4. Select **Email**, **First Name**, and **Last Name** as the attributes to associate with the OpenID scope.
    5. Click **Save** and then click **Save Changes**.

        ![Save attributes as scopes](../assets/img/administer/self-sign-up/save-attributes-as-scopes.png)

8. To configure basic authentication as the sign-in method, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Applications**.
    2. In the **Applications** pane, click the **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL** application to edit it.
    3. Click the **Sign-in Method** tab and then click **Start with default configuration**.

        ![Add sign-in method](../assets/img/administer/self-sign-up/add-sign-in-method.png)

    4. Click **Update**.

9.  To configure self-registration, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Self Registration**.
    2. In the **Self Registration** pane, click **Configure**.
    3. To enable self-registration, turn on the toggle.
    4. Select **Account verification**. This displays a confirmation message to enable account verification. 
    5. Click **Continue**.
    6. Specify an appropriate value in the **Account verification link expiry time** field.
    7. Click **Update**. 
     
        ![Configure self-registration](../assets/img/administer/self-sign-up/configure-self-registration.png)

Once you complete these steps, you will see a sign up link similar to the following in your Developer Portal:

![Sign-up](../assets/img/administer/self-sign-up/sign-up.png){.cInlineImage-half}
 
Users can click **LOGIN/SIGN UP** and then click **Create an account** to sign up to access your Developer Portal.

![Create an account](../assets/img/administer/self-sign-up/create-an-account.png)

## Manage new users

To manage users who want to access your Developer Portal via self-sign-up, you have two possible approaches:

- Enable auto-approval for new user registrations: This approach automates the user approval process.  When you enable auto-approval, each user who creates an account and signs up to your Developer Portal can access it by default.
- Manually approve or reject user accounts: This allows you to review the list of user registrations and manually approve or reject each registration as needed.

### Enable auto-approval for new user registrations

To automatically approve each new user account registered on your Developer Portal, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**.
4. To enable auto-approval, turn on the toggle.

Once you enable auto-approval, users can sign in to your Developer Portal and view your APIs and applications immediately after creating an account.

### Manually approve or reject user accounts

If you have not enabled auto-approval, you can manually approve or reject new user registrations. Once a user creates an account, Choreo sends an email to ask the user to confirm the account. To manually approve or reject user accounts, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**. You will see the user accounts listed for approval.
4. To approve a user account, click **Approve**. To reject an account, click **Reject**.

    - If you approve an account, the user will receive an email confirming the approval.
    - If you reject an account, the user will receive an email mentioning that their account is rejected. 

        !!! info "Note"
               A rejected user cannot sign up to your Developer Portal using the same account again.


# Control Access in the Choreo Console

In the Choreo Console, you have the ability to manage access to projects and the actions that can be performed within them. Administrators have the capability to restrict project access to specific user groups. This feature is useful when you need certain user groups to have access to particular projects or for a set of projects.

Choreo uses **Roles**, **Groups**, and a **Mapping level** to control access to the Choreo Console as follows: 

- **Role** : Role is a collection of permissions. Choreo has a predefined set of roles with permissions assigned to them. [Learn more](../choreo-concepts/organization.md#roles)
- **Group** : Group is a collection of users. A user group requires a role or multiple roles to be assigned to it so that the users in those groups get the relevant permissions via the assigned roles. [Learn more](../choreo-concepts/organization.md#groups)

- **Mapping level** : A mapping level defines the extent at which a role-group mapping can be done. Choreo has two defined resource levels.
    - **Organization** : You can assign a role to a group or associate a group with a role within the organization. This ensures that    
                         all users in a group inherit the permissions granted by that role across all organizational resources.
                         For example, if a user has edit_project permission at the organization mapping level, that user can edit all the projects in the organization.
    - **Project** : You can assign a role to a group or associate a group with a role within a specific project resource. This ensures 
                    that users in the group inherit the permissions granted by that role only within the context of the specified project.
                    For example, If a user has edit_project permission at the project mapping level, that user can only edit the specified project.


In Choreo, authorization operates by assigning a role to a group at a specified level. The level at which the role is assigned determines the extent of permissions granted to users.

!!! warning "Important"
    Avoid assigning multiple roles to a single user across different projects or levels (organization and project). Such assignments can grant users unintended permission to some projects, allowing them to perform tasks they shouldn't have access to. Therefore, it is recommended to assign only one role to a user across projects or levels to ensure proper access control.

!!! info
    In Choreo, organization-level permissions take precedence over project-level permissions.

To elaborate further, refer to the following diagram. 

The following diagram depicts a role-group assignment at a specific resource level. In the diagram, an admin user has assigned the Developer role to all members of the Engineering group within the Engineering Project. This grants users in the Engineering group the ability to perform all actions allowed by the Developer role within the Engineering Project.

![Console access control](../assets/img/administer/access-control-to-console.png)

## Sample scenario

Now that you understand the basic concepts of access control within the Choreo Console, let’s try out a sample scenario to manage access within a project. 

Assume you are overseeing the Engineering Project within your organization and you need to grant development access to specific users solely within this project. Here's a step-by-step guide on how to achieve this:

### Step 1: Create a project

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | `Engineering Project`              |
    | **Name**                 | `engineering-project`              |
    | **Project Description**  | `My sample project`                |

4. Click **Create**. This creates the project and takes you to the project home page.

### Step 2: Create a new group

Follow the steps given below to create a group with the name `Engineering Project Developer`:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. Click **+ Create Group**.
5. Enter a group name and group description. You can enter the values given below:

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Group Name**           | `Engineering Project Developer`    |
    | **Group Description**    | `Users with development access within the engineering project`|

6. Click **Create**.

### Step 3: Assign roles to the group

Follow the steps given below to assign the **Developer** role to the **Engineering Project Developer** group that you created:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the **Engineering Project** that you created.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. On the **Groups** tab, search for the **Engineering Project Developer** group and click the corresponding edit icon.
5. Click **+Add Roles**. 
6. In the **Add Roles to Group in Project** dialog that opens, click the **Roles** list and select **Developer**.
7. Click **Add**. This assigns the **Developer** role to the group. You should see the mapping level as **Project (Engineering Project)** as follows, indicating the scope of the mapping:

    ![Mapping level](../assets/img/administer/mapping-level.png)

   This means that you have granted developer access to users in the Engineering Project Developer group in the scope of the Engineering Project. 

Now that you have set up access control, you can proceed to add users to the new group.

### Step 4: Add users to the group

There are two approaches you can follow to add users to the group.

#### Add a new user as a project developer 

Follow the steps given below to add a new user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Click **+Invite Users**.
5. In the **Invite Users** dialog,
   1. Specify the email addresses of the users in the **Emails** field.
   2. Click the **Groups** list and select **Engineering Project Developer**.
6. Click **Invite**.

#### Add an existing user as a project developer 

Follow the steps given below to add an existing user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Search for the existing user you want to add to the **Engineering Project Developer** group.
5. Click the edit icon corresponding to the user.
6. Click **+Assign Groups**.
7. In the **Add Groups to User** dialog, click the **Groups** list and select **Engineering Project Developer**.
8. Click **Add**.

!!! tip
     Make sure to remove the user from any other groups to avoid granting organization-level access unintentionally.


!!! note
     - Existing groups are already mapped to similar roles at the organization level. Therefore, adding users to those groups or keeping users in them, will give organization-level access to the users.
     - When users are added to the **Engineering Project Developer** group, they will only have developer access to the **Engineering Project**.
     - You can invite new users or add existing users to new groups within the Engineering Project, and based on their requirements, assign roles like Developer, API Publisher, etc.

Now you have successfully set up access control within your project.


# Control Egress Traffic for Your Organization

In Choreo, you can manage egress traffic originating from your applications by setting up an allow list or deny list. By default, egress traffic is allowed to any destination unless specifically restricted.

## Configure an egress policy at the organization level

To configure an egress policy at the organization level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Egress Control** tab.
5. Click **+ Create** to add a new egress policy.
6. Select the type of egress control to apply and add the required rules:

    - **Allow All**: Allows all egress traffic by default. You can selectively block traffic to specific IP ranges.
    - **Deny All**: Blocks all egress traffic by default. You can selectively allow traffic to specific IP ranges or domains.

        !!! note

             - Once you select an egress control type and create a rule, you cannot change the type. To change the type, you must delete existing rules.
             - Egress rules you add can disrupt your application if they block traffic to required destinations. Ensure you add rules appropriately to prevent such disruptions.
             - If you use the **Deny All** type, be sure to add Choreo-managed database hosts to the allowed list.
             - Egress policies apply across all environments in an organization.
             - Egress policies do not apply to API proxies.

    ![Configure an organization-level egress policy](../assets/img/administer/configure-an-organization-level-egress-policy.png)

## Override the organization-level egress policy at the project level

An egress policy set at the project level can override the organization-level policy, depending on the egress control type you select.

To override the organization-level egress policy at the project level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Project** list and select your project.
3. In the left navigation menu, click **Settings**. This opens the project-level settings page.
4. Click the **Egress Control** tab. You will see that the organization-level egress policy is enforced by default.
5. Add required project-level rules to further restrict egress traffic.

    - If the **Allow All** egress control type is selected at the organization level, you can add project-level deny rules to further restrict traffic.
    - If the **Deny All** egress control type is selected at the organization level, you can remove allow rules inherited from the organization level to further restrict traffic.

    ![Add project-level rules](../assets/img/administer/add-project-level-rules.png)


# Create API Subscription Plans

API subscription plans are essential to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security. With the option to set rate limits and burst control, subscription plans allow API providers to manage traffic, prevent misuse, and offer tiered service levels. Organizations can implement subscription plans to provide varying levels of API access, accommodating different user needs and business models, while ensuring optimal performance and security. 

In Choreo, users with the administrator role can create, update, and delete subscription plans at the organization level. 

!!! tip
    Deleting a subscription plan is only possible if there are no active subscriptions associated with it.  

To create an organization-level subscription plan, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **API Management** tab and then click **Subscription Plans**.
5. Click **+ Add Subscription Plan**.
6. In the **Create Subscription Plan** pane, enter the appropriate values for each field:
    
    !!! note
         - In the **Name** field, you must specify a name to uniquely identify the subscription plan in various contexts. The value is editable only at the time you create the subscription plan. You cannot change the name after you create it.
         - The **Stop on Quota Reach** checkbox is selected by default when creating a subscription plan. When selected, requests return an HTTP 429 response if the request count exceeds the limit. If you clear the checkbox, requests are allowed even if the quota is exceeded.
         - Burst control protects your backend from sudden request spikes and manages API usage. It’s especially useful for subscription plans where the request count is enforced over a long period, to prevent consumers from using their entire quota too quickly. Ensure you select the **Burst Control** checkbox when the **Request Count Time Unit** is selected as **Hour** or **Day**.
         - Select the **Approval required** checkbox if subscription requests made to this plan require administrator or API publisher approval to activate the plan. This allows for manual review and approval of a subscription before granting API access.
  
    ![Create subscription plan](../assets/img/administer/create-subscription-plan.png)

7. Click **Create**. This creates the subscription plan and lists it under **Subscription Plans**.

After creating subscription plans, users with the API publisher role can [assign subscription plans to APIs](../api-management/manage-api-traffic/assign-subscription-plans-to-apis.md). API consumers can then choose the appropriate subscription plan during the subscription process depending on their requirements.


# Customize the Developer Portal

The Developer Portal allows API consumers to find and consume APIs with ease. You can change the look and feel of your Developer Portal by changing the theme to match your brand. Doing so will help you give a better developer experience to your users.

To customize the Developer Portal theme, follow the steps given below:

!!! Note
    - To customize the Developer Portal theme for an organization, you need to be an admin user of that organization.
    - You cannot undo a change and restore or revert to a previous version of the theme. However, you can reset it to the default theme.

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google/ GitHub/ Microsoft account.


2. In the left pane, click **Settings**.

4. In the header, click the **Organization** list. This will open the organization level settings page. 

5. In the **API Management** tab, click **Devportal Theme**.

    ![Access Devportal theme](../assets/img/administer/devportal-theme/access-devportal-theme.png){.cInlineImage-threeQuarter}

    Once you access the theme, you can customize the **Home** page, color theme, font, header and footer, logos, etc., by expanding the relevant sections.

6. Make a change to the theme. For example, let's change the title on the **Home** page and the color theme. 

    1. To update the title on the **Home** page, expand the **Home Page** section, and in the **Title** field, change the default text (for example, to `Try our APIs!`).
   
    2. To update the color theme, expand the **Color Palette** section, and change the colors as required (for example, change the background color to `#C3C5CD` and the primary color of the buttons to `#086634`).
   
    3. Click **Preview** to view a preview of the Developer Portal with the changes you made. Based on the changes given in the examples, the preview appears as follows.

         ![Preview of customization](../assets/img/administer/devportal-theme/preview-of-customization.png){.cInlineImage-threeQuarter}
   
    4. Click **Save** to save your changes as a draft theme.
    
    5. To apply the changes to the Developer Portal, toggle the **Go Live** switch. To confirm that you want to go live with the changes, click **Enable** in the message that appears.
    	
7. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).

The **Home** page will appear as it did in the preview.

## Reset the Developer Portal theme

To reset the Developer Portal theme to the default theme, follow the steps given below:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google, GitHub, or Microsoft account.

2. In the left pane, click **Settings**.

3. In the header, click the **Organization** list. This will open the organization level settings page. 

4. In the **Organization** tab, click **Devportal Theme**, and then click **Reset to Default**.



## Inviting users

An organization administrator can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Manage Members of an Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a user of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a user of that organization.

{% include "inviting-members.md" %}

## Manage user permission

For details on how Choreo manages user permission, see [Manage user permission](../choreo-concepts/organization.md#manage-user-permission).


# Review Workflow Approval Requests

In Choreo, administrators can [configure approvals for workflows](./configure-approvals-for-choreo-workflows.md) and assign specific users as approvers.

If you are assigned as an authorized reviewer for a particular workflow approval request, you will receive an email notification when a [request is submitted for approval](../develop-components/submit-and-manage-workflow-approval-requests.md). The email includes a summary of the request and a link to the **Approvals** page in the Choreo Console, where you can review the details and either approve or reject the request.

!!! note
     - Workflow approvals are managed at the project level. If a role with the necessary permissions is assigned in a project context, only members of the user group bound to that role within the specific project will receive notifications for requests made in that project. For example, if you are assigned the Project Admin role (which includes the necessary permissions) for project A, you will only be notified of workflow requests within project A.
     - Users with organization-level permissions will receive notifications for all workflow requests across any project in the organization.

Other approvers within your organization will also receive notifications for workflow requests and may review a request before you. If a request has already been reviewed, it will appear under the **Past** tab on the **Approvals** page.

Approval requests are submitted on behalf of the team. Once approved, any authorized team member can execute the task. For certain tasks, execution may occur automatically upon approval.

## View workflow approval requests

To view workflow approval requests assigned to you, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Approvals**. This opens the **Approvals** page where you can see all approval requests assigned to you. The **Pending** tab lists requests that are yet to be reviewed. The **Past** tab displays requests already reviewed by you or other approvers, as well as requests canceled by the requester.
4. To view details of a specific request, click **Review** corresponding to it.

## Approve or reject an approval request

To approve or reject a request, follow these steps:

1. Follow the instructions in the [View workflow approval requests](#view-workflow-approval-requests) section above to see details of the workflow you want to review.
   Alternatively, click the Choreo Console link in the approval request email notification you received. This takes you to the request details in the Choreo Console.
2. Review the request and click **Approve** or **Reject** based on your decision.



# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Choreo, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Choreo, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Add Asgardeo as an external IdP in Choreo

Follow the steps below to add Asgardeo as an external IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list.

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Choreo.


# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

In organizations leveraging Microsoft Azure Active Directory (Azure AD) for identity and access management (IAM), integrating it with Choreo offers powerful API access control. This control hinges on the use of API scopes. That is, it enables the restriction of access to a designated group of users. This document guide you step-by-step to configure Azure AD as your external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- An Azure Active Directory account:  If you don’t already have one,  setup an Azure Active Directory account at [https://azure.microsoft.com/en-gb/](https://azure.microsoft.com/en-gb/).
- Administrator rights to your Choreo organization: You need this to configure the Azure AD account in your organization.

## Add Azure Active Directory as an external IdP in Choreo

Follow the steps below to add Azure AD as an IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Microsoft Entra ID (Azure AD)** as the Identity Provider. 
6. Provide a name and a description for the IdP. 
7. To obtain the `Well-Known URL` of your Azure AD instance, on your Azure account, under **Azure Active Directory** go to **App registrations**, and then **Endpoints**. Copy the URI under`OpenID Connect metadata document`.
    
    !!! info
        - In azure, there are two versions of access tokens available. By default, the IDP applications you create use the v1 access token. Therefore, if you intend to use the v1 access token, when providing the `Well-Known URL`, omit the v2.0 path segment from the URL. [Learn more](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats)
        For example, convert `https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration`-> `https://login.microsoftonline.com/<tenant-id>/.well-known/openid-configuration`
        - If you intend to work with v2.0, then the IDP application's manifest should be changed as explained in the [access tokendocumentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats). 
        
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Review the endpoints and click **Next**.




# Configure a Custom Domain for Your Organization

A custom domain is essential for effective branding, discoverability, and credibility of a website. Choreo allows you to easily configure custom domains for your organization, enabling developers to utilize it to configure custom URLs for their components such as API proxies, services, web applications, and webhooks.

This section provides an overview of Choreo’s custom domain configuration model and guides you through configuring a custom domain for your organization. It also walks you through utilizing a custom domain to configure a custom URL for a component.

## Choreo custom domain configuration model

Choreo allows organization administrators to add custom domains for their organizations. When an administrator adds custom domains to an organization, component developers can submit requests to utilize the custom domains for their respective components. These requests require approval from the organization administrator. Upon approval, the custom domain and the relevant URL customization become available to the component.

## Configure a custom domain for an organization

### Prerequisites

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Create an organization in Choreo.
    
    ![Create an organization in Choreo](../assets/img/administer/create-choreo-organization.png)

### Add a custom domain

To add a custom domain for your organization, follow the steps given below:

!!! info "Note"
     To add a custom domain, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Active Domains** tab.
5. Click **+ Add Domains**. 
6. In the **Add a Custom Domain** pane, do the following:
    1. Enter your domain name.
    2. Select the environment to apply the domain name.
    3. Select the entity type to apply the domain name.

        !!! tip
             In this context:

              - The **API** entity type represents Choreo components exposed via an endpoint, including API Proxy, Service, and Webhook components.
              - The **Web App** entity type represents the Web Application component.
       
 7. Take a look at the generated CNAME target value displayed and create a DNS record associating the domain name to the CNAME target value with your DNS provider.
    
    ![CNAME target value](../assets/img/administer/configure-domain/cname-target-value.png)

    !!! info
          When you select **Developer Portal** as the type, the environment is not applicable, and the CNAME alias will be displayed as follows:
           ![Developer Portal CNAME target value](../assets/img/administer/configure-domain/developer-portal-cname-target-value.png)

 8. Once the CNAME type DNS record is created, click **Verify**.

    !!! info "Note"
          If the CNAME mapping is correct, the verification completes successfully. It can take some time for the configured CNAME mapping to be globally available.

 9. On successful verification of the custom domain, click **Next**.
 10. Select a TLS certificate provider depending on your preference. You can either import the TLS certificates you created for the custom domain or click **Let's Encrypt** to allow Choreo to generate and manage the certificates for you.

    !!! note "If you want to import your own certificate, it should adhere to specific guidelines"
          - TLS certificate guidelines:
             - It should be issued by a certificate authority (CA) and should contain the domain's public key along with additional information such as the domain name, the company that owns the domain, the certificate's expiration date, and the digital signature of the issuing CA.
             - It should be an X509 certificate.
             - It should be in the PEM format.
             - It should be issued directly or through a wildcard entry for the provided custom URL. For example,
                - For direct issuance, the SSL file must include the exact domain name. For example, if the domain is `apis.choreo.dev`, the SSL file must include `apis.choreo.com`.
                - For wildcard entries, the SSL file should use a wildcard notation to cover all subdomains under the provided URL. For example, if the CNAME is `apis.choreo.dev`, the SSL file should use `*.choreo.dev`.
          - TLS key file guidelines:
             - It should be in the PEM format.
             - It must be encrypted using RSA encryption.
          - Certificate chain file guidelines:
             - The chain file, which is essential for some clients to verify the authenticity of a server's SSL/TLS certificate, should contain your domain's SSL/TLS certificate (optional, as this can be provided via the certificate itself) and one or more intermediate certificates in the correct order, leading back to a root certificate. 
             - All certificates in the chain should be X509 certificates in PEM format.
               <details><summary>For step-by-step instructions on constructing a certificate chain with a root certificate, click here</summary>
               To construct a certificate chain with a root certificate, you must organize and combine the certificates in the correct sequence. A typical certificate chain consists of the following:
                 - **Root certificate**: The trusted self-signed certificate issued by the certificate authority (CA).
                 - **Intermediate certificates** (if any): Certificates issued by the root CA to subordinate CAs.
                 - **Leaf certificate**: Your end-entity certificate issued by the CA. This is an optional certificate that may be included within the chain or provided separately.<br><br>
                Follow these steps to construct the certificate chain:
                    1. Obtain and organize your certificates in the correct order:
                        - **Leaf certificate**: The public certificate issued by the CA. This is optional and may be included within the chain or provided separately.
                        - **Intermediate certificates**: Obtain these from the CA, if applicable.
                        - **Root certificate**: Obtain this from the CA.  If it is self-signed, it serves as the trust anchor.
                    2. Combine the certificates into a single file in the following order:
                        - Leaf certificate: This is your public certificate issued by the CA.
                        - Intermediate certificates if applicable: Include these in the correct hierarchical order.
                        - Root certificate: Include this at the end of the file.<br><br>
                        Use a text editor or a command-line tool to concatenate the certificates into one file, ensuring each certificate begins and ends with the proper markers. Also make sure the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers appear on a new line:
                    ```
                     -----BEGIN CERTIFICATE-----
                     <Leaf Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Intermediate Certificate Content>
                     -----END CERTIFICATE-----
                     -----BEGIN CERTIFICATE-----
                     <Root Certificate Content>
                     -----END CERTIFICATE-----
                    ```
                    3. Save the concatenated file. You can save it with a name such as `certificate_chain.pem`.
                    4. Use the following command to verify that your certificate chain is constructed correctly:
                    ```
                    openssl verify -CAfile <root_or_bundle_cert>.pem certificate_chain.pem
                    ```
                    Replace `<root_or_bundle_cert>.pem` with the path to your root certificate or a bundle containing both the root and intermediate certificates.
                    5. Once the certificate chain is verified, upload it via the Choreo Console:
                        ![Upload certificate chain](../assets/img/administer/configure-domain/upload-certificate-chain.png)
                        - If the constructed chain includes the leaf certificate, follow these steps:
                            - Upload the constructed certificate chain in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Do not upload a certificate chain file, as it is already included in the TLS certificate.
                        - If the constructed chain does not include the leaf certificate, follow these steps:
                            - Upload the leaf certificate in the **TLS Certificate** field.
                            - Upload the private key file in the **TLS Key File** field.
                            - Upload the constructed certificate chain in the **Certificate Chain File** field.
 
     To proceed with this step in this guide, click **Let's Encrypt**.

 11. To save the custom domain, click **Add**.
 
Now, you have successfully added a custom domain for your organization.

You can see the added custom domain listed in the **Active Domains** tab under the URL **Settings** tab.
    
 ![Active domains](../assets/img/administer/configure-domain/active-domains.png)

The custom domain you added will be available to the entity types in the specified environment. You can request the custom domain when configuring a custom URL for a component.

!!! info "Note"
     If you add a custom domain for the **Developer Portal** type, the customization is applied immediately, and you can access the organization’s Developer Portal via the added domain.

If you want to view the entity types that use a particular custom domain, click the specific custom domain listed in the **Active Domains** tab under **URL Settings**.
 
## Configure a custom URL for a component

When an organization administrator adds custom domains for specific environments, developers can request any available custom domain to configure a custom URL for a component in a specific environment.

### Request a custom URL for a component

To request a custom URL for your component, follow the steps given below:

!!! info "Note"
     Before you request a custom domain for a specific environment, ensure that the component is deployed to that environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to customize the URL.
3. In the left navigation menu, click **Settings**. This opens the component-level settings page.
4. Click the **URL Settings** tab. This displays the active deployments of the component across different environments and indicates whether a custom URL is configured. If an active custom domain is available to configure a custom URL for a component in a specific environment, the **Edit URL Mapping** icon in the corresponding **Action** column becomes enabled.
    
    ![Active deployments](../assets/img/administer/configure-domain/active-deployments.png)

5. To configure a custom URL for a component in a specific environment, click the **Edit URL Mapping** icon under the **Action** column corresponding to the respective environment. This opens the **URL Settings** dialog, where you can specify values to request for a custom URL.
    
    ![URL settings](../assets/img/administer/configure-domain/url-settings.png)

6. In the **URL Settings** dialog, select a domain to configure a custom URL.

    !!! tip
          - The **Domain** drop-down lists the available domains for the component. You can  request for any listed domain.
          - If you want to request a custom URL for an API, you must specify an appropriate context path in the **Path** field. The **Path** field displays the default context path for the API. You can edit the path depending on your preference. 

7. Click **Configure**. This creates the custom URL mapping, which you can see under the **URL Settings** tab.  The custom URL request will be in the **Pending** status until an organization administrator approves the request.
    
    ![Pending custom URL request](../assets/img/administer/configure-domain/pending-custom-url-request.png)

### Approve a custom URL request

When a developer requests a custom URL, the request will be listed in the organization-level settings page under the **URL Settings** tab.

To approve a custom URL mapping, follow the steps given below:

!!! info "Note"
     To approve custom URL requests, you must have organization administrator privileges.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, click the **Organization** list.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **URL Settings** tab and then click the **Pending URL Requests** tab. You will see all the pending URL mapping requests sent by developers.
    
    ![Pending URL requests](../assets/img/administer/configure-domain/pending-url-requests.png)


5. Go to the custom URL you want to approve and click the corresponding **Approve URL Mapping** icon under the **Action** column.
6. Review the details and click **Approve**.
   
   Once approved, the invoke URL of the component gets replaced with the configured custom URL.
    
   ![Custom URL](../assets/img/administer/configure-domain/custom-url.png)

   Now you have successfully utilized the configured custom domain to set up a custom URL for a component.


# Configure a User Store with the Built-In Identity Provider

Developers looking to experiment with a complete application development process that includes user authentication and authorization can utilize Choreo's built-in identity provider (IdP). Choreo's built-in identity provider allows you to seamlessly test your application's authentication by setting up test users and groups within Choreo. 

!!! note
     Although the built-in IdP facilitates user management support, it is limited to adding users with attributes and groups. Therefore, the built-in IdP user management capabilities are not recommended for use in production.

## Prerequisites

Before you try out the steps in this guide, be sure you have administrator rights to your Choreo organization. This permission is essential to configure a user store with the built-in IdP.

## Configure a Choreo built-in IdP user store

Follow the steps given below to configure a Choreo built-in IdP user store for an environment:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in.
2. In the Choreo Console top navigation menu, click the **Organization** list and then click on your organization.
3. In the left navigation menu, click **Settings**. This takes you to your organization settings.
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. On the **Identity Providers** tab, click **Manage** in the **Choreo Built-in Identity Provider** pane.
6. In the Manage IdP pane, click on a specific environment tab depending on where you want to configure the built-in IdP user store.
7. You can download the sample **User store template file(.csv )** from the **User Store** section. The template file content is similar to the following:

   ```csv
   username,password,groups,first_name,last_name,email
   "demouser","password1","[manager, engineering]","John","Doe","john@acme.org"
   ```

!!! note
     The provided template file includes a sample user with associated attributes. To add new users, insert additional rows in the `.csv` file. To include more user attributes, add columns as required in the `.csv` file.
   
8. Specify appropriate user details in the template file and save it.
9. Select the template file that you saved and click **Upload**. A successful upload creates the user store and displays the configured users in the **Users** section.


# Configure Approvals for Choreo Workflows

Choreo allows you to configure approval processes for specific workflows within the platform. An approval process for a workflow ensures that critical or sensitive changes are properly managed and controlled.

Choreo currently allows you to configure approvals for environment promotion and API subscription workflows.

Configuring approvals for environment promotion allows authorized users to control components being promoted to a critical/production environment. 

Configuring approvals for the API subscription workflow allows you to create subscription plans that require approval before being activated. This feature allows you to control access to APIs by requiring administrative review and authorization of subscriptions before they become active.

## Permissions to review and respond to approval requests

Click the respective tab for details on permissions depending on the workflow for which you want to configure approvals:

=== "Environment promotion"

     To review and respond to environment promotion approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**: 
          - Approve component promotion requests: Grants access to review and approve the promotion of components to critical environments.
      - **PROJECT-MANAGEMENT**: Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

=== "API subscription"

     To review and respond to API subscription approval requests, a user must have the following permissions. Administrators must ensure that users designated to review and respond to approval requests have these permissions:

      - **WORKFLOW-MANAGEMENT**:
          - Approve API subscriptions: Grants access to review and approve API subscription workflow requests.
      - **PROJECT-MANAGEMENT**: 
          Grants access to view and approve workflow requests. This is the same permission used to update or delete projects.

## Set up an approval process for a workflow

To set up an approval process for a workflow, follow these steps:

!!! note
     - You must have administrator privileges in Choreo to configure workflow approvals.
     - Administrators can designate specific roles and assignees to review and respond to requests associated with each workflow.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Workflows** tab.
5. Click the edit icon corresponding to the workflow for which you want to configure an approval.
6. In the **Configure Workflow** dialog that opens, select roles and assignees to review and respond to workflow approval requests.

    - In the **Roles** field, select one or more roles depending on your preference. Any user assigned to these roles can review and respond to requests.
    - In the **Assignees** field, select specific users who can review and approve workflow requests. Assignees can be any Choreo user, even if they are not assigned to a selected role.

    !!! info "Important"
         Currently, there is no validation to ensure that the specified roles and assignees have the necessary permissions to review and respond to requests. If the [required permissions](#permissions-to-review-and-respond-to-approval-requests) are not correctly configured, some users may receive email notifications but will be unable to review the requests.
         
7. Click **Save**. This configures and enables the approval process for the workflow.

Once you enable the approval process for a workflow, see the following details on how to submit a request for approval and the approval process. Click the respective tab depending on the workflow for which you enabled the approval process:  

=== "Environment promotion"

     Once you configure an approval process for environment promotion, developers must [submit a request for approval to use the workflow](../develop-components/submit-and-manage-workflow-approval-requests.md). An authorized assignee must then [review and approve the request](./review-workflow-approval-requests.md) for a developer to proceed with the task related to the workflow.

=== "API subscription"

     Once you configure an approval process for API subscription, administrators can select the **Approval required** checkbox to create or update subscription plans to require approval. For details, see [Create API Subscription Plans](../administer/create-api-subscription-plans.md). API consumers using these plans must request approval to proceed. For details, see step 7 in [Subscribe to an API with a Subscription Plan](../api-management/manage-api-traffic/subscribe-to-an-api-with-a-subscription-plan.md). An authorized approver must then [review and approve the request](./review-workflow-approval-requests.md) before the subscription is granted.


# Configure Enterprise Login

With Choreo, you can configure enterprise login to allow users from an external identity provider (IdP) to sign in to Choreo seamlessly without changing their credentials.

This guide walks you through the steps to configure enterprise login for your organization in Choreo. 


## Prerequisites 

Before you proceed with the configuration, set up the following:

- A valid email domain for your organization.
- Access the Choreo Console at https://console.choreo.dev/ via your Google, GitHub, or Microsoft account. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries". 

## Configure enterprise login for your Choreo organization

To configure enterprise login for your Choreo organization, follow the steps given below:

 - **If you already have a support account with us**, send us your organization name/handle and the email domains specific to your organization through our support portal. 

 - **If you do not have a support account with us yet**, send an email to `choreo-help@wso2.com` requesting to enable enterprise login for your organization. 
      
    !!! tip
        Ensure you include the following information in the request:

         - Organization name or handle. For example, “Stark Industries” or “starkindustries”.
         - Email domains specific to your organization. For example, “@stark.com”, “@starkindustries.com”, and “@stark.eu.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise login
        
        Hi CS team,

        I need to configure enterprise login for my organization. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries
          - Email domains specific to my organization: “@stark.com”, “@starkindustries.com”, and “@stark.eu”

        Thank you.

    The Choreo support team will perform the necessary configurations and respond to you with a verification code. You must sign in to your domain host account and configure the DNS record for your email domain with the following values:

    | **Field**                          | **Value**                                      |
    |------------------------------------|------------------------------------------------|
    | **Name/Host/Alias**                | Specify `@` or leave it blank                  |
    | **Time to Live (TTL)**             | Keep the default value or use `86400`          |
    | **Value/Answer/Destination**       | wso2-domain-verification:<`verification_code`> |


Now, you are ready to bring your own identity to Choreo.

## Bring your own identity to Choreo

When you create an organization in Choreo, an organization with the same name is provisioned for you in Asgardeo. To bring your own identity to Choreo, you must configure a federated enterprise IdP on Asgardeo in the organization that is provisioned for you.

Follow the steps given below to configure the federated IdP:

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. To configure a federated enterprise identity provider for your Asgardeo organization, follow the steps in [Asgardeo documentation - Add Standard-Based Login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/).
3. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
4. Click on the application to edit it.
5. Click the **Sign-in Method** tab. You can observe the configured connection.

Now, users in your enterprise IdP can sign in to the Choreo Console using their enterprise IDs.

## Configure role-based access control for enterprise login

To streamline the enterprise login process and grant appropriate permission, Choreo provides the flexibility to configure role-based access control for users who reside in an external IdP. 

To set up role-based access control for enterprise login within Choreo, follow the steps given below:

### Prerequisites

Before you proceed with the configuration, make sure you complete the following:

1. Configure enterprise login for your organization. For instructions, see [Configure enterprise login for your Choreo organization](#configure-enterprise-login-for-your-choreo-organization). 
2. Ensure your enterprise identity provider includes the group/role attributes in tokens it sends to Asgardeo via the respective protocol.
3. Be sure you have administrator privileges in Choreo.

### Step 1: Configure Asgardeo

1. Sign in to [Asgardeo](https://asgardeo.io/).
2. [Configure your IdP as an external IdP in Asgardeo](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/). Depending on your IdP, you can select OpenID Connect or SAML as the protocol between Asgardeo and your IdP.

    !!! note
        If you are using OpenID Connect, configure the requested scopes accordingly for Asgardeo to get the relevant group/role details from the external IdP.

3. To configure the application, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Applications**. You will see an application named **WSO2_LOGIN_FOR_CHOREO_CONSOLE**.
    2. Click on the application to edit it.
    3. Click the **Sign-in Method** tab.
    4. Configure the IdP for login depending on the protocol you selected:
        - For OpenID Connect, follow the instructions in [Enable the OIDC IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-oidc-idp-login/#enable-the-oidc-idp-for-login).
        - For SAML, follow the instructions in [Enable the SAML IdP for login](https://wso2.com/asgardeo/docs/guides/authentication/enterprise-login/add-saml-idp-login/#enable-the-saml-idp-for-login).
            
    5. Click the **User Attributes** tab.
    6. Select the **Groups** attribute and click the arrow to expand the section. Then, select the **Requested** checkbox.
    7. Click **Update**.

4. To add the user attributes as OpenID Connect scopes, follow the steps given below:
    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **New Attribute** and select the **Groups** attribute.
    4. Click **Save** and then click **Save Changes**.

### Step 2: Map Choreo groups to enterprise IdP groups via the Choreo Console 

!!! note
    
    Before you map Choreo groups to enterprise IdP groups, ensure you meet the following criteria:

    - Asgardeo is your key manager.
    - You have permission to perform actions of the organization administrator role.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**. This takes you to the organization's home page.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page. 
4. In the **Access Control** tab, click **Groups**. 
5. Click **Manage IdP Group Mapping**.
    ![Group mapping](../assets/img/administer/enterprise-login/group-mapping.png)

6. Click the edit icon corresponding to the Choreo group you want to map to the enterprise IdP group.
7. In the **IdP Group Name** field, specify the exact name you configured in the enterprise IdP and enter to add it.
   
    !!! tip
        If there is a change to the IdP group mapping, it takes effect from the next login session onwards. 

8. Click **Save**. 

By following these steps, you have successfully configured role-based access control for enterprise login in Choreo, allowing users from the external IdP to have the appropriate permission.


# Configure Self-Sign-Up

With Choreo, you can set up a self-sign-up page for your Developer Portal. The self-sign-up page allows users to easily access your Developer Portal and subscribe to APIs. When you configure self-sign-up, users can create their accounts and access your Developer Portal without any manual intervention from you.

This page walks you through the steps to configure self-sign-up for your Developer Portal.

## Prerequisites

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using your Google, GitHub, or Microsoft account.
2. If you are a new user, create an organization with a unique organization name. For example, "Stark Industries".


## Configure Developer Portal self-sign-up

To configure self-sign-up, follow the steps given below:

1. Send an email to <choreo-help@wso2.com> requesting to configure enterprise IdP for the Developer Portal of your organization. 

    !!! tip
        Ensure you include the organization name or handle in the request.


    !!! note "Sample email"
        Subject : [Stark Industries] Configure enterprise IdP for Developer Portal
        
        Hi CS team,

        I need to configure enterprise IdP for my organization’s Developer Portal to enable self-sign-up. Can you please do the necessary configurations to proceed?

        My organization details are as follows: 

          - Organization name: Stark Industries
          - Organization handle:  starkindustries

        Thank you

    The Choreo support team will perform the necessary configurations and respond to your request.

2. When you receive a response, sign in to [Asgardeo](https://console.asgardeo.io/) using the same credentials that you used to sign in to Choreo.
3. In the Asgardeo Console, click **View all applications**.

    ![View all applications](../assets/img/administer/self-sign-up/view-all-applications.png)

    You will see an application named **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL**. 

    ![Applications](../assets/img/administer/self-sign-up/application.png)

4. Click on the application to edit it and enter your organization’s Developer Portal URL as the **Access URL** of the application. For example, `https://devportal.choreo.dev/starkindustries`.
5. Click **Update**.
6. To add user attributes, follow these steps:

    !!! info "Note"
          If you have enabled enterprise login and you want to add the **Groups** attribute during self-sign-up configuration, avoid making it mandatory. This ensures proper access control and prevents unauthorized privileges. If you make the **Groups** attribute mandatory, it allows self-signed-up users to specify a group and assume roles associated with it.

    1. Click the **User Attributes** tab.
    2. To add the email as a mandatory user attribute, select **Email** and click the arrow to expand the section. Then, select the **Requested** and **Mandatory** checkboxes.

        ![Email attribute](../assets/img/administer/self-sign-up/email-attribute.png)

    3. To add the first name and last name as optional attributes, select **Profile** and click the arrow to expand the section. Then, select the **Requested** checkbox for the **First Name** and the **Last Name** attributes.

        ![Profile attribute](../assets/img/administer/self-sign-up/profile-attribute.png)

    4. Click **Update**.

7. To add the user attributes as OpenID Connect scopes, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Scopes**.
    2. In the **OpenID Connect Scopes** pane, click **OpenID** to edit it.
    3. Click **+ New Attribute**.
    4. Select **Email**, **First Name**, and **Last Name** as the attributes to associate with the OpenID scope.
    5. Click **Save** and then click **Save Changes**.

        ![Save attributes as scopes](../assets/img/administer/self-sign-up/save-attributes-as-scopes.png)

8. To configure basic authentication as the sign-in method, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Applications**.
    2. In the **Applications** pane, click the **WSO2_LOGIN_FOR_CHOREO_DEV_PORTAL** application to edit it.
    3. Click the **Sign-in Method** tab and then click **Start with default configuration**.

        ![Add sign-in method](../assets/img/administer/self-sign-up/add-sign-in-method.png)

    4. Click **Update**.

9.  To configure self-registration, follow these steps:

    1. In the Asgardeo Console left navigation menu, click **Self Registration**.
    2. In the **Self Registration** pane, click **Configure**.
    3. To enable self-registration, turn on the toggle.
    4. Select **Account verification**. This displays a confirmation message to enable account verification. 
    5. Click **Continue**.
    6. Specify an appropriate value in the **Account verification link expiry time** field.
    7. Click **Update**. 
     
        ![Configure self-registration](../assets/img/administer/self-sign-up/configure-self-registration.png)

Once you complete these steps, you will see a sign up link similar to the following in your Developer Portal:

![Sign-up](../assets/img/administer/self-sign-up/sign-up.png){.cInlineImage-half}
 
Users can click **LOGIN/SIGN UP** and then click **Create an account** to sign up to access your Developer Portal.

![Create an account](../assets/img/administer/self-sign-up/create-an-account.png)

## Manage new users

To manage users who want to access your Developer Portal via self-sign-up, you have two possible approaches:

- Enable auto-approval for new user registrations: This approach automates the user approval process.  When you enable auto-approval, each user who creates an account and signs up to your Developer Portal can access it by default.
- Manually approve or reject user accounts: This allows you to review the list of user registrations and manually approve or reject each registration as needed.

### Enable auto-approval for new user registrations

To automatically approve each new user account registered on your Developer Portal, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**.
4. To enable auto-approval, turn on the toggle.

Once you enable auto-approval, users can sign in to your Developer Portal and view your APIs and applications immediately after creating an account.

### Manually approve or reject user accounts

If you have not enabled auto-approval, you can manually approve or reject new user registrations. Once a user creates an account, Choreo sends an email to ask the user to confirm the account. To manually approve or reject user accounts, follow the steps given below:

1. In the [Choreo Console](https://console.choreo.dev/), click your username in the top right corner.
2. In the drop-down menu, click **Settings**. This opens the **Organization** pane, where you can make necessary changes to organization settings.
3. In the **Organization** pane, click **Self Signups**. You will see the user accounts listed for approval.
4. To approve a user account, click **Approve**. To reject an account, click **Reject**.

    - If you approve an account, the user will receive an email confirming the approval.
    - If you reject an account, the user will receive an email mentioning that their account is rejected. 

        !!! info "Note"
               A rejected user cannot sign up to your Developer Portal using the same account again.


# Control Access in the Choreo Console

In the Choreo Console, you have the ability to manage access to projects and the actions that can be performed within them. Administrators have the capability to restrict project access to specific user groups. This feature is useful when you need certain user groups to have access to particular projects or for a set of projects.

Choreo uses **Roles**, **Groups**, and a **Mapping level** to control access to the Choreo Console as follows: 

- **Role** : Role is a collection of permissions. Choreo has a predefined set of roles with permissions assigned to them. [Learn more](../choreo-concepts/organization.md#roles)
- **Group** : Group is a collection of users. A user group requires a role or multiple roles to be assigned to it so that the users in those groups get the relevant permissions via the assigned roles. [Learn more](../choreo-concepts/organization.md#groups)

- **Mapping level** : A mapping level defines the extent at which a role-group mapping can be done. Choreo has two defined resource levels.
    - **Organization** : You can assign a role to a group or associate a group with a role within the organization. This ensures that    
                         all users in a group inherit the permissions granted by that role across all organizational resources.
                         For example, if a user has edit_project permission at the organization mapping level, that user can edit all the projects in the organization.
    - **Project** : You can assign a role to a group or associate a group with a role within a specific project resource. This ensures 
                    that users in the group inherit the permissions granted by that role only within the context of the specified project.
                    For example, If a user has edit_project permission at the project mapping level, that user can only edit the specified project.


In Choreo, authorization operates by assigning a role to a group at a specified level. The level at which the role is assigned determines the extent of permissions granted to users.

!!! warning "Important"
    Avoid assigning multiple roles to a single user across different projects or levels (organization and project). Such assignments can grant users unintended permission to some projects, allowing them to perform tasks they shouldn't have access to. Therefore, it is recommended to assign only one role to a user across projects or levels to ensure proper access control.

!!! info
    In Choreo, organization-level permissions take precedence over project-level permissions.

To elaborate further, refer to the following diagram. 

The following diagram depicts a role-group assignment at a specific resource level. In the diagram, an admin user has assigned the Developer role to all members of the Engineering group within the Engineering Project. This grants users in the Engineering group the ability to perform all actions allowed by the Developer role within the Engineering Project.

![Console access control](../assets/img/administer/access-control-to-console.png)

## Sample scenario

Now that you understand the basic concepts of access control within the Choreo Console, let’s try out a sample scenario to manage access within a project. 

Assume you are overseeing the Engineering Project within your organization and you need to grant development access to specific users solely within this project. Here's a step-by-step guide on how to achieve this:

### Step 1: Create a project

Follow the steps given below to create a project:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter a display name, unique name, and description for the project. You can enter the values given below:
    
    !!! info
         In the **Name** field, you must specify a name to uniquely identify your project in various contexts. The value is editable only at the time you create the project. You cannot change the name after you create the project.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | `Engineering Project`              |
    | **Name**                 | `engineering-project`              |
    | **Project Description**  | `My sample project`                |

4. Click **Create**. This creates the project and takes you to the project home page.

### Step 2: Create a new group

Follow the steps given below to create a group with the name `Engineering Project Developer`:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. Click **+ Create Group**.
5. Enter a group name and group description. You can enter the values given below:

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Group Name**           | `Engineering Project Developer`    |
    | **Group Description**    | `Users with development access within the engineering project`|

6. Click **Create**.

### Step 3: Assign roles to the group

Follow the steps given below to assign the **Developer** role to the **Engineering Project Developer** group that you created:

1. In the Choreo Console, go to the top navigation menu, click the **Project** list, and select the **Engineering Project** that you created.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Groups** tab.
4. On the **Groups** tab, search for the **Engineering Project Developer** group and click the corresponding edit icon.
5. Click **+Add Roles**. 
6. In the **Add Roles to Group in Project** dialog that opens, click the **Roles** list and select **Developer**.
7. Click **Add**. This assigns the **Developer** role to the group. You should see the mapping level as **Project (Engineering Project)** as follows, indicating the scope of the mapping:

    ![Mapping level](../assets/img/administer/mapping-level.png)

   This means that you have granted developer access to users in the Engineering Project Developer group in the scope of the Engineering Project. 

Now that you have set up access control, you can proceed to add users to the new group.

### Step 4: Add users to the group

There are two approaches you can follow to add users to the group.

#### Add a new user as a project developer 

Follow the steps given below to add a new user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Click **+Invite Users**.
5. In the **Invite Users** dialog,
   1. Specify the email addresses of the users in the **Emails** field.
   2. Click the **Groups** list and select **Engineering Project Developer**.
6. Click **Invite**.

#### Add an existing user as a project developer 

Follow the steps given below to add an existing user as a project developer:

1. In the Choreo Console, go to the top navigation menu, click the **Organization** list, and select the organization where you created your project.
2. In the left navigation menu, click **Settings**.
3. Click the **Access Control** tab and then click the **Users** tab.
4. Search for the existing user you want to add to the **Engineering Project Developer** group.
5. Click the edit icon corresponding to the user.
6. Click **+Assign Groups**.
7. In the **Add Groups to User** dialog, click the **Groups** list and select **Engineering Project Developer**.
8. Click **Add**.

!!! tip
     Make sure to remove the user from any other groups to avoid granting organization-level access unintentionally.


!!! note
     - Existing groups are already mapped to similar roles at the organization level. Therefore, adding users to those groups or keeping users in them, will give organization-level access to the users.
     - When users are added to the **Engineering Project Developer** group, they will only have developer access to the **Engineering Project**.
     - You can invite new users or add existing users to new groups within the Engineering Project, and based on their requirements, assign roles like Developer, API Publisher, etc.

Now you have successfully set up access control within your project.


# Control Egress Traffic for Your Organization

In Choreo, you can manage egress traffic originating from your applications by setting up an allow list or deny list. By default, egress traffic is allowed to any destination unless specifically restricted.

## Configure an egress policy at the organization level

To configure an egress policy at the organization level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **Egress Control** tab.
5. Click **+ Create** to add a new egress policy.
6. Select the type of egress control to apply and add the required rules:

    - **Allow All**: Allows all egress traffic by default. You can selectively block traffic to specific IP ranges.
    - **Deny All**: Blocks all egress traffic by default. You can selectively allow traffic to specific IP ranges or domains.

        !!! note

             - Once you select an egress control type and create a rule, you cannot change the type. To change the type, you must delete existing rules.
             - Egress rules you add can disrupt your application if they block traffic to required destinations. Ensure you add rules appropriately to prevent such disruptions.
             - If you use the **Deny All** type, be sure to add Choreo-managed database hosts to the allowed list.
             - Egress policies apply across all environments in an organization.
             - Egress policies do not apply to API proxies.

    ![Configure an organization-level egress policy](../assets/img/administer/configure-an-organization-level-egress-policy.png)

## Override the organization-level egress policy at the project level

An egress policy set at the project level can override the organization-level policy, depending on the egress control type you select.

To override the organization-level egress policy at the project level, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Project** list and select your project.
3. In the left navigation menu, click **Settings**. This opens the project-level settings page.
4. Click the **Egress Control** tab. You will see that the organization-level egress policy is enforced by default.
5. Add required project-level rules to further restrict egress traffic.

    - If the **Allow All** egress control type is selected at the organization level, you can add project-level deny rules to further restrict traffic.
    - If the **Deny All** egress control type is selected at the organization level, you can remove allow rules inherited from the organization level to further restrict traffic.

    ![Add project-level rules](../assets/img/administer/add-project-level-rules.png)


# Create API Subscription Plans

API subscription plans are essential to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security. With the option to set rate limits and burst control, subscription plans allow API providers to manage traffic, prevent misuse, and offer tiered service levels. Organizations can implement subscription plans to provide varying levels of API access, accommodating different user needs and business models, while ensuring optimal performance and security. 

In Choreo, users with the administrator role can create, update, and delete subscription plans at the organization level. 

!!! tip
    Deleting a subscription plan is only possible if there are no active subscriptions associated with it.  

To create an organization-level subscription plan, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization. 
3. In the left navigation menu, click **Settings**. This opens the organization-level settings page.
4. Click the **API Management** tab and then click **Subscription Plans**.
5. Click **+ Add Subscription Plan**.
6. In the **Create Subscription Plan** pane, enter the appropriate values for each field:
    
    !!! note
         - In the **Name** field, you must specify a name to uniquely identify the subscription plan in various contexts. The value is editable only at the time you create the subscription plan. You cannot change the name after you create it.
         - The **Stop on Quota Reach** checkbox is selected by default when creating a subscription plan. When selected, requests return an HTTP 429 response if the request count exceeds the limit. If you clear the checkbox, requests are allowed even if the quota is exceeded.
         - Burst control protects your backend from sudden request spikes and manages API usage. It’s especially useful for subscription plans where the request count is enforced over a long period, to prevent consumers from using their entire quota too quickly. Ensure you select the **Burst Control** checkbox when the **Request Count Time Unit** is selected as **Hour** or **Day**.
         - Select the **Approval required** checkbox if subscription requests made to this plan require administrator or API publisher approval to activate the plan. This allows for manual review and approval of a subscription before granting API access.
  
    ![Create subscription plan](../assets/img/administer/create-subscription-plan.png)

7. Click **Create**. This creates the subscription plan and lists it under **Subscription Plans**.

After creating subscription plans, users with the API publisher role can [assign subscription plans to APIs](../api-management/manage-api-traffic/assign-subscription-plans-to-apis.md). API consumers can then choose the appropriate subscription plan during the subscription process depending on their requirements.


# Customize the Developer Portal

The Developer Portal allows API consumers to find and consume APIs with ease. You can change the look and feel of your Developer Portal by changing the theme to match your brand. Doing so will help you give a better developer experience to your users.

To customize the Developer Portal theme, follow the steps given below:

!!! Note
    - To customize the Developer Portal theme for an organization, you need to be an admin user of that organization.
    - You cannot undo a change and restore or revert to a previous version of the theme. However, you can reset it to the default theme.

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google/ GitHub/ Microsoft account.


2. In the left pane, click **Settings**.

4. In the header, click the **Organization** list. This will open the organization level settings page. 

5. In the **API Management** tab, click **Devportal Theme**.

    ![Access Devportal theme](../assets/img/administer/devportal-theme/access-devportal-theme.png){.cInlineImage-threeQuarter}

    Once you access the theme, you can customize the **Home** page, color theme, font, header and footer, logos, etc., by expanding the relevant sections.

6. Make a change to the theme. For example, let's change the title on the **Home** page and the color theme. 

    1. To update the title on the **Home** page, expand the **Home Page** section, and in the **Title** field, change the default text (for example, to `Try our APIs!`).
   
    2. To update the color theme, expand the **Color Palette** section, and change the colors as required (for example, change the background color to `#C3C5CD` and the primary color of the buttons to `#086634`).
   
    3. Click **Preview** to view a preview of the Developer Portal with the changes you made. Based on the changes given in the examples, the preview appears as follows.

         ![Preview of customization](../assets/img/administer/devportal-theme/preview-of-customization.png){.cInlineImage-threeQuarter}
   
    4. Click **Save** to save your changes as a draft theme.
    
    5. To apply the changes to the Developer Portal, toggle the **Go Live** switch. To confirm that you want to go live with the changes, click **Enable** in the message that appears.
    	
7. Sign in to the Choreo Developer Portal at [https://devportal.choreo.dev](https://devportal.choreo.dev).

The **Home** page will appear as it did in the preview.

## Reset the Developer Portal theme

To reset the Developer Portal theme to the default theme, follow the steps given below:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev/) using a Google, GitHub, or Microsoft account.

2. In the left pane, click **Settings**.

3. In the header, click the **Organization** list. This will open the organization level settings page. 

4. In the **Organization** tab, click **Devportal Theme**, and then click **Reset to Default**.



## Inviting users

An organization administrator can invite users to the organization by assigning them specific groups. Invited users receive an invitation via email. An invited user must accept the invitation to join the organization and access the resources of that organization.

# Manage Members of an Organization

An organization in Choreo is a logical grouping of users and user resources. A first-time user must create an organization and be a user of it when signing in to Choreo. Users and resources in an organization cannot access resources in another organization unless an admin of the other organization invites them and adds them as a user of that organization.

{% include "inviting-members.md" %}

## Manage user permission

For details on how Choreo manages user permission, see [Manage user permission](../choreo-concepts/organization.md#manage-user-permission).


# Review Workflow Approval Requests

In Choreo, administrators can [configure approvals for workflows](./configure-approvals-for-choreo-workflows.md) and assign specific users as approvers.

If you are assigned as an authorized reviewer for a particular workflow approval request, you will receive an email notification when a [request is submitted for approval](../develop-components/submit-and-manage-workflow-approval-requests.md). The email includes a summary of the request and a link to the **Approvals** page in the Choreo Console, where you can review the details and either approve or reject the request.

!!! note
     - Workflow approvals are managed at the project level. If a role with the necessary permissions is assigned in a project context, only members of the user group bound to that role within the specific project will receive notifications for requests made in that project. For example, if you are assigned the Project Admin role (which includes the necessary permissions) for project A, you will only be notified of workflow requests within project A.
     - Users with organization-level permissions will receive notifications for all workflow requests across any project in the organization.

Other approvers within your organization will also receive notifications for workflow requests and may review a request before you. If a request has already been reviewed, it will appear under the **Past** tab on the **Approvals** page.

Approval requests are submitted on behalf of the team. Once approved, any authorized team member can execute the task. For certain tasks, execution may occur automatically upon approval.

## View workflow approval requests

To view workflow approval requests assigned to you, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the Choreo Console header, go to the **Organization** list and select your organization.
3. In the left navigation menu, click **Approvals**. This opens the **Approvals** page where you can see all approval requests assigned to you. The **Pending** tab lists requests that are yet to be reviewed. The **Past** tab displays requests already reviewed by you or other approvers, as well as requests canceled by the requester.
4. To view details of a specific request, click **Review** corresponding to it.

## Approve or reject an approval request

To approve or reject a request, follow these steps:

1. Follow the instructions in the [View workflow approval requests](#view-workflow-approval-requests) section above to see details of the workflow you want to review.
   Alternatively, click the Choreo Console link in the approval request email notification you received. This takes you to the request details in the Choreo Console.
2. Review the request and click **Approve** or **Reject** based on your decision.



# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Choreo, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Choreo, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Add Asgardeo as an external IdP in Choreo

Follow the steps below to add Asgardeo as an external IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list.

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Choreo.


# Configure Azure Active Directory (Azure AD) as an External Identity Provider (IdP)

In organizations leveraging Microsoft Azure Active Directory (Azure AD) for identity and access management (IAM), integrating it with Choreo offers powerful API access control. This control hinges on the use of API scopes. That is, it enables the restriction of access to a designated group of users. This document guide you step-by-step to configure Azure AD as your external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- An Azure Active Directory account:  If you don’t already have one,  setup an Azure Active Directory account at [https://azure.microsoft.com/en-gb/](https://azure.microsoft.com/en-gb/).
- Administrator rights to your Choreo organization: You need this to configure the Azure AD account in your organization.

## Add Azure Active Directory as an external IdP in Choreo

Follow the steps below to add Azure AD as an IdP in Choreo:

1. Sign in to the Choreo Console at [https://console.choreo.dev/](https://console.choreo.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Microsoft Entra ID (Azure AD)** as the Identity Provider. 
6. Provide a name and a description for the IdP. 
7. To obtain the `Well-Known URL` of your Azure AD instance, on your Azure account, under **Azure Active Directory** go to **App registrations**, and then **Endpoints**. Copy the URI under`OpenID Connect metadata document`.
    
    !!! info
        - In azure, there are two versions of access tokens available. By default, the IDP applications you create use the v1 access token. Therefore, if you intend to use the v1 access token, when providing the `Well-Known URL`, omit the v2.0 path segment from the URL. [Learn more](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats)
        For example, convert `https://login.microsoftonline.com/<tenant-id>/v2.0/.well-known/openid-configuration`-> `https://login.microsoftonline.com/<tenant-id>/.well-known/openid-configuration`
        - If you intend to work with v2.0, then the IDP application's manifest should be changed as explained in the [access tokendocumentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#token-formats). 
        
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Review the endpoints and click **Next**.


