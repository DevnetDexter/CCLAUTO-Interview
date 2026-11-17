import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("mask")
args = parser.parse_args()
api = "https://networkcalc.com/api/ip"
subnet = "172.16.0.0"
mask = args.mask

def api_call():
    url = f"{api}/{subnet}/{mask}"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()["address"]

def assignable_hosts(hosts, cidr):
    print("There are",hosts,"assignable hosts for the",cidr,"subnet")

def first_host(first_ip):
    print("The first address is",first_ip)

def mask_decimal(subnet_mask):
    print("The subnet mask in decimal form is", subnet_mask)

def mask_cidr(subnet_bits):
    subnet_bits = str(subnet_bits)
    mask_cidr = "/"+subnet_bits
    print("The subnet mask in cidr notation is", mask_cidr)

if __name__ == '__main__':
    address = api_call()
    assignable_hosts(address["assignable_hosts"], address["cidr_notation"])
    first_host(address["first_assignable_host"])
    mask_decimal(address["subnet_mask"])
    mask_cidr(address["subnet_bits"])
