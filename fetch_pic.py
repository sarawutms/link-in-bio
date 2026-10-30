import urllib.request
import re

url = 'https://www.instagram.com/kadashilab/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'\"avatarLarger\":\"(.*?)\"', html)
    
    if not match:
        match = re.search(r'property=\"og:image\" content=\"(.*?)\"', html)
        
    if match:
        img_url = match.group(1).replace('\\u002F', '/').replace('&amp;', '&')
        print('Found Image URL:', img_url)
        
        req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_img) as response, open('profile.jpg', 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            
        print('Saved as profile.jpg')
    else:
        print('Image not found.')
except Exception as e:
    print('Error:', e)
