# SkynetAccessibility Scanner

## Overview

SkynetAccessibility Scanner is a powerful Wagtail accessibility testing and scanning module designed to help organizations identify, monitor, and fix accessibility issues across their websites. It enables businesses, agencies, and government organizations to maintain compliance with global accessibility standards while improving user experience for all visitors.

Built for Wagtail, this module provides automated scanning, detailed reporting, and continuous monitoring - making accessibility management simple and scalable.

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

Explore the full capabilities of the accessibility monitoring Wagtail module. Flexible plans allow you to evaluate website accessibility requirements.

### Pricing

- 10 Days free trial

#### Single Site

- Small Site (Up to 25 pages): $9 per month
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
- Configure your website domain from the scanner dashboard.
- Start monitoring WCAG compliance, track accessibility issues, and download detailed audit reports.

### Prerequisites

- **Python:** 3.10 or higher
- **Django:** 4.0 or higher
- **Wagtail:** 4.0 or higher

## Installation

1. Install the plugin:

   ```bash
   pip install wagtail_skynetaccessibility_scanner
   ```

2. Add it to `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       # ... your existing apps ...
       'wagtail_skynetaccessibility_scanner',
   ]
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

That's it. Once migrations complete, a default settings record is created automatically and **SkynetAccessibility Scanner** appears in the Wagtail Admin sidebar — no manual configuration needed to get started.

> **No URL or template configuration needed.** The module registers its own admin page automatically through Wagtail's hook system as soon as it's in `INSTALLED_APPS` — do **not** add a route for it in your project's `urls.py`. Adding one manually creates a duplicate, unauthenticated copy of the dashboard outside Wagtail's admin login wall and can break the sidebar link. Likewise, no `context_processors` entry is required.

**To deactivate:** remove `'wagtail_skynetaccessibility_scanner'` from `INSTALLED_APPS` and re-run `python manage.py migrate`.

## Configuration

After installation, open the Wagtail Admin sidebar and select **SkynetAccessibility Scanner** to set up your domain and scan preferences from the dashboard.

## CORS Policy Configuration

To avoid CORS policy issues, ensure the following URL is allowed in your website's CORS configuration or trusted domains list.

| **Domain**                            | **Description**                           | **Usage**                 |
|----------------------------------------|--------------------------------------------|----------------------------|
| `https://skynetaccessibilityscan.com`  | Skynet Accessibility Scan (Global Domain)  | API access and resources  |

If you use [`django-cors-headers`](https://pypi.org/project/django-cors-headers/), add:

```python
CORS_ALLOWED_ORIGINS = [
    # ... your existing origins ...
    "https://skynetaccessibilityscan.com",
]
```

### Instructions

1. Update your server's CORS configuration to include this domain.
2. Ensure wildcard subdomains (`*`) are supported where necessary.
3. Verify the application functionality by testing requests to this domain.
4. If issues persist, consult the documentation for CORS configuration guidance.

## Known Issues / Before You Deploy

- **Static asset paths on non-default storage:** the scanner's plan-tier icons are served from a hardcoded `/static/...` path and can fail to load (404) on sites that serve static files from S3, a CDN, or any `STATIC_URL` other than Django's default `/static/`. If your icons don't appear, check your browser console for 404s on `img/assets/*.svg` and verify your static file routing.
- Do not manually add a `urls.py` route or a `TEMPLATES` context processor entry for this app — see the note under Installation above.

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