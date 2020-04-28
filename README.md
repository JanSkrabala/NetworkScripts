# NetworkScripts

Colection of simple python scripts for remote management of multiple devices.

NapalmMultipleDevices - Configuration push configuration to multiple devices using Napalm. Utilizing list to loop through devices

NetmikoMultipleDevices - Configuration push configuration to multiple devices using Netmiko.Utilizing list to loop through devices

ldapAdGroupUserAdd - Remote Ldap3 script to check if the user is in Windows Active Directory group, if not adds user in to group. 
                     Utilizing list to loop through users.
                     
LinuxDNSChange - Uses Netmiko to connect and loop through linux OS devices read contains of /etc/resolf.conf and if entry is
                 diferent than the desired DNS server, change the entry. Utilizing list to loop through devices

