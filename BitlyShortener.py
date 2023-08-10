import requests

def shorten_url(url, access_token):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'long_url': url
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        short_url = response_data.get('id')
        return short_url
    else:
        return None

# Contoh penggunaan
url = input('Masukkan URL yang ingin dipendekkan: ')
# ganti dengan access token Anda
access_token = 'ganti dengan access token Anda'
print(url)
short_url = shorten_url(url, access_token)
if short_url:
    print(f'Short URL: {short_url}')
else:
    print('Gagal membuat short URL')
