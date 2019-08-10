import os
import re
import requests
import sys


def query_org_name(mac_addr, api_key):
    url = "https://api.macaddress.io/v1"

    headers = {
        'X-Authentication-Token': api_key
    }
    payload = {
        'output': 'json',
        'search': mac_addr
    }
    r = requests.get(url, headers=headers, params=payload)
    return r.json()['vendorDetails']['companyName']


def verify_mac(mac_addr):
    mac_pattern = re.compile('([0-9a-fA-F]{2}[:]){5}[0-9a-fA-F]{2}')

    # bit zero of first octet must be zero
    if int(mac_addr[:2], 16) % 2 != 0:
        return False

    if re.match(mac_pattern, mac_addr):
        return True

    return False


def main(args = sys.argv[1:]):
    if len(args) != 1:
        sys.exit('One and only one argument should be provided')

    api_key = os.getenv('API_KEY')
    if not api_key:
        sys.exit('You must provide a macaddress.io API key')

    mac = args[0]
    if not verify_mac(mac):
        sys.exit('Invalid mac address: {}'.format(mac))

    print(query_org_name(mac, api_key))


if __name__ == '__main__':
    main()