
import capsolver
import requests

# Consider using environment variables for sensitive information
## Key from https://capsolver.com

capsolver.api_key = "capsolver.com api key"
PAGE_URL = "https://iframe.arkoselabs.com"
PAGE_KEY = "2F1CD804-FE45-F12B-9723-240962EBA6F8"

def solver_funcaptcha(url,key, data):
    solution = capsolver.solve({
        "type": "FunCaptchaTaskProxyless",
        "websiteURL": url,
        "websitePublicKey":key,
      "data":"{\"blob\": \"flaR60YY3tnRXv6w.l32U2KgdgEUCbyoSPI4jOxU...\"}"}'
    })
    return solution

def set_session_headers(session, user_agent=None):
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "upgrade-insecure-requests": "1",
        "user-agent": user_agent if user_agent else "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7"
    }
    session.headers.update(headers)

def main():
    s = requests.Session()
    
    print("Solving Funcaptcha...")
  data  = ""
    solution = solver_funcaptcha(PAGE_URL, PAGE_KEY, data)
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
