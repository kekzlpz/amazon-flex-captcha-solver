# amazon-flex-captcha-solver
Solve amazon flex captcha with python / nodejs

# Site key of amazon flex captcha
This is the site key used for the captcha of amazon.
2F1CD804-FE45-F12B-9723-240962EBA6F8

# Requeriments
- Scrape correct data[blob] value, where to find this value? In the request https://www.amazon.[yourdomain, ex: .es , .it, .com]/aaut/verify/flex-offers/challenge?challengeType=ARKOSE_LEVEL_2&returnTo=https://www.amazon.com&headerFooter=false , check the response for https://iframe.arkoselabs.com/2F1CD804-FE45-F12B-9723-240962EBA6F8/index.html?data=THIS GET and get this data, everytime is new one.

- [Capsolver.com](https://www.capsolver.com/) API Key
