import ipaddress # https://docs.python.org/3/library/ipaddress.html 
import argparse  # https://docs.python.org/3/library/argparse.html
import texttable # https://pypi.org/project/texttable/

def largest_num(num1, num2):
    if (num1 >= num2):
        return int(num1)
    elif num1 <= num2:
        return int(num2)

if __name__ == "__main__":
    try:
        # argment parser used to handle the inputs given to the script
        parser = argparse.ArgumentParser(description="Prints a table with network information for the given IP address or network. Compatible with IPv4 & IPv6, with or with out CIDR notation.")
        parser.add_argument("ip_str", help="IPv4/IPv6 Address or Network. Can be in CIDR notation.")

        args = parser.parse_args()

        network = ipaddress.ip_network(args.ip_str, strict=False)
        net_version = str(network.version)
        network_ip = str(network.network_address)
        networks = list(network.subnets())
        broadcast = str(network.broadcast_address)
        netmask = str(network.netmask)
        hostmask = str(network.hostmask)
        hosts = list(network.hosts())
        total_hosts = len(hosts)
        total_nets = len(networks)

        table = texttable.Texttable()
        
        column_header = ["Network IP", "Broadcast IP", "Subnet Mask", "Hostmask", "# useable IP's"]
        row = [network_ip, broadcast, netmask, hostmask, "{:,}".format(total_hosts)]
        column_width = []

        for column in column_header:
            column_width.append(largest_num(len(column),
                                len(row[column_header.index(column)])
                                ))

        table.header(column_header)
        table.add_row(row)
        table.set_header_align(["c","c","c","c","c"])
        table.set_cols_align(["c","c","c","c","c"])
        table.set_cols_width(column_width)
        print("\nIP String entered: " + args.ip_str + " - IPv" + net_version + " network")
        print(table.draw())
    except KeyboardInterrupt:
        print("\nExiting")