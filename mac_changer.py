import subprocess
import optparse

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interace to change it's MAC Address")
    parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC Address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")

    elif not options.new_MAC:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")

    return options

def change_MAC(interface, new_MAC):

    print("[-] Changing MAC Address for " + interface + " to " + new_MAC)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_MAC(options.interface, options.new_MAC)
