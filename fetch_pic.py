import urllib.request
import re
import html

url = 'https://www.instagram.com/kadashilab/'
# Instagram returns Open Graph tags to social bot crawlers
req = urllib.request.Request(url, headers={'User-Agent': 'facebookexternalhit/1.1'})

try:
    page_html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    match = re.search(r'property="og:image"\s+content="([^"]+)"', page_html)
    
    if not match:
        match = re.search(r'content="([^"]+)"\s+property="og:image"', page_html)
        
    if match:
        img_url = html.unescape(match.group(1))
        print('Found Image URL:', img_url)
        
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response, open('profile.jpg', 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            
        print('Successfully saved as profile.jpg (size:', len(data), 'bytes)')
    else:
        print('Image not found in page HTML.')
except Exception as e:
    print('Error:', e)
