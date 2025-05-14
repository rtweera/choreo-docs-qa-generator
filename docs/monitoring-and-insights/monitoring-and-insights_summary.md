 # Alert Overview

This section explains how you can configure alerts for your Choreo components. Setting up alerts allows you to proactively monitor your components ecosystem and take corrective measures when necessary.

!!! tip
    Setting up alerts in only available in the component level.

## Alert Types

Choreo supports the following types of alerts to help you monitor and manage your components effectively:

- [Latency alerts](#latency-alerts)
- [Traffic alerts](#traffic-alerts)
- [Resource alerts](#resource-alerts)
- [Log alerts](#log-alerts)
- [Build failure alerts](#build-failure-alerts)
- [Status code alerts](#status-code-alerts)

### Latency Alerts

Latency alerts notify you if the response latency of a component exceeds a predefined threshold in a given time period. This is useful for components that need to meet specific SLAs and for proactively identifying slow components.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | 99th, 95th, 90th, or 50th percentile.                                           |
| Threshold     | Latency in milliseconds (e.g.: 1800).                                           |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

### Traffic Alerts

Traffic alerts notify you when the request count of a component exceeds a predefined threshold. This is useful for managing components with backend traffic limits or monetized backends that require proactive scaling based on incoming traffic.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Threshold     | Requests per minute (e.g.: 200).                                                |
| Period        | Monitoring window (e.g.: 5 minutes).                                            |

### Resource Alerts

Resource alerts notify you when your component’s CPU or memory usage exceeds the defined thresholds. This ensures you can fix the resources allocations early to avoid performance issues or downtimes.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | CPU or Memory.                                                                  |
| Threshold     | **mCPU** for CPU and **MiB** for Memory(e.g.: 1000).                            |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

!!! Tip
    - **CPU**: mCPU (milliCPU) measures CPU usage in fractions of a core, where 1000m = 1 full core.
    - **Memory**: MiB (Mebibyte) measures memory in binary units, where 1 MiB = 2^20^ bytes.

### Log Alerts

Log alerts trigger notifications when a specific phrase appears **a specific number of times** in your component logs within a defined Time window. This helps to identify recurring issues or critical errors quickly, enabling faster troubleshooting.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Search Phrase | Keyword or phrase to look for to trigger the alert (e.g.: failed).                                               |
| Count         | Minimum number of occurrences to trigger the alert (e.g.: 10).                  |
| Interval      | Time window for counting occurrences (e.g.: 5 minutes).                         |

### Build Failure Alerts

Build failure alerts inform you if a build failure occurs for your component. This is essential for maintaining smooth development workflows.

### Status Code Alerts

Status code alert triggers when your component returns specific HTTP error(s) (e.g.: **403** Forbidden, **500** Internal Error). These alerts help to detect issues affecting your component’s availability.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Status Code   | Error code or series (e.g.: 400:Bad Request).                                   |
| Count         | Minimum number of occurrences (e.g.: 5).                                        |
| Interval      | Time window (e.g.: 5 minutes).                                                  |

!!! note
    Status code alerts are only supported for API proxy component types.

## Configure Alert

Follow these steps to configure an alert:

1. Navigate to the component you wish to configure alerts for.

    !!! info
        You need to have a scope of **Choreo DevOps** or **Choreo Platform Engineer** inorder to create Alerts.  

2. In the Choreo left menu, click **Observability** and then click **Alerts**.
3. Click **Create Alert Rule** to create a new alert rule.

    ![Create Alert Rule](../assets/img/monitoring-and-insights/alerts/alert-creation.png){.cInlineImage-full}

4. Select the **[Alert Type](#alert-types)** you want to create.
5. Select the **Environment** you want to create the alert for.
6. Select the **Deployment Track** or **Version** as required for the component.
7. Configure the remaining fields specific to your selected alert type.
8. In the **Emails** field, specify the list of emails that should be notified when the alert is triggered.

    !!! note
        - When adding an email, enter the required email and press enter to add it.
        - You can add a maximum of 5 email addresses per alert.

9. You can configure additional parameters in **Advanced Configurations** dropdown as needed, which vary based on your alert type.
10. The **Explanation window** provides a concise summary of the configured alert based on your alert configurations.
11. Click **Create** to save and activate your alert rule.

    !!! info
        - You can configure a maximum of 10 alerts per component.

12. Once successfully added, your alert will be listed in the **Configure Alerts** pane alongside any existing alerts for the component.
13. Each alert can be **edited**, **removed** and **disabled** or **enabled** via this pane.

    !!! note
        when editing an alert, you can't edit the **Alert Type**, **Environment** and **Deployment Track**.

## Alert History & Notifications

### View Alert History

You can check the past alerts that have triggered for your component when you click the  **Alerts History** pane in Choreo Alerts. You can filter the alert history by **Alert Type**, **Environment**, **Deployment Track** or **Version** and **Time Range**.

!!! note  
    When filtering, **API Proxy components** show a **Version** filter and other components display a **Deployment Track** filter, based on their monitoring context.  

You can click on an alert to expand it and see more details of the triggered alert.

### Email Notifications

When an alert is triggered, **recipients** added to the alert rule receive an email with **alert details** including a direct **Alert View link** to Choreo console.

![Email Notification](../assets/img/monitoring-and-insights/alerts/email-notification.png){.cInlineImage-full}


# Generate Custom Reports

Choreo insights allow you to generate custom reports to view the information that is important to you to make timely decisions for the betterment of your business. With custom reports, you can generate reports for a set of metrics of your choice and aggregate results by specific fields. Once generated, the metrics can be filtered out using any selected group-by filters. Custom reports support three visualizations: overtime charts, pie charts, and tables.

## Metrics

Choreo Insights allow you to retrieve data for the following metrics:

 - Successful Hit Count
 - Response Cache Hits
 - Request Mediation Latency
 - Response Mediation Latency
 - Backend Latency
 - Total Latency
 - API Errors
 - Target Errors

## Group-by

**Group-by** fields specify how to group the metric data. e.g., You can select **Successful Hit Count** in the **Metrics** field and **API Name** under **Group-by** to retrieve the successful hit count grouped by the API name.

Choreo Insights allow you to group metric data by the following fields:

 - API Name
 - API Version
 - API Resource Template
 - API Method
 - API Creator
 - Application
 - Application Owner
 - Destination
 - User Agent
 - Platform

To generate a custom report, follow the steps below:

1. In the left navigation menu, click **Custom Reports**.

    ![Select Custom Reports](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-1.png){.cInlineImage-full}

2. Select metric(s) from the **Metrics** drop-down selector.

    ![Generate report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-2-to-4.png){.cInlineImage-full}

3. Select a minimum of 1 and a maximum of 3 group-by field(s) from the **Group By** drop down selector.

4. Set the order of the group-by filters by drag and drop to determine the grouping order of the selected metric(s).

5. Once you determine the order of the group-by fields, you can set values for each group-by field from the respective dropdown. 

    ![Group by field selection](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-5.png){.cInlineImage-full}

6. Click **Generate**.

    ![Generate](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-6.png){.cInlineImage-full}

## Download Reports

Choreo Insights allow you to download report data related to each chart as a **PDF** or a **CSV** file.

To do this, click the **Download** icon on the top right of the relevant chart and select the required file format.
    ![Download Report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-7.png){.cInlineImage-full}


# Insights Overview

Choreo provides comprehensive insights into APIs created within both the on-premises API Manager and the Choreo platform. Choreo insights provide a range of metrics, including API traffic, error rates, and latency, allowing you to monitor and optimize API performance effectively.

With Choreo insights, you can:

- **Analyze API traffic**: Monitor the volume of requests and responses to understand usage patterns.
- **Track errors**: Identify and analyze errors to improve API reliability.
- **Monitor latency**: Measure and optimize the response times of your APIs.
- **Generate reports**: Generate detailed reports to keep stakeholders informed and support data-driven decision-making.
- **Configure alerts**: Set up alerts for specific events or thresholds to proactively manage API performance.
- **Obtain granular insights**: Obtain detailed information on a per-application, per-API, and per-user basis for more targeted analysis.
- **Drill down into data**: Dive deeper into data to perform root cause analysis.

By leveraging these insights, businesses can make informed decisions to enhance their API strategies and drive their digital transformation initiatives forward.

## View insights

To view usage insights, go to the [Choreo Console](https://console.choreo.dev/) and click **Insights** and then click **Usage** in the left navigation menu.

If you are viewing insights on the Choreo platform at the organization level, note the following:

- **Permission-based access**: Signed-in users can only view insights for components or projects that they have permission to access.
- **Data exclusion**: Insights exclude data from components you cannot access and the data related to deleted components.
- **Comprehensive view permission**: To view insights for all components, including deleted ones, across the organization regardless of project visibility, you must have the `View Organization Insights` permission under `OBSERVABILITY-MANAGEMENT` with the mapping level defined at the `Organization` level.
- **Admin role**: Users with the admin role have the `View Organization Insights` permission by default and can view organization-wide insights.
- **Configuring permissions**: For detailed steps on configuring permissions, see [Control Access in the Choreo Console](/choreo/docs/administer/control-access-in-the-choreo-console/).

By ensuring proper permissions are set, organizations can manage access to insights effectively while maintaining data security and relevance.

## Analyze statistics

Once you access the **Usage Insights** page, you can access the following subpages.

### Overview

The **Overview** page gives you a quick overview of the system status.

![Overview](../assets/img/monitoring-and-insights/api-insights/overview.png){.cInlineImage-full}

The information displayed is as follows:

- **Total Traffic**

    ![Total traffic](../assets/img/monitoring-and-insights/api-insights/overview-page-total-traffic.png){.cInlineImage-small}

    This widget displays the total traffic of the selected environment received during a given time interval. Both successful requests and failed requests are displayed. To investigate further, you can click the arrow icon on the bottom right corner of the widget to open the [**Traffic**](#traffic) page.

- **Error Request Count**

    ![Error request count](../assets/img/monitoring-and-insights/api-insights/overview-page-error-request-count.png){.cInlineImage-small}

    This widget displays the total number of requests that have resulted in errors in your selected environment during the selected time range.

- **Average Error Rate**

    ![Average error rate](../assets/img//monitoring-and-insights/api-insights/overview-page-error-rate.png){.cInlineImage-small}

    This widget displays the average error rate (i.e., error count/total request count) of the selected environment for a given time interval. You can use this widget as an indicator to understand the health of the system. If the error rate is high, you can investigate further by clicking the arrow on the bottom right of the widget and opening the [**Errors**](#errors) page.

- **95th Percentile Latency**

    ![95th percentile latency](../assets/img/monitoring-and-insights/api-insights/overview-page-latency.png){.cInlineImage-small}

    This widget displays the 95th percentile of all API latencies in your selected environment for the given time interval. You can use this widget to know whether the complete system operates under given SLAs. This metric provides the first indication of slow APIs. To investigate further, you can click the arrow on the bottom right of the widget to open the [**Latency**](#latency) page where you can further analyze the latency.

- **API Request Summary**

    ![API request summary](../assets/img/monitoring-and-insights/api-insights/overview-page-timeline.png){.cInlineImage-full}

    This chart displays the total successful requests, the total requests that have resulted in errors, and the latency in a timeline. The y-axis on the left displays the request count and the error count. The x-axis shows time, and the y-axis on the right shows the latency in milliseconds. The granularity of the data points is decided based on the time range you have selected. The tooltip provides the exact value of all three metrics accurately.

### Traffic

The **Traffic** page shows information related to the traffic that goes through your API management deployments. This includes API usage, application usage, resource usage, etc. You can use this page to investigate the usage of APIs and applications, traffic patterns, etc.

![Traffic](../assets/img/monitoring-and-insights/api-insights/traffic-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API**         | In the **API** field, you can select one or more APIs for which you want to view analytics. **All** is selected by default. Once you select an API, you can further filter by a specific application that uses the selected API via the **Application** field described below. |
| **By Application** | In the **Application** field, you can select the applications for which you want to view analytics. **All** is selected by default. The available applications are all the applications that have subscribed to one or more of the APIs you selected in the **API** field.|

You can view the following information for the APIs you have selected using the above filtering criteria:

- **API Usage Over Time**

     This timeline shows the count of API hits for the APIs for the filtered APIs. If multiple APIs are selected, the timeline shows each API in a separate line with a legend separating each line. You can also zoom in on a selected time range by selecting that area in the chart. To restore to the original view use the **Zoom out** button on the top right-hand corner of the plot.

    ![API usage over time](../assets/img/monitoring-and-insights/api-insights/api-usage-timeline.png){.cInlineImage-full}

- **API Usage By Application**

     This widget shows the per-application breakdown of requests for the APIs you selected. You can use the pie chart view or the line chart view. You can switch between the two views using the small icon at the upper-right corner of the widget.

    ![API usage by application](../assets/img/monitoring-and-insights/api-insights/usage-by-application.png){.cInlineImage-half}

- **API Usage By Target**

     This widget shows the per-backend breakdown of requests for the APIs you selected. This information is useful when multiple APIs share the same backend that has traffic restrictions. You can use these stats to scale your backends proactively. You can switch between the two views using the small icon at the upper-right corner of the widget.

     ![API usage by target](../assets/img/monitoring-and-insights/api-insights/usage-by-target.png){.cInlineImage-half}

- **API Resource Usage**

     This table shows a resource-level breakdown of API traffic. Each row represents an API resource and it shows the API name, resource path, API method, and the hit count for that combination.

     ![API resource usage](../assets/img/monitoring-and-insights/api-insights/resource-usage.png){.cInlineImage-full}

### Errors

The **Errors** page shows information related to erroneous API calls that are received by your system. The errors are categorized based on the error type. You can further drill down using the error subtypes. Use this page as the starting point for debugging any API errors.

![Error statistics](../assets/img/monitoring-and-insights/api-insights/error-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API** | In the **API** field, select the APIs for which you want to view analytics. By default, all APIs are selected. You can select one or multiple APIs from this selector and view the aggregated result. |
| **By Category** | The **Category** field is displayed when you click **Category** in the upper right corner of the page. In this field, you can select one or all of the following error categories:<br/>**Authentication**: Any kind of authentication error falls into this category including expired/missing/invalid credentials.<br/>**Target Connectivity**: Any kind of back-end error falls into this category including connection time-outs/other back-end errors (for example, 4xx and 5xx status codes).<br/>**Throttling**: Any request that fails due to rate-limiting falls into this category including application throttling/subscription throttling.<br/>**Other**: All other errors fall into this category including mediation errors/resource not found errors. |
| **By Status Code** | The **Status Code** field is displayed when you click **Status Code** in the upper right corner of the page. In this field, you can select all or any available HTTP status code categories (4xx, 5xx, etc.). These status codes represent the response status of the API Gateway. |

#### Viewing errors by category

The following widgets are available for monitoring errors when you have selected **Category** in the upper-right corner of the page.

- This graph shows the error by category over time for the selected period. Apply the required filters as explained above to select the APIs and the error categories to which this content applies. When you select multiple APIs, the error count is grouped by category.

    ![Errors by category graph](../assets/img/monitoring-and-insights/api-insights/error-category-graph.png){.cInlineImage-full}

- This table provides further information about the errors such as application details and the error reason. For some authentication errors, the application name is not available. You can use this table to get more concrete information about the errors related to your APIs and then start the problem identification.

    ![Errors by category table](../assets/img/monitoring-and-insights/api-insights/error-category-table.png){.cInlineImage-full}

#### Viewing errors by status code

The following widgets are available for monitoring errors when you select **Status Code** in the upper-right corner of the page.

- **Errors by Status Code**

    This graph shows the distribution of HTTP status codes received for errors over time for the selected period. Apply the required filters as explained above to select the APIs and status code groups to which this content applies. When you select multiple APIs, the error count is grouped by the status code.

    ![Errors by status code](../assets/img/monitoring-and-insights/api-insights/error-by-status-code.png){.cInlineImage-full}

- **Target Errors by Status Code**

    This graph shows the distribution of target errors that have occurred during the selected time interval by HTTP status code. Apply the required filters as explained in the table above to view the APIs and status code groups to which this content applies. If you select multiple APIs, the widget groups the target error count by the status code.

    ![Target errors by status code](../assets/img/monitoring-and-insights/api-insights/target-error-by-status-code.png){.cInlineImage-full}


- **Errors**

    The Errors heat map shows the HTTP response codes of errors sent to the client by the API Gateway. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Errors by Status Code** graph.

    ![Errors](../assets/img/monitoring-and-insights/api-insights/error-heatmap.png){.cInlineImage-full}

- **Target Errors**

    The Target errors heat map shows the HTTP response codes of errors that the API Gateway received from the backend. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Target Errors by Status Code** graph.

    ![Target errors](../assets/img/monitoring-and-insights/api-insights/target-error-heatmap.png){.cInlineImage-full}

### Latency

The **Latency** page shows information related to the latency of API calls within the API management deployment. You can view a summary of the slowest APIs and then drill down into the API view for further analysis. Use this page as a starting point to debug API slowness.

![Latency](../assets/img/monitoring-and-insights/api-insights/latency-page-full.png){.cInlineImage-full}

The information displayed is as follows:

- **Top 10 Slowest APIs**

    This widget allows you to identify the slowest APIs of the API management system at a glance. Since these are the APIs that contribute to the higher 95th percentile of the system, improving these APIs lowers the 95th percentile of latency in the API Management deployments.

    ![Slowest APIs](../assets/img/monitoring-and-insights/api-insights/slowest-apis.png){.cInlineImage-full}

- **Latencies By Category**

    This widget allows you to further drill down details in the above chart. Use the API selector in this widget to select the slow API you identified in the earlier step and then analyze further. Use the charts available in the widget to view the 95th percentile and the median latency over the selected period of the following:

      - Backend
      - Request mediation
      - Response mediation

    ![Latencies by category](../assets/img/monitoring-and-insights/api-insights/latency-by-category.png){.cInlineImage-full}

  You can use these charts to further drill down and analyze whether the latency occurs in the backend, request mediation, or response mediation. Also, because you can see both the median and 95th percentile, you can easily identify whether the slowness is occurring in each request or whether it is intermittent.

### Cache

The **Cache** page shows statistics that indicate the efficiency with which response caching is carried out for the requests sent to your APIs.

![Cache statistics](../assets/img/monitoring-and-insights/api-insights/cache-page-full.png){.cInlineImage-full}

The page displays the following statistics:

- **Cache Hit Percentage**

    This graph shows the percentage of requests the system has handled via the response cache over time and the total hits over time. This information allows you to assess how efficiently the backend handles API requests. For example, if the cache hit rate is low, it may indicate that the backend generates the same response each time a specific request is sent instead of returning the response via the cache. In such a scenario, there is scope to improve performance via response caching.

    ![Cache hit percentage](../assets/img/monitoring-and-insights/api-insights/cache-statistics.png){.cInlineImage-full}

- **Latency**

    This section shows the total latency reported during the same time interval applied to the **Cache Hit Percentage** graph above.

    ![Cache hits and misses](../assets/img/monitoring-and-insights/api-insights/cache-latency.png){.cInlineImage-full}

### Devices

The **Devices** page displays information about operating systems and HTTP agents that end users use to invoke the APIs. You can use this page to get an idea of the distribution of your user base and improve your APIs to match the audience.

![Device statistics](../assets/img/monitoring-and-insights/api-insights/devices-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. **All** is selected by default.

The information displayed is as follows:

- **Top Platforms**

    This chart shows the breakdown of the API clients by the operating system. The pie chart only shows platforms with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top platforms](../assets/img/monitoring-and-insights/api-insights/top-platforms.png){.cInlineImage-half}

- **Top User Agents**

    This chart shows the breakdown of the API clients by user-agent. The pie chart only shows user agents with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top user agents](../assets/img/monitoring-and-insights/api-insights/top-user-agents.png){.cInlineImage-half}

### Alerts

The **Alerts** page shows information related to business alerts issued by Choreo for your currently selected environment and organization. You can use this page as a health monitoring dashboard and make it visible to your project team. Using this page you can drill down on each alert and discover possible anomalies in your published APIs. See the topics given below to get details of the available widgets and understand how to use them effectively.

![Alerts statistics](../assets/img/monitoring-and-insights/api-insights/alerts-page-full.png){.cInlineImage-full}

**Prerequisites**

To use this page, be sure to configure alerts and have API invocations that trigger alerts. 

!!! Note
    Alerts are retained only for a week.

- **Alert Summary**

    This table lists each alert generated during the selected time interval. The message of the alert can be viewed by expanding the arrow icon on the details column. The drop-downs can be used to filter alerts based on the alert type and API.

    ![Alert summary](../assets/img/monitoring-and-insights/api-insights/alert-summary.png){.cInlineImage-full}

- **Top APIs by Alert Count**

    This shows a pie chart and a table to visualize the alert distribution during the selected time interval.

    ![Top APIs by alert count](../assets/img/monitoring-and-insights/api-insights/top-apis-by-alert-count.png){.cInlineImage-full}

### Reports

The **Reports** page allows you to download monthly usage reports for your system. There are preconfigured reports with system-wide statistics, and a custom report generator to generate reports based on a subset of APIs/applications.

![Report page](../assets/img/monitoring-and-insights/api-insights/report-page-full.png){.cInlineImage-full}

#### Download custom reports

This widget allows you to generate a custom report for the statistics that have been generated up to now and download it.

![Custom report download](../assets/img/monitoring-and-insights/api-insights/custom-report.png){.cInlineImage-full}

To generate a custom report, follow the steps below:

1. In the **API** field, select one or more APIs for which you want to generate the report. If required, you can select all the APIs by selecting **All**.

2. If you need to further filter the content printed in the report, select one or more applications in the **Application** field. By default, all the applications that have subscribed to one or more of the selected APIs are selected.

    !!! Tip
        If you want to filter the report content by the API consumer instead of the application, click on the toggle switch to the right of the **Application** field, and then select the required consumer. Only consumers who have subscribed to one or more of the selected APIs are displayed in the list. You can either select one or all of them.

3. Select the required year and the month in the **Year** and **Month** fields to specify the time interval for which you want to generate the report.

4. Click **Download**, and select the required format.

The report is downloaded in the specified format. The following is a sample report generated in PDF format.

![Sample report](../assets/img/monitoring-and-insights/api-insights/custom-report-sample.png){.cInlineImage-half}

The contents of the report are as follows.

| **Item** | **Description** |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Generated Time**      | The date and the time the report was generated.                                            |
| **Organization**        | The organization to which the report applies. Each report always applies to a specific organization. |
| **Environment**         | The environment to which the report applies. Each report always applies to a specific environment.  |
| **Tenant**              | The tenant to which the report applies. Each report always applies to a specific tenant.            |
| **Reporting period**    | The time interval for which the report is generated.                                       |
| **Total request count** | The total request count received by all selected APIs during the report time interval.     |

The table in the report contains the following rows.

| **Item** | **Description** |
|-----------------------|------------------------------------------------------------------------------|
| **API**          | The name of the API.                                                         |
| **Application** | The name of the application. The name of the subscriber is also provided within brackets. |
| **Usage**       | The usage count.                                                           |

#### Download pregenerated reports

These widgets allow you to download monthly reports for the last three months.

![Pre-generated reports](../assets/img/monitoring-and-insights/api-insights/configured-report.png){.cInlineImage-half}

To download a pregenerated report, click **Download** for the relevant month and then click on the required format.

### Geo Map

The **Geo Map** page allows you to see a geographical representation of your API usage. You can use this page to make business decisions such as identifying growing regions, analyzing the impact of a region-specific marketing campaign, etc.

![Geo Map page](../assets/img/monitoring-and-insights/api-insights/geomap-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. The default value is **All**.

This heat map highlights the countries with the appropriate color based on the hit count. It uses a relative color scale to depict the highest hit count to the lowest non-zero hit count.

![Geo Map Hit Scale](../assets/img/monitoring-and-insights/api-insights/geomap-hit-count-scale.png){.cInlineImage-xsmall}

#### Viewing the number of requests by country

You can hold the pointer over the highlighted countries to view the country name and the total number of hits from that location. You can also use the mouse to zoom the map or pan it. Optionally, you can download geo-map data in a tabular format using the PDF or CSV download options by clicking ![download](../assets/img/monitoring-and-insights/api-insights/insights-download-report.svg) on the top right corner.

![Geo Map by country](../assets/img/monitoring-and-insights/api-insights/geomap-requests-by-country.png){.cInlineImage-half}

!!! Note
    -  Currently, this feature is only available for on-premises environments.
    - The geo-map page utilizes the IP address of the incoming request to derive the geolocation. The actual source IP address can be replaced if there are intermediate hosts between the client and the gateway node. Therefore, the reverse proxy or the load balancer fronting the gateway node must add the `x-forwarded-for` header to each request to preserve the source IP address. If you do not configure this correctly, the **Geo Map** page will not show any data. To test this, you can manually add an `x-forwarded-for` header to the request.


# Integrate Choreo with Moesif

Moesif is an API analytics and monetization service that helps you grow your API products. You can integrate Choreo with Moesif and gain valuable insights into your API's usage.  While Moesif's API analytics capabilities empower you to make informed decision-making on behalf of your organization, its monetization options simplify revenue generation from your APIs, eliminating the need for complex coding. 

In this guide, you will:

- Generate a key in Moesif.
- Configure Choreo to connect to Moesif.
- Invoke an API and observe the insights on the Moesif dashboard. 

## Step 1: Generate an API key in Moesif

Let's generate an API key in Moesif. 
If you're an existing Moesif user with a registered organization, proceed to [step 1.2](#step-12-access-the-api-key-in-moesif-as-an-existing-user).

### Step 1.1: Generate a key in Moesif as a new user 

If you are a new user, follow the steps below to register an organization and generate a key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click **Sign Up** and select an authentication option and proceed. 
3. On the **Get Started** page, enter meaningful values for the fields and create a new organization. 

    | Field                 |  Description                                            |
    |-----------------------|---------------------------------------------------------|
    | **Organization Name** |  The name of your company or team.                      |
    | **Application Name**  | The name of your application that represents one project or environment.   |

 4. Click **Next**.
 5. On the **Overview** page, click **Next**.

     This opens the **Quick Install** page. As there is no data, you cannot proceed. Let's configure Moesif to receive data from Choreo. 

 6. Select a **WSO2 Choreo** as the **Server Integration**
 7. Copy the **Application Id**. 
    
     ![First Time user API Key](../assets/img/monitoring-and-insights/first_time_key_moesif.png)
     

### Step 1.2: Access the API key in Moesif as an existing user

If you are an existing user with a registered organization, or you do not have an API key for the organization you created,  follow the steps below to access the generated API key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click on your profile in the bottom left corner, and navigate to the **API Keys** page.
3. Copy the **Collection Application Id**.


## Step 2: Integrate Choreo with Moesif

Let's configure Choreo to publish events to Moesif.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in.
2. On the left navigation, click **Settings**. 
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. Click the **API Management** tab, and click **Moesif Dashboard**.
5. Select the environment you want to publish data for.
6. Paste the **Application Id** you copied. 
7. Click **Add**.

Once you successfully add the key, you will see a delete option next to it. Currently, you can only configure one API key. If you need to add a new API key, you need to delete the existing key and add the new one. 

!!! Note
    Once you configure the Moesif API key on Choreo, **wait for five minutes before you publish any data to the Moesif** API analytics platform. 


## Step 3: Invoke an API and observe the data on the Moesif Dashboard 

You have configured Choreo to publish data to Moesif. Let's see how you can view the insights on Moesif.

!!! tip
    - If you have not created an API and deployed it on Choreo, you can follow the [create and deploy a REST API](https://wso2.com/choreo/docs/develop-components/develop-services/develop-a-rest-api/) guide to get started.

1. Invoke your API by following the [Test REST Endpoints via the OpenAPI Console](https://wso2.com/choreo/docs/testing/test-rest-endpoints-via-the-openapi-console/) guide. 

2. Once you publish data, your Moesif dashboard will receive events. Once Moesif receives events, you will see a notification on Moesif confirming that it received data. 

    ![Data Recieved Moesif Notification](../assets/img/monitoring-and-insights/data_recieved_moesif_notification.png){.cInlineImage-small}

3. Click **Next** on the notification. This will take you to the final step, where you can opt to add team members. In this guide, let's skip this step. 
4. Click **Finish**.

You can now view your API's insights in the Moesif dashboard. 


 # Alert Overview

This section explains how you can configure alerts for your Choreo components. Setting up alerts allows you to proactively monitor your components ecosystem and take corrective measures when necessary.

!!! tip
    Setting up alerts in only available in the component level.

## Alert Types

Choreo supports the following types of alerts to help you monitor and manage your components effectively:

- [Latency alerts](#latency-alerts)
- [Traffic alerts](#traffic-alerts)
- [Resource alerts](#resource-alerts)
- [Log alerts](#log-alerts)
- [Build failure alerts](#build-failure-alerts)
- [Status code alerts](#status-code-alerts)

### Latency Alerts

Latency alerts notify you if the response latency of a component exceeds a predefined threshold in a given time period. This is useful for components that need to meet specific SLAs and for proactively identifying slow components.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | 99th, 95th, 90th, or 50th percentile.                                           |
| Threshold     | Latency in milliseconds (e.g.: 1800).                                           |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

### Traffic Alerts

Traffic alerts notify you when the request count of a component exceeds a predefined threshold. This is useful for managing components with backend traffic limits or monetized backends that require proactive scaling based on incoming traffic.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Threshold     | Requests per minute (e.g.: 200).                                                |
| Period        | Monitoring window (e.g.: 5 minutes).                                            |

### Resource Alerts

Resource alerts notify you when your component’s CPU or memory usage exceeds the defined thresholds. This ensures you can fix the resources allocations early to avoid performance issues or downtimes.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | CPU or Memory.                                                                  |
| Threshold     | **mCPU** for CPU and **MiB** for Memory(e.g.: 1000).                            |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

!!! Tip
    - **CPU**: mCPU (milliCPU) measures CPU usage in fractions of a core, where 1000m = 1 full core.
    - **Memory**: MiB (Mebibyte) measures memory in binary units, where 1 MiB = 2^20^ bytes.

### Log Alerts

Log alerts trigger notifications when a specific phrase appears **a specific number of times** in your component logs within a defined Time window. This helps to identify recurring issues or critical errors quickly, enabling faster troubleshooting.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Search Phrase | Keyword or phrase to look for to trigger the alert (e.g.: failed).                                               |
| Count         | Minimum number of occurrences to trigger the alert (e.g.: 10).                  |
| Interval      | Time window for counting occurrences (e.g.: 5 minutes).                         |

### Build Failure Alerts

Build failure alerts inform you if a build failure occurs for your component. This is essential for maintaining smooth development workflows.

### Status Code Alerts

Status code alert triggers when your component returns specific HTTP error(s) (e.g.: **403** Forbidden, **500** Internal Error). These alerts help to detect issues affecting your component’s availability.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Status Code   | Error code or series (e.g.: 400:Bad Request).                                   |
| Count         | Minimum number of occurrences (e.g.: 5).                                        |
| Interval      | Time window (e.g.: 5 minutes).                                                  |

!!! note
    Status code alerts are only supported for API proxy component types.

## Configure Alert

Follow these steps to configure an alert:

1. Navigate to the component you wish to configure alerts for.

    !!! info
        You need to have a scope of **Choreo DevOps** or **Choreo Platform Engineer** inorder to create Alerts.  

2. In the Choreo left menu, click **Observability** and then click **Alerts**.
3. Click **Create Alert Rule** to create a new alert rule.

    ![Create Alert Rule](../assets/img/monitoring-and-insights/alerts/alert-creation.png){.cInlineImage-full}

4. Select the **[Alert Type](#alert-types)** you want to create.
5. Select the **Environment** you want to create the alert for.
6. Select the **Deployment Track** or **Version** as required for the component.
7. Configure the remaining fields specific to your selected alert type.
8. In the **Emails** field, specify the list of emails that should be notified when the alert is triggered.

    !!! note
        - When adding an email, enter the required email and press enter to add it.
        - You can add a maximum of 5 email addresses per alert.

9. You can configure additional parameters in **Advanced Configurations** dropdown as needed, which vary based on your alert type.
10. The **Explanation window** provides a concise summary of the configured alert based on your alert configurations.
11. Click **Create** to save and activate your alert rule.

    !!! info
        - You can configure a maximum of 10 alerts per component.

12. Once successfully added, your alert will be listed in the **Configure Alerts** pane alongside any existing alerts for the component.
13. Each alert can be **edited**, **removed** and **disabled** or **enabled** via this pane.

    !!! note
        when editing an alert, you can't edit the **Alert Type**, **Environment** and **Deployment Track**.

## Alert History & Notifications

### View Alert History

You can check the past alerts that have triggered for your component when you click the  **Alerts History** pane in Choreo Alerts. You can filter the alert history by **Alert Type**, **Environment**, **Deployment Track** or **Version** and **Time Range**.

!!! note  
    When filtering, **API Proxy components** show a **Version** filter and other components display a **Deployment Track** filter, based on their monitoring context.  

You can click on an alert to expand it and see more details of the triggered alert.

### Email Notifications

When an alert is triggered, **recipients** added to the alert rule receive an email with **alert details** including a direct **Alert View link** to Choreo console.

![Email Notification](../assets/img/monitoring-and-insights/alerts/email-notification.png){.cInlineImage-full}


# Generate Custom Reports

Choreo insights allow you to generate custom reports to view the information that is important to you to make timely decisions for the betterment of your business. With custom reports, you can generate reports for a set of metrics of your choice and aggregate results by specific fields. Once generated, the metrics can be filtered out using any selected group-by filters. Custom reports support three visualizations: overtime charts, pie charts, and tables.

## Metrics

Choreo Insights allow you to retrieve data for the following metrics:

 - Successful Hit Count
 - Response Cache Hits
 - Request Mediation Latency
 - Response Mediation Latency
 - Backend Latency
 - Total Latency
 - API Errors
 - Target Errors

## Group-by

**Group-by** fields specify how to group the metric data. e.g., You can select **Successful Hit Count** in the **Metrics** field and **API Name** under **Group-by** to retrieve the successful hit count grouped by the API name.

Choreo Insights allow you to group metric data by the following fields:

 - API Name
 - API Version
 - API Resource Template
 - API Method
 - API Creator
 - Application
 - Application Owner
 - Destination
 - User Agent
 - Platform

To generate a custom report, follow the steps below:

1. In the left navigation menu, click **Custom Reports**.

    ![Select Custom Reports](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-1.png){.cInlineImage-full}

2. Select metric(s) from the **Metrics** drop-down selector.

    ![Generate report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-2-to-4.png){.cInlineImage-full}

3. Select a minimum of 1 and a maximum of 3 group-by field(s) from the **Group By** drop down selector.

4. Set the order of the group-by filters by drag and drop to determine the grouping order of the selected metric(s).

5. Once you determine the order of the group-by fields, you can set values for each group-by field from the respective dropdown. 

    ![Group by field selection](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-5.png){.cInlineImage-full}

6. Click **Generate**.

    ![Generate](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-6.png){.cInlineImage-full}

## Download Reports

Choreo Insights allow you to download report data related to each chart as a **PDF** or a **CSV** file.

To do this, click the **Download** icon on the top right of the relevant chart and select the required file format.
    ![Download Report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-7.png){.cInlineImage-full}


# Insights Overview

Choreo provides comprehensive insights into APIs created within both the on-premises API Manager and the Choreo platform. Choreo insights provide a range of metrics, including API traffic, error rates, and latency, allowing you to monitor and optimize API performance effectively.

With Choreo insights, you can:

- **Analyze API traffic**: Monitor the volume of requests and responses to understand usage patterns.
- **Track errors**: Identify and analyze errors to improve API reliability.
- **Monitor latency**: Measure and optimize the response times of your APIs.
- **Generate reports**: Generate detailed reports to keep stakeholders informed and support data-driven decision-making.
- **Configure alerts**: Set up alerts for specific events or thresholds to proactively manage API performance.
- **Obtain granular insights**: Obtain detailed information on a per-application, per-API, and per-user basis for more targeted analysis.
- **Drill down into data**: Dive deeper into data to perform root cause analysis.

By leveraging these insights, businesses can make informed decisions to enhance their API strategies and drive their digital transformation initiatives forward.

## View insights

To view usage insights, go to the [Choreo Console](https://console.choreo.dev/) and click **Insights** and then click **Usage** in the left navigation menu.

If you are viewing insights on the Choreo platform at the organization level, note the following:

- **Permission-based access**: Signed-in users can only view insights for components or projects that they have permission to access.
- **Data exclusion**: Insights exclude data from components you cannot access and the data related to deleted components.
- **Comprehensive view permission**: To view insights for all components, including deleted ones, across the organization regardless of project visibility, you must have the `View Organization Insights` permission under `OBSERVABILITY-MANAGEMENT` with the mapping level defined at the `Organization` level.
- **Admin role**: Users with the admin role have the `View Organization Insights` permission by default and can view organization-wide insights.
- **Configuring permissions**: For detailed steps on configuring permissions, see [Control Access in the Choreo Console](/choreo/docs/administer/control-access-in-the-choreo-console/).

By ensuring proper permissions are set, organizations can manage access to insights effectively while maintaining data security and relevance.

## Analyze statistics

Once you access the **Usage Insights** page, you can access the following subpages.

### Overview

The **Overview** page gives you a quick overview of the system status.

![Overview](../assets/img/monitoring-and-insights/api-insights/overview.png){.cInlineImage-full}

The information displayed is as follows:

- **Total Traffic**

    ![Total traffic](../assets/img/monitoring-and-insights/api-insights/overview-page-total-traffic.png){.cInlineImage-small}

    This widget displays the total traffic of the selected environment received during a given time interval. Both successful requests and failed requests are displayed. To investigate further, you can click the arrow icon on the bottom right corner of the widget to open the [**Traffic**](#traffic) page.

- **Error Request Count**

    ![Error request count](../assets/img/monitoring-and-insights/api-insights/overview-page-error-request-count.png){.cInlineImage-small}

    This widget displays the total number of requests that have resulted in errors in your selected environment during the selected time range.

- **Average Error Rate**

    ![Average error rate](../assets/img//monitoring-and-insights/api-insights/overview-page-error-rate.png){.cInlineImage-small}

    This widget displays the average error rate (i.e., error count/total request count) of the selected environment for a given time interval. You can use this widget as an indicator to understand the health of the system. If the error rate is high, you can investigate further by clicking the arrow on the bottom right of the widget and opening the [**Errors**](#errors) page.

- **95th Percentile Latency**

    ![95th percentile latency](../assets/img/monitoring-and-insights/api-insights/overview-page-latency.png){.cInlineImage-small}

    This widget displays the 95th percentile of all API latencies in your selected environment for the given time interval. You can use this widget to know whether the complete system operates under given SLAs. This metric provides the first indication of slow APIs. To investigate further, you can click the arrow on the bottom right of the widget to open the [**Latency**](#latency) page where you can further analyze the latency.

- **API Request Summary**

    ![API request summary](../assets/img/monitoring-and-insights/api-insights/overview-page-timeline.png){.cInlineImage-full}

    This chart displays the total successful requests, the total requests that have resulted in errors, and the latency in a timeline. The y-axis on the left displays the request count and the error count. The x-axis shows time, and the y-axis on the right shows the latency in milliseconds. The granularity of the data points is decided based on the time range you have selected. The tooltip provides the exact value of all three metrics accurately.

### Traffic

The **Traffic** page shows information related to the traffic that goes through your API management deployments. This includes API usage, application usage, resource usage, etc. You can use this page to investigate the usage of APIs and applications, traffic patterns, etc.

![Traffic](../assets/img/monitoring-and-insights/api-insights/traffic-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API**         | In the **API** field, you can select one or more APIs for which you want to view analytics. **All** is selected by default. Once you select an API, you can further filter by a specific application that uses the selected API via the **Application** field described below. |
| **By Application** | In the **Application** field, you can select the applications for which you want to view analytics. **All** is selected by default. The available applications are all the applications that have subscribed to one or more of the APIs you selected in the **API** field.|

You can view the following information for the APIs you have selected using the above filtering criteria:

- **API Usage Over Time**

     This timeline shows the count of API hits for the APIs for the filtered APIs. If multiple APIs are selected, the timeline shows each API in a separate line with a legend separating each line. You can also zoom in on a selected time range by selecting that area in the chart. To restore to the original view use the **Zoom out** button on the top right-hand corner of the plot.

    ![API usage over time](../assets/img/monitoring-and-insights/api-insights/api-usage-timeline.png){.cInlineImage-full}

- **API Usage By Application**

     This widget shows the per-application breakdown of requests for the APIs you selected. You can use the pie chart view or the line chart view. You can switch between the two views using the small icon at the upper-right corner of the widget.

    ![API usage by application](../assets/img/monitoring-and-insights/api-insights/usage-by-application.png){.cInlineImage-half}

- **API Usage By Target**

     This widget shows the per-backend breakdown of requests for the APIs you selected. This information is useful when multiple APIs share the same backend that has traffic restrictions. You can use these stats to scale your backends proactively. You can switch between the two views using the small icon at the upper-right corner of the widget.

     ![API usage by target](../assets/img/monitoring-and-insights/api-insights/usage-by-target.png){.cInlineImage-half}

- **API Resource Usage**

     This table shows a resource-level breakdown of API traffic. Each row represents an API resource and it shows the API name, resource path, API method, and the hit count for that combination.

     ![API resource usage](../assets/img/monitoring-and-insights/api-insights/resource-usage.png){.cInlineImage-full}

### Errors

The **Errors** page shows information related to erroneous API calls that are received by your system. The errors are categorized based on the error type. You can further drill down using the error subtypes. Use this page as the starting point for debugging any API errors.

![Error statistics](../assets/img/monitoring-and-insights/api-insights/error-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API** | In the **API** field, select the APIs for which you want to view analytics. By default, all APIs are selected. You can select one or multiple APIs from this selector and view the aggregated result. |
| **By Category** | The **Category** field is displayed when you click **Category** in the upper right corner of the page. In this field, you can select one or all of the following error categories:<br/>**Authentication**: Any kind of authentication error falls into this category including expired/missing/invalid credentials.<br/>**Target Connectivity**: Any kind of back-end error falls into this category including connection time-outs/other back-end errors (for example, 4xx and 5xx status codes).<br/>**Throttling**: Any request that fails due to rate-limiting falls into this category including application throttling/subscription throttling.<br/>**Other**: All other errors fall into this category including mediation errors/resource not found errors. |
| **By Status Code** | The **Status Code** field is displayed when you click **Status Code** in the upper right corner of the page. In this field, you can select all or any available HTTP status code categories (4xx, 5xx, etc.). These status codes represent the response status of the API Gateway. |

#### Viewing errors by category

The following widgets are available for monitoring errors when you have selected **Category** in the upper-right corner of the page.

- This graph shows the error by category over time for the selected period. Apply the required filters as explained above to select the APIs and the error categories to which this content applies. When you select multiple APIs, the error count is grouped by category.

    ![Errors by category graph](../assets/img/monitoring-and-insights/api-insights/error-category-graph.png){.cInlineImage-full}

- This table provides further information about the errors such as application details and the error reason. For some authentication errors, the application name is not available. You can use this table to get more concrete information about the errors related to your APIs and then start the problem identification.

    ![Errors by category table](../assets/img/monitoring-and-insights/api-insights/error-category-table.png){.cInlineImage-full}

#### Viewing errors by status code

The following widgets are available for monitoring errors when you select **Status Code** in the upper-right corner of the page.

- **Errors by Status Code**

    This graph shows the distribution of HTTP status codes received for errors over time for the selected period. Apply the required filters as explained above to select the APIs and status code groups to which this content applies. When you select multiple APIs, the error count is grouped by the status code.

    ![Errors by status code](../assets/img/monitoring-and-insights/api-insights/error-by-status-code.png){.cInlineImage-full}

- **Target Errors by Status Code**

    This graph shows the distribution of target errors that have occurred during the selected time interval by HTTP status code. Apply the required filters as explained in the table above to view the APIs and status code groups to which this content applies. If you select multiple APIs, the widget groups the target error count by the status code.

    ![Target errors by status code](../assets/img/monitoring-and-insights/api-insights/target-error-by-status-code.png){.cInlineImage-full}


- **Errors**

    The Errors heat map shows the HTTP response codes of errors sent to the client by the API Gateway. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Errors by Status Code** graph.

    ![Errors](../assets/img/monitoring-and-insights/api-insights/error-heatmap.png){.cInlineImage-full}

- **Target Errors**

    The Target errors heat map shows the HTTP response codes of errors that the API Gateway received from the backend. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Target Errors by Status Code** graph.

    ![Target errors](../assets/img/monitoring-and-insights/api-insights/target-error-heatmap.png){.cInlineImage-full}

### Latency

The **Latency** page shows information related to the latency of API calls within the API management deployment. You can view a summary of the slowest APIs and then drill down into the API view for further analysis. Use this page as a starting point to debug API slowness.

![Latency](../assets/img/monitoring-and-insights/api-insights/latency-page-full.png){.cInlineImage-full}

The information displayed is as follows:

- **Top 10 Slowest APIs**

    This widget allows you to identify the slowest APIs of the API management system at a glance. Since these are the APIs that contribute to the higher 95th percentile of the system, improving these APIs lowers the 95th percentile of latency in the API Management deployments.

    ![Slowest APIs](../assets/img/monitoring-and-insights/api-insights/slowest-apis.png){.cInlineImage-full}

- **Latencies By Category**

    This widget allows you to further drill down details in the above chart. Use the API selector in this widget to select the slow API you identified in the earlier step and then analyze further. Use the charts available in the widget to view the 95th percentile and the median latency over the selected period of the following:

      - Backend
      - Request mediation
      - Response mediation

    ![Latencies by category](../assets/img/monitoring-and-insights/api-insights/latency-by-category.png){.cInlineImage-full}

  You can use these charts to further drill down and analyze whether the latency occurs in the backend, request mediation, or response mediation. Also, because you can see both the median and 95th percentile, you can easily identify whether the slowness is occurring in each request or whether it is intermittent.

### Cache

The **Cache** page shows statistics that indicate the efficiency with which response caching is carried out for the requests sent to your APIs.

![Cache statistics](../assets/img/monitoring-and-insights/api-insights/cache-page-full.png){.cInlineImage-full}

The page displays the following statistics:

- **Cache Hit Percentage**

    This graph shows the percentage of requests the system has handled via the response cache over time and the total hits over time. This information allows you to assess how efficiently the backend handles API requests. For example, if the cache hit rate is low, it may indicate that the backend generates the same response each time a specific request is sent instead of returning the response via the cache. In such a scenario, there is scope to improve performance via response caching.

    ![Cache hit percentage](../assets/img/monitoring-and-insights/api-insights/cache-statistics.png){.cInlineImage-full}

- **Latency**

    This section shows the total latency reported during the same time interval applied to the **Cache Hit Percentage** graph above.

    ![Cache hits and misses](../assets/img/monitoring-and-insights/api-insights/cache-latency.png){.cInlineImage-full}

### Devices

The **Devices** page displays information about operating systems and HTTP agents that end users use to invoke the APIs. You can use this page to get an idea of the distribution of your user base and improve your APIs to match the audience.

![Device statistics](../assets/img/monitoring-and-insights/api-insights/devices-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. **All** is selected by default.

The information displayed is as follows:

- **Top Platforms**

    This chart shows the breakdown of the API clients by the operating system. The pie chart only shows platforms with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top platforms](../assets/img/monitoring-and-insights/api-insights/top-platforms.png){.cInlineImage-half}

- **Top User Agents**

    This chart shows the breakdown of the API clients by user-agent. The pie chart only shows user agents with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top user agents](../assets/img/monitoring-and-insights/api-insights/top-user-agents.png){.cInlineImage-half}

### Alerts

The **Alerts** page shows information related to business alerts issued by Choreo for your currently selected environment and organization. You can use this page as a health monitoring dashboard and make it visible to your project team. Using this page you can drill down on each alert and discover possible anomalies in your published APIs. See the topics given below to get details of the available widgets and understand how to use them effectively.

![Alerts statistics](../assets/img/monitoring-and-insights/api-insights/alerts-page-full.png){.cInlineImage-full}

**Prerequisites**

To use this page, be sure to configure alerts and have API invocations that trigger alerts. 

!!! Note
    Alerts are retained only for a week.

- **Alert Summary**

    This table lists each alert generated during the selected time interval. The message of the alert can be viewed by expanding the arrow icon on the details column. The drop-downs can be used to filter alerts based on the alert type and API.

    ![Alert summary](../assets/img/monitoring-and-insights/api-insights/alert-summary.png){.cInlineImage-full}

- **Top APIs by Alert Count**

    This shows a pie chart and a table to visualize the alert distribution during the selected time interval.

    ![Top APIs by alert count](../assets/img/monitoring-and-insights/api-insights/top-apis-by-alert-count.png){.cInlineImage-full}

### Reports

The **Reports** page allows you to download monthly usage reports for your system. There are preconfigured reports with system-wide statistics, and a custom report generator to generate reports based on a subset of APIs/applications.

![Report page](../assets/img/monitoring-and-insights/api-insights/report-page-full.png){.cInlineImage-full}

#### Download custom reports

This widget allows you to generate a custom report for the statistics that have been generated up to now and download it.

![Custom report download](../assets/img/monitoring-and-insights/api-insights/custom-report.png){.cInlineImage-full}

To generate a custom report, follow the steps below:

1. In the **API** field, select one or more APIs for which you want to generate the report. If required, you can select all the APIs by selecting **All**.

2. If you need to further filter the content printed in the report, select one or more applications in the **Application** field. By default, all the applications that have subscribed to one or more of the selected APIs are selected.

    !!! Tip
        If you want to filter the report content by the API consumer instead of the application, click on the toggle switch to the right of the **Application** field, and then select the required consumer. Only consumers who have subscribed to one or more of the selected APIs are displayed in the list. You can either select one or all of them.

3. Select the required year and the month in the **Year** and **Month** fields to specify the time interval for which you want to generate the report.

4. Click **Download**, and select the required format.

The report is downloaded in the specified format. The following is a sample report generated in PDF format.

![Sample report](../assets/img/monitoring-and-insights/api-insights/custom-report-sample.png){.cInlineImage-half}

The contents of the report are as follows.

| **Item** | **Description** |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Generated Time**      | The date and the time the report was generated.                                            |
| **Organization**        | The organization to which the report applies. Each report always applies to a specific organization. |
| **Environment**         | The environment to which the report applies. Each report always applies to a specific environment.  |
| **Tenant**              | The tenant to which the report applies. Each report always applies to a specific tenant.            |
| **Reporting period**    | The time interval for which the report is generated.                                       |
| **Total request count** | The total request count received by all selected APIs during the report time interval.     |

The table in the report contains the following rows.

| **Item** | **Description** |
|-----------------------|------------------------------------------------------------------------------|
| **API**          | The name of the API.                                                         |
| **Application** | The name of the application. The name of the subscriber is also provided within brackets. |
| **Usage**       | The usage count.                                                           |

#### Download pregenerated reports

These widgets allow you to download monthly reports for the last three months.

![Pre-generated reports](../assets/img/monitoring-and-insights/api-insights/configured-report.png){.cInlineImage-half}

To download a pregenerated report, click **Download** for the relevant month and then click on the required format.

### Geo Map

The **Geo Map** page allows you to see a geographical representation of your API usage. You can use this page to make business decisions such as identifying growing regions, analyzing the impact of a region-specific marketing campaign, etc.

![Geo Map page](../assets/img/monitoring-and-insights/api-insights/geomap-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. The default value is **All**.

This heat map highlights the countries with the appropriate color based on the hit count. It uses a relative color scale to depict the highest hit count to the lowest non-zero hit count.

![Geo Map Hit Scale](../assets/img/monitoring-and-insights/api-insights/geomap-hit-count-scale.png){.cInlineImage-xsmall}

#### Viewing the number of requests by country

You can hold the pointer over the highlighted countries to view the country name and the total number of hits from that location. You can also use the mouse to zoom the map or pan it. Optionally, you can download geo-map data in a tabular format using the PDF or CSV download options by clicking ![download](../assets/img/monitoring-and-insights/api-insights/insights-download-report.svg) on the top right corner.

![Geo Map by country](../assets/img/monitoring-and-insights/api-insights/geomap-requests-by-country.png){.cInlineImage-half}

!!! Note
    -  Currently, this feature is only available for on-premises environments.
    - The geo-map page utilizes the IP address of the incoming request to derive the geolocation. The actual source IP address can be replaced if there are intermediate hosts between the client and the gateway node. Therefore, the reverse proxy or the load balancer fronting the gateway node must add the `x-forwarded-for` header to each request to preserve the source IP address. If you do not configure this correctly, the **Geo Map** page will not show any data. To test this, you can manually add an `x-forwarded-for` header to the request.


# Integrate Choreo with Moesif

Moesif is an API analytics and monetization service that helps you grow your API products. You can integrate Choreo with Moesif and gain valuable insights into your API's usage.  While Moesif's API analytics capabilities empower you to make informed decision-making on behalf of your organization, its monetization options simplify revenue generation from your APIs, eliminating the need for complex coding. 

In this guide, you will:

- Generate a key in Moesif.
- Configure Choreo to connect to Moesif.
- Invoke an API and observe the insights on the Moesif dashboard. 

## Step 1: Generate an API key in Moesif

Let's generate an API key in Moesif. 
If you're an existing Moesif user with a registered organization, proceed to [step 1.2](#step-12-access-the-api-key-in-moesif-as-an-existing-user).

### Step 1.1: Generate a key in Moesif as a new user 

If you are a new user, follow the steps below to register an organization and generate a key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click **Sign Up** and select an authentication option and proceed. 
3. On the **Get Started** page, enter meaningful values for the fields and create a new organization. 

    | Field                 |  Description                                            |
    |-----------------------|---------------------------------------------------------|
    | **Organization Name** |  The name of your company or team.                      |
    | **Application Name**  | The name of your application that represents one project or environment.   |

 4. Click **Next**.
 5. On the **Overview** page, click **Next**.

     This opens the **Quick Install** page. As there is no data, you cannot proceed. Let's configure Moesif to receive data from Choreo. 

 6. Select a **WSO2 Choreo** as the **Server Integration**
 7. Copy the **Application Id**. 
    
     ![First Time user API Key](../assets/img/monitoring-and-insights/first_time_key_moesif.png)
     

### Step 1.2: Access the API key in Moesif as an existing user

If you are an existing user with a registered organization, or you do not have an API key for the organization you created,  follow the steps below to access the generated API key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click on your profile in the bottom left corner, and navigate to the **API Keys** page.
3. Copy the **Collection Application Id**.


## Step 2: Integrate Choreo with Moesif

Let's configure Choreo to publish events to Moesif.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in.
2. On the left navigation, click **Settings**. 
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. Click the **API Management** tab, and click **Moesif Dashboard**.
5. Select the environment you want to publish data for.
6. Paste the **Application Id** you copied. 
7. Click **Add**.

Once you successfully add the key, you will see a delete option next to it. Currently, you can only configure one API key. If you need to add a new API key, you need to delete the existing key and add the new one. 

!!! Note
    Once you configure the Moesif API key on Choreo, **wait for five minutes before you publish any data to the Moesif** API analytics platform. 


## Step 3: Invoke an API and observe the data on the Moesif Dashboard 

You have configured Choreo to publish data to Moesif. Let's see how you can view the insights on Moesif.

!!! tip
    - If you have not created an API and deployed it on Choreo, you can follow the [create and deploy a REST API](https://wso2.com/choreo/docs/develop-components/develop-services/develop-a-rest-api/) guide to get started.

1. Invoke your API by following the [Test REST Endpoints via the OpenAPI Console](https://wso2.com/choreo/docs/testing/test-rest-endpoints-via-the-openapi-console/) guide. 

2. Once you publish data, your Moesif dashboard will receive events. Once Moesif receives events, you will see a notification on Moesif confirming that it received data. 

    ![Data Recieved Moesif Notification](../assets/img/monitoring-and-insights/data_recieved_moesif_notification.png){.cInlineImage-small}

3. Click **Next** on the notification. This will take you to the final step, where you can opt to add team members. In this guide, let's skip this step. 
4. Click **Finish**.

You can now view your API's insights in the Moesif dashboard. 


 # Alert Overview

This section explains how you can configure alerts for your Choreo components. Setting up alerts allows you to proactively monitor your components ecosystem and take corrective measures when necessary.

!!! tip
    Setting up alerts in only available in the component level.

## Alert Types

Choreo supports the following types of alerts to help you monitor and manage your components effectively:

- [Latency alerts](#latency-alerts)
- [Traffic alerts](#traffic-alerts)
- [Resource alerts](#resource-alerts)
- [Log alerts](#log-alerts)
- [Build failure alerts](#build-failure-alerts)
- [Status code alerts](#status-code-alerts)

### Latency Alerts

Latency alerts notify you if the response latency of a component exceeds a predefined threshold in a given time period. This is useful for components that need to meet specific SLAs and for proactively identifying slow components.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | 99th, 95th, 90th, or 50th percentile.                                           |
| Threshold     | Latency in milliseconds (e.g.: 1800).                                           |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

### Traffic Alerts

Traffic alerts notify you when the request count of a component exceeds a predefined threshold. This is useful for managing components with backend traffic limits or monetized backends that require proactive scaling based on incoming traffic.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Threshold     | Requests per minute (e.g.: 200).                                                |
| Period        | Monitoring window (e.g.: 5 minutes).                                            |

### Resource Alerts

Resource alerts notify you when your component’s CPU or memory usage exceeds the defined thresholds. This ensures you can fix the resources allocations early to avoid performance issues or downtimes.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | CPU or Memory.                                                                  |
| Threshold     | **mCPU** for CPU and **MiB** for Memory(e.g.: 1000).                            |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

!!! Tip
    - **CPU**: mCPU (milliCPU) measures CPU usage in fractions of a core, where 1000m = 1 full core.
    - **Memory**: MiB (Mebibyte) measures memory in binary units, where 1 MiB = 2^20^ bytes.

### Log Alerts

Log alerts trigger notifications when a specific phrase appears **a specific number of times** in your component logs within a defined Time window. This helps to identify recurring issues or critical errors quickly, enabling faster troubleshooting.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Search Phrase | Keyword or phrase to look for to trigger the alert (e.g.: failed).                                               |
| Count         | Minimum number of occurrences to trigger the alert (e.g.: 10).                  |
| Interval      | Time window for counting occurrences (e.g.: 5 minutes).                         |

### Build Failure Alerts

Build failure alerts inform you if a build failure occurs for your component. This is essential for maintaining smooth development workflows.

### Status Code Alerts

Status code alert triggers when your component returns specific HTTP error(s) (e.g.: **403** Forbidden, **500** Internal Error). These alerts help to detect issues affecting your component’s availability.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Status Code   | Error code or series (e.g.: 400:Bad Request).                                   |
| Count         | Minimum number of occurrences (e.g.: 5).                                        |
| Interval      | Time window (e.g.: 5 minutes).                                                  |

!!! note
    Status code alerts are only supported for API proxy component types.

## Configure Alert

Follow these steps to configure an alert:

1. Navigate to the component you wish to configure alerts for.

    !!! info
        You need to have a scope of **Choreo DevOps** or **Choreo Platform Engineer** inorder to create Alerts.  

2. In the Choreo left menu, click **Observability** and then click **Alerts**.
3. Click **Create Alert Rule** to create a new alert rule.

    ![Create Alert Rule](../assets/img/monitoring-and-insights/alerts/alert-creation.png){.cInlineImage-full}

4. Select the **[Alert Type](#alert-types)** you want to create.
5. Select the **Environment** you want to create the alert for.
6. Select the **Deployment Track** or **Version** as required for the component.
7. Configure the remaining fields specific to your selected alert type.
8. In the **Emails** field, specify the list of emails that should be notified when the alert is triggered.

    !!! note
        - When adding an email, enter the required email and press enter to add it.
        - You can add a maximum of 5 email addresses per alert.

9. You can configure additional parameters in **Advanced Configurations** dropdown as needed, which vary based on your alert type.
10. The **Explanation window** provides a concise summary of the configured alert based on your alert configurations.
11. Click **Create** to save and activate your alert rule.

    !!! info
        - You can configure a maximum of 10 alerts per component.

12. Once successfully added, your alert will be listed in the **Configure Alerts** pane alongside any existing alerts for the component.
13. Each alert can be **edited**, **removed** and **disabled** or **enabled** via this pane.

    !!! note
        when editing an alert, you can't edit the **Alert Type**, **Environment** and **Deployment Track**.

## Alert History & Notifications

### View Alert History

You can check the past alerts that have triggered for your component when you click the  **Alerts History** pane in Choreo Alerts. You can filter the alert history by **Alert Type**, **Environment**, **Deployment Track** or **Version** and **Time Range**.

!!! note  
    When filtering, **API Proxy components** show a **Version** filter and other components display a **Deployment Track** filter, based on their monitoring context.  

You can click on an alert to expand it and see more details of the triggered alert.

### Email Notifications

When an alert is triggered, **recipients** added to the alert rule receive an email with **alert details** including a direct **Alert View link** to Choreo console.

![Email Notification](../assets/img/monitoring-and-insights/alerts/email-notification.png){.cInlineImage-full}


# Generate Custom Reports

Choreo insights allow you to generate custom reports to view the information that is important to you to make timely decisions for the betterment of your business. With custom reports, you can generate reports for a set of metrics of your choice and aggregate results by specific fields. Once generated, the metrics can be filtered out using any selected group-by filters. Custom reports support three visualizations: overtime charts, pie charts, and tables.

## Metrics

Choreo Insights allow you to retrieve data for the following metrics:

 - Successful Hit Count
 - Response Cache Hits
 - Request Mediation Latency
 - Response Mediation Latency
 - Backend Latency
 - Total Latency
 - API Errors
 - Target Errors

## Group-by

**Group-by** fields specify how to group the metric data. e.g., You can select **Successful Hit Count** in the **Metrics** field and **API Name** under **Group-by** to retrieve the successful hit count grouped by the API name.

Choreo Insights allow you to group metric data by the following fields:

 - API Name
 - API Version
 - API Resource Template
 - API Method
 - API Creator
 - Application
 - Application Owner
 - Destination
 - User Agent
 - Platform

To generate a custom report, follow the steps below:

1. In the left navigation menu, click **Custom Reports**.

    ![Select Custom Reports](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-1.png){.cInlineImage-full}

2. Select metric(s) from the **Metrics** drop-down selector.

    ![Generate report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-2-to-4.png){.cInlineImage-full}

3. Select a minimum of 1 and a maximum of 3 group-by field(s) from the **Group By** drop down selector.

4. Set the order of the group-by filters by drag and drop to determine the grouping order of the selected metric(s).

5. Once you determine the order of the group-by fields, you can set values for each group-by field from the respective dropdown. 

    ![Group by field selection](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-5.png){.cInlineImage-full}

6. Click **Generate**.

    ![Generate](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-6.png){.cInlineImage-full}

## Download Reports

Choreo Insights allow you to download report data related to each chart as a **PDF** or a **CSV** file.

To do this, click the **Download** icon on the top right of the relevant chart and select the required file format.
    ![Download Report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-7.png){.cInlineImage-full}


# Insights Overview

Choreo provides comprehensive insights into APIs created within both the on-premises API Manager and the Choreo platform. Choreo insights provide a range of metrics, including API traffic, error rates, and latency, allowing you to monitor and optimize API performance effectively.

With Choreo insights, you can:

- **Analyze API traffic**: Monitor the volume of requests and responses to understand usage patterns.
- **Track errors**: Identify and analyze errors to improve API reliability.
- **Monitor latency**: Measure and optimize the response times of your APIs.
- **Generate reports**: Generate detailed reports to keep stakeholders informed and support data-driven decision-making.
- **Configure alerts**: Set up alerts for specific events or thresholds to proactively manage API performance.
- **Obtain granular insights**: Obtain detailed information on a per-application, per-API, and per-user basis for more targeted analysis.
- **Drill down into data**: Dive deeper into data to perform root cause analysis.

By leveraging these insights, businesses can make informed decisions to enhance their API strategies and drive their digital transformation initiatives forward.

## View insights

To view usage insights, go to the [Choreo Console](https://console.choreo.dev/) and click **Insights** and then click **Usage** in the left navigation menu.

If you are viewing insights on the Choreo platform at the organization level, note the following:

- **Permission-based access**: Signed-in users can only view insights for components or projects that they have permission to access.
- **Data exclusion**: Insights exclude data from components you cannot access and the data related to deleted components.
- **Comprehensive view permission**: To view insights for all components, including deleted ones, across the organization regardless of project visibility, you must have the `View Organization Insights` permission under `OBSERVABILITY-MANAGEMENT` with the mapping level defined at the `Organization` level.
- **Admin role**: Users with the admin role have the `View Organization Insights` permission by default and can view organization-wide insights.
- **Configuring permissions**: For detailed steps on configuring permissions, see [Control Access in the Choreo Console](/choreo/docs/administer/control-access-in-the-choreo-console/).

By ensuring proper permissions are set, organizations can manage access to insights effectively while maintaining data security and relevance.

## Analyze statistics

Once you access the **Usage Insights** page, you can access the following subpages.

### Overview

The **Overview** page gives you a quick overview of the system status.

![Overview](../assets/img/monitoring-and-insights/api-insights/overview.png){.cInlineImage-full}

The information displayed is as follows:

- **Total Traffic**

    ![Total traffic](../assets/img/monitoring-and-insights/api-insights/overview-page-total-traffic.png){.cInlineImage-small}

    This widget displays the total traffic of the selected environment received during a given time interval. Both successful requests and failed requests are displayed. To investigate further, you can click the arrow icon on the bottom right corner of the widget to open the [**Traffic**](#traffic) page.

- **Error Request Count**

    ![Error request count](../assets/img/monitoring-and-insights/api-insights/overview-page-error-request-count.png){.cInlineImage-small}

    This widget displays the total number of requests that have resulted in errors in your selected environment during the selected time range.

- **Average Error Rate**

    ![Average error rate](../assets/img//monitoring-and-insights/api-insights/overview-page-error-rate.png){.cInlineImage-small}

    This widget displays the average error rate (i.e., error count/total request count) of the selected environment for a given time interval. You can use this widget as an indicator to understand the health of the system. If the error rate is high, you can investigate further by clicking the arrow on the bottom right of the widget and opening the [**Errors**](#errors) page.

- **95th Percentile Latency**

    ![95th percentile latency](../assets/img/monitoring-and-insights/api-insights/overview-page-latency.png){.cInlineImage-small}

    This widget displays the 95th percentile of all API latencies in your selected environment for the given time interval. You can use this widget to know whether the complete system operates under given SLAs. This metric provides the first indication of slow APIs. To investigate further, you can click the arrow on the bottom right of the widget to open the [**Latency**](#latency) page where you can further analyze the latency.

- **API Request Summary**

    ![API request summary](../assets/img/monitoring-and-insights/api-insights/overview-page-timeline.png){.cInlineImage-full}

    This chart displays the total successful requests, the total requests that have resulted in errors, and the latency in a timeline. The y-axis on the left displays the request count and the error count. The x-axis shows time, and the y-axis on the right shows the latency in milliseconds. The granularity of the data points is decided based on the time range you have selected. The tooltip provides the exact value of all three metrics accurately.

### Traffic

The **Traffic** page shows information related to the traffic that goes through your API management deployments. This includes API usage, application usage, resource usage, etc. You can use this page to investigate the usage of APIs and applications, traffic patterns, etc.

![Traffic](../assets/img/monitoring-and-insights/api-insights/traffic-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API**         | In the **API** field, you can select one or more APIs for which you want to view analytics. **All** is selected by default. Once you select an API, you can further filter by a specific application that uses the selected API via the **Application** field described below. |
| **By Application** | In the **Application** field, you can select the applications for which you want to view analytics. **All** is selected by default. The available applications are all the applications that have subscribed to one or more of the APIs you selected in the **API** field.|

You can view the following information for the APIs you have selected using the above filtering criteria:

- **API Usage Over Time**

     This timeline shows the count of API hits for the APIs for the filtered APIs. If multiple APIs are selected, the timeline shows each API in a separate line with a legend separating each line. You can also zoom in on a selected time range by selecting that area in the chart. To restore to the original view use the **Zoom out** button on the top right-hand corner of the plot.

    ![API usage over time](../assets/img/monitoring-and-insights/api-insights/api-usage-timeline.png){.cInlineImage-full}

- **API Usage By Application**

     This widget shows the per-application breakdown of requests for the APIs you selected. You can use the pie chart view or the line chart view. You can switch between the two views using the small icon at the upper-right corner of the widget.

    ![API usage by application](../assets/img/monitoring-and-insights/api-insights/usage-by-application.png){.cInlineImage-half}

- **API Usage By Target**

     This widget shows the per-backend breakdown of requests for the APIs you selected. This information is useful when multiple APIs share the same backend that has traffic restrictions. You can use these stats to scale your backends proactively. You can switch between the two views using the small icon at the upper-right corner of the widget.

     ![API usage by target](../assets/img/monitoring-and-insights/api-insights/usage-by-target.png){.cInlineImage-half}

- **API Resource Usage**

     This table shows a resource-level breakdown of API traffic. Each row represents an API resource and it shows the API name, resource path, API method, and the hit count for that combination.

     ![API resource usage](../assets/img/monitoring-and-insights/api-insights/resource-usage.png){.cInlineImage-full}

### Errors

The **Errors** page shows information related to erroneous API calls that are received by your system. The errors are categorized based on the error type. You can further drill down using the error subtypes. Use this page as the starting point for debugging any API errors.

![Error statistics](../assets/img/monitoring-and-insights/api-insights/error-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API** | In the **API** field, select the APIs for which you want to view analytics. By default, all APIs are selected. You can select one or multiple APIs from this selector and view the aggregated result. |
| **By Category** | The **Category** field is displayed when you click **Category** in the upper right corner of the page. In this field, you can select one or all of the following error categories:<br/>**Authentication**: Any kind of authentication error falls into this category including expired/missing/invalid credentials.<br/>**Target Connectivity**: Any kind of back-end error falls into this category including connection time-outs/other back-end errors (for example, 4xx and 5xx status codes).<br/>**Throttling**: Any request that fails due to rate-limiting falls into this category including application throttling/subscription throttling.<br/>**Other**: All other errors fall into this category including mediation errors/resource not found errors. |
| **By Status Code** | The **Status Code** field is displayed when you click **Status Code** in the upper right corner of the page. In this field, you can select all or any available HTTP status code categories (4xx, 5xx, etc.). These status codes represent the response status of the API Gateway. |

#### Viewing errors by category

The following widgets are available for monitoring errors when you have selected **Category** in the upper-right corner of the page.

- This graph shows the error by category over time for the selected period. Apply the required filters as explained above to select the APIs and the error categories to which this content applies. When you select multiple APIs, the error count is grouped by category.

    ![Errors by category graph](../assets/img/monitoring-and-insights/api-insights/error-category-graph.png){.cInlineImage-full}

- This table provides further information about the errors such as application details and the error reason. For some authentication errors, the application name is not available. You can use this table to get more concrete information about the errors related to your APIs and then start the problem identification.

    ![Errors by category table](../assets/img/monitoring-and-insights/api-insights/error-category-table.png){.cInlineImage-full}

#### Viewing errors by status code

The following widgets are available for monitoring errors when you select **Status Code** in the upper-right corner of the page.

- **Errors by Status Code**

    This graph shows the distribution of HTTP status codes received for errors over time for the selected period. Apply the required filters as explained above to select the APIs and status code groups to which this content applies. When you select multiple APIs, the error count is grouped by the status code.

    ![Errors by status code](../assets/img/monitoring-and-insights/api-insights/error-by-status-code.png){.cInlineImage-full}

- **Target Errors by Status Code**

    This graph shows the distribution of target errors that have occurred during the selected time interval by HTTP status code. Apply the required filters as explained in the table above to view the APIs and status code groups to which this content applies. If you select multiple APIs, the widget groups the target error count by the status code.

    ![Target errors by status code](../assets/img/monitoring-and-insights/api-insights/target-error-by-status-code.png){.cInlineImage-full}


- **Errors**

    The Errors heat map shows the HTTP response codes of errors sent to the client by the API Gateway. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Errors by Status Code** graph.

    ![Errors](../assets/img/monitoring-and-insights/api-insights/error-heatmap.png){.cInlineImage-full}

- **Target Errors**

    The Target errors heat map shows the HTTP response codes of errors that the API Gateway received from the backend. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Target Errors by Status Code** graph.

    ![Target errors](../assets/img/monitoring-and-insights/api-insights/target-error-heatmap.png){.cInlineImage-full}

### Latency

The **Latency** page shows information related to the latency of API calls within the API management deployment. You can view a summary of the slowest APIs and then drill down into the API view for further analysis. Use this page as a starting point to debug API slowness.

![Latency](../assets/img/monitoring-and-insights/api-insights/latency-page-full.png){.cInlineImage-full}

The information displayed is as follows:

- **Top 10 Slowest APIs**

    This widget allows you to identify the slowest APIs of the API management system at a glance. Since these are the APIs that contribute to the higher 95th percentile of the system, improving these APIs lowers the 95th percentile of latency in the API Management deployments.

    ![Slowest APIs](../assets/img/monitoring-and-insights/api-insights/slowest-apis.png){.cInlineImage-full}

- **Latencies By Category**

    This widget allows you to further drill down details in the above chart. Use the API selector in this widget to select the slow API you identified in the earlier step and then analyze further. Use the charts available in the widget to view the 95th percentile and the median latency over the selected period of the following:

      - Backend
      - Request mediation
      - Response mediation

    ![Latencies by category](../assets/img/monitoring-and-insights/api-insights/latency-by-category.png){.cInlineImage-full}

  You can use these charts to further drill down and analyze whether the latency occurs in the backend, request mediation, or response mediation. Also, because you can see both the median and 95th percentile, you can easily identify whether the slowness is occurring in each request or whether it is intermittent.

### Cache

The **Cache** page shows statistics that indicate the efficiency with which response caching is carried out for the requests sent to your APIs.

![Cache statistics](../assets/img/monitoring-and-insights/api-insights/cache-page-full.png){.cInlineImage-full}

The page displays the following statistics:

- **Cache Hit Percentage**

    This graph shows the percentage of requests the system has handled via the response cache over time and the total hits over time. This information allows you to assess how efficiently the backend handles API requests. For example, if the cache hit rate is low, it may indicate that the backend generates the same response each time a specific request is sent instead of returning the response via the cache. In such a scenario, there is scope to improve performance via response caching.

    ![Cache hit percentage](../assets/img/monitoring-and-insights/api-insights/cache-statistics.png){.cInlineImage-full}

- **Latency**

    This section shows the total latency reported during the same time interval applied to the **Cache Hit Percentage** graph above.

    ![Cache hits and misses](../assets/img/monitoring-and-insights/api-insights/cache-latency.png){.cInlineImage-full}

### Devices

The **Devices** page displays information about operating systems and HTTP agents that end users use to invoke the APIs. You can use this page to get an idea of the distribution of your user base and improve your APIs to match the audience.

![Device statistics](../assets/img/monitoring-and-insights/api-insights/devices-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. **All** is selected by default.

The information displayed is as follows:

- **Top Platforms**

    This chart shows the breakdown of the API clients by the operating system. The pie chart only shows platforms with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top platforms](../assets/img/monitoring-and-insights/api-insights/top-platforms.png){.cInlineImage-half}

- **Top User Agents**

    This chart shows the breakdown of the API clients by user-agent. The pie chart only shows user agents with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top user agents](../assets/img/monitoring-and-insights/api-insights/top-user-agents.png){.cInlineImage-half}

### Alerts

The **Alerts** page shows information related to business alerts issued by Choreo for your currently selected environment and organization. You can use this page as a health monitoring dashboard and make it visible to your project team. Using this page you can drill down on each alert and discover possible anomalies in your published APIs. See the topics given below to get details of the available widgets and understand how to use them effectively.

![Alerts statistics](../assets/img/monitoring-and-insights/api-insights/alerts-page-full.png){.cInlineImage-full}

**Prerequisites**

To use this page, be sure to configure alerts and have API invocations that trigger alerts. 

!!! Note
    Alerts are retained only for a week.

- **Alert Summary**

    This table lists each alert generated during the selected time interval. The message of the alert can be viewed by expanding the arrow icon on the details column. The drop-downs can be used to filter alerts based on the alert type and API.

    ![Alert summary](../assets/img/monitoring-and-insights/api-insights/alert-summary.png){.cInlineImage-full}

- **Top APIs by Alert Count**

    This shows a pie chart and a table to visualize the alert distribution during the selected time interval.

    ![Top APIs by alert count](../assets/img/monitoring-and-insights/api-insights/top-apis-by-alert-count.png){.cInlineImage-full}

### Reports

The **Reports** page allows you to download monthly usage reports for your system. There are preconfigured reports with system-wide statistics, and a custom report generator to generate reports based on a subset of APIs/applications.

![Report page](../assets/img/monitoring-and-insights/api-insights/report-page-full.png){.cInlineImage-full}

#### Download custom reports

This widget allows you to generate a custom report for the statistics that have been generated up to now and download it.

![Custom report download](../assets/img/monitoring-and-insights/api-insights/custom-report.png){.cInlineImage-full}

To generate a custom report, follow the steps below:

1. In the **API** field, select one or more APIs for which you want to generate the report. If required, you can select all the APIs by selecting **All**.

2. If you need to further filter the content printed in the report, select one or more applications in the **Application** field. By default, all the applications that have subscribed to one or more of the selected APIs are selected.

    !!! Tip
        If you want to filter the report content by the API consumer instead of the application, click on the toggle switch to the right of the **Application** field, and then select the required consumer. Only consumers who have subscribed to one or more of the selected APIs are displayed in the list. You can either select one or all of them.

3. Select the required year and the month in the **Year** and **Month** fields to specify the time interval for which you want to generate the report.

4. Click **Download**, and select the required format.

The report is downloaded in the specified format. The following is a sample report generated in PDF format.

![Sample report](../assets/img/monitoring-and-insights/api-insights/custom-report-sample.png){.cInlineImage-half}

The contents of the report are as follows.

| **Item** | **Description** |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Generated Time**      | The date and the time the report was generated.                                            |
| **Organization**        | The organization to which the report applies. Each report always applies to a specific organization. |
| **Environment**         | The environment to which the report applies. Each report always applies to a specific environment.  |
| **Tenant**              | The tenant to which the report applies. Each report always applies to a specific tenant.            |
| **Reporting period**    | The time interval for which the report is generated.                                       |
| **Total request count** | The total request count received by all selected APIs during the report time interval.     |

The table in the report contains the following rows.

| **Item** | **Description** |
|-----------------------|------------------------------------------------------------------------------|
| **API**          | The name of the API.                                                         |
| **Application** | The name of the application. The name of the subscriber is also provided within brackets. |
| **Usage**       | The usage count.                                                           |

#### Download pregenerated reports

These widgets allow you to download monthly reports for the last three months.

![Pre-generated reports](../assets/img/monitoring-and-insights/api-insights/configured-report.png){.cInlineImage-half}

To download a pregenerated report, click **Download** for the relevant month and then click on the required format.

### Geo Map

The **Geo Map** page allows you to see a geographical representation of your API usage. You can use this page to make business decisions such as identifying growing regions, analyzing the impact of a region-specific marketing campaign, etc.

![Geo Map page](../assets/img/monitoring-and-insights/api-insights/geomap-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. The default value is **All**.

This heat map highlights the countries with the appropriate color based on the hit count. It uses a relative color scale to depict the highest hit count to the lowest non-zero hit count.

![Geo Map Hit Scale](../assets/img/monitoring-and-insights/api-insights/geomap-hit-count-scale.png){.cInlineImage-xsmall}

#### Viewing the number of requests by country

You can hold the pointer over the highlighted countries to view the country name and the total number of hits from that location. You can also use the mouse to zoom the map or pan it. Optionally, you can download geo-map data in a tabular format using the PDF or CSV download options by clicking ![download](../assets/img/monitoring-and-insights/api-insights/insights-download-report.svg) on the top right corner.

![Geo Map by country](../assets/img/monitoring-and-insights/api-insights/geomap-requests-by-country.png){.cInlineImage-half}

!!! Note
    -  Currently, this feature is only available for on-premises environments.
    - The geo-map page utilizes the IP address of the incoming request to derive the geolocation. The actual source IP address can be replaced if there are intermediate hosts between the client and the gateway node. Therefore, the reverse proxy or the load balancer fronting the gateway node must add the `x-forwarded-for` header to each request to preserve the source IP address. If you do not configure this correctly, the **Geo Map** page will not show any data. To test this, you can manually add an `x-forwarded-for` header to the request.


# Integrate Choreo with Moesif

Moesif is an API analytics and monetization service that helps you grow your API products. You can integrate Choreo with Moesif and gain valuable insights into your API's usage.  While Moesif's API analytics capabilities empower you to make informed decision-making on behalf of your organization, its monetization options simplify revenue generation from your APIs, eliminating the need for complex coding. 

In this guide, you will:

- Generate a key in Moesif.
- Configure Choreo to connect to Moesif.
- Invoke an API and observe the insights on the Moesif dashboard. 

## Step 1: Generate an API key in Moesif

Let's generate an API key in Moesif. 
If you're an existing Moesif user with a registered organization, proceed to [step 1.2](#step-12-access-the-api-key-in-moesif-as-an-existing-user).

### Step 1.1: Generate a key in Moesif as a new user 

If you are a new user, follow the steps below to register an organization and generate a key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click **Sign Up** and select an authentication option and proceed. 
3. On the **Get Started** page, enter meaningful values for the fields and create a new organization. 

    | Field                 |  Description                                            |
    |-----------------------|---------------------------------------------------------|
    | **Organization Name** |  The name of your company or team.                      |
    | **Application Name**  | The name of your application that represents one project or environment.   |

 4. Click **Next**.
 5. On the **Overview** page, click **Next**.

     This opens the **Quick Install** page. As there is no data, you cannot proceed. Let's configure Moesif to receive data from Choreo. 

 6. Select a **WSO2 Choreo** as the **Server Integration**
 7. Copy the **Application Id**. 
    
     ![First Time user API Key](../assets/img/monitoring-and-insights/first_time_key_moesif.png)
     

### Step 1.2: Access the API key in Moesif as an existing user

If you are an existing user with a registered organization, or you do not have an API key for the organization you created,  follow the steps below to access the generated API key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click on your profile in the bottom left corner, and navigate to the **API Keys** page.
3. Copy the **Collection Application Id**.


## Step 2: Integrate Choreo with Moesif

Let's configure Choreo to publish events to Moesif.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in.
2. On the left navigation, click **Settings**. 
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. Click the **API Management** tab, and click **Moesif Dashboard**.
5. Select the environment you want to publish data for.
6. Paste the **Application Id** you copied. 
7. Click **Add**.

Once you successfully add the key, you will see a delete option next to it. Currently, you can only configure one API key. If you need to add a new API key, you need to delete the existing key and add the new one. 

!!! Note
    Once you configure the Moesif API key on Choreo, **wait for five minutes before you publish any data to the Moesif** API analytics platform. 


## Step 3: Invoke an API and observe the data on the Moesif Dashboard 

You have configured Choreo to publish data to Moesif. Let's see how you can view the insights on Moesif.

!!! tip
    - If you have not created an API and deployed it on Choreo, you can follow the [create and deploy a REST API](https://wso2.com/choreo/docs/develop-components/develop-services/develop-a-rest-api/) guide to get started.

1. Invoke your API by following the [Test REST Endpoints via the OpenAPI Console](https://wso2.com/choreo/docs/testing/test-rest-endpoints-via-the-openapi-console/) guide. 

2. Once you publish data, your Moesif dashboard will receive events. Once Moesif receives events, you will see a notification on Moesif confirming that it received data. 

    ![Data Recieved Moesif Notification](../assets/img/monitoring-and-insights/data_recieved_moesif_notification.png){.cInlineImage-small}

3. Click **Next** on the notification. This will take you to the final step, where you can opt to add team members. In this guide, let's skip this step. 
4. Click **Finish**.

You can now view your API's insights in the Moesif dashboard. 


 # Alert Overview

This section explains how you can configure alerts for your Choreo components. Setting up alerts allows you to proactively monitor your components ecosystem and take corrective measures when necessary.

!!! tip
    Setting up alerts in only available in the component level.

## Alert Types

Choreo supports the following types of alerts to help you monitor and manage your components effectively:

- [Latency alerts](#latency-alerts)
- [Traffic alerts](#traffic-alerts)
- [Resource alerts](#resource-alerts)
- [Log alerts](#log-alerts)
- [Build failure alerts](#build-failure-alerts)
- [Status code alerts](#status-code-alerts)

### Latency Alerts

Latency alerts notify you if the response latency of a component exceeds a predefined threshold in a given time period. This is useful for components that need to meet specific SLAs and for proactively identifying slow components.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | 99th, 95th, 90th, or 50th percentile.                                           |
| Threshold     | Latency in milliseconds (e.g.: 1800).                                           |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

### Traffic Alerts

Traffic alerts notify you when the request count of a component exceeds a predefined threshold. This is useful for managing components with backend traffic limits or monetized backends that require proactive scaling based on incoming traffic.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Threshold     | Requests per minute (e.g.: 200).                                                |
| Period        | Monitoring window (e.g.: 5 minutes).                                            |

### Resource Alerts

Resource alerts notify you when your component’s CPU or memory usage exceeds the defined thresholds. This ensures you can fix the resources allocations early to avoid performance issues or downtimes.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | CPU or Memory.                                                                  |
| Threshold     | **mCPU** for CPU and **MiB** for Memory(e.g.: 1000).                            |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

!!! Tip
    - **CPU**: mCPU (milliCPU) measures CPU usage in fractions of a core, where 1000m = 1 full core.
    - **Memory**: MiB (Mebibyte) measures memory in binary units, where 1 MiB = 2^20^ bytes.

### Log Alerts

Log alerts trigger notifications when a specific phrase appears **a specific number of times** in your component logs within a defined Time window. This helps to identify recurring issues or critical errors quickly, enabling faster troubleshooting.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Search Phrase | Keyword or phrase to look for to trigger the alert (e.g.: failed).                                               |
| Count         | Minimum number of occurrences to trigger the alert (e.g.: 10).                  |
| Interval      | Time window for counting occurrences (e.g.: 5 minutes).                         |

### Build Failure Alerts

Build failure alerts inform you if a build failure occurs for your component. This is essential for maintaining smooth development workflows.

### Status Code Alerts

Status code alert triggers when your component returns specific HTTP error(s) (e.g.: **403** Forbidden, **500** Internal Error). These alerts help to detect issues affecting your component’s availability.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Status Code   | Error code or series (e.g.: 400:Bad Request).                                   |
| Count         | Minimum number of occurrences (e.g.: 5).                                        |
| Interval      | Time window (e.g.: 5 minutes).                                                  |

!!! note
    Status code alerts are only supported for API proxy component types.

## Configure Alert

Follow these steps to configure an alert:

1. Navigate to the component you wish to configure alerts for.

    !!! info
        You need to have a scope of **Choreo DevOps** or **Choreo Platform Engineer** inorder to create Alerts.  

2. In the Choreo left menu, click **Observability** and then click **Alerts**.
3. Click **Create Alert Rule** to create a new alert rule.

    ![Create Alert Rule](../assets/img/monitoring-and-insights/alerts/alert-creation.png){.cInlineImage-full}

4. Select the **[Alert Type](#alert-types)** you want to create.
5. Select the **Environment** you want to create the alert for.
6. Select the **Deployment Track** or **Version** as required for the component.
7. Configure the remaining fields specific to your selected alert type.
8. In the **Emails** field, specify the list of emails that should be notified when the alert is triggered.

    !!! note
        - When adding an email, enter the required email and press enter to add it.
        - You can add a maximum of 5 email addresses per alert.

9. You can configure additional parameters in **Advanced Configurations** dropdown as needed, which vary based on your alert type.
10. The **Explanation window** provides a concise summary of the configured alert based on your alert configurations.
11. Click **Create** to save and activate your alert rule.

    !!! info
        - You can configure a maximum of 10 alerts per component.

12. Once successfully added, your alert will be listed in the **Configure Alerts** pane alongside any existing alerts for the component.
13. Each alert can be **edited**, **removed** and **disabled** or **enabled** via this pane.

    !!! note
        when editing an alert, you can't edit the **Alert Type**, **Environment** and **Deployment Track**.

## Alert History & Notifications

### View Alert History

You can check the past alerts that have triggered for your component when you click the  **Alerts History** pane in Choreo Alerts. You can filter the alert history by **Alert Type**, **Environment**, **Deployment Track** or **Version** and **Time Range**.

!!! note  
    When filtering, **API Proxy components** show a **Version** filter and other components display a **Deployment Track** filter, based on their monitoring context.  

You can click on an alert to expand it and see more details of the triggered alert.

### Email Notifications

When an alert is triggered, **recipients** added to the alert rule receive an email with **alert details** including a direct **Alert View link** to Choreo console.

![Email Notification](../assets/img/monitoring-and-insights/alerts/email-notification.png){.cInlineImage-full}


# Generate Custom Reports

Choreo insights allow you to generate custom reports to view the information that is important to you to make timely decisions for the betterment of your business. With custom reports, you can generate reports for a set of metrics of your choice and aggregate results by specific fields. Once generated, the metrics can be filtered out using any selected group-by filters. Custom reports support three visualizations: overtime charts, pie charts, and tables.

## Metrics

Choreo Insights allow you to retrieve data for the following metrics:

 - Successful Hit Count
 - Response Cache Hits
 - Request Mediation Latency
 - Response Mediation Latency
 - Backend Latency
 - Total Latency
 - API Errors
 - Target Errors

## Group-by

**Group-by** fields specify how to group the metric data. e.g., You can select **Successful Hit Count** in the **Metrics** field and **API Name** under **Group-by** to retrieve the successful hit count grouped by the API name.

Choreo Insights allow you to group metric data by the following fields:

 - API Name
 - API Version
 - API Resource Template
 - API Method
 - API Creator
 - Application
 - Application Owner
 - Destination
 - User Agent
 - Platform

To generate a custom report, follow the steps below:

1. In the left navigation menu, click **Custom Reports**.

    ![Select Custom Reports](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-1.png){.cInlineImage-full}

2. Select metric(s) from the **Metrics** drop-down selector.

    ![Generate report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-2-to-4.png){.cInlineImage-full}

3. Select a minimum of 1 and a maximum of 3 group-by field(s) from the **Group By** drop down selector.

4. Set the order of the group-by filters by drag and drop to determine the grouping order of the selected metric(s).

5. Once you determine the order of the group-by fields, you can set values for each group-by field from the respective dropdown. 

    ![Group by field selection](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-5.png){.cInlineImage-full}

6. Click **Generate**.

    ![Generate](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-6.png){.cInlineImage-full}

## Download Reports

Choreo Insights allow you to download report data related to each chart as a **PDF** or a **CSV** file.

To do this, click the **Download** icon on the top right of the relevant chart and select the required file format.
    ![Download Report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-7.png){.cInlineImage-full}


# Insights Overview

Choreo provides comprehensive insights into APIs created within both the on-premises API Manager and the Choreo platform. Choreo insights provide a range of metrics, including API traffic, error rates, and latency, allowing you to monitor and optimize API performance effectively.

With Choreo insights, you can:

- **Analyze API traffic**: Monitor the volume of requests and responses to understand usage patterns.
- **Track errors**: Identify and analyze errors to improve API reliability.
- **Monitor latency**: Measure and optimize the response times of your APIs.
- **Generate reports**: Generate detailed reports to keep stakeholders informed and support data-driven decision-making.
- **Configure alerts**: Set up alerts for specific events or thresholds to proactively manage API performance.
- **Obtain granular insights**: Obtain detailed information on a per-application, per-API, and per-user basis for more targeted analysis.
- **Drill down into data**: Dive deeper into data to perform root cause analysis.

By leveraging these insights, businesses can make informed decisions to enhance their API strategies and drive their digital transformation initiatives forward.

## View insights

To view usage insights, go to the [Choreo Console](https://console.choreo.dev/) and click **Insights** and then click **Usage** in the left navigation menu.

If you are viewing insights on the Choreo platform at the organization level, note the following:

- **Permission-based access**: Signed-in users can only view insights for components or projects that they have permission to access.
- **Data exclusion**: Insights exclude data from components you cannot access and the data related to deleted components.
- **Comprehensive view permission**: To view insights for all components, including deleted ones, across the organization regardless of project visibility, you must have the `View Organization Insights` permission under `OBSERVABILITY-MANAGEMENT` with the mapping level defined at the `Organization` level.
- **Admin role**: Users with the admin role have the `View Organization Insights` permission by default and can view organization-wide insights.
- **Configuring permissions**: For detailed steps on configuring permissions, see [Control Access in the Choreo Console](/choreo/docs/administer/control-access-in-the-choreo-console/).

By ensuring proper permissions are set, organizations can manage access to insights effectively while maintaining data security and relevance.

## Analyze statistics

Once you access the **Usage Insights** page, you can access the following subpages.

### Overview

The **Overview** page gives you a quick overview of the system status.

![Overview](../assets/img/monitoring-and-insights/api-insights/overview.png){.cInlineImage-full}

The information displayed is as follows:

- **Total Traffic**

    ![Total traffic](../assets/img/monitoring-and-insights/api-insights/overview-page-total-traffic.png){.cInlineImage-small}

    This widget displays the total traffic of the selected environment received during a given time interval. Both successful requests and failed requests are displayed. To investigate further, you can click the arrow icon on the bottom right corner of the widget to open the [**Traffic**](#traffic) page.

- **Error Request Count**

    ![Error request count](../assets/img/monitoring-and-insights/api-insights/overview-page-error-request-count.png){.cInlineImage-small}

    This widget displays the total number of requests that have resulted in errors in your selected environment during the selected time range.

- **Average Error Rate**

    ![Average error rate](../assets/img//monitoring-and-insights/api-insights/overview-page-error-rate.png){.cInlineImage-small}

    This widget displays the average error rate (i.e., error count/total request count) of the selected environment for a given time interval. You can use this widget as an indicator to understand the health of the system. If the error rate is high, you can investigate further by clicking the arrow on the bottom right of the widget and opening the [**Errors**](#errors) page.

- **95th Percentile Latency**

    ![95th percentile latency](../assets/img/monitoring-and-insights/api-insights/overview-page-latency.png){.cInlineImage-small}

    This widget displays the 95th percentile of all API latencies in your selected environment for the given time interval. You can use this widget to know whether the complete system operates under given SLAs. This metric provides the first indication of slow APIs. To investigate further, you can click the arrow on the bottom right of the widget to open the [**Latency**](#latency) page where you can further analyze the latency.

- **API Request Summary**

    ![API request summary](../assets/img/monitoring-and-insights/api-insights/overview-page-timeline.png){.cInlineImage-full}

    This chart displays the total successful requests, the total requests that have resulted in errors, and the latency in a timeline. The y-axis on the left displays the request count and the error count. The x-axis shows time, and the y-axis on the right shows the latency in milliseconds. The granularity of the data points is decided based on the time range you have selected. The tooltip provides the exact value of all three metrics accurately.

### Traffic

The **Traffic** page shows information related to the traffic that goes through your API management deployments. This includes API usage, application usage, resource usage, etc. You can use this page to investigate the usage of APIs and applications, traffic patterns, etc.

![Traffic](../assets/img/monitoring-and-insights/api-insights/traffic-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API**         | In the **API** field, you can select one or more APIs for which you want to view analytics. **All** is selected by default. Once you select an API, you can further filter by a specific application that uses the selected API via the **Application** field described below. |
| **By Application** | In the **Application** field, you can select the applications for which you want to view analytics. **All** is selected by default. The available applications are all the applications that have subscribed to one or more of the APIs you selected in the **API** field.|

You can view the following information for the APIs you have selected using the above filtering criteria:

- **API Usage Over Time**

     This timeline shows the count of API hits for the APIs for the filtered APIs. If multiple APIs are selected, the timeline shows each API in a separate line with a legend separating each line. You can also zoom in on a selected time range by selecting that area in the chart. To restore to the original view use the **Zoom out** button on the top right-hand corner of the plot.

    ![API usage over time](../assets/img/monitoring-and-insights/api-insights/api-usage-timeline.png){.cInlineImage-full}

- **API Usage By Application**

     This widget shows the per-application breakdown of requests for the APIs you selected. You can use the pie chart view or the line chart view. You can switch between the two views using the small icon at the upper-right corner of the widget.

    ![API usage by application](../assets/img/monitoring-and-insights/api-insights/usage-by-application.png){.cInlineImage-half}

- **API Usage By Target**

     This widget shows the per-backend breakdown of requests for the APIs you selected. This information is useful when multiple APIs share the same backend that has traffic restrictions. You can use these stats to scale your backends proactively. You can switch between the two views using the small icon at the upper-right corner of the widget.

     ![API usage by target](../assets/img/monitoring-and-insights/api-insights/usage-by-target.png){.cInlineImage-half}

- **API Resource Usage**

     This table shows a resource-level breakdown of API traffic. Each row represents an API resource and it shows the API name, resource path, API method, and the hit count for that combination.

     ![API resource usage](../assets/img/monitoring-and-insights/api-insights/resource-usage.png){.cInlineImage-full}

### Errors

The **Errors** page shows information related to erroneous API calls that are received by your system. The errors are categorized based on the error type. You can further drill down using the error subtypes. Use this page as the starting point for debugging any API errors.

![Error statistics](../assets/img/monitoring-and-insights/api-insights/error-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API** | In the **API** field, select the APIs for which you want to view analytics. By default, all APIs are selected. You can select one or multiple APIs from this selector and view the aggregated result. |
| **By Category** | The **Category** field is displayed when you click **Category** in the upper right corner of the page. In this field, you can select one or all of the following error categories:<br/>**Authentication**: Any kind of authentication error falls into this category including expired/missing/invalid credentials.<br/>**Target Connectivity**: Any kind of back-end error falls into this category including connection time-outs/other back-end errors (for example, 4xx and 5xx status codes).<br/>**Throttling**: Any request that fails due to rate-limiting falls into this category including application throttling/subscription throttling.<br/>**Other**: All other errors fall into this category including mediation errors/resource not found errors. |
| **By Status Code** | The **Status Code** field is displayed when you click **Status Code** in the upper right corner of the page. In this field, you can select all or any available HTTP status code categories (4xx, 5xx, etc.). These status codes represent the response status of the API Gateway. |

#### Viewing errors by category

The following widgets are available for monitoring errors when you have selected **Category** in the upper-right corner of the page.

- This graph shows the error by category over time for the selected period. Apply the required filters as explained above to select the APIs and the error categories to which this content applies. When you select multiple APIs, the error count is grouped by category.

    ![Errors by category graph](../assets/img/monitoring-and-insights/api-insights/error-category-graph.png){.cInlineImage-full}

- This table provides further information about the errors such as application details and the error reason. For some authentication errors, the application name is not available. You can use this table to get more concrete information about the errors related to your APIs and then start the problem identification.

    ![Errors by category table](../assets/img/monitoring-and-insights/api-insights/error-category-table.png){.cInlineImage-full}

#### Viewing errors by status code

The following widgets are available for monitoring errors when you select **Status Code** in the upper-right corner of the page.

- **Errors by Status Code**

    This graph shows the distribution of HTTP status codes received for errors over time for the selected period. Apply the required filters as explained above to select the APIs and status code groups to which this content applies. When you select multiple APIs, the error count is grouped by the status code.

    ![Errors by status code](../assets/img/monitoring-and-insights/api-insights/error-by-status-code.png){.cInlineImage-full}

- **Target Errors by Status Code**

    This graph shows the distribution of target errors that have occurred during the selected time interval by HTTP status code. Apply the required filters as explained in the table above to view the APIs and status code groups to which this content applies. If you select multiple APIs, the widget groups the target error count by the status code.

    ![Target errors by status code](../assets/img/monitoring-and-insights/api-insights/target-error-by-status-code.png){.cInlineImage-full}


- **Errors**

    The Errors heat map shows the HTTP response codes of errors sent to the client by the API Gateway. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Errors by Status Code** graph.

    ![Errors](../assets/img/monitoring-and-insights/api-insights/error-heatmap.png){.cInlineImage-full}

- **Target Errors**

    The Target errors heat map shows the HTTP response codes of errors that the API Gateway received from the backend. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Target Errors by Status Code** graph.

    ![Target errors](../assets/img/monitoring-and-insights/api-insights/target-error-heatmap.png){.cInlineImage-full}

### Latency

The **Latency** page shows information related to the latency of API calls within the API management deployment. You can view a summary of the slowest APIs and then drill down into the API view for further analysis. Use this page as a starting point to debug API slowness.

![Latency](../assets/img/monitoring-and-insights/api-insights/latency-page-full.png){.cInlineImage-full}

The information displayed is as follows:

- **Top 10 Slowest APIs**

    This widget allows you to identify the slowest APIs of the API management system at a glance. Since these are the APIs that contribute to the higher 95th percentile of the system, improving these APIs lowers the 95th percentile of latency in the API Management deployments.

    ![Slowest APIs](../assets/img/monitoring-and-insights/api-insights/slowest-apis.png){.cInlineImage-full}

- **Latencies By Category**

    This widget allows you to further drill down details in the above chart. Use the API selector in this widget to select the slow API you identified in the earlier step and then analyze further. Use the charts available in the widget to view the 95th percentile and the median latency over the selected period of the following:

      - Backend
      - Request mediation
      - Response mediation

    ![Latencies by category](../assets/img/monitoring-and-insights/api-insights/latency-by-category.png){.cInlineImage-full}

  You can use these charts to further drill down and analyze whether the latency occurs in the backend, request mediation, or response mediation. Also, because you can see both the median and 95th percentile, you can easily identify whether the slowness is occurring in each request or whether it is intermittent.

### Cache

The **Cache** page shows statistics that indicate the efficiency with which response caching is carried out for the requests sent to your APIs.

![Cache statistics](../assets/img/monitoring-and-insights/api-insights/cache-page-full.png){.cInlineImage-full}

The page displays the following statistics:

- **Cache Hit Percentage**

    This graph shows the percentage of requests the system has handled via the response cache over time and the total hits over time. This information allows you to assess how efficiently the backend handles API requests. For example, if the cache hit rate is low, it may indicate that the backend generates the same response each time a specific request is sent instead of returning the response via the cache. In such a scenario, there is scope to improve performance via response caching.

    ![Cache hit percentage](../assets/img/monitoring-and-insights/api-insights/cache-statistics.png){.cInlineImage-full}

- **Latency**

    This section shows the total latency reported during the same time interval applied to the **Cache Hit Percentage** graph above.

    ![Cache hits and misses](../assets/img/monitoring-and-insights/api-insights/cache-latency.png){.cInlineImage-full}

### Devices

The **Devices** page displays information about operating systems and HTTP agents that end users use to invoke the APIs. You can use this page to get an idea of the distribution of your user base and improve your APIs to match the audience.

![Device statistics](../assets/img/monitoring-and-insights/api-insights/devices-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. **All** is selected by default.

The information displayed is as follows:

- **Top Platforms**

    This chart shows the breakdown of the API clients by the operating system. The pie chart only shows platforms with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top platforms](../assets/img/monitoring-and-insights/api-insights/top-platforms.png){.cInlineImage-half}

- **Top User Agents**

    This chart shows the breakdown of the API clients by user-agent. The pie chart only shows user agents with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top user agents](../assets/img/monitoring-and-insights/api-insights/top-user-agents.png){.cInlineImage-half}

### Alerts

The **Alerts** page shows information related to business alerts issued by Choreo for your currently selected environment and organization. You can use this page as a health monitoring dashboard and make it visible to your project team. Using this page you can drill down on each alert and discover possible anomalies in your published APIs. See the topics given below to get details of the available widgets and understand how to use them effectively.

![Alerts statistics](../assets/img/monitoring-and-insights/api-insights/alerts-page-full.png){.cInlineImage-full}

**Prerequisites**

To use this page, be sure to configure alerts and have API invocations that trigger alerts. 

!!! Note
    Alerts are retained only for a week.

- **Alert Summary**

    This table lists each alert generated during the selected time interval. The message of the alert can be viewed by expanding the arrow icon on the details column. The drop-downs can be used to filter alerts based on the alert type and API.

    ![Alert summary](../assets/img/monitoring-and-insights/api-insights/alert-summary.png){.cInlineImage-full}

- **Top APIs by Alert Count**

    This shows a pie chart and a table to visualize the alert distribution during the selected time interval.

    ![Top APIs by alert count](../assets/img/monitoring-and-insights/api-insights/top-apis-by-alert-count.png){.cInlineImage-full}

### Reports

The **Reports** page allows you to download monthly usage reports for your system. There are preconfigured reports with system-wide statistics, and a custom report generator to generate reports based on a subset of APIs/applications.

![Report page](../assets/img/monitoring-and-insights/api-insights/report-page-full.png){.cInlineImage-full}

#### Download custom reports

This widget allows you to generate a custom report for the statistics that have been generated up to now and download it.

![Custom report download](../assets/img/monitoring-and-insights/api-insights/custom-report.png){.cInlineImage-full}

To generate a custom report, follow the steps below:

1. In the **API** field, select one or more APIs for which you want to generate the report. If required, you can select all the APIs by selecting **All**.

2. If you need to further filter the content printed in the report, select one or more applications in the **Application** field. By default, all the applications that have subscribed to one or more of the selected APIs are selected.

    !!! Tip
        If you want to filter the report content by the API consumer instead of the application, click on the toggle switch to the right of the **Application** field, and then select the required consumer. Only consumers who have subscribed to one or more of the selected APIs are displayed in the list. You can either select one or all of them.

3. Select the required year and the month in the **Year** and **Month** fields to specify the time interval for which you want to generate the report.

4. Click **Download**, and select the required format.

The report is downloaded in the specified format. The following is a sample report generated in PDF format.

![Sample report](../assets/img/monitoring-and-insights/api-insights/custom-report-sample.png){.cInlineImage-half}

The contents of the report are as follows.

| **Item** | **Description** |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Generated Time**      | The date and the time the report was generated.                                            |
| **Organization**        | The organization to which the report applies. Each report always applies to a specific organization. |
| **Environment**         | The environment to which the report applies. Each report always applies to a specific environment.  |
| **Tenant**              | The tenant to which the report applies. Each report always applies to a specific tenant.            |
| **Reporting period**    | The time interval for which the report is generated.                                       |
| **Total request count** | The total request count received by all selected APIs during the report time interval.     |

The table in the report contains the following rows.

| **Item** | **Description** |
|-----------------------|------------------------------------------------------------------------------|
| **API**          | The name of the API.                                                         |
| **Application** | The name of the application. The name of the subscriber is also provided within brackets. |
| **Usage**       | The usage count.                                                           |

#### Download pregenerated reports

These widgets allow you to download monthly reports for the last three months.

![Pre-generated reports](../assets/img/monitoring-and-insights/api-insights/configured-report.png){.cInlineImage-half}

To download a pregenerated report, click **Download** for the relevant month and then click on the required format.

### Geo Map

The **Geo Map** page allows you to see a geographical representation of your API usage. You can use this page to make business decisions such as identifying growing regions, analyzing the impact of a region-specific marketing campaign, etc.

![Geo Map page](../assets/img/monitoring-and-insights/api-insights/geomap-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. The default value is **All**.

This heat map highlights the countries with the appropriate color based on the hit count. It uses a relative color scale to depict the highest hit count to the lowest non-zero hit count.

![Geo Map Hit Scale](../assets/img/monitoring-and-insights/api-insights/geomap-hit-count-scale.png){.cInlineImage-xsmall}

#### Viewing the number of requests by country

You can hold the pointer over the highlighted countries to view the country name and the total number of hits from that location. You can also use the mouse to zoom the map or pan it. Optionally, you can download geo-map data in a tabular format using the PDF or CSV download options by clicking ![download](../assets/img/monitoring-and-insights/api-insights/insights-download-report.svg) on the top right corner.

![Geo Map by country](../assets/img/monitoring-and-insights/api-insights/geomap-requests-by-country.png){.cInlineImage-half}

!!! Note
    -  Currently, this feature is only available for on-premises environments.
    - The geo-map page utilizes the IP address of the incoming request to derive the geolocation. The actual source IP address can be replaced if there are intermediate hosts between the client and the gateway node. Therefore, the reverse proxy or the load balancer fronting the gateway node must add the `x-forwarded-for` header to each request to preserve the source IP address. If you do not configure this correctly, the **Geo Map** page will not show any data. To test this, you can manually add an `x-forwarded-for` header to the request.


# Integrate Choreo with Moesif

Moesif is an API analytics and monetization service that helps you grow your API products. You can integrate Choreo with Moesif and gain valuable insights into your API's usage.  While Moesif's API analytics capabilities empower you to make informed decision-making on behalf of your organization, its monetization options simplify revenue generation from your APIs, eliminating the need for complex coding. 

In this guide, you will:

- Generate a key in Moesif.
- Configure Choreo to connect to Moesif.
- Invoke an API and observe the insights on the Moesif dashboard. 

## Step 1: Generate an API key in Moesif

Let's generate an API key in Moesif. 
If you're an existing Moesif user with a registered organization, proceed to [step 1.2](#step-12-access-the-api-key-in-moesif-as-an-existing-user).

### Step 1.1: Generate a key in Moesif as a new user 

If you are a new user, follow the steps below to register an organization and generate a key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click **Sign Up** and select an authentication option and proceed. 
3. On the **Get Started** page, enter meaningful values for the fields and create a new organization. 

    | Field                 |  Description                                            |
    |-----------------------|---------------------------------------------------------|
    | **Organization Name** |  The name of your company or team.                      |
    | **Application Name**  | The name of your application that represents one project or environment.   |

 4. Click **Next**.
 5. On the **Overview** page, click **Next**.

     This opens the **Quick Install** page. As there is no data, you cannot proceed. Let's configure Moesif to receive data from Choreo. 

 6. Select a **WSO2 Choreo** as the **Server Integration**
 7. Copy the **Application Id**. 
    
     ![First Time user API Key](../assets/img/monitoring-and-insights/first_time_key_moesif.png)
     

### Step 1.2: Access the API key in Moesif as an existing user

If you are an existing user with a registered organization, or you do not have an API key for the organization you created,  follow the steps below to access the generated API key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click on your profile in the bottom left corner, and navigate to the **API Keys** page.
3. Copy the **Collection Application Id**.


## Step 2: Integrate Choreo with Moesif

Let's configure Choreo to publish events to Moesif.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in.
2. On the left navigation, click **Settings**. 
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. Click the **API Management** tab, and click **Moesif Dashboard**.
5. Select the environment you want to publish data for.
6. Paste the **Application Id** you copied. 
7. Click **Add**.

Once you successfully add the key, you will see a delete option next to it. Currently, you can only configure one API key. If you need to add a new API key, you need to delete the existing key and add the new one. 

!!! Note
    Once you configure the Moesif API key on Choreo, **wait for five minutes before you publish any data to the Moesif** API analytics platform. 


## Step 3: Invoke an API and observe the data on the Moesif Dashboard 

You have configured Choreo to publish data to Moesif. Let's see how you can view the insights on Moesif.

!!! tip
    - If you have not created an API and deployed it on Choreo, you can follow the [create and deploy a REST API](https://wso2.com/choreo/docs/develop-components/develop-services/develop-a-rest-api/) guide to get started.

1. Invoke your API by following the [Test REST Endpoints via the OpenAPI Console](https://wso2.com/choreo/docs/testing/test-rest-endpoints-via-the-openapi-console/) guide. 

2. Once you publish data, your Moesif dashboard will receive events. Once Moesif receives events, you will see a notification on Moesif confirming that it received data. 

    ![Data Recieved Moesif Notification](../assets/img/monitoring-and-insights/data_recieved_moesif_notification.png){.cInlineImage-small}

3. Click **Next** on the notification. This will take you to the final step, where you can opt to add team members. In this guide, let's skip this step. 
4. Click **Finish**.

You can now view your API's insights in the Moesif dashboard. 


 # Alert Overview

This section explains how you can configure alerts for your Choreo components. Setting up alerts allows you to proactively monitor your components ecosystem and take corrective measures when necessary.

!!! tip
    Setting up alerts in only available in the component level.

## Alert Types

Choreo supports the following types of alerts to help you monitor and manage your components effectively:

- [Latency alerts](#latency-alerts)
- [Traffic alerts](#traffic-alerts)
- [Resource alerts](#resource-alerts)
- [Log alerts](#log-alerts)
- [Build failure alerts](#build-failure-alerts)
- [Status code alerts](#status-code-alerts)

### Latency Alerts

Latency alerts notify you if the response latency of a component exceeds a predefined threshold in a given time period. This is useful for components that need to meet specific SLAs and for proactively identifying slow components.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | 99th, 95th, 90th, or 50th percentile.                                           |
| Threshold     | Latency in milliseconds (e.g.: 1800).                                           |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

### Traffic Alerts

Traffic alerts notify you when the request count of a component exceeds a predefined threshold. This is useful for managing components with backend traffic limits or monetized backends that require proactive scaling based on incoming traffic.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Threshold     | Requests per minute (e.g.: 200).                                                |
| Period        | Monitoring window (e.g.: 5 minutes).                                            |

### Resource Alerts

Resource alerts notify you when your component’s CPU or memory usage exceeds the defined thresholds. This ensures you can fix the resources allocations early to avoid performance issues or downtimes.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Metric        | CPU or Memory.                                                                  |
| Threshold     | **mCPU** for CPU and **MiB** for Memory(e.g.: 1000).                            |
| Period        | Duration the threshold must be exceeded (e.g.: 5 minutes).                      |

!!! Tip
    - **CPU**: mCPU (milliCPU) measures CPU usage in fractions of a core, where 1000m = 1 full core.
    - **Memory**: MiB (Mebibyte) measures memory in binary units, where 1 MiB = 2^20^ bytes.

### Log Alerts

Log alerts trigger notifications when a specific phrase appears **a specific number of times** in your component logs within a defined Time window. This helps to identify recurring issues or critical errors quickly, enabling faster troubleshooting.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Search Phrase | Keyword or phrase to look for to trigger the alert (e.g.: failed).                                               |
| Count         | Minimum number of occurrences to trigger the alert (e.g.: 10).                  |
| Interval      | Time window for counting occurrences (e.g.: 5 minutes).                         |

### Build Failure Alerts

Build failure alerts inform you if a build failure occurs for your component. This is essential for maintaining smooth development workflows.

### Status Code Alerts

Status code alert triggers when your component returns specific HTTP error(s) (e.g.: **403** Forbidden, **500** Internal Error). These alerts help to detect issues affecting your component’s availability.

Configurable parameters

| **Parameter** | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| Status Code   | Error code or series (e.g.: 400:Bad Request).                                   |
| Count         | Minimum number of occurrences (e.g.: 5).                                        |
| Interval      | Time window (e.g.: 5 minutes).                                                  |

!!! note
    Status code alerts are only supported for API proxy component types.

## Configure Alert

Follow these steps to configure an alert:

1. Navigate to the component you wish to configure alerts for.

    !!! info
        You need to have a scope of **Choreo DevOps** or **Choreo Platform Engineer** inorder to create Alerts.  

2. In the Choreo left menu, click **Observability** and then click **Alerts**.
3. Click **Create Alert Rule** to create a new alert rule.

    ![Create Alert Rule](../assets/img/monitoring-and-insights/alerts/alert-creation.png){.cInlineImage-full}

4. Select the **[Alert Type](#alert-types)** you want to create.
5. Select the **Environment** you want to create the alert for.
6. Select the **Deployment Track** or **Version** as required for the component.
7. Configure the remaining fields specific to your selected alert type.
8. In the **Emails** field, specify the list of emails that should be notified when the alert is triggered.

    !!! note
        - When adding an email, enter the required email and press enter to add it.
        - You can add a maximum of 5 email addresses per alert.

9. You can configure additional parameters in **Advanced Configurations** dropdown as needed, which vary based on your alert type.
10. The **Explanation window** provides a concise summary of the configured alert based on your alert configurations.
11. Click **Create** to save and activate your alert rule.

    !!! info
        - You can configure a maximum of 10 alerts per component.

12. Once successfully added, your alert will be listed in the **Configure Alerts** pane alongside any existing alerts for the component.
13. Each alert can be **edited**, **removed** and **disabled** or **enabled** via this pane.

    !!! note
        when editing an alert, you can't edit the **Alert Type**, **Environment** and **Deployment Track**.

## Alert History & Notifications

### View Alert History

You can check the past alerts that have triggered for your component when you click the  **Alerts History** pane in Choreo Alerts. You can filter the alert history by **Alert Type**, **Environment**, **Deployment Track** or **Version** and **Time Range**.

!!! note  
    When filtering, **API Proxy components** show a **Version** filter and other components display a **Deployment Track** filter, based on their monitoring context.  

You can click on an alert to expand it and see more details of the triggered alert.

### Email Notifications

When an alert is triggered, **recipients** added to the alert rule receive an email with **alert details** including a direct **Alert View link** to Choreo console.

![Email Notification](../assets/img/monitoring-and-insights/alerts/email-notification.png){.cInlineImage-full}


# Generate Custom Reports

Choreo insights allow you to generate custom reports to view the information that is important to you to make timely decisions for the betterment of your business. With custom reports, you can generate reports for a set of metrics of your choice and aggregate results by specific fields. Once generated, the metrics can be filtered out using any selected group-by filters. Custom reports support three visualizations: overtime charts, pie charts, and tables.

## Metrics

Choreo Insights allow you to retrieve data for the following metrics:

 - Successful Hit Count
 - Response Cache Hits
 - Request Mediation Latency
 - Response Mediation Latency
 - Backend Latency
 - Total Latency
 - API Errors
 - Target Errors

## Group-by

**Group-by** fields specify how to group the metric data. e.g., You can select **Successful Hit Count** in the **Metrics** field and **API Name** under **Group-by** to retrieve the successful hit count grouped by the API name.

Choreo Insights allow you to group metric data by the following fields:

 - API Name
 - API Version
 - API Resource Template
 - API Method
 - API Creator
 - Application
 - Application Owner
 - Destination
 - User Agent
 - Platform

To generate a custom report, follow the steps below:

1. In the left navigation menu, click **Custom Reports**.

    ![Select Custom Reports](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-1.png){.cInlineImage-full}

2. Select metric(s) from the **Metrics** drop-down selector.

    ![Generate report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-2-to-4.png){.cInlineImage-full}

3. Select a minimum of 1 and a maximum of 3 group-by field(s) from the **Group By** drop down selector.

4. Set the order of the group-by filters by drag and drop to determine the grouping order of the selected metric(s).

5. Once you determine the order of the group-by fields, you can set values for each group-by field from the respective dropdown. 

    ![Group by field selection](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-5.png){.cInlineImage-full}

6. Click **Generate**.

    ![Generate](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-6.png){.cInlineImage-full}

## Download Reports

Choreo Insights allow you to download report data related to each chart as a **PDF** or a **CSV** file.

To do this, click the **Download** icon on the top right of the relevant chart and select the required file format.
    ![Download Report](../assets/img/monitoring-and-insights/api-insights/custom-reports-step-7.png){.cInlineImage-full}


# Insights Overview

Choreo provides comprehensive insights into APIs created within both the on-premises API Manager and the Choreo platform. Choreo insights provide a range of metrics, including API traffic, error rates, and latency, allowing you to monitor and optimize API performance effectively.

With Choreo insights, you can:

- **Analyze API traffic**: Monitor the volume of requests and responses to understand usage patterns.
- **Track errors**: Identify and analyze errors to improve API reliability.
- **Monitor latency**: Measure and optimize the response times of your APIs.
- **Generate reports**: Generate detailed reports to keep stakeholders informed and support data-driven decision-making.
- **Configure alerts**: Set up alerts for specific events or thresholds to proactively manage API performance.
- **Obtain granular insights**: Obtain detailed information on a per-application, per-API, and per-user basis for more targeted analysis.
- **Drill down into data**: Dive deeper into data to perform root cause analysis.

By leveraging these insights, businesses can make informed decisions to enhance their API strategies and drive their digital transformation initiatives forward.

## View insights

To view usage insights, go to the [Choreo Console](https://console.choreo.dev/) and click **Insights** and then click **Usage** in the left navigation menu.

If you are viewing insights on the Choreo platform at the organization level, note the following:

- **Permission-based access**: Signed-in users can only view insights for components or projects that they have permission to access.
- **Data exclusion**: Insights exclude data from components you cannot access and the data related to deleted components.
- **Comprehensive view permission**: To view insights for all components, including deleted ones, across the organization regardless of project visibility, you must have the `View Organization Insights` permission under `OBSERVABILITY-MANAGEMENT` with the mapping level defined at the `Organization` level.
- **Admin role**: Users with the admin role have the `View Organization Insights` permission by default and can view organization-wide insights.
- **Configuring permissions**: For detailed steps on configuring permissions, see [Control Access in the Choreo Console](/choreo/docs/administer/control-access-in-the-choreo-console/).

By ensuring proper permissions are set, organizations can manage access to insights effectively while maintaining data security and relevance.

## Analyze statistics

Once you access the **Usage Insights** page, you can access the following subpages.

### Overview

The **Overview** page gives you a quick overview of the system status.

![Overview](../assets/img/monitoring-and-insights/api-insights/overview.png){.cInlineImage-full}

The information displayed is as follows:

- **Total Traffic**

    ![Total traffic](../assets/img/monitoring-and-insights/api-insights/overview-page-total-traffic.png){.cInlineImage-small}

    This widget displays the total traffic of the selected environment received during a given time interval. Both successful requests and failed requests are displayed. To investigate further, you can click the arrow icon on the bottom right corner of the widget to open the [**Traffic**](#traffic) page.

- **Error Request Count**

    ![Error request count](../assets/img/monitoring-and-insights/api-insights/overview-page-error-request-count.png){.cInlineImage-small}

    This widget displays the total number of requests that have resulted in errors in your selected environment during the selected time range.

- **Average Error Rate**

    ![Average error rate](../assets/img//monitoring-and-insights/api-insights/overview-page-error-rate.png){.cInlineImage-small}

    This widget displays the average error rate (i.e., error count/total request count) of the selected environment for a given time interval. You can use this widget as an indicator to understand the health of the system. If the error rate is high, you can investigate further by clicking the arrow on the bottom right of the widget and opening the [**Errors**](#errors) page.

- **95th Percentile Latency**

    ![95th percentile latency](../assets/img/monitoring-and-insights/api-insights/overview-page-latency.png){.cInlineImage-small}

    This widget displays the 95th percentile of all API latencies in your selected environment for the given time interval. You can use this widget to know whether the complete system operates under given SLAs. This metric provides the first indication of slow APIs. To investigate further, you can click the arrow on the bottom right of the widget to open the [**Latency**](#latency) page where you can further analyze the latency.

- **API Request Summary**

    ![API request summary](../assets/img/monitoring-and-insights/api-insights/overview-page-timeline.png){.cInlineImage-full}

    This chart displays the total successful requests, the total requests that have resulted in errors, and the latency in a timeline. The y-axis on the left displays the request count and the error count. The x-axis shows time, and the y-axis on the right shows the latency in milliseconds. The granularity of the data points is decided based on the time range you have selected. The tooltip provides the exact value of all three metrics accurately.

### Traffic

The **Traffic** page shows information related to the traffic that goes through your API management deployments. This includes API usage, application usage, resource usage, etc. You can use this page to investigate the usage of APIs and applications, traffic patterns, etc.

![Traffic](../assets/img/monitoring-and-insights/api-insights/traffic-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API**         | In the **API** field, you can select one or more APIs for which you want to view analytics. **All** is selected by default. Once you select an API, you can further filter by a specific application that uses the selected API via the **Application** field described below. |
| **By Application** | In the **Application** field, you can select the applications for which you want to view analytics. **All** is selected by default. The available applications are all the applications that have subscribed to one or more of the APIs you selected in the **API** field.|

You can view the following information for the APIs you have selected using the above filtering criteria:

- **API Usage Over Time**

     This timeline shows the count of API hits for the APIs for the filtered APIs. If multiple APIs are selected, the timeline shows each API in a separate line with a legend separating each line. You can also zoom in on a selected time range by selecting that area in the chart. To restore to the original view use the **Zoom out** button on the top right-hand corner of the plot.

    ![API usage over time](../assets/img/monitoring-and-insights/api-insights/api-usage-timeline.png){.cInlineImage-full}

- **API Usage By Application**

     This widget shows the per-application breakdown of requests for the APIs you selected. You can use the pie chart view or the line chart view. You can switch between the two views using the small icon at the upper-right corner of the widget.

    ![API usage by application](../assets/img/monitoring-and-insights/api-insights/usage-by-application.png){.cInlineImage-half}

- **API Usage By Target**

     This widget shows the per-backend breakdown of requests for the APIs you selected. This information is useful when multiple APIs share the same backend that has traffic restrictions. You can use these stats to scale your backends proactively. You can switch between the two views using the small icon at the upper-right corner of the widget.

     ![API usage by target](../assets/img/monitoring-and-insights/api-insights/usage-by-target.png){.cInlineImage-half}

- **API Resource Usage**

     This table shows a resource-level breakdown of API traffic. Each row represents an API resource and it shows the API name, resource path, API method, and the hit count for that combination.

     ![API resource usage](../assets/img/monitoring-and-insights/api-insights/resource-usage.png){.cInlineImage-full}

### Errors

The **Errors** page shows information related to erroneous API calls that are received by your system. The errors are categorized based on the error type. You can further drill down using the error subtypes. Use this page as the starting point for debugging any API errors.

![Error statistics](../assets/img/monitoring-and-insights/api-insights/error-page-full.png){.cInlineImage-full}

You can filter the information displayed in the widgets as follows:

| **Filtering Option** | **Description** |
|--------------------|-------------------------------------------------------------------------------------------------|
| **By API** | In the **API** field, select the APIs for which you want to view analytics. By default, all APIs are selected. You can select one or multiple APIs from this selector and view the aggregated result. |
| **By Category** | The **Category** field is displayed when you click **Category** in the upper right corner of the page. In this field, you can select one or all of the following error categories:<br/>**Authentication**: Any kind of authentication error falls into this category including expired/missing/invalid credentials.<br/>**Target Connectivity**: Any kind of back-end error falls into this category including connection time-outs/other back-end errors (for example, 4xx and 5xx status codes).<br/>**Throttling**: Any request that fails due to rate-limiting falls into this category including application throttling/subscription throttling.<br/>**Other**: All other errors fall into this category including mediation errors/resource not found errors. |
| **By Status Code** | The **Status Code** field is displayed when you click **Status Code** in the upper right corner of the page. In this field, you can select all or any available HTTP status code categories (4xx, 5xx, etc.). These status codes represent the response status of the API Gateway. |

#### Viewing errors by category

The following widgets are available for monitoring errors when you have selected **Category** in the upper-right corner of the page.

- This graph shows the error by category over time for the selected period. Apply the required filters as explained above to select the APIs and the error categories to which this content applies. When you select multiple APIs, the error count is grouped by category.

    ![Errors by category graph](../assets/img/monitoring-and-insights/api-insights/error-category-graph.png){.cInlineImage-full}

- This table provides further information about the errors such as application details and the error reason. For some authentication errors, the application name is not available. You can use this table to get more concrete information about the errors related to your APIs and then start the problem identification.

    ![Errors by category table](../assets/img/monitoring-and-insights/api-insights/error-category-table.png){.cInlineImage-full}

#### Viewing errors by status code

The following widgets are available for monitoring errors when you select **Status Code** in the upper-right corner of the page.

- **Errors by Status Code**

    This graph shows the distribution of HTTP status codes received for errors over time for the selected period. Apply the required filters as explained above to select the APIs and status code groups to which this content applies. When you select multiple APIs, the error count is grouped by the status code.

    ![Errors by status code](../assets/img/monitoring-and-insights/api-insights/error-by-status-code.png){.cInlineImage-full}

- **Target Errors by Status Code**

    This graph shows the distribution of target errors that have occurred during the selected time interval by HTTP status code. Apply the required filters as explained in the table above to view the APIs and status code groups to which this content applies. If you select multiple APIs, the widget groups the target error count by the status code.

    ![Target errors by status code](../assets/img/monitoring-and-insights/api-insights/target-error-by-status-code.png){.cInlineImage-full}


- **Errors**

    The Errors heat map shows the HTTP response codes of errors sent to the client by the API Gateway. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Errors by Status Code** graph.

    ![Errors](../assets/img/monitoring-and-insights/api-insights/error-heatmap.png){.cInlineImage-full}

- **Target Errors**

    The Target errors heat map shows the HTTP response codes of errors that the API Gateway received from the backend. Each row displays the number of times the system returned each status code for the selected APIs. The cell color is red for higher numbers and white for lower numbers. If required, you can further filter the results by the error code groups you identified with the **Target Errors by Status Code** graph.

    ![Target errors](../assets/img/monitoring-and-insights/api-insights/target-error-heatmap.png){.cInlineImage-full}

### Latency

The **Latency** page shows information related to the latency of API calls within the API management deployment. You can view a summary of the slowest APIs and then drill down into the API view for further analysis. Use this page as a starting point to debug API slowness.

![Latency](../assets/img/monitoring-and-insights/api-insights/latency-page-full.png){.cInlineImage-full}

The information displayed is as follows:

- **Top 10 Slowest APIs**

    This widget allows you to identify the slowest APIs of the API management system at a glance. Since these are the APIs that contribute to the higher 95th percentile of the system, improving these APIs lowers the 95th percentile of latency in the API Management deployments.

    ![Slowest APIs](../assets/img/monitoring-and-insights/api-insights/slowest-apis.png){.cInlineImage-full}

- **Latencies By Category**

    This widget allows you to further drill down details in the above chart. Use the API selector in this widget to select the slow API you identified in the earlier step and then analyze further. Use the charts available in the widget to view the 95th percentile and the median latency over the selected period of the following:

      - Backend
      - Request mediation
      - Response mediation

    ![Latencies by category](../assets/img/monitoring-and-insights/api-insights/latency-by-category.png){.cInlineImage-full}

  You can use these charts to further drill down and analyze whether the latency occurs in the backend, request mediation, or response mediation. Also, because you can see both the median and 95th percentile, you can easily identify whether the slowness is occurring in each request or whether it is intermittent.

### Cache

The **Cache** page shows statistics that indicate the efficiency with which response caching is carried out for the requests sent to your APIs.

![Cache statistics](../assets/img/monitoring-and-insights/api-insights/cache-page-full.png){.cInlineImage-full}

The page displays the following statistics:

- **Cache Hit Percentage**

    This graph shows the percentage of requests the system has handled via the response cache over time and the total hits over time. This information allows you to assess how efficiently the backend handles API requests. For example, if the cache hit rate is low, it may indicate that the backend generates the same response each time a specific request is sent instead of returning the response via the cache. In such a scenario, there is scope to improve performance via response caching.

    ![Cache hit percentage](../assets/img/monitoring-and-insights/api-insights/cache-statistics.png){.cInlineImage-full}

- **Latency**

    This section shows the total latency reported during the same time interval applied to the **Cache Hit Percentage** graph above.

    ![Cache hits and misses](../assets/img/monitoring-and-insights/api-insights/cache-latency.png){.cInlineImage-full}

### Devices

The **Devices** page displays information about operating systems and HTTP agents that end users use to invoke the APIs. You can use this page to get an idea of the distribution of your user base and improve your APIs to match the audience.

![Device statistics](../assets/img/monitoring-and-insights/api-insights/devices-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. **All** is selected by default.

The information displayed is as follows:

- **Top Platforms**

    This chart shows the breakdown of the API clients by the operating system. The pie chart only shows platforms with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top platforms](../assets/img/monitoring-and-insights/api-insights/top-platforms.png){.cInlineImage-half}

- **Top User Agents**

    This chart shows the breakdown of the API clients by user-agent. The pie chart only shows user agents with a significant amount of requests. Other platforms are grouped under the **Other** category.

    ![Top user agents](../assets/img/monitoring-and-insights/api-insights/top-user-agents.png){.cInlineImage-half}

### Alerts

The **Alerts** page shows information related to business alerts issued by Choreo for your currently selected environment and organization. You can use this page as a health monitoring dashboard and make it visible to your project team. Using this page you can drill down on each alert and discover possible anomalies in your published APIs. See the topics given below to get details of the available widgets and understand how to use them effectively.

![Alerts statistics](../assets/img/monitoring-and-insights/api-insights/alerts-page-full.png){.cInlineImage-full}

**Prerequisites**

To use this page, be sure to configure alerts and have API invocations that trigger alerts. 

!!! Note
    Alerts are retained only for a week.

- **Alert Summary**

    This table lists each alert generated during the selected time interval. The message of the alert can be viewed by expanding the arrow icon on the details column. The drop-downs can be used to filter alerts based on the alert type and API.

    ![Alert summary](../assets/img/monitoring-and-insights/api-insights/alert-summary.png){.cInlineImage-full}

- **Top APIs by Alert Count**

    This shows a pie chart and a table to visualize the alert distribution during the selected time interval.

    ![Top APIs by alert count](../assets/img/monitoring-and-insights/api-insights/top-apis-by-alert-count.png){.cInlineImage-full}

### Reports

The **Reports** page allows you to download monthly usage reports for your system. There are preconfigured reports with system-wide statistics, and a custom report generator to generate reports based on a subset of APIs/applications.

![Report page](../assets/img/monitoring-and-insights/api-insights/report-page-full.png){.cInlineImage-full}

#### Download custom reports

This widget allows you to generate a custom report for the statistics that have been generated up to now and download it.

![Custom report download](../assets/img/monitoring-and-insights/api-insights/custom-report.png){.cInlineImage-full}

To generate a custom report, follow the steps below:

1. In the **API** field, select one or more APIs for which you want to generate the report. If required, you can select all the APIs by selecting **All**.

2. If you need to further filter the content printed in the report, select one or more applications in the **Application** field. By default, all the applications that have subscribed to one or more of the selected APIs are selected.

    !!! Tip
        If you want to filter the report content by the API consumer instead of the application, click on the toggle switch to the right of the **Application** field, and then select the required consumer. Only consumers who have subscribed to one or more of the selected APIs are displayed in the list. You can either select one or all of them.

3. Select the required year and the month in the **Year** and **Month** fields to specify the time interval for which you want to generate the report.

4. Click **Download**, and select the required format.

The report is downloaded in the specified format. The following is a sample report generated in PDF format.

![Sample report](../assets/img/monitoring-and-insights/api-insights/custom-report-sample.png){.cInlineImage-half}

The contents of the report are as follows.

| **Item** | **Description** |
|-------------------------|--------------------------------------------------------------------------------------------|
| **Generated Time**      | The date and the time the report was generated.                                            |
| **Organization**        | The organization to which the report applies. Each report always applies to a specific organization. |
| **Environment**         | The environment to which the report applies. Each report always applies to a specific environment.  |
| **Tenant**              | The tenant to which the report applies. Each report always applies to a specific tenant.            |
| **Reporting period**    | The time interval for which the report is generated.                                       |
| **Total request count** | The total request count received by all selected APIs during the report time interval.     |

The table in the report contains the following rows.

| **Item** | **Description** |
|-----------------------|------------------------------------------------------------------------------|
| **API**          | The name of the API.                                                         |
| **Application** | The name of the application. The name of the subscriber is also provided within brackets. |
| **Usage**       | The usage count.                                                           |

#### Download pregenerated reports

These widgets allow you to download monthly reports for the last three months.

![Pre-generated reports](../assets/img/monitoring-and-insights/api-insights/configured-report.png){.cInlineImage-half}

To download a pregenerated report, click **Download** for the relevant month and then click on the required format.

### Geo Map

The **Geo Map** page allows you to see a geographical representation of your API usage. You can use this page to make business decisions such as identifying growing regions, analyzing the impact of a region-specific marketing campaign, etc.

![Geo Map page](../assets/img/monitoring-and-insights/api-insights/geomap-page-full.png){.cInlineImage-full}

To filter the information displayed on this page by API, select the required API(s) in the **API** field. The default value is **All**.

This heat map highlights the countries with the appropriate color based on the hit count. It uses a relative color scale to depict the highest hit count to the lowest non-zero hit count.

![Geo Map Hit Scale](../assets/img/monitoring-and-insights/api-insights/geomap-hit-count-scale.png){.cInlineImage-xsmall}

#### Viewing the number of requests by country

You can hold the pointer over the highlighted countries to view the country name and the total number of hits from that location. You can also use the mouse to zoom the map or pan it. Optionally, you can download geo-map data in a tabular format using the PDF or CSV download options by clicking ![download](../assets/img/monitoring-and-insights/api-insights/insights-download-report.svg) on the top right corner.

![Geo Map by country](../assets/img/monitoring-and-insights/api-insights/geomap-requests-by-country.png){.cInlineImage-half}

!!! Note
    -  Currently, this feature is only available for on-premises environments.
    - The geo-map page utilizes the IP address of the incoming request to derive the geolocation. The actual source IP address can be replaced if there are intermediate hosts between the client and the gateway node. Therefore, the reverse proxy or the load balancer fronting the gateway node must add the `x-forwarded-for` header to each request to preserve the source IP address. If you do not configure this correctly, the **Geo Map** page will not show any data. To test this, you can manually add an `x-forwarded-for` header to the request.


# Integrate Choreo with Moesif

Moesif is an API analytics and monetization service that helps you grow your API products. You can integrate Choreo with Moesif and gain valuable insights into your API's usage.  While Moesif's API analytics capabilities empower you to make informed decision-making on behalf of your organization, its monetization options simplify revenue generation from your APIs, eliminating the need for complex coding. 

In this guide, you will:

- Generate a key in Moesif.
- Configure Choreo to connect to Moesif.
- Invoke an API and observe the insights on the Moesif dashboard. 

## Step 1: Generate an API key in Moesif

Let's generate an API key in Moesif. 
If you're an existing Moesif user with a registered organization, proceed to [step 1.2](#step-12-access-the-api-key-in-moesif-as-an-existing-user).

### Step 1.1: Generate a key in Moesif as a new user 

If you are a new user, follow the steps below to register an organization and generate a key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click **Sign Up** and select an authentication option and proceed. 
3. On the **Get Started** page, enter meaningful values for the fields and create a new organization. 

    | Field                 |  Description                                            |
    |-----------------------|---------------------------------------------------------|
    | **Organization Name** |  The name of your company or team.                      |
    | **Application Name**  | The name of your application that represents one project or environment.   |

 4. Click **Next**.
 5. On the **Overview** page, click **Next**.

     This opens the **Quick Install** page. As there is no data, you cannot proceed. Let's configure Moesif to receive data from Choreo. 

 6. Select a **WSO2 Choreo** as the **Server Integration**
 7. Copy the **Application Id**. 
    
     ![First Time user API Key](../assets/img/monitoring-and-insights/first_time_key_moesif.png)
     

### Step 1.2: Access the API key in Moesif as an existing user

If you are an existing user with a registered organization, or you do not have an API key for the organization you created,  follow the steps below to access the generated API key:

1. Go to [https://www.moesif.com/](https://www.moesif.com/).
2. Click on your profile in the bottom left corner, and navigate to the **API Keys** page.
3. Copy the **Collection Application Id**.


## Step 2: Integrate Choreo with Moesif

Let's configure Choreo to publish events to Moesif.

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/cloud-native-app-developer) and sign in.
2. On the left navigation, click **Settings**. 
3. In the header, click the **Organization** list. This will open the organization level settings page. 
4. Click the **API Management** tab, and click **Moesif Dashboard**.
5. Select the environment you want to publish data for.
6. Paste the **Application Id** you copied. 
7. Click **Add**.

Once you successfully add the key, you will see a delete option next to it. Currently, you can only configure one API key. If you need to add a new API key, you need to delete the existing key and add the new one. 

!!! Note
    Once you configure the Moesif API key on Choreo, **wait for five minutes before you publish any data to the Moesif** API analytics platform. 


## Step 3: Invoke an API and observe the data on the Moesif Dashboard 

You have configured Choreo to publish data to Moesif. Let's see how you can view the insights on Moesif.

!!! tip
    - If you have not created an API and deployed it on Choreo, you can follow the [create and deploy a REST API](https://wso2.com/choreo/docs/develop-components/develop-services/develop-a-rest-api/) guide to get started.

1. Invoke your API by following the [Test REST Endpoints via the OpenAPI Console](https://wso2.com/choreo/docs/testing/test-rest-endpoints-via-the-openapi-console/) guide. 

2. Once you publish data, your Moesif dashboard will receive events. Once Moesif receives events, you will see a notification on Moesif confirming that it received data. 

    ![Data Recieved Moesif Notification](../assets/img/monitoring-and-insights/data_recieved_moesif_notification.png){.cInlineImage-small}

3. Click **Next** on the notification. This will take you to the final step, where you can opt to add team members. In this guide, let's skip this step. 
4. Click **Finish**.

You can now view your API's insights in the Moesif dashboard. 


# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.azure.com/.
2. Follow the [AWS Analyzing Log Data documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and open **Log Insights**.
3. Select the relevant region and the relevant log group (the log group string has the cluster name and “/application” appended at the end).
4. Select the required time range. 
4. Copy the query below and paste it into the query editor. 
5. Replace the `<RELEASE_ID>` with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
6. Run the query to extract the logs.

```  SQL 
fields @timestamp, @message
| filter kubernetes.labels.release_id == "<RELEASE_ID>"
| filter @message like "<OPTIONAL SEARCH PHRASE>"
```


# Access the Choreo Insights API

The **Usage Insights** page in the Choreo Console displays data retrieved from the Insights API exposed over the Internet. However, in some scenarios, you may need to retrieve data from external systems and implement custom dashboards to display the data.

Choreo provides a secure and user-friendly approach to accomplish this requirement. Follow the steps given below:

## Become a member of the Choreo System organization

1. Access the Developer Portal of the `Choreo System` organization via [https://devportal.choreo.dev/choreosystem/applications](https://devportal.choreo.dev/choreosystem/applications) and sign in using your preferred method.
   
2. To obtain access to the `Choreo System` organization, click **Request Access**.

    ![Request access](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/request-access.png){.cInlineImage-full}

## Create an application and generate keys

To create an application and generate keys, follow the steps below:

1. To create a new application in the `Choreo System` organization, click **+ Create Application**. 

2. Enter a name for the application and click **Create**. This creates the application and takes you to the **Overview** page.

3. To subscribe to the **Insights** API via the newly created application, follow the steps below:
    1.  In the left navigation menu, click **Subscriptions**.
    2.  In the **Subscription Management** pane, click **+ Add APIs**.
    3.  Search for `Insights` and click **Add**.

4. To generate credentials for the application, follow the steps given below:
    1. In the left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates tokens and populates the **Consumer Key** and **Consumer Secret** fields in the **Application Keys** pane.

5. To specify an appropriate token expiry time for the application, follow the steps given below:
    1. In the **Application Keys** pane, click to expand **Advanced Configurations**.
    2. Specify an appropriate value in the **Application access token expiry time** field and click **Update**.
   
        ![Update token expiry time](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/update-token-expirary-time.png){.cInlineImage-threeQuarter}

6. Execute the following cURL command to generate an access token:

    ```bash
    curl --location --request POST 'https://sts.choreo.dev/oauth2/token' \
    --header 'Authorization: Basic <BASE64_ENCODED_CONSUMER_KEY_AND_CONSUMER_SECRET_OF_YOUR_APP_HERE>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'orgHandle=<YOUR_ORG_HANDLE_HERE>' \
    --data-urlencode 'scope=apim:api_manage'
    ```

    !!! info
        To obtain your organization handle, follow the steps given below:

         1. Go to [https://console.choreo.dev](https://console.choreo.dev) and sign in using your preferred method.
         2. In the Choreo Console, click your username in the top right corner.
         3. In the drop-down menu, click **Settings**.
         4. In the **Organization** pane, click **Copy Handle**. 

    You can use the generated token to access the Insights API exposed via [https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api](https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api).

    The following is a sample cURL command to invoke the Insights API:

    ```bash
    curl --location --request POST 'https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <TOKEN_HERE>' \
    --data-raw '{"query":"query ($org: OrgFilter!) {listEnvironments(org: $org){id\n name}}","variables":{"org":{"orgId":"<ORG_UUID_HERE>"}}}'
    ```

    !!! tip
         - When the token expires, you can generate a new token programmatically by making an API call to the token endpoint using the client credentials grant type.
        - If a token theft occurs, you can revoke the token by making an API call to the revoke endpoint.

        ![Endpoints](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/endpoints.png){.cInlineImage-threeQuarter}


# Choreo Insights API

The Choreo Insights API is a GraphQL API that allows you to retrieve data from external systems based on specific criteria. This guide describes the operations and schema-defined types you can use to retrieve data via the Choreo Insights API.

 - **Allowed operations:** [Queries](#query)
 - **Schema-defined types:** [Objects](#objects), [Inputs](#inputs), [Enums](#enums), and [Scalars](#scalars)

##Try out

You can try out the Choreo Insights API with your data via [GraphQL Explorer](graphiql-explorer/index.html).

!!! warning
    The GraphQL Explorer is currently not compatible with the Safari web browser due to a [known issue](https://developer.apple.com/forums/thread/658688).

## Query
The query root of the Choreo Insights GraphQL API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>listAllAPI</strong></td>
<td valign="top">[<a href="#api">API</a>]</td>
<td>

Fetches all the APIs with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>provider</code> parameter to further filter the APIs by a specific provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">provider</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the API provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listApplications</strong></td>
<td valign="top">[<a href="#application">Application</a>]</td>
<td>

Fetches all the applications with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>applicationFilter</code> parameter to further filter the applications by a specific application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">applicationFilter</td>
<td valign="top"><a href="#applicationfilter">ApplicationFilter</a></td>
<td>

The application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listProviders</strong></td>
<td valign="top">[<a href="#provider">Provider</a>]</td>
<td>

Fetches all the API providers with the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listSubscribers</strong></td>
<td valign="top">[<a href="#subscriber">Subscriber</a>]</td>
<td>

Fetches all the API subscribers with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>subscriberFilter</code> parameter to further filter the subscribers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscriberFilter</td>
<td valign="top"><a href="#subscriberfilter">SubscriberFilter</a></td>
<td>

The subscriber filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listOrganizations</strong></td>
<td valign="top">[<a href="#organization">Organization</a>]</td>
<td>

Fetches all the organizations of a user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listEnvironments</strong></td>
<td valign="top">[<a href="#environment">Environment</a>]</td>
<td>

Fetches all the environments of an organization.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">org</td>
<td valign="top"><a href="#orgfilter">OrgFilter</a>!</td>
<td>

The organization filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">projectId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listTenants</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

Fetches all the tenants with the given combination of environment ID and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tenantDataFilter</td>
<td valign="top"><a href="#tenantdatafilter">TenantDataFilter</a>!</td>
<td>

The tenant filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTraffic</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total traffic during the given time range for the specified combination of tenant ID, environment ID,
and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrors</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total number of errors that occurred during the given time range for the specified combination of tenant
ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatency</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Returns the overall response latency (95th percentile value) during the given time range for the specified
combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatencySummary</strong></td>
<td valign="top"><a href="#latencysummary">LatencySummary</a></td>
<td>

Returns the response latency value (95th percentile value) for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>latencySummaryFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencySummaryFilter</td>
<td valign="top"><a href="#latencysummaryfilter">LatencySummaryFilter</a></td>
<td>

The latency summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessSummary</strong></td>
<td valign="top"><a href="#successsummary">SuccessSummary</a></td>
<td>

Returns the number of successful (2xx response code) hit count for each time granularity within the specified time
range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorSummary</strong></td>
<td valign="top"><a href="#errorsummary">ErrorSummary</a></td>
<td>

Returns the number of unsuccessful hits (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID. Optionally, you can configure the <code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByCategory</strong></td>
<td valign="top"><a href="#errorsbycategory">ErrorsByCategory</a></td>
<td>

Returns the number of proxy errors (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) by each error category
for each time granularity within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>errorsByCategoryFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByCategoryFilter</td>
<td valign="top"><a href="#errorsbycategoryfilter">ErrorsByCategoryFilter</a></td>
<td>

The errors by category filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsDetails</strong></td>
<td valign="top"><a href="#detailsoferrors">DetailsOfErrors</a></td>
<td>

Returns details of each proxy error (for both <code>4xx</code> and <code>5xx</code> response codes) within the specified time range for
the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>errorsDetailsFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsDetailsFilter</td>
<td valign="top"><a href="#errorsdetailsfilter">ErrorsDetailsFilter</a></td>
<td>

The error details filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getProxyTargetErrorsOverTime</strong></td>
<td valign="top">[<a href="#errorsbystatuscodecategory">ErrorsByStatusCodeCategory</a>]</td>
<td>

Returns a list of hit counts for proxy and target errors for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. The errors in each proxy and target
result set are grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>. Optionally, you can configure the <code>errorsByStatusCodeFilter</code>
parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByStatusCodeFilter</td>
<td valign="top"><a href="#errorsbystatuscodefilter">ErrorsByStatusCodeFilter</a></td>
<td>

The errors by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByStatusCode</strong></td>
<td valign="top"><a href="#errorsbystatuscode">ErrorsByStatusCode</a></td>
<td>

Returns the hit count for each error response code (<code>401</code>, <code>404</code>, and <code>500</code> etc.,) for each API within the specified
time range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorCountByStatusCodeFilter</td>
<td valign="top"><a href="#errorcountbystatuscodefilter">ErrorCountByStatusCodeFilter</a>!</td>
<td>

The error count by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrorsByAPI</strong></td>
<td valign="top"><a href="#totalerror">TotalError</a></td>
<td>

Returns the total proxy error hit count for an API across for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given
time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageOverTime</strong></td>
<td valign="top">[<a href="#apiusageovertime">APIUsageOverTime</a>]</td>
<td>

Returns a list of details related to the usage of each API over time for each time granularity within the specified
time range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can
configure the <code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByAppOverTime</strong></td>
<td valign="top"><a href="#apiusagebyappovertime">APIUsageByAppOverTime</a></td>
<td>

Returns API usage by each application over time for each time granularity within the specified time range for the
given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByBackendOverTime</strong></td>
<td valign="top"><a href="#apiusagebybackendovertime">APIUsageByBackendOverTime</a></td>
<td>

Returns API usage by each backend over time for each time granularity within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByBackendOverTimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByBackendOverTimeFilter</td>
<td valign="top"><a href="#apiusagebybackendovertimefilter">APIUsageByBackendOverTimeFilter</a></td>
<td>

The API usage by backend overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getResourceUsage</strong></td>
<td valign="top"><a href="#resourceusages">ResourceUsages</a></td>
<td>

Returns API usage by resource within the specified time range for the given combination of tenant ID, environment
ID, and organization ID. Optionally, you can configure the <code>resourceUsageFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">resourceUsageFilter</td>
<td valign="top"><a href="#resourceusagefilter">ResourceUsageFilter</a></td>
<td>

The resource usage filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTrafficByAPI</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total hit count for an API for the given combination of tenant ID, environment ID, and organization ID.
Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>topSlowestAPIs</strong></td>
<td valign="top">[<a href="#slowapi">SlowAPI</a>]</td>
<td>

Returns a list of top slowest APIs based on the response latency (95th percentile value) within the specified time
range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The limit for the slow APIs list.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatency</strong></td>
<td valign="top"><a href="#apilatency">APILatency</a></td>
<td>

Returns different latency category values (95th percentile values) for a given API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencyFilter</td>
<td valign="top"><a href="#latencyfilter">LatencyFilter</a>!</td>
<td>

The latency filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatencyByAPI</strong></td>
<td valign="top"><a href="#overalllatency">OverallLatency</a></td>
<td>

Returns the overall response latency (95th percentile value) for an API for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the
results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCacheHitsAndMisses</strong></td>
<td valign="top"><a href="#cachehits">CacheHits</a></td>
<td>

Return the total number of response cache hits, misses, and hit percentage for an API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and
organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cacheFilter</td>
<td valign="top"><a href="#cachefilter">CacheFilter</a></td>
<td>

The cache filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopPlatforms</strong></td>
<td valign="top">[<a href="#platform">Platform</a>]</td>
<td>

Returns a list of top platforms ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine platforms with
the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit count.
Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopUserAgents</strong></td>
<td valign="top">[<a href="#useragent">UserAgent</a>]</td>
<td>

Returns a list of top user agents ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine user agents
with the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit
count. Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByGeoLocation</strong></td>
<td valign="top">[<a href="#usagebygeolocation">UsageByGeoLocation</a>]</td>
<td>

NOTE: Currently, this operation returns data only for on-premise environments.

Returns API usage by country within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>geoLocationFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">geoLocationFilter</td>
<td valign="top"><a href="#geolocationfilter">GeoLocationFilter</a></td>
<td>

The geolocation filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#apiusagebyapplication">APIUsageByApplication</a>]</td>
<td>

Returns details relating to the usage of each API by application within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByAppFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByAppFilter</td>
<td valign="top"><a href="#apiusagebyappfilter">APIUsageByAppFilter</a></td>
<td>

The API usage by app filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopAPIsByAlertCount</strong></td>
<td valign="top"><a href="#topapisbyalertcount">TopAPIsByAlertCount</a></td>
<td>

Returns top APIs ranked based on the alert count within the specified time range for the given combination of tenant
ID, environment ID, and organization ID. Optionally, you can configure the <code>topAPIsByAlertCountFilter</code> parameter to
further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">topAPIsByAlertCountFilter</td>
<td valign="top"><a href="#topapisbyalertcountfilter">TopAPIsByAlertCountFilter</a></td>
<td>

The top APIs by alert count filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAlertSummary</strong></td>
<td valign="top"><a href="#alertsummaries">AlertSummaries</a></td>
<td>

Returns a summary for each alert within the specified time range for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>alertSummaryFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">alertSummaryFilter</td>
<td valign="top"><a href="#alertsummaryfilter">AlertSummaryFilter</a></td>
<td>

The alert summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

NOTE: This operation can only be invoked via using an on-prem key as the authentication header.

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplicationsWithOnPremKey</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">onPremKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The value of the On-Prem key.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportOvertime</strong></td>
<td valign="top"><a href="#customreportovertime">CustomReportOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportTopOvertime</strong></td>
<td valign="top"><a href="#customreporttopovertime">CustomReportTopOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans for
the top N values for the selected groupByField.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which the data should be grouped.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getGroupByValues</strong></td>
<td valign="top">[[<a href="#string">String</a>]]</td>
<td>

Returns a list of value sets by which you can group the data available for the selected <code>groupBy</code> fields.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field for which the API needs to retrieve distinct values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
</tbody>
</table>

## Objects

### API

Represents API details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API version.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>provider</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### APILatency

Represents latency values for a single API over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latency">Latency</a>]</td>
<td>

A list containing latency category values over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsage

Represents the API usage for a single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The API usage count.

</td>
</tr>
</tbody>
</table>

### APIUsageByApp

Represents API usage across APIs by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByAppOverTime

Represents API usage across APIs by applications over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebyapp">APIUsageByApp</a>]</td>
<td>

A list containing the API usage values across APIs, grouped by the application. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageByApplication

Represents a single API usage by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API by the application.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackend

Represents API usage across APIs by a single backend.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the backend.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTime

Represents API usage across APIs by each backend over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebybackend">APIUsageByBackend</a>]</td>
<td>

A list containing the API usage values across APIs by each backend. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTime

Represents a single API usage over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the API usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### AlertSummaries

Represents alert summaries.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#alertsummary">AlertSummary</a>]</td>
<td>

A list containing the alert summary for each alert. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### AlertSummary

Represents a summary for an alert.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert category. Possible values are <code>LATENCY</code> and <code>TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>metric</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert metric. Possible values are <code>RESPONSE_LATENCY</code> and <code>TOTAL_TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The severity level of the alert. Possible values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert details.

</td>
</tr>
</tbody>
</table>

### Application

Represents application details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
</tbody>
</table>

### CacheHit

Represents the response cache hits and misses for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was hit.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>misses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was missed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hitPercentage</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

The response cache hits as a percentage of the sum of hits and misses.

</td>
</tr>
</tbody>
</table>

### CacheHits

Represents the response cache hits and misses over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#cachehit">CacheHit</a>]</td>
<td>

A list containing cache hits, misses, and the hit percentage over time. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportGroupBy

Represents the usage data overtime for the selected parameters of a specific <code>groupByValue</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groupByValue</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The distinct group-by value that is used as an ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### CustomReportOvertime

Represents usage data overtime for the selected parameters.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportTopOvertime

Represents usage data overtime for the selected parameters grouped by the top N <code>groupByValues</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportgroupby">CustomReportGroupBy</a>]</td>
<td>

A list containing the usage values grouped by the selected <code>groupByField</code>. This returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportUsage

Represents usage data for a single timestamp in <code>CustomReports</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>value</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage value (Hit Count/ Latency).

</td>
</tr>
</tbody>
</table>

### DetailsOfErrors

Represents error details over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#errordetails">ErrorDetails</a>]!</td>
<td>

A list containing error details over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### Environment

Represents an environment.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>externalEnvId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The external environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internalEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The internal environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sandboxEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The sandbox environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#environmenttype">EnvironmentType</a>!</td>
<td>

The environment type. A Choreo environment is labeled as <code>CHOREO</code>, a private Choreo environment is labeled as
<code>CHOREO_PRIVATE</code>, and the on-premise environment is labeled as <code>ON_PREM</code>.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCategory

Represents the number of errors from each category for a single timestamp. The timestamp is calculated according to the
provided granularity value. If you select some categories, the error counts are retrieved only for those categories,
and a <code>null</code> value is shown for the other categories that are not selected.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of authorization errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targetConnectivity</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of target connectivity errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>throttled</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of throttling errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>other</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of other errors.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCode

Represents the error count for a single error status code.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>statusCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The error status code.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCodeForAPI

Represents the error count for each status code for a single API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCountByCode</strong></td>
<td valign="top">[<a href="#errorcountbycode">ErrorCountByCode</a>]</td>
<td>

A list containing the error count for each error status code. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### ErrorDetails

Represents details of an error for a single timestamp. The timestamp is calculated according to the granularity value
provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The reason for the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorStatusCodeCategoryCounts

Represents errors by the main status code (<code>4xx</code> or <code>5xx</code>) and the total error count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_4xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of client errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_5xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of server errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of client and server errors.

</td>
</tr>
</tbody>
</table>

### ErrorSummary

Provides the unsuccessful usage (i.e., <code>4xx</code> and <code>5xx</code> response codes) summary across all APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#errorvalue">ErrorValue</a>]!</td>
<td>

A list containing unsuccessful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorValue

Represents the unsuccessful request count (i.e., <code>4xx</code> and <code>5xx</code> response codes) for a single timestamp. The timestamp
is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Represents the error request count.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategory

Represents the errors by category over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycategory">ErrorCountByCategory</a>]</td>
<td>

A list containing the error count for each error category over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCode

Represents the error counts grouped by status code for each API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycodeforapi">ErrorCountByCodeForAPI</a>]!</td>
<td>

A list containing the error count for each status code for each API. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeCategory

Represents the error category values (grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>) for both proxy and target errors for a
single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents proxy-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code> response
codes), and the total of both categories.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents target-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code>
response codes), and the total of both categories.

</td>
</tr>
</tbody>
</table>

### Latency

Represents latency values for each latency category for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The backend latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The request mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backendMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the backend latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the request mediation latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response mediation latency in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### LatencySummary

Provides the latency summary.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latencyvalue">LatencyValue</a>]!</td>
<td>

A list containing latency values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### LatencyValue

Represents the latency value for a single timestamp. The timestamp is calculated according to the provided granularity
value.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latencyTime</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Organization

Represents an organization.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>uuid</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The organization UUID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>handle</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization handle name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization name.

</td>
</tr>
</tbody>
</table>

### OverallLatency

Represents the overall latency values.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The response latency (95th percentile value) in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Pagination

Represents pagination details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The total number of results.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of items in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The offset value for the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting column name of the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting order of the result set. Possible values are <code>asc</code> and <code>desc</code>.

</td>
</tr>
</tbody>
</table>

### Platform

Represents a platform.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>platform</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the platform.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the platform.

</td>
</tr>
</tbody>
</table>

### Provider

Represents API Provider details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### ResourceUsage

Represents the usage of a single API resource.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiResourceTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiMethod</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API method.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API resource.

</td>
</tr>
</tbody>
</table>

### ResourceUsages

Represents API resource usages.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#resourceusage">ResourceUsage</a>]</td>
<td>

A list with the usage of each API resource. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### SlowAPI

A slow API identified based on the response latency (95th percentile).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latency</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Subscriber

Represents API Subscriber details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API subscriber.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByApplication

Represents successful usages(that have resulted in the <code>2xx</code> response code) of an API by an application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiVersion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The version of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiCreatorTenantDomain</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The tenant domain of the API creator.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SuccessSummary

Provides the successful (2xx response code) usage summary across all the APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#successvalue">SuccessValue</a>]!</td>
<td>

A list containing successful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### SuccessValue

Represents the successful request count (i.e., requests that have received the <code>2xx</code> response code) for a single
timestamp. The timestamp is calculated according to the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the successful request count.

</td>
</tr>
</tbody>
</table>

### TopAPIByAlertCount

Represents a top API by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The alert count.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCount

Represents the top APIs by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#topapibyalertcount">TopAPIByAlertCount</a>]</td>
<td>

A list containing top APIs by alert count. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### TotalError

Represents the total errors.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The proxy-related error count.

</td>
</tr>
</tbody>
</table>

### UsageByGeoLocation

Represents the usage of a single API in a single country.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the country.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API.

</td>
</tr>
</tbody>
</table>

### UserAgent

Represents a user agent.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>userAgent</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the user agent.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the user agent.

</td>
</tr>
</tbody>
</table>

## Inputs

### APIUsageByAppFilter

Filters the API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribers</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of subscribers you specify here. A maximum of five subscriber IDs can be
defined.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTimeFilter

Filters the results for API usage by backend over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTimeFilter

Filters the results for API usage over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### AlertSummaryFilter

Filters the alerts summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The alert category by which the results need to be filtered. The available categories to select are <code>TRAFFIC</code> and
<code>LATENCY</code>.

</td>
</tr>
</tbody>
</table>

### ApplicationFilter

Filters applications by the application owner and API IDs.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### CacheFilter

Filters response cache results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### DataFilter

Filters results by the given combination of organization, environment, and tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The environment ID by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenant</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the tenant by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>projectId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
</tbody>
</table>

### DeviceFilter

Filters results related to devices.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### ErrorCountByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorType</strong></td>
<td valign="top"><a href="#errortype">ErrorType</a>!</td>
<td>

The type of the error. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCodeType</strong></td>
<td valign="top"><a href="#errorcodetype">ErrorCodeType</a></td>
<td>

The error code type. If this parameter is not configured, both client-related error response codes (<code>401</code>, <code>404</code>,
etc.) and server-related response codes (<code>500</code>, <code>501</code>, etc.) are included in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategoryFilter

Filters errors by category results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>categories</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of categories by which the results need to be filtered. Category values that you can specify here are
<code>AUTH</code>, <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsDetailsFilter

Filters the results for error details.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application ID by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The error category by which the results need to be filtered. The error category that you can specify here must be
one of the <code>AUTH</code> <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code> values.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### GeoLocationFilter

Filters the API usage by geolocation results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here.

</td>
</tr>
</tbody>
</table>

### LatencyFilter

Filters latency results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The results are filtered by the API ID specified here. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### LatencySummaryFilter

Filters latency summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### OrgFilter

Filters results for the given organization.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
</tbody>
</table>

### PaginationFilter

Filters related to pagination.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of rows in the result set. This value must be a positive integer. If this limit value is not set,
the total number of rows is five by default.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The offset value to set when filtering results. This value must be zero or a positive integer. If you do not specify
an offset value, the default offset value (i.e., <code>0</code>) applies.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The column name by which the results are sorted. If the <code>sortBy</code> value is not set, the default column of the related
operation that is available for sorting purposes is used.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The order in which the results are sorted. Possible values are <code>asc</code> (to sort in ascending order) and <code>desc</code> (to
sort in descending order). If no value is specified, the results are sorted in ascending order by default (except
for count-specific operations such as <code>getTopAPIsByAlertCount</code> where the results are always sorted in descending
order).

</td>
</tr>
</tbody>
</table>

### ResourceUsageFilter

Filters resource usage results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### SearchFilter

Filters results by searching matching results for the provided search text.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs that need to be searched with the given search text. Note that it is not possible to define API
IDs without a search text in the search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchText</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Text which needs to be searched among the results. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### SubscriberFilter

Filters the subscriber results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByAppFilter

Filters successful API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenantDomains</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The tenant domain name by which the results need to be filtered.

</td>
</tr>
</tbody>
</table>

### TenantDataFilter

Filters results by the tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>envId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the environment by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### TimeFilter

Filters results by the provided date range.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The start date of the time range. The date specified here must be a date earlier than the date specified via the
<code>to</code> parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:00:00.000+05:30'</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The end date of the time range. The date specified here must be a date later than the date specified via the <code>from</code>
parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:30:00.000+05:30'</code>.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCountFilter

Filters the top APIs by alert count results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

## Enums

### EnvironmentType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHOREO</strong></td>
<td>

The Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>CHOREO_PRIVATE</strong></td>
<td>

The private data-plane Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>ON_PREM</strong></td>
<td>

The On-Premise environments.

</td>
</tr>
</tbody>
</table>

### ErrorCodeType

Represents an error code type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>_4XX</strong></td>
<td>

The client-side errors.

</td>
</tr>
<tr>
<td valign="top"><strong>_5XX</strong></td>
<td>

The server-side errors.

</td>
</tr>
</tbody>
</table>

### ErrorType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PROXY</strong></td>
<td>

The proxy-related errors.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET</strong></td>
<td>

The target-related errors.

</td>
</tr>
</tbody>
</table>

### GroupByField

Represents an <code>groupByField</code> used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>API_NAME</strong></td>
<td>

The API name.

</td>
</tr>
<tr>
<td valign="top"><strong>API_VERSION</strong></td>
<td>

The API version.

</td>
</tr>
<tr>
<td valign="top"><strong>API_RESOURCE_TEMPLATE</strong></td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td valign="top"><strong>API_METHOD</strong></td>
<td>

The API method.

</td>
</tr>
<tr>
<td valign="top"><strong>API_CREATOR</strong></td>
<td>

The API creator.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_NAME</strong></td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_OWNER</strong></td>
<td>

The owner of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>DESTINATION</strong></td>
<td>

The destination.

</td>
</tr>
<tr>
<td valign="top"><strong>USER_AGENT</strong></td>
<td>

The user Agent.

</td>
</tr>
<tr>
<td valign="top"><strong>PLATFORM</strong></td>
<td>

The platform.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_RESPONSE_CODE</strong></td>
<td>

The target response code.

</td>
</tr>
</tbody>
</table>

### Metric

Represents a metric used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>HIT_COUNT</strong></td>
<td>

The number of API calls.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_CACHE_HIT</strong></td>
<td>

The number of API calls that used the response cache.

</td>
</tr>
<tr>
<td valign="top"><strong>REQUEST_MEDIATION_LATENCY</strong></td>
<td>

The request mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_MEDIATION_LATENCY</strong></td>
<td>

The response mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>BACKEND_LATENCY</strong></td>
<td>

The backend latency.

</td>
</tr>
<tr>
<td valign="top"><strong>TOTAL_LATENCY</strong></td>
<td>

The total latency.

</td>
</tr>
<tr>
<td valign="top"><strong>API_ERRORS</strong></td>
<td>

The number of hits for which API errors are returned.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_ERRORS</strong></td>
<td>

The number of hits for which target errors are returned.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.

### Float

The <code>Float</code> scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The <code>ID</code> scalar type represents a unique identifier, often used to re-fetch an object or as the key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value is accepted as an ID.

### Int

The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.





# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.azure.com/.
2. Follow the [AWS Analyzing Log Data documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and open **Log Insights**.
3. Select the relevant region and the relevant log group (the log group string has the cluster name and “/application” appended at the end).
4. Select the required time range. 
4. Copy the query below and paste it into the query editor. 
5. Replace the `<RELEASE_ID>` with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
6. Run the query to extract the logs.

```  SQL 
fields @timestamp, @message
| filter kubernetes.labels.release_id == "<RELEASE_ID>"
| filter @message like "<OPTIONAL SEARCH PHRASE>"
```


# Access the Choreo Insights API

The **Usage Insights** page in the Choreo Console displays data retrieved from the Insights API exposed over the Internet. However, in some scenarios, you may need to retrieve data from external systems and implement custom dashboards to display the data.

Choreo provides a secure and user-friendly approach to accomplish this requirement. Follow the steps given below:

## Become a member of the Choreo System organization

1. Access the Developer Portal of the `Choreo System` organization via [https://devportal.choreo.dev/choreosystem/applications](https://devportal.choreo.dev/choreosystem/applications) and sign in using your preferred method.
   
2. To obtain access to the `Choreo System` organization, click **Request Access**.

    ![Request access](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/request-access.png){.cInlineImage-full}

## Create an application and generate keys

To create an application and generate keys, follow the steps below:

1. To create a new application in the `Choreo System` organization, click **+ Create Application**. 

2. Enter a name for the application and click **Create**. This creates the application and takes you to the **Overview** page.

3. To subscribe to the **Insights** API via the newly created application, follow the steps below:
    1.  In the left navigation menu, click **Subscriptions**.
    2.  In the **Subscription Management** pane, click **+ Add APIs**.
    3.  Search for `Insights` and click **Add**.

4. To generate credentials for the application, follow the steps given below:
    1. In the left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates tokens and populates the **Consumer Key** and **Consumer Secret** fields in the **Application Keys** pane.

5. To specify an appropriate token expiry time for the application, follow the steps given below:
    1. In the **Application Keys** pane, click to expand **Advanced Configurations**.
    2. Specify an appropriate value in the **Application access token expiry time** field and click **Update**.
   
        ![Update token expiry time](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/update-token-expirary-time.png){.cInlineImage-threeQuarter}

6. Execute the following cURL command to generate an access token:

    ```bash
    curl --location --request POST 'https://sts.choreo.dev/oauth2/token' \
    --header 'Authorization: Basic <BASE64_ENCODED_CONSUMER_KEY_AND_CONSUMER_SECRET_OF_YOUR_APP_HERE>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'orgHandle=<YOUR_ORG_HANDLE_HERE>' \
    --data-urlencode 'scope=apim:api_manage'
    ```

    !!! info
        To obtain your organization handle, follow the steps given below:

         1. Go to [https://console.choreo.dev](https://console.choreo.dev) and sign in using your preferred method.
         2. In the Choreo Console, click your username in the top right corner.
         3. In the drop-down menu, click **Settings**.
         4. In the **Organization** pane, click **Copy Handle**. 

    You can use the generated token to access the Insights API exposed via [https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api](https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api).

    The following is a sample cURL command to invoke the Insights API:

    ```bash
    curl --location --request POST 'https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <TOKEN_HERE>' \
    --data-raw '{"query":"query ($org: OrgFilter!) {listEnvironments(org: $org){id\n name}}","variables":{"org":{"orgId":"<ORG_UUID_HERE>"}}}'
    ```

    !!! tip
         - When the token expires, you can generate a new token programmatically by making an API call to the token endpoint using the client credentials grant type.
        - If a token theft occurs, you can revoke the token by making an API call to the revoke endpoint.

        ![Endpoints](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/endpoints.png){.cInlineImage-threeQuarter}


# Choreo Insights API

The Choreo Insights API is a GraphQL API that allows you to retrieve data from external systems based on specific criteria. This guide describes the operations and schema-defined types you can use to retrieve data via the Choreo Insights API.

 - **Allowed operations:** [Queries](#query)
 - **Schema-defined types:** [Objects](#objects), [Inputs](#inputs), [Enums](#enums), and [Scalars](#scalars)

##Try out

You can try out the Choreo Insights API with your data via [GraphQL Explorer](graphiql-explorer/index.html).

!!! warning
    The GraphQL Explorer is currently not compatible with the Safari web browser due to a [known issue](https://developer.apple.com/forums/thread/658688).

## Query
The query root of the Choreo Insights GraphQL API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>listAllAPI</strong></td>
<td valign="top">[<a href="#api">API</a>]</td>
<td>

Fetches all the APIs with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>provider</code> parameter to further filter the APIs by a specific provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">provider</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the API provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listApplications</strong></td>
<td valign="top">[<a href="#application">Application</a>]</td>
<td>

Fetches all the applications with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>applicationFilter</code> parameter to further filter the applications by a specific application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">applicationFilter</td>
<td valign="top"><a href="#applicationfilter">ApplicationFilter</a></td>
<td>

The application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listProviders</strong></td>
<td valign="top">[<a href="#provider">Provider</a>]</td>
<td>

Fetches all the API providers with the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listSubscribers</strong></td>
<td valign="top">[<a href="#subscriber">Subscriber</a>]</td>
<td>

Fetches all the API subscribers with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>subscriberFilter</code> parameter to further filter the subscribers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscriberFilter</td>
<td valign="top"><a href="#subscriberfilter">SubscriberFilter</a></td>
<td>

The subscriber filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listOrganizations</strong></td>
<td valign="top">[<a href="#organization">Organization</a>]</td>
<td>

Fetches all the organizations of a user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listEnvironments</strong></td>
<td valign="top">[<a href="#environment">Environment</a>]</td>
<td>

Fetches all the environments of an organization.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">org</td>
<td valign="top"><a href="#orgfilter">OrgFilter</a>!</td>
<td>

The organization filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">projectId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listTenants</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

Fetches all the tenants with the given combination of environment ID and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tenantDataFilter</td>
<td valign="top"><a href="#tenantdatafilter">TenantDataFilter</a>!</td>
<td>

The tenant filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTraffic</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total traffic during the given time range for the specified combination of tenant ID, environment ID,
and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrors</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total number of errors that occurred during the given time range for the specified combination of tenant
ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatency</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Returns the overall response latency (95th percentile value) during the given time range for the specified
combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatencySummary</strong></td>
<td valign="top"><a href="#latencysummary">LatencySummary</a></td>
<td>

Returns the response latency value (95th percentile value) for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>latencySummaryFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencySummaryFilter</td>
<td valign="top"><a href="#latencysummaryfilter">LatencySummaryFilter</a></td>
<td>

The latency summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessSummary</strong></td>
<td valign="top"><a href="#successsummary">SuccessSummary</a></td>
<td>

Returns the number of successful (2xx response code) hit count for each time granularity within the specified time
range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorSummary</strong></td>
<td valign="top"><a href="#errorsummary">ErrorSummary</a></td>
<td>

Returns the number of unsuccessful hits (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID. Optionally, you can configure the <code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByCategory</strong></td>
<td valign="top"><a href="#errorsbycategory">ErrorsByCategory</a></td>
<td>

Returns the number of proxy errors (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) by each error category
for each time granularity within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>errorsByCategoryFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByCategoryFilter</td>
<td valign="top"><a href="#errorsbycategoryfilter">ErrorsByCategoryFilter</a></td>
<td>

The errors by category filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsDetails</strong></td>
<td valign="top"><a href="#detailsoferrors">DetailsOfErrors</a></td>
<td>

Returns details of each proxy error (for both <code>4xx</code> and <code>5xx</code> response codes) within the specified time range for
the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>errorsDetailsFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsDetailsFilter</td>
<td valign="top"><a href="#errorsdetailsfilter">ErrorsDetailsFilter</a></td>
<td>

The error details filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getProxyTargetErrorsOverTime</strong></td>
<td valign="top">[<a href="#errorsbystatuscodecategory">ErrorsByStatusCodeCategory</a>]</td>
<td>

Returns a list of hit counts for proxy and target errors for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. The errors in each proxy and target
result set are grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>. Optionally, you can configure the <code>errorsByStatusCodeFilter</code>
parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByStatusCodeFilter</td>
<td valign="top"><a href="#errorsbystatuscodefilter">ErrorsByStatusCodeFilter</a></td>
<td>

The errors by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByStatusCode</strong></td>
<td valign="top"><a href="#errorsbystatuscode">ErrorsByStatusCode</a></td>
<td>

Returns the hit count for each error response code (<code>401</code>, <code>404</code>, and <code>500</code> etc.,) for each API within the specified
time range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorCountByStatusCodeFilter</td>
<td valign="top"><a href="#errorcountbystatuscodefilter">ErrorCountByStatusCodeFilter</a>!</td>
<td>

The error count by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrorsByAPI</strong></td>
<td valign="top"><a href="#totalerror">TotalError</a></td>
<td>

Returns the total proxy error hit count for an API across for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given
time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageOverTime</strong></td>
<td valign="top">[<a href="#apiusageovertime">APIUsageOverTime</a>]</td>
<td>

Returns a list of details related to the usage of each API over time for each time granularity within the specified
time range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can
configure the <code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByAppOverTime</strong></td>
<td valign="top"><a href="#apiusagebyappovertime">APIUsageByAppOverTime</a></td>
<td>

Returns API usage by each application over time for each time granularity within the specified time range for the
given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByBackendOverTime</strong></td>
<td valign="top"><a href="#apiusagebybackendovertime">APIUsageByBackendOverTime</a></td>
<td>

Returns API usage by each backend over time for each time granularity within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByBackendOverTimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByBackendOverTimeFilter</td>
<td valign="top"><a href="#apiusagebybackendovertimefilter">APIUsageByBackendOverTimeFilter</a></td>
<td>

The API usage by backend overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getResourceUsage</strong></td>
<td valign="top"><a href="#resourceusages">ResourceUsages</a></td>
<td>

Returns API usage by resource within the specified time range for the given combination of tenant ID, environment
ID, and organization ID. Optionally, you can configure the <code>resourceUsageFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">resourceUsageFilter</td>
<td valign="top"><a href="#resourceusagefilter">ResourceUsageFilter</a></td>
<td>

The resource usage filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTrafficByAPI</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total hit count for an API for the given combination of tenant ID, environment ID, and organization ID.
Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>topSlowestAPIs</strong></td>
<td valign="top">[<a href="#slowapi">SlowAPI</a>]</td>
<td>

Returns a list of top slowest APIs based on the response latency (95th percentile value) within the specified time
range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The limit for the slow APIs list.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatency</strong></td>
<td valign="top"><a href="#apilatency">APILatency</a></td>
<td>

Returns different latency category values (95th percentile values) for a given API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencyFilter</td>
<td valign="top"><a href="#latencyfilter">LatencyFilter</a>!</td>
<td>

The latency filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatencyByAPI</strong></td>
<td valign="top"><a href="#overalllatency">OverallLatency</a></td>
<td>

Returns the overall response latency (95th percentile value) for an API for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the
results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCacheHitsAndMisses</strong></td>
<td valign="top"><a href="#cachehits">CacheHits</a></td>
<td>

Return the total number of response cache hits, misses, and hit percentage for an API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and
organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cacheFilter</td>
<td valign="top"><a href="#cachefilter">CacheFilter</a></td>
<td>

The cache filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopPlatforms</strong></td>
<td valign="top">[<a href="#platform">Platform</a>]</td>
<td>

Returns a list of top platforms ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine platforms with
the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit count.
Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopUserAgents</strong></td>
<td valign="top">[<a href="#useragent">UserAgent</a>]</td>
<td>

Returns a list of top user agents ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine user agents
with the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit
count. Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByGeoLocation</strong></td>
<td valign="top">[<a href="#usagebygeolocation">UsageByGeoLocation</a>]</td>
<td>

NOTE: Currently, this operation returns data only for on-premise environments.

Returns API usage by country within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>geoLocationFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">geoLocationFilter</td>
<td valign="top"><a href="#geolocationfilter">GeoLocationFilter</a></td>
<td>

The geolocation filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#apiusagebyapplication">APIUsageByApplication</a>]</td>
<td>

Returns details relating to the usage of each API by application within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByAppFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByAppFilter</td>
<td valign="top"><a href="#apiusagebyappfilter">APIUsageByAppFilter</a></td>
<td>

The API usage by app filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopAPIsByAlertCount</strong></td>
<td valign="top"><a href="#topapisbyalertcount">TopAPIsByAlertCount</a></td>
<td>

Returns top APIs ranked based on the alert count within the specified time range for the given combination of tenant
ID, environment ID, and organization ID. Optionally, you can configure the <code>topAPIsByAlertCountFilter</code> parameter to
further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">topAPIsByAlertCountFilter</td>
<td valign="top"><a href="#topapisbyalertcountfilter">TopAPIsByAlertCountFilter</a></td>
<td>

The top APIs by alert count filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAlertSummary</strong></td>
<td valign="top"><a href="#alertsummaries">AlertSummaries</a></td>
<td>

Returns a summary for each alert within the specified time range for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>alertSummaryFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">alertSummaryFilter</td>
<td valign="top"><a href="#alertsummaryfilter">AlertSummaryFilter</a></td>
<td>

The alert summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

NOTE: This operation can only be invoked via using an on-prem key as the authentication header.

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplicationsWithOnPremKey</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">onPremKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The value of the On-Prem key.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportOvertime</strong></td>
<td valign="top"><a href="#customreportovertime">CustomReportOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportTopOvertime</strong></td>
<td valign="top"><a href="#customreporttopovertime">CustomReportTopOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans for
the top N values for the selected groupByField.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which the data should be grouped.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getGroupByValues</strong></td>
<td valign="top">[[<a href="#string">String</a>]]</td>
<td>

Returns a list of value sets by which you can group the data available for the selected <code>groupBy</code> fields.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field for which the API needs to retrieve distinct values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
</tbody>
</table>

## Objects

### API

Represents API details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API version.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>provider</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### APILatency

Represents latency values for a single API over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latency">Latency</a>]</td>
<td>

A list containing latency category values over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsage

Represents the API usage for a single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The API usage count.

</td>
</tr>
</tbody>
</table>

### APIUsageByApp

Represents API usage across APIs by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByAppOverTime

Represents API usage across APIs by applications over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebyapp">APIUsageByApp</a>]</td>
<td>

A list containing the API usage values across APIs, grouped by the application. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageByApplication

Represents a single API usage by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API by the application.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackend

Represents API usage across APIs by a single backend.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the backend.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTime

Represents API usage across APIs by each backend over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebybackend">APIUsageByBackend</a>]</td>
<td>

A list containing the API usage values across APIs by each backend. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTime

Represents a single API usage over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the API usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### AlertSummaries

Represents alert summaries.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#alertsummary">AlertSummary</a>]</td>
<td>

A list containing the alert summary for each alert. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### AlertSummary

Represents a summary for an alert.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert category. Possible values are <code>LATENCY</code> and <code>TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>metric</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert metric. Possible values are <code>RESPONSE_LATENCY</code> and <code>TOTAL_TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The severity level of the alert. Possible values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert details.

</td>
</tr>
</tbody>
</table>

### Application

Represents application details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
</tbody>
</table>

### CacheHit

Represents the response cache hits and misses for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was hit.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>misses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was missed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hitPercentage</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

The response cache hits as a percentage of the sum of hits and misses.

</td>
</tr>
</tbody>
</table>

### CacheHits

Represents the response cache hits and misses over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#cachehit">CacheHit</a>]</td>
<td>

A list containing cache hits, misses, and the hit percentage over time. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportGroupBy

Represents the usage data overtime for the selected parameters of a specific <code>groupByValue</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groupByValue</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The distinct group-by value that is used as an ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### CustomReportOvertime

Represents usage data overtime for the selected parameters.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportTopOvertime

Represents usage data overtime for the selected parameters grouped by the top N <code>groupByValues</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportgroupby">CustomReportGroupBy</a>]</td>
<td>

A list containing the usage values grouped by the selected <code>groupByField</code>. This returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportUsage

Represents usage data for a single timestamp in <code>CustomReports</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>value</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage value (Hit Count/ Latency).

</td>
</tr>
</tbody>
</table>

### DetailsOfErrors

Represents error details over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#errordetails">ErrorDetails</a>]!</td>
<td>

A list containing error details over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### Environment

Represents an environment.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>externalEnvId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The external environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internalEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The internal environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sandboxEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The sandbox environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#environmenttype">EnvironmentType</a>!</td>
<td>

The environment type. A Choreo environment is labeled as <code>CHOREO</code>, a private Choreo environment is labeled as
<code>CHOREO_PRIVATE</code>, and the on-premise environment is labeled as <code>ON_PREM</code>.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCategory

Represents the number of errors from each category for a single timestamp. The timestamp is calculated according to the
provided granularity value. If you select some categories, the error counts are retrieved only for those categories,
and a <code>null</code> value is shown for the other categories that are not selected.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of authorization errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targetConnectivity</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of target connectivity errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>throttled</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of throttling errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>other</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of other errors.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCode

Represents the error count for a single error status code.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>statusCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The error status code.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCodeForAPI

Represents the error count for each status code for a single API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCountByCode</strong></td>
<td valign="top">[<a href="#errorcountbycode">ErrorCountByCode</a>]</td>
<td>

A list containing the error count for each error status code. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### ErrorDetails

Represents details of an error for a single timestamp. The timestamp is calculated according to the granularity value
provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The reason for the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorStatusCodeCategoryCounts

Represents errors by the main status code (<code>4xx</code> or <code>5xx</code>) and the total error count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_4xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of client errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_5xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of server errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of client and server errors.

</td>
</tr>
</tbody>
</table>

### ErrorSummary

Provides the unsuccessful usage (i.e., <code>4xx</code> and <code>5xx</code> response codes) summary across all APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#errorvalue">ErrorValue</a>]!</td>
<td>

A list containing unsuccessful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorValue

Represents the unsuccessful request count (i.e., <code>4xx</code> and <code>5xx</code> response codes) for a single timestamp. The timestamp
is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Represents the error request count.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategory

Represents the errors by category over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycategory">ErrorCountByCategory</a>]</td>
<td>

A list containing the error count for each error category over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCode

Represents the error counts grouped by status code for each API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycodeforapi">ErrorCountByCodeForAPI</a>]!</td>
<td>

A list containing the error count for each status code for each API. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeCategory

Represents the error category values (grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>) for both proxy and target errors for a
single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents proxy-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code> response
codes), and the total of both categories.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents target-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code>
response codes), and the total of both categories.

</td>
</tr>
</tbody>
</table>

### Latency

Represents latency values for each latency category for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The backend latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The request mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backendMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the backend latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the request mediation latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response mediation latency in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### LatencySummary

Provides the latency summary.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latencyvalue">LatencyValue</a>]!</td>
<td>

A list containing latency values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### LatencyValue

Represents the latency value for a single timestamp. The timestamp is calculated according to the provided granularity
value.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latencyTime</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Organization

Represents an organization.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>uuid</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The organization UUID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>handle</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization handle name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization name.

</td>
</tr>
</tbody>
</table>

### OverallLatency

Represents the overall latency values.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The response latency (95th percentile value) in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Pagination

Represents pagination details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The total number of results.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of items in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The offset value for the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting column name of the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting order of the result set. Possible values are <code>asc</code> and <code>desc</code>.

</td>
</tr>
</tbody>
</table>

### Platform

Represents a platform.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>platform</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the platform.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the platform.

</td>
</tr>
</tbody>
</table>

### Provider

Represents API Provider details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### ResourceUsage

Represents the usage of a single API resource.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiResourceTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiMethod</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API method.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API resource.

</td>
</tr>
</tbody>
</table>

### ResourceUsages

Represents API resource usages.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#resourceusage">ResourceUsage</a>]</td>
<td>

A list with the usage of each API resource. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### SlowAPI

A slow API identified based on the response latency (95th percentile).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latency</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Subscriber

Represents API Subscriber details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API subscriber.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByApplication

Represents successful usages(that have resulted in the <code>2xx</code> response code) of an API by an application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiVersion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The version of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiCreatorTenantDomain</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The tenant domain of the API creator.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SuccessSummary

Provides the successful (2xx response code) usage summary across all the APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#successvalue">SuccessValue</a>]!</td>
<td>

A list containing successful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### SuccessValue

Represents the successful request count (i.e., requests that have received the <code>2xx</code> response code) for a single
timestamp. The timestamp is calculated according to the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the successful request count.

</td>
</tr>
</tbody>
</table>

### TopAPIByAlertCount

Represents a top API by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The alert count.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCount

Represents the top APIs by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#topapibyalertcount">TopAPIByAlertCount</a>]</td>
<td>

A list containing top APIs by alert count. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### TotalError

Represents the total errors.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The proxy-related error count.

</td>
</tr>
</tbody>
</table>

### UsageByGeoLocation

Represents the usage of a single API in a single country.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the country.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API.

</td>
</tr>
</tbody>
</table>

### UserAgent

Represents a user agent.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>userAgent</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the user agent.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the user agent.

</td>
</tr>
</tbody>
</table>

## Inputs

### APIUsageByAppFilter

Filters the API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribers</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of subscribers you specify here. A maximum of five subscriber IDs can be
defined.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTimeFilter

Filters the results for API usage by backend over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTimeFilter

Filters the results for API usage over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### AlertSummaryFilter

Filters the alerts summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The alert category by which the results need to be filtered. The available categories to select are <code>TRAFFIC</code> and
<code>LATENCY</code>.

</td>
</tr>
</tbody>
</table>

### ApplicationFilter

Filters applications by the application owner and API IDs.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### CacheFilter

Filters response cache results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### DataFilter

Filters results by the given combination of organization, environment, and tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The environment ID by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenant</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the tenant by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>projectId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
</tbody>
</table>

### DeviceFilter

Filters results related to devices.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### ErrorCountByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorType</strong></td>
<td valign="top"><a href="#errortype">ErrorType</a>!</td>
<td>

The type of the error. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCodeType</strong></td>
<td valign="top"><a href="#errorcodetype">ErrorCodeType</a></td>
<td>

The error code type. If this parameter is not configured, both client-related error response codes (<code>401</code>, <code>404</code>,
etc.) and server-related response codes (<code>500</code>, <code>501</code>, etc.) are included in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategoryFilter

Filters errors by category results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>categories</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of categories by which the results need to be filtered. Category values that you can specify here are
<code>AUTH</code>, <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsDetailsFilter

Filters the results for error details.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application ID by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The error category by which the results need to be filtered. The error category that you can specify here must be
one of the <code>AUTH</code> <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code> values.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### GeoLocationFilter

Filters the API usage by geolocation results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here.

</td>
</tr>
</tbody>
</table>

### LatencyFilter

Filters latency results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The results are filtered by the API ID specified here. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### LatencySummaryFilter

Filters latency summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### OrgFilter

Filters results for the given organization.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
</tbody>
</table>

### PaginationFilter

Filters related to pagination.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of rows in the result set. This value must be a positive integer. If this limit value is not set,
the total number of rows is five by default.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The offset value to set when filtering results. This value must be zero or a positive integer. If you do not specify
an offset value, the default offset value (i.e., <code>0</code>) applies.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The column name by which the results are sorted. If the <code>sortBy</code> value is not set, the default column of the related
operation that is available for sorting purposes is used.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The order in which the results are sorted. Possible values are <code>asc</code> (to sort in ascending order) and <code>desc</code> (to
sort in descending order). If no value is specified, the results are sorted in ascending order by default (except
for count-specific operations such as <code>getTopAPIsByAlertCount</code> where the results are always sorted in descending
order).

</td>
</tr>
</tbody>
</table>

### ResourceUsageFilter

Filters resource usage results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### SearchFilter

Filters results by searching matching results for the provided search text.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs that need to be searched with the given search text. Note that it is not possible to define API
IDs without a search text in the search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchText</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Text which needs to be searched among the results. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### SubscriberFilter

Filters the subscriber results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByAppFilter

Filters successful API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenantDomains</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The tenant domain name by which the results need to be filtered.

</td>
</tr>
</tbody>
</table>

### TenantDataFilter

Filters results by the tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>envId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the environment by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### TimeFilter

Filters results by the provided date range.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The start date of the time range. The date specified here must be a date earlier than the date specified via the
<code>to</code> parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:00:00.000+05:30'</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The end date of the time range. The date specified here must be a date later than the date specified via the <code>from</code>
parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:30:00.000+05:30'</code>.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCountFilter

Filters the top APIs by alert count results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

## Enums

### EnvironmentType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHOREO</strong></td>
<td>

The Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>CHOREO_PRIVATE</strong></td>
<td>

The private data-plane Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>ON_PREM</strong></td>
<td>

The On-Premise environments.

</td>
</tr>
</tbody>
</table>

### ErrorCodeType

Represents an error code type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>_4XX</strong></td>
<td>

The client-side errors.

</td>
</tr>
<tr>
<td valign="top"><strong>_5XX</strong></td>
<td>

The server-side errors.

</td>
</tr>
</tbody>
</table>

### ErrorType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PROXY</strong></td>
<td>

The proxy-related errors.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET</strong></td>
<td>

The target-related errors.

</td>
</tr>
</tbody>
</table>

### GroupByField

Represents an <code>groupByField</code> used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>API_NAME</strong></td>
<td>

The API name.

</td>
</tr>
<tr>
<td valign="top"><strong>API_VERSION</strong></td>
<td>

The API version.

</td>
</tr>
<tr>
<td valign="top"><strong>API_RESOURCE_TEMPLATE</strong></td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td valign="top"><strong>API_METHOD</strong></td>
<td>

The API method.

</td>
</tr>
<tr>
<td valign="top"><strong>API_CREATOR</strong></td>
<td>

The API creator.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_NAME</strong></td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_OWNER</strong></td>
<td>

The owner of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>DESTINATION</strong></td>
<td>

The destination.

</td>
</tr>
<tr>
<td valign="top"><strong>USER_AGENT</strong></td>
<td>

The user Agent.

</td>
</tr>
<tr>
<td valign="top"><strong>PLATFORM</strong></td>
<td>

The platform.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_RESPONSE_CODE</strong></td>
<td>

The target response code.

</td>
</tr>
</tbody>
</table>

### Metric

Represents a metric used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>HIT_COUNT</strong></td>
<td>

The number of API calls.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_CACHE_HIT</strong></td>
<td>

The number of API calls that used the response cache.

</td>
</tr>
<tr>
<td valign="top"><strong>REQUEST_MEDIATION_LATENCY</strong></td>
<td>

The request mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_MEDIATION_LATENCY</strong></td>
<td>

The response mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>BACKEND_LATENCY</strong></td>
<td>

The backend latency.

</td>
</tr>
<tr>
<td valign="top"><strong>TOTAL_LATENCY</strong></td>
<td>

The total latency.

</td>
</tr>
<tr>
<td valign="top"><strong>API_ERRORS</strong></td>
<td>

The number of hits for which API errors are returned.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_ERRORS</strong></td>
<td>

The number of hits for which target errors are returned.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.

### Float

The <code>Float</code> scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The <code>ID</code> scalar type represents a unique identifier, often used to re-fetch an object or as the key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value is accepted as an ID.

### Int

The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.





# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.azure.com/.
2. Follow the [AWS Analyzing Log Data documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and open **Log Insights**.
3. Select the relevant region and the relevant log group (the log group string has the cluster name and “/application” appended at the end).
4. Select the required time range. 
4. Copy the query below and paste it into the query editor. 
5. Replace the `<RELEASE_ID>` with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
6. Run the query to extract the logs.

```  SQL 
fields @timestamp, @message
| filter kubernetes.labels.release_id == "<RELEASE_ID>"
| filter @message like "<OPTIONAL SEARCH PHRASE>"
```


# Access the Choreo Insights API

The **Usage Insights** page in the Choreo Console displays data retrieved from the Insights API exposed over the Internet. However, in some scenarios, you may need to retrieve data from external systems and implement custom dashboards to display the data.

Choreo provides a secure and user-friendly approach to accomplish this requirement. Follow the steps given below:

## Become a member of the Choreo System organization

1. Access the Developer Portal of the `Choreo System` organization via [https://devportal.choreo.dev/choreosystem/applications](https://devportal.choreo.dev/choreosystem/applications) and sign in using your preferred method.
   
2. To obtain access to the `Choreo System` organization, click **Request Access**.

    ![Request access](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/request-access.png){.cInlineImage-full}

## Create an application and generate keys

To create an application and generate keys, follow the steps below:

1. To create a new application in the `Choreo System` organization, click **+ Create Application**. 

2. Enter a name for the application and click **Create**. This creates the application and takes you to the **Overview** page.

3. To subscribe to the **Insights** API via the newly created application, follow the steps below:
    1.  In the left navigation menu, click **Subscriptions**.
    2.  In the **Subscription Management** pane, click **+ Add APIs**.
    3.  Search for `Insights` and click **Add**.

4. To generate credentials for the application, follow the steps given below:
    1. In the left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates tokens and populates the **Consumer Key** and **Consumer Secret** fields in the **Application Keys** pane.

5. To specify an appropriate token expiry time for the application, follow the steps given below:
    1. In the **Application Keys** pane, click to expand **Advanced Configurations**.
    2. Specify an appropriate value in the **Application access token expiry time** field and click **Update**.
   
        ![Update token expiry time](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/update-token-expirary-time.png){.cInlineImage-threeQuarter}

6. Execute the following cURL command to generate an access token:

    ```bash
    curl --location --request POST 'https://sts.choreo.dev/oauth2/token' \
    --header 'Authorization: Basic <BASE64_ENCODED_CONSUMER_KEY_AND_CONSUMER_SECRET_OF_YOUR_APP_HERE>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'orgHandle=<YOUR_ORG_HANDLE_HERE>' \
    --data-urlencode 'scope=apim:api_manage'
    ```

    !!! info
        To obtain your organization handle, follow the steps given below:

         1. Go to [https://console.choreo.dev](https://console.choreo.dev) and sign in using your preferred method.
         2. In the Choreo Console, click your username in the top right corner.
         3. In the drop-down menu, click **Settings**.
         4. In the **Organization** pane, click **Copy Handle**. 

    You can use the generated token to access the Insights API exposed via [https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api](https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api).

    The following is a sample cURL command to invoke the Insights API:

    ```bash
    curl --location --request POST 'https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <TOKEN_HERE>' \
    --data-raw '{"query":"query ($org: OrgFilter!) {listEnvironments(org: $org){id\n name}}","variables":{"org":{"orgId":"<ORG_UUID_HERE>"}}}'
    ```

    !!! tip
         - When the token expires, you can generate a new token programmatically by making an API call to the token endpoint using the client credentials grant type.
        - If a token theft occurs, you can revoke the token by making an API call to the revoke endpoint.

        ![Endpoints](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/endpoints.png){.cInlineImage-threeQuarter}


# Choreo Insights API

The Choreo Insights API is a GraphQL API that allows you to retrieve data from external systems based on specific criteria. This guide describes the operations and schema-defined types you can use to retrieve data via the Choreo Insights API.

 - **Allowed operations:** [Queries](#query)
 - **Schema-defined types:** [Objects](#objects), [Inputs](#inputs), [Enums](#enums), and [Scalars](#scalars)

##Try out

You can try out the Choreo Insights API with your data via [GraphQL Explorer](graphiql-explorer/index.html).

!!! warning
    The GraphQL Explorer is currently not compatible with the Safari web browser due to a [known issue](https://developer.apple.com/forums/thread/658688).

## Query
The query root of the Choreo Insights GraphQL API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>listAllAPI</strong></td>
<td valign="top">[<a href="#api">API</a>]</td>
<td>

Fetches all the APIs with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>provider</code> parameter to further filter the APIs by a specific provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">provider</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the API provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listApplications</strong></td>
<td valign="top">[<a href="#application">Application</a>]</td>
<td>

Fetches all the applications with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>applicationFilter</code> parameter to further filter the applications by a specific application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">applicationFilter</td>
<td valign="top"><a href="#applicationfilter">ApplicationFilter</a></td>
<td>

The application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listProviders</strong></td>
<td valign="top">[<a href="#provider">Provider</a>]</td>
<td>

Fetches all the API providers with the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listSubscribers</strong></td>
<td valign="top">[<a href="#subscriber">Subscriber</a>]</td>
<td>

Fetches all the API subscribers with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>subscriberFilter</code> parameter to further filter the subscribers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscriberFilter</td>
<td valign="top"><a href="#subscriberfilter">SubscriberFilter</a></td>
<td>

The subscriber filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listOrganizations</strong></td>
<td valign="top">[<a href="#organization">Organization</a>]</td>
<td>

Fetches all the organizations of a user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listEnvironments</strong></td>
<td valign="top">[<a href="#environment">Environment</a>]</td>
<td>

Fetches all the environments of an organization.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">org</td>
<td valign="top"><a href="#orgfilter">OrgFilter</a>!</td>
<td>

The organization filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">projectId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listTenants</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

Fetches all the tenants with the given combination of environment ID and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tenantDataFilter</td>
<td valign="top"><a href="#tenantdatafilter">TenantDataFilter</a>!</td>
<td>

The tenant filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTraffic</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total traffic during the given time range for the specified combination of tenant ID, environment ID,
and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrors</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total number of errors that occurred during the given time range for the specified combination of tenant
ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatency</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Returns the overall response latency (95th percentile value) during the given time range for the specified
combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatencySummary</strong></td>
<td valign="top"><a href="#latencysummary">LatencySummary</a></td>
<td>

Returns the response latency value (95th percentile value) for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>latencySummaryFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencySummaryFilter</td>
<td valign="top"><a href="#latencysummaryfilter">LatencySummaryFilter</a></td>
<td>

The latency summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessSummary</strong></td>
<td valign="top"><a href="#successsummary">SuccessSummary</a></td>
<td>

Returns the number of successful (2xx response code) hit count for each time granularity within the specified time
range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorSummary</strong></td>
<td valign="top"><a href="#errorsummary">ErrorSummary</a></td>
<td>

Returns the number of unsuccessful hits (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID. Optionally, you can configure the <code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByCategory</strong></td>
<td valign="top"><a href="#errorsbycategory">ErrorsByCategory</a></td>
<td>

Returns the number of proxy errors (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) by each error category
for each time granularity within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>errorsByCategoryFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByCategoryFilter</td>
<td valign="top"><a href="#errorsbycategoryfilter">ErrorsByCategoryFilter</a></td>
<td>

The errors by category filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsDetails</strong></td>
<td valign="top"><a href="#detailsoferrors">DetailsOfErrors</a></td>
<td>

Returns details of each proxy error (for both <code>4xx</code> and <code>5xx</code> response codes) within the specified time range for
the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>errorsDetailsFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsDetailsFilter</td>
<td valign="top"><a href="#errorsdetailsfilter">ErrorsDetailsFilter</a></td>
<td>

The error details filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getProxyTargetErrorsOverTime</strong></td>
<td valign="top">[<a href="#errorsbystatuscodecategory">ErrorsByStatusCodeCategory</a>]</td>
<td>

Returns a list of hit counts for proxy and target errors for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. The errors in each proxy and target
result set are grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>. Optionally, you can configure the <code>errorsByStatusCodeFilter</code>
parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByStatusCodeFilter</td>
<td valign="top"><a href="#errorsbystatuscodefilter">ErrorsByStatusCodeFilter</a></td>
<td>

The errors by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByStatusCode</strong></td>
<td valign="top"><a href="#errorsbystatuscode">ErrorsByStatusCode</a></td>
<td>

Returns the hit count for each error response code (<code>401</code>, <code>404</code>, and <code>500</code> etc.,) for each API within the specified
time range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorCountByStatusCodeFilter</td>
<td valign="top"><a href="#errorcountbystatuscodefilter">ErrorCountByStatusCodeFilter</a>!</td>
<td>

The error count by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrorsByAPI</strong></td>
<td valign="top"><a href="#totalerror">TotalError</a></td>
<td>

Returns the total proxy error hit count for an API across for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given
time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageOverTime</strong></td>
<td valign="top">[<a href="#apiusageovertime">APIUsageOverTime</a>]</td>
<td>

Returns a list of details related to the usage of each API over time for each time granularity within the specified
time range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can
configure the <code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByAppOverTime</strong></td>
<td valign="top"><a href="#apiusagebyappovertime">APIUsageByAppOverTime</a></td>
<td>

Returns API usage by each application over time for each time granularity within the specified time range for the
given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByBackendOverTime</strong></td>
<td valign="top"><a href="#apiusagebybackendovertime">APIUsageByBackendOverTime</a></td>
<td>

Returns API usage by each backend over time for each time granularity within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByBackendOverTimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByBackendOverTimeFilter</td>
<td valign="top"><a href="#apiusagebybackendovertimefilter">APIUsageByBackendOverTimeFilter</a></td>
<td>

The API usage by backend overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getResourceUsage</strong></td>
<td valign="top"><a href="#resourceusages">ResourceUsages</a></td>
<td>

Returns API usage by resource within the specified time range for the given combination of tenant ID, environment
ID, and organization ID. Optionally, you can configure the <code>resourceUsageFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">resourceUsageFilter</td>
<td valign="top"><a href="#resourceusagefilter">ResourceUsageFilter</a></td>
<td>

The resource usage filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTrafficByAPI</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total hit count for an API for the given combination of tenant ID, environment ID, and organization ID.
Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>topSlowestAPIs</strong></td>
<td valign="top">[<a href="#slowapi">SlowAPI</a>]</td>
<td>

Returns a list of top slowest APIs based on the response latency (95th percentile value) within the specified time
range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The limit for the slow APIs list.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatency</strong></td>
<td valign="top"><a href="#apilatency">APILatency</a></td>
<td>

Returns different latency category values (95th percentile values) for a given API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencyFilter</td>
<td valign="top"><a href="#latencyfilter">LatencyFilter</a>!</td>
<td>

The latency filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatencyByAPI</strong></td>
<td valign="top"><a href="#overalllatency">OverallLatency</a></td>
<td>

Returns the overall response latency (95th percentile value) for an API for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the
results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCacheHitsAndMisses</strong></td>
<td valign="top"><a href="#cachehits">CacheHits</a></td>
<td>

Return the total number of response cache hits, misses, and hit percentage for an API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and
organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cacheFilter</td>
<td valign="top"><a href="#cachefilter">CacheFilter</a></td>
<td>

The cache filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopPlatforms</strong></td>
<td valign="top">[<a href="#platform">Platform</a>]</td>
<td>

Returns a list of top platforms ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine platforms with
the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit count.
Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopUserAgents</strong></td>
<td valign="top">[<a href="#useragent">UserAgent</a>]</td>
<td>

Returns a list of top user agents ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine user agents
with the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit
count. Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByGeoLocation</strong></td>
<td valign="top">[<a href="#usagebygeolocation">UsageByGeoLocation</a>]</td>
<td>

NOTE: Currently, this operation returns data only for on-premise environments.

Returns API usage by country within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>geoLocationFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">geoLocationFilter</td>
<td valign="top"><a href="#geolocationfilter">GeoLocationFilter</a></td>
<td>

The geolocation filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#apiusagebyapplication">APIUsageByApplication</a>]</td>
<td>

Returns details relating to the usage of each API by application within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByAppFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByAppFilter</td>
<td valign="top"><a href="#apiusagebyappfilter">APIUsageByAppFilter</a></td>
<td>

The API usage by app filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopAPIsByAlertCount</strong></td>
<td valign="top"><a href="#topapisbyalertcount">TopAPIsByAlertCount</a></td>
<td>

Returns top APIs ranked based on the alert count within the specified time range for the given combination of tenant
ID, environment ID, and organization ID. Optionally, you can configure the <code>topAPIsByAlertCountFilter</code> parameter to
further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">topAPIsByAlertCountFilter</td>
<td valign="top"><a href="#topapisbyalertcountfilter">TopAPIsByAlertCountFilter</a></td>
<td>

The top APIs by alert count filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAlertSummary</strong></td>
<td valign="top"><a href="#alertsummaries">AlertSummaries</a></td>
<td>

Returns a summary for each alert within the specified time range for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>alertSummaryFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">alertSummaryFilter</td>
<td valign="top"><a href="#alertsummaryfilter">AlertSummaryFilter</a></td>
<td>

The alert summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

NOTE: This operation can only be invoked via using an on-prem key as the authentication header.

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplicationsWithOnPremKey</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">onPremKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The value of the On-Prem key.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportOvertime</strong></td>
<td valign="top"><a href="#customreportovertime">CustomReportOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportTopOvertime</strong></td>
<td valign="top"><a href="#customreporttopovertime">CustomReportTopOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans for
the top N values for the selected groupByField.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which the data should be grouped.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getGroupByValues</strong></td>
<td valign="top">[[<a href="#string">String</a>]]</td>
<td>

Returns a list of value sets by which you can group the data available for the selected <code>groupBy</code> fields.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field for which the API needs to retrieve distinct values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
</tbody>
</table>

## Objects

### API

Represents API details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API version.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>provider</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### APILatency

Represents latency values for a single API over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latency">Latency</a>]</td>
<td>

A list containing latency category values over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsage

Represents the API usage for a single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The API usage count.

</td>
</tr>
</tbody>
</table>

### APIUsageByApp

Represents API usage across APIs by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByAppOverTime

Represents API usage across APIs by applications over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebyapp">APIUsageByApp</a>]</td>
<td>

A list containing the API usage values across APIs, grouped by the application. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageByApplication

Represents a single API usage by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API by the application.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackend

Represents API usage across APIs by a single backend.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the backend.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTime

Represents API usage across APIs by each backend over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebybackend">APIUsageByBackend</a>]</td>
<td>

A list containing the API usage values across APIs by each backend. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTime

Represents a single API usage over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the API usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### AlertSummaries

Represents alert summaries.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#alertsummary">AlertSummary</a>]</td>
<td>

A list containing the alert summary for each alert. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### AlertSummary

Represents a summary for an alert.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert category. Possible values are <code>LATENCY</code> and <code>TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>metric</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert metric. Possible values are <code>RESPONSE_LATENCY</code> and <code>TOTAL_TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The severity level of the alert. Possible values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert details.

</td>
</tr>
</tbody>
</table>

### Application

Represents application details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
</tbody>
</table>

### CacheHit

Represents the response cache hits and misses for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was hit.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>misses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was missed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hitPercentage</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

The response cache hits as a percentage of the sum of hits and misses.

</td>
</tr>
</tbody>
</table>

### CacheHits

Represents the response cache hits and misses over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#cachehit">CacheHit</a>]</td>
<td>

A list containing cache hits, misses, and the hit percentage over time. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportGroupBy

Represents the usage data overtime for the selected parameters of a specific <code>groupByValue</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groupByValue</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The distinct group-by value that is used as an ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### CustomReportOvertime

Represents usage data overtime for the selected parameters.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportTopOvertime

Represents usage data overtime for the selected parameters grouped by the top N <code>groupByValues</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportgroupby">CustomReportGroupBy</a>]</td>
<td>

A list containing the usage values grouped by the selected <code>groupByField</code>. This returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportUsage

Represents usage data for a single timestamp in <code>CustomReports</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>value</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage value (Hit Count/ Latency).

</td>
</tr>
</tbody>
</table>

### DetailsOfErrors

Represents error details over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#errordetails">ErrorDetails</a>]!</td>
<td>

A list containing error details over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### Environment

Represents an environment.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>externalEnvId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The external environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internalEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The internal environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sandboxEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The sandbox environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#environmenttype">EnvironmentType</a>!</td>
<td>

The environment type. A Choreo environment is labeled as <code>CHOREO</code>, a private Choreo environment is labeled as
<code>CHOREO_PRIVATE</code>, and the on-premise environment is labeled as <code>ON_PREM</code>.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCategory

Represents the number of errors from each category for a single timestamp. The timestamp is calculated according to the
provided granularity value. If you select some categories, the error counts are retrieved only for those categories,
and a <code>null</code> value is shown for the other categories that are not selected.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of authorization errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targetConnectivity</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of target connectivity errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>throttled</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of throttling errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>other</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of other errors.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCode

Represents the error count for a single error status code.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>statusCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The error status code.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCodeForAPI

Represents the error count for each status code for a single API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCountByCode</strong></td>
<td valign="top">[<a href="#errorcountbycode">ErrorCountByCode</a>]</td>
<td>

A list containing the error count for each error status code. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### ErrorDetails

Represents details of an error for a single timestamp. The timestamp is calculated according to the granularity value
provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The reason for the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorStatusCodeCategoryCounts

Represents errors by the main status code (<code>4xx</code> or <code>5xx</code>) and the total error count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_4xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of client errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_5xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of server errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of client and server errors.

</td>
</tr>
</tbody>
</table>

### ErrorSummary

Provides the unsuccessful usage (i.e., <code>4xx</code> and <code>5xx</code> response codes) summary across all APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#errorvalue">ErrorValue</a>]!</td>
<td>

A list containing unsuccessful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorValue

Represents the unsuccessful request count (i.e., <code>4xx</code> and <code>5xx</code> response codes) for a single timestamp. The timestamp
is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Represents the error request count.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategory

Represents the errors by category over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycategory">ErrorCountByCategory</a>]</td>
<td>

A list containing the error count for each error category over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCode

Represents the error counts grouped by status code for each API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycodeforapi">ErrorCountByCodeForAPI</a>]!</td>
<td>

A list containing the error count for each status code for each API. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeCategory

Represents the error category values (grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>) for both proxy and target errors for a
single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents proxy-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code> response
codes), and the total of both categories.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents target-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code>
response codes), and the total of both categories.

</td>
</tr>
</tbody>
</table>

### Latency

Represents latency values for each latency category for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The backend latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The request mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backendMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the backend latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the request mediation latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response mediation latency in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### LatencySummary

Provides the latency summary.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latencyvalue">LatencyValue</a>]!</td>
<td>

A list containing latency values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### LatencyValue

Represents the latency value for a single timestamp. The timestamp is calculated according to the provided granularity
value.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latencyTime</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Organization

Represents an organization.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>uuid</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The organization UUID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>handle</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization handle name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization name.

</td>
</tr>
</tbody>
</table>

### OverallLatency

Represents the overall latency values.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The response latency (95th percentile value) in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Pagination

Represents pagination details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The total number of results.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of items in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The offset value for the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting column name of the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting order of the result set. Possible values are <code>asc</code> and <code>desc</code>.

</td>
</tr>
</tbody>
</table>

### Platform

Represents a platform.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>platform</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the platform.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the platform.

</td>
</tr>
</tbody>
</table>

### Provider

Represents API Provider details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### ResourceUsage

Represents the usage of a single API resource.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiResourceTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiMethod</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API method.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API resource.

</td>
</tr>
</tbody>
</table>

### ResourceUsages

Represents API resource usages.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#resourceusage">ResourceUsage</a>]</td>
<td>

A list with the usage of each API resource. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### SlowAPI

A slow API identified based on the response latency (95th percentile).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latency</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Subscriber

Represents API Subscriber details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API subscriber.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByApplication

Represents successful usages(that have resulted in the <code>2xx</code> response code) of an API by an application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiVersion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The version of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiCreatorTenantDomain</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The tenant domain of the API creator.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SuccessSummary

Provides the successful (2xx response code) usage summary across all the APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#successvalue">SuccessValue</a>]!</td>
<td>

A list containing successful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### SuccessValue

Represents the successful request count (i.e., requests that have received the <code>2xx</code> response code) for a single
timestamp. The timestamp is calculated according to the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the successful request count.

</td>
</tr>
</tbody>
</table>

### TopAPIByAlertCount

Represents a top API by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The alert count.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCount

Represents the top APIs by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#topapibyalertcount">TopAPIByAlertCount</a>]</td>
<td>

A list containing top APIs by alert count. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### TotalError

Represents the total errors.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The proxy-related error count.

</td>
</tr>
</tbody>
</table>

### UsageByGeoLocation

Represents the usage of a single API in a single country.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the country.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API.

</td>
</tr>
</tbody>
</table>

### UserAgent

Represents a user agent.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>userAgent</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the user agent.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the user agent.

</td>
</tr>
</tbody>
</table>

## Inputs

### APIUsageByAppFilter

Filters the API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribers</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of subscribers you specify here. A maximum of five subscriber IDs can be
defined.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTimeFilter

Filters the results for API usage by backend over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTimeFilter

Filters the results for API usage over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### AlertSummaryFilter

Filters the alerts summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The alert category by which the results need to be filtered. The available categories to select are <code>TRAFFIC</code> and
<code>LATENCY</code>.

</td>
</tr>
</tbody>
</table>

### ApplicationFilter

Filters applications by the application owner and API IDs.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### CacheFilter

Filters response cache results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### DataFilter

Filters results by the given combination of organization, environment, and tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The environment ID by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenant</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the tenant by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>projectId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
</tbody>
</table>

### DeviceFilter

Filters results related to devices.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### ErrorCountByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorType</strong></td>
<td valign="top"><a href="#errortype">ErrorType</a>!</td>
<td>

The type of the error. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCodeType</strong></td>
<td valign="top"><a href="#errorcodetype">ErrorCodeType</a></td>
<td>

The error code type. If this parameter is not configured, both client-related error response codes (<code>401</code>, <code>404</code>,
etc.) and server-related response codes (<code>500</code>, <code>501</code>, etc.) are included in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategoryFilter

Filters errors by category results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>categories</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of categories by which the results need to be filtered. Category values that you can specify here are
<code>AUTH</code>, <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsDetailsFilter

Filters the results for error details.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application ID by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The error category by which the results need to be filtered. The error category that you can specify here must be
one of the <code>AUTH</code> <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code> values.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### GeoLocationFilter

Filters the API usage by geolocation results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here.

</td>
</tr>
</tbody>
</table>

### LatencyFilter

Filters latency results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The results are filtered by the API ID specified here. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### LatencySummaryFilter

Filters latency summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### OrgFilter

Filters results for the given organization.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
</tbody>
</table>

### PaginationFilter

Filters related to pagination.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of rows in the result set. This value must be a positive integer. If this limit value is not set,
the total number of rows is five by default.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The offset value to set when filtering results. This value must be zero or a positive integer. If you do not specify
an offset value, the default offset value (i.e., <code>0</code>) applies.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The column name by which the results are sorted. If the <code>sortBy</code> value is not set, the default column of the related
operation that is available for sorting purposes is used.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The order in which the results are sorted. Possible values are <code>asc</code> (to sort in ascending order) and <code>desc</code> (to
sort in descending order). If no value is specified, the results are sorted in ascending order by default (except
for count-specific operations such as <code>getTopAPIsByAlertCount</code> where the results are always sorted in descending
order).

</td>
</tr>
</tbody>
</table>

### ResourceUsageFilter

Filters resource usage results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### SearchFilter

Filters results by searching matching results for the provided search text.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs that need to be searched with the given search text. Note that it is not possible to define API
IDs without a search text in the search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchText</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Text which needs to be searched among the results. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### SubscriberFilter

Filters the subscriber results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByAppFilter

Filters successful API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenantDomains</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The tenant domain name by which the results need to be filtered.

</td>
</tr>
</tbody>
</table>

### TenantDataFilter

Filters results by the tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>envId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the environment by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### TimeFilter

Filters results by the provided date range.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The start date of the time range. The date specified here must be a date earlier than the date specified via the
<code>to</code> parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:00:00.000+05:30'</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The end date of the time range. The date specified here must be a date later than the date specified via the <code>from</code>
parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:30:00.000+05:30'</code>.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCountFilter

Filters the top APIs by alert count results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

## Enums

### EnvironmentType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHOREO</strong></td>
<td>

The Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>CHOREO_PRIVATE</strong></td>
<td>

The private data-plane Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>ON_PREM</strong></td>
<td>

The On-Premise environments.

</td>
</tr>
</tbody>
</table>

### ErrorCodeType

Represents an error code type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>_4XX</strong></td>
<td>

The client-side errors.

</td>
</tr>
<tr>
<td valign="top"><strong>_5XX</strong></td>
<td>

The server-side errors.

</td>
</tr>
</tbody>
</table>

### ErrorType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PROXY</strong></td>
<td>

The proxy-related errors.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET</strong></td>
<td>

The target-related errors.

</td>
</tr>
</tbody>
</table>

### GroupByField

Represents an <code>groupByField</code> used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>API_NAME</strong></td>
<td>

The API name.

</td>
</tr>
<tr>
<td valign="top"><strong>API_VERSION</strong></td>
<td>

The API version.

</td>
</tr>
<tr>
<td valign="top"><strong>API_RESOURCE_TEMPLATE</strong></td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td valign="top"><strong>API_METHOD</strong></td>
<td>

The API method.

</td>
</tr>
<tr>
<td valign="top"><strong>API_CREATOR</strong></td>
<td>

The API creator.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_NAME</strong></td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_OWNER</strong></td>
<td>

The owner of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>DESTINATION</strong></td>
<td>

The destination.

</td>
</tr>
<tr>
<td valign="top"><strong>USER_AGENT</strong></td>
<td>

The user Agent.

</td>
</tr>
<tr>
<td valign="top"><strong>PLATFORM</strong></td>
<td>

The platform.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_RESPONSE_CODE</strong></td>
<td>

The target response code.

</td>
</tr>
</tbody>
</table>

### Metric

Represents a metric used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>HIT_COUNT</strong></td>
<td>

The number of API calls.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_CACHE_HIT</strong></td>
<td>

The number of API calls that used the response cache.

</td>
</tr>
<tr>
<td valign="top"><strong>REQUEST_MEDIATION_LATENCY</strong></td>
<td>

The request mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_MEDIATION_LATENCY</strong></td>
<td>

The response mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>BACKEND_LATENCY</strong></td>
<td>

The backend latency.

</td>
</tr>
<tr>
<td valign="top"><strong>TOTAL_LATENCY</strong></td>
<td>

The total latency.

</td>
</tr>
<tr>
<td valign="top"><strong>API_ERRORS</strong></td>
<td>

The number of hits for which API errors are returned.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_ERRORS</strong></td>
<td>

The number of hits for which target errors are returned.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.

### Float

The <code>Float</code> scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The <code>ID</code> scalar type represents a unique identifier, often used to re-fetch an object or as the key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value is accepted as an ID.

### Int

The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.





# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.azure.com/.
2. Follow the [AWS Analyzing Log Data documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and open **Log Insights**.
3. Select the relevant region and the relevant log group (the log group string has the cluster name and “/application” appended at the end).
4. Select the required time range. 
4. Copy the query below and paste it into the query editor. 
5. Replace the `<RELEASE_ID>` with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
6. Run the query to extract the logs.

```  SQL 
fields @timestamp, @message
| filter kubernetes.labels.release_id == "<RELEASE_ID>"
| filter @message like "<OPTIONAL SEARCH PHRASE>"
```


# Access the Choreo Insights API

The **Usage Insights** page in the Choreo Console displays data retrieved from the Insights API exposed over the Internet. However, in some scenarios, you may need to retrieve data from external systems and implement custom dashboards to display the data.

Choreo provides a secure and user-friendly approach to accomplish this requirement. Follow the steps given below:

## Become a member of the Choreo System organization

1. Access the Developer Portal of the `Choreo System` organization via [https://devportal.choreo.dev/choreosystem/applications](https://devportal.choreo.dev/choreosystem/applications) and sign in using your preferred method.
   
2. To obtain access to the `Choreo System` organization, click **Request Access**.

    ![Request access](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/request-access.png){.cInlineImage-full}

## Create an application and generate keys

To create an application and generate keys, follow the steps below:

1. To create a new application in the `Choreo System` organization, click **+ Create Application**. 

2. Enter a name for the application and click **Create**. This creates the application and takes you to the **Overview** page.

3. To subscribe to the **Insights** API via the newly created application, follow the steps below:
    1.  In the left navigation menu, click **Subscriptions**.
    2.  In the **Subscription Management** pane, click **+ Add APIs**.
    3.  Search for `Insights` and click **Add**.

4. To generate credentials for the application, follow the steps given below:
    1. In the left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates tokens and populates the **Consumer Key** and **Consumer Secret** fields in the **Application Keys** pane.

5. To specify an appropriate token expiry time for the application, follow the steps given below:
    1. In the **Application Keys** pane, click to expand **Advanced Configurations**.
    2. Specify an appropriate value in the **Application access token expiry time** field and click **Update**.
   
        ![Update token expiry time](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/update-token-expirary-time.png){.cInlineImage-threeQuarter}

6. Execute the following cURL command to generate an access token:

    ```bash
    curl --location --request POST 'https://sts.choreo.dev/oauth2/token' \
    --header 'Authorization: Basic <BASE64_ENCODED_CONSUMER_KEY_AND_CONSUMER_SECRET_OF_YOUR_APP_HERE>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'orgHandle=<YOUR_ORG_HANDLE_HERE>' \
    --data-urlencode 'scope=apim:api_manage'
    ```

    !!! info
        To obtain your organization handle, follow the steps given below:

         1. Go to [https://console.choreo.dev](https://console.choreo.dev) and sign in using your preferred method.
         2. In the Choreo Console, click your username in the top right corner.
         3. In the drop-down menu, click **Settings**.
         4. In the **Organization** pane, click **Copy Handle**. 

    You can use the generated token to access the Insights API exposed via [https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api](https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api).

    The following is a sample cURL command to invoke the Insights API:

    ```bash
    curl --location --request POST 'https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <TOKEN_HERE>' \
    --data-raw '{"query":"query ($org: OrgFilter!) {listEnvironments(org: $org){id\n name}}","variables":{"org":{"orgId":"<ORG_UUID_HERE>"}}}'
    ```

    !!! tip
         - When the token expires, you can generate a new token programmatically by making an API call to the token endpoint using the client credentials grant type.
        - If a token theft occurs, you can revoke the token by making an API call to the revoke endpoint.

        ![Endpoints](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/endpoints.png){.cInlineImage-threeQuarter}


# Choreo Insights API

The Choreo Insights API is a GraphQL API that allows you to retrieve data from external systems based on specific criteria. This guide describes the operations and schema-defined types you can use to retrieve data via the Choreo Insights API.

 - **Allowed operations:** [Queries](#query)
 - **Schema-defined types:** [Objects](#objects), [Inputs](#inputs), [Enums](#enums), and [Scalars](#scalars)

##Try out

You can try out the Choreo Insights API with your data via [GraphQL Explorer](graphiql-explorer/index.html).

!!! warning
    The GraphQL Explorer is currently not compatible with the Safari web browser due to a [known issue](https://developer.apple.com/forums/thread/658688).

## Query
The query root of the Choreo Insights GraphQL API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>listAllAPI</strong></td>
<td valign="top">[<a href="#api">API</a>]</td>
<td>

Fetches all the APIs with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>provider</code> parameter to further filter the APIs by a specific provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">provider</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the API provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listApplications</strong></td>
<td valign="top">[<a href="#application">Application</a>]</td>
<td>

Fetches all the applications with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>applicationFilter</code> parameter to further filter the applications by a specific application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">applicationFilter</td>
<td valign="top"><a href="#applicationfilter">ApplicationFilter</a></td>
<td>

The application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listProviders</strong></td>
<td valign="top">[<a href="#provider">Provider</a>]</td>
<td>

Fetches all the API providers with the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listSubscribers</strong></td>
<td valign="top">[<a href="#subscriber">Subscriber</a>]</td>
<td>

Fetches all the API subscribers with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>subscriberFilter</code> parameter to further filter the subscribers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscriberFilter</td>
<td valign="top"><a href="#subscriberfilter">SubscriberFilter</a></td>
<td>

The subscriber filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listOrganizations</strong></td>
<td valign="top">[<a href="#organization">Organization</a>]</td>
<td>

Fetches all the organizations of a user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listEnvironments</strong></td>
<td valign="top">[<a href="#environment">Environment</a>]</td>
<td>

Fetches all the environments of an organization.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">org</td>
<td valign="top"><a href="#orgfilter">OrgFilter</a>!</td>
<td>

The organization filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">projectId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listTenants</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

Fetches all the tenants with the given combination of environment ID and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tenantDataFilter</td>
<td valign="top"><a href="#tenantdatafilter">TenantDataFilter</a>!</td>
<td>

The tenant filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTraffic</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total traffic during the given time range for the specified combination of tenant ID, environment ID,
and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrors</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total number of errors that occurred during the given time range for the specified combination of tenant
ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatency</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Returns the overall response latency (95th percentile value) during the given time range for the specified
combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatencySummary</strong></td>
<td valign="top"><a href="#latencysummary">LatencySummary</a></td>
<td>

Returns the response latency value (95th percentile value) for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>latencySummaryFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencySummaryFilter</td>
<td valign="top"><a href="#latencysummaryfilter">LatencySummaryFilter</a></td>
<td>

The latency summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessSummary</strong></td>
<td valign="top"><a href="#successsummary">SuccessSummary</a></td>
<td>

Returns the number of successful (2xx response code) hit count for each time granularity within the specified time
range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorSummary</strong></td>
<td valign="top"><a href="#errorsummary">ErrorSummary</a></td>
<td>

Returns the number of unsuccessful hits (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID. Optionally, you can configure the <code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByCategory</strong></td>
<td valign="top"><a href="#errorsbycategory">ErrorsByCategory</a></td>
<td>

Returns the number of proxy errors (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) by each error category
for each time granularity within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>errorsByCategoryFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByCategoryFilter</td>
<td valign="top"><a href="#errorsbycategoryfilter">ErrorsByCategoryFilter</a></td>
<td>

The errors by category filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsDetails</strong></td>
<td valign="top"><a href="#detailsoferrors">DetailsOfErrors</a></td>
<td>

Returns details of each proxy error (for both <code>4xx</code> and <code>5xx</code> response codes) within the specified time range for
the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>errorsDetailsFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsDetailsFilter</td>
<td valign="top"><a href="#errorsdetailsfilter">ErrorsDetailsFilter</a></td>
<td>

The error details filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getProxyTargetErrorsOverTime</strong></td>
<td valign="top">[<a href="#errorsbystatuscodecategory">ErrorsByStatusCodeCategory</a>]</td>
<td>

Returns a list of hit counts for proxy and target errors for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. The errors in each proxy and target
result set are grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>. Optionally, you can configure the <code>errorsByStatusCodeFilter</code>
parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByStatusCodeFilter</td>
<td valign="top"><a href="#errorsbystatuscodefilter">ErrorsByStatusCodeFilter</a></td>
<td>

The errors by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByStatusCode</strong></td>
<td valign="top"><a href="#errorsbystatuscode">ErrorsByStatusCode</a></td>
<td>

Returns the hit count for each error response code (<code>401</code>, <code>404</code>, and <code>500</code> etc.,) for each API within the specified
time range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorCountByStatusCodeFilter</td>
<td valign="top"><a href="#errorcountbystatuscodefilter">ErrorCountByStatusCodeFilter</a>!</td>
<td>

The error count by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrorsByAPI</strong></td>
<td valign="top"><a href="#totalerror">TotalError</a></td>
<td>

Returns the total proxy error hit count for an API across for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given
time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageOverTime</strong></td>
<td valign="top">[<a href="#apiusageovertime">APIUsageOverTime</a>]</td>
<td>

Returns a list of details related to the usage of each API over time for each time granularity within the specified
time range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can
configure the <code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByAppOverTime</strong></td>
<td valign="top"><a href="#apiusagebyappovertime">APIUsageByAppOverTime</a></td>
<td>

Returns API usage by each application over time for each time granularity within the specified time range for the
given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByBackendOverTime</strong></td>
<td valign="top"><a href="#apiusagebybackendovertime">APIUsageByBackendOverTime</a></td>
<td>

Returns API usage by each backend over time for each time granularity within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByBackendOverTimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByBackendOverTimeFilter</td>
<td valign="top"><a href="#apiusagebybackendovertimefilter">APIUsageByBackendOverTimeFilter</a></td>
<td>

The API usage by backend overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getResourceUsage</strong></td>
<td valign="top"><a href="#resourceusages">ResourceUsages</a></td>
<td>

Returns API usage by resource within the specified time range for the given combination of tenant ID, environment
ID, and organization ID. Optionally, you can configure the <code>resourceUsageFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">resourceUsageFilter</td>
<td valign="top"><a href="#resourceusagefilter">ResourceUsageFilter</a></td>
<td>

The resource usage filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTrafficByAPI</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total hit count for an API for the given combination of tenant ID, environment ID, and organization ID.
Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>topSlowestAPIs</strong></td>
<td valign="top">[<a href="#slowapi">SlowAPI</a>]</td>
<td>

Returns a list of top slowest APIs based on the response latency (95th percentile value) within the specified time
range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The limit for the slow APIs list.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatency</strong></td>
<td valign="top"><a href="#apilatency">APILatency</a></td>
<td>

Returns different latency category values (95th percentile values) for a given API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencyFilter</td>
<td valign="top"><a href="#latencyfilter">LatencyFilter</a>!</td>
<td>

The latency filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatencyByAPI</strong></td>
<td valign="top"><a href="#overalllatency">OverallLatency</a></td>
<td>

Returns the overall response latency (95th percentile value) for an API for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the
results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCacheHitsAndMisses</strong></td>
<td valign="top"><a href="#cachehits">CacheHits</a></td>
<td>

Return the total number of response cache hits, misses, and hit percentage for an API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and
organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cacheFilter</td>
<td valign="top"><a href="#cachefilter">CacheFilter</a></td>
<td>

The cache filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopPlatforms</strong></td>
<td valign="top">[<a href="#platform">Platform</a>]</td>
<td>

Returns a list of top platforms ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine platforms with
the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit count.
Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopUserAgents</strong></td>
<td valign="top">[<a href="#useragent">UserAgent</a>]</td>
<td>

Returns a list of top user agents ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine user agents
with the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit
count. Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByGeoLocation</strong></td>
<td valign="top">[<a href="#usagebygeolocation">UsageByGeoLocation</a>]</td>
<td>

NOTE: Currently, this operation returns data only for on-premise environments.

Returns API usage by country within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>geoLocationFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">geoLocationFilter</td>
<td valign="top"><a href="#geolocationfilter">GeoLocationFilter</a></td>
<td>

The geolocation filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#apiusagebyapplication">APIUsageByApplication</a>]</td>
<td>

Returns details relating to the usage of each API by application within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByAppFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByAppFilter</td>
<td valign="top"><a href="#apiusagebyappfilter">APIUsageByAppFilter</a></td>
<td>

The API usage by app filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopAPIsByAlertCount</strong></td>
<td valign="top"><a href="#topapisbyalertcount">TopAPIsByAlertCount</a></td>
<td>

Returns top APIs ranked based on the alert count within the specified time range for the given combination of tenant
ID, environment ID, and organization ID. Optionally, you can configure the <code>topAPIsByAlertCountFilter</code> parameter to
further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">topAPIsByAlertCountFilter</td>
<td valign="top"><a href="#topapisbyalertcountfilter">TopAPIsByAlertCountFilter</a></td>
<td>

The top APIs by alert count filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAlertSummary</strong></td>
<td valign="top"><a href="#alertsummaries">AlertSummaries</a></td>
<td>

Returns a summary for each alert within the specified time range for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>alertSummaryFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">alertSummaryFilter</td>
<td valign="top"><a href="#alertsummaryfilter">AlertSummaryFilter</a></td>
<td>

The alert summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

NOTE: This operation can only be invoked via using an on-prem key as the authentication header.

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplicationsWithOnPremKey</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">onPremKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The value of the On-Prem key.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportOvertime</strong></td>
<td valign="top"><a href="#customreportovertime">CustomReportOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportTopOvertime</strong></td>
<td valign="top"><a href="#customreporttopovertime">CustomReportTopOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans for
the top N values for the selected groupByField.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which the data should be grouped.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getGroupByValues</strong></td>
<td valign="top">[[<a href="#string">String</a>]]</td>
<td>

Returns a list of value sets by which you can group the data available for the selected <code>groupBy</code> fields.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field for which the API needs to retrieve distinct values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
</tbody>
</table>

## Objects

### API

Represents API details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API version.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>provider</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### APILatency

Represents latency values for a single API over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latency">Latency</a>]</td>
<td>

A list containing latency category values over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsage

Represents the API usage for a single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The API usage count.

</td>
</tr>
</tbody>
</table>

### APIUsageByApp

Represents API usage across APIs by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByAppOverTime

Represents API usage across APIs by applications over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebyapp">APIUsageByApp</a>]</td>
<td>

A list containing the API usage values across APIs, grouped by the application. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageByApplication

Represents a single API usage by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API by the application.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackend

Represents API usage across APIs by a single backend.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the backend.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTime

Represents API usage across APIs by each backend over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebybackend">APIUsageByBackend</a>]</td>
<td>

A list containing the API usage values across APIs by each backend. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTime

Represents a single API usage over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the API usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### AlertSummaries

Represents alert summaries.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#alertsummary">AlertSummary</a>]</td>
<td>

A list containing the alert summary for each alert. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### AlertSummary

Represents a summary for an alert.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert category. Possible values are <code>LATENCY</code> and <code>TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>metric</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert metric. Possible values are <code>RESPONSE_LATENCY</code> and <code>TOTAL_TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The severity level of the alert. Possible values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert details.

</td>
</tr>
</tbody>
</table>

### Application

Represents application details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
</tbody>
</table>

### CacheHit

Represents the response cache hits and misses for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was hit.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>misses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was missed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hitPercentage</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

The response cache hits as a percentage of the sum of hits and misses.

</td>
</tr>
</tbody>
</table>

### CacheHits

Represents the response cache hits and misses over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#cachehit">CacheHit</a>]</td>
<td>

A list containing cache hits, misses, and the hit percentage over time. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportGroupBy

Represents the usage data overtime for the selected parameters of a specific <code>groupByValue</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groupByValue</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The distinct group-by value that is used as an ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### CustomReportOvertime

Represents usage data overtime for the selected parameters.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportTopOvertime

Represents usage data overtime for the selected parameters grouped by the top N <code>groupByValues</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportgroupby">CustomReportGroupBy</a>]</td>
<td>

A list containing the usage values grouped by the selected <code>groupByField</code>. This returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportUsage

Represents usage data for a single timestamp in <code>CustomReports</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>value</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage value (Hit Count/ Latency).

</td>
</tr>
</tbody>
</table>

### DetailsOfErrors

Represents error details over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#errordetails">ErrorDetails</a>]!</td>
<td>

A list containing error details over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### Environment

Represents an environment.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>externalEnvId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The external environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internalEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The internal environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sandboxEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The sandbox environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#environmenttype">EnvironmentType</a>!</td>
<td>

The environment type. A Choreo environment is labeled as <code>CHOREO</code>, a private Choreo environment is labeled as
<code>CHOREO_PRIVATE</code>, and the on-premise environment is labeled as <code>ON_PREM</code>.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCategory

Represents the number of errors from each category for a single timestamp. The timestamp is calculated according to the
provided granularity value. If you select some categories, the error counts are retrieved only for those categories,
and a <code>null</code> value is shown for the other categories that are not selected.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of authorization errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targetConnectivity</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of target connectivity errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>throttled</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of throttling errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>other</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of other errors.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCode

Represents the error count for a single error status code.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>statusCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The error status code.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCodeForAPI

Represents the error count for each status code for a single API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCountByCode</strong></td>
<td valign="top">[<a href="#errorcountbycode">ErrorCountByCode</a>]</td>
<td>

A list containing the error count for each error status code. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### ErrorDetails

Represents details of an error for a single timestamp. The timestamp is calculated according to the granularity value
provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The reason for the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorStatusCodeCategoryCounts

Represents errors by the main status code (<code>4xx</code> or <code>5xx</code>) and the total error count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_4xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of client errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_5xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of server errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of client and server errors.

</td>
</tr>
</tbody>
</table>

### ErrorSummary

Provides the unsuccessful usage (i.e., <code>4xx</code> and <code>5xx</code> response codes) summary across all APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#errorvalue">ErrorValue</a>]!</td>
<td>

A list containing unsuccessful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorValue

Represents the unsuccessful request count (i.e., <code>4xx</code> and <code>5xx</code> response codes) for a single timestamp. The timestamp
is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Represents the error request count.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategory

Represents the errors by category over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycategory">ErrorCountByCategory</a>]</td>
<td>

A list containing the error count for each error category over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCode

Represents the error counts grouped by status code for each API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycodeforapi">ErrorCountByCodeForAPI</a>]!</td>
<td>

A list containing the error count for each status code for each API. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeCategory

Represents the error category values (grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>) for both proxy and target errors for a
single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents proxy-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code> response
codes), and the total of both categories.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents target-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code>
response codes), and the total of both categories.

</td>
</tr>
</tbody>
</table>

### Latency

Represents latency values for each latency category for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The backend latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The request mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backendMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the backend latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the request mediation latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response mediation latency in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### LatencySummary

Provides the latency summary.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latencyvalue">LatencyValue</a>]!</td>
<td>

A list containing latency values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### LatencyValue

Represents the latency value for a single timestamp. The timestamp is calculated according to the provided granularity
value.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latencyTime</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Organization

Represents an organization.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>uuid</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The organization UUID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>handle</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization handle name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization name.

</td>
</tr>
</tbody>
</table>

### OverallLatency

Represents the overall latency values.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The response latency (95th percentile value) in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Pagination

Represents pagination details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The total number of results.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of items in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The offset value for the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting column name of the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting order of the result set. Possible values are <code>asc</code> and <code>desc</code>.

</td>
</tr>
</tbody>
</table>

### Platform

Represents a platform.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>platform</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the platform.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the platform.

</td>
</tr>
</tbody>
</table>

### Provider

Represents API Provider details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### ResourceUsage

Represents the usage of a single API resource.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiResourceTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiMethod</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API method.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API resource.

</td>
</tr>
</tbody>
</table>

### ResourceUsages

Represents API resource usages.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#resourceusage">ResourceUsage</a>]</td>
<td>

A list with the usage of each API resource. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### SlowAPI

A slow API identified based on the response latency (95th percentile).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latency</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Subscriber

Represents API Subscriber details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API subscriber.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByApplication

Represents successful usages(that have resulted in the <code>2xx</code> response code) of an API by an application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiVersion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The version of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiCreatorTenantDomain</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The tenant domain of the API creator.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SuccessSummary

Provides the successful (2xx response code) usage summary across all the APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#successvalue">SuccessValue</a>]!</td>
<td>

A list containing successful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### SuccessValue

Represents the successful request count (i.e., requests that have received the <code>2xx</code> response code) for a single
timestamp. The timestamp is calculated according to the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the successful request count.

</td>
</tr>
</tbody>
</table>

### TopAPIByAlertCount

Represents a top API by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The alert count.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCount

Represents the top APIs by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#topapibyalertcount">TopAPIByAlertCount</a>]</td>
<td>

A list containing top APIs by alert count. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### TotalError

Represents the total errors.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The proxy-related error count.

</td>
</tr>
</tbody>
</table>

### UsageByGeoLocation

Represents the usage of a single API in a single country.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the country.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API.

</td>
</tr>
</tbody>
</table>

### UserAgent

Represents a user agent.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>userAgent</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the user agent.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the user agent.

</td>
</tr>
</tbody>
</table>

## Inputs

### APIUsageByAppFilter

Filters the API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribers</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of subscribers you specify here. A maximum of five subscriber IDs can be
defined.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTimeFilter

Filters the results for API usage by backend over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTimeFilter

Filters the results for API usage over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### AlertSummaryFilter

Filters the alerts summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The alert category by which the results need to be filtered. The available categories to select are <code>TRAFFIC</code> and
<code>LATENCY</code>.

</td>
</tr>
</tbody>
</table>

### ApplicationFilter

Filters applications by the application owner and API IDs.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### CacheFilter

Filters response cache results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### DataFilter

Filters results by the given combination of organization, environment, and tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The environment ID by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenant</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the tenant by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>projectId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
</tbody>
</table>

### DeviceFilter

Filters results related to devices.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### ErrorCountByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorType</strong></td>
<td valign="top"><a href="#errortype">ErrorType</a>!</td>
<td>

The type of the error. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCodeType</strong></td>
<td valign="top"><a href="#errorcodetype">ErrorCodeType</a></td>
<td>

The error code type. If this parameter is not configured, both client-related error response codes (<code>401</code>, <code>404</code>,
etc.) and server-related response codes (<code>500</code>, <code>501</code>, etc.) are included in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategoryFilter

Filters errors by category results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>categories</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of categories by which the results need to be filtered. Category values that you can specify here are
<code>AUTH</code>, <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsDetailsFilter

Filters the results for error details.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application ID by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The error category by which the results need to be filtered. The error category that you can specify here must be
one of the <code>AUTH</code> <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code> values.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### GeoLocationFilter

Filters the API usage by geolocation results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here.

</td>
</tr>
</tbody>
</table>

### LatencyFilter

Filters latency results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The results are filtered by the API ID specified here. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### LatencySummaryFilter

Filters latency summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### OrgFilter

Filters results for the given organization.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
</tbody>
</table>

### PaginationFilter

Filters related to pagination.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of rows in the result set. This value must be a positive integer. If this limit value is not set,
the total number of rows is five by default.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The offset value to set when filtering results. This value must be zero or a positive integer. If you do not specify
an offset value, the default offset value (i.e., <code>0</code>) applies.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The column name by which the results are sorted. If the <code>sortBy</code> value is not set, the default column of the related
operation that is available for sorting purposes is used.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The order in which the results are sorted. Possible values are <code>asc</code> (to sort in ascending order) and <code>desc</code> (to
sort in descending order). If no value is specified, the results are sorted in ascending order by default (except
for count-specific operations such as <code>getTopAPIsByAlertCount</code> where the results are always sorted in descending
order).

</td>
</tr>
</tbody>
</table>

### ResourceUsageFilter

Filters resource usage results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### SearchFilter

Filters results by searching matching results for the provided search text.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs that need to be searched with the given search text. Note that it is not possible to define API
IDs without a search text in the search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchText</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Text which needs to be searched among the results. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### SubscriberFilter

Filters the subscriber results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByAppFilter

Filters successful API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenantDomains</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The tenant domain name by which the results need to be filtered.

</td>
</tr>
</tbody>
</table>

### TenantDataFilter

Filters results by the tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>envId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the environment by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### TimeFilter

Filters results by the provided date range.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The start date of the time range. The date specified here must be a date earlier than the date specified via the
<code>to</code> parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:00:00.000+05:30'</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The end date of the time range. The date specified here must be a date later than the date specified via the <code>from</code>
parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:30:00.000+05:30'</code>.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCountFilter

Filters the top APIs by alert count results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

## Enums

### EnvironmentType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHOREO</strong></td>
<td>

The Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>CHOREO_PRIVATE</strong></td>
<td>

The private data-plane Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>ON_PREM</strong></td>
<td>

The On-Premise environments.

</td>
</tr>
</tbody>
</table>

### ErrorCodeType

Represents an error code type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>_4XX</strong></td>
<td>

The client-side errors.

</td>
</tr>
<tr>
<td valign="top"><strong>_5XX</strong></td>
<td>

The server-side errors.

</td>
</tr>
</tbody>
</table>

### ErrorType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PROXY</strong></td>
<td>

The proxy-related errors.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET</strong></td>
<td>

The target-related errors.

</td>
</tr>
</tbody>
</table>

### GroupByField

Represents an <code>groupByField</code> used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>API_NAME</strong></td>
<td>

The API name.

</td>
</tr>
<tr>
<td valign="top"><strong>API_VERSION</strong></td>
<td>

The API version.

</td>
</tr>
<tr>
<td valign="top"><strong>API_RESOURCE_TEMPLATE</strong></td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td valign="top"><strong>API_METHOD</strong></td>
<td>

The API method.

</td>
</tr>
<tr>
<td valign="top"><strong>API_CREATOR</strong></td>
<td>

The API creator.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_NAME</strong></td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_OWNER</strong></td>
<td>

The owner of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>DESTINATION</strong></td>
<td>

The destination.

</td>
</tr>
<tr>
<td valign="top"><strong>USER_AGENT</strong></td>
<td>

The user Agent.

</td>
</tr>
<tr>
<td valign="top"><strong>PLATFORM</strong></td>
<td>

The platform.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_RESPONSE_CODE</strong></td>
<td>

The target response code.

</td>
</tr>
</tbody>
</table>

### Metric

Represents a metric used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>HIT_COUNT</strong></td>
<td>

The number of API calls.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_CACHE_HIT</strong></td>
<td>

The number of API calls that used the response cache.

</td>
</tr>
<tr>
<td valign="top"><strong>REQUEST_MEDIATION_LATENCY</strong></td>
<td>

The request mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_MEDIATION_LATENCY</strong></td>
<td>

The response mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>BACKEND_LATENCY</strong></td>
<td>

The backend latency.

</td>
</tr>
<tr>
<td valign="top"><strong>TOTAL_LATENCY</strong></td>
<td>

The total latency.

</td>
</tr>
<tr>
<td valign="top"><strong>API_ERRORS</strong></td>
<td>

The number of hits for which API errors are returned.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_ERRORS</strong></td>
<td>

The number of hits for which target errors are returned.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.

### Float

The <code>Float</code> scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The <code>ID</code> scalar type represents a unique identifier, often used to re-fetch an object or as the key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value is accepted as an ID.

### Int

The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.





# Observability Overview

The Choreo observability dashboard provides a comprehensive interface to visualize and monitor the performance of services deployed on Choreo.

![Dashboard overview](../assets/img/monitoring-and-insights/observability/overview-overall.png){.cInlineImage-full}

The Observability dashboard allows you to:

- Observe the throughput and latencies of requests served over a given period.
- Compare metrics side-by-side to facilitate efficient diagnosis.
- Observe the diagnostics view generated over a given period.
- View logs generated over a specific timeframe.

!!! tip
    If you are a Choreo private data plane customer and you want to observe your private data plane using New Relic, see [Observing Choreo Private Data Planes With New Relic](https://wso2.com/blogs/thesource/observing-choreo-private-data-planes-with-new-relic/).

## Throughput and latency graphs

The throughput graph depicts the throughput of requests per second for a selected timestamp.   

![Throughput and latency graph](../assets/img/monitoring-and-insights/observability/throughput-and-latency.png){.cInlineImage-full} 
    
By default, Choreo renders this graph for the data generated within the past 24 hours. You can change the default time window by selecting the time range and zone from the options bar. To expand the graph, click and drag the cursor over the period you want to drill down. 

You can view the Choreo service logs in the **Logs** pane below the throughput and latency graph. Clicking on a graph updates the **Logs** view to contain the corresponding log entries generated at that time. You can use these logs to identify the reasons for any latency and throughput anomalies you detect using the graph.

## Diagnostics view

The **Diagnostics view** allows you to simultaneously analyze errors, throughput, latencies, CPU usage, memory usage, and logs for a particular event. This facilitates detailed error detection and analysis.

By default, the time range selected for the **Throughput & Latency** graphs is the same time range used for the **Diagnostics view**.

Each horizontal section of the graph, termed a *bin*, represents a specific period and comprises:

- **Date/Time:** Indicates when the log entries began to appear.
- **Logs:**  List of log entries and respective log counts within the bin's timeframe, sorted by precedence (error logs followed by info logs). Each bin displays a maximum of five log entries.
- **Error:** The number of HTTP errors that occurred at the selected time.
- **TP:** Throughput of the requests at the selected time (req/s).
- **Latency:** Request latency at the selected time (ms).
- **CPU:** CPU usage at the selected time (millicores).
- **Memory:** Memory usage at the selected time (MiB).

## Logs

The **Logs** pane serves as a centralized view to observe logs of the components you deploy on Choreo. This facilitates rigorous troubleshooting and analysis.


# View Logs

The unified log view in Choreo allows you to view runtime and audit logs to gain application and user insights while ensuring data privacy.

Choreo provides real-time insights through live logs and allows you to view historical logs for insights into the past. You also have the flexibility to define a required time range to view relevant log entries, where an intuitive scrolling capability facilitates easy viewing of appropriate logs within the selected time frame.

The log view also provides advanced filtering capabilities that allow you to efficiently navigate through appropriate logs to expedite troubleshooting in distributed environments.

!!! info "Note"
        All personally identifiable information (PII) gets resolved at the frontend service level, with only relevant UUIDs stored in logs.

## Runtime logs

Choreo runtime logs provide insights into both project and component-level logs, covering application and gateway logs. These logs streamline the debugging process by centralizing diverse log sources.

In Choreo, any organization member can view runtime logs via the runtime logs page. Choreo allows you to apply filters based on parameters such as log level (error, warn, info, debug), log type (application, gateway), and environment (development, staging, production) to simplify the debugging process. 

To access runtime logs, follow the steps below:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the left navigation menu, click **Observability** and then click **Runtime Logs**. This displays runtime logs for the past 30 days by default.

    To view logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Runtime logs](../assets/img/monitoring-and-insights/view-logs/runtime-logs.png)

### Understand runtime logs

When you view component-level logs on the **Runtime Logs** page, you will see both application and gateway logs.

#### Application logs

Each application log entry displays the following details:

  - `timestamp`: The time when the request is received by the component.
  - `level`: Indicates the severity of the log message. Possible values are **Debug**, **Info**, **Warn**, and **Error**.
  - `componentVersion`: The version of the invoked component.
  - `componentVersionId`: The identifier of the invoked component’s version.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

#### Gateway logs

Each gateway log entry displays the following details:

  - `timestamp`: The time when the request is received by the gateway component.
  - `logLine`: Contains the following details about the request, including inbound and outbound information from the gateway perspective.
    - `Method`: The HTTP method of the request.
    - `RequestPath`: The path of the inbound request.
    - `ServicePath`: The path of the outbound request.
    - `UserAgent`: The user-agent header of the request.
    - `CorrelationID`: The request identifier of the inbound request. This is useful to track a request.
    - `ServiceHost`: The host IP of the backend.
    - `Duration`: The time taken for the gateway to serve the request.  
  - `gatewayCode`: Indicates the state of the request from the gateway perspective. Possible values are as follows:
    - `BACKEND_RESPONSE`:  Indicates successful processing of the request by the gateway with a response to the client from the backend application.
    - `CORS_RESPONSE`: Denotes a CORS (Cross Origin Resource Sharing) request.
    - `AUTH_FAILURE`: Indicates a request failure at the gateway due to authentication or authorization issues, such as an invalid token.
    - `NO_HEALTHY_BACKEND`: Indicates a request failure at the gateway due to a non-existent backend.
    - `RATE_LIMITED`: Indicates a request failure at the gateway due to surpassing the rate limit enforced within the component.
    - `RESOURCE_NOT_FOUND`: Indicates a request failure at the gateway due to the absence of a matching API resource for the inbound request. This can be caused by a mismatch in the HTTP method, path, or host.
    - `BACKEND_TIMEOUT`: Indicates a request timeout when calling the backend application from the gateway.
    - `GATEWAY_ERROR`: Indicates a request failure due to an erroneous behavior in the gateway.

    !!! info "Note"
         Occasionally, a request may not fit into any of the above categories. In such instances, the `gatewayCode` is displayed as `UNKNOWN`.

  - `statusCode`: The HTTP status code returned to the client.
  - `componentVersion`: The version of the invoked component.
  - `envName`: The environment of the inbound request. For example, Development, Production, etc.

## Audit logs

Audit logs, also called audit trails, enhance security, ensure compliance, provide operational insights, and help manage risks. 

In Choreo, an audit log records organization-level user-specific operations performed via the Choreo Console. It also captures the timestamp and the outcome of the action. 

As of now, Choreo captures the following user-specific operations as audit logs:

- Project creation, update, and deletion.
- Component creation, update, and deletion.
- Component promotion initiation.
- Component version creation.
- Component deployment, redeployment, and undeployment initiation for all components other than REST API Proxy components.
- Component API access mode update.
- Enabling and disabling component auto-deployment on commit. 
- Component build configuration update.
- Component endpoint creation, update, and deletion.
- Organization user management.
- On-premises key management.
- Project-level configuration management.

In Choreo, organization administrators are allowed to view audit logs by default. If other members need to access organization-specific audit logs, the administrator can create a role with the relevant permission and assign it to members. For step-by-step instructions on how to create and assign a role with relevant permission, see [Manage audit log access](#manage-audit-log-access).

To view audit logs, follow these steps:

1. Sign in to [Choreo](https://console.choreo.dev/).
2. In the Choreo Console, go to the top navigation menu and click **Organization**.
   
    !!! tip
         As of now, you can only view organization-level audit logs.

3. In the left navigation menu, click **DevOps** and then click **Audit Logs**. This displays audit logs for the past 30 days by default.

    To view audit logs based on a specific time range and other requirements, you can apply the necessary filter criteria.

    ![Audit logs](../assets/img/monitoring-and-insights/view-logs/audit-logs.png)

### Audit log retention

Choreo retains audit logs for one year and archives them for an additional year. Therefore, the total retention period for audit logs is two years.

### Manage audit log access

Follow the steps given below to create a role with audit log access permission and assign it to organization members who need access to audit logs:

!!! info "Note"
        You must be the organization administrator to perform this action.

#### Step 1: Create a role with audit log access permission

1. In the Choreo Console, go to the top navigation menu and click **Organization**.
2. In the left navigation menu, click **Settings**.
3. On the **Organization** tab, click **Roles** and then click **+ Create Role**.
4. Enter a name and description for the role.
   
     ![Create role](../assets/img/monitoring-and-insights/view-logs/create-role-to-view-audit-logs.png)

5. Click **Next**.
6. In the **Create Role** dialog, select **LOG-MANAGEMENT** under **Permissions**.

     ![Select log management permission](../assets/img/monitoring-and-insights/view-logs/log-management-permission.png)

7. Click **Create**.  


#### Step 2: Assign the created role to an organization member

1. On the **Organization** tab, click **Members**. This lists the members of the organization with their respective details.
2. Click on a member who needs to have access to audit logs, and then click **+ Add Role**.
   
    !!! tip
         If you want to invite one or more members and assign them the audit log viewer role, follow the steps given below:

           1. Click **+ Invite Member** and then click to expand the **Roles** list.
           2. Select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
           3. In the **Emails** field, enter the email addresses of members you want to invite and grant permission to access audit logs.
           4. Click **Invite**. This sends an invitation email to each email address so that the members can accept and obtain access to view audit logs.

3. Click to expand the **Roles** list and select the role you created in [Step 1](#step-1-create-a-role-with-audit-log-access-permission).
4. Click **Add**. This assigns the selected role to the member. 


# Configure CIO Dashboard

![CIO dashboard](../../assets/img/monitoring-and-insights/engineering-insights/cio-dashboard.png){.cInlineImage-full}

You can view DORA metrics in Choreo to use as KPIs to measure your organization's DevOps team's performance. Choreo enables this feature by default for all organizations. DORA includes the following four key metrics that are regarded as the most important metrics to indicate team performance:

- Deployment Frequency: How often an organization successfully releases to production
- Lead Time for Changes: The amount of time it takes a commit to get into production
- Change Failure Rate: The percentage of deployments causing a failure in production
- Time to Restore Service: How long it takes an organization to recover from a failure in production


Choreo enables two DORA metrics by default; deployment frequency and lead time for change.

## Configure the CIO Dashboard with all metrics

To configure the CIO dashboard by enabling the other two metrics, follow the steps below:

1. Sign in to Choreo using your Google, GitHub, or Microsoft account.
2. On the left navigation menu, click **Insights** and then click **Delivery**.
4. Scroll to the bottom of the dashboard and click **Configure**.
5. Select your incident management system. Currently, Choreo only supports GitHub. 

## Configuring GitHub as the incident management system

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/enable-dora-metrics.png){.cInlineImage-full}

To configure GitHub as the incident management system, follow the steps below: 

### Step 1: Authorize

![Authorize](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-cio-dashboard.png){.cInlineImage-threeQuarter}

First, let's authorize Choreo to access the repositories used to record incidents. 

On the **Add Integration** page,  select **GitHub** and click **Authorize with GitHub**.

Once the authorization process is complete, you can start configuring the GitHub repository.

### Step 2: Configure

![Configure](../../assets/img/monitoring-and-insights/engineering-insights/add-integration-configure.png){.cInlineImage-threeQuarter}

By default, Choreo collects incident details(issues) from all repositories containing Choreo components. However, you can configure a GitHub account and a GitHub repository to allow Choreo to read issues from a specific repository, and then click **Next**. 

| **Field**       | **Description**                   |   **Value**   |
|-----------------|-----------------------------|-----------------------------|
| **Data Plane**  | Choreo collects incident details by running a scheduled job which invokes the GitHub API periodically. This job runs on the user's data plane.   This configuration allows users to specify a preferred data plane to run the job, especially when they have multiple data planes. | Select a preferred data plane from the **Data Plane** list.        |
| **GitHub Account** | The GitHub account you have your repositories in.  | Select your GitHub account that includes the repository used for incident collection.|
| **GitHub Repository**| By default, Choreo will collect incident details(issues) from all repositories that already have Choreo components. |
    

### Step 3: Filter label

![Filter Label](../../assets/img/monitoring-and-insights/engineering-insights/filter-label.png){.cInlineImage-threeQuarter}

The filter label allows Choreo to scrape issues associated with that label.

- **Incident Label**:  The label Choreo uses to identify incidents. For example, `Type/Incident`. 

- **Invalid incident label**(Optional): Choreo will not scrape issues with this label and will proceed to skip these issues. For example, `Resolution/Invalid`. You can use this label when you want to ignore issues. For example, closing an issue after identifying that it doesn't qualify as an incident issue as it was due to a user error. 

Once you configure the labels, click **Save**.

Choreo will enable incident data publishing in the background once you save. Once completed, DORA metric charts will appear in the CIO dashboard for **Mean Time To Recover** and **Change Failure Rate**. If there are any issues in the configuration, the configure banner will reappear, and the user can proceed to reconfigure.

### Step 4: Enrich incident tickets with deployment information

Choreo extracts deployment information from the relevant incident and generates DORA metrics that help you analyze the deployment statistics related to the incidents. Therefore, you must manually update the GitHub issue with the relevant deployment-related information. Follow the steps below to add the deployment information to the GitHub issue. 
 
#### Get deployment details

1. On the Choreo Console header, select the project and the component for which the incident was reported.
2. On the left navigation menu, click **Deploy**.
3. On the **Production Environment** card, click **Deployment History**.
4. On the right-hand side panel, select the relevant deployment, and click **Release details** to copy the deployment details to the clipboard. 

    ![Copy to clipboard](../../assets/img/monitoring-and-insights/engineering-insights/deployment-copy-to-clipboard.png){.cInlineImage-small}

#### Add deployment information to the GitHub issue

1. Edit the GitHub issue to add the deployment information. 
2. Paste the deployment information you copied (in step 4 under the section `Get deployment details`) at the end of the issue body.
3. Click **Save**.

That's it! You have successfully configured your CIO dashboard to include the DORA metrics. 

!!! note
    The CIO Dashboard is expected to reflect the latest statistics within approximately 30 minutes.

## Edit configurations

   ![Edit configurations](../../assets/img/monitoring-and-insights/engineering-insights/edit-configurations.png){.cInlineImage-small}

   You can edit or override the configurations you made via the edit option in the dashboard. 


# View DORA metrics

DORA metrics comprise four key metrics. Let's explore what each metric represents in Choreo. Choreo displays a summary and graphical representation of each metric.

### Snapshot view

![DORA metric summary](../../assets/img/monitoring-and-insights/engineering-insights/dora-metrics-summary.png){.cInlineImage-full}

The snapshot view includes four tiles on the top of the dashboard, summarizing DORA metrics for the entire time period you select. The snapshot view categorizes each metric into four performance levels: elite, high, medium, and low. The categorization is based on the 2020 DORA metric report.

![DORA matrix](../../assets/img/monitoring-and-insights/engineering-insights/dora-matrix.png){.cInlineImage-threeQuarter}

### Time series view

The time series view provides a graphical representation of how the statistics have changed over a period of time. You can use this view to analyze team performance and identify trends. 

![Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/time-series-view.jpg){.cInlineImage-full}


## Deployment frequency

DORA team definition: The frequency at which an organization successfully releases to production.

In Choreo, this translates to the number of times an organization deploys a component to the production environment. Choreo does not count the deployment done to the development or other lower environments. 

### Snapshot view

![Deployment Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-snapshot.png){.cInlineImage-small}

The snapshot view of the `Deployment Frequency` metric shows the deployment frequency for all components within the selected organization. The frequency is dynamically determined and rounded to the nearest measurement. For example, if there is more than one deployment daily, the deployment frequency is measured in `deployments per day`. If the deployment frequency is less, it is measured in a higher granularity. For example, `deployments per week`.

A lower deployment frequency indicates that your organizational efficiency is low and that you need to evaluate and improve the processes to encourage frequent releases.

Choreo also displays the total number of deployments for the selected time range and the percentage increase or decrease compared to the previous time range.

### Time series view

![Deployment Frequency time series view](../../assets/img/monitoring-and-insights/engineering-insights/deployment-frequency-time-series.png){.cInlineImage-half}

The time series view for the `Deployment Frequency` metric visualizes the deployment count as a bar chart for the selected time period. Deployment count is aggregated based on the ‘view by’ selector. Hovering over each bar shows the counts for the aggregated period. 
Using this chart, organizations can identify deployment patterns, such as days of the week/months of the year where more deployments are likely to happen (near quarterly release days) and periods with fewer deployments. Decision-makers can then take steps to investigate and improve performance. 
This chart displays the pattern before and after a process change so you can use it to evaluate the team's performance after a significant process change. 

## Lead Time for Change

 DORA team definition: The time it takes for a commit to reach production.

 In Choreo, this translates into the time between committing and promoting a deployment to production. Although this approach may overlook any commits you push to production between two commits, it effectively assesses the efficiency of the review, approval, and CI/CD processes. Therefore, focusing on the production commits is adequate.  If a team commits locally for extended periods without deploying to production, this gets reflected in the `Deployment Frequency` charts.

### Snapshot view

![Lead Time For Change Frequency Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-summary.png){.cInlineImage-small}

The snapshot view of this metric displays the 95th percentile of the lead time for the selected time period. 95th percentile serves as a better representation as it filters out large outliers that can taint the average value. Lower lead times for change suggest that your organization has efficient processes for change review, approval, and CI/CD, while longer times suggest that the process needs to improve. Organizations can also use the categorization label to determine their standpoint on global standards.

Additionally, Choreo also displays the percentage increase or decrease compared to the last time period.

### Time series view

![Lead Time For Change Frequency Time Series View](../../assets/img/monitoring-and-insights/engineering-insights/lead-time-for-a-change-chart.png){.cInlineImage-half}

The time series view of this metric visualizes the lead time as a bar chart for the selected time period. The time is summed based on the ‘view by’ selector. To handle outliers, the y-axis employs a log scale that represents values read dynamically. Hovering over each bar displays the actual counts for the aggregated period. 
Using this chart, organizations can identify trends in their release process. For example, organizations can identify the time of the year when lead time rises, such as summer break. Also, organizations can use this to benchmark and evaluate new process changes. For example, if you introduced a process to include peer programming and reviewing, this chart can be used to evaluate its effect on the lead time and provide leadership with factual information to proceed further.

## Change failure rate

The DORA team definition: The percentage of deployments causing a failure in production. 

In Choreo, this translates to the ratio of deployments causing production failures to the total number of deployments. If there is at least one incident reported against a deployment, Choreo considers that deployment as a failed deployment in production. Any deployment-time failures are not counted as production failures because such failures don't impact the end user. For this metric to be accurate, the organization is expected to open incidents adhering to the proper format as it is crucial for Choreo to identify production failures. 

### Snapshot view

![Change Failure Rate Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-summary.png){.cInlineImage-small}

The snapshot view of this metric visualizes the change failure rate as a percentage for the selected time period. This will be the absolute percentage for the entire time period. When deciding on the time, the time of deployment is considered instead of the incident reported time. For example, the change failure rate for January 2023 will reflect the following:
 -  All deployments that happened within January.
 -  Any incidents that were reported at any time (in or after January) against the January deployments.

This view helps leadership assess the quality of deliverables and identify areas for improvement. Higher rates suggest that the organization needs to improve its processes to bring in more quality assurance aspects such as improved code coverage and end-to-end test coverage.

Additionally, Choreo also shows the percentage increase or decrease compared to the previous time period.

### Time series view

![Change Failure Rate Time Series](../../assets/img/monitoring-and-insights/engineering-insights/change-failure-rate-chart.png){.cInlineImage-half}

The time series view of this metric displays it as a line chart with data points corresponding to the granularity selected by the ‘view by’ selector. The absolute percentage is shown for each granularity.  Hovering over the line chart displays the actual counts for the aggregated period. 
This chart helps leadership identify timely trends in product quality aspects. For example, this view displays the months of the year where the failure rate is high (for example, close to quarterly release/announcement dates). Also, you can use this to measure the effectiveness of changes introduced to improve quality. For example, if the organization introduced an end-to-end test pipeline integration to the PR approval process, they can use this view to factually observe the timely impact of that change and determine how it decreases the failure rate.

## Mean Time to Recover(MTTR)

The DORA team definition: The time it takes for an organization to recover from a production failure.

In Choreo, this measures the time from identifying a production incident to resolving it. This metric reflects the responsiveness and agility of incident management teams.

Choreo depends on the open and close times of incidents to gather the relevant information. Therefore, for the dashboards to be accurate, organizations must follow process guidelines to update and close incident tickets efficiently in their incident management system.

### Snapshot view

![Mean Time to Recovery Snapshot](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-summary.png){.cInlineImage-small}

The snapshot view for this metric displays the  mean recovery time for the selected time period. Choreo dynamically adjusts the time unit to measure this metric for better readability.
This chart helps organizations evaluate the response time and agility of their incident handling teams, which in turn is an indication of stability. Higher MTTR means the leadership should look at new ways of improving the efficiency and agility of the teams handling incidents.

### Time series view

![Mean Time to Recovery Time Series](../../assets/img/monitoring-and-insights/engineering-insights/mean-time-to-recovery-chart.png){.cInlineImage-half}

The time series view of this metric shows how the mean time to recovery changes over time on a granularity based on the ‘view by’ selector. Each time the `granularity mean` would be used as the aggregation factor. Hovering over the line chart displays the actual counts for the aggregated period. 
This view helps leadership understand timely trends on mean time to recovery, such as higher values during holiday periods when there is less staff. Also, you can use this measurement to evaluate the effectiveness of process changes such as introducing an incident response plan. The trend view clearly shows the before and after statistics and the effectiveness of the process change.


# View Private Data Plane (PDP) Logs 

Choreo offers the capability to access runtime logs through its console. However, in cases where viewing logs for your PDP is not supported by Choreo yet, you can still view the runtime logs of your components via the log analyzing solution provided by your cloud vendor as a workaround.

## Prerequisites

Before you try out this guide, complete the following:

1. Go to [https://console.choreo.dev/](https://console.choreo.dev/), and sign in using your preferred method.
2. Select your component from **Components Listing**. This will open the **Overview** page of your component.
3. In the left navigation menu, click **Runtime** under **DevOps**.
4. Copy the `Release ID` and the `Namespace`. Save it for later.

## View Private Data Plane (PDP) logs with Azure Log Analytics

You can view your PDP logs with Azure Log Analytics by following the steps below: 

1. Go to https://portal.azure.com/.
2. Follow the [Azure Log Analytics Tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial#open-log-analytics) and open log analytics of your relative log analytics workspace.
3. Copy and paste the query below into the query editor. 
4. Replace the `<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>` and `<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>` values as required. Replace the '<RELEASE_ID>' and '<NAMESPACE>' with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
5. Run the query to extract the relevant logs.

```SQL
let startDateTime = datetime('<START_TIME_STAMP EX: 2023-04-10T07:07:31.684Z>');
let endDateTime = datetime('<END_TIME_STAMP EX: 2023-04-21T07:27:31.684Z>');
let releaseId = '<RELEASE_ID>';
let namespace = '<NAMESPACE>';
let searchPhrase = '<OPTIONAL SEARCH PHRASE>';
let startDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, startDateTime, endDateTime - 2m);let endDateTimeKPI = iff(datetime_diff('second', endDateTime, startDateTime) > 60, endDateTime, startDateTime + 2m);let filteredLogLevels = dynamic([]);
let hasNoLevelFilter = array_length(filteredLogLevels) == 0;
let commonKeys = dynamic(['time', 'level', 'module', 'traceId', 'spanId', 'message']);
let ContainerIdList = KubePodInventory
| where TimeGenerated > startDateTimeKPI and TimeGenerated < endDateTimeKPI
| where Namespace == namespace
| where extractjson('$.[0].release_id', PodLabel) == releaseId
| distinct ContainerID;
let data = ContainerLog
| where TimeGenerated > startDateTime and TimeGenerated < endDateTime
| where ContainerID in (ContainerIdList)
| where searchPhrase == "" or LogEntry contains searchPhrase
| top 126 by TimeGenerated desc
| extend logs = parse_json(LogEntry)
| project TimeGenerated, 
LogLevel = iif(isempty(logs['level']), iff(LogEntrySource == 'stderr', 'ERROR', 'INFO'), logs['level']), 
LogEntry = iif(isempty(logs['message']), logs, logs['message']),
KeyValuePair = bag_remove_keys(logs, commonKeys)
| where hasNoLevelFilter or LogLevel in (filteredLogLevels);
let lastTimeStamp = data 
| top 1 by TimeGenerated asc | project TimeGenerated;
let trimmedData = data | where TimeGenerated > toscalar(lastTimeStamp)| sort by TimeGenerated desc;
let selected = iff(toscalar(data | count) == 126, 'trimmedData', 'data');
let choose = (selector:string){   union   (trimmedData | where selector == 'trimmedData'),    (data | where selector == 'data')};
choose(selected);
```

## View Private Data Plane (PDP) logs with Amazon CloudWatch

1. Go to https://portal.azure.com/.
2. Follow the [AWS Analyzing Log Data documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) and open **Log Insights**.
3. Select the relevant region and the relevant log group (the log group string has the cluster name and “/application” appended at the end).
4. Select the required time range. 
4. Copy the query below and paste it into the query editor. 
5. Replace the `<RELEASE_ID>` with the values you copied by following the steps in the [prerequisites](#prerequisites) section. Replace the `<OPTIONAL SEARCH PHRASE>` with your search term, or leave it blank if you don't require any search filtering.
6. Run the query to extract the logs.

```  SQL 
fields @timestamp, @message
| filter kubernetes.labels.release_id == "<RELEASE_ID>"
| filter @message like "<OPTIONAL SEARCH PHRASE>"
```


# Access the Choreo Insights API

The **Usage Insights** page in the Choreo Console displays data retrieved from the Insights API exposed over the Internet. However, in some scenarios, you may need to retrieve data from external systems and implement custom dashboards to display the data.

Choreo provides a secure and user-friendly approach to accomplish this requirement. Follow the steps given below:

## Become a member of the Choreo System organization

1. Access the Developer Portal of the `Choreo System` organization via [https://devportal.choreo.dev/choreosystem/applications](https://devportal.choreo.dev/choreosystem/applications) and sign in using your preferred method.
   
2. To obtain access to the `Choreo System` organization, click **Request Access**.

    ![Request access](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/request-access.png){.cInlineImage-full}

## Create an application and generate keys

To create an application and generate keys, follow the steps below:

1. To create a new application in the `Choreo System` organization, click **+ Create Application**. 

2. Enter a name for the application and click **Create**. This creates the application and takes you to the **Overview** page.

3. To subscribe to the **Insights** API via the newly created application, follow the steps below:
    1.  In the left navigation menu, click **Subscriptions**.
    2.  In the **Subscription Management** pane, click **+ Add APIs**.
    3.  Search for `Insights` and click **Add**.

4. To generate credentials for the application, follow the steps given below:
    1. In the left navigation menu, click **Production** under **Credentials**.
    2. Click **Generate Credentials**. Choreo generates tokens and populates the **Consumer Key** and **Consumer Secret** fields in the **Application Keys** pane.

5. To specify an appropriate token expiry time for the application, follow the steps given below:
    1. In the **Application Keys** pane, click to expand **Advanced Configurations**.
    2. Specify an appropriate value in the **Application access token expiry time** field and click **Update**.
   
        ![Update token expiry time](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/update-token-expirary-time.png){.cInlineImage-threeQuarter}

6. Execute the following cURL command to generate an access token:

    ```bash
    curl --location --request POST 'https://sts.choreo.dev/oauth2/token' \
    --header 'Authorization: Basic <BASE64_ENCODED_CONSUMER_KEY_AND_CONSUMER_SECRET_OF_YOUR_APP_HERE>' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' \
    --data-urlencode 'orgHandle=<YOUR_ORG_HANDLE_HERE>' \
    --data-urlencode 'scope=apim:api_manage'
    ```

    !!! info
        To obtain your organization handle, follow the steps given below:

         1. Go to [https://console.choreo.dev](https://console.choreo.dev) and sign in using your preferred method.
         2. In the Choreo Console, click your username in the top right corner.
         3. In the drop-down menu, click **Settings**.
         4. In the **Organization** pane, click **Copy Handle**. 

    You can use the generated token to access the Insights API exposed via [https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api](https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api).

    The following is a sample cURL command to invoke the Insights API:

    ```bash
    curl --location --request POST 'https://choreocontrolplane.choreo.dev/93tu/insights/1.0.0/query-api' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <TOKEN_HERE>' \
    --data-raw '{"query":"query ($org: OrgFilter!) {listEnvironments(org: $org){id\n name}}","variables":{"org":{"orgId":"<ORG_UUID_HERE>"}}}'
    ```

    !!! tip
         - When the token expires, you can generate a new token programmatically by making an API call to the token endpoint using the client credentials grant type.
        - If a token theft occurs, you can revoke the token by making an API call to the revoke endpoint.

        ![Endpoints](../../assets/img/monitoring-and-insights/work-with-choreo-insights-api/endpoints.png){.cInlineImage-threeQuarter}


# Choreo Insights API

The Choreo Insights API is a GraphQL API that allows you to retrieve data from external systems based on specific criteria. This guide describes the operations and schema-defined types you can use to retrieve data via the Choreo Insights API.

 - **Allowed operations:** [Queries](#query)
 - **Schema-defined types:** [Objects](#objects), [Inputs](#inputs), [Enums](#enums), and [Scalars](#scalars)

##Try out

You can try out the Choreo Insights API with your data via [GraphQL Explorer](graphiql-explorer/index.html).

!!! warning
    The GraphQL Explorer is currently not compatible with the Safari web browser due to a [known issue](https://developer.apple.com/forums/thread/658688).

## Query
The query root of the Choreo Insights GraphQL API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>listAllAPI</strong></td>
<td valign="top">[<a href="#api">API</a>]</td>
<td>

Fetches all the APIs with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>provider</code> parameter to further filter the APIs by a specific provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">provider</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the API provider.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listApplications</strong></td>
<td valign="top">[<a href="#application">Application</a>]</td>
<td>

Fetches all the applications with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>applicationFilter</code> parameter to further filter the applications by a specific application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">applicationFilter</td>
<td valign="top"><a href="#applicationfilter">ApplicationFilter</a></td>
<td>

The application filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listProviders</strong></td>
<td valign="top">[<a href="#provider">Provider</a>]</td>
<td>

Fetches all the API providers with the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listSubscribers</strong></td>
<td valign="top">[<a href="#subscriber">Subscriber</a>]</td>
<td>

Fetches all the API subscribers with the given combination of tenant ID, environment ID, and organization ID. Optionally, you
can configure the <code>subscriberFilter</code> parameter to further filter the subscribers.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">subscriberFilter</td>
<td valign="top"><a href="#subscriberfilter">SubscriberFilter</a></td>
<td>

The subscriber filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listOrganizations</strong></td>
<td valign="top">[<a href="#organization">Organization</a>]</td>
<td>

Fetches all the organizations of a user.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listEnvironments</strong></td>
<td valign="top">[<a href="#environment">Environment</a>]</td>
<td>

Fetches all the environments of an organization.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">org</td>
<td valign="top"><a href="#orgfilter">OrgFilter</a>!</td>
<td>

The organization filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">projectId</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>listTenants</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

Fetches all the tenants with the given combination of environment ID and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">tenantDataFilter</td>
<td valign="top"><a href="#tenantdatafilter">TenantDataFilter</a>!</td>
<td>

The tenant filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTraffic</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total traffic during the given time range for the specified combination of tenant ID, environment ID,
and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrors</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total number of errors that occurred during the given time range for the specified combination of tenant
ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatency</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

Returns the overall response latency (95th percentile value) during the given time range for the specified
combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatencySummary</strong></td>
<td valign="top"><a href="#latencysummary">LatencySummary</a></td>
<td>

Returns the response latency value (95th percentile value) for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>latencySummaryFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencySummaryFilter</td>
<td valign="top"><a href="#latencysummaryfilter">LatencySummaryFilter</a></td>
<td>

The latency summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessSummary</strong></td>
<td valign="top"><a href="#successsummary">SuccessSummary</a></td>
<td>

Returns the number of successful (2xx response code) hit count for each time granularity within the specified time
range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorSummary</strong></td>
<td valign="top"><a href="#errorsummary">ErrorSummary</a></td>
<td>

Returns the number of unsuccessful hits (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID. Optionally, you can configure the <code>granularity</code> parameter to override the default granularity value.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByCategory</strong></td>
<td valign="top"><a href="#errorsbycategory">ErrorsByCategory</a></td>
<td>

Returns the number of proxy errors (i.e., the total of both <code>4xx</code> and <code>5xx</code> response codes) by each error category
for each time granularity within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>errorsByCategoryFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByCategoryFilter</td>
<td valign="top"><a href="#errorsbycategoryfilter">ErrorsByCategoryFilter</a></td>
<td>

The errors by category filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsDetails</strong></td>
<td valign="top"><a href="#detailsoferrors">DetailsOfErrors</a></td>
<td>

Returns details of each proxy error (for both <code>4xx</code> and <code>5xx</code> response codes) within the specified time range for
the given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>errorsDetailsFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsDetailsFilter</td>
<td valign="top"><a href="#errorsdetailsfilter">ErrorsDetailsFilter</a></td>
<td>

The error details filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getProxyTargetErrorsOverTime</strong></td>
<td valign="top">[<a href="#errorsbystatuscodecategory">ErrorsByStatusCodeCategory</a>]</td>
<td>

Returns a list of hit counts for proxy and target errors for each time granularity within the specified time range
for the given combination of tenant ID, environment ID, and organization ID. The errors in each proxy and target
result set are grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>. Optionally, you can configure the <code>errorsByStatusCodeFilter</code>
parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorsByStatusCodeFilter</td>
<td valign="top"><a href="#errorsbystatuscodefilter">ErrorsByStatusCodeFilter</a></td>
<td>

The errors by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getErrorsByStatusCode</strong></td>
<td valign="top"><a href="#errorsbystatuscode">ErrorsByStatusCode</a></td>
<td>

Returns the hit count for each error response code (<code>401</code>, <code>404</code>, and <code>500</code> etc.,) for each API within the specified
time range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">errorCountByStatusCodeFilter</td>
<td valign="top"><a href="#errorcountbystatuscodefilter">ErrorCountByStatusCodeFilter</a>!</td>
<td>

The error count by status code filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalErrorsByAPI</strong></td>
<td valign="top"><a href="#totalerror">TotalError</a></td>
<td>

Returns the total proxy error hit count for an API across for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given
time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageOverTime</strong></td>
<td valign="top">[<a href="#apiusageovertime">APIUsageOverTime</a>]</td>
<td>

Returns a list of details related to the usage of each API over time for each time granularity within the specified
time range for the given combination of tenant ID, environment ID, and organization ID. Optionally, you can
configure the <code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByAppOverTime</strong></td>
<td valign="top"><a href="#apiusagebyappovertime">APIUsageByAppOverTime</a></td>
<td>

Returns API usage by each application over time for each time granularity within the specified time range for the
given combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageOvertimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageOvertimeFilter</td>
<td valign="top"><a href="#apiusageovertimefilter">APIUsageOverTimeFilter</a></td>
<td>

The API usage overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByBackendOverTime</strong></td>
<td valign="top"><a href="#apiusagebybackendovertime">APIUsageByBackendOverTime</a></td>
<td>

Returns API usage by each backend over time for each time granularity within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByBackendOverTimeFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByBackendOverTimeFilter</td>
<td valign="top"><a href="#apiusagebybackendovertimefilter">APIUsageByBackendOverTimeFilter</a></td>
<td>

The API usage by backend overtime filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getResourceUsage</strong></td>
<td valign="top"><a href="#resourceusages">ResourceUsages</a></td>
<td>

Returns API usage by resource within the specified time range for the given combination of tenant ID, environment
ID, and organization ID. Optionally, you can configure the <code>resourceUsageFilter</code> parameter to further filter the
results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">resourceUsageFilter</td>
<td valign="top"><a href="#resourceusagefilter">ResourceUsageFilter</a></td>
<td>

The resource usage filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTotalTrafficByAPI</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Returns the total hit count for an API for the given combination of tenant ID, environment ID, and organization ID.
Optionally, you can configure the <code>filter</code> parameter to further filter the results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>topSlowestAPIs</strong></td>
<td valign="top">[<a href="#slowapi">SlowAPI</a>]</td>
<td>

Returns a list of top slowest APIs based on the response latency (95th percentile value) within the specified time
range for the given combination of tenant ID, environment ID, and organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The limit for the slow APIs list.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getLatency</strong></td>
<td valign="top"><a href="#apilatency">APILatency</a></td>
<td>

Returns different latency category values (95th percentile values) for a given API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and organization
ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">latencyFilter</td>
<td valign="top"><a href="#latencyfilter">LatencyFilter</a>!</td>
<td>

The latency filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getOverallLatencyByAPI</strong></td>
<td valign="top"><a href="#overalllatency">OverallLatency</a></td>
<td>

Returns the overall response latency (95th percentile value) for an API for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>filter</code> parameter to further filter the
results by a given time range.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">filter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a></td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiId</td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The API ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCacheHitsAndMisses</strong></td>
<td valign="top"><a href="#cachehits">CacheHits</a></td>
<td>

Return the total number of response cache hits, misses, and hit percentage for an API over time for each time
granularity within the specified time range for the given combination of tenant ID, environment ID, and
organization ID.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cacheFilter</td>
<td valign="top"><a href="#cachefilter">CacheFilter</a></td>
<td>

The cache filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopPlatforms</strong></td>
<td valign="top">[<a href="#platform">Platform</a>]</td>
<td>

Returns a list of top platforms ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine platforms with
the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit count.
Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopUserAgents</strong></td>
<td valign="top">[<a href="#useragent">UserAgent</a>]</td>
<td>

Returns a list of top user agents ranked based on the hit count within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. The result list includes the top nine user agents
with the respective hit count, and all the rest of the platforms are labeled as **Other** with the cumulated hit
count. Optionally, you can configure the <code>deviceFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">deviceFilter</td>
<td valign="top"><a href="#devicefilter">DeviceFilter</a></td>
<td>

The device filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIUsageByGeoLocation</strong></td>
<td valign="top">[<a href="#usagebygeolocation">UsageByGeoLocation</a>]</td>
<td>

NOTE: Currently, this operation returns data only for on-premise environments.

Returns API usage by country within the specified time range for the given combination of tenant ID, environment ID,
and organization ID. Optionally, you can configure the <code>geoLocationFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">geoLocationFilter</td>
<td valign="top"><a href="#geolocationfilter">GeoLocationFilter</a></td>
<td>

The geolocation filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#apiusagebyapplication">APIUsageByApplication</a>]</td>
<td>

Returns details relating to the usage of each API by application within the specified time range for the given
combination of tenant ID, environment ID, and organization ID. Optionally, you can configure the
<code>apiUsageByAppFilter</code> parameter to further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">apiUsageByAppFilter</td>
<td valign="top"><a href="#apiusagebyappfilter">APIUsageByAppFilter</a></td>
<td>

The API usage by app filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getTopAPIsByAlertCount</strong></td>
<td valign="top"><a href="#topapisbyalertcount">TopAPIsByAlertCount</a></td>
<td>

Returns top APIs ranked based on the alert count within the specified time range for the given combination of tenant
ID, environment ID, and organization ID. Optionally, you can configure the <code>topAPIsByAlertCountFilter</code> parameter to
further filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">topAPIsByAlertCountFilter</td>
<td valign="top"><a href="#topapisbyalertcountfilter">TopAPIsByAlertCountFilter</a></td>
<td>

The top APIs by alert count filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getAlertSummary</strong></td>
<td valign="top"><a href="#alertsummaries">AlertSummaries</a></td>
<td>

Returns a summary for each alert within the specified time range for the given combination of tenant ID,
environment ID, and organization ID. Optionally, you can configure the <code>alertSummaryFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">alertSummaryFilter</td>
<td valign="top"><a href="#alertsummaryfilter">AlertSummaryFilter</a></td>
<td>

The alert summary filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplications</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

NOTE: This operation can only be invoked via using an on-prem key as the authentication header.

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getSuccessAPIsUsageByApplicationsWithOnPremKey</strong></td>
<td valign="top">[<a href="#successapiusagebyapplication">SuccessAPIUsageByApplication</a>]</td>
<td>

Returns a list of successful hit counts (i.e., 2xx response codes) within the specified time range for each API,
grouped by each application. Optionally, you can configure the <code>successAPIUsageByAppFilter</code> parameter to further
filter the results.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">onPremKey</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The value of the On-Prem key.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">successAPIUsageByAppFilter</td>
<td valign="top"><a href="#successapiusagebyappfilter">SuccessAPIUsageByAppFilter</a></td>
<td>

The successful API usage by application filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportOvertime</strong></td>
<td valign="top"><a href="#customreportovertime">CustomReportOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getCustomReportTopOvertime</strong></td>
<td valign="top"><a href="#customreporttopovertime">CustomReportTopOvertime</a></td>
<td>

Returns the summary of hits or latency data as specified for the selected time duration, grouped by time spans for
the top N values for the selected groupByField.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeFilter</td>
<td valign="top"><a href="#timefilter">TimeFilter</a>!</td>
<td>

The time filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">metric</td>
<td valign="top"><a href="#metric">Metric</a>!</td>
<td>

The metric for which data needs to be retrieved.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field by which the data should be grouped.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">granularity</td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>getGroupByValues</strong></td>
<td valign="top">[[<a href="#string">String</a>]]</td>
<td>

Returns a list of value sets by which you can group the data available for the selected <code>groupBy</code> fields.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">dataFilter</td>
<td valign="top"><a href="#datafilter">DataFilter</a>!</td>
<td>

The data filter.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByFields</td>
<td valign="top">[<a href="#groupbyfield">GroupByField</a>]!</td>
<td>

The column/field for which the API needs to retrieve distinct values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">groupByValues</td>
<td valign="top">[<a href="#string">String</a>]!</td>
<td>

The value used to filter by the <code>groupByField</code>.

</td>
</tr>
</tbody>
</table>

## Objects

### API

Represents API details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>version</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API version.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>provider</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### APILatency

Represents latency values for a single API over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latency">Latency</a>]</td>
<td>

A list containing latency category values over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsage

Represents the API usage for a single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The API usage count.

</td>
</tr>
</tbody>
</table>

### APIUsageByApp

Represents API usage across APIs by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByAppOverTime

Represents API usage across APIs by applications over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebyapp">APIUsageByApp</a>]</td>
<td>

A list containing the API usage values across APIs, grouped by the application. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageByApplication

Represents a single API usage by a single application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API by the application.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackend

Represents API usage across APIs by a single backend.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the backend.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the APIs usage values. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTime

Represents API usage across APIs by each backend over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusagebybackend">APIUsageByBackend</a>]</td>
<td>

A list containing the API usage values across APIs by each backend. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTime

Represents a single API usage over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#apiusage">APIUsage</a>]</td>
<td>

A list containing the API usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### AlertSummaries

Represents alert summaries.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#alertsummary">AlertSummary</a>]</td>
<td>

A list containing the alert summary for each alert. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### AlertSummary

Represents a summary for an alert.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timestamp</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert category. Possible values are <code>LATENCY</code> and <code>TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>metric</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert metric. Possible values are <code>RESPONSE_LATENCY</code> and <code>TOTAL_TRAFFIC</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>severity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The severity level of the alert. Possible values are <code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>message</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The alert details.

</td>
</tr>
</tbody>
</table>

### Application

Represents application details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
</tbody>
</table>

### CacheHit

Represents the response cache hits and misses for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hits</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was hit.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>misses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of times the response cache was missed.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hitPercentage</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

The response cache hits as a percentage of the sum of hits and misses.

</td>
</tr>
</tbody>
</table>

### CacheHits

Represents the response cache hits and misses over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#cachehit">CacheHit</a>]</td>
<td>

A list containing cache hits, misses, and the hit percentage over time. Returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportGroupBy

Represents the usage data overtime for the selected parameters of a specific <code>groupByValue</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>groupByValue</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The distinct group-by value that is used as an ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### CustomReportOvertime

Represents usage data overtime for the selected parameters.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportusage">CustomReportUsage</a>]</td>
<td>

A list containing the usage values. This returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportTopOvertime

Represents usage data overtime for the selected parameters grouped by the top N <code>groupByValues</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#customreportgroupby">CustomReportGroupBy</a>]</td>
<td>

A list containing the usage values grouped by the selected <code>groupByField</code>. This returns an empty array if no data is
available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### CustomReportUsage

Represents usage data for a single timestamp in <code>CustomReports</code>.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>value</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage value (Hit Count/ Latency).

</td>
</tr>
</tbody>
</table>

### DetailsOfErrors

Represents error details over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#errordetails">ErrorDetails</a>]!</td>
<td>

A list containing error details over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### Environment

Represents an environment.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>externalEnvId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The external environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>internalEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The internal environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sandboxEnvId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The sandbox environment ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The environment name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>type</strong></td>
<td valign="top"><a href="#environmenttype">EnvironmentType</a>!</td>
<td>

The environment type. A Choreo environment is labeled as <code>CHOREO</code>, a private Choreo environment is labeled as
<code>CHOREO_PRIVATE</code>, and the on-premise environment is labeled as <code>ON_PREM</code>.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCategory

Represents the number of errors from each category for a single timestamp. The timestamp is calculated according to the
provided granularity value. If you select some categories, the error counts are retrieved only for those categories,
and a <code>null</code> value is shown for the other categories that are not selected.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>auth</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of authorization errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>targetConnectivity</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of target connectivity errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>throttled</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of throttling errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>other</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The count of other errors.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCode

Represents the error count for a single error status code.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>statusCode</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The error status code.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorCountByCodeForAPI

Represents the error count for each status code for a single API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCountByCode</strong></td>
<td valign="top">[<a href="#errorcountbycode">ErrorCountByCode</a>]</td>
<td>

A list containing the error count for each error status code. Returns an empty array if no data is available.

</td>
</tr>
</tbody>
</table>

### ErrorDetails

Represents details of an error for a single timestamp. The timestamp is calculated according to the granularity value
provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The Application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>reason</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The reason for the error.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The error count.

</td>
</tr>
</tbody>
</table>

### ErrorStatusCodeCategoryCounts

Represents errors by the main status code (<code>4xx</code> or <code>5xx</code>) and the total error count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_4xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of client errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_5xx</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The number of server errors.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of client and server errors.

</td>
</tr>
</tbody>
</table>

### ErrorSummary

Provides the unsuccessful usage (i.e., <code>4xx</code> and <code>5xx</code> response codes) summary across all APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#errorvalue">ErrorValue</a>]!</td>
<td>

A list containing unsuccessful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorValue

Represents the unsuccessful request count (i.e., <code>4xx</code> and <code>5xx</code> response codes) for a single timestamp. The timestamp
is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCount</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

Represents the error request count.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategory

Represents the errors by category over time.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycategory">ErrorCountByCategory</a>]</td>
<td>

A list containing the error count for each error category over time. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCode

Represents the error counts grouped by status code for each API.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>errors</strong></td>
<td valign="top">[<a href="#errorcountbycodeforapi">ErrorCountByCodeForAPI</a>]!</td>
<td>

A list containing the error count for each status code for each API. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeCategory

Represents the error category values (grouped as <code>4xx</code>, <code>5xx</code>, and <code>total</code>) for both proxy and target errors for a
single timestamp. The timestamp is calculated based on the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents proxy-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code> response
codes), and the total of both categories.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#errorstatuscodecategorycounts">ErrorStatusCodeCategoryCounts</a></td>
<td>

Represents target-related errors categorized as client errors (<code>4xx</code> response codes) or server errors (<code>5xx</code>
response codes), and the total of both categories.

</td>
</tr>
</tbody>
</table>

### Latency

Represents latency values for each latency category for a single timestamp. The timestamp is calculated based on the
granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backend</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The backend latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The request mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediation</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The response mediation latency (95th percentile) in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>backendMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the backend latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the request mediation latency in milliseconds (ms).

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>responseMediationMedian</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The median (50th percentile) of the response mediation latency in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### LatencySummary

Provides the latency summary.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#latencyvalue">LatencyValue</a>]!</td>
<td>

A list containing latency values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### LatencyValue

Represents the latency value for a single timestamp. The timestamp is calculated according to the provided granularity
value.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latencyTime</strong></td>
<td valign="top"><a href="#float">Float</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Organization

Represents an organization.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>uuid</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The organization UUID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>handle</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization handle name.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization name.

</td>
</tr>
</tbody>
</table>

### OverallLatency

Represents the overall latency values.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>response</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td>

The response latency (95th percentile value) in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Pagination

Represents pagination details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>total</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The total number of results.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The number of items in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The offset value for the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting column name of the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The sorting order of the result set. Possible values are <code>asc</code> and <code>desc</code>.

</td>
</tr>
</tbody>
</table>

### Platform

Represents a platform.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>platform</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the platform.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the platform.

</td>
</tr>
</tbody>
</table>

### Provider

Represents API Provider details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API provider name.

</td>
</tr>
</tbody>
</table>

### ResourceUsage

Represents the usage of a single API resource.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiResourceTemplate</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiMethod</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The API method.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API resource.

</td>
</tr>
</tbody>
</table>

### ResourceUsages

Represents API resource usages.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#resourceusage">ResourceUsage</a>]</td>
<td>

A list with the usage of each API resource. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

Pagination details.

</td>
</tr>
</tbody>
</table>

### SlowAPI

A slow API identified based on the response latency (95th percentile).

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>latency</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the latency (95th percentile) time in milliseconds (ms).

</td>
</tr>
</tbody>
</table>

### Subscriber

Represents API Subscriber details.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API subscriber.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByApplication

Represents successful usages(that have resulted in the <code>2xx</code> response code) of an API by an application.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiVersion</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The version of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiCreatorTenantDomain</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The tenant domain of the API creator.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The application ID.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationName</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>applicationOwner</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the application owner.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### SuccessSummary

Provides the successful (2xx response code) usage summary across all the APIs.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>summary</strong></td>
<td valign="top">[<a href="#successvalue">SuccessValue</a>]!</td>
<td>

A list containing successful usage values. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The granularity value for which data is retrieved.

</td>
</tr>
</tbody>
</table>

### SuccessValue

Represents the successful request count (i.e., requests that have received the <code>2xx</code> response code) for a single
timestamp. The timestamp is calculated according to the granularity value provided.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeSpan</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Represents a timestamp value that is calculated based on the specified granularity value. For example, if the
granularity value is <code>1d</code>, the timestamp represents the start of the day calculated adhering to the timezone
provided in the time filter.
e.g., <code>timeSpan: '2021-06-21T00:00:00.0000000+05:30'</code>

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>requestCount</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

Represents the successful request count.

</td>
</tr>
</tbody>
</table>

### TopAPIByAlertCount

Represents a top API by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#id">ID</a>!</td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The alert count.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCount

Represents the top APIs by alert count.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>usage</strong></td>
<td valign="top">[<a href="#topapibyalertcount">TopAPIByAlertCount</a>]</td>
<td>

A list containing top APIs by alert count. Returns an empty array if no data is available.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>pagination</strong></td>
<td valign="top"><a href="#pagination">Pagination</a>!</td>
<td>

The pagination details.

</td>
</tr>
</tbody>
</table>

### TotalError

Represents the total errors.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>proxy</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The proxy-related error count.

</td>
</tr>
</tbody>
</table>

### UsageByGeoLocation

Represents the usage of a single API in a single country.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>country</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the country.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the API.

</td>
</tr>
</tbody>
</table>

### UserAgent

Represents a user agent.

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>userAgent</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the user agent.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td>

The usage of the user agent.

</td>
</tr>
</tbody>
</table>

## Inputs

### APIUsageByAppFilter

Filters the API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribers</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of subscribers you specify here. A maximum of five subscriber IDs can be
defined.

</td>
</tr>
</tbody>
</table>

### APIUsageByBackendOverTimeFilter

Filters the results for API usage by backend over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### APIUsageOverTimeFilter

Filters the results for API usage over time.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of applications you specify here. A maximum of five application IDs can be
defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### AlertSummaryFilter

Filters the alerts summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The alert category by which the results need to be filtered. The available categories to select are <code>TRAFFIC</code> and
<code>LATENCY</code>.

</td>
</tr>
</tbody>
</table>

### ApplicationFilter

Filters applications by the application owner and API IDs.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>owner</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### CacheFilter

Filters response cache results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### DataFilter

Filters results by the given combination of organization, environment, and tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The organization by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The environment ID by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenant</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The name of the tenant by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>projectId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The project ID by which the results need to be filtered. It is optional to specify a value for this
parameter. Note that providing a project ID with an on-prem key is not allowed.

</td>
</tr>
</tbody>
</table>

### DeviceFilter

Filters results related to devices.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### ErrorCountByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorType</strong></td>
<td valign="top"><a href="#errortype">ErrorType</a>!</td>
<td>

The type of the error. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>errorCodeType</strong></td>
<td valign="top"><a href="#errorcodetype">ErrorCodeType</a></td>
<td>

The error code type. If this parameter is not configured, both client-related error response codes (<code>401</code>, <code>404</code>,
etc.) and server-related response codes (<code>500</code>, <code>501</code>, etc.) are included in the result set.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
</tbody>
</table>

### ErrorsByCategoryFilter

Filters errors by category results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the API.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>categories</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of categories by which the results need to be filtered. Category values that you can specify here are
<code>AUTH</code>, <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsByStatusCodeFilter

Filters errors by status code results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### ErrorsDetailsFilter

Filters the results for error details.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>appId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The application ID by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>category</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The error category by which the results need to be filtered. The error category that you can specify here must be
one of the <code>AUTH</code> <code>TARGET_CONNECTIVITY</code>, <code>THROTTLED</code>, and <code>OTHER</code> values.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### GeoLocationFilter

Filters the API usage by geolocation results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here.

</td>
</tr>
</tbody>
</table>

### LatencyFilter

Filters latency results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The results are filtered by the API ID specified here. It is required to specify a value for this parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### LatencySummaryFilter

Filters latency summary results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The results are filtered by the API ID specified here.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>granularity</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The granularity value that is used for data retrieval. If the granularity value is not set, the default granularity
for the related time range is applied. The possible granularity values that you can specify are <code>1m</code>, <code>15m</code>, <code>1h</code>,
<code>1d</code>, and <code>7d</code>.

</td>
</tr>
</tbody>
</table>

### OrgFilter

Filters results for the given organization.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
</tbody>
</table>

### PaginationFilter

Filters related to pagination.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>limit</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The total number of rows in the result set. This value must be a positive integer. If this limit value is not set,
the total number of rows is five by default.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>offset</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td>

The offset value to set when filtering results. This value must be zero or a positive integer. If you do not specify
an offset value, the default offset value (i.e., <code>0</code>) applies.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortBy</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The column name by which the results are sorted. If the <code>sortBy</code> value is not set, the default column of the related
operation that is available for sorting purposes is used.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sortOrder</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The order in which the results are sorted. Possible values are <code>asc</code> (to sort in ascending order) and <code>desc</code> (to
sort in descending order). If no value is specified, the results are sorted in ascending order by default (except
for count-specific operations such as <code>getTopAPIsByAlertCount</code> where the results are always sorted in descending
order).

</td>
</tr>
</tbody>
</table>

### ResourceUsageFilter

Filters resource usage results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

### SearchFilter

Filters results by searching matching results for the provided search text.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs that need to be searched with the given search text. Note that it is not possible to define API
IDs without a search text in the search filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchText</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

Text which needs to be searched among the results. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### SubscriberFilter

Filters the subscriber results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The results are filtered for the list of APIs you specify here. A maximum of five API IDs can be defined.

</td>
</tr>
</tbody>
</table>

### SuccessAPIUsageByAppFilter

Filters successful API usage by application results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>apiIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The list of API IDs by which the results need to be filtered.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>tenantDomains</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The tenant domain name by which the results need to be filtered.

</td>
</tr>
</tbody>
</table>

### TenantDataFilter

Filters results by the tenant.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>orgId</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The ID of the organization by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>envId</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td>

The ID of the environment by which the results need to be filtered. It is required to specify a value for this
parameter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>environmentIds</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td>

The environment IDs by which the results need to be filtered. It is required to specify a value for this parameter.

</td>
</tr>
</tbody>
</table>

### TimeFilter

Filters results by the provided date range.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>from</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The start date of the time range. The date specified here must be a date earlier than the date specified via the
<code>to</code> parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:00:00.000+05:30'</code>.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>to</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td>

The end date of the time range. The date specified here must be a date later than the date specified via the <code>from</code>
parameter. If the defined date and time entry do not have a timezone, the <code>UTC</code> time zone (z) is used. It is
required to specify a value for this parameter.
e.g., <code>'2021-08-16T12:30:00.000+05:30'</code>.

</td>
</tr>
</tbody>
</table>

### TopAPIsByAlertCountFilter

Filters the top APIs by alert count results.

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>paginationFilter</strong></td>
<td valign="top"><a href="#paginationfilter">PaginationFilter</a></td>
<td>

The pagination filter.

</td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>searchFilter</strong></td>
<td valign="top"><a href="#searchfilter">SearchFilter</a></td>
<td>

The search filter.

</td>
</tr>
</tbody>
</table>

## Enums

### EnvironmentType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>CHOREO</strong></td>
<td>

The Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>CHOREO_PRIVATE</strong></td>
<td>

The private data-plane Choreo environments.

</td>
</tr>
<tr>
<td valign="top"><strong>ON_PREM</strong></td>
<td>

The On-Premise environments.

</td>
</tr>
</tbody>
</table>

### ErrorCodeType

Represents an error code type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>_4XX</strong></td>
<td>

The client-side errors.

</td>
</tr>
<tr>
<td valign="top"><strong>_5XX</strong></td>
<td>

The server-side errors.

</td>
</tr>
</tbody>
</table>

### ErrorType

Represents an error type.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>PROXY</strong></td>
<td>

The proxy-related errors.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET</strong></td>
<td>

The target-related errors.

</td>
</tr>
</tbody>
</table>

### GroupByField

Represents an <code>groupByField</code> used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>API_NAME</strong></td>
<td>

The API name.

</td>
</tr>
<tr>
<td valign="top"><strong>API_VERSION</strong></td>
<td>

The API version.

</td>
</tr>
<tr>
<td valign="top"><strong>API_RESOURCE_TEMPLATE</strong></td>
<td>

The API resource template.

</td>
</tr>
<tr>
<td valign="top"><strong>API_METHOD</strong></td>
<td>

The API method.

</td>
</tr>
<tr>
<td valign="top"><strong>API_CREATOR</strong></td>
<td>

The API creator.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_NAME</strong></td>
<td>

The name of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>APPLICATION_OWNER</strong></td>
<td>

The owner of the application.

</td>
</tr>
<tr>
<td valign="top"><strong>DESTINATION</strong></td>
<td>

The destination.

</td>
</tr>
<tr>
<td valign="top"><strong>USER_AGENT</strong></td>
<td>

The user Agent.

</td>
</tr>
<tr>
<td valign="top"><strong>PLATFORM</strong></td>
<td>

The platform.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_RESPONSE_CODE</strong></td>
<td>

The target response code.

</td>
</tr>
</tbody>
</table>

### Metric

Represents a metric used in <code>CustomReports</code>.

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>HIT_COUNT</strong></td>
<td>

The number of API calls.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_CACHE_HIT</strong></td>
<td>

The number of API calls that used the response cache.

</td>
</tr>
<tr>
<td valign="top"><strong>REQUEST_MEDIATION_LATENCY</strong></td>
<td>

The request mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>RESPONSE_MEDIATION_LATENCY</strong></td>
<td>

The response mediation latency.

</td>
</tr>
<tr>
<td valign="top"><strong>BACKEND_LATENCY</strong></td>
<td>

The backend latency.

</td>
</tr>
<tr>
<td valign="top"><strong>TOTAL_LATENCY</strong></td>
<td>

The total latency.

</td>
</tr>
<tr>
<td valign="top"><strong>API_ERRORS</strong></td>
<td>

The number of hits for which API errors are returned.

</td>
</tr>
<tr>
<td valign="top"><strong>TARGET_ERRORS</strong></td>
<td>

The number of hits for which target errors are returned.

</td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The <code>Boolean</code> scalar type represents <code>true</code> or <code>false</code>.

### Float

The <code>Float</code> scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### ID

The <code>ID</code> scalar type represents a unique identifier, often used to re-fetch an object or as the key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as <code>"4"</code>) or integer (such as <code>4</code>) input value is accepted as an ID.

### Int

The <code>Int</code> scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The <code>String</code> scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.



