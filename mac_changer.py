#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



# interface = raw_input("interface > ") #input for Python3
# new_mac = raw_input("new Mac > ")
# interface = options.interface
# new_mac = options.new_mac

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)