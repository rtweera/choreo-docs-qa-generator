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