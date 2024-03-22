# Asset Management System

## Overview

The Asset Management System is a Flask web application designed to facilitate the efficient tracking, monitoring, and management of assets within an organization. This system aims to streamline asset management processes, improve accountability, and optimize resource allocation.

## Features

1. **Asset Tracking:** 
   - Maintain a centralized repository of all assets including hardware, software, equipment, and other resources.
   - Assign unique identifiers to each asset for easy tracking and identification.
   - Capture detailed information about each asset such as its description, location, acquisition date, and assigned user.

2. **Inventory Management:**
   - Keep an up-to-date inventory of available assets, including quantities, conditions, and usage history.
   - Automatically update inventory records upon asset addition, disposal, or transfer.
   - Generate inventory reports to analyze asset utilization and identify potential optimization opportunities.

3. **Asset Lifecycle Management:**
   - Monitor the entire lifecycle of assets from procurement to retirement.
   - Schedule maintenance tasks, inspections, and renewals to ensure optimal asset performance and longevity.
   - Implement workflows for asset request, approval, and provisioning.

4. **Asset Tracking:**
   - Track asset movements and changes in status in real-time.
   - Utilize barcode or RFID technology for efficient asset identification and scanning.
   - Generate audit trails and historical logs to trace asset activities and maintain compliance.

5. **Reporting and Analytics:**
   - Generate customizable reports and dashboards to analyze asset-related data.
   - Monitor key performance indicators (KPIs) such as asset utilization, depreciation, and maintenance costs.
   - Gain insights into asset trends and patterns to support informed decision-making.

6. **Integration and Customization:**
   - Integrate with existing IT systems such as ERP, CRM, and ticketing systems for seamless data exchange.
   - Customize fields, workflows, and notifications to align with specific organizational requirements.
   - Support multi-user access with role-based permissions to ensure data security and integrity.

## Getting Started

1. **Installation:**
   - Clone the repository from [GitHub](https://github.com/Pavaneega/asset-management-system).
   - Install the required dependencies by running `pip install -r requirements.txt`.
   - Set up the database by running `flask db upgrade`.
   - Run the Flask application using `flask run`.

2. **Configuration:**
   - Configure database settings, authentication methods, and email notifications in the `config.py` file.
   - Customize asset categories, fields, and workflows in the Flask application according to your organization's requirements.

3. **Usage:**
   - Access the Asset Management System through the web interface by navigating to `http://localhost:5004`.
   - Log in with the default administrator credentials (username: admin, password: admin) to access administrative features.
   - Add new assets, update asset information, and perform asset transactions such as transfers and disposals.
   - Generate reports, analyze data, and leverage system features to optimize asset management processes.

