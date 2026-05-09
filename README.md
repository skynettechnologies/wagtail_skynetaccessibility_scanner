# SkynetAccessibility Scanner

## Overview

SkynetAccessibility Scanner is a powerful Wagtail accessibility testing and scanning module designed to help organizations identify, monitor, and fix accessibility issues across their websites. It enables businesses, agencies, and government organizations to maintain compliance with global accessibility standards while improving user experience for all visitors.

Built for Wagtail 4.0 and above (Python 3.10+, Django 4.0–6.x), this module provides automated scanning, detailed reporting, and continuous monitoring - making accessibility management simple and scalable.

[**Start 10-Days Free Trial!**](https://skynetaccessibilityscan.com/trial-subscription)

## Why use Automated Wagtail accessibility monitoring plugin - SkynetAccessibility Scanner?

Accessibility is not a one-time task. With evolving standards and legal requirements, websites require continuous monitoring and improvements. This module helps you:

- Detect accessibility issues automatically
- Track compliance across multiple pages
- Prioritize fixes with actionable recommendations
- Maintain long-term accessibility compliance

It acts as both an accessibility checker and compliance testing tool, helping teams proactively manage accessibility risks.

## Features

- Automated Accessibility Scanning.
- Detailed Automated generated reports with severity levels, issues descriptions, and clear remediation guidance.
- Sitemap-Based Scanning and Monitoring
- Multi Resolution Monitoring
- Set up weekly, monthly, or quarterly scheduled ongoing accessibility compliance monitoring
- Supports scanning in 190+ languages, making it ideal for global websites.
- Seamlessly integrates with the All in One Accessibility dashboard for centralized management.

### Supported Global Accessibility Compliance Standards

- WCAG 2.0, 2.1, 2.2
- ADA
- Section 508
- EAA EN 301 549 (EU)
- UK Equality Act
- Australian DDA
- Canada ACA
- Ontario AODA
- California Unruh
- Israeli Standard 5568
- Germany BITV 2.0
- France RGAA
- Spain UNE 139803
- Italy Stanca Act
- Indian RPD Act
- GIGW 3.0
- Brazilian Inclusion law LBI 13.146/2015
- Japan JIS X 8341

### Key Benefits for Wagtail Users

- Works directly within the Wagtail ecosystem
- Reduces manual accessibility testing efforts
- Helps improve user experience for people with disabilities
- Supports legal and compliance requirements
- Scales across multiple Wagtail websites and projects

Explore the full capabilities of the accessibility monitoring Wagtail module. Flexible plans allow to evaluate website accessibility requirements.

### Pricing

- 10 Days free trial

#### Single Site

- Small Site (Up to 25 pages): $9 Per Month
- Medium Site (Up to 250 pages): $19 per month
- Large Site (Up to 1000 pages): $89 per month
- Extra Large Site (Up to 2500 pages): $199 per month

#### Multi-site

- Silver (3 websites up to 1500 pages): $129 per month
- Gold (5 websites up to 2500 pages): $219 per month
- Platinum (10 websites up to 5000 pages): $399 per month

### Paid Add-ons

- Manual Accessibility Audit Report
- Manual Accessibility Remediation
- PDF/Document Accessibility Remediation
- VPAT Report/Accessibility Conformance Report (ACR)

## How does Wagtail accessibility scanning and monitoring work?

- **Scan Your Website** – Run automated scans to detect accessibility issues with our Accessibility Testing Tool.
- **Review Reports** – Access prioritized issue lists with remediation recommendations.
- **Monitor & Maintain** – Keep your website accessible with ongoing monitoring using the Accessibility Scanning Monitoring Application.

## Getting Started with SkynetAccessibility Scanner

- Visit [WCAG Accessibility Scanning and Monitoring](https://www.skynettechnologies.com/accessibility-scanning-and-monitoring)
- Request a demo or [sign up for a free trial](https://skynetaccessibilityscan.com/trial-subscription) to explore accessibility scanning features.
- Configure website domains and customize accessibility scan settings.
- Start monitoring WCAG compliance, track accessibility issues, and download detailed audit report.

## Installation

### Prerequisites

- **Python Version:** 3.10 or higher
- **Django Version:** 4.0 – 6.x
- **Wagtail Version:** 4.0 or higher

### Compatibility

#### Version Support

![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)
![Django](https://img.shields.io/badge/django-4.0%20%7C%204.1%20%7C%204.2%20%7C%205.0%20%7C%205.1%20%7C%205.2-blue)
![Wagtail](https://img.shields.io/badge/wagtail-4.x%20%7C%205.x%20%7C%206.x-blue)

### Steps

To install the plugin, follow these instructions.

## Using pip (Recommended)

### Requirements

Must have Python and pip installed, and your Wagtail project set up.

1. Open your terminal and go to your Wagtail project:

   ```bash
   cd /path/to/project
   ```

2. Activate your Python virtual environment:

   **On Linux / macOS:**
   ```bash
   source venv/bin/activate
   ```

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   > You should see your terminal prompt change to show the virtual environment name (e.g. `(venv)`). All pip commands must be run inside this activated environment so Wagtail can find the installed package.

3. Install the plugin using pip:

   ```bash
   pip install wagtail_skynetaccessibility_scanner
   ```

4. Add to `INSTALLED_APPS` in your `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ... your existing apps ...
       'wagtail_skynetaccessibility_scanner',
   ]
   ```

5. Add the context processor to `TEMPLATES` in your `settings.py`:

   ```python
   TEMPLATES = [
       {
           # ...
           'OPTIONS': {
               'context_processors': [
                   # ... your existing context processors ...
                   'wagtail_skynetaccessibility_scanner.context_processors.skynet_scanner',
               ],
           },
       },
   ]
   ```

   > This context processor makes your site's domain URL available to the scanner's templates. It is required for the scanner dashboard to function correctly.

6. Add to `urls.py`:

   ```python
   from django.urls import path, include

   urlpatterns = [
       # ... your existing URLs ...
       path('skynet/', include('wagtail_skynetaccessibility_scanner.urls',
                                namespace='wagtail_skynetaccessibility_scanner')),
   ]
   ```

7. Run migrations:

   ```bash
   python manage.py migrate
   ```

8. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

9. Restart your server:

   ```bash
   python manage.py runserver
   ```

10. In the Wagtail Admin, go to **SkynetAccessibility Scanner** in the left sidebar menu.

## Using Download ZIP

1. Download the `.whl` or ZIP file from the repository.

2. Activate your Python virtual environment:

   **On Linux / macOS:**
   ```bash
   source venv/bin/activate
   ```

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

3. Install from the `.whl` file:

   ```bash
   pip install wagtail_skynetaccessibility_scanner-1.0.1-py3-none-any.whl
   ```

4. Follow steps 4–10 from the pip installation above to complete setup.

## Activation and Deactivation

**To activate:** Follow the installation steps above. After running migrations, a default settings record is created automatically — no manual configuration is needed to get started.

**To deactivate:**

1. Remove `'wagtail_skynetaccessibility_scanner'` from `INSTALLED_APPS` in `settings.py`.
2. Remove the context processor entry from `TEMPLATES` in `settings.py`.
3. Remove the `skynet/` URL entry from `urls.py`.
4. Re-run migrations:

   ```bash
   python manage.py migrate
   ```

## CORS Policy Configuration

To avoid CORS policy issues, ensure the following domain is allowed in your server's CORS configuration or trusted origins list.

| **Domain**                            | **Description**                           | **Usage**                |
|---------------------------------------|-------------------------------------------|--------------------------|
| `https://skynetaccessibilityscan.com` | Skynet Accessibility Scan (Global Domain) | API access and resources |

If you are using [`django-cors-headers`](https://pypi.org/project/django-cors-headers/), add the following to `settings.py`:

```python
CORS_ALLOWED_ORIGINS = [
    # ... your existing origins ...
    "https://skynetaccessibilityscan.com",
]
```

**Additional instructions:**

1. Update your server's CORS configuration to include the domain above.
2. Ensure wildcard subdomains (`*`) are supported where necessary.
3. Verify the application functionality by testing requests to these domains.
4. If issues persist, consult the documentation for CORS configuration guidance.

## Screenshots

![SkynetAccessibility_Scanner_Image_1](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_1.jpg)
![SkynetAccessibility_Scanner_Image_2](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_2.jpg)
![SkynetAccessibility_Scanner_Image_3](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_3.jpg)
![SkynetAccessibility_Scanner_Image_4](https://www.skynettechnologies.com/sites/default/files/SkynetAccessibilityScanner/SkynetAccessibility_Scanner_Image_4.jpg)

## Video

[![SkynetAccessibility Scanner](https://img.youtube.com/vi/g0RNlTOQImY/0.jpg)](https://www.youtube.com/watch?v=g0RNlTOQImY)

## Submit a Support Request

Please visit our **[support page](https://www.skynettechnologies.com/report-accessibility-problem)** and fill out the form. Our team will get back to you as soon as possible.

## Send Us an Email

Alternatively, you can send an email to our support team:  
**[hello@skynettechnologies.com](mailto:hello@skynettechnologies.com)**

## Accessibility Partnership Opportunities

### **[Accessibility Agency Partnership](https://www.skynettechnologies.com/agency-partners)**

Partner with us as an agency to provide comprehensive accessibility solutions to your existing clients. Get access to exclusive resources, training, and support to help you implement and manage accessibility features effectively.

### **[Accessibility Affiliate Partnership](https://www.skynettechnologies.com/affiliate-partner)**

Join our affiliate program and earn hefty commissions by promoting SkynetAccessibility Scanner. Share our accessibility solution within your network and help businesses improve their website accessibility while generating additional revenue.

For more details, please visit **[Accessibility Partnership Opportunities Page](https://www.skynettechnologies.com/partner-program)**.

## Credits

This **Accessibility Scanning Monitoring Application** is developed and maintained by **[Skynet Technologies USA LLC](https://www.skynettechnologies.com)**