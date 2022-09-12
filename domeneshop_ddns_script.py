# Script to update domeneshop DNS records

from domeneshop import Client
import urllib.request

def main():
    # Create a client object with your API token
    client = Client('token', 'secret_key')
    # Get the current external IP address
    external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
    
    # Create the data for the record
    record = {
    "host": "@",
    "ttl": 3600,
    "type": "A",
    "data": f'{external_ip}'
    }

    # Update the record
    client.modify_record(1550173, 4932199, record)

    # Create the data for the record
    record = {
    "host": "www",
    "ttl": 3600,
    "type": "A",
    "data": f'{external_ip}'
    }
    
    # Update the record
    client.modify_record(1550173, 4932200, record)


if __name__ == "__main__":
    main()
    exit(0)