# HTTP Security Header Checker

A Python script designed for Red Team assessments and IT support audits to quickly identify missing HTTP security headers on a web server.

## Why this matters?
Missing security headers (like CSP, HSTS, or X-Frame-Options) can lead to Cross-Site Scripting (XSS), Clickjacking, and Man-in-the-Middle (MitM) attacks. This script helps administrators and penetration testers quickly audit a web server's configuration.

## Usage
`python header_checker.py <target_url>`

*Disclaimer: This tool is for authorized testing and educational purposes only.*
