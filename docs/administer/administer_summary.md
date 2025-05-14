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