import requests
import sys

# Suppress harmless SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_headers(url):
    if not url.startswith('http'):
        url = 'http://' + url

    print(f"[*] Checking security headers for: {url}\n")
    
    try:
        response = requests.get(url, timeout=5, verify=False)
        headers = response.headers
        
        # List of important security headers
        security_headers = {
            "Strict-Transport-Security": "Enforces HTTPS connections (HSTS).",
            "Content-Security-Policy": "Prevents XSS and data injection attacks (CSP).",
            "X-Frame-Options": "Protects against Clickjacking attacks.",
            "X-Content-Type-Options": "Prevents MIME-sniffing vulnerabilities.",
            "Referrer-Policy": "Controls how much referrer information is sent.",
            "Permissions-Policy": "Controls which browser features can be used."
        }

        for header, description in security_headers.items():
            if header in headers:
                print(f"[+] {header}: FOUND - {headers[header]}")
            else:
                print(f"[-] {header}: MISSING - {description}")
                
    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python header_checker.py <target_url>")
        print("Example: python header_checker.py google.com")
        sys.exit(1)
        
    check_headers(sys.argv[1])
