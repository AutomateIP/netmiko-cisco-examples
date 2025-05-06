from netmiko import Netmiko

devices = [
{
    "device_type": "cisco_xe",
    "ip": "10.1.8.97",
    "username": "itential",
    "password": "itential",
    "port": "22",
}]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show interfaces")
    net_connect.disconnect()
    print (output)
