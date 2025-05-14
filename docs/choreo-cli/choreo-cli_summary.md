# Choreo Command-Line Interface (CLI) Overview

The Choreo CLI is a command-line tool designed to simplify interactions with Choreo, a comprehensive internal platform-as-a-service. It streamlines the development process, offering benefits such as simplified deployment processes and versatile workflow across frameworks. The CLI supports various component types including Services, Web Applications, Webhooks, Scheduled Tasks, and Manual Tasks.

## Key features of the Choreo CLI

-   **Create and Manage Resources**: Simplifies project and component management.
    -   **Create Builds and Deployments**: Streamlines building and deploying components, allowing for easy promotion to different environments.
-   **Monitor with Logs**: Provides integrated log functionality for effective component monitoring and insights into behavior and performance.

For troubleshooting and FAQs, refer to the Choreo CLI FAQ.

# Get Started with the Choreo CLI

This guide demonstrates how to use the Choreo CLI with a sample to-do app built with Next.js, covering the process of creating, building, deploying, and promoting a web application.

## Prerequisites

Installation involves running a command specific to your OS (Linux, macOS, or Windows) and verifying the installation with `choreo --version`.

## Steps

1.  **Login to Choreo**: Use `choreo login` and follow the console instructions.
2.  **Create a project**: Create a multi-repository project with `choreo create project web-app-project --type=multi-repository`.
3.  **Create a Web Application component**:
    *   Fork the sample to-do app repository.
    *   Create a component with `choreo create component my-web-app --project=web-app-project --type=webApp`.
    *   Provide repository details when prompted, including the repository URL, branch, directory, build-pack (nodejs), language version (20.x.x), and port (8080).
4.  **View component details**: Use `choreo describe component "my-web-app" --project="web-app-project"` to view component information.
5.  **Build the component**: Initiate the build with `choreo create build "my-web-app" --project="web-app-project"`.
    *   **View build status**: Check the status using `choreo describe build <build-id> --project="web-app-project" --component="my-web-app"`.
    *   **View build logs**: Access logs with `choreo logs --type=build --project="web-app-project" --component="my-web-app" --deployment-track="main" --build-id=<build_id>`.
6.  **Deploy to the Development environment**: Deploy with `choreo create deployment "my-web-app" --env=Development --project="web-app-project" --build-id=<build-id>`.
    *   **Verify the deployment**: Retrieve the URL with `choreo describe component "my-web-app" --project="web-app-project"`.
    *   **View runtime logs**: Observe logs with `choreo logs --type component-application --component my-web-app --project web-app-project --env Development --follow`.
7.  **Deploy to the Production environment**: Deploy with `choreo create deployment "my-web-app" --env=Production --project="web-app-project" --build-id=<build-id>`.
    *   **Verify the deployment**: Retrieve the URL with `choreo describe component "my-web-app" --project="web-app-project"`.

To see all available CLI functions, use `choreo --help`.

# Manage Authentication with Personal Access Tokens

Personal Access Tokens (PATs) offer a secure alternative to username/password authentication for the Choreo CLI, enabling granular access management.

## What are personal access tokens?

PATs are unique strings providing an alternative to username and password authentication.

## Sample use cases for personal access tokens

PATs are useful for automated scripting, granular permissions, temporary access, integration with third-party tools and multiple account management.

## Set up personal access tokens

1.  Sign in to the Choreo Console and navigate to Account Settings > Personal Access Tokens.
2.  Click "+ Create New", name the token, define scopes/permissions, and click "Generate".
3.  Copy and store the token securely.

## Use a personal access token with the Choreo CLI

To log in, use `choreo login --with-token` and provide the token via standard input, for example:

```bash
export CHOREO_TOKEN= <YOUR_PERSONAL_ACCESS_TOKEN>
echo "$CHOREO_TOKEN" | choreo login --with-token
```

## Manage and revoke tokens

Manage or revoke tokens via Account Settings > Personal Access Tokens in the Choreo Console.

## Best practices for token management

-   Limit scope
-   Rotate tokens regularly
-   Use secure storage
-   Revoke unused tokens