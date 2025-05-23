Here's a summary of the provided content, maintaining the headings for organization:

# Test APIs with Choreo API Chat

Choreo API Chat simplifies API testing by allowing you to interact with your APIs using natural language. This eliminates the need for manual test scenario creation and concerns about JSON payload accuracy. It supports REST API Proxy and Service components with REST endpoints. You can test APIs by signing into Choreo Console, selecting a component, navigating to the API Chat pane, and entering queries in natural language.

## Prerequisites
- A REST API Proxy component or a Service component that exposes a REST API with a valid OpenAPI specification. 

## Test your APIs
- Sign in to the Choreo Console.
- Select the component you want to test.
- On the left navigation, click **Test** and then click **API Chat**. This opens the **API Chat** pane.
- Enter your query in natural language and execute it. 

# Test APIs with cURL

Choreo allows you to use cURL commands generated by Choreo. To test your API method follow the steps below:

1. Sign in to the [Choreo Console](https://console.choreo.dev/).
2. Select the component you want to test.
3. Click **Test** in the left navigation menu and then click **cURL**.
4. Select the environment from the drop-down list.
5. Select an appropriate HTTP method from the **Method** list.
6. Add the necessary parameters for the API method in the **Parameters** tab.
7. Add the required header values in the **Headers** tab.
8. Select the message body type to invoke the API method in the **Body** tab.
9. Copy the generated cURL command.
10. Use the copied cURL command via a cURL client to test your API method.

# Test Components with Test Runner

Test Runner simplifies automated testing of components deployed in Choreo, enabling developers to evaluate applications in various setups. Tests can be created using languages like Go, Java, JavaScript, and Python, or by using a Dockerfile with test scripts or Postman Collections.

## Prerequisites
- Create an organization in Choreo Console.
- Fork the Choreo examples repository.

## Create a test runner component using a buildpack

1.  Sign in to the Choreo Console and navigate to the project home page.
2.  Click **+Create** in the **Component Listing** section.
3.  Click the **Test Runner** card.
4.  Connect a Git Repository.
5.  Select a buildpack based on the language of your choice.
6.  Enter a display name, unique name, and description for the test runner component.
7.  Click **Create**. 

## Build and deploy the test runner component to execute the tests

1.  In the left navigation menu, click **Build**.
2.  In the **Builds** pane, click **Build Latest**.
3.  On the left navigation, click **Deploy**.
4.  In the **Set Up** card, click **Deploy** to deploy the test runner component.
5.  Once the deployment is successful, click **Execute** in the left navigation menu.
6.  Select the environment from the environment list and click **Run Now** to trigger a test execution.
7.  Once the execution is completed it is listed on the execution page. 

# Test GraphQL Endpoints via the GraphQL Console

Choreo offers a GraphQL Console for testing GraphQL endpoints of Service components. It uses OAuth 2.0 for security and generates test keys.

1.  Sign in to the [Choreo Console](https://console.choreo.dev/).
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu and then click **Console**.
4.  In the **GraphQL Console** pane, select the environment from the drop-down list.
5.  Select the required endpoint from the **Endpoint** list.
6.  If the **Network Visibilities** of the endpoint contains **Organization**, click on **Generate URL** to generate a temporary test URL that will be active for 15 minutes.
7.  Enter the API path and the query or mutation you want to test.
8.  Click the play icon.

# Test REST Endpoints via the OpenAPI Console

Choreo provides an OpenAPI Console for testing REST endpoints, securing them with OAuth 2.0 and generating test keys.

1.  Go to the [Choreo Console](https://console.choreo.dev/) and log in.
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu, then select **Console**.
4.  In the **OpenAPI Console** pane, select the desired environment from the drop-down menu.
5.  Choose the endpoint you want to test from the **Endpoint** list.
6.  If the **Network Visibility** is set to **Organization**, click **Generate URL** to create a temporary test URL.
7.  Expand the resource you want to test.
8.  Click the **Try it out** button to enable testing.
9.  Provide values for any parameters, if applicable.
10. Click **Execute**.

# Test Websocket Endpoints via the Websocket Console

Choreo offers a WebSocket Console for testing WebSocket endpoints, securing them with OAuth 2.0 and generating test keys.

1.  Go to the [Choreo Console](https://console.choreo.dev/) and log in.
2.  In the **Component Listing** pane, click on the component you want to test.
3.  Click **Test** in the left navigation menu, then select **Console**.
4.  In the **WebSocket Console** pane, select the desired environment from the drop-down list.
5.  Choose the endpoint you want to test from the **Endpoint** list.
6.  If the **Network Visibility** is set to **Organization**, click **Generate URL** to create a temporary test URL.
7.  Expand the channel you want to test.
8.  Click **Connect** to establish a connection.
9.  Send and receive messages.