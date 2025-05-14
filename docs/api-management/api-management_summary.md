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