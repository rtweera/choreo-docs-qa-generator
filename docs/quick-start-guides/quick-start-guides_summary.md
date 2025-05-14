# Deploy a Web Application that Consumes a Backend Service

This guide explains how to expose a service endpoint via Choreo, securely consume it from a web application, and use Choreo's managed authentication. The sample web application allows users to sign in, view, add to, and delete books from their reading lists, and sign out. The steps include deploying and testing a service, creating a web application, creating a connection to the service, enabling managed authentication, deploying the web application, and consuming the service. The prerequisite is forking the Choreo sample book list app repository and creating a Choreo organization.

# Prerequisites

A GitHub account is required to fork the Choreo sample book list app repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Connect your sample repository and configure the service

Connect Choreo to your GitHub account and select the forked repository. Configure the `Reading List Service` component by specifying the directory, component type (Service), and buildpack (NodeJS).

# Step 3: Build the service

Navigate to the `Reading List Service` component's overview page, and initiate a build. Monitor the build progress until it completes successfully.

# Step 4: Deploy the service

Deploy the service by configuring the environment and verifying that the network visibility is set to public.

# Step 5: Test the service

Test the service using the OpenAPI Console to ensure the endpoints are working as expected. You can test GET, POST and DELETE methods.

# Step 6: Consume the service

Create a web application component, connect it to the GitHub repository, select React as the buildpack, and configure the build command and path. Then, create a connection between the web application and the deployed service, build the web application component, and configure and deploy the web application, replacing the placeholder service URL in `config.js` with the actual URL. Enable managed authentication and create a test user.

# Step 7: Test the front-end application

Access the front-end application via its web URL, log in with the created credentials, and verify the reading list functionality, including adding and deleting items.

# Deploy Your First Service

This guide provides instructions on how to deploy a service using Choreo, an Internal Developer Platform (IDevP). It involves using a pre-built book list service, building and deploying it using the Node.js buildpack, and testing the service.

# Prerequisites

A GitHub account is required to fork the Choreo sample book list service repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Create a service component

Create a service component, connect it to the GitHub repository, and select NodeJS as the buildpack.

# Step 3: Build and deploy

Build the service component and then deploy it by configuring the environment and reviewing the endpoint details.

# Step 4: Test the service

Test the service using the OpenAPI Console to ensure the endpoints are working as expected.

# Deploy Your First Static Web Application

This guide details how to deploy a static web application using Choreo. The example application is a to-do list where users can add tasks.

# Prerequisites

A GitHub account is required to fork the choreo-sample-todo-list-app repository. If signing in to the Choreo Console for the first time, you need to create an organization.

# Step 1: Create a project

Sign in to the Choreo Console, create a new project, and provide a unique name, display name, and description for the project.

# Step 2: Create a web application component

Create a web application component, connect it to the GitHub repository, and select NodeJS as the buildpack.

# Step 3: Build your web application

Build the web application component.

# Step 4: Deploy and access your web application

Deploy the web application and verify that it is hosted successfully by accessing the Web App URL.