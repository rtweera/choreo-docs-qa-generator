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