#!/usr/bin/python
import sys,commands 
n=sys.argv[1]
vm_install='sudo virt-install --ram 512 --vcpu 1 --disk path=/var/lib/libvirt/images/dnimg'+n+'.qcow2 --import --name dn'+n
print vm_install
result_install=commands.getstatusoutput(vm_install+' --noautoconsole')
print result_install 
