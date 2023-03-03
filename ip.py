import socket
import requests
import script

url = 'home.jnsfullstack.com'
old_ip = socket.gethostbyname(url)
print(f"The IP address for {url} is {old_ip}")



response = requests.get('https://httpbin.org/ip')
new_ip = response.json()['origin']
print("My public IP address is:", new_ip)

if old_ip != new_ip:
    script.update_ip(new_ip)
    print("Updated home.jnsfullstack.com to ", new_ip)

