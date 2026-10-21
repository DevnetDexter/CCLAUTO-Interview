import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("subnet")
parser.add_argument("mask")

args = parser.parse_args()

api = "https://networkcalc.com/api/ip"

subnet = args.subnet
mask = args.mask


def api_call():

    url = f"{api}/{subnet}/{mask}"

    data = requests.get(url).json()

    global hosts
    global first_ip
    global subnet_mask
    global subnet_bits
    global cidr

    hosts = data["address"]["host_count_v4"]
    first_ip = data["address"]["first_host"]
    subnet_mask = data["address"]["netmask"]
    subnet_bits = data["address"]["cidr"]
    cidr = f"{subnet}/{subnet_bits}"


def assignable_hosts(hosts, cidr):
    print(
        f"There are {hosts} assignable hosts for the {cidr} subnet"
    )


def first_host(first_ip):
    print(f"The first address is {first_ip}")


def mask_decimal(subnet_mask):
    print(
        f"The subnet mask in decimal form is {subnet_mask}"
    )


def mask_cidr(subnet_bits):
    print(
        f"The subnet mask in cidr notation is /{subnet_bits}"
    )


if __name__ == "__main__":
    api_call()
    assignable_hosts(hosts, cidr)
    first_host(first_ip)
    mask_decimal(subnet_mask)
    mask_cidr(subnet_bits)
