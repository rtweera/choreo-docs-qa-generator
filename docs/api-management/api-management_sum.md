     # API Rate Limiting

API rate limiting is a technique that allows you to control the rate of requests made to an API. Rate limiting helps 
prevent system overload and enhances API performance. When you limit the number of requests that can be made in a 
specific time frame, you can ensure that your API is available and responsive to all users while protecting it from 
malicious attacks.

This page walks you through the steps to enable rate limiting for your APIs via Choreo and also provides information on 
the rate-limiting options supported by Choreo.

## Enable rate limiting for an API

To enable rate limiting for an API, follow the steps given below: 

!!! note
     You can apply rate-limiting settings separately for each environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). 
2. In the **Component Listing** pane, click on the component for which you want to apply rate limiting.
3. In the left navigation menu, click **Deploy**.
4. Go to the required environment card and click the view icon corresponding to the endpoint for which you want to apply rate limiting. 

    !!! info 
         If you are applying rate limiting for an API Proxy component, go to the required environment card, click the setting icon corresponding to **API Configuration**, and proceed to step 6.

5. In the **Endpoint Details** pane that opens, click the settings icon.
6. In the **Manage** section, click **Rate Limiting** to expand it.
7. Select a **Rate Limiting Level** depending on your requirement and click **Apply**.

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

By default, the APIs published in Choreo are visible to anyone who visits the Choreo Developer Portal. By default, Choreo sets the visibility of the API to `Public`. However, developers can control the visibility of their APIs by changing the default option to `Private` or `Restricted`. 

Visibility settings control users from viewing and modifying APIs. API visibility can be one of the following options:

 - **Public** : The API is **visible to all** in the developer portal.

 - **Private** : The API is visible to the **users who only sign in to the Developer Portal**.

 - **Restricted**: The API is **visible to only the user that has the roles that you specify**. This option helps developers to enforce fine-grained access control to the API.

## Change API visibility

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the REST API (Service) for which you want to control API visibility. 
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, select the required visibility setting from the **Visibility** list. 

    !!! note "Enable fine-grained role-based access control to the API"
         1. To enable fine-grained role-based access control to an API in the Developer Portal, select `Restricted` from the **API visibility** list. Once selected, you will see the roles available in your organization in the **Visible Roles** list. 
         2. Select any combination of roles. Only the users with the given roles can access the APIs through the Dev Portal. 
         3. Alternatively, You can create a new role and assign it to an API by following the steps below: 
             1. Click **+ Create New Role** in the list.
             2. Add the role name and description. 
             3. Click **Next**.
             4. Assign the relevant permissions to the new role.
             5. Click **Create**.
             6. Select the newly created role from the **Visible Roles** list.

6. Click **Save**.


# Documents

When an API consumer signs in to the Choreo Developer Portal to browse APIs, it is not sufficient to just have an API thumbnail along with the name and version of the API. An API consumer would expect to see more details about the API, such as the following:

 - A brief description of the API.
 - How to invoke the API.
 - The limitations/restrictions of the API.
 - Version history.

To provide such information that improves the overall visibility of the API, an API developer can add such documentation to an API before publishing it to the Developer Portal.

## Add documents to an API

To add documentation for an API, follow the steps given below.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).

2. In the **Component Listing** pane, click on the component for which you want to add documents. 

3. In the left navigation menu, click **Manage** and then click **Documents**.

4. Specify a title for the document and provide the content in markdown syntax. 
   
5. Click **Add** to save the document.

Depending on the information you need to add to the API, you can add one or more documents.

You can also edit existing documents and delete documents if necessary.


# Lifecycle Management

API lifecycle management is an important aspect of API management. The API lifecycle consists of various states that an API passes through, from creation to retirement. In Choreo, there are six distinct lifecycle states: created, pre-released, published, blocked, deprecated, and retired.

By leveraging the various lifecycle states, API managers can optimize the development process and ensure that subscribers have access to the latest and most reliable APIs.

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

To change the lifecycle state of an API via the Choreo Console, follow the instructions given below:

!!! tip      
     You must have publishing privileges to manage the lifecycle states of a component.

1. Sign in to the Choreo Console.
2. In the **Component Listing** pane, click on the component for which you want to manage the lifecycle.
3. In the left navigation menu, click **Manage**, and then click **Lifecycle**.
4. In the **Lifecycle Management** pane, you will see the lifecycle state transition diagram indicating the current lifecycle state of the component. Just above the lifecycle state transition diagram, The possible lifecycle states you can apply to the component are displayed just above the lifecycle state transition diagram. Click on a required lifecycle state to apply it to the component. For example, if a component is in the **Created** state, you can click either **Pre-release** or **Publish**.


# Rename API Display Name

Choreo allows you to make one or more endpoints accessible through its service and integration components. These endpoints are published as individual APIs in Choreo, accessible via the Choreo Developer Portal. By default, Choreo assigns an API name by combining the component name and the endpoint name, resulting in the following format: `<component name>-<endpoint name>`. For example, if you create a component named `Ballerina Reading List,` the API is displayed as `Ballerina Reading List - GraphQL Reading List 591.`

Choreo provides you with the flexibility to personalize the display name of the API, enhancing its user-friendliness and readability. Once you modify the API display name within the Choreo Console, Choreo applies the change immediately. From there onwards, Choreo displays the published API by this name in the Choreo Developer Portal.

Follow the steps below to rename the API display name:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. In the **Component Listing** pane, click on the component for which you want to rename the API display name. This opens the **Overview** page of the component.
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, specify an appropriate API display name in the **Name** field.
6. Click **Save**.

Now, you can view the updated API display name in the Choreo Developer Portal.


# OWASP Top 10

A set of rules enforcing OWASP security guidelines to prevent common vulnerabilities and ensure secure coding practices.
### ❌ owasp:api1:2023-no-numeric-ids

Use random IDs that cannot be guessed. UUIDs are preferred but any other random string will do.

---

### ❌ owasp:api2:2023-no-http-basic

Basic authentication credentials transported over network are more susceptible to interception than other forms of authentication, and as they are not encrypted it means passwords and tokens are more easily leaked.

---

### ❌ owasp:api2:2023-no-api-keys-in-url

API Keys are passed in headers, cookies, or query parameters to access APIs. Those keys can be eavesdropped, especially when they are passed in the URL, as logging or history tools will keep track of them and potentially expose them.

---

### ❌ owasp:api2:2023-no-credentials-in-url

URL parameters MUST NOT contain credentials such as API key, password, or secret.

---

### ❌ owasp:api2:2023-auth-insecure-schemes

There are many [HTTP authorization schemes](https://www.iana.org/assignments/http-authschemes/) but some of them are now considered insecure, such as negotiating authentication using specifications like NTLM or OAuth v1.

---

### ❌ owasp:api2:2023-jwt-best-practices

JSON Web Tokens RFC7519 is a compact, URL-safe, means of representing claims to be transferred between two parties. JWT can be enclosed in encrypted or signed tokens like JWS and JWE.

The [JOSE IANA registry](https://www.iana.org/assignments/jose/jose.xhtml) provides algorithms information.

RFC8725 describes common pitfalls in the JWx specifications and in
their implementations, such as:
- the ability to ignore algorithms, eg. `{"alg": "none"}`;
- using insecure algorithms like `RSASSA-PKCS1-v1_5` eg. `{"alg": "RS256"}`.
An API using JWT should explicit in the `description`
that the implementation conforms to RFC8725.
```
components:
  securitySchemes:
    JWTBearer:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        A bearer token in the format of a JWS and conformato
        to the specifications included in RFC8725.
```

---

### ❌ owasp:api2:2023-short-lived-access-tokens

Using short-lived access tokens is a good practice, and when using OAuth 2 this is done by using refresh tokens. If a malicious actor is able to get hold of an access token then rotation means that token might not work by the time they try to use it, or it could at least reduce how long they are able to perform malicious requests.

---

### ❌ owasp:api4:2023-rate-limit

Define proper rate limiting to avoid attackers overloading the API. There are many ways to implement rate-limiting, but most of them involve using HTTP headers, and there are two popular ways to do that:

IETF Draft HTTP RateLimit Headers:. [https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers)/

Customer headers like X-Rate-Limit-Limit (Twitter: [https://developer.twitter.com/en/docs/twitter-api/rate-limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) or X-RateLimit-Limit (GitHub: [https://docs.github.com/en/rest/overview/resources-in-the-rest-api](https://docs.github.com/en/rest/overview/resources-in-the-rest-api))

---

### ❌ owasp:api4:2023-rate-limit-retry-after

Define proper rate limiting to avoid attackers overloading the API. Part of that involves setting a Retry-After header so well meaning consumers are not polling and potentially exacerbating problems.

---

### ❌ owasp:api4:2023-array-limit

Array size should be limited to mitigate resource exhaustion attacks. This can be done using `maxItems`. You should ensure that the subschema in `items` is constrained too.

---

### ❌ owasp:api4:2023-string-limit

String size should be limited to mitigate resource exhaustion attacks. This can be done using `maxLength`, `enum` or `const`.

---

### ❌ owasp:api4:2023-integer-limit

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-limit-legacy

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-format

Integers should be limited to mitigate resource exhaustion attacks. Specifying whether int32 or int64 is expected via `format`.

---

### ❌ owasp:api8:2023-define-cors-origin

Setting up CORS headers will control which websites can make browser-based HTTP requests to your API, using either the wildcard "*" to allow any origin, or "null" to disable any origin. Alternatively you can use "Access-Control-Allow-Origin: https://example.com" to indicate that only requests originating from the specified domain (https://example.com) are allowed to access its resources.

More about CORS here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

---

### ❌ owasp:api8:2023-no-scheme-http

Server interactions must use the http protocol as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use the https or wss schemes instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api8:2023-no-server-http

Server interactions must not use the http:// as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use https:// or wss:// protocols instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api9:2023-inventory-access

Servers are required to use vendor extension x-internal set to true or false to explicitly explain the audience for the API, which will be picked up by most documentation tools.

---

### ❌ owasp:api9:2023-inventory-environment

Make it clear which servers are expected to run as which environment to avoid unexpected problems, exposing test data to the public, or letting bad actors bypass security measures to get to production-like environments.

---

### ⚠️ owasp:api3:2023-no-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api3:2023-no-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api4:2023-rate-limit-responses-429

OWASP API Security recommends defining schemas for all responses, even errors. A HTTP 429 response signals the API client is making too many requests, and will supply information about when to retry so that the client can back off calmly without everything breaking. Defining this response is important not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces. It also ensures your API/framework/gateway actually has rate limiting set up.

---

### ⚠️ owasp:api4:2023-string-restricted

To avoid unexpected values being sent or leaked, strings should have a `format`, RegEx `pattern`, `enum`, or `const`.

---

### ⚠️ owasp:api8:2023-define-error-validation

Carefully define schemas for all the API responses, including either 400, 422 or 4XX responses which describe errors caused by invalid requests.

---

### ⚠️ owasp:api8:2023-define-error-responses-401

OWASP API Security recommends defining schemas for all responses, even errors. The 401 describes what happens when a request is unauthorized, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ⚠️ owasp:api8:2023-define-error-responses-500

OWASP API Security recommends defining schemas for all responses, even errors. The 500 describes what happens when a request fails with an internal server error, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ℹ️ owasp:api7:2023-concerning-url-parameter

Using external resources based on user input for webhooks, file fetching from URLs, custom SSO, URL previews, or redirects can lead to a wide variety of security issues.

Learn more about Server Side Request Forgery [https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/).

---


# WSO2 API Design Guidelines

A guide detailing best practices for creating robust, scalable, and secure APIs, ensuring alignment with industry standards for optimal design.
### ❌ path-casing

Paths must be `kebab-case`, with hyphens separating words.

**Invalid Example**

`userInfo` must be separated with a hyphen.

```json
{
    "/userInfo": {
        "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user-info": {
       "post: }
       ....
}
```

---

### ❌ paths-no-file-extensions

Paths must not include `json` or `xml` file extensions.

**Invalid Example**

The path contains a `.json` extension. 

```json
{
    "/user.json": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ paths-no-http-verbs

Verbs such as `get`, `delete`, and `put` must not be included in paths because this information is conveyed by the HTTP method.

**Invalid Example**

The path contains the verb `get`. 

```json
{
    "/getUsers": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ path-parameters-snake-case

Path parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the path parameter must not contain digits.

**Invalid Example**

The `name` property on line 9 (`userId`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "userId",
            "in": "path"
          }
        ]
      }
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ]
      }
    }
  }
```

---

### ❌ query-parameters-snake-case

Query parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the query parameter must not contain digits.

**Invalid Example**

The `name` property on line 8 (`user-Id`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
   "parameters": [
     {
       "schema": {
         "type": "string"
       },
       "in": "query",
       "name": "user-Id"
     }
   ]
}
```

**Valid Example**

```json
{
    "parameters": [
      {
        "schema": {
          "type": "string"
        },
        "in": "query",
        "name": "user_id"
      }
    ]
 }
```

---

### ⚠️ resource-names-plural

Resource names should generally be plural. 

**Invalid Example**

```json
{
    "paths": {
      "/user": 
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users": 
    }
}
```

---

### ⚠️ paths-avoid-special-characters

Paths should not contain special characters, such as `$` `&` `+` `,` `;` `=` `?` and `@%`.

**Invalid Example**

The path contains an ampersand. 

```json
{
    "/user&info": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ℹ️ server-has-api

Server must have /api

---


# WSO2 Style Guidelines

A set of guidelines focused on enforcing uniformity in API style, including naming conventions, formatting, and documentation to ensure clarity and maintainability across all APIs.
### ❌ operation-operationId-valid-in-url

Operation IDs must not contain characters that are invalid for URLs.

**Invalid Example**

The `operationId` in this example includes a pipe and space, which are invalid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "invalid|operationID"
    }
  }
}
```

**Valid Example**

This `operationId` is valid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "this-must-be-unique"
    }
  }
}
```

---

### ❌ path-declarations-must-exist

Path parameter declarations must not be empty.

**Invalid Example**

`/users/{}`

**Valid Example**

`/users/{userId}`

---

### ❌ paths-no-trailing-slash

Paths must not end with a trailing slash.

`/users` and `/users/` are separate paths. It's considered bad practice for them to differ based only on a trailing slash. It's usually preferred to not have a trailing slash.

**Invalid Example**

The `users` path ends with a slash.

```json
{
  "/users/": {
    "post": {}
  }
}
```

**Valid Example**

```json
{
  "/user": {
    "post": {}
  }
}
```

---

### ❌ server-lowercase

Server URLs must be lowercase. This standard helps meet industry best practices.

**Invalid Example**

The `url` property uses uppercase letters.

```json
{
  "servers": [
    {
      "url": "https://ACME.com/api"
    }
  ]
}
```

**Valid Example**

The `url` property is fully lowercase.

```json
{
  "servers": [
    {
      "url": "https://acme.com/api"
    }
  ]
}
```

---

### ❌ oas2-api-schemes

OpenAPI 2 host `schemes` reflect the transfer protocol of the API. 
Host schemes must be present and an array with one or more of these values: 
`http`, `https`, `ws`, or `wss`.

**Valid Example**

This example shows that host schemes are `http` and `https`.

```json
{
  "schemes": [
    "http",
    "https"
  ]
}
```


---

### ❌ array-items

Schemas with `type: array`, require a sibling `items` field.

**Recommended:** Yes

**Good Example**

```yaml
TheGoodModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
        items: {}
```

**Bad Example**

```yaml
TheBadModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
```

---

### ⚠️ contact-url

The `contact` object should have a valid organization URL. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "url": "https://acme.com",
     ... 
  },
```

---

### ⚠️ contact-email

The `contact` object should have a valid email. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "email": "support.contact@acme.com"
  },
```

---

### ⚠️ info-contact

The `info` object should include a `contact` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "contact": {
      "name": "ACME Corporation",
      "url": "https://acme.com",
      "email": "support.contact@acme.com"
    }
  }
}
```

---

### ⚠️ info-description

The `info` object should have a `description` object.

**Valid Example**

```json
{
  "info": {
     ... ,
     "description": "This describes my API."
  }
}
```

---

### ⚠️ info-license

The `info` object should have a `license` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "license": {
      "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "url": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  }
}
```

---

### ⚠️ license-url

The `license` object should include a valid url.

**Valid Example**

```json
{
  "license": {
    "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "url": "https://creativecommons.org/licenses/by-sa/4.0/"
  }
}
```

---

### ⚠️ no-eval-in-markdown

Markdown descriptions should not contain [`eval()` functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval),
which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. eval()"
  }
}
```

---

### ⚠️ no-script-tags-in-markdown

Markdown descriptions should not contain `script` tags, which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. <script>alert(\"You are Hacked\");</script>"
  }
}
```

---

### ⚠️ openapi-tags-alphabetical

Global tags specified at the root OpenAPI Document level should be in alphabetical order based on the `name` property.

**Invalid Example**

```json
{
  "tags":[
    {
      "name":"Z Global Tag"
    },
    {
      "name":"A Global Tag"
    }
  ]
}
```

**Valid Example**

```json
{
  "tags":[
    {
      "name":"A Global Tag"
    },
    {
      "name":"Z Global Tag"
    }
  ]
}
```

---

### ⚠️ openapi-tags

At least one global tag should be specified at the root OpenAPI Document level.

**Valid Example**

```json
{
  "tags":[
    {
      "name":"Global Tag #1"
    },
    {
      "name":"Global Tag #2"
    }
  ]
}
```

---

### ⚠️ operation-description

Each operation should have a description.

**Valid Example**

```json
{
  "get": {
    "description": "Get a list of users."
  }
}
```

---

### ⚠️ operation-operationId

All operations should have an `operationId`.

**Valid Example**

```json
{
  "get": {
    "summary": "Get users",
    "operationId": "get-users"
  }
}
```

---

### ⚠️ operation-tags

At least one tag should be defined for each operation.

**Valid Example**

```json
{
  "get": {
    "tags": ["Users"]
  }
}
```

---

### ⚠️ contact-name

The `contact` object should have an organization name.

**Valid Example**

```json
{
  "contact": {
    "name": "ACME Corporation"
  }
}
```

---

### ⚠️ path-keys-no-trailing-slash

Path keys should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "/users/": {
  }
}
```

**Valid Example**

```json
{
  "/users": {
  }
}
```

---

### ⚠️ path-not-include-query

Paths should not include `query` string items. Instead, add them as parameters with `in: query`.

**Invalid Example**

```json
{
  "/users/{?id}": {
  }
}
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ⚠️ tag-description

Tags defined at the global level should have a description.

**Valid Example**

```json
{
  "tags": [
    {
      "name": "Users",
      "description": "End-user information"
    }
  ]
}
```

---

### ⚠️ api-servers

A server should be defined at the root document level. This can be localhost, a development server, or a production server.

**Valid OpenAPI V3 Example**

```json
{
  "servers": [
    {
      "url": "https://staging.myprodserver.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://myprodserver.com/v1",
      "description": "Production server"
    }
  ]
}
```

**Valid OpenAPI V2 Example**

```json
{
  "host": "myprodserver.com",
  "basePath": "/v2",
  "schemes": [
    "https"
  ]
}
```

---

### ⚠️ server-trailing-slash

Server URLs should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5/"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```

---

### ⚠️ server-not-example

Server URLs must not direct to example.com. This helps ensure URLs 
are valid before you distribute your API document.

**Invalid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://example.com"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```


---

### ⚠️ parameter-description

All `parameter` objects should have a description.

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "integer"
      },
      ... ,
      ... ,
      "description": "The number of days to include in the response."
    }
  ]
}
```


---

### ⚠️ oas2-anyOf

The `anyOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "anyOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas2-oneOf

The `oneOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "oneOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas3-examples-value-or-externalValue

The `examples` object should include a `value` or `externalValue` field, but cannot include both.

**Invalid Example**

This example includes both a `value` field and an `externalValue` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      },
      "externalValue": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```

**Valid Example**

This example includes only a `value` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```


---

### ⚠️ path-parameters-on-path-only

Path parameters should be defined on the path level instead of the operation level.

**Invalid Example**

The `user_id` path parameter on line 8 should not be included with the `patch` operation.

```json
{      
  "patch": {
    "parameters": [
      {
        "schema": {
          "type": "integer"
        },
        "name": "user_id",
        "in": "path"
      }
    ]
  }
}
```

**Valid Example**

The `user-id` path parameter is correctly located at the path level.

```json
{
  "paths": {
    "/users/{userId}": {
      "parameters": [
        {
          "schema": {
            "type": "integer"
          },
          "name": "user_id",
          "in": "path"
        }
      ]
    }
  }
}
```

---

### ⚠️ paths-no-query-params

Paths should not have query parameters in them. They should be defined separately in the OpenAPI.

**Invalid Example**

```json
{
  "/users/{?id}": {
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ℹ️ operation-singular-tag

Operation should not have more than a single tag.

---


# About API Policies

API policies are units of business logic that you can apply to modify the flow of API invocations. 

You can apply a policy to alter the  `Request`, `Response`, or `Error` flow of an API invocation before it reaches the backend or the client. For example, you can add a policy to the response flow to transform the payload from JSON to XML and add a header to the response. 

## Inbuilt mediation policies

Choreo supports a set of inbuilt mediation policies that can handle common API transformation and mediation tasks. These policies run within a single mediation service, making it straightforward to implement and manage complex mediation logic. The following inbuilt policies are available in Choreo:

- **JSON to XML**: Transforms a JSON payload in a request or response into XML format. This policy is applicable only to JSON payloads in mediation flows. Applying it to a non-JSON payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to XML.
- **XML to JSON**: Converts an XML payload in a request or response into JSON format. This policy is applicable only to XML payloads in mediation flows. Applying it to a non-XML payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to JSON.
- **Remove Query Parameter**: Removes specified query parameters from a request. You can use this policy multiple times to remove different parameters. Attempting to remove a non-existent parameter has no effect. If the parameter exists, it will be removed; otherwise, the request proceeds as usual.
- **Remove Header**: Removes specified headers from a request or response. You can attach this policy multiple times to remove multiple headers. The header name must be static, but you can use placeholders to configure different values for different environments. For example, `${headerName}`.
- **Add Query Parameter**: Adds query parameters to a request. You can attach this policy multiple times to add various parameters. Adding the same parameter multiple times creates an array of values. The parameter name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${fooValue}`.
- **Add Header**: Adds headers to a request or response. If the same header is added multiple times, values are appended rather than overwritten. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`.
- **Set Header**: Sets headers in a request or response, overwriting any existing values. You can attach this policy multiple times to set multiple headers. Each time the same header is set, it replaces the previous value. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`. 
- **Rewrite Resource Path**: Modifies the resource path of an HTTP request by replacing the original path with a new relative path. You can apply this policy multiple times, but only the last instance will take effect. The new path must be static, but you can use placeholders to configure different values for different environments. For example, `${myResourcePath}`.
- **Log Message**: Logs the payload and headers of a request or response. Attaching this policy multiple times results in duplicate log entries. By default, headers and payloads are not logged. To log them, you can enable `Log Headers` and `Log Payload` parameters. To exclude specific headers when logging, you can use the `Excluded Headers` parameter, which takes a comma-separated list of header names. An error will occur if payload logging is enabled but the payload cannot be read.

These inbuilt mediation policies provide flexibility to manage API requests and responses, allowing for custom transformations and logic without requiring custom code.

For details on attaching and managing one or more policies to an API proxy component implementation via the Choreo Console, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

For details on applying advanced settings on mediation policies, see [Apply Advanced Settings on Mediation Policies](../api-policies/apply-advanced-settings-on-mediation-policies.md).


# Apply Advanced Settings on Mediation Policies

Advanced settings for mediation policies are available for proxy components with an attached mediation policy. For details on attaching a mediation policy to a proxy component, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

The approach to applying advanced settings depends on whether the proxy component is deployed or not.

## Mediation policy advanced settings

| **Setting**                     | **Purpose**    | **How to apply**  | **Impact**   |
|---------------------------------|----------------|-------------------|--------------|
| **HTTP version**                | By default, Choreo supports HTTP 1.1. If necessary, you can change to HTTP 1.0 or HTTP 2.0. | Specify the required HTTP version in the **Advanced Settings** field. <br> ![HTTP version setting](../../assets/img/api-management/api-policies/advanced-settings/http-version-setting.png) | The mediation application will use the specified HTTP version when interacting with backend services.  |
| **Hostname verification**       | Choreo enables hostname verification by default when using mTLS. You can disable it if necessary. | Set the `verifyHostname` parameter to `false` in the **Advanced Settings** field. <br> ![Hostname verification setting](../../assets/img/api-management/api-policies/advanced-settings/hostname-verification-setting.png)   | Hostname verification will be skipped during mTLS interactions.                              |
| **Minimum evictable idle time** | Determines how long (in seconds) an outgoing connection remains idle before eviction. The default is 300 seconds. | Set the required idle time in the **Advanced Settings** field. <br> ![Minimum evictable idle time setting](../../assets/img/api-management/api-policies/advanced-settings/minimum-evictable-idle-time-setting.png)          | Idle connections will be closed and evicted after the defined period.                    |
| **Detailed access log**         | By default, logs related to the mediation application are generated and can be viewed as [runtime logs](../../monitoring-and-insights/view-logs.md#runtime-logs). You can disable these logs if necessary.      | Set the `detailedAccessLog` parameter in the **Advanced Settings** field. <br> ![Detailed access log setting](../../assets/img/api-management/api-policies/advanced-settings/detailed-access-log-setting.png)  | Logs related to the mediation application will not be generated.    |

## Configure advanced settings for a proxy component

To configure advanced settings for a proxy component with an attached mediation policy, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to configure advanced settings.
3. In the left navigation menu, click **Deploy**.
4. Depending on the deployment status of the proxy component, follow one of these steps:
   - If the proxy component is not deployed, go to the **Set Up** card and click **Configure & Deploy**. 
   - If the proxy component is already deployed, go to the respective environment card depending on the environment you want to apply advanced settings, and then click the **Environment Variables** icon.
5. In the **Configurations** pane that opens, expand the **Defaultable Configurables** section. 
6. In the **Advanced Settings** field, configure the necessary settings as described in the [Mediation policy advanced settings](#mediation-policy-advanced-settings) section.
7. Click **Save & Deploy**.


# Attach and Manage Policies

You can easily attach one or more policies to an API proxy component implementation via the Choreo Console. If necessary, you can also rearrange or swap the policies you attach.

In Choreo, when you attach a mediation policy to a proxy, the deployment is a two-step process.

1. Deployment initiation: 

     If the component to which you want to attach the mediation policy is new, the system creates and commits a new repository with the mediation service code based on the attached policy. This new service is called the mediation application. 

2. Deploying the API:

     Once the deployment initiation is complete, you can specify configuration values if any, and proceed to deploy. Choreo builds the generated mediation application and pushes the Docker image to the Docker registry. Finally, Choreo deploys the mediation application with the API Proxy.

When a mediation policy is attached to a specific flow, the API invocation undergoes the following behavioral modification:
 
 ![Request/Response flow](../../assets/img/api-management/api-policies/request-response-flow.png)

 - In the request path, the requests that pass through the gateway reach the relevant component, and Choreo executes any attached policies to the resource's request path before sending it to the backend. 

- In the response path, the mediation component receives response messages from the backend, and Choreo executes any mediation policies attached to the `Response` flow or the `Error` flow. Then the response is forwarded to the client.

- If an error occurs during the execution of policies or due to an internal error, Choreo executes the `Error` flow and sends an error response to the client.

## Attach a policy

To attach a policy to the `Request`, `Response`, or `Error` flow of a REST API proxy, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to attach a policy.
3. In the left navigation menu, click **Develop** and then click **Policies**.
4. From the list of resources, expand the resource to which you want to attach the policy. 
5. Click **Attach Mediation Policy** in the respective flow for which you want to attach a policy.
6. In the **Policy List** pane that opens, click on a required policy to view its details.
7. If the attached policy requires parameter configuration, on the policy pane enter the appropriate values and configure the parameters. To make a parameter a configurable variable, input the value in the `${<variableName>}` format. For example, you can use `${name}` as an example.

    ![Configure parameters](../../assets/img/api-management/api-policies/configure-parameters.png)
 
8. To attach the policy, click **Add**.

After attaching an API Policy, it is necessary to deploy the API for the policy to become active within its corresponding flow. 
To deploy the API follow the steps below: 

9. In the left navigation menu, click **Deploy** and then click **Configure & Deploy**. Choreo performs the mediation application generation step and opens the **Configure & Deploy** pane.

10. In the **Configure & Deploy** pane, if you have any configurable variables that require values, specify appropriate values for them.

     ![Save and deploy values](../../assets/img/api-management/api-policies/save-and-deploy.png)

11. Click **Save & Deploy**.

## Refresh mediation policies

Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. These changes include:

 - Addition, deletion, or modification of API resources.
 - Attachment, removal, or editing of API mediation policies.
 - Endpoint modifications via the **Develop** page.
 - Initial configuration or removal of backend endpoints or mutual TLS certificates.

If none of the above changes occur during deployment, Choreo skips the code generation and build process of the mediation application.

!!! info
    - If you want to enforce the code generation and build process of the mediation application in instances where the specified changes do not take place, you must turn on the **Refresh Mediation Policies** toggle when you configure and deploy the component. 
    - It is useful to enable **Refresh Mediation Policies** when you want to incorporate the latest Ballerina patches for your generated mediation application. However, this can result in longer deployment times.

## Implement an API policy

Choreo allows you to implement an API policy as a Ballerina project and attach it to an API proxy component. 

!!! info
    Supported Ballerina version: 2201.5.5 

To implement a policy, follow the steps given below: 

### Prerequisites

1. Set up [ Ballerina 2201.5.5](https://ballerina.io/downloads/swan-lake-release-notes/swan-lake-2201.5.5).
2. Open the `~/.ballerina/settings.toml` file and ensure you have configured an access token to Ballerina Central. If you have not configured an access token, follow the steps given below to configure one: 
    1. Generate a token via [https://central.ballerina.io/dashboard?tab=token](https://central.ballerina.io/dashboard?tab=token).
    2. Download the generated `Settings.toml` file and copy it to your local `~/.ballerina` directory.
    
Alternatively, you can set the access token via the `BALLERINA_CENTRAL_ACCESS_TOKEN` environment variable.

``` 
export BALLERINA_CENTRAL_ACCESS_TOKEN=<access-token> 
```

### Step 1: Initialize a Ballerina project

Choreo provides a template to initialize a mediation policy project with all the required configurations. The mediation policy project will be created as a Ballerina project.

To create a Ballerina project for the mediation policy using `mediation.template` as the project template, issue the following command:  
   
**Format:**

```
    bal new -t choreo/mediation.template:1.0.0 <policy-name> 
```
    
**Example:**

```
    bal new -t choreo/mediation.template:1.0.0 validateHeader 
```
 The Ballerina project that is created should have the following content: 

![Ballerina project](../../assets/img/api-management/api-policies/ballerina-project.png)

Depending on your requirement, you can modify the `Ballerina.toml` and the `Package.md` files of the generated project. For example, you can update the org, package, package version, API documentation content, keywords, etc.

!!! note
    To successfully publish to Ballerina Central, make sure you update the `org` value to your organization name.

```
     [package]
        org = "starkindustries"
        name = "validateHeader"
        version = "1.0.0"
        export = ["validateHeader"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
```

### Step 2: Implement the policy

In this step, you will implement the policy. 

Let's assume you want to implement a policy to validate an incoming header in the request and the response. 

- **Request path**: If the request header is not present or if the validation fails, you want to log an error and return a `403 Bad Request` response to the client.
- **Response path**: You want to log a message to indicate whether the request is valid or not.

To implement the policy, open the `policy.bal` file in the Ballerina project and update the generated policy stubs(i.e., request, response, or fault) appropriately. 

The following sections walk you through sample implementations for the **Request** and **Response** stubs:

#### Request flow

The following is a sample implementation for the request flow:
 
```ballerina
@mediation:RequestFlow
public function validateRequestHeader(mediation:Context ctx, http:Request req, string headerName, string headerValue) returns http:Response|false|error|() {
   string|http:HeaderNotFoundError header = req.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return generateResponse(message, http:STATUS_BAD_REQUEST);
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return generateResponse(validationFailedMessage, http:STATUS_BAD_REQUEST);
    }
    log:printInfo("Header validation successful");
    return ();
};
    
function generateResponse(string message, int statusCode) returns http:Response {
    http:Response response = new();
    response.setTextPayload(message); 
    response.statusCode = statusCode;
    return response;
}

```

#### Response flow

The following is a sample implementation for the response flow:

```ballerina
@mediation:ResponseFlow
public function validateResponseHeader(mediation:Context ctx, http:Request req, http:Response res, string headerName, string headerValue) returns http:Response|false|error|() { 
   string|http:HeaderNotFoundError header = res.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return ();
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return ();
   }
   return ();
}

```

#### Fault flow

In this guide, you are not going to make any changes to the `Fault` flow. Therefore, you can remove the `Fault` flow stub from the `policy.bal` file.

!!! note 
    The  **@mediation:RequestFlow**, **@mediation:ResponseFlow**, and **@mediation:FaultFlow** annotations are bound with the keywords in the `Ballerina.toml`. Therefore, the changes you make to the policy stubs should reflect in the `Ballerina.toml` file. For example, if the policy is applicable only on the request and response paths, you can remove the  **@mediation:FaultFlow** annotation from the policy. Then, you **MUST** also remove the **choreo-apim-mediation-fault-flow** keyword from the generated `Ballerina.toml` file. If you do not do so, the Ballerina compiler will show an error at compile time.

#### Publish as a private custom policy
 
 Choreo supports publishing a policy as a private custom policy. Publishing a policy as a private custom policy makes the policy inaccessible outside of the organization. To publish a policy as a private custom policy, change the visibility to `private` prior to pushing the package to Ballerina Central as follows:

 1. Open the `Ballerina.toml` file of your policy. 
 2. Set the visibility to **private** by adding the configuration `visibility="private"`. For example:

     ```
     [package]
        org = "orgName"
        name = "packageName"
        version = "1.0.2"
        export = ["packageName"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
        visibility = "private"
     ```

 3. Package and publish your policy to Ballerina Central.     

#### Best practices 

When implementing a policy, it is essential to follow best practices to ensure efficiency and maintainability. Here are some recommended best practices to follow:

- Organize the source code within the default module of the package. Do not add any additional modules.
- A policy implementation can contain any combination of flows. A generated project contains stubs for all three flows: `Request`, `Response`, and `Fault`. You can remove any stub that you do not require. For example, when you create a policy that re-writes the resource paths, you can remove the `Response` and `fault` stubs. 
- The HTTP request/response objects and context record parameters gets passed as references to the policy functions. Therefore, the changes you make to these values persist throughout the policy execution and are propagated to subsequent policies. This behavior allows the request and response objects to accumulate transformations applied by attached policies.
- Familiarize yourself with the different return types of policy flows. The following return types are unmodifiable:
    - **http:Response** - Returns an HTTP response when you terminate the mediation flow prematurely. For example,  in the in-flow sequence, the mediation sequence terminates before calling the backend. The mediation policy then sends an HTTP response to the client.
    - **false** - Returns `false` if you want to terminate the mediation sequence with a predefined response (on the Choreo side).
    - **error** - Returns an error if you want to terminate the mediation flow and transfer control to the fault flow. The fault flow would then construct an error response and send it to the client.
    - **()** - Returns () to signal the successful completion of the policy. Once the proxy has completed executing the policy, it starts to execute the next policy in the sequence.

### Step 3: Publish the policy

Once you implement a policy, you must publish it to Ballerina Central. 

When you attach a policy and deploy an API, Choreo pulls the necessary packages from Ballerina Central and bundles them into the mediation application under the hood. Therefore to use policies in your APIs, you must publish them as public packages. 

To publish the policy, follow the steps given below:

1. To package the policy before you publish it to Ballerina Central, issue the following command:
    ``` 
        bal pack 
    ```
2. To publish the package to Ballerina Central, issue the following command:

    ``` 
        bal push 
    ```

Once you publish the package, it will appear as follows in the policy list:

![Published policy](../../assets/img/api-management/api-policies/published-policy.png)

### Write unit tests

You can write unit tests to test policy functions in a manner similar to how you write unit tests for a regular [Ballerina function](https://ballerina.io/learn/test-ballerina-code/test-a-simple-function/). 

The following is a sample unit test for the `validateRequestHeader` function:

```
import ballerina/http;
import choreo/mediation;
import ballerina/test;


@test:Config {}
public function testRequestHeaderValidationFailure() {
  http:Request req = new;
  http:Response|false|error|() result = validateRequestHeader(createContext("get", "/test"), req, "testHeader", "test");


  if !(result is http:Response) {
    test:assertFail("Expected http:Response, found " + (typeof result).toString());
  }


  test:assertEquals(result.statusCode, http:STATUS_BAD_REQUEST, "Status code mismatch");
}


function createContext(string httpMethod, string resPath) returns mediation:Context {
   mediation:ResourcePath originalPath = checkpanic mediation:createImmutableResourcePath(resPath);
   mediation:Context originalCtx =
               mediation:createImmutableMediationContext(httpMethod, originalPath.pathSegments(), {}, {});
   mediation:ResourcePath mutableResPath = checkpanic mediation:createMutableResourcePath(resPath);
   return mediation:createMutableMediationContext(originalCtx, mutableResPath.pathSegments(), {}, {});
}

```

The policy function modifies the same request/response/context instance that you pass to it. You can check the request/response/context instance after calling the policy function to verify changes.

### Glossary

Here are some of the common terms used when working with policies in Choreo:

#### mediation:Context

The mediation context is used to pass parameters between policies. It is created per request and you can access it in any of the flows. For example, if a correlation ID needs to be set to the request, you can set it in the context of the request flow and access it in the response or fault flow. 

The mediation context can include the following functions:

```
# Retrieves the value for the specified key.   
public function get(string name) returns anydata;


# Stores the provided key-value pair. If a mapping exists for the key, the value is overwritten.
public function put(string name, anydata value);


# Removes the entry mapped by the specified key and returns the removed value.
public function remove(string name) returns anydata;


# Retrieves the value for the specified key. If there is no mapping for the key, return the specified
public function getOrDefault(string name, anydata default) returns anydata;


# Checks whether a mapping exists for the specified key.
public function hasKey(string name) returns boolean;


# Returns the `mediation:Context` instance which captured the initial contextual information of the resource,
# before the mediation flow was invoked. Calling this on an original `mediation:Context` object will return itself.
public function originalContext() returns Context;


# The HTTP method of the resource method
public function httpMethod() returns string;


# Retrieves an instance of `mediation:ResourcePath` which is an API for contextual information on the resource path
# of this resource. It also contains methods for modifying the resource path as the user sees fit. This resource
# path is the same path used by the mediation service for deriving the backend endpoint's resource to invoke.
# Therefore, the default behavior of the mediation service is to invoke a resource in the backend endpoint which
# has the same relative resource path as the corresponding mediation service resource.
public function resourcePath() returns ResourcePath;


# Sets the given `mediation:ResourcePath` instance as the resource path of this context.
public function setResourcePath(ResourcePath path);


# Adds a mapping between a path param name and a resolved value for it. There need not be a path parameter in the
# resource path by the name specified in `name` for one to use this method. On its own, the path param values have
# no bearing on the resource path.
public function addPathParamValue(string name, PathParamValue value);


# Returns the collection of resolved values for the path parameters in this particular context, mapped
# by the parameter name.
public function resolvedPathParams() returns map<PathParamValue> & readonly;


# Removes the resolved path parameter value which maps to the specified name.
public function removePathParamValue(string name);


# Adds a query parameter to the request to be sent to the backend. If there is already a query parameter by
# with the same name, the new value will be appended to it, making it an array.
public function addQueryParam(string name, string value);


# Removes the specified query parameter from the request. If the value of the parameter is an array, the whole
# array will be removed.
public function removeQueryParam(string name);


# Retrieves a map of all the query parameters in the current request context. The returned map is a read-only snapshot
# of the map of query parameters in the context at the time this method was called.
public function queryParams() returns map<string[]> & readonly;
```

### Keywords

The `Ballerina.toml` file needs to include the following keywords for the mediation policies to work:

- **choreo-apim-mediation-policy**: This keyword is a mandatory keyword that is required to identify that the package is a mediation policy type.
- **choreo-apim-mediation-request-flow**: Specifies whether the policy applies to the request flow.
- **choreo-apim-mediation-response-flow**: Specifies whether the policy applies to the response flow.
- **choreo-apim-mediation-fault-flow**: Specifies whether the policy is applicable for the fault flow.

#### Policy name and description

The `Package.md` file contains information about the policy. Choreo uses this information to render the policy configuring UI. This file is written in Markdown format and should be structured as follows.

**Format:**

```
# <policy-name>


## Overview


<policy description>

```

**Example:**

```
# ValidateHeader


## Overview


This policy validates the request and response headers with the configured values.

```

#### Policy versioning

When it comes to policy versioning in Choreo or mediation dependencies, it is important to consider the major version changes in the Ballerina language. For example, transitioning from update 1 to update 2 requires a major version increment, which can introduce significant incompatibilities.

Therefore, to ensure compatibility, the recommended approach is to version the policy package in a manner that the major version gets upgraded when the Choreo/mediation dependency version is upgraded to a major version.  


# Assign Subscription Plans to APIs

API subscription plans allow API publishers to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security.

Choreo allows users with the administrator role to create, update, and delete subscription plans at the organization level. For instructions on creating subscription plans, see [Create API Subscription Plans](../../administer/create-api-subscription-plans.md).

Once created, Choreo allows API publishers to assign subscription plans to APIs, providing different levels of access based on user needs.

To assign subscription plans to an API, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to assign subscription plans.
3. In the left navigation menu, click **Manage** and then click **Subscription Plans**. This displays the subscription plans available for the component.
4. Enable the **Subscription Plan Status** toggle corresponding to the subscription plans you want to assign to the API.

    ![Enable toggle](../../assets/img/api-management/manage-api-traffic/enable-toggle.png)

5. Click **Save**.

When an API has subscription plans assigned to it, API consumers can select the plan that best fits their requirements during the subscription process. For details, see [Subscribe to an API with a Subscription Plan](./subscribe-to-an-api-with-a-subscription-plan.md)


# Subscribe to an API with a Subscription Plan

If an API has subscription plans assigned to it, API consumers can select the subscription plan that best fits their requirements at the time of subscribing to the API.

To subscribe to an API with a subscription plan, follow the steps given below:

1. Sign in to the [Choreo Developer Portal](https://devportal.choreo.dev).
2. In the Developer Portal header, click **Applications**.
3. On the **My Applications** page, click on the application you want to use to subscribe to an API.
4. In the left navigation menu, click **Subscriptions**. 
5. In the **Subscription Management** pane that opens, click **+ Add APIs**.
6. In the **Add APIs** pane that opens, select the API, API version, and subscription plan with which you want to subscribe to the API.
7. If the selected subscription plan requires administrator or API publisher approval to become active, click Request Subscription. Otherwise, click Add Subscription. If the selected subscription plan requires approval, your subscription will be shown as "Pending" until it is approved by an organization admin or the API publisher.

    !!! Note
        If the subscription plan requires administrator or API publisher approval to become active, the subscription status will be set to Pending Creation until it is reviewed and approved.

    ![Add subscription](../../assets/img/api-management/manage-api-traffic/add-subscription.png)

To verify that the subscription plan works as expected, follow the steps given below:

1. In the Developer Portal header, click **APIs**.
2. Search for the API you subscribed to and click **Try Out**.
3. Invoke the API until you exceed the request limit set in the subscription plan. You will see that the API throttles further requests once the limit is reached.

    ![Throttle response](../../assets/img/api-management/manage-api-traffic/throttle-response.png)




# API Rate Limiting

API rate limiting is a technique that allows you to control the rate of requests made to an API. Rate limiting helps 
prevent system overload and enhances API performance. When you limit the number of requests that can be made in a 
specific time frame, you can ensure that your API is available and responsive to all users while protecting it from 
malicious attacks.

This page walks you through the steps to enable rate limiting for your APIs via Choreo and also provides information on 
the rate-limiting options supported by Choreo.

## Enable rate limiting for an API

To enable rate limiting for an API, follow the steps given below: 

!!! note
     You can apply rate-limiting settings separately for each environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). 
2. In the **Component Listing** pane, click on the component for which you want to apply rate limiting.
3. In the left navigation menu, click **Deploy**.
4. Go to the required environment card and click the view icon corresponding to the endpoint for which you want to apply rate limiting. 

    !!! info 
         If you are applying rate limiting for an API Proxy component, go to the required environment card, click the setting icon corresponding to **API Configuration**, and proceed to step 6.

5. In the **Endpoint Details** pane that opens, click the settings icon.
6. In the **Manage** section, click **Rate Limiting** to expand it.
7. Select a **Rate Limiting Level** depending on your requirement and click **Apply**.

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

By default, the APIs published in Choreo are visible to anyone who visits the Choreo Developer Portal. By default, Choreo sets the visibility of the API to `Public`. However, developers can control the visibility of their APIs by changing the default option to `Private` or `Restricted`. 

Visibility settings control users from viewing and modifying APIs. API visibility can be one of the following options:

 - **Public** : The API is **visible to all** in the developer portal.

 - **Private** : The API is visible to the **users who only sign in to the Developer Portal**.

 - **Restricted**: The API is **visible to only the user that has the roles that you specify**. This option helps developers to enforce fine-grained access control to the API.

## Change API visibility

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the REST API (Service) for which you want to control API visibility. 
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, select the required visibility setting from the **Visibility** list. 

    !!! note "Enable fine-grained role-based access control to the API"
         1. To enable fine-grained role-based access control to an API in the Developer Portal, select `Restricted` from the **API visibility** list. Once selected, you will see the roles available in your organization in the **Visible Roles** list. 
         2. Select any combination of roles. Only the users with the given roles can access the APIs through the Dev Portal. 
         3. Alternatively, You can create a new role and assign it to an API by following the steps below: 
             1. Click **+ Create New Role** in the list.
             2. Add the role name and description. 
             3. Click **Next**.
             4. Assign the relevant permissions to the new role.
             5. Click **Create**.
             6. Select the newly created role from the **Visible Roles** list.

6. Click **Save**.


# Documents

When an API consumer signs in to the Choreo Developer Portal to browse APIs, it is not sufficient to just have an API thumbnail along with the name and version of the API. An API consumer would expect to see more details about the API, such as the following:

 - A brief description of the API.
 - How to invoke the API.
 - The limitations/restrictions of the API.
 - Version history.

To provide such information that improves the overall visibility of the API, an API developer can add such documentation to an API before publishing it to the Developer Portal.

## Add documents to an API

To add documentation for an API, follow the steps given below.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).

2. In the **Component Listing** pane, click on the component for which you want to add documents. 

3. In the left navigation menu, click **Manage** and then click **Documents**.

4. Specify a title for the document and provide the content in markdown syntax. 
   
5. Click **Add** to save the document.

Depending on the information you need to add to the API, you can add one or more documents.

You can also edit existing documents and delete documents if necessary.


# Lifecycle Management

API lifecycle management is an important aspect of API management. The API lifecycle consists of various states that an API passes through, from creation to retirement. In Choreo, there are six distinct lifecycle states: created, pre-released, published, blocked, deprecated, and retired.

By leveraging the various lifecycle states, API managers can optimize the development process and ensure that subscribers have access to the latest and most reliable APIs.

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

To change the lifecycle state of an API via the Choreo Console, follow the instructions given below:

!!! tip      
     You must have publishing privileges to manage the lifecycle states of a component.

1. Sign in to the Choreo Console.
2. In the **Component Listing** pane, click on the component for which you want to manage the lifecycle.
3. In the left navigation menu, click **Manage**, and then click **Lifecycle**.
4. In the **Lifecycle Management** pane, you will see the lifecycle state transition diagram indicating the current lifecycle state of the component. Just above the lifecycle state transition diagram, The possible lifecycle states you can apply to the component are displayed just above the lifecycle state transition diagram. Click on a required lifecycle state to apply it to the component. For example, if a component is in the **Created** state, you can click either **Pre-release** or **Publish**.


# Rename API Display Name

Choreo allows you to make one or more endpoints accessible through its service and integration components. These endpoints are published as individual APIs in Choreo, accessible via the Choreo Developer Portal. By default, Choreo assigns an API name by combining the component name and the endpoint name, resulting in the following format: `<component name>-<endpoint name>`. For example, if you create a component named `Ballerina Reading List,` the API is displayed as `Ballerina Reading List - GraphQL Reading List 591.`

Choreo provides you with the flexibility to personalize the display name of the API, enhancing its user-friendliness and readability. Once you modify the API display name within the Choreo Console, Choreo applies the change immediately. From there onwards, Choreo displays the published API by this name in the Choreo Developer Portal.

Follow the steps below to rename the API display name:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. In the **Component Listing** pane, click on the component for which you want to rename the API display name. This opens the **Overview** page of the component.
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, specify an appropriate API display name in the **Name** field.
6. Click **Save**.

Now, you can view the updated API display name in the Choreo Developer Portal.


# OWASP Top 10

A set of rules enforcing OWASP security guidelines to prevent common vulnerabilities and ensure secure coding practices.
### ❌ owasp:api1:2023-no-numeric-ids

Use random IDs that cannot be guessed. UUIDs are preferred but any other random string will do.

---

### ❌ owasp:api2:2023-no-http-basic

Basic authentication credentials transported over network are more susceptible to interception than other forms of authentication, and as they are not encrypted it means passwords and tokens are more easily leaked.

---

### ❌ owasp:api2:2023-no-api-keys-in-url

API Keys are passed in headers, cookies, or query parameters to access APIs. Those keys can be eavesdropped, especially when they are passed in the URL, as logging or history tools will keep track of them and potentially expose them.

---

### ❌ owasp:api2:2023-no-credentials-in-url

URL parameters MUST NOT contain credentials such as API key, password, or secret.

---

### ❌ owasp:api2:2023-auth-insecure-schemes

There are many [HTTP authorization schemes](https://www.iana.org/assignments/http-authschemes/) but some of them are now considered insecure, such as negotiating authentication using specifications like NTLM or OAuth v1.

---

### ❌ owasp:api2:2023-jwt-best-practices

JSON Web Tokens RFC7519 is a compact, URL-safe, means of representing claims to be transferred between two parties. JWT can be enclosed in encrypted or signed tokens like JWS and JWE.

The [JOSE IANA registry](https://www.iana.org/assignments/jose/jose.xhtml) provides algorithms information.

RFC8725 describes common pitfalls in the JWx specifications and in
their implementations, such as:
- the ability to ignore algorithms, eg. `{"alg": "none"}`;
- using insecure algorithms like `RSASSA-PKCS1-v1_5` eg. `{"alg": "RS256"}`.
An API using JWT should explicit in the `description`
that the implementation conforms to RFC8725.
```
components:
  securitySchemes:
    JWTBearer:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        A bearer token in the format of a JWS and conformato
        to the specifications included in RFC8725.
```

---

### ❌ owasp:api2:2023-short-lived-access-tokens

Using short-lived access tokens is a good practice, and when using OAuth 2 this is done by using refresh tokens. If a malicious actor is able to get hold of an access token then rotation means that token might not work by the time they try to use it, or it could at least reduce how long they are able to perform malicious requests.

---

### ❌ owasp:api4:2023-rate-limit

Define proper rate limiting to avoid attackers overloading the API. There are many ways to implement rate-limiting, but most of them involve using HTTP headers, and there are two popular ways to do that:

IETF Draft HTTP RateLimit Headers:. [https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers)/

Customer headers like X-Rate-Limit-Limit (Twitter: [https://developer.twitter.com/en/docs/twitter-api/rate-limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) or X-RateLimit-Limit (GitHub: [https://docs.github.com/en/rest/overview/resources-in-the-rest-api](https://docs.github.com/en/rest/overview/resources-in-the-rest-api))

---

### ❌ owasp:api4:2023-rate-limit-retry-after

Define proper rate limiting to avoid attackers overloading the API. Part of that involves setting a Retry-After header so well meaning consumers are not polling and potentially exacerbating problems.

---

### ❌ owasp:api4:2023-array-limit

Array size should be limited to mitigate resource exhaustion attacks. This can be done using `maxItems`. You should ensure that the subschema in `items` is constrained too.

---

### ❌ owasp:api4:2023-string-limit

String size should be limited to mitigate resource exhaustion attacks. This can be done using `maxLength`, `enum` or `const`.

---

### ❌ owasp:api4:2023-integer-limit

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-limit-legacy

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-format

Integers should be limited to mitigate resource exhaustion attacks. Specifying whether int32 or int64 is expected via `format`.

---

### ❌ owasp:api8:2023-define-cors-origin

Setting up CORS headers will control which websites can make browser-based HTTP requests to your API, using either the wildcard "*" to allow any origin, or "null" to disable any origin. Alternatively you can use "Access-Control-Allow-Origin: https://example.com" to indicate that only requests originating from the specified domain (https://example.com) are allowed to access its resources.

More about CORS here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

---

### ❌ owasp:api8:2023-no-scheme-http

Server interactions must use the http protocol as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use the https or wss schemes instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api8:2023-no-server-http

Server interactions must not use the http:// as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use https:// or wss:// protocols instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api9:2023-inventory-access

Servers are required to use vendor extension x-internal set to true or false to explicitly explain the audience for the API, which will be picked up by most documentation tools.

---

### ❌ owasp:api9:2023-inventory-environment

Make it clear which servers are expected to run as which environment to avoid unexpected problems, exposing test data to the public, or letting bad actors bypass security measures to get to production-like environments.

---

### ⚠️ owasp:api3:2023-no-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api3:2023-no-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api4:2023-rate-limit-responses-429

OWASP API Security recommends defining schemas for all responses, even errors. A HTTP 429 response signals the API client is making too many requests, and will supply information about when to retry so that the client can back off calmly without everything breaking. Defining this response is important not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces. It also ensures your API/framework/gateway actually has rate limiting set up.

---

### ⚠️ owasp:api4:2023-string-restricted

To avoid unexpected values being sent or leaked, strings should have a `format`, RegEx `pattern`, `enum`, or `const`.

---

### ⚠️ owasp:api8:2023-define-error-validation

Carefully define schemas for all the API responses, including either 400, 422 or 4XX responses which describe errors caused by invalid requests.

---

### ⚠️ owasp:api8:2023-define-error-responses-401

OWASP API Security recommends defining schemas for all responses, even errors. The 401 describes what happens when a request is unauthorized, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ⚠️ owasp:api8:2023-define-error-responses-500

OWASP API Security recommends defining schemas for all responses, even errors. The 500 describes what happens when a request fails with an internal server error, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ℹ️ owasp:api7:2023-concerning-url-parameter

Using external resources based on user input for webhooks, file fetching from URLs, custom SSO, URL previews, or redirects can lead to a wide variety of security issues.

Learn more about Server Side Request Forgery [https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/).

---


# WSO2 API Design Guidelines

A guide detailing best practices for creating robust, scalable, and secure APIs, ensuring alignment with industry standards for optimal design.
### ❌ path-casing

Paths must be `kebab-case`, with hyphens separating words.

**Invalid Example**

`userInfo` must be separated with a hyphen.

```json
{
    "/userInfo": {
        "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user-info": {
       "post: }
       ....
}
```

---

### ❌ paths-no-file-extensions

Paths must not include `json` or `xml` file extensions.

**Invalid Example**

The path contains a `.json` extension. 

```json
{
    "/user.json": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ paths-no-http-verbs

Verbs such as `get`, `delete`, and `put` must not be included in paths because this information is conveyed by the HTTP method.

**Invalid Example**

The path contains the verb `get`. 

```json
{
    "/getUsers": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ path-parameters-snake-case

Path parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the path parameter must not contain digits.

**Invalid Example**

The `name` property on line 9 (`userId`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "userId",
            "in": "path"
          }
        ]
      }
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ]
      }
    }
  }
```

---

### ❌ query-parameters-snake-case

Query parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the query parameter must not contain digits.

**Invalid Example**

The `name` property on line 8 (`user-Id`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
   "parameters": [
     {
       "schema": {
         "type": "string"
       },
       "in": "query",
       "name": "user-Id"
     }
   ]
}
```

**Valid Example**

```json
{
    "parameters": [
      {
        "schema": {
          "type": "string"
        },
        "in": "query",
        "name": "user_id"
      }
    ]
 }
```

---

### ⚠️ resource-names-plural

Resource names should generally be plural. 

**Invalid Example**

```json
{
    "paths": {
      "/user": 
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users": 
    }
}
```

---

### ⚠️ paths-avoid-special-characters

Paths should not contain special characters, such as `$` `&` `+` `,` `;` `=` `?` and `@%`.

**Invalid Example**

The path contains an ampersand. 

```json
{
    "/user&info": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ℹ️ server-has-api

Server must have /api

---


# WSO2 Style Guidelines

A set of guidelines focused on enforcing uniformity in API style, including naming conventions, formatting, and documentation to ensure clarity and maintainability across all APIs.
### ❌ operation-operationId-valid-in-url

Operation IDs must not contain characters that are invalid for URLs.

**Invalid Example**

The `operationId` in this example includes a pipe and space, which are invalid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "invalid|operationID"
    }
  }
}
```

**Valid Example**

This `operationId` is valid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "this-must-be-unique"
    }
  }
}
```

---

### ❌ path-declarations-must-exist

Path parameter declarations must not be empty.

**Invalid Example**

`/users/{}`

**Valid Example**

`/users/{userId}`

---

### ❌ paths-no-trailing-slash

Paths must not end with a trailing slash.

`/users` and `/users/` are separate paths. It's considered bad practice for them to differ based only on a trailing slash. It's usually preferred to not have a trailing slash.

**Invalid Example**

The `users` path ends with a slash.

```json
{
  "/users/": {
    "post": {}
  }
}
```

**Valid Example**

```json
{
  "/user": {
    "post": {}
  }
}
```

---

### ❌ server-lowercase

Server URLs must be lowercase. This standard helps meet industry best practices.

**Invalid Example**

The `url` property uses uppercase letters.

```json
{
  "servers": [
    {
      "url": "https://ACME.com/api"
    }
  ]
}
```

**Valid Example**

The `url` property is fully lowercase.

```json
{
  "servers": [
    {
      "url": "https://acme.com/api"
    }
  ]
}
```

---

### ❌ oas2-api-schemes

OpenAPI 2 host `schemes` reflect the transfer protocol of the API. 
Host schemes must be present and an array with one or more of these values: 
`http`, `https`, `ws`, or `wss`.

**Valid Example**

This example shows that host schemes are `http` and `https`.

```json
{
  "schemes": [
    "http",
    "https"
  ]
}
```


---

### ❌ array-items

Schemas with `type: array`, require a sibling `items` field.

**Recommended:** Yes

**Good Example**

```yaml
TheGoodModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
        items: {}
```

**Bad Example**

```yaml
TheBadModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
```

---

### ⚠️ contact-url

The `contact` object should have a valid organization URL. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "url": "https://acme.com",
     ... 
  },
```

---

### ⚠️ contact-email

The `contact` object should have a valid email. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "email": "support.contact@acme.com"
  },
```

---

### ⚠️ info-contact

The `info` object should include a `contact` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "contact": {
      "name": "ACME Corporation",
      "url": "https://acme.com",
      "email": "support.contact@acme.com"
    }
  }
}
```

---

### ⚠️ info-description

The `info` object should have a `description` object.

**Valid Example**

```json
{
  "info": {
     ... ,
     "description": "This describes my API."
  }
}
```

---

### ⚠️ info-license

The `info` object should have a `license` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "license": {
      "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "url": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  }
}
```

---

### ⚠️ license-url

The `license` object should include a valid url.

**Valid Example**

```json
{
  "license": {
    "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "url": "https://creativecommons.org/licenses/by-sa/4.0/"
  }
}
```

---

### ⚠️ no-eval-in-markdown

Markdown descriptions should not contain [`eval()` functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval),
which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. eval()"
  }
}
```

---

### ⚠️ no-script-tags-in-markdown

Markdown descriptions should not contain `script` tags, which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. <script>alert(\"You are Hacked\");</script>"
  }
}
```

---

### ⚠️ openapi-tags-alphabetical

Global tags specified at the root OpenAPI Document level should be in alphabetical order based on the `name` property.

**Invalid Example**

```json
{
  "tags":[
    {
      "name":"Z Global Tag"
    },
    {
      "name":"A Global Tag"
    }
  ]
}
```

**Valid Example**

```json
{
  "tags":[
    {
      "name":"A Global Tag"
    },
    {
      "name":"Z Global Tag"
    }
  ]
}
```

---

### ⚠️ openapi-tags

At least one global tag should be specified at the root OpenAPI Document level.

**Valid Example**

```json
{
  "tags":[
    {
      "name":"Global Tag #1"
    },
    {
      "name":"Global Tag #2"
    }
  ]
}
```

---

### ⚠️ operation-description

Each operation should have a description.

**Valid Example**

```json
{
  "get": {
    "description": "Get a list of users."
  }
}
```

---

### ⚠️ operation-operationId

All operations should have an `operationId`.

**Valid Example**

```json
{
  "get": {
    "summary": "Get users",
    "operationId": "get-users"
  }
}
```

---

### ⚠️ operation-tags

At least one tag should be defined for each operation.

**Valid Example**

```json
{
  "get": {
    "tags": ["Users"]
  }
}
```

---

### ⚠️ contact-name

The `contact` object should have an organization name.

**Valid Example**

```json
{
  "contact": {
    "name": "ACME Corporation"
  }
}
```

---

### ⚠️ path-keys-no-trailing-slash

Path keys should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "/users/": {
  }
}
```

**Valid Example**

```json
{
  "/users": {
  }
}
```

---

### ⚠️ path-not-include-query

Paths should not include `query` string items. Instead, add them as parameters with `in: query`.

**Invalid Example**

```json
{
  "/users/{?id}": {
  }
}
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ⚠️ tag-description

Tags defined at the global level should have a description.

**Valid Example**

```json
{
  "tags": [
    {
      "name": "Users",
      "description": "End-user information"
    }
  ]
}
```

---

### ⚠️ api-servers

A server should be defined at the root document level. This can be localhost, a development server, or a production server.

**Valid OpenAPI V3 Example**

```json
{
  "servers": [
    {
      "url": "https://staging.myprodserver.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://myprodserver.com/v1",
      "description": "Production server"
    }
  ]
}
```

**Valid OpenAPI V2 Example**

```json
{
  "host": "myprodserver.com",
  "basePath": "/v2",
  "schemes": [
    "https"
  ]
}
```

---

### ⚠️ server-trailing-slash

Server URLs should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5/"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```

---

### ⚠️ server-not-example

Server URLs must not direct to example.com. This helps ensure URLs 
are valid before you distribute your API document.

**Invalid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://example.com"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```


---

### ⚠️ parameter-description

All `parameter` objects should have a description.

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "integer"
      },
      ... ,
      ... ,
      "description": "The number of days to include in the response."
    }
  ]
}
```


---

### ⚠️ oas2-anyOf

The `anyOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "anyOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas2-oneOf

The `oneOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "oneOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas3-examples-value-or-externalValue

The `examples` object should include a `value` or `externalValue` field, but cannot include both.

**Invalid Example**

This example includes both a `value` field and an `externalValue` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      },
      "externalValue": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```

**Valid Example**

This example includes only a `value` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```


---

### ⚠️ path-parameters-on-path-only

Path parameters should be defined on the path level instead of the operation level.

**Invalid Example**

The `user_id` path parameter on line 8 should not be included with the `patch` operation.

```json
{      
  "patch": {
    "parameters": [
      {
        "schema": {
          "type": "integer"
        },
        "name": "user_id",
        "in": "path"
      }
    ]
  }
}
```

**Valid Example**

The `user-id` path parameter is correctly located at the path level.

```json
{
  "paths": {
    "/users/{userId}": {
      "parameters": [
        {
          "schema": {
            "type": "integer"
          },
          "name": "user_id",
          "in": "path"
        }
      ]
    }
  }
}
```

---

### ⚠️ paths-no-query-params

Paths should not have query parameters in them. They should be defined separately in the OpenAPI.

**Invalid Example**

```json
{
  "/users/{?id}": {
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ℹ️ operation-singular-tag

Operation should not have more than a single tag.

---


# About API Policies

API policies are units of business logic that you can apply to modify the flow of API invocations. 

You can apply a policy to alter the  `Request`, `Response`, or `Error` flow of an API invocation before it reaches the backend or the client. For example, you can add a policy to the response flow to transform the payload from JSON to XML and add a header to the response. 

## Inbuilt mediation policies

Choreo supports a set of inbuilt mediation policies that can handle common API transformation and mediation tasks. These policies run within a single mediation service, making it straightforward to implement and manage complex mediation logic. The following inbuilt policies are available in Choreo:

- **JSON to XML**: Transforms a JSON payload in a request or response into XML format. This policy is applicable only to JSON payloads in mediation flows. Applying it to a non-JSON payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to XML.
- **XML to JSON**: Converts an XML payload in a request or response into JSON format. This policy is applicable only to XML payloads in mediation flows. Applying it to a non-XML payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to JSON.
- **Remove Query Parameter**: Removes specified query parameters from a request. You can use this policy multiple times to remove different parameters. Attempting to remove a non-existent parameter has no effect. If the parameter exists, it will be removed; otherwise, the request proceeds as usual.
- **Remove Header**: Removes specified headers from a request or response. You can attach this policy multiple times to remove multiple headers. The header name must be static, but you can use placeholders to configure different values for different environments. For example, `${headerName}`.
- **Add Query Parameter**: Adds query parameters to a request. You can attach this policy multiple times to add various parameters. Adding the same parameter multiple times creates an array of values. The parameter name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${fooValue}`.
- **Add Header**: Adds headers to a request or response. If the same header is added multiple times, values are appended rather than overwritten. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`.
- **Set Header**: Sets headers in a request or response, overwriting any existing values. You can attach this policy multiple times to set multiple headers. Each time the same header is set, it replaces the previous value. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`. 
- **Rewrite Resource Path**: Modifies the resource path of an HTTP request by replacing the original path with a new relative path. You can apply this policy multiple times, but only the last instance will take effect. The new path must be static, but you can use placeholders to configure different values for different environments. For example, `${myResourcePath}`.
- **Log Message**: Logs the payload and headers of a request or response. Attaching this policy multiple times results in duplicate log entries. By default, headers and payloads are not logged. To log them, you can enable `Log Headers` and `Log Payload` parameters. To exclude specific headers when logging, you can use the `Excluded Headers` parameter, which takes a comma-separated list of header names. An error will occur if payload logging is enabled but the payload cannot be read.

These inbuilt mediation policies provide flexibility to manage API requests and responses, allowing for custom transformations and logic without requiring custom code.

For details on attaching and managing one or more policies to an API proxy component implementation via the Choreo Console, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

For details on applying advanced settings on mediation policies, see [Apply Advanced Settings on Mediation Policies](../api-policies/apply-advanced-settings-on-mediation-policies.md).


# Apply Advanced Settings on Mediation Policies

Advanced settings for mediation policies are available for proxy components with an attached mediation policy. For details on attaching a mediation policy to a proxy component, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

The approach to applying advanced settings depends on whether the proxy component is deployed or not.

## Mediation policy advanced settings

| **Setting**                     | **Purpose**    | **How to apply**  | **Impact**   |
|---------------------------------|----------------|-------------------|--------------|
| **HTTP version**                | By default, Choreo supports HTTP 1.1. If necessary, you can change to HTTP 1.0 or HTTP 2.0. | Specify the required HTTP version in the **Advanced Settings** field. <br> ![HTTP version setting](../../assets/img/api-management/api-policies/advanced-settings/http-version-setting.png) | The mediation application will use the specified HTTP version when interacting with backend services.  |
| **Hostname verification**       | Choreo enables hostname verification by default when using mTLS. You can disable it if necessary. | Set the `verifyHostname` parameter to `false` in the **Advanced Settings** field. <br> ![Hostname verification setting](../../assets/img/api-management/api-policies/advanced-settings/hostname-verification-setting.png)   | Hostname verification will be skipped during mTLS interactions.                              |
| **Minimum evictable idle time** | Determines how long (in seconds) an outgoing connection remains idle before eviction. The default is 300 seconds. | Set the required idle time in the **Advanced Settings** field. <br> ![Minimum evictable idle time setting](../../assets/img/api-management/api-policies/advanced-settings/minimum-evictable-idle-time-setting.png)          | Idle connections will be closed and evicted after the defined period.                    |
| **Detailed access log**         | By default, logs related to the mediation application are generated and can be viewed as [runtime logs](../../monitoring-and-insights/view-logs.md#runtime-logs). You can disable these logs if necessary.      | Set the `detailedAccessLog` parameter in the **Advanced Settings** field. <br> ![Detailed access log setting](../../assets/img/api-management/api-policies/advanced-settings/detailed-access-log-setting.png)  | Logs related to the mediation application will not be generated.    |

## Configure advanced settings for a proxy component

To configure advanced settings for a proxy component with an attached mediation policy, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to configure advanced settings.
3. In the left navigation menu, click **Deploy**.
4. Depending on the deployment status of the proxy component, follow one of these steps:
   - If the proxy component is not deployed, go to the **Set Up** card and click **Configure & Deploy**. 
   - If the proxy component is already deployed, go to the respective environment card depending on the environment you want to apply advanced settings, and then click the **Environment Variables** icon.
5. In the **Configurations** pane that opens, expand the **Defaultable Configurables** section. 
6. In the **Advanced Settings** field, configure the necessary settings as described in the [Mediation policy advanced settings](#mediation-policy-advanced-settings) section.
7. Click **Save & Deploy**.


# Attach and Manage Policies

You can easily attach one or more policies to an API proxy component implementation via the Choreo Console. If necessary, you can also rearrange or swap the policies you attach.

In Choreo, when you attach a mediation policy to a proxy, the deployment is a two-step process.

1. Deployment initiation: 

     If the component to which you want to attach the mediation policy is new, the system creates and commits a new repository with the mediation service code based on the attached policy. This new service is called the mediation application. 

2. Deploying the API:

     Once the deployment initiation is complete, you can specify configuration values if any, and proceed to deploy. Choreo builds the generated mediation application and pushes the Docker image to the Docker registry. Finally, Choreo deploys the mediation application with the API Proxy.

When a mediation policy is attached to a specific flow, the API invocation undergoes the following behavioral modification:
 
 ![Request/Response flow](../../assets/img/api-management/api-policies/request-response-flow.png)

 - In the request path, the requests that pass through the gateway reach the relevant component, and Choreo executes any attached policies to the resource's request path before sending it to the backend. 

- In the response path, the mediation component receives response messages from the backend, and Choreo executes any mediation policies attached to the `Response` flow or the `Error` flow. Then the response is forwarded to the client.

- If an error occurs during the execution of policies or due to an internal error, Choreo executes the `Error` flow and sends an error response to the client.

## Attach a policy

To attach a policy to the `Request`, `Response`, or `Error` flow of a REST API proxy, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to attach a policy.
3. In the left navigation menu, click **Develop** and then click **Policies**.
4. From the list of resources, expand the resource to which you want to attach the policy. 
5. Click **Attach Mediation Policy** in the respective flow for which you want to attach a policy.
6. In the **Policy List** pane that opens, click on a required policy to view its details.
7. If the attached policy requires parameter configuration, on the policy pane enter the appropriate values and configure the parameters. To make a parameter a configurable variable, input the value in the `${<variableName>}` format. For example, you can use `${name}` as an example.

    ![Configure parameters](../../assets/img/api-management/api-policies/configure-parameters.png)
 
8. To attach the policy, click **Add**.

After attaching an API Policy, it is necessary to deploy the API for the policy to become active within its corresponding flow. 
To deploy the API follow the steps below: 

9. In the left navigation menu, click **Deploy** and then click **Configure & Deploy**. Choreo performs the mediation application generation step and opens the **Configure & Deploy** pane.

10. In the **Configure & Deploy** pane, if you have any configurable variables that require values, specify appropriate values for them.

     ![Save and deploy values](../../assets/img/api-management/api-policies/save-and-deploy.png)

11. Click **Save & Deploy**.

## Refresh mediation policies

Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. These changes include:

 - Addition, deletion, or modification of API resources.
 - Attachment, removal, or editing of API mediation policies.
 - Endpoint modifications via the **Develop** page.
 - Initial configuration or removal of backend endpoints or mutual TLS certificates.

If none of the above changes occur during deployment, Choreo skips the code generation and build process of the mediation application.

!!! info
    - If you want to enforce the code generation and build process of the mediation application in instances where the specified changes do not take place, you must turn on the **Refresh Mediation Policies** toggle when you configure and deploy the component. 
    - It is useful to enable **Refresh Mediation Policies** when you want to incorporate the latest Ballerina patches for your generated mediation application. However, this can result in longer deployment times.

## Implement an API policy

Choreo allows you to implement an API policy as a Ballerina project and attach it to an API proxy component. 

!!! info
    Supported Ballerina version: 2201.5.5 

To implement a policy, follow the steps given below: 

### Prerequisites

1. Set up [ Ballerina 2201.5.5](https://ballerina.io/downloads/swan-lake-release-notes/swan-lake-2201.5.5).
2. Open the `~/.ballerina/settings.toml` file and ensure you have configured an access token to Ballerina Central. If you have not configured an access token, follow the steps given below to configure one: 
    1. Generate a token via [https://central.ballerina.io/dashboard?tab=token](https://central.ballerina.io/dashboard?tab=token).
    2. Download the generated `Settings.toml` file and copy it to your local `~/.ballerina` directory.
    
Alternatively, you can set the access token via the `BALLERINA_CENTRAL_ACCESS_TOKEN` environment variable.

``` 
export BALLERINA_CENTRAL_ACCESS_TOKEN=<access-token> 
```

### Step 1: Initialize a Ballerina project

Choreo provides a template to initialize a mediation policy project with all the required configurations. The mediation policy project will be created as a Ballerina project.

To create a Ballerina project for the mediation policy using `mediation.template` as the project template, issue the following command:  
   
**Format:**

```
    bal new -t choreo/mediation.template:1.0.0 <policy-name> 
```
    
**Example:**

```
    bal new -t choreo/mediation.template:1.0.0 validateHeader 
```
 The Ballerina project that is created should have the following content: 

![Ballerina project](../../assets/img/api-management/api-policies/ballerina-project.png)

Depending on your requirement, you can modify the `Ballerina.toml` and the `Package.md` files of the generated project. For example, you can update the org, package, package version, API documentation content, keywords, etc.

!!! note
    To successfully publish to Ballerina Central, make sure you update the `org` value to your organization name.

```
     [package]
        org = "starkindustries"
        name = "validateHeader"
        version = "1.0.0"
        export = ["validateHeader"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
```

### Step 2: Implement the policy

In this step, you will implement the policy. 

Let's assume you want to implement a policy to validate an incoming header in the request and the response. 

- **Request path**: If the request header is not present or if the validation fails, you want to log an error and return a `403 Bad Request` response to the client.
- **Response path**: You want to log a message to indicate whether the request is valid or not.

To implement the policy, open the `policy.bal` file in the Ballerina project and update the generated policy stubs(i.e., request, response, or fault) appropriately. 

The following sections walk you through sample implementations for the **Request** and **Response** stubs:

#### Request flow

The following is a sample implementation for the request flow:
 
```ballerina
@mediation:RequestFlow
public function validateRequestHeader(mediation:Context ctx, http:Request req, string headerName, string headerValue) returns http:Response|false|error|() {
   string|http:HeaderNotFoundError header = req.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return generateResponse(message, http:STATUS_BAD_REQUEST);
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return generateResponse(validationFailedMessage, http:STATUS_BAD_REQUEST);
    }
    log:printInfo("Header validation successful");
    return ();
};
    
function generateResponse(string message, int statusCode) returns http:Response {
    http:Response response = new();
    response.setTextPayload(message); 
    response.statusCode = statusCode;
    return response;
}

```

#### Response flow

The following is a sample implementation for the response flow:

```ballerina
@mediation:ResponseFlow
public function validateResponseHeader(mediation:Context ctx, http:Request req, http:Response res, string headerName, string headerValue) returns http:Response|false|error|() { 
   string|http:HeaderNotFoundError header = res.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return ();
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return ();
   }
   return ();
}

```

#### Fault flow

In this guide, you are not going to make any changes to the `Fault` flow. Therefore, you can remove the `Fault` flow stub from the `policy.bal` file.

!!! note 
    The  **@mediation:RequestFlow**, **@mediation:ResponseFlow**, and **@mediation:FaultFlow** annotations are bound with the keywords in the `Ballerina.toml`. Therefore, the changes you make to the policy stubs should reflect in the `Ballerina.toml` file. For example, if the policy is applicable only on the request and response paths, you can remove the  **@mediation:FaultFlow** annotation from the policy. Then, you **MUST** also remove the **choreo-apim-mediation-fault-flow** keyword from the generated `Ballerina.toml` file. If you do not do so, the Ballerina compiler will show an error at compile time.

#### Publish as a private custom policy
 
 Choreo supports publishing a policy as a private custom policy. Publishing a policy as a private custom policy makes the policy inaccessible outside of the organization. To publish a policy as a private custom policy, change the visibility to `private` prior to pushing the package to Ballerina Central as follows:

 1. Open the `Ballerina.toml` file of your policy. 
 2. Set the visibility to **private** by adding the configuration `visibility="private"`. For example:

     ```
     [package]
        org = "orgName"
        name = "packageName"
        version = "1.0.2"
        export = ["packageName"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
        visibility = "private"
     ```

 3. Package and publish your policy to Ballerina Central.     

#### Best practices 

When implementing a policy, it is essential to follow best practices to ensure efficiency and maintainability. Here are some recommended best practices to follow:

- Organize the source code within the default module of the package. Do not add any additional modules.
- A policy implementation can contain any combination of flows. A generated project contains stubs for all three flows: `Request`, `Response`, and `Fault`. You can remove any stub that you do not require. For example, when you create a policy that re-writes the resource paths, you can remove the `Response` and `fault` stubs. 
- The HTTP request/response objects and context record parameters gets passed as references to the policy functions. Therefore, the changes you make to these values persist throughout the policy execution and are propagated to subsequent policies. This behavior allows the request and response objects to accumulate transformations applied by attached policies.
- Familiarize yourself with the different return types of policy flows. The following return types are unmodifiable:
    - **http:Response** - Returns an HTTP response when you terminate the mediation flow prematurely. For example,  in the in-flow sequence, the mediation sequence terminates before calling the backend. The mediation policy then sends an HTTP response to the client.
    - **false** - Returns `false` if you want to terminate the mediation sequence with a predefined response (on the Choreo side).
    - **error** - Returns an error if you want to terminate the mediation flow and transfer control to the fault flow. The fault flow would then construct an error response and send it to the client.
    - **()** - Returns () to signal the successful completion of the policy. Once the proxy has completed executing the policy, it starts to execute the next policy in the sequence.

### Step 3: Publish the policy

Once you implement a policy, you must publish it to Ballerina Central. 

When you attach a policy and deploy an API, Choreo pulls the necessary packages from Ballerina Central and bundles them into the mediation application under the hood. Therefore to use policies in your APIs, you must publish them as public packages. 

To publish the policy, follow the steps given below:

1. To package the policy before you publish it to Ballerina Central, issue the following command:
    ``` 
        bal pack 
    ```
2. To publish the package to Ballerina Central, issue the following command:

    ``` 
        bal push 
    ```

Once you publish the package, it will appear as follows in the policy list:

![Published policy](../../assets/img/api-management/api-policies/published-policy.png)

### Write unit tests

You can write unit tests to test policy functions in a manner similar to how you write unit tests for a regular [Ballerina function](https://ballerina.io/learn/test-ballerina-code/test-a-simple-function/). 

The following is a sample unit test for the `validateRequestHeader` function:

```
import ballerina/http;
import choreo/mediation;
import ballerina/test;


@test:Config {}
public function testRequestHeaderValidationFailure() {
  http:Request req = new;
  http:Response|false|error|() result = validateRequestHeader(createContext("get", "/test"), req, "testHeader", "test");


  if !(result is http:Response) {
    test:assertFail("Expected http:Response, found " + (typeof result).toString());
  }


  test:assertEquals(result.statusCode, http:STATUS_BAD_REQUEST, "Status code mismatch");
}


function createContext(string httpMethod, string resPath) returns mediation:Context {
   mediation:ResourcePath originalPath = checkpanic mediation:createImmutableResourcePath(resPath);
   mediation:Context originalCtx =
               mediation:createImmutableMediationContext(httpMethod, originalPath.pathSegments(), {}, {});
   mediation:ResourcePath mutableResPath = checkpanic mediation:createMutableResourcePath(resPath);
   return mediation:createMutableMediationContext(originalCtx, mutableResPath.pathSegments(), {}, {});
}

```

The policy function modifies the same request/response/context instance that you pass to it. You can check the request/response/context instance after calling the policy function to verify changes.

### Glossary

Here are some of the common terms used when working with policies in Choreo:

#### mediation:Context

The mediation context is used to pass parameters between policies. It is created per request and you can access it in any of the flows. For example, if a correlation ID needs to be set to the request, you can set it in the context of the request flow and access it in the response or fault flow. 

The mediation context can include the following functions:

```
# Retrieves the value for the specified key.   
public function get(string name) returns anydata;


# Stores the provided key-value pair. If a mapping exists for the key, the value is overwritten.
public function put(string name, anydata value);


# Removes the entry mapped by the specified key and returns the removed value.
public function remove(string name) returns anydata;


# Retrieves the value for the specified key. If there is no mapping for the key, return the specified
public function getOrDefault(string name, anydata default) returns anydata;


# Checks whether a mapping exists for the specified key.
public function hasKey(string name) returns boolean;


# Returns the `mediation:Context` instance which captured the initial contextual information of the resource,
# before the mediation flow was invoked. Calling this on an original `mediation:Context` object will return itself.
public function originalContext() returns Context;


# The HTTP method of the resource method
public function httpMethod() returns string;


# Retrieves an instance of `mediation:ResourcePath` which is an API for contextual information on the resource path
# of this resource. It also contains methods for modifying the resource path as the user sees fit. This resource
# path is the same path used by the mediation service for deriving the backend endpoint's resource to invoke.
# Therefore, the default behavior of the mediation service is to invoke a resource in the backend endpoint which
# has the same relative resource path as the corresponding mediation service resource.
public function resourcePath() returns ResourcePath;


# Sets the given `mediation:ResourcePath` instance as the resource path of this context.
public function setResourcePath(ResourcePath path);


# Adds a mapping between a path param name and a resolved value for it. There need not be a path parameter in the
# resource path by the name specified in `name` for one to use this method. On its own, the path param values have
# no bearing on the resource path.
public function addPathParamValue(string name, PathParamValue value);


# Returns the collection of resolved values for the path parameters in this particular context, mapped
# by the parameter name.
public function resolvedPathParams() returns map<PathParamValue> & readonly;


# Removes the resolved path parameter value which maps to the specified name.
public function removePathParamValue(string name);


# Adds a query parameter to the request to be sent to the backend. If there is already a query parameter by
# with the same name, the new value will be appended to it, making it an array.
public function addQueryParam(string name, string value);


# Removes the specified query parameter from the request. If the value of the parameter is an array, the whole
# array will be removed.
public function removeQueryParam(string name);


# Retrieves a map of all the query parameters in the current request context. The returned map is a read-only snapshot
# of the map of query parameters in the context at the time this method was called.
public function queryParams() returns map<string[]> & readonly;
```

### Keywords

The `Ballerina.toml` file needs to include the following keywords for the mediation policies to work:

- **choreo-apim-mediation-policy**: This keyword is a mandatory keyword that is required to identify that the package is a mediation policy type.
- **choreo-apim-mediation-request-flow**: Specifies whether the policy applies to the request flow.
- **choreo-apim-mediation-response-flow**: Specifies whether the policy applies to the response flow.
- **choreo-apim-mediation-fault-flow**: Specifies whether the policy is applicable for the fault flow.

#### Policy name and description

The `Package.md` file contains information about the policy. Choreo uses this information to render the policy configuring UI. This file is written in Markdown format and should be structured as follows.

**Format:**

```
# <policy-name>


## Overview


<policy description>

```

**Example:**

```
# ValidateHeader


## Overview


This policy validates the request and response headers with the configured values.

```

#### Policy versioning

When it comes to policy versioning in Choreo or mediation dependencies, it is important to consider the major version changes in the Ballerina language. For example, transitioning from update 1 to update 2 requires a major version increment, which can introduce significant incompatibilities.

Therefore, to ensure compatibility, the recommended approach is to version the policy package in a manner that the major version gets upgraded when the Choreo/mediation dependency version is upgraded to a major version.  


# Assign Subscription Plans to APIs

API subscription plans allow API publishers to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security.

Choreo allows users with the administrator role to create, update, and delete subscription plans at the organization level. For instructions on creating subscription plans, see [Create API Subscription Plans](../../administer/create-api-subscription-plans.md).

Once created, Choreo allows API publishers to assign subscription plans to APIs, providing different levels of access based on user needs.

To assign subscription plans to an API, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to assign subscription plans.
3. In the left navigation menu, click **Manage** and then click **Subscription Plans**. This displays the subscription plans available for the component.
4. Enable the **Subscription Plan Status** toggle corresponding to the subscription plans you want to assign to the API.

    ![Enable toggle](../../assets/img/api-management/manage-api-traffic/enable-toggle.png)

5. Click **Save**.

When an API has subscription plans assigned to it, API consumers can select the plan that best fits their requirements during the subscription process. For details, see [Subscribe to an API with a Subscription Plan](./subscribe-to-an-api-with-a-subscription-plan.md)


# Subscribe to an API with a Subscription Plan

If an API has subscription plans assigned to it, API consumers can select the subscription plan that best fits their requirements at the time of subscribing to the API.

To subscribe to an API with a subscription plan, follow the steps given below:

1. Sign in to the [Choreo Developer Portal](https://devportal.choreo.dev).
2. In the Developer Portal header, click **Applications**.
3. On the **My Applications** page, click on the application you want to use to subscribe to an API.
4. In the left navigation menu, click **Subscriptions**. 
5. In the **Subscription Management** pane that opens, click **+ Add APIs**.
6. In the **Add APIs** pane that opens, select the API, API version, and subscription plan with which you want to subscribe to the API.
7. If the selected subscription plan requires administrator or API publisher approval to become active, click Request Subscription. Otherwise, click Add Subscription. If the selected subscription plan requires approval, your subscription will be shown as "Pending" until it is approved by an organization admin or the API publisher.

    !!! Note
        If the subscription plan requires administrator or API publisher approval to become active, the subscription status will be set to Pending Creation until it is reviewed and approved.

    ![Add subscription](../../assets/img/api-management/manage-api-traffic/add-subscription.png)

To verify that the subscription plan works as expected, follow the steps given below:

1. In the Developer Portal header, click **APIs**.
2. Search for the API you subscribed to and click **Try Out**.
3. Invoke the API until you exceed the request limit set in the subscription plan. You will see that the API throttles further requests once the limit is reached.

    ![Throttle response](../../assets/img/api-management/manage-api-traffic/throttle-response.png)




# API Rate Limiting

API rate limiting is a technique that allows you to control the rate of requests made to an API. Rate limiting helps 
prevent system overload and enhances API performance. When you limit the number of requests that can be made in a 
specific time frame, you can ensure that your API is available and responsive to all users while protecting it from 
malicious attacks.

This page walks you through the steps to enable rate limiting for your APIs via Choreo and also provides information on 
the rate-limiting options supported by Choreo.

## Enable rate limiting for an API

To enable rate limiting for an API, follow the steps given below: 

!!! note
     You can apply rate-limiting settings separately for each environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). 
2. In the **Component Listing** pane, click on the component for which you want to apply rate limiting.
3. In the left navigation menu, click **Deploy**.
4. Go to the required environment card and click the view icon corresponding to the endpoint for which you want to apply rate limiting. 

    !!! info 
         If you are applying rate limiting for an API Proxy component, go to the required environment card, click the setting icon corresponding to **API Configuration**, and proceed to step 6.

5. In the **Endpoint Details** pane that opens, click the settings icon.
6. In the **Manage** section, click **Rate Limiting** to expand it.
7. Select a **Rate Limiting Level** depending on your requirement and click **Apply**.

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

By default, the APIs published in Choreo are visible to anyone who visits the Choreo Developer Portal. By default, Choreo sets the visibility of the API to `Public`. However, developers can control the visibility of their APIs by changing the default option to `Private` or `Restricted`. 

Visibility settings control users from viewing and modifying APIs. API visibility can be one of the following options:

 - **Public** : The API is **visible to all** in the developer portal.

 - **Private** : The API is visible to the **users who only sign in to the Developer Portal**.

 - **Restricted**: The API is **visible to only the user that has the roles that you specify**. This option helps developers to enforce fine-grained access control to the API.

## Change API visibility

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the REST API (Service) for which you want to control API visibility. 
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, select the required visibility setting from the **Visibility** list. 

    !!! note "Enable fine-grained role-based access control to the API"
         1. To enable fine-grained role-based access control to an API in the Developer Portal, select `Restricted` from the **API visibility** list. Once selected, you will see the roles available in your organization in the **Visible Roles** list. 
         2. Select any combination of roles. Only the users with the given roles can access the APIs through the Dev Portal. 
         3. Alternatively, You can create a new role and assign it to an API by following the steps below: 
             1. Click **+ Create New Role** in the list.
             2. Add the role name and description. 
             3. Click **Next**.
             4. Assign the relevant permissions to the new role.
             5. Click **Create**.
             6. Select the newly created role from the **Visible Roles** list.

6. Click **Save**.


# Documents

When an API consumer signs in to the Choreo Developer Portal to browse APIs, it is not sufficient to just have an API thumbnail along with the name and version of the API. An API consumer would expect to see more details about the API, such as the following:

 - A brief description of the API.
 - How to invoke the API.
 - The limitations/restrictions of the API.
 - Version history.

To provide such information that improves the overall visibility of the API, an API developer can add such documentation to an API before publishing it to the Developer Portal.

## Add documents to an API

To add documentation for an API, follow the steps given below.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).

2. In the **Component Listing** pane, click on the component for which you want to add documents. 

3. In the left navigation menu, click **Manage** and then click **Documents**.

4. Specify a title for the document and provide the content in markdown syntax. 
   
5. Click **Add** to save the document.

Depending on the information you need to add to the API, you can add one or more documents.

You can also edit existing documents and delete documents if necessary.


# Lifecycle Management

API lifecycle management is an important aspect of API management. The API lifecycle consists of various states that an API passes through, from creation to retirement. In Choreo, there are six distinct lifecycle states: created, pre-released, published, blocked, deprecated, and retired.

By leveraging the various lifecycle states, API managers can optimize the development process and ensure that subscribers have access to the latest and most reliable APIs.

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

To change the lifecycle state of an API via the Choreo Console, follow the instructions given below:

!!! tip      
     You must have publishing privileges to manage the lifecycle states of a component.

1. Sign in to the Choreo Console.
2. In the **Component Listing** pane, click on the component for which you want to manage the lifecycle.
3. In the left navigation menu, click **Manage**, and then click **Lifecycle**.
4. In the **Lifecycle Management** pane, you will see the lifecycle state transition diagram indicating the current lifecycle state of the component. Just above the lifecycle state transition diagram, The possible lifecycle states you can apply to the component are displayed just above the lifecycle state transition diagram. Click on a required lifecycle state to apply it to the component. For example, if a component is in the **Created** state, you can click either **Pre-release** or **Publish**.


# Rename API Display Name

Choreo allows you to make one or more endpoints accessible through its service and integration components. These endpoints are published as individual APIs in Choreo, accessible via the Choreo Developer Portal. By default, Choreo assigns an API name by combining the component name and the endpoint name, resulting in the following format: `<component name>-<endpoint name>`. For example, if you create a component named `Ballerina Reading List,` the API is displayed as `Ballerina Reading List - GraphQL Reading List 591.`

Choreo provides you with the flexibility to personalize the display name of the API, enhancing its user-friendliness and readability. Once you modify the API display name within the Choreo Console, Choreo applies the change immediately. From there onwards, Choreo displays the published API by this name in the Choreo Developer Portal.

Follow the steps below to rename the API display name:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. In the **Component Listing** pane, click on the component for which you want to rename the API display name. This opens the **Overview** page of the component.
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, specify an appropriate API display name in the **Name** field.
6. Click **Save**.

Now, you can view the updated API display name in the Choreo Developer Portal.


# OWASP Top 10

A set of rules enforcing OWASP security guidelines to prevent common vulnerabilities and ensure secure coding practices.
### ❌ owasp:api1:2023-no-numeric-ids

Use random IDs that cannot be guessed. UUIDs are preferred but any other random string will do.

---

### ❌ owasp:api2:2023-no-http-basic

Basic authentication credentials transported over network are more susceptible to interception than other forms of authentication, and as they are not encrypted it means passwords and tokens are more easily leaked.

---

### ❌ owasp:api2:2023-no-api-keys-in-url

API Keys are passed in headers, cookies, or query parameters to access APIs. Those keys can be eavesdropped, especially when they are passed in the URL, as logging or history tools will keep track of them and potentially expose them.

---

### ❌ owasp:api2:2023-no-credentials-in-url

URL parameters MUST NOT contain credentials such as API key, password, or secret.

---

### ❌ owasp:api2:2023-auth-insecure-schemes

There are many [HTTP authorization schemes](https://www.iana.org/assignments/http-authschemes/) but some of them are now considered insecure, such as negotiating authentication using specifications like NTLM or OAuth v1.

---

### ❌ owasp:api2:2023-jwt-best-practices

JSON Web Tokens RFC7519 is a compact, URL-safe, means of representing claims to be transferred between two parties. JWT can be enclosed in encrypted or signed tokens like JWS and JWE.

The [JOSE IANA registry](https://www.iana.org/assignments/jose/jose.xhtml) provides algorithms information.

RFC8725 describes common pitfalls in the JWx specifications and in
their implementations, such as:
- the ability to ignore algorithms, eg. `{"alg": "none"}`;
- using insecure algorithms like `RSASSA-PKCS1-v1_5` eg. `{"alg": "RS256"}`.
An API using JWT should explicit in the `description`
that the implementation conforms to RFC8725.
```
components:
  securitySchemes:
    JWTBearer:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        A bearer token in the format of a JWS and conformato
        to the specifications included in RFC8725.
```

---

### ❌ owasp:api2:2023-short-lived-access-tokens

Using short-lived access tokens is a good practice, and when using OAuth 2 this is done by using refresh tokens. If a malicious actor is able to get hold of an access token then rotation means that token might not work by the time they try to use it, or it could at least reduce how long they are able to perform malicious requests.

---

### ❌ owasp:api4:2023-rate-limit

Define proper rate limiting to avoid attackers overloading the API. There are many ways to implement rate-limiting, but most of them involve using HTTP headers, and there are two popular ways to do that:

IETF Draft HTTP RateLimit Headers:. [https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers)/

Customer headers like X-Rate-Limit-Limit (Twitter: [https://developer.twitter.com/en/docs/twitter-api/rate-limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) or X-RateLimit-Limit (GitHub: [https://docs.github.com/en/rest/overview/resources-in-the-rest-api](https://docs.github.com/en/rest/overview/resources-in-the-rest-api))

---

### ❌ owasp:api4:2023-rate-limit-retry-after

Define proper rate limiting to avoid attackers overloading the API. Part of that involves setting a Retry-After header so well meaning consumers are not polling and potentially exacerbating problems.

---

### ❌ owasp:api4:2023-array-limit

Array size should be limited to mitigate resource exhaustion attacks. This can be done using `maxItems`. You should ensure that the subschema in `items` is constrained too.

---

### ❌ owasp:api4:2023-string-limit

String size should be limited to mitigate resource exhaustion attacks. This can be done using `maxLength`, `enum` or `const`.

---

### ❌ owasp:api4:2023-integer-limit

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-limit-legacy

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-format

Integers should be limited to mitigate resource exhaustion attacks. Specifying whether int32 or int64 is expected via `format`.

---

### ❌ owasp:api8:2023-define-cors-origin

Setting up CORS headers will control which websites can make browser-based HTTP requests to your API, using either the wildcard "*" to allow any origin, or "null" to disable any origin. Alternatively you can use "Access-Control-Allow-Origin: https://example.com" to indicate that only requests originating from the specified domain (https://example.com) are allowed to access its resources.

More about CORS here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

---

### ❌ owasp:api8:2023-no-scheme-http

Server interactions must use the http protocol as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use the https or wss schemes instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api8:2023-no-server-http

Server interactions must not use the http:// as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use https:// or wss:// protocols instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api9:2023-inventory-access

Servers are required to use vendor extension x-internal set to true or false to explicitly explain the audience for the API, which will be picked up by most documentation tools.

---

### ❌ owasp:api9:2023-inventory-environment

Make it clear which servers are expected to run as which environment to avoid unexpected problems, exposing test data to the public, or letting bad actors bypass security measures to get to production-like environments.

---

### ⚠️ owasp:api3:2023-no-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api3:2023-no-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api4:2023-rate-limit-responses-429

OWASP API Security recommends defining schemas for all responses, even errors. A HTTP 429 response signals the API client is making too many requests, and will supply information about when to retry so that the client can back off calmly without everything breaking. Defining this response is important not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces. It also ensures your API/framework/gateway actually has rate limiting set up.

---

### ⚠️ owasp:api4:2023-string-restricted

To avoid unexpected values being sent or leaked, strings should have a `format`, RegEx `pattern`, `enum`, or `const`.

---

### ⚠️ owasp:api8:2023-define-error-validation

Carefully define schemas for all the API responses, including either 400, 422 or 4XX responses which describe errors caused by invalid requests.

---

### ⚠️ owasp:api8:2023-define-error-responses-401

OWASP API Security recommends defining schemas for all responses, even errors. The 401 describes what happens when a request is unauthorized, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ⚠️ owasp:api8:2023-define-error-responses-500

OWASP API Security recommends defining schemas for all responses, even errors. The 500 describes what happens when a request fails with an internal server error, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ℹ️ owasp:api7:2023-concerning-url-parameter

Using external resources based on user input for webhooks, file fetching from URLs, custom SSO, URL previews, or redirects can lead to a wide variety of security issues.

Learn more about Server Side Request Forgery [https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/).

---


# WSO2 API Design Guidelines

A guide detailing best practices for creating robust, scalable, and secure APIs, ensuring alignment with industry standards for optimal design.
### ❌ path-casing

Paths must be `kebab-case`, with hyphens separating words.

**Invalid Example**

`userInfo` must be separated with a hyphen.

```json
{
    "/userInfo": {
        "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user-info": {
       "post: }
       ....
}
```

---

### ❌ paths-no-file-extensions

Paths must not include `json` or `xml` file extensions.

**Invalid Example**

The path contains a `.json` extension. 

```json
{
    "/user.json": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ paths-no-http-verbs

Verbs such as `get`, `delete`, and `put` must not be included in paths because this information is conveyed by the HTTP method.

**Invalid Example**

The path contains the verb `get`. 

```json
{
    "/getUsers": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ path-parameters-snake-case

Path parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the path parameter must not contain digits.

**Invalid Example**

The `name` property on line 9 (`userId`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "userId",
            "in": "path"
          }
        ]
      }
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ]
      }
    }
  }
```

---

### ❌ query-parameters-snake-case

Query parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the query parameter must not contain digits.

**Invalid Example**

The `name` property on line 8 (`user-Id`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
   "parameters": [
     {
       "schema": {
         "type": "string"
       },
       "in": "query",
       "name": "user-Id"
     }
   ]
}
```

**Valid Example**

```json
{
    "parameters": [
      {
        "schema": {
          "type": "string"
        },
        "in": "query",
        "name": "user_id"
      }
    ]
 }
```

---

### ⚠️ resource-names-plural

Resource names should generally be plural. 

**Invalid Example**

```json
{
    "paths": {
      "/user": 
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users": 
    }
}
```

---

### ⚠️ paths-avoid-special-characters

Paths should not contain special characters, such as `$` `&` `+` `,` `;` `=` `?` and `@%`.

**Invalid Example**

The path contains an ampersand. 

```json
{
    "/user&info": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ℹ️ server-has-api

Server must have /api

---


# WSO2 Style Guidelines

A set of guidelines focused on enforcing uniformity in API style, including naming conventions, formatting, and documentation to ensure clarity and maintainability across all APIs.
### ❌ operation-operationId-valid-in-url

Operation IDs must not contain characters that are invalid for URLs.

**Invalid Example**

The `operationId` in this example includes a pipe and space, which are invalid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "invalid|operationID"
    }
  }
}
```

**Valid Example**

This `operationId` is valid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "this-must-be-unique"
    }
  }
}
```

---

### ❌ path-declarations-must-exist

Path parameter declarations must not be empty.

**Invalid Example**

`/users/{}`

**Valid Example**

`/users/{userId}`

---

### ❌ paths-no-trailing-slash

Paths must not end with a trailing slash.

`/users` and `/users/` are separate paths. It's considered bad practice for them to differ based only on a trailing slash. It's usually preferred to not have a trailing slash.

**Invalid Example**

The `users` path ends with a slash.

```json
{
  "/users/": {
    "post": {}
  }
}
```

**Valid Example**

```json
{
  "/user": {
    "post": {}
  }
}
```

---

### ❌ server-lowercase

Server URLs must be lowercase. This standard helps meet industry best practices.

**Invalid Example**

The `url` property uses uppercase letters.

```json
{
  "servers": [
    {
      "url": "https://ACME.com/api"
    }
  ]
}
```

**Valid Example**

The `url` property is fully lowercase.

```json
{
  "servers": [
    {
      "url": "https://acme.com/api"
    }
  ]
}
```

---

### ❌ oas2-api-schemes

OpenAPI 2 host `schemes` reflect the transfer protocol of the API. 
Host schemes must be present and an array with one or more of these values: 
`http`, `https`, `ws`, or `wss`.

**Valid Example**

This example shows that host schemes are `http` and `https`.

```json
{
  "schemes": [
    "http",
    "https"
  ]
}
```


---

### ❌ array-items

Schemas with `type: array`, require a sibling `items` field.

**Recommended:** Yes

**Good Example**

```yaml
TheGoodModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
        items: {}
```

**Bad Example**

```yaml
TheBadModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
```

---

### ⚠️ contact-url

The `contact` object should have a valid organization URL. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "url": "https://acme.com",
     ... 
  },
```

---

### ⚠️ contact-email

The `contact` object should have a valid email. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "email": "support.contact@acme.com"
  },
```

---

### ⚠️ info-contact

The `info` object should include a `contact` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "contact": {
      "name": "ACME Corporation",
      "url": "https://acme.com",
      "email": "support.contact@acme.com"
    }
  }
}
```

---

### ⚠️ info-description

The `info` object should have a `description` object.

**Valid Example**

```json
{
  "info": {
     ... ,
     "description": "This describes my API."
  }
}
```

---

### ⚠️ info-license

The `info` object should have a `license` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "license": {
      "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "url": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  }
}
```

---

### ⚠️ license-url

The `license` object should include a valid url.

**Valid Example**

```json
{
  "license": {
    "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "url": "https://creativecommons.org/licenses/by-sa/4.0/"
  }
}
```

---

### ⚠️ no-eval-in-markdown

Markdown descriptions should not contain [`eval()` functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval),
which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. eval()"
  }
}
```

---

### ⚠️ no-script-tags-in-markdown

Markdown descriptions should not contain `script` tags, which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. <script>alert(\"You are Hacked\");</script>"
  }
}
```

---

### ⚠️ openapi-tags-alphabetical

Global tags specified at the root OpenAPI Document level should be in alphabetical order based on the `name` property.

**Invalid Example**

```json
{
  "tags":[
    {
      "name":"Z Global Tag"
    },
    {
      "name":"A Global Tag"
    }
  ]
}
```

**Valid Example**

```json
{
  "tags":[
    {
      "name":"A Global Tag"
    },
    {
      "name":"Z Global Tag"
    }
  ]
}
```

---

### ⚠️ openapi-tags

At least one global tag should be specified at the root OpenAPI Document level.

**Valid Example**

```json
{
  "tags":[
    {
      "name":"Global Tag #1"
    },
    {
      "name":"Global Tag #2"
    }
  ]
}
```

---

### ⚠️ operation-description

Each operation should have a description.

**Valid Example**

```json
{
  "get": {
    "description": "Get a list of users."
  }
}
```

---

### ⚠️ operation-operationId

All operations should have an `operationId`.

**Valid Example**

```json
{
  "get": {
    "summary": "Get users",
    "operationId": "get-users"
  }
}
```

---

### ⚠️ operation-tags

At least one tag should be defined for each operation.

**Valid Example**

```json
{
  "get": {
    "tags": ["Users"]
  }
}
```

---

### ⚠️ contact-name

The `contact` object should have an organization name.

**Valid Example**

```json
{
  "contact": {
    "name": "ACME Corporation"
  }
}
```

---

### ⚠️ path-keys-no-trailing-slash

Path keys should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "/users/": {
  }
}
```

**Valid Example**

```json
{
  "/users": {
  }
}
```

---

### ⚠️ path-not-include-query

Paths should not include `query` string items. Instead, add them as parameters with `in: query`.

**Invalid Example**

```json
{
  "/users/{?id}": {
  }
}
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ⚠️ tag-description

Tags defined at the global level should have a description.

**Valid Example**

```json
{
  "tags": [
    {
      "name": "Users",
      "description": "End-user information"
    }
  ]
}
```

---

### ⚠️ api-servers

A server should be defined at the root document level. This can be localhost, a development server, or a production server.

**Valid OpenAPI V3 Example**

```json
{
  "servers": [
    {
      "url": "https://staging.myprodserver.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://myprodserver.com/v1",
      "description": "Production server"
    }
  ]
}
```

**Valid OpenAPI V2 Example**

```json
{
  "host": "myprodserver.com",
  "basePath": "/v2",
  "schemes": [
    "https"
  ]
}
```

---

### ⚠️ server-trailing-slash

Server URLs should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5/"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```

---

### ⚠️ server-not-example

Server URLs must not direct to example.com. This helps ensure URLs 
are valid before you distribute your API document.

**Invalid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://example.com"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```


---

### ⚠️ parameter-description

All `parameter` objects should have a description.

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "integer"
      },
      ... ,
      ... ,
      "description": "The number of days to include in the response."
    }
  ]
}
```


---

### ⚠️ oas2-anyOf

The `anyOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "anyOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas2-oneOf

The `oneOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "oneOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas3-examples-value-or-externalValue

The `examples` object should include a `value` or `externalValue` field, but cannot include both.

**Invalid Example**

This example includes both a `value` field and an `externalValue` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      },
      "externalValue": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```

**Valid Example**

This example includes only a `value` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```


---

### ⚠️ path-parameters-on-path-only

Path parameters should be defined on the path level instead of the operation level.

**Invalid Example**

The `user_id` path parameter on line 8 should not be included with the `patch` operation.

```json
{      
  "patch": {
    "parameters": [
      {
        "schema": {
          "type": "integer"
        },
        "name": "user_id",
        "in": "path"
      }
    ]
  }
}
```

**Valid Example**

The `user-id` path parameter is correctly located at the path level.

```json
{
  "paths": {
    "/users/{userId}": {
      "parameters": [
        {
          "schema": {
            "type": "integer"
          },
          "name": "user_id",
          "in": "path"
        }
      ]
    }
  }
}
```

---

### ⚠️ paths-no-query-params

Paths should not have query parameters in them. They should be defined separately in the OpenAPI.

**Invalid Example**

```json
{
  "/users/{?id}": {
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ℹ️ operation-singular-tag

Operation should not have more than a single tag.

---


# About API Policies

API policies are units of business logic that you can apply to modify the flow of API invocations. 

You can apply a policy to alter the  `Request`, `Response`, or `Error` flow of an API invocation before it reaches the backend or the client. For example, you can add a policy to the response flow to transform the payload from JSON to XML and add a header to the response. 

## Inbuilt mediation policies

Choreo supports a set of inbuilt mediation policies that can handle common API transformation and mediation tasks. These policies run within a single mediation service, making it straightforward to implement and manage complex mediation logic. The following inbuilt policies are available in Choreo:

- **JSON to XML**: Transforms a JSON payload in a request or response into XML format. This policy is applicable only to JSON payloads in mediation flows. Applying it to a non-JSON payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to XML.
- **XML to JSON**: Converts an XML payload in a request or response into JSON format. This policy is applicable only to XML payloads in mediation flows. Applying it to a non-XML payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to JSON.
- **Remove Query Parameter**: Removes specified query parameters from a request. You can use this policy multiple times to remove different parameters. Attempting to remove a non-existent parameter has no effect. If the parameter exists, it will be removed; otherwise, the request proceeds as usual.
- **Remove Header**: Removes specified headers from a request or response. You can attach this policy multiple times to remove multiple headers. The header name must be static, but you can use placeholders to configure different values for different environments. For example, `${headerName}`.
- **Add Query Parameter**: Adds query parameters to a request. You can attach this policy multiple times to add various parameters. Adding the same parameter multiple times creates an array of values. The parameter name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${fooValue}`.
- **Add Header**: Adds headers to a request or response. If the same header is added multiple times, values are appended rather than overwritten. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`.
- **Set Header**: Sets headers in a request or response, overwriting any existing values. You can attach this policy multiple times to set multiple headers. Each time the same header is set, it replaces the previous value. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`. 
- **Rewrite Resource Path**: Modifies the resource path of an HTTP request by replacing the original path with a new relative path. You can apply this policy multiple times, but only the last instance will take effect. The new path must be static, but you can use placeholders to configure different values for different environments. For example, `${myResourcePath}`.
- **Log Message**: Logs the payload and headers of a request or response. Attaching this policy multiple times results in duplicate log entries. By default, headers and payloads are not logged. To log them, you can enable `Log Headers` and `Log Payload` parameters. To exclude specific headers when logging, you can use the `Excluded Headers` parameter, which takes a comma-separated list of header names. An error will occur if payload logging is enabled but the payload cannot be read.

These inbuilt mediation policies provide flexibility to manage API requests and responses, allowing for custom transformations and logic without requiring custom code.

For details on attaching and managing one or more policies to an API proxy component implementation via the Choreo Console, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

For details on applying advanced settings on mediation policies, see [Apply Advanced Settings on Mediation Policies](../api-policies/apply-advanced-settings-on-mediation-policies.md).


# Apply Advanced Settings on Mediation Policies

Advanced settings for mediation policies are available for proxy components with an attached mediation policy. For details on attaching a mediation policy to a proxy component, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

The approach to applying advanced settings depends on whether the proxy component is deployed or not.

## Mediation policy advanced settings

| **Setting**                     | **Purpose**    | **How to apply**  | **Impact**   |
|---------------------------------|----------------|-------------------|--------------|
| **HTTP version**                | By default, Choreo supports HTTP 1.1. If necessary, you can change to HTTP 1.0 or HTTP 2.0. | Specify the required HTTP version in the **Advanced Settings** field. <br> ![HTTP version setting](../../assets/img/api-management/api-policies/advanced-settings/http-version-setting.png) | The mediation application will use the specified HTTP version when interacting with backend services.  |
| **Hostname verification**       | Choreo enables hostname verification by default when using mTLS. You can disable it if necessary. | Set the `verifyHostname` parameter to `false` in the **Advanced Settings** field. <br> ![Hostname verification setting](../../assets/img/api-management/api-policies/advanced-settings/hostname-verification-setting.png)   | Hostname verification will be skipped during mTLS interactions.                              |
| **Minimum evictable idle time** | Determines how long (in seconds) an outgoing connection remains idle before eviction. The default is 300 seconds. | Set the required idle time in the **Advanced Settings** field. <br> ![Minimum evictable idle time setting](../../assets/img/api-management/api-policies/advanced-settings/minimum-evictable-idle-time-setting.png)          | Idle connections will be closed and evicted after the defined period.                    |
| **Detailed access log**         | By default, logs related to the mediation application are generated and can be viewed as [runtime logs](../../monitoring-and-insights/view-logs.md#runtime-logs). You can disable these logs if necessary.      | Set the `detailedAccessLog` parameter in the **Advanced Settings** field. <br> ![Detailed access log setting](../../assets/img/api-management/api-policies/advanced-settings/detailed-access-log-setting.png)  | Logs related to the mediation application will not be generated.    |

## Configure advanced settings for a proxy component

To configure advanced settings for a proxy component with an attached mediation policy, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to configure advanced settings.
3. In the left navigation menu, click **Deploy**.
4. Depending on the deployment status of the proxy component, follow one of these steps:
   - If the proxy component is not deployed, go to the **Set Up** card and click **Configure & Deploy**. 
   - If the proxy component is already deployed, go to the respective environment card depending on the environment you want to apply advanced settings, and then click the **Environment Variables** icon.
5. In the **Configurations** pane that opens, expand the **Defaultable Configurables** section. 
6. In the **Advanced Settings** field, configure the necessary settings as described in the [Mediation policy advanced settings](#mediation-policy-advanced-settings) section.
7. Click **Save & Deploy**.


# Attach and Manage Policies

You can easily attach one or more policies to an API proxy component implementation via the Choreo Console. If necessary, you can also rearrange or swap the policies you attach.

In Choreo, when you attach a mediation policy to a proxy, the deployment is a two-step process.

1. Deployment initiation: 

     If the component to which you want to attach the mediation policy is new, the system creates and commits a new repository with the mediation service code based on the attached policy. This new service is called the mediation application. 

2. Deploying the API:

     Once the deployment initiation is complete, you can specify configuration values if any, and proceed to deploy. Choreo builds the generated mediation application and pushes the Docker image to the Docker registry. Finally, Choreo deploys the mediation application with the API Proxy.

When a mediation policy is attached to a specific flow, the API invocation undergoes the following behavioral modification:
 
 ![Request/Response flow](../../assets/img/api-management/api-policies/request-response-flow.png)

 - In the request path, the requests that pass through the gateway reach the relevant component, and Choreo executes any attached policies to the resource's request path before sending it to the backend. 

- In the response path, the mediation component receives response messages from the backend, and Choreo executes any mediation policies attached to the `Response` flow or the `Error` flow. Then the response is forwarded to the client.

- If an error occurs during the execution of policies or due to an internal error, Choreo executes the `Error` flow and sends an error response to the client.

## Attach a policy

To attach a policy to the `Request`, `Response`, or `Error` flow of a REST API proxy, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to attach a policy.
3. In the left navigation menu, click **Develop** and then click **Policies**.
4. From the list of resources, expand the resource to which you want to attach the policy. 
5. Click **Attach Mediation Policy** in the respective flow for which you want to attach a policy.
6. In the **Policy List** pane that opens, click on a required policy to view its details.
7. If the attached policy requires parameter configuration, on the policy pane enter the appropriate values and configure the parameters. To make a parameter a configurable variable, input the value in the `${<variableName>}` format. For example, you can use `${name}` as an example.

    ![Configure parameters](../../assets/img/api-management/api-policies/configure-parameters.png)
 
8. To attach the policy, click **Add**.

After attaching an API Policy, it is necessary to deploy the API for the policy to become active within its corresponding flow. 
To deploy the API follow the steps below: 

9. In the left navigation menu, click **Deploy** and then click **Configure & Deploy**. Choreo performs the mediation application generation step and opens the **Configure & Deploy** pane.

10. In the **Configure & Deploy** pane, if you have any configurable variables that require values, specify appropriate values for them.

     ![Save and deploy values](../../assets/img/api-management/api-policies/save-and-deploy.png)

11. Click **Save & Deploy**.

## Refresh mediation policies

Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. These changes include:

 - Addition, deletion, or modification of API resources.
 - Attachment, removal, or editing of API mediation policies.
 - Endpoint modifications via the **Develop** page.
 - Initial configuration or removal of backend endpoints or mutual TLS certificates.

If none of the above changes occur during deployment, Choreo skips the code generation and build process of the mediation application.

!!! info
    - If you want to enforce the code generation and build process of the mediation application in instances where the specified changes do not take place, you must turn on the **Refresh Mediation Policies** toggle when you configure and deploy the component. 
    - It is useful to enable **Refresh Mediation Policies** when you want to incorporate the latest Ballerina patches for your generated mediation application. However, this can result in longer deployment times.

## Implement an API policy

Choreo allows you to implement an API policy as a Ballerina project and attach it to an API proxy component. 

!!! info
    Supported Ballerina version: 2201.5.5 

To implement a policy, follow the steps given below: 

### Prerequisites

1. Set up [ Ballerina 2201.5.5](https://ballerina.io/downloads/swan-lake-release-notes/swan-lake-2201.5.5).
2. Open the `~/.ballerina/settings.toml` file and ensure you have configured an access token to Ballerina Central. If you have not configured an access token, follow the steps given below to configure one: 
    1. Generate a token via [https://central.ballerina.io/dashboard?tab=token](https://central.ballerina.io/dashboard?tab=token).
    2. Download the generated `Settings.toml` file and copy it to your local `~/.ballerina` directory.
    
Alternatively, you can set the access token via the `BALLERINA_CENTRAL_ACCESS_TOKEN` environment variable.

``` 
export BALLERINA_CENTRAL_ACCESS_TOKEN=<access-token> 
```

### Step 1: Initialize a Ballerina project

Choreo provides a template to initialize a mediation policy project with all the required configurations. The mediation policy project will be created as a Ballerina project.

To create a Ballerina project for the mediation policy using `mediation.template` as the project template, issue the following command:  
   
**Format:**

```
    bal new -t choreo/mediation.template:1.0.0 <policy-name> 
```
    
**Example:**

```
    bal new -t choreo/mediation.template:1.0.0 validateHeader 
```
 The Ballerina project that is created should have the following content: 

![Ballerina project](../../assets/img/api-management/api-policies/ballerina-project.png)

Depending on your requirement, you can modify the `Ballerina.toml` and the `Package.md` files of the generated project. For example, you can update the org, package, package version, API documentation content, keywords, etc.

!!! note
    To successfully publish to Ballerina Central, make sure you update the `org` value to your organization name.

```
     [package]
        org = "starkindustries"
        name = "validateHeader"
        version = "1.0.0"
        export = ["validateHeader"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
```

### Step 2: Implement the policy

In this step, you will implement the policy. 

Let's assume you want to implement a policy to validate an incoming header in the request and the response. 

- **Request path**: If the request header is not present or if the validation fails, you want to log an error and return a `403 Bad Request` response to the client.
- **Response path**: You want to log a message to indicate whether the request is valid or not.

To implement the policy, open the `policy.bal` file in the Ballerina project and update the generated policy stubs(i.e., request, response, or fault) appropriately. 

The following sections walk you through sample implementations for the **Request** and **Response** stubs:

#### Request flow

The following is a sample implementation for the request flow:
 
```ballerina
@mediation:RequestFlow
public function validateRequestHeader(mediation:Context ctx, http:Request req, string headerName, string headerValue) returns http:Response|false|error|() {
   string|http:HeaderNotFoundError header = req.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return generateResponse(message, http:STATUS_BAD_REQUEST);
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return generateResponse(validationFailedMessage, http:STATUS_BAD_REQUEST);
    }
    log:printInfo("Header validation successful");
    return ();
};
    
function generateResponse(string message, int statusCode) returns http:Response {
    http:Response response = new();
    response.setTextPayload(message); 
    response.statusCode = statusCode;
    return response;
}

```

#### Response flow

The following is a sample implementation for the response flow:

```ballerina
@mediation:ResponseFlow
public function validateResponseHeader(mediation:Context ctx, http:Request req, http:Response res, string headerName, string headerValue) returns http:Response|false|error|() { 
   string|http:HeaderNotFoundError header = res.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return ();
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return ();
   }
   return ();
}

```

#### Fault flow

In this guide, you are not going to make any changes to the `Fault` flow. Therefore, you can remove the `Fault` flow stub from the `policy.bal` file.

!!! note 
    The  **@mediation:RequestFlow**, **@mediation:ResponseFlow**, and **@mediation:FaultFlow** annotations are bound with the keywords in the `Ballerina.toml`. Therefore, the changes you make to the policy stubs should reflect in the `Ballerina.toml` file. For example, if the policy is applicable only on the request and response paths, you can remove the  **@mediation:FaultFlow** annotation from the policy. Then, you **MUST** also remove the **choreo-apim-mediation-fault-flow** keyword from the generated `Ballerina.toml` file. If you do not do so, the Ballerina compiler will show an error at compile time.

#### Publish as a private custom policy
 
 Choreo supports publishing a policy as a private custom policy. Publishing a policy as a private custom policy makes the policy inaccessible outside of the organization. To publish a policy as a private custom policy, change the visibility to `private` prior to pushing the package to Ballerina Central as follows:

 1. Open the `Ballerina.toml` file of your policy. 
 2. Set the visibility to **private** by adding the configuration `visibility="private"`. For example:

     ```
     [package]
        org = "orgName"
        name = "packageName"
        version = "1.0.2"
        export = ["packageName"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
        visibility = "private"
     ```

 3. Package and publish your policy to Ballerina Central.     

#### Best practices 

When implementing a policy, it is essential to follow best practices to ensure efficiency and maintainability. Here are some recommended best practices to follow:

- Organize the source code within the default module of the package. Do not add any additional modules.
- A policy implementation can contain any combination of flows. A generated project contains stubs for all three flows: `Request`, `Response`, and `Fault`. You can remove any stub that you do not require. For example, when you create a policy that re-writes the resource paths, you can remove the `Response` and `fault` stubs. 
- The HTTP request/response objects and context record parameters gets passed as references to the policy functions. Therefore, the changes you make to these values persist throughout the policy execution and are propagated to subsequent policies. This behavior allows the request and response objects to accumulate transformations applied by attached policies.
- Familiarize yourself with the different return types of policy flows. The following return types are unmodifiable:
    - **http:Response** - Returns an HTTP response when you terminate the mediation flow prematurely. For example,  in the in-flow sequence, the mediation sequence terminates before calling the backend. The mediation policy then sends an HTTP response to the client.
    - **false** - Returns `false` if you want to terminate the mediation sequence with a predefined response (on the Choreo side).
    - **error** - Returns an error if you want to terminate the mediation flow and transfer control to the fault flow. The fault flow would then construct an error response and send it to the client.
    - **()** - Returns () to signal the successful completion of the policy. Once the proxy has completed executing the policy, it starts to execute the next policy in the sequence.

### Step 3: Publish the policy

Once you implement a policy, you must publish it to Ballerina Central. 

When you attach a policy and deploy an API, Choreo pulls the necessary packages from Ballerina Central and bundles them into the mediation application under the hood. Therefore to use policies in your APIs, you must publish them as public packages. 

To publish the policy, follow the steps given below:

1. To package the policy before you publish it to Ballerina Central, issue the following command:
    ``` 
        bal pack 
    ```
2. To publish the package to Ballerina Central, issue the following command:

    ``` 
        bal push 
    ```

Once you publish the package, it will appear as follows in the policy list:

![Published policy](../../assets/img/api-management/api-policies/published-policy.png)

### Write unit tests

You can write unit tests to test policy functions in a manner similar to how you write unit tests for a regular [Ballerina function](https://ballerina.io/learn/test-ballerina-code/test-a-simple-function/). 

The following is a sample unit test for the `validateRequestHeader` function:

```
import ballerina/http;
import choreo/mediation;
import ballerina/test;


@test:Config {}
public function testRequestHeaderValidationFailure() {
  http:Request req = new;
  http:Response|false|error|() result = validateRequestHeader(createContext("get", "/test"), req, "testHeader", "test");


  if !(result is http:Response) {
    test:assertFail("Expected http:Response, found " + (typeof result).toString());
  }


  test:assertEquals(result.statusCode, http:STATUS_BAD_REQUEST, "Status code mismatch");
}


function createContext(string httpMethod, string resPath) returns mediation:Context {
   mediation:ResourcePath originalPath = checkpanic mediation:createImmutableResourcePath(resPath);
   mediation:Context originalCtx =
               mediation:createImmutableMediationContext(httpMethod, originalPath.pathSegments(), {}, {});
   mediation:ResourcePath mutableResPath = checkpanic mediation:createMutableResourcePath(resPath);
   return mediation:createMutableMediationContext(originalCtx, mutableResPath.pathSegments(), {}, {});
}

```

The policy function modifies the same request/response/context instance that you pass to it. You can check the request/response/context instance after calling the policy function to verify changes.

### Glossary

Here are some of the common terms used when working with policies in Choreo:

#### mediation:Context

The mediation context is used to pass parameters between policies. It is created per request and you can access it in any of the flows. For example, if a correlation ID needs to be set to the request, you can set it in the context of the request flow and access it in the response or fault flow. 

The mediation context can include the following functions:

```
# Retrieves the value for the specified key.   
public function get(string name) returns anydata;


# Stores the provided key-value pair. If a mapping exists for the key, the value is overwritten.
public function put(string name, anydata value);


# Removes the entry mapped by the specified key and returns the removed value.
public function remove(string name) returns anydata;


# Retrieves the value for the specified key. If there is no mapping for the key, return the specified
public function getOrDefault(string name, anydata default) returns anydata;


# Checks whether a mapping exists for the specified key.
public function hasKey(string name) returns boolean;


# Returns the `mediation:Context` instance which captured the initial contextual information of the resource,
# before the mediation flow was invoked. Calling this on an original `mediation:Context` object will return itself.
public function originalContext() returns Context;


# The HTTP method of the resource method
public function httpMethod() returns string;


# Retrieves an instance of `mediation:ResourcePath` which is an API for contextual information on the resource path
# of this resource. It also contains methods for modifying the resource path as the user sees fit. This resource
# path is the same path used by the mediation service for deriving the backend endpoint's resource to invoke.
# Therefore, the default behavior of the mediation service is to invoke a resource in the backend endpoint which
# has the same relative resource path as the corresponding mediation service resource.
public function resourcePath() returns ResourcePath;


# Sets the given `mediation:ResourcePath` instance as the resource path of this context.
public function setResourcePath(ResourcePath path);


# Adds a mapping between a path param name and a resolved value for it. There need not be a path parameter in the
# resource path by the name specified in `name` for one to use this method. On its own, the path param values have
# no bearing on the resource path.
public function addPathParamValue(string name, PathParamValue value);


# Returns the collection of resolved values for the path parameters in this particular context, mapped
# by the parameter name.
public function resolvedPathParams() returns map<PathParamValue> & readonly;


# Removes the resolved path parameter value which maps to the specified name.
public function removePathParamValue(string name);


# Adds a query parameter to the request to be sent to the backend. If there is already a query parameter by
# with the same name, the new value will be appended to it, making it an array.
public function addQueryParam(string name, string value);


# Removes the specified query parameter from the request. If the value of the parameter is an array, the whole
# array will be removed.
public function removeQueryParam(string name);


# Retrieves a map of all the query parameters in the current request context. The returned map is a read-only snapshot
# of the map of query parameters in the context at the time this method was called.
public function queryParams() returns map<string[]> & readonly;
```

### Keywords

The `Ballerina.toml` file needs to include the following keywords for the mediation policies to work:

- **choreo-apim-mediation-policy**: This keyword is a mandatory keyword that is required to identify that the package is a mediation policy type.
- **choreo-apim-mediation-request-flow**: Specifies whether the policy applies to the request flow.
- **choreo-apim-mediation-response-flow**: Specifies whether the policy applies to the response flow.
- **choreo-apim-mediation-fault-flow**: Specifies whether the policy is applicable for the fault flow.

#### Policy name and description

The `Package.md` file contains information about the policy. Choreo uses this information to render the policy configuring UI. This file is written in Markdown format and should be structured as follows.

**Format:**

```
# <policy-name>


## Overview


<policy description>

```

**Example:**

```
# ValidateHeader


## Overview


This policy validates the request and response headers with the configured values.

```

#### Policy versioning

When it comes to policy versioning in Choreo or mediation dependencies, it is important to consider the major version changes in the Ballerina language. For example, transitioning from update 1 to update 2 requires a major version increment, which can introduce significant incompatibilities.

Therefore, to ensure compatibility, the recommended approach is to version the policy package in a manner that the major version gets upgraded when the Choreo/mediation dependency version is upgraded to a major version.  


# Assign Subscription Plans to APIs

API subscription plans allow API publishers to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security.

Choreo allows users with the administrator role to create, update, and delete subscription plans at the organization level. For instructions on creating subscription plans, see [Create API Subscription Plans](../../administer/create-api-subscription-plans.md).

Once created, Choreo allows API publishers to assign subscription plans to APIs, providing different levels of access based on user needs.

To assign subscription plans to an API, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to assign subscription plans.
3. In the left navigation menu, click **Manage** and then click **Subscription Plans**. This displays the subscription plans available for the component.
4. Enable the **Subscription Plan Status** toggle corresponding to the subscription plans you want to assign to the API.

    ![Enable toggle](../../assets/img/api-management/manage-api-traffic/enable-toggle.png)

5. Click **Save**.

When an API has subscription plans assigned to it, API consumers can select the plan that best fits their requirements during the subscription process. For details, see [Subscribe to an API with a Subscription Plan](./subscribe-to-an-api-with-a-subscription-plan.md)


# Subscribe to an API with a Subscription Plan

If an API has subscription plans assigned to it, API consumers can select the subscription plan that best fits their requirements at the time of subscribing to the API.

To subscribe to an API with a subscription plan, follow the steps given below:

1. Sign in to the [Choreo Developer Portal](https://devportal.choreo.dev).
2. In the Developer Portal header, click **Applications**.
3. On the **My Applications** page, click on the application you want to use to subscribe to an API.
4. In the left navigation menu, click **Subscriptions**. 
5. In the **Subscription Management** pane that opens, click **+ Add APIs**.
6. In the **Add APIs** pane that opens, select the API, API version, and subscription plan with which you want to subscribe to the API.
7. If the selected subscription plan requires administrator or API publisher approval to become active, click Request Subscription. Otherwise, click Add Subscription. If the selected subscription plan requires approval, your subscription will be shown as "Pending" until it is approved by an organization admin or the API publisher.

    !!! Note
        If the subscription plan requires administrator or API publisher approval to become active, the subscription status will be set to Pending Creation until it is reviewed and approved.

    ![Add subscription](../../assets/img/api-management/manage-api-traffic/add-subscription.png)

To verify that the subscription plan works as expected, follow the steps given below:

1. In the Developer Portal header, click **APIs**.
2. Search for the API you subscribed to and click **Try Out**.
3. Invoke the API until you exceed the request limit set in the subscription plan. You will see that the API throttles further requests once the limit is reached.

    ![Throttle response](../../assets/img/api-management/manage-api-traffic/throttle-response.png)




# API Rate Limiting

API rate limiting is a technique that allows you to control the rate of requests made to an API. Rate limiting helps 
prevent system overload and enhances API performance. When you limit the number of requests that can be made in a 
specific time frame, you can ensure that your API is available and responsive to all users while protecting it from 
malicious attacks.

This page walks you through the steps to enable rate limiting for your APIs via Choreo and also provides information on 
the rate-limiting options supported by Choreo.

## Enable rate limiting for an API

To enable rate limiting for an API, follow the steps given below: 

!!! note
     You can apply rate-limiting settings separately for each environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). 
2. In the **Component Listing** pane, click on the component for which you want to apply rate limiting.
3. In the left navigation menu, click **Deploy**.
4. Go to the required environment card and click the view icon corresponding to the endpoint for which you want to apply rate limiting. 

    !!! info 
         If you are applying rate limiting for an API Proxy component, go to the required environment card, click the setting icon corresponding to **API Configuration**, and proceed to step 6.

5. In the **Endpoint Details** pane that opens, click the settings icon.
6. In the **Manage** section, click **Rate Limiting** to expand it.
7. Select a **Rate Limiting Level** depending on your requirement and click **Apply**.

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

By default, the APIs published in Choreo are visible to anyone who visits the Choreo Developer Portal. By default, Choreo sets the visibility of the API to `Public`. However, developers can control the visibility of their APIs by changing the default option to `Private` or `Restricted`. 

Visibility settings control users from viewing and modifying APIs. API visibility can be one of the following options:

 - **Public** : The API is **visible to all** in the developer portal.

 - **Private** : The API is visible to the **users who only sign in to the Developer Portal**.

 - **Restricted**: The API is **visible to only the user that has the roles that you specify**. This option helps developers to enforce fine-grained access control to the API.

## Change API visibility

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the REST API (Service) for which you want to control API visibility. 
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, select the required visibility setting from the **Visibility** list. 

    !!! note "Enable fine-grained role-based access control to the API"
         1. To enable fine-grained role-based access control to an API in the Developer Portal, select `Restricted` from the **API visibility** list. Once selected, you will see the roles available in your organization in the **Visible Roles** list. 
         2. Select any combination of roles. Only the users with the given roles can access the APIs through the Dev Portal. 
         3. Alternatively, You can create a new role and assign it to an API by following the steps below: 
             1. Click **+ Create New Role** in the list.
             2. Add the role name and description. 
             3. Click **Next**.
             4. Assign the relevant permissions to the new role.
             5. Click **Create**.
             6. Select the newly created role from the **Visible Roles** list.

6. Click **Save**.


# Documents

When an API consumer signs in to the Choreo Developer Portal to browse APIs, it is not sufficient to just have an API thumbnail along with the name and version of the API. An API consumer would expect to see more details about the API, such as the following:

 - A brief description of the API.
 - How to invoke the API.
 - The limitations/restrictions of the API.
 - Version history.

To provide such information that improves the overall visibility of the API, an API developer can add such documentation to an API before publishing it to the Developer Portal.

## Add documents to an API

To add documentation for an API, follow the steps given below.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).

2. In the **Component Listing** pane, click on the component for which you want to add documents. 

3. In the left navigation menu, click **Manage** and then click **Documents**.

4. Specify a title for the document and provide the content in markdown syntax. 
   
5. Click **Add** to save the document.

Depending on the information you need to add to the API, you can add one or more documents.

You can also edit existing documents and delete documents if necessary.


# Lifecycle Management

API lifecycle management is an important aspect of API management. The API lifecycle consists of various states that an API passes through, from creation to retirement. In Choreo, there are six distinct lifecycle states: created, pre-released, published, blocked, deprecated, and retired.

By leveraging the various lifecycle states, API managers can optimize the development process and ensure that subscribers have access to the latest and most reliable APIs.

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

To change the lifecycle state of an API via the Choreo Console, follow the instructions given below:

!!! tip      
     You must have publishing privileges to manage the lifecycle states of a component.

1. Sign in to the Choreo Console.
2. In the **Component Listing** pane, click on the component for which you want to manage the lifecycle.
3. In the left navigation menu, click **Manage**, and then click **Lifecycle**.
4. In the **Lifecycle Management** pane, you will see the lifecycle state transition diagram indicating the current lifecycle state of the component. Just above the lifecycle state transition diagram, The possible lifecycle states you can apply to the component are displayed just above the lifecycle state transition diagram. Click on a required lifecycle state to apply it to the component. For example, if a component is in the **Created** state, you can click either **Pre-release** or **Publish**.


# Rename API Display Name

Choreo allows you to make one or more endpoints accessible through its service and integration components. These endpoints are published as individual APIs in Choreo, accessible via the Choreo Developer Portal. By default, Choreo assigns an API name by combining the component name and the endpoint name, resulting in the following format: `<component name>-<endpoint name>`. For example, if you create a component named `Ballerina Reading List,` the API is displayed as `Ballerina Reading List - GraphQL Reading List 591.`

Choreo provides you with the flexibility to personalize the display name of the API, enhancing its user-friendliness and readability. Once you modify the API display name within the Choreo Console, Choreo applies the change immediately. From there onwards, Choreo displays the published API by this name in the Choreo Developer Portal.

Follow the steps below to rename the API display name:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. In the **Component Listing** pane, click on the component for which you want to rename the API display name. This opens the **Overview** page of the component.
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, specify an appropriate API display name in the **Name** field.
6. Click **Save**.

Now, you can view the updated API display name in the Choreo Developer Portal.


# OWASP Top 10

A set of rules enforcing OWASP security guidelines to prevent common vulnerabilities and ensure secure coding practices.
### ❌ owasp:api1:2023-no-numeric-ids

Use random IDs that cannot be guessed. UUIDs are preferred but any other random string will do.

---

### ❌ owasp:api2:2023-no-http-basic

Basic authentication credentials transported over network are more susceptible to interception than other forms of authentication, and as they are not encrypted it means passwords and tokens are more easily leaked.

---

### ❌ owasp:api2:2023-no-api-keys-in-url

API Keys are passed in headers, cookies, or query parameters to access APIs. Those keys can be eavesdropped, especially when they are passed in the URL, as logging or history tools will keep track of them and potentially expose them.

---

### ❌ owasp:api2:2023-no-credentials-in-url

URL parameters MUST NOT contain credentials such as API key, password, or secret.

---

### ❌ owasp:api2:2023-auth-insecure-schemes

There are many [HTTP authorization schemes](https://www.iana.org/assignments/http-authschemes/) but some of them are now considered insecure, such as negotiating authentication using specifications like NTLM or OAuth v1.

---

### ❌ owasp:api2:2023-jwt-best-practices

JSON Web Tokens RFC7519 is a compact, URL-safe, means of representing claims to be transferred between two parties. JWT can be enclosed in encrypted or signed tokens like JWS and JWE.

The [JOSE IANA registry](https://www.iana.org/assignments/jose/jose.xhtml) provides algorithms information.

RFC8725 describes common pitfalls in the JWx specifications and in
their implementations, such as:
- the ability to ignore algorithms, eg. `{"alg": "none"}`;
- using insecure algorithms like `RSASSA-PKCS1-v1_5` eg. `{"alg": "RS256"}`.
An API using JWT should explicit in the `description`
that the implementation conforms to RFC8725.
```
components:
  securitySchemes:
    JWTBearer:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        A bearer token in the format of a JWS and conformato
        to the specifications included in RFC8725.
```

---

### ❌ owasp:api2:2023-short-lived-access-tokens

Using short-lived access tokens is a good practice, and when using OAuth 2 this is done by using refresh tokens. If a malicious actor is able to get hold of an access token then rotation means that token might not work by the time they try to use it, or it could at least reduce how long they are able to perform malicious requests.

---

### ❌ owasp:api4:2023-rate-limit

Define proper rate limiting to avoid attackers overloading the API. There are many ways to implement rate-limiting, but most of them involve using HTTP headers, and there are two popular ways to do that:

IETF Draft HTTP RateLimit Headers:. [https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers)/

Customer headers like X-Rate-Limit-Limit (Twitter: [https://developer.twitter.com/en/docs/twitter-api/rate-limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) or X-RateLimit-Limit (GitHub: [https://docs.github.com/en/rest/overview/resources-in-the-rest-api](https://docs.github.com/en/rest/overview/resources-in-the-rest-api))

---

### ❌ owasp:api4:2023-rate-limit-retry-after

Define proper rate limiting to avoid attackers overloading the API. Part of that involves setting a Retry-After header so well meaning consumers are not polling and potentially exacerbating problems.

---

### ❌ owasp:api4:2023-array-limit

Array size should be limited to mitigate resource exhaustion attacks. This can be done using `maxItems`. You should ensure that the subschema in `items` is constrained too.

---

### ❌ owasp:api4:2023-string-limit

String size should be limited to mitigate resource exhaustion attacks. This can be done using `maxLength`, `enum` or `const`.

---

### ❌ owasp:api4:2023-integer-limit

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-limit-legacy

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-format

Integers should be limited to mitigate resource exhaustion attacks. Specifying whether int32 or int64 is expected via `format`.

---

### ❌ owasp:api8:2023-define-cors-origin

Setting up CORS headers will control which websites can make browser-based HTTP requests to your API, using either the wildcard "*" to allow any origin, or "null" to disable any origin. Alternatively you can use "Access-Control-Allow-Origin: https://example.com" to indicate that only requests originating from the specified domain (https://example.com) are allowed to access its resources.

More about CORS here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

---

### ❌ owasp:api8:2023-no-scheme-http

Server interactions must use the http protocol as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use the https or wss schemes instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api8:2023-no-server-http

Server interactions must not use the http:// as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use https:// or wss:// protocols instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api9:2023-inventory-access

Servers are required to use vendor extension x-internal set to true or false to explicitly explain the audience for the API, which will be picked up by most documentation tools.

---

### ❌ owasp:api9:2023-inventory-environment

Make it clear which servers are expected to run as which environment to avoid unexpected problems, exposing test data to the public, or letting bad actors bypass security measures to get to production-like environments.

---

### ⚠️ owasp:api3:2023-no-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api3:2023-no-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api4:2023-rate-limit-responses-429

OWASP API Security recommends defining schemas for all responses, even errors. A HTTP 429 response signals the API client is making too many requests, and will supply information about when to retry so that the client can back off calmly without everything breaking. Defining this response is important not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces. It also ensures your API/framework/gateway actually has rate limiting set up.

---

### ⚠️ owasp:api4:2023-string-restricted

To avoid unexpected values being sent or leaked, strings should have a `format`, RegEx `pattern`, `enum`, or `const`.

---

### ⚠️ owasp:api8:2023-define-error-validation

Carefully define schemas for all the API responses, including either 400, 422 or 4XX responses which describe errors caused by invalid requests.

---

### ⚠️ owasp:api8:2023-define-error-responses-401

OWASP API Security recommends defining schemas for all responses, even errors. The 401 describes what happens when a request is unauthorized, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ⚠️ owasp:api8:2023-define-error-responses-500

OWASP API Security recommends defining schemas for all responses, even errors. The 500 describes what happens when a request fails with an internal server error, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ℹ️ owasp:api7:2023-concerning-url-parameter

Using external resources based on user input for webhooks, file fetching from URLs, custom SSO, URL previews, or redirects can lead to a wide variety of security issues.

Learn more about Server Side Request Forgery [https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/).

---


# WSO2 API Design Guidelines

A guide detailing best practices for creating robust, scalable, and secure APIs, ensuring alignment with industry standards for optimal design.
### ❌ path-casing

Paths must be `kebab-case`, with hyphens separating words.

**Invalid Example**

`userInfo` must be separated with a hyphen.

```json
{
    "/userInfo": {
        "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user-info": {
       "post: }
       ....
}
```

---

### ❌ paths-no-file-extensions

Paths must not include `json` or `xml` file extensions.

**Invalid Example**

The path contains a `.json` extension. 

```json
{
    "/user.json": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ paths-no-http-verbs

Verbs such as `get`, `delete`, and `put` must not be included in paths because this information is conveyed by the HTTP method.

**Invalid Example**

The path contains the verb `get`. 

```json
{
    "/getUsers": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ path-parameters-snake-case

Path parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the path parameter must not contain digits.

**Invalid Example**

The `name` property on line 9 (`userId`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "userId",
            "in": "path"
          }
        ]
      }
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ]
      }
    }
  }
```

---

### ❌ query-parameters-snake-case

Query parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the query parameter must not contain digits.

**Invalid Example**

The `name` property on line 8 (`user-Id`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
   "parameters": [
     {
       "schema": {
         "type": "string"
       },
       "in": "query",
       "name": "user-Id"
     }
   ]
}
```

**Valid Example**

```json
{
    "parameters": [
      {
        "schema": {
          "type": "string"
        },
        "in": "query",
        "name": "user_id"
      }
    ]
 }
```

---

### ⚠️ resource-names-plural

Resource names should generally be plural. 

**Invalid Example**

```json
{
    "paths": {
      "/user": 
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users": 
    }
}
```

---

### ⚠️ paths-avoid-special-characters

Paths should not contain special characters, such as `$` `&` `+` `,` `;` `=` `?` and `@%`.

**Invalid Example**

The path contains an ampersand. 

```json
{
    "/user&info": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ℹ️ server-has-api

Server must have /api

---


# WSO2 Style Guidelines

A set of guidelines focused on enforcing uniformity in API style, including naming conventions, formatting, and documentation to ensure clarity and maintainability across all APIs.
### ❌ operation-operationId-valid-in-url

Operation IDs must not contain characters that are invalid for URLs.

**Invalid Example**

The `operationId` in this example includes a pipe and space, which are invalid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "invalid|operationID"
    }
  }
}
```

**Valid Example**

This `operationId` is valid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "this-must-be-unique"
    }
  }
}
```

---

### ❌ path-declarations-must-exist

Path parameter declarations must not be empty.

**Invalid Example**

`/users/{}`

**Valid Example**

`/users/{userId}`

---

### ❌ paths-no-trailing-slash

Paths must not end with a trailing slash.

`/users` and `/users/` are separate paths. It's considered bad practice for them to differ based only on a trailing slash. It's usually preferred to not have a trailing slash.

**Invalid Example**

The `users` path ends with a slash.

```json
{
  "/users/": {
    "post": {}
  }
}
```

**Valid Example**

```json
{
  "/user": {
    "post": {}
  }
}
```

---

### ❌ server-lowercase

Server URLs must be lowercase. This standard helps meet industry best practices.

**Invalid Example**

The `url` property uses uppercase letters.

```json
{
  "servers": [
    {
      "url": "https://ACME.com/api"
    }
  ]
}
```

**Valid Example**

The `url` property is fully lowercase.

```json
{
  "servers": [
    {
      "url": "https://acme.com/api"
    }
  ]
}
```

---

### ❌ oas2-api-schemes

OpenAPI 2 host `schemes` reflect the transfer protocol of the API. 
Host schemes must be present and an array with one or more of these values: 
`http`, `https`, `ws`, or `wss`.

**Valid Example**

This example shows that host schemes are `http` and `https`.

```json
{
  "schemes": [
    "http",
    "https"
  ]
}
```


---

### ❌ array-items

Schemas with `type: array`, require a sibling `items` field.

**Recommended:** Yes

**Good Example**

```yaml
TheGoodModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
        items: {}
```

**Bad Example**

```yaml
TheBadModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
```

---

### ⚠️ contact-url

The `contact` object should have a valid organization URL. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "url": "https://acme.com",
     ... 
  },
```

---

### ⚠️ contact-email

The `contact` object should have a valid email. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "email": "support.contact@acme.com"
  },
```

---

### ⚠️ info-contact

The `info` object should include a `contact` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "contact": {
      "name": "ACME Corporation",
      "url": "https://acme.com",
      "email": "support.contact@acme.com"
    }
  }
}
```

---

### ⚠️ info-description

The `info` object should have a `description` object.

**Valid Example**

```json
{
  "info": {
     ... ,
     "description": "This describes my API."
  }
}
```

---

### ⚠️ info-license

The `info` object should have a `license` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "license": {
      "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "url": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  }
}
```

---

### ⚠️ license-url

The `license` object should include a valid url.

**Valid Example**

```json
{
  "license": {
    "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "url": "https://creativecommons.org/licenses/by-sa/4.0/"
  }
}
```

---

### ⚠️ no-eval-in-markdown

Markdown descriptions should not contain [`eval()` functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval),
which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. eval()"
  }
}
```

---

### ⚠️ no-script-tags-in-markdown

Markdown descriptions should not contain `script` tags, which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. <script>alert(\"You are Hacked\");</script>"
  }
}
```

---

### ⚠️ openapi-tags-alphabetical

Global tags specified at the root OpenAPI Document level should be in alphabetical order based on the `name` property.

**Invalid Example**

```json
{
  "tags":[
    {
      "name":"Z Global Tag"
    },
    {
      "name":"A Global Tag"
    }
  ]
}
```

**Valid Example**

```json
{
  "tags":[
    {
      "name":"A Global Tag"
    },
    {
      "name":"Z Global Tag"
    }
  ]
}
```

---

### ⚠️ openapi-tags

At least one global tag should be specified at the root OpenAPI Document level.

**Valid Example**

```json
{
  "tags":[
    {
      "name":"Global Tag #1"
    },
    {
      "name":"Global Tag #2"
    }
  ]
}
```

---

### ⚠️ operation-description

Each operation should have a description.

**Valid Example**

```json
{
  "get": {
    "description": "Get a list of users."
  }
}
```

---

### ⚠️ operation-operationId

All operations should have an `operationId`.

**Valid Example**

```json
{
  "get": {
    "summary": "Get users",
    "operationId": "get-users"
  }
}
```

---

### ⚠️ operation-tags

At least one tag should be defined for each operation.

**Valid Example**

```json
{
  "get": {
    "tags": ["Users"]
  }
}
```

---

### ⚠️ contact-name

The `contact` object should have an organization name.

**Valid Example**

```json
{
  "contact": {
    "name": "ACME Corporation"
  }
}
```

---

### ⚠️ path-keys-no-trailing-slash

Path keys should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "/users/": {
  }
}
```

**Valid Example**

```json
{
  "/users": {
  }
}
```

---

### ⚠️ path-not-include-query

Paths should not include `query` string items. Instead, add them as parameters with `in: query`.

**Invalid Example**

```json
{
  "/users/{?id}": {
  }
}
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ⚠️ tag-description

Tags defined at the global level should have a description.

**Valid Example**

```json
{
  "tags": [
    {
      "name": "Users",
      "description": "End-user information"
    }
  ]
}
```

---

### ⚠️ api-servers

A server should be defined at the root document level. This can be localhost, a development server, or a production server.

**Valid OpenAPI V3 Example**

```json
{
  "servers": [
    {
      "url": "https://staging.myprodserver.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://myprodserver.com/v1",
      "description": "Production server"
    }
  ]
}
```

**Valid OpenAPI V2 Example**

```json
{
  "host": "myprodserver.com",
  "basePath": "/v2",
  "schemes": [
    "https"
  ]
}
```

---

### ⚠️ server-trailing-slash

Server URLs should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5/"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```

---

### ⚠️ server-not-example

Server URLs must not direct to example.com. This helps ensure URLs 
are valid before you distribute your API document.

**Invalid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://example.com"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```


---

### ⚠️ parameter-description

All `parameter` objects should have a description.

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "integer"
      },
      ... ,
      ... ,
      "description": "The number of days to include in the response."
    }
  ]
}
```


---

### ⚠️ oas2-anyOf

The `anyOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "anyOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas2-oneOf

The `oneOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "oneOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas3-examples-value-or-externalValue

The `examples` object should include a `value` or `externalValue` field, but cannot include both.

**Invalid Example**

This example includes both a `value` field and an `externalValue` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      },
      "externalValue": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```

**Valid Example**

This example includes only a `value` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```


---

### ⚠️ path-parameters-on-path-only

Path parameters should be defined on the path level instead of the operation level.

**Invalid Example**

The `user_id` path parameter on line 8 should not be included with the `patch` operation.

```json
{      
  "patch": {
    "parameters": [
      {
        "schema": {
          "type": "integer"
        },
        "name": "user_id",
        "in": "path"
      }
    ]
  }
}
```

**Valid Example**

The `user-id` path parameter is correctly located at the path level.

```json
{
  "paths": {
    "/users/{userId}": {
      "parameters": [
        {
          "schema": {
            "type": "integer"
          },
          "name": "user_id",
          "in": "path"
        }
      ]
    }
  }
}
```

---

### ⚠️ paths-no-query-params

Paths should not have query parameters in them. They should be defined separately in the OpenAPI.

**Invalid Example**

```json
{
  "/users/{?id}": {
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ℹ️ operation-singular-tag

Operation should not have more than a single tag.

---


# About API Policies

API policies are units of business logic that you can apply to modify the flow of API invocations. 

You can apply a policy to alter the  `Request`, `Response`, or `Error` flow of an API invocation before it reaches the backend or the client. For example, you can add a policy to the response flow to transform the payload from JSON to XML and add a header to the response. 

## Inbuilt mediation policies

Choreo supports a set of inbuilt mediation policies that can handle common API transformation and mediation tasks. These policies run within a single mediation service, making it straightforward to implement and manage complex mediation logic. The following inbuilt policies are available in Choreo:

- **JSON to XML**: Transforms a JSON payload in a request or response into XML format. This policy is applicable only to JSON payloads in mediation flows. Applying it to a non-JSON payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to XML.
- **XML to JSON**: Converts an XML payload in a request or response into JSON format. This policy is applicable only to XML payloads in mediation flows. Applying it to a non-XML payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to JSON.
- **Remove Query Parameter**: Removes specified query parameters from a request. You can use this policy multiple times to remove different parameters. Attempting to remove a non-existent parameter has no effect. If the parameter exists, it will be removed; otherwise, the request proceeds as usual.
- **Remove Header**: Removes specified headers from a request or response. You can attach this policy multiple times to remove multiple headers. The header name must be static, but you can use placeholders to configure different values for different environments. For example, `${headerName}`.
- **Add Query Parameter**: Adds query parameters to a request. You can attach this policy multiple times to add various parameters. Adding the same parameter multiple times creates an array of values. The parameter name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${fooValue}`.
- **Add Header**: Adds headers to a request or response. If the same header is added multiple times, values are appended rather than overwritten. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`.
- **Set Header**: Sets headers in a request or response, overwriting any existing values. You can attach this policy multiple times to set multiple headers. Each time the same header is set, it replaces the previous value. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`. 
- **Rewrite Resource Path**: Modifies the resource path of an HTTP request by replacing the original path with a new relative path. You can apply this policy multiple times, but only the last instance will take effect. The new path must be static, but you can use placeholders to configure different values for different environments. For example, `${myResourcePath}`.
- **Log Message**: Logs the payload and headers of a request or response. Attaching this policy multiple times results in duplicate log entries. By default, headers and payloads are not logged. To log them, you can enable `Log Headers` and `Log Payload` parameters. To exclude specific headers when logging, you can use the `Excluded Headers` parameter, which takes a comma-separated list of header names. An error will occur if payload logging is enabled but the payload cannot be read.

These inbuilt mediation policies provide flexibility to manage API requests and responses, allowing for custom transformations and logic without requiring custom code.

For details on attaching and managing one or more policies to an API proxy component implementation via the Choreo Console, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

For details on applying advanced settings on mediation policies, see [Apply Advanced Settings on Mediation Policies](../api-policies/apply-advanced-settings-on-mediation-policies.md).


# Apply Advanced Settings on Mediation Policies

Advanced settings for mediation policies are available for proxy components with an attached mediation policy. For details on attaching a mediation policy to a proxy component, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

The approach to applying advanced settings depends on whether the proxy component is deployed or not.

## Mediation policy advanced settings

| **Setting**                     | **Purpose**    | **How to apply**  | **Impact**   |
|---------------------------------|----------------|-------------------|--------------|
| **HTTP version**                | By default, Choreo supports HTTP 1.1. If necessary, you can change to HTTP 1.0 or HTTP 2.0. | Specify the required HTTP version in the **Advanced Settings** field. <br> ![HTTP version setting](../../assets/img/api-management/api-policies/advanced-settings/http-version-setting.png) | The mediation application will use the specified HTTP version when interacting with backend services.  |
| **Hostname verification**       | Choreo enables hostname verification by default when using mTLS. You can disable it if necessary. | Set the `verifyHostname` parameter to `false` in the **Advanced Settings** field. <br> ![Hostname verification setting](../../assets/img/api-management/api-policies/advanced-settings/hostname-verification-setting.png)   | Hostname verification will be skipped during mTLS interactions.                              |
| **Minimum evictable idle time** | Determines how long (in seconds) an outgoing connection remains idle before eviction. The default is 300 seconds. | Set the required idle time in the **Advanced Settings** field. <br> ![Minimum evictable idle time setting](../../assets/img/api-management/api-policies/advanced-settings/minimum-evictable-idle-time-setting.png)          | Idle connections will be closed and evicted after the defined period.                    |
| **Detailed access log**         | By default, logs related to the mediation application are generated and can be viewed as [runtime logs](../../monitoring-and-insights/view-logs.md#runtime-logs). You can disable these logs if necessary.      | Set the `detailedAccessLog` parameter in the **Advanced Settings** field. <br> ![Detailed access log setting](../../assets/img/api-management/api-policies/advanced-settings/detailed-access-log-setting.png)  | Logs related to the mediation application will not be generated.    |

## Configure advanced settings for a proxy component

To configure advanced settings for a proxy component with an attached mediation policy, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to configure advanced settings.
3. In the left navigation menu, click **Deploy**.
4. Depending on the deployment status of the proxy component, follow one of these steps:
   - If the proxy component is not deployed, go to the **Set Up** card and click **Configure & Deploy**. 
   - If the proxy component is already deployed, go to the respective environment card depending on the environment you want to apply advanced settings, and then click the **Environment Variables** icon.
5. In the **Configurations** pane that opens, expand the **Defaultable Configurables** section. 
6. In the **Advanced Settings** field, configure the necessary settings as described in the [Mediation policy advanced settings](#mediation-policy-advanced-settings) section.
7. Click **Save & Deploy**.


# Attach and Manage Policies

You can easily attach one or more policies to an API proxy component implementation via the Choreo Console. If necessary, you can also rearrange or swap the policies you attach.

In Choreo, when you attach a mediation policy to a proxy, the deployment is a two-step process.

1. Deployment initiation: 

     If the component to which you want to attach the mediation policy is new, the system creates and commits a new repository with the mediation service code based on the attached policy. This new service is called the mediation application. 

2. Deploying the API:

     Once the deployment initiation is complete, you can specify configuration values if any, and proceed to deploy. Choreo builds the generated mediation application and pushes the Docker image to the Docker registry. Finally, Choreo deploys the mediation application with the API Proxy.

When a mediation policy is attached to a specific flow, the API invocation undergoes the following behavioral modification:
 
 ![Request/Response flow](../../assets/img/api-management/api-policies/request-response-flow.png)

 - In the request path, the requests that pass through the gateway reach the relevant component, and Choreo executes any attached policies to the resource's request path before sending it to the backend. 

- In the response path, the mediation component receives response messages from the backend, and Choreo executes any mediation policies attached to the `Response` flow or the `Error` flow. Then the response is forwarded to the client.

- If an error occurs during the execution of policies or due to an internal error, Choreo executes the `Error` flow and sends an error response to the client.

## Attach a policy

To attach a policy to the `Request`, `Response`, or `Error` flow of a REST API proxy, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to attach a policy.
3. In the left navigation menu, click **Develop** and then click **Policies**.
4. From the list of resources, expand the resource to which you want to attach the policy. 
5. Click **Attach Mediation Policy** in the respective flow for which you want to attach a policy.
6. In the **Policy List** pane that opens, click on a required policy to view its details.
7. If the attached policy requires parameter configuration, on the policy pane enter the appropriate values and configure the parameters. To make a parameter a configurable variable, input the value in the `${<variableName>}` format. For example, you can use `${name}` as an example.

    ![Configure parameters](../../assets/img/api-management/api-policies/configure-parameters.png)
 
8. To attach the policy, click **Add**.

After attaching an API Policy, it is necessary to deploy the API for the policy to become active within its corresponding flow. 
To deploy the API follow the steps below: 

9. In the left navigation menu, click **Deploy** and then click **Configure & Deploy**. Choreo performs the mediation application generation step and opens the **Configure & Deploy** pane.

10. In the **Configure & Deploy** pane, if you have any configurable variables that require values, specify appropriate values for them.

     ![Save and deploy values](../../assets/img/api-management/api-policies/save-and-deploy.png)

11. Click **Save & Deploy**.

## Refresh mediation policies

Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. These changes include:

 - Addition, deletion, or modification of API resources.
 - Attachment, removal, or editing of API mediation policies.
 - Endpoint modifications via the **Develop** page.
 - Initial configuration or removal of backend endpoints or mutual TLS certificates.

If none of the above changes occur during deployment, Choreo skips the code generation and build process of the mediation application.

!!! info
    - If you want to enforce the code generation and build process of the mediation application in instances where the specified changes do not take place, you must turn on the **Refresh Mediation Policies** toggle when you configure and deploy the component. 
    - It is useful to enable **Refresh Mediation Policies** when you want to incorporate the latest Ballerina patches for your generated mediation application. However, this can result in longer deployment times.

## Implement an API policy

Choreo allows you to implement an API policy as a Ballerina project and attach it to an API proxy component. 

!!! info
    Supported Ballerina version: 2201.5.5 

To implement a policy, follow the steps given below: 

### Prerequisites

1. Set up [ Ballerina 2201.5.5](https://ballerina.io/downloads/swan-lake-release-notes/swan-lake-2201.5.5).
2. Open the `~/.ballerina/settings.toml` file and ensure you have configured an access token to Ballerina Central. If you have not configured an access token, follow the steps given below to configure one: 
    1. Generate a token via [https://central.ballerina.io/dashboard?tab=token](https://central.ballerina.io/dashboard?tab=token).
    2. Download the generated `Settings.toml` file and copy it to your local `~/.ballerina` directory.
    
Alternatively, you can set the access token via the `BALLERINA_CENTRAL_ACCESS_TOKEN` environment variable.

``` 
export BALLERINA_CENTRAL_ACCESS_TOKEN=<access-token> 
```

### Step 1: Initialize a Ballerina project

Choreo provides a template to initialize a mediation policy project with all the required configurations. The mediation policy project will be created as a Ballerina project.

To create a Ballerina project for the mediation policy using `mediation.template` as the project template, issue the following command:  
   
**Format:**

```
    bal new -t choreo/mediation.template:1.0.0 <policy-name> 
```
    
**Example:**

```
    bal new -t choreo/mediation.template:1.0.0 validateHeader 
```
 The Ballerina project that is created should have the following content: 

![Ballerina project](../../assets/img/api-management/api-policies/ballerina-project.png)

Depending on your requirement, you can modify the `Ballerina.toml` and the `Package.md` files of the generated project. For example, you can update the org, package, package version, API documentation content, keywords, etc.

!!! note
    To successfully publish to Ballerina Central, make sure you update the `org` value to your organization name.

```
     [package]
        org = "starkindustries"
        name = "validateHeader"
        version = "1.0.0"
        export = ["validateHeader"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
```

### Step 2: Implement the policy

In this step, you will implement the policy. 

Let's assume you want to implement a policy to validate an incoming header in the request and the response. 

- **Request path**: If the request header is not present or if the validation fails, you want to log an error and return a `403 Bad Request` response to the client.
- **Response path**: You want to log a message to indicate whether the request is valid or not.

To implement the policy, open the `policy.bal` file in the Ballerina project and update the generated policy stubs(i.e., request, response, or fault) appropriately. 

The following sections walk you through sample implementations for the **Request** and **Response** stubs:

#### Request flow

The following is a sample implementation for the request flow:
 
```ballerina
@mediation:RequestFlow
public function validateRequestHeader(mediation:Context ctx, http:Request req, string headerName, string headerValue) returns http:Response|false|error|() {
   string|http:HeaderNotFoundError header = req.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return generateResponse(message, http:STATUS_BAD_REQUEST);
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return generateResponse(validationFailedMessage, http:STATUS_BAD_REQUEST);
    }
    log:printInfo("Header validation successful");
    return ();
};
    
function generateResponse(string message, int statusCode) returns http:Response {
    http:Response response = new();
    response.setTextPayload(message); 
    response.statusCode = statusCode;
    return response;
}

```

#### Response flow

The following is a sample implementation for the response flow:

```ballerina
@mediation:ResponseFlow
public function validateResponseHeader(mediation:Context ctx, http:Request req, http:Response res, string headerName, string headerValue) returns http:Response|false|error|() { 
   string|http:HeaderNotFoundError header = res.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return ();
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return ();
   }
   return ();
}

```

#### Fault flow

In this guide, you are not going to make any changes to the `Fault` flow. Therefore, you can remove the `Fault` flow stub from the `policy.bal` file.

!!! note 
    The  **@mediation:RequestFlow**, **@mediation:ResponseFlow**, and **@mediation:FaultFlow** annotations are bound with the keywords in the `Ballerina.toml`. Therefore, the changes you make to the policy stubs should reflect in the `Ballerina.toml` file. For example, if the policy is applicable only on the request and response paths, you can remove the  **@mediation:FaultFlow** annotation from the policy. Then, you **MUST** also remove the **choreo-apim-mediation-fault-flow** keyword from the generated `Ballerina.toml` file. If you do not do so, the Ballerina compiler will show an error at compile time.

#### Publish as a private custom policy
 
 Choreo supports publishing a policy as a private custom policy. Publishing a policy as a private custom policy makes the policy inaccessible outside of the organization. To publish a policy as a private custom policy, change the visibility to `private` prior to pushing the package to Ballerina Central as follows:

 1. Open the `Ballerina.toml` file of your policy. 
 2. Set the visibility to **private** by adding the configuration `visibility="private"`. For example:

     ```
     [package]
        org = "orgName"
        name = "packageName"
        version = "1.0.2"
        export = ["packageName"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
        visibility = "private"
     ```

 3. Package and publish your policy to Ballerina Central.     

#### Best practices 

When implementing a policy, it is essential to follow best practices to ensure efficiency and maintainability. Here are some recommended best practices to follow:

- Organize the source code within the default module of the package. Do not add any additional modules.
- A policy implementation can contain any combination of flows. A generated project contains stubs for all three flows: `Request`, `Response`, and `Fault`. You can remove any stub that you do not require. For example, when you create a policy that re-writes the resource paths, you can remove the `Response` and `fault` stubs. 
- The HTTP request/response objects and context record parameters gets passed as references to the policy functions. Therefore, the changes you make to these values persist throughout the policy execution and are propagated to subsequent policies. This behavior allows the request and response objects to accumulate transformations applied by attached policies.
- Familiarize yourself with the different return types of policy flows. The following return types are unmodifiable:
    - **http:Response** - Returns an HTTP response when you terminate the mediation flow prematurely. For example,  in the in-flow sequence, the mediation sequence terminates before calling the backend. The mediation policy then sends an HTTP response to the client.
    - **false** - Returns `false` if you want to terminate the mediation sequence with a predefined response (on the Choreo side).
    - **error** - Returns an error if you want to terminate the mediation flow and transfer control to the fault flow. The fault flow would then construct an error response and send it to the client.
    - **()** - Returns () to signal the successful completion of the policy. Once the proxy has completed executing the policy, it starts to execute the next policy in the sequence.

### Step 3: Publish the policy

Once you implement a policy, you must publish it to Ballerina Central. 

When you attach a policy and deploy an API, Choreo pulls the necessary packages from Ballerina Central and bundles them into the mediation application under the hood. Therefore to use policies in your APIs, you must publish them as public packages. 

To publish the policy, follow the steps given below:

1. To package the policy before you publish it to Ballerina Central, issue the following command:
    ``` 
        bal pack 
    ```
2. To publish the package to Ballerina Central, issue the following command:

    ``` 
        bal push 
    ```

Once you publish the package, it will appear as follows in the policy list:

![Published policy](../../assets/img/api-management/api-policies/published-policy.png)

### Write unit tests

You can write unit tests to test policy functions in a manner similar to how you write unit tests for a regular [Ballerina function](https://ballerina.io/learn/test-ballerina-code/test-a-simple-function/). 

The following is a sample unit test for the `validateRequestHeader` function:

```
import ballerina/http;
import choreo/mediation;
import ballerina/test;


@test:Config {}
public function testRequestHeaderValidationFailure() {
  http:Request req = new;
  http:Response|false|error|() result = validateRequestHeader(createContext("get", "/test"), req, "testHeader", "test");


  if !(result is http:Response) {
    test:assertFail("Expected http:Response, found " + (typeof result).toString());
  }


  test:assertEquals(result.statusCode, http:STATUS_BAD_REQUEST, "Status code mismatch");
}


function createContext(string httpMethod, string resPath) returns mediation:Context {
   mediation:ResourcePath originalPath = checkpanic mediation:createImmutableResourcePath(resPath);
   mediation:Context originalCtx =
               mediation:createImmutableMediationContext(httpMethod, originalPath.pathSegments(), {}, {});
   mediation:ResourcePath mutableResPath = checkpanic mediation:createMutableResourcePath(resPath);
   return mediation:createMutableMediationContext(originalCtx, mutableResPath.pathSegments(), {}, {});
}

```

The policy function modifies the same request/response/context instance that you pass to it. You can check the request/response/context instance after calling the policy function to verify changes.

### Glossary

Here are some of the common terms used when working with policies in Choreo:

#### mediation:Context

The mediation context is used to pass parameters between policies. It is created per request and you can access it in any of the flows. For example, if a correlation ID needs to be set to the request, you can set it in the context of the request flow and access it in the response or fault flow. 

The mediation context can include the following functions:

```
# Retrieves the value for the specified key.   
public function get(string name) returns anydata;


# Stores the provided key-value pair. If a mapping exists for the key, the value is overwritten.
public function put(string name, anydata value);


# Removes the entry mapped by the specified key and returns the removed value.
public function remove(string name) returns anydata;


# Retrieves the value for the specified key. If there is no mapping for the key, return the specified
public function getOrDefault(string name, anydata default) returns anydata;


# Checks whether a mapping exists for the specified key.
public function hasKey(string name) returns boolean;


# Returns the `mediation:Context` instance which captured the initial contextual information of the resource,
# before the mediation flow was invoked. Calling this on an original `mediation:Context` object will return itself.
public function originalContext() returns Context;


# The HTTP method of the resource method
public function httpMethod() returns string;


# Retrieves an instance of `mediation:ResourcePath` which is an API for contextual information on the resource path
# of this resource. It also contains methods for modifying the resource path as the user sees fit. This resource
# path is the same path used by the mediation service for deriving the backend endpoint's resource to invoke.
# Therefore, the default behavior of the mediation service is to invoke a resource in the backend endpoint which
# has the same relative resource path as the corresponding mediation service resource.
public function resourcePath() returns ResourcePath;


# Sets the given `mediation:ResourcePath` instance as the resource path of this context.
public function setResourcePath(ResourcePath path);


# Adds a mapping between a path param name and a resolved value for it. There need not be a path parameter in the
# resource path by the name specified in `name` for one to use this method. On its own, the path param values have
# no bearing on the resource path.
public function addPathParamValue(string name, PathParamValue value);


# Returns the collection of resolved values for the path parameters in this particular context, mapped
# by the parameter name.
public function resolvedPathParams() returns map<PathParamValue> & readonly;


# Removes the resolved path parameter value which maps to the specified name.
public function removePathParamValue(string name);


# Adds a query parameter to the request to be sent to the backend. If there is already a query parameter by
# with the same name, the new value will be appended to it, making it an array.
public function addQueryParam(string name, string value);


# Removes the specified query parameter from the request. If the value of the parameter is an array, the whole
# array will be removed.
public function removeQueryParam(string name);


# Retrieves a map of all the query parameters in the current request context. The returned map is a read-only snapshot
# of the map of query parameters in the context at the time this method was called.
public function queryParams() returns map<string[]> & readonly;
```

### Keywords

The `Ballerina.toml` file needs to include the following keywords for the mediation policies to work:

- **choreo-apim-mediation-policy**: This keyword is a mandatory keyword that is required to identify that the package is a mediation policy type.
- **choreo-apim-mediation-request-flow**: Specifies whether the policy applies to the request flow.
- **choreo-apim-mediation-response-flow**: Specifies whether the policy applies to the response flow.
- **choreo-apim-mediation-fault-flow**: Specifies whether the policy is applicable for the fault flow.

#### Policy name and description

The `Package.md` file contains information about the policy. Choreo uses this information to render the policy configuring UI. This file is written in Markdown format and should be structured as follows.

**Format:**

```
# <policy-name>


## Overview


<policy description>

```

**Example:**

```
# ValidateHeader


## Overview


This policy validates the request and response headers with the configured values.

```

#### Policy versioning

When it comes to policy versioning in Choreo or mediation dependencies, it is important to consider the major version changes in the Ballerina language. For example, transitioning from update 1 to update 2 requires a major version increment, which can introduce significant incompatibilities.

Therefore, to ensure compatibility, the recommended approach is to version the policy package in a manner that the major version gets upgraded when the Choreo/mediation dependency version is upgraded to a major version.  


# Assign Subscription Plans to APIs

API subscription plans allow API publishers to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security.

Choreo allows users with the administrator role to create, update, and delete subscription plans at the organization level. For instructions on creating subscription plans, see [Create API Subscription Plans](../../administer/create-api-subscription-plans.md).

Once created, Choreo allows API publishers to assign subscription plans to APIs, providing different levels of access based on user needs.

To assign subscription plans to an API, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to assign subscription plans.
3. In the left navigation menu, click **Manage** and then click **Subscription Plans**. This displays the subscription plans available for the component.
4. Enable the **Subscription Plan Status** toggle corresponding to the subscription plans you want to assign to the API.

    ![Enable toggle](../../assets/img/api-management/manage-api-traffic/enable-toggle.png)

5. Click **Save**.

When an API has subscription plans assigned to it, API consumers can select the plan that best fits their requirements during the subscription process. For details, see [Subscribe to an API with a Subscription Plan](./subscribe-to-an-api-with-a-subscription-plan.md)


# Subscribe to an API with a Subscription Plan

If an API has subscription plans assigned to it, API consumers can select the subscription plan that best fits their requirements at the time of subscribing to the API.

To subscribe to an API with a subscription plan, follow the steps given below:

1. Sign in to the [Choreo Developer Portal](https://devportal.choreo.dev).
2. In the Developer Portal header, click **Applications**.
3. On the **My Applications** page, click on the application you want to use to subscribe to an API.
4. In the left navigation menu, click **Subscriptions**. 
5. In the **Subscription Management** pane that opens, click **+ Add APIs**.
6. In the **Add APIs** pane that opens, select the API, API version, and subscription plan with which you want to subscribe to the API.
7. If the selected subscription plan requires administrator or API publisher approval to become active, click Request Subscription. Otherwise, click Add Subscription. If the selected subscription plan requires approval, your subscription will be shown as "Pending" until it is approved by an organization admin or the API publisher.

    !!! Note
        If the subscription plan requires administrator or API publisher approval to become active, the subscription status will be set to Pending Creation until it is reviewed and approved.

    ![Add subscription](../../assets/img/api-management/manage-api-traffic/add-subscription.png)

To verify that the subscription plan works as expected, follow the steps given below:

1. In the Developer Portal header, click **APIs**.
2. Search for the API you subscribed to and click **Try Out**.
3. Invoke the API until you exceed the request limit set in the subscription plan. You will see that the API throttles further requests once the limit is reached.

    ![Throttle response](../../assets/img/api-management/manage-api-traffic/throttle-response.png)




# API Rate Limiting

API rate limiting is a technique that allows you to control the rate of requests made to an API. Rate limiting helps 
prevent system overload and enhances API performance. When you limit the number of requests that can be made in a 
specific time frame, you can ensure that your API is available and responsive to all users while protecting it from 
malicious attacks.

This page walks you through the steps to enable rate limiting for your APIs via Choreo and also provides information on 
the rate-limiting options supported by Choreo.

## Enable rate limiting for an API

To enable rate limiting for an API, follow the steps given below: 

!!! note
     You can apply rate-limiting settings separately for each environment.

1. Sign in to the [Choreo Console](https://console.choreo.dev/). 
2. In the **Component Listing** pane, click on the component for which you want to apply rate limiting.
3. In the left navigation menu, click **Deploy**.
4. Go to the required environment card and click the view icon corresponding to the endpoint for which you want to apply rate limiting. 

    !!! info 
         If you are applying rate limiting for an API Proxy component, go to the required environment card, click the setting icon corresponding to **API Configuration**, and proceed to step 6.

5. In the **Endpoint Details** pane that opens, click the settings icon.
6. In the **Manage** section, click **Rate Limiting** to expand it.
7. Select a **Rate Limiting Level** depending on your requirement and click **Apply**.

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

By default, the APIs published in Choreo are visible to anyone who visits the Choreo Developer Portal. By default, Choreo sets the visibility of the API to `Public`. However, developers can control the visibility of their APIs by changing the default option to `Private` or `Restricted`. 

Visibility settings control users from viewing and modifying APIs. API visibility can be one of the following options:

 - **Public** : The API is **visible to all** in the developer portal.

 - **Private** : The API is visible to the **users who only sign in to the Developer Portal**.

 - **Restricted**: The API is **visible to only the user that has the roles that you specify**. This option helps developers to enforce fine-grained access control to the API.

## Change API visibility

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the REST API (Service) for which you want to control API visibility. 
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, select the required visibility setting from the **Visibility** list. 

    !!! note "Enable fine-grained role-based access control to the API"
         1. To enable fine-grained role-based access control to an API in the Developer Portal, select `Restricted` from the **API visibility** list. Once selected, you will see the roles available in your organization in the **Visible Roles** list. 
         2. Select any combination of roles. Only the users with the given roles can access the APIs through the Dev Portal. 
         3. Alternatively, You can create a new role and assign it to an API by following the steps below: 
             1. Click **+ Create New Role** in the list.
             2. Add the role name and description. 
             3. Click **Next**.
             4. Assign the relevant permissions to the new role.
             5. Click **Create**.
             6. Select the newly created role from the **Visible Roles** list.

6. Click **Save**.


# Documents

When an API consumer signs in to the Choreo Developer Portal to browse APIs, it is not sufficient to just have an API thumbnail along with the name and version of the API. An API consumer would expect to see more details about the API, such as the following:

 - A brief description of the API.
 - How to invoke the API.
 - The limitations/restrictions of the API.
 - Version history.

To provide such information that improves the overall visibility of the API, an API developer can add such documentation to an API before publishing it to the Developer Portal.

## Add documents to an API

To add documentation for an API, follow the steps given below.

1. Sign in to the [Choreo Console](https://console.choreo.dev/).

2. In the **Component Listing** pane, click on the component for which you want to add documents. 

3. In the left navigation menu, click **Manage** and then click **Documents**.

4. Specify a title for the document and provide the content in markdown syntax. 
   
5. Click **Add** to save the document.

Depending on the information you need to add to the API, you can add one or more documents.

You can also edit existing documents and delete documents if necessary.


# Lifecycle Management

API lifecycle management is an important aspect of API management. The API lifecycle consists of various states that an API passes through, from creation to retirement. In Choreo, there are six distinct lifecycle states: created, pre-released, published, blocked, deprecated, and retired.

By leveraging the various lifecycle states, API managers can optimize the development process and ensure that subscribers have access to the latest and most reliable APIs.

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

To change the lifecycle state of an API via the Choreo Console, follow the instructions given below:

!!! tip      
     You must have publishing privileges to manage the lifecycle states of a component.

1. Sign in to the Choreo Console.
2. In the **Component Listing** pane, click on the component for which you want to manage the lifecycle.
3. In the left navigation menu, click **Manage**, and then click **Lifecycle**.
4. In the **Lifecycle Management** pane, you will see the lifecycle state transition diagram indicating the current lifecycle state of the component. Just above the lifecycle state transition diagram, The possible lifecycle states you can apply to the component are displayed just above the lifecycle state transition diagram. Click on a required lifecycle state to apply it to the component. For example, if a component is in the **Created** state, you can click either **Pre-release** or **Publish**.


# Rename API Display Name

Choreo allows you to make one or more endpoints accessible through its service and integration components. These endpoints are published as individual APIs in Choreo, accessible via the Choreo Developer Portal. By default, Choreo assigns an API name by combining the component name and the endpoint name, resulting in the following format: `<component name>-<endpoint name>`. For example, if you create a component named `Ballerina Reading List,` the API is displayed as `Ballerina Reading List - GraphQL Reading List 591.`

Choreo provides you with the flexibility to personalize the display name of the API, enhancing its user-friendliness and readability. Once you modify the API display name within the Choreo Console, Choreo applies the change immediately. From there onwards, Choreo displays the published API by this name in the Choreo Developer Portal.

Follow the steps below to rename the API display name:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in. This opens the project home page.
2. In the **Component Listing** pane, click on the component for which you want to rename the API display name. This opens the **Overview** page of the component.
3. In the left navigation menu, click **Manage** and then click **API Info**.
4. On the **API Info** page that opens, click the **Developer Portal** tab.
5. Under **General Details**, specify an appropriate API display name in the **Name** field.
6. Click **Save**.

Now, you can view the updated API display name in the Choreo Developer Portal.


# OWASP Top 10

A set of rules enforcing OWASP security guidelines to prevent common vulnerabilities and ensure secure coding practices.
### ❌ owasp:api1:2023-no-numeric-ids

Use random IDs that cannot be guessed. UUIDs are preferred but any other random string will do.

---

### ❌ owasp:api2:2023-no-http-basic

Basic authentication credentials transported over network are more susceptible to interception than other forms of authentication, and as they are not encrypted it means passwords and tokens are more easily leaked.

---

### ❌ owasp:api2:2023-no-api-keys-in-url

API Keys are passed in headers, cookies, or query parameters to access APIs. Those keys can be eavesdropped, especially when they are passed in the URL, as logging or history tools will keep track of them and potentially expose them.

---

### ❌ owasp:api2:2023-no-credentials-in-url

URL parameters MUST NOT contain credentials such as API key, password, or secret.

---

### ❌ owasp:api2:2023-auth-insecure-schemes

There are many [HTTP authorization schemes](https://www.iana.org/assignments/http-authschemes/) but some of them are now considered insecure, such as negotiating authentication using specifications like NTLM or OAuth v1.

---

### ❌ owasp:api2:2023-jwt-best-practices

JSON Web Tokens RFC7519 is a compact, URL-safe, means of representing claims to be transferred between two parties. JWT can be enclosed in encrypted or signed tokens like JWS and JWE.

The [JOSE IANA registry](https://www.iana.org/assignments/jose/jose.xhtml) provides algorithms information.

RFC8725 describes common pitfalls in the JWx specifications and in
their implementations, such as:
- the ability to ignore algorithms, eg. `{"alg": "none"}`;
- using insecure algorithms like `RSASSA-PKCS1-v1_5` eg. `{"alg": "RS256"}`.
An API using JWT should explicit in the `description`
that the implementation conforms to RFC8725.
```
components:
  securitySchemes:
    JWTBearer:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |-
        A bearer token in the format of a JWS and conformato
        to the specifications included in RFC8725.
```

---

### ❌ owasp:api2:2023-short-lived-access-tokens

Using short-lived access tokens is a good practice, and when using OAuth 2 this is done by using refresh tokens. If a malicious actor is able to get hold of an access token then rotation means that token might not work by the time they try to use it, or it could at least reduce how long they are able to perform malicious requests.

---

### ❌ owasp:api4:2023-rate-limit

Define proper rate limiting to avoid attackers overloading the API. There are many ways to implement rate-limiting, but most of them involve using HTTP headers, and there are two popular ways to do that:

IETF Draft HTTP RateLimit Headers:. [https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers)/

Customer headers like X-Rate-Limit-Limit (Twitter: [https://developer.twitter.com/en/docs/twitter-api/rate-limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits) or X-RateLimit-Limit (GitHub: [https://docs.github.com/en/rest/overview/resources-in-the-rest-api](https://docs.github.com/en/rest/overview/resources-in-the-rest-api))

---

### ❌ owasp:api4:2023-rate-limit-retry-after

Define proper rate limiting to avoid attackers overloading the API. Part of that involves setting a Retry-After header so well meaning consumers are not polling and potentially exacerbating problems.

---

### ❌ owasp:api4:2023-array-limit

Array size should be limited to mitigate resource exhaustion attacks. This can be done using `maxItems`. You should ensure that the subschema in `items` is constrained too.

---

### ❌ owasp:api4:2023-string-limit

String size should be limited to mitigate resource exhaustion attacks. This can be done using `maxLength`, `enum` or `const`.

---

### ❌ owasp:api4:2023-integer-limit

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-limit-legacy

Integers should be limited to mitigate resource exhaustion attacks. This can be done using `minimum` and `maximum`, which can with e.g.: avoiding negative numbers when positive are expected, or reducing unreasonable iterations like doing something 1000 times when 10 is expected.

---

### ❌ owasp:api4:2023-integer-format

Integers should be limited to mitigate resource exhaustion attacks. Specifying whether int32 or int64 is expected via `format`.

---

### ❌ owasp:api8:2023-define-cors-origin

Setting up CORS headers will control which websites can make browser-based HTTP requests to your API, using either the wildcard "*" to allow any origin, or "null" to disable any origin. Alternatively you can use "Access-Control-Allow-Origin: https://example.com" to indicate that only requests originating from the specified domain (https://example.com) are allowed to access its resources.

More about CORS here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

---

### ❌ owasp:api8:2023-no-scheme-http

Server interactions must use the http protocol as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use the https or wss schemes instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api8:2023-no-server-http

Server interactions must not use the http:// as it's inherently insecure and can lead to PII and other sensitive information being leaked through traffic sniffing or man-in-the-middle attacks. Use https:// or wss:// protocols instead.

Learn more about the importance of TLS (over SSL) here: [https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

---

### ❌ owasp:api9:2023-inventory-access

Servers are required to use vendor extension x-internal set to true or false to explicitly explain the audience for the API, which will be picked up by most documentation tools.

---

### ❌ owasp:api9:2023-inventory-environment

Make it clear which servers are expected to run as which environment to avoid unexpected problems, exposing test data to the public, or letting bad actors bypass security measures to get to production-like environments.

---

### ⚠️ owasp:api3:2023-no-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-additionalProperties

By default JSON Schema allows additional properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `additionalProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api3:2023-no-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`.

---

### ⚠️ owasp:api3:2023-constrained-unevaluatedProperties

By default JSON Schema allows unevaluated properties, which can potentially lead to mass assignment issues, where unspecified fields are passed to the API without validation. Disable them with `unevaluatedProperties: false` or add `maxProperties`

---

### ⚠️ owasp:api4:2023-rate-limit-responses-429

OWASP API Security recommends defining schemas for all responses, even errors. A HTTP 429 response signals the API client is making too many requests, and will supply information about when to retry so that the client can back off calmly without everything breaking. Defining this response is important not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces. It also ensures your API/framework/gateway actually has rate limiting set up.

---

### ⚠️ owasp:api4:2023-string-restricted

To avoid unexpected values being sent or leaked, strings should have a `format`, RegEx `pattern`, `enum`, or `const`.

---

### ⚠️ owasp:api8:2023-define-error-validation

Carefully define schemas for all the API responses, including either 400, 422 or 4XX responses which describe errors caused by invalid requests.

---

### ⚠️ owasp:api8:2023-define-error-responses-401

OWASP API Security recommends defining schemas for all responses, even errors. The 401 describes what happens when a request is unauthorized, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ⚠️ owasp:api8:2023-define-error-responses-500

OWASP API Security recommends defining schemas for all responses, even errors. The 500 describes what happens when a request fails with an internal server error, so its important to define this not just for documentation, but to empower contract testing to make sure the proper JSON structure is being returned instead of leaking implementation details in backtraces.

---

### ℹ️ owasp:api7:2023-concerning-url-parameter

Using external resources based on user input for webhooks, file fetching from URLs, custom SSO, URL previews, or redirects can lead to a wide variety of security issues.

Learn more about Server Side Request Forgery [https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/](https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/).

---


# WSO2 API Design Guidelines

A guide detailing best practices for creating robust, scalable, and secure APIs, ensuring alignment with industry standards for optimal design.
### ❌ path-casing

Paths must be `kebab-case`, with hyphens separating words.

**Invalid Example**

`userInfo` must be separated with a hyphen.

```json
{
    "/userInfo": {
        "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user-info": {
       "post: }
       ....
}
```

---

### ❌ paths-no-file-extensions

Paths must not include `json` or `xml` file extensions.

**Invalid Example**

The path contains a `.json` extension. 

```json
{
    "/user.json": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ paths-no-http-verbs

Verbs such as `get`, `delete`, and `put` must not be included in paths because this information is conveyed by the HTTP method.

**Invalid Example**

The path contains the verb `get`. 

```json
{
    "/getUsers": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ❌ path-parameters-snake-case

Path parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the path parameter must not contain digits.

**Invalid Example**

The `name` property on line 9 (`userId`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "userId",
            "in": "path"
          }
        ]
      }
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users/{userId}": {
        "parameters": [
          {
            "schema": {
              "type": "integer"
            },
            "name": "user_id",
            "in": "path"
          }
        ]
      }
    }
  }
```

---

### ❌ query-parameters-snake-case

Query parameters must be `snake_case`, with each word separated by an underscore character and the first letter of each word lowercase. Also, the query parameter must not contain digits.

**Invalid Example**

The `name` property on line 8 (`user-Id`) must be separated by an underscore character and the `I` must be lowercase.

```json
{
   "parameters": [
     {
       "schema": {
         "type": "string"
       },
       "in": "query",
       "name": "user-Id"
     }
   ]
}
```

**Valid Example**

```json
{
    "parameters": [
      {
        "schema": {
          "type": "string"
        },
        "in": "query",
        "name": "user_id"
      }
    ]
 }
```

---

### ⚠️ resource-names-plural

Resource names should generally be plural. 

**Invalid Example**

```json
{
    "paths": {
      "/user": 
    }
  }
```

**Valid Example**

```json
{
    "paths": {
      "/users": 
    }
}
```

---

### ⚠️ paths-avoid-special-characters

Paths should not contain special characters, such as `$` `&` `+` `,` `;` `=` `?` and `@%`.

**Invalid Example**

The path contains an ampersand. 

```json
{
    "/user&info": {
       "post: }
       ....
}
``` 

**Valid Example**

```json
{
    "/user": {
       "post: }
       ....
}
```

---

### ℹ️ server-has-api

Server must have /api

---


# WSO2 Style Guidelines

A set of guidelines focused on enforcing uniformity in API style, including naming conventions, formatting, and documentation to ensure clarity and maintainability across all APIs.
### ❌ operation-operationId-valid-in-url

Operation IDs must not contain characters that are invalid for URLs.

**Invalid Example**

The `operationId` in this example includes a pipe and space, which are invalid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "invalid|operationID"
    }
  }
}
```

**Valid Example**

This `operationId` is valid for URLs.

```json
{
  "/users": {
    "get": {
      "operationId": "this-must-be-unique"
    }
  }
}
```

---

### ❌ path-declarations-must-exist

Path parameter declarations must not be empty.

**Invalid Example**

`/users/{}`

**Valid Example**

`/users/{userId}`

---

### ❌ paths-no-trailing-slash

Paths must not end with a trailing slash.

`/users` and `/users/` are separate paths. It's considered bad practice for them to differ based only on a trailing slash. It's usually preferred to not have a trailing slash.

**Invalid Example**

The `users` path ends with a slash.

```json
{
  "/users/": {
    "post": {}
  }
}
```

**Valid Example**

```json
{
  "/user": {
    "post": {}
  }
}
```

---

### ❌ server-lowercase

Server URLs must be lowercase. This standard helps meet industry best practices.

**Invalid Example**

The `url` property uses uppercase letters.

```json
{
  "servers": [
    {
      "url": "https://ACME.com/api"
    }
  ]
}
```

**Valid Example**

The `url` property is fully lowercase.

```json
{
  "servers": [
    {
      "url": "https://acme.com/api"
    }
  ]
}
```

---

### ❌ oas2-api-schemes

OpenAPI 2 host `schemes` reflect the transfer protocol of the API. 
Host schemes must be present and an array with one or more of these values: 
`http`, `https`, `ws`, or `wss`.

**Valid Example**

This example shows that host schemes are `http` and `https`.

```json
{
  "schemes": [
    "http",
    "https"
  ]
}
```


---

### ❌ array-items

Schemas with `type: array`, require a sibling `items` field.

**Recommended:** Yes

**Good Example**

```yaml
TheGoodModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
        items: {}
```

**Bad Example**

```yaml
TheBadModel:
  type: object
  properties:
    favoriteColorSets:
      type: array
      items:
        type: array
```

---

### ⚠️ contact-url

The `contact` object should have a valid organization URL. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "url": "https://acme.com",
     ... 
  },
```

---

### ⚠️ contact-email

The `contact` object should have a valid email. 

**Valid Example**

```json
{
  "contact": {
     ... ,
     "email": "support.contact@acme.com"
  },
```

---

### ⚠️ info-contact

The `info` object should include a `contact` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "contact": {
      "name": "ACME Corporation",
      "url": "https://acme.com",
      "email": "support.contact@acme.com"
    }
  }
}
```

---

### ⚠️ info-description

The `info` object should have a `description` object.

**Valid Example**

```json
{
  "info": {
     ... ,
     "description": "This describes my API."
  }
}
```

---

### ⚠️ info-license

The `info` object should have a `license` object.

**Valid Example**

```json
{
  "info": {
    ... ,
    "license": {
      "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
      "url": "https://creativecommons.org/licenses/by-sa/4.0/"
    }
  }
}
```

---

### ⚠️ license-url

The `license` object should include a valid url.

**Valid Example**

```json
{
  "license": {
    "name": "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
    "url": "https://creativecommons.org/licenses/by-sa/4.0/"
  }
}
```

---

### ⚠️ no-eval-in-markdown

Markdown descriptions should not contain [`eval()` functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval),
which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. eval()"
  }
}
```

---

### ⚠️ no-script-tags-in-markdown

Markdown descriptions should not contain `script` tags, which pose a security risk.

**Invalid Example**

```json
{
  "info": {
    ... ,
    "description": "API for users. <script>alert(\"You are Hacked\");</script>"
  }
}
```

---

### ⚠️ openapi-tags-alphabetical

Global tags specified at the root OpenAPI Document level should be in alphabetical order based on the `name` property.

**Invalid Example**

```json
{
  "tags":[
    {
      "name":"Z Global Tag"
    },
    {
      "name":"A Global Tag"
    }
  ]
}
```

**Valid Example**

```json
{
  "tags":[
    {
      "name":"A Global Tag"
    },
    {
      "name":"Z Global Tag"
    }
  ]
}
```

---

### ⚠️ openapi-tags

At least one global tag should be specified at the root OpenAPI Document level.

**Valid Example**

```json
{
  "tags":[
    {
      "name":"Global Tag #1"
    },
    {
      "name":"Global Tag #2"
    }
  ]
}
```

---

### ⚠️ operation-description

Each operation should have a description.

**Valid Example**

```json
{
  "get": {
    "description": "Get a list of users."
  }
}
```

---

### ⚠️ operation-operationId

All operations should have an `operationId`.

**Valid Example**

```json
{
  "get": {
    "summary": "Get users",
    "operationId": "get-users"
  }
}
```

---

### ⚠️ operation-tags

At least one tag should be defined for each operation.

**Valid Example**

```json
{
  "get": {
    "tags": ["Users"]
  }
}
```

---

### ⚠️ contact-name

The `contact` object should have an organization name.

**Valid Example**

```json
{
  "contact": {
    "name": "ACME Corporation"
  }
}
```

---

### ⚠️ path-keys-no-trailing-slash

Path keys should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "/users/": {
  }
}
```

**Valid Example**

```json
{
  "/users": {
  }
}
```

---

### ⚠️ path-not-include-query

Paths should not include `query` string items. Instead, add them as parameters with `in: query`.

**Invalid Example**

```json
{
  "/users/{?id}": {
  }
}
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ⚠️ tag-description

Tags defined at the global level should have a description.

**Valid Example**

```json
{
  "tags": [
    {
      "name": "Users",
      "description": "End-user information"
    }
  ]
}
```

---

### ⚠️ api-servers

A server should be defined at the root document level. This can be localhost, a development server, or a production server.

**Valid OpenAPI V3 Example**

```json
{
  "servers": [
    {
      "url": "https://staging.myprodserver.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://myprodserver.com/v1",
      "description": "Production server"
    }
  ]
}
```

**Valid OpenAPI V2 Example**

```json
{
  "host": "myprodserver.com",
  "basePath": "/v2",
  "schemes": [
    "https"
  ]
}
```

---

### ⚠️ server-trailing-slash

Server URLs should not end in forward slashes. This is a best practice for working with web tooling, such as mock servers, code generators, application frameworks, and more.

**Invalid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5/"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```

---

### ⚠️ server-not-example

Server URLs must not direct to example.com. This helps ensure URLs 
are valid before you distribute your API document.

**Invalid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://example.com"
    }
  ]
}
```

**Valid Example**

```json
{
  "servers": [
    {
      ... ,
      "url": "https://api.openweathermap.org/data/2.5"
    }
  ]
}
```


---

### ⚠️ parameter-description

All `parameter` objects should have a description.

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "integer"
      },
      ... ,
      ... ,
      "description": "The number of days to include in the response."
    }
  ]
}
```


---

### ⚠️ oas2-anyOf

The `anyOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "anyOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas2-oneOf

The `oneOf` keyword is not supported in OAS2. Only `allOf` is supported.

**Invalid Example**

```json
{
  "schema": {
    "oneOf": [
      {
        "properties": {
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string"
          }
        }
      },
      {}
    ]
  }
}
```

**Valid Example**

```json
{
  "schema": {
    "type": "object",
    "properties": {
      "firstName": {
        "type": "string"
      },
      "lastName": {
        "type": "string"
      }
    }
  }
}
```


---

### ⚠️ oas3-examples-value-or-externalValue

The `examples` object should include a `value` or `externalValue` field, but cannot include both.

**Invalid Example**

This example includes both a `value` field and an `externalValue` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      },
      "externalValue": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```

**Valid Example**

This example includes only a `value` field.

```json
{
  "examples": {
    "example-1": {
      "value": {
        "id": "string",
        "name": "string"
      }
    }
  }
}
```


---

### ⚠️ path-parameters-on-path-only

Path parameters should be defined on the path level instead of the operation level.

**Invalid Example**

The `user_id` path parameter on line 8 should not be included with the `patch` operation.

```json
{      
  "patch": {
    "parameters": [
      {
        "schema": {
          "type": "integer"
        },
        "name": "user_id",
        "in": "path"
      }
    ]
  }
}
```

**Valid Example**

The `user-id` path parameter is correctly located at the path level.

```json
{
  "paths": {
    "/users/{userId}": {
      "parameters": [
        {
          "schema": {
            "type": "integer"
          },
          "name": "user_id",
          "in": "path"
        }
      ]
    }
  }
}
```

---

### ⚠️ paths-no-query-params

Paths should not have query parameters in them. They should be defined separately in the OpenAPI.

**Invalid Example**

```json
{
  "/users/{?id}": {
```

**Valid Example**

```json
{
  "parameters": [
    {
      "schema": {
        "type": "string"
      },
      "name": "id",
      "in": "path",
      "required": true,
      "description": "User's ID"
    }
  ]
}
```

---

### ℹ️ operation-singular-tag

Operation should not have more than a single tag.

---


# About API Policies

API policies are units of business logic that you can apply to modify the flow of API invocations. 

You can apply a policy to alter the  `Request`, `Response`, or `Error` flow of an API invocation before it reaches the backend or the client. For example, you can add a policy to the response flow to transform the payload from JSON to XML and add a header to the response. 

## Inbuilt mediation policies

Choreo supports a set of inbuilt mediation policies that can handle common API transformation and mediation tasks. These policies run within a single mediation service, making it straightforward to implement and manage complex mediation logic. The following inbuilt policies are available in Choreo:

- **JSON to XML**: Transforms a JSON payload in a request or response into XML format. This policy is applicable only to JSON payloads in mediation flows. Applying it to a non-JSON payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to XML.
- **XML to JSON**: Converts an XML payload in a request or response into JSON format. This policy is applicable only to XML payloads in mediation flows. Applying it to a non-XML payload terminates the flow. This policy cannot be used more than once on the same resource because the payload will already be converted to JSON.
- **Remove Query Parameter**: Removes specified query parameters from a request. You can use this policy multiple times to remove different parameters. Attempting to remove a non-existent parameter has no effect. If the parameter exists, it will be removed; otherwise, the request proceeds as usual.
- **Remove Header**: Removes specified headers from a request or response. You can attach this policy multiple times to remove multiple headers. The header name must be static, but you can use placeholders to configure different values for different environments. For example, `${headerName}`.
- **Add Query Parameter**: Adds query parameters to a request. You can attach this policy multiple times to add various parameters. Adding the same parameter multiple times creates an array of values. The parameter name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${fooValue}`.
- **Add Header**: Adds headers to a request or response. If the same header is added multiple times, values are appended rather than overwritten. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`.
- **Set Header**: Sets headers in a request or response, overwriting any existing values. You can attach this policy multiple times to set multiple headers. Each time the same header is set, it replaces the previous value. The header name and value must be static, but you can use placeholders to configure different values for different environments. For example, `${authzHeaderValue}`. 
- **Rewrite Resource Path**: Modifies the resource path of an HTTP request by replacing the original path with a new relative path. You can apply this policy multiple times, but only the last instance will take effect. The new path must be static, but you can use placeholders to configure different values for different environments. For example, `${myResourcePath}`.
- **Log Message**: Logs the payload and headers of a request or response. Attaching this policy multiple times results in duplicate log entries. By default, headers and payloads are not logged. To log them, you can enable `Log Headers` and `Log Payload` parameters. To exclude specific headers when logging, you can use the `Excluded Headers` parameter, which takes a comma-separated list of header names. An error will occur if payload logging is enabled but the payload cannot be read.

These inbuilt mediation policies provide flexibility to manage API requests and responses, allowing for custom transformations and logic without requiring custom code.

For details on attaching and managing one or more policies to an API proxy component implementation via the Choreo Console, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

For details on applying advanced settings on mediation policies, see [Apply Advanced Settings on Mediation Policies](../api-policies/apply-advanced-settings-on-mediation-policies.md).


# Apply Advanced Settings on Mediation Policies

Advanced settings for mediation policies are available for proxy components with an attached mediation policy. For details on attaching a mediation policy to a proxy component, see [Attach and Manage Policies](../api-policies/attach-and-manage-policies.md).

The approach to applying advanced settings depends on whether the proxy component is deployed or not.

## Mediation policy advanced settings

| **Setting**                     | **Purpose**    | **How to apply**  | **Impact**   |
|---------------------------------|----------------|-------------------|--------------|
| **HTTP version**                | By default, Choreo supports HTTP 1.1. If necessary, you can change to HTTP 1.0 or HTTP 2.0. | Specify the required HTTP version in the **Advanced Settings** field. <br> ![HTTP version setting](../../assets/img/api-management/api-policies/advanced-settings/http-version-setting.png) | The mediation application will use the specified HTTP version when interacting with backend services.  |
| **Hostname verification**       | Choreo enables hostname verification by default when using mTLS. You can disable it if necessary. | Set the `verifyHostname` parameter to `false` in the **Advanced Settings** field. <br> ![Hostname verification setting](../../assets/img/api-management/api-policies/advanced-settings/hostname-verification-setting.png)   | Hostname verification will be skipped during mTLS interactions.                              |
| **Minimum evictable idle time** | Determines how long (in seconds) an outgoing connection remains idle before eviction. The default is 300 seconds. | Set the required idle time in the **Advanced Settings** field. <br> ![Minimum evictable idle time setting](../../assets/img/api-management/api-policies/advanced-settings/minimum-evictable-idle-time-setting.png)          | Idle connections will be closed and evicted after the defined period.                    |
| **Detailed access log**         | By default, logs related to the mediation application are generated and can be viewed as [runtime logs](../../monitoring-and-insights/view-logs.md#runtime-logs). You can disable these logs if necessary.      | Set the `detailedAccessLog` parameter in the **Advanced Settings** field. <br> ![Detailed access log setting](../../assets/img/api-management/api-policies/advanced-settings/detailed-access-log-setting.png)  | Logs related to the mediation application will not be generated.    |

## Configure advanced settings for a proxy component

To configure advanced settings for a proxy component with an attached mediation policy, follow these steps:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to configure advanced settings.
3. In the left navigation menu, click **Deploy**.
4. Depending on the deployment status of the proxy component, follow one of these steps:
   - If the proxy component is not deployed, go to the **Set Up** card and click **Configure & Deploy**. 
   - If the proxy component is already deployed, go to the respective environment card depending on the environment you want to apply advanced settings, and then click the **Environment Variables** icon.
5. In the **Configurations** pane that opens, expand the **Defaultable Configurables** section. 
6. In the **Advanced Settings** field, configure the necessary settings as described in the [Mediation policy advanced settings](#mediation-policy-advanced-settings) section.
7. Click **Save & Deploy**.


# Attach and Manage Policies

You can easily attach one or more policies to an API proxy component implementation via the Choreo Console. If necessary, you can also rearrange or swap the policies you attach.

In Choreo, when you attach a mediation policy to a proxy, the deployment is a two-step process.

1. Deployment initiation: 

     If the component to which you want to attach the mediation policy is new, the system creates and commits a new repository with the mediation service code based on the attached policy. This new service is called the mediation application. 

2. Deploying the API:

     Once the deployment initiation is complete, you can specify configuration values if any, and proceed to deploy. Choreo builds the generated mediation application and pushes the Docker image to the Docker registry. Finally, Choreo deploys the mediation application with the API Proxy.

When a mediation policy is attached to a specific flow, the API invocation undergoes the following behavioral modification:
 
 ![Request/Response flow](../../assets/img/api-management/api-policies/request-response-flow.png)

 - In the request path, the requests that pass through the gateway reach the relevant component, and Choreo executes any attached policies to the resource's request path before sending it to the backend. 

- In the response path, the mediation component receives response messages from the backend, and Choreo executes any mediation policies attached to the `Response` flow or the `Error` flow. Then the response is forwarded to the client.

- If an error occurs during the execution of policies or due to an internal error, Choreo executes the `Error` flow and sends an error response to the client.

## Attach a policy

To attach a policy to the `Request`, `Response`, or `Error` flow of a REST API proxy, follow the steps given below:

1. Sign in to the [Choreo Console](https://console.choreo.dev).
2. In the **Component Listing** pane, click on the REST API Proxy component for which you want to attach a policy.
3. In the left navigation menu, click **Develop** and then click **Policies**.
4. From the list of resources, expand the resource to which you want to attach the policy. 
5. Click **Attach Mediation Policy** in the respective flow for which you want to attach a policy.
6. In the **Policy List** pane that opens, click on a required policy to view its details.
7. If the attached policy requires parameter configuration, on the policy pane enter the appropriate values and configure the parameters. To make a parameter a configurable variable, input the value in the `${<variableName>}` format. For example, you can use `${name}` as an example.

    ![Configure parameters](../../assets/img/api-management/api-policies/configure-parameters.png)
 
8. To attach the policy, click **Add**.

After attaching an API Policy, it is necessary to deploy the API for the policy to become active within its corresponding flow. 
To deploy the API follow the steps below: 

9. In the left navigation menu, click **Deploy** and then click **Configure & Deploy**. Choreo performs the mediation application generation step and opens the **Configure & Deploy** pane.

10. In the **Configure & Deploy** pane, if you have any configurable variables that require values, specify appropriate values for them.

     ![Save and deploy values](../../assets/img/api-management/api-policies/save-and-deploy.png)

11. Click **Save & Deploy**.

## Refresh mediation policies

Choreo selectively generates and builds the mediation application code during component deployment depending on specific changes. These changes include:

 - Addition, deletion, or modification of API resources.
 - Attachment, removal, or editing of API mediation policies.
 - Endpoint modifications via the **Develop** page.
 - Initial configuration or removal of backend endpoints or mutual TLS certificates.

If none of the above changes occur during deployment, Choreo skips the code generation and build process of the mediation application.

!!! info
    - If you want to enforce the code generation and build process of the mediation application in instances where the specified changes do not take place, you must turn on the **Refresh Mediation Policies** toggle when you configure and deploy the component. 
    - It is useful to enable **Refresh Mediation Policies** when you want to incorporate the latest Ballerina patches for your generated mediation application. However, this can result in longer deployment times.

## Implement an API policy

Choreo allows you to implement an API policy as a Ballerina project and attach it to an API proxy component. 

!!! info
    Supported Ballerina version: 2201.5.5 

To implement a policy, follow the steps given below: 

### Prerequisites

1. Set up [ Ballerina 2201.5.5](https://ballerina.io/downloads/swan-lake-release-notes/swan-lake-2201.5.5).
2. Open the `~/.ballerina/settings.toml` file and ensure you have configured an access token to Ballerina Central. If you have not configured an access token, follow the steps given below to configure one: 
    1. Generate a token via [https://central.ballerina.io/dashboard?tab=token](https://central.ballerina.io/dashboard?tab=token).
    2. Download the generated `Settings.toml` file and copy it to your local `~/.ballerina` directory.
    
Alternatively, you can set the access token via the `BALLERINA_CENTRAL_ACCESS_TOKEN` environment variable.

``` 
export BALLERINA_CENTRAL_ACCESS_TOKEN=<access-token> 
```

### Step 1: Initialize a Ballerina project

Choreo provides a template to initialize a mediation policy project with all the required configurations. The mediation policy project will be created as a Ballerina project.

To create a Ballerina project for the mediation policy using `mediation.template` as the project template, issue the following command:  
   
**Format:**

```
    bal new -t choreo/mediation.template:1.0.0 <policy-name> 
```
    
**Example:**

```
    bal new -t choreo/mediation.template:1.0.0 validateHeader 
```
 The Ballerina project that is created should have the following content: 

![Ballerina project](../../assets/img/api-management/api-policies/ballerina-project.png)

Depending on your requirement, you can modify the `Ballerina.toml` and the `Package.md` files of the generated project. For example, you can update the org, package, package version, API documentation content, keywords, etc.

!!! note
    To successfully publish to Ballerina Central, make sure you update the `org` value to your organization name.

```
     [package]
        org = "starkindustries"
        name = "validateHeader"
        version = "1.0.0"
        export = ["validateHeader"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
```

### Step 2: Implement the policy

In this step, you will implement the policy. 

Let's assume you want to implement a policy to validate an incoming header in the request and the response. 

- **Request path**: If the request header is not present or if the validation fails, you want to log an error and return a `403 Bad Request` response to the client.
- **Response path**: You want to log a message to indicate whether the request is valid or not.

To implement the policy, open the `policy.bal` file in the Ballerina project and update the generated policy stubs(i.e., request, response, or fault) appropriately. 

The following sections walk you through sample implementations for the **Request** and **Response** stubs:

#### Request flow

The following is a sample implementation for the request flow:
 
```ballerina
@mediation:RequestFlow
public function validateRequestHeader(mediation:Context ctx, http:Request req, string headerName, string headerValue) returns http:Response|false|error|() {
   string|http:HeaderNotFoundError header = req.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return generateResponse(message, http:STATUS_BAD_REQUEST);
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return generateResponse(validationFailedMessage, http:STATUS_BAD_REQUEST);
    }
    log:printInfo("Header validation successful");
    return ();
};
    
function generateResponse(string message, int statusCode) returns http:Response {
    http:Response response = new();
    response.setTextPayload(message); 
    response.statusCode = statusCode;
    return response;
}

```

#### Response flow

The following is a sample implementation for the response flow:

```ballerina
@mediation:ResponseFlow
public function validateResponseHeader(mediation:Context ctx, http:Request req, http:Response res, string headerName, string headerValue) returns http:Response|false|error|() { 
   string|http:HeaderNotFoundError header = res.getHeader(headerName);
   if (header is http:HeaderNotFoundError) {
    string message = string `Header ${headerName} is not found`;
    log:printError(message);
    return ();
   }
   if (header != headerValue) {
    string validationFailedMessage = string `Header validation failed. Expected ${headerValue} but found ${header}`;
    log:printError(validationFailedMessage);
    return ();
   }
   return ();
}

```

#### Fault flow

In this guide, you are not going to make any changes to the `Fault` flow. Therefore, you can remove the `Fault` flow stub from the `policy.bal` file.

!!! note 
    The  **@mediation:RequestFlow**, **@mediation:ResponseFlow**, and **@mediation:FaultFlow** annotations are bound with the keywords in the `Ballerina.toml`. Therefore, the changes you make to the policy stubs should reflect in the `Ballerina.toml` file. For example, if the policy is applicable only on the request and response paths, you can remove the  **@mediation:FaultFlow** annotation from the policy. Then, you **MUST** also remove the **choreo-apim-mediation-fault-flow** keyword from the generated `Ballerina.toml` file. If you do not do so, the Ballerina compiler will show an error at compile time.

#### Publish as a private custom policy
 
 Choreo supports publishing a policy as a private custom policy. Publishing a policy as a private custom policy makes the policy inaccessible outside of the organization. To publish a policy as a private custom policy, change the visibility to `private` prior to pushing the package to Ballerina Central as follows:

 1. Open the `Ballerina.toml` file of your policy. 
 2. Set the visibility to **private** by adding the configuration `visibility="private"`. For example:

     ```
     [package]
        org = "orgName"
        name = "packageName"
        version = "1.0.2"
        export = ["packageName"]
        distribution = "2201.5.5"
        keywords = ["choreo-apim-mediation-policy","choreo-apim-mediation-request-flow","choreo-apim-mediation-response-flow","choreo-apim-mediation-fault-flow"]
        visibility = "private"
     ```

 3. Package and publish your policy to Ballerina Central.     

#### Best practices 

When implementing a policy, it is essential to follow best practices to ensure efficiency and maintainability. Here are some recommended best practices to follow:

- Organize the source code within the default module of the package. Do not add any additional modules.
- A policy implementation can contain any combination of flows. A generated project contains stubs for all three flows: `Request`, `Response`, and `Fault`. You can remove any stub that you do not require. For example, when you create a policy that re-writes the resource paths, you can remove the `Response` and `fault` stubs. 
- The HTTP request/response objects and context record parameters gets passed as references to the policy functions. Therefore, the changes you make to these values persist throughout the policy execution and are propagated to subsequent policies. This behavior allows the request and response objects to accumulate transformations applied by attached policies.
- Familiarize yourself with the different return types of policy flows. The following return types are unmodifiable:
    - **http:Response** - Returns an HTTP response when you terminate the mediation flow prematurely. For example,  in the in-flow sequence, the mediation sequence terminates before calling the backend. The mediation policy then sends an HTTP response to the client.
    - **false** - Returns `false` if you want to terminate the mediation sequence with a predefined response (on the Choreo side).
    - **error** - Returns an error if you want to terminate the mediation flow and transfer control to the fault flow. The fault flow would then construct an error response and send it to the client.
    - **()** - Returns () to signal the successful completion of the policy. Once the proxy has completed executing the policy, it starts to execute the next policy in the sequence.

### Step 3: Publish the policy

Once you implement a policy, you must publish it to Ballerina Central. 

When you attach a policy and deploy an API, Choreo pulls the necessary packages from Ballerina Central and bundles them into the mediation application under the hood. Therefore to use policies in your APIs, you must publish them as public packages. 

To publish the policy, follow the steps given below:

1. To package the policy before you publish it to Ballerina Central, issue the following command:
    ``` 
        bal pack 
    ```
2. To publish the package to Ballerina Central, issue the following command:

    ``` 
        bal push 
    ```

Once you publish the package, it will appear as follows in the policy list:

![Published policy](../../assets/img/api-management/api-policies/published-policy.png)

### Write unit tests

You can write unit tests to test policy functions in a manner similar to how you write unit tests for a regular [Ballerina function](https://ballerina.io/learn/test-ballerina-code/test-a-simple-function/). 

The following is a sample unit test for the `validateRequestHeader` function:

```
import ballerina/http;
import choreo/mediation;
import ballerina/test;


@test:Config {}
public function testRequestHeaderValidationFailure() {
  http:Request req = new;
  http:Response|false|error|() result = validateRequestHeader(createContext("get", "/test"), req, "testHeader", "test");


  if !(result is http:Response) {
    test:assertFail("Expected http:Response, found " + (typeof result).toString());
  }


  test:assertEquals(result.statusCode, http:STATUS_BAD_REQUEST, "Status code mismatch");
}


function createContext(string httpMethod, string resPath) returns mediation:Context {
   mediation:ResourcePath originalPath = checkpanic mediation:createImmutableResourcePath(resPath);
   mediation:Context originalCtx =
               mediation:createImmutableMediationContext(httpMethod, originalPath.pathSegments(), {}, {});
   mediation:ResourcePath mutableResPath = checkpanic mediation:createMutableResourcePath(resPath);
   return mediation:createMutableMediationContext(originalCtx, mutableResPath.pathSegments(), {}, {});
}

```

The policy function modifies the same request/response/context instance that you pass to it. You can check the request/response/context instance after calling the policy function to verify changes.

### Glossary

Here are some of the common terms used when working with policies in Choreo:

#### mediation:Context

The mediation context is used to pass parameters between policies. It is created per request and you can access it in any of the flows. For example, if a correlation ID needs to be set to the request, you can set it in the context of the request flow and access it in the response or fault flow. 

The mediation context can include the following functions:

```
# Retrieves the value for the specified key.   
public function get(string name) returns anydata;


# Stores the provided key-value pair. If a mapping exists for the key, the value is overwritten.
public function put(string name, anydata value);


# Removes the entry mapped by the specified key and returns the removed value.
public function remove(string name) returns anydata;


# Retrieves the value for the specified key. If there is no mapping for the key, return the specified
public function getOrDefault(string name, anydata default) returns anydata;


# Checks whether a mapping exists for the specified key.
public function hasKey(string name) returns boolean;


# Returns the `mediation:Context` instance which captured the initial contextual information of the resource,
# before the mediation flow was invoked. Calling this on an original `mediation:Context` object will return itself.
public function originalContext() returns Context;


# The HTTP method of the resource method
public function httpMethod() returns string;


# Retrieves an instance of `mediation:ResourcePath` which is an API for contextual information on the resource path
# of this resource. It also contains methods for modifying the resource path as the user sees fit. This resource
# path is the same path used by the mediation service for deriving the backend endpoint's resource to invoke.
# Therefore, the default behavior of the mediation service is to invoke a resource in the backend endpoint which
# has the same relative resource path as the corresponding mediation service resource.
public function resourcePath() returns ResourcePath;


# Sets the given `mediation:ResourcePath` instance as the resource path of this context.
public function setResourcePath(ResourcePath path);


# Adds a mapping between a path param name and a resolved value for it. There need not be a path parameter in the
# resource path by the name specified in `name` for one to use this method. On its own, the path param values have
# no bearing on the resource path.
public function addPathParamValue(string name, PathParamValue value);


# Returns the collection of resolved values for the path parameters in this particular context, mapped
# by the parameter name.
public function resolvedPathParams() returns map<PathParamValue> & readonly;


# Removes the resolved path parameter value which maps to the specified name.
public function removePathParamValue(string name);


# Adds a query parameter to the request to be sent to the backend. If there is already a query parameter by
# with the same name, the new value will be appended to it, making it an array.
public function addQueryParam(string name, string value);


# Removes the specified query parameter from the request. If the value of the parameter is an array, the whole
# array will be removed.
public function removeQueryParam(string name);


# Retrieves a map of all the query parameters in the current request context. The returned map is a read-only snapshot
# of the map of query parameters in the context at the time this method was called.
public function queryParams() returns map<string[]> & readonly;
```

### Keywords

The `Ballerina.toml` file needs to include the following keywords for the mediation policies to work:

- **choreo-apim-mediation-policy**: This keyword is a mandatory keyword that is required to identify that the package is a mediation policy type.
- **choreo-apim-mediation-request-flow**: Specifies whether the policy applies to the request flow.
- **choreo-apim-mediation-response-flow**: Specifies whether the policy applies to the response flow.
- **choreo-apim-mediation-fault-flow**: Specifies whether the policy is applicable for the fault flow.

#### Policy name and description

The `Package.md` file contains information about the policy. Choreo uses this information to render the policy configuring UI. This file is written in Markdown format and should be structured as follows.

**Format:**

```
# <policy-name>


## Overview


<policy description>

```

**Example:**

```
# ValidateHeader


## Overview


This policy validates the request and response headers with the configured values.

```

#### Policy versioning

When it comes to policy versioning in Choreo or mediation dependencies, it is important to consider the major version changes in the Ballerina language. For example, transitioning from update 1 to update 2 requires a major version increment, which can introduce significant incompatibilities.

Therefore, to ensure compatibility, the recommended approach is to version the policy package in a manner that the major version gets upgraded when the Choreo/mediation dependency version is upgraded to a major version.  


# Assign Subscription Plans to APIs

API subscription plans allow API publishers to control and manage access to APIs. These plans define the rules and limitations on how clients can interact with APIs, ensuring efficient resource utilization and robust security.

Choreo allows users with the administrator role to create, update, and delete subscription plans at the organization level. For instructions on creating subscription plans, see [Create API Subscription Plans](../../administer/create-api-subscription-plans.md).

Once created, Choreo allows API publishers to assign subscription plans to APIs, providing different levels of access based on user needs.

To assign subscription plans to an API, follow the steps given below: 

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. In the **Component Listing** pane, click on the component for which you want to assign subscription plans.
3. In the left navigation menu, click **Manage** and then click **Subscription Plans**. This displays the subscription plans available for the component.
4. Enable the **Subscription Plan Status** toggle corresponding to the subscription plans you want to assign to the API.

    ![Enable toggle](../../assets/img/api-management/manage-api-traffic/enable-toggle.png)

5. Click **Save**.

When an API has subscription plans assigned to it, API consumers can select the plan that best fits their requirements during the subscription process. For details, see [Subscribe to an API with a Subscription Plan](./subscribe-to-an-api-with-a-subscription-plan.md)


# Subscribe to an API with a Subscription Plan

If an API has subscription plans assigned to it, API consumers can select the subscription plan that best fits their requirements at the time of subscribing to the API.

To subscribe to an API with a subscription plan, follow the steps given below:

1. Sign in to the [Choreo Developer Portal](https://devportal.choreo.dev).
2. In the Developer Portal header, click **Applications**.
3. On the **My Applications** page, click on the application you want to use to subscribe to an API.
4. In the left navigation menu, click **Subscriptions**. 
5. In the **Subscription Management** pane that opens, click **+ Add APIs**.
6. In the **Add APIs** pane that opens, select the API, API version, and subscription plan with which you want to subscribe to the API.
7. If the selected subscription plan requires administrator or API publisher approval to become active, click Request Subscription. Otherwise, click Add Subscription. If the selected subscription plan requires approval, your subscription will be shown as "Pending" until it is approved by an organization admin or the API publisher.

    !!! Note
        If the subscription plan requires administrator or API publisher approval to become active, the subscription status will be set to Pending Creation until it is reviewed and approved.

    ![Add subscription](../../assets/img/api-management/manage-api-traffic/add-subscription.png)

To verify that the subscription plan works as expected, follow the steps given below:

1. In the Developer Portal header, click **APIs**.
2. Search for the API you subscribed to and click **Try Out**.
3. Invoke the API until you exceed the request limit set in the subscription plan. You will see that the API throttles further requests once the limit is reached.

    ![Throttle response](../../assets/img/api-management/manage-api-traffic/throttle-response.png)


