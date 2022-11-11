import os
import socket
from requests import get

from shodan import Shodan
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api = Shodan(os.environ['TOKEN_SHODAN'])


def get_ip_info(ip: str):
    host = api.host(ip)
    print("""
            IP: {}
            Organization: {}
            Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    # Print all banners
    for item in host['data']:
        print("""
                    Port: {}
                    Banner: {}
    
            """.format(item['port'], item['data']))


if __name__ == '__main__':
    get_ip_info('87.250.250.242')
