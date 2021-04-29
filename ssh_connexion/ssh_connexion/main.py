import getpass
from netmiko import ConnectHandler

def ssh_connexion(host_ip, username, password):
    equipment = {
        'device_type': 'nokia_sros',
        'host': host_ip,
        'username': username,
        'password': password,
    }
    return equipment

def send_command(equipment,command):
    net_connect = ConnectHandler(**equipment)
    output = net_connect.send_command(command)
    print(output)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host_ip = input("Enter ssh ip : ")
    username = input("Enter username : ")
    password = getpass.getpass()
    command = input("Enter command")

    # SSH CONNEXION
    equipment = ssh_connexion(host_ip,username,password)

    # SENDING COMMAND
    send_command(equipment, command)