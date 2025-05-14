# Choreo Kubernetes Infrastructure Upgrade Notice

**Upgrade Date: September 4, 2023, from 3:00 a.m. to 6:00 a.m. UTC**

An upgrade to the Choreo Kubernetes infrastructure is scheduled for September 4, 2023.

## Impact on Java-based Components

Java-based components, specifically those using Java Runtime versions older than jdk8u372 or 11.0.16, may experience out-of-memory errors due to increased memory consumption after the upgrade.

## Affected Component Types

The following Choreo component types are affected:

-   Components created using the Ballerina preset.
-   Integration components created using the WSO2 Micro Integrator preset.
-   REST API Proxies that include mediation policies.
-   Components created using the Dockerfile preset that utilize the Java Runtime.

## Action Required

**Recommended action date: Before September 4, 2023, 3:00 a.m. UTC**

To ensure compatibility and a smooth transition, users are advised to take the following actions before the upgrade:

-   **Ballerina or Micro Integrator-based components**: Redeploy components.
-   **REST API Proxy components with mediation policies**: Redeploy components.
-   **Other Java-based containerized components**:
    1.  Upgrade Java version to OpenJDK / HotSpot - jdk8u372, 11.0.16, 15, or later.
    2.  Rebuild the containerized application.
    3.  Redeploy the containerized component.

### Redeploy a component in Choreo

Instructions to redeploy a component:

1.  Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in.
2.  Select component from **Components Listing**.
3.  In the left navigation menu, click **Deploy**.
4.  Deploy component via the **Build Area** card.