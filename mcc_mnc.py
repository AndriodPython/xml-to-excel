import xml.etree.ElementTree as ET

def tree():
    tree = ET.parse('vendor.xml')
    root = tree.getroot()
    mcc_mnc_list = []
    for mcc_mnc in root:
        mcc_mnc= str((mcc_mnc.attrib).get('mcc'))+"_"+ str((mcc_mnc.attrib).get('mnc'))
        mcc_mnc_list.append(mcc_mnc)
    print (mcc_mnc_list[1])#none will come means kindly remove those and make count of mcc mnc 
    print (root.find("./carrier_config[@mnc='16'][@mcc='502']/boolean[@name][1]").get('name'))#index need start with 1 
    print (root.find("./carrier_config[@mnc='16'][@mcc='502']/boolean[@value][1]").get('value'))
    print (root.find("./carrier_config[@mnc='16'][@mcc='502']/boolean[@name][2]").get('name'))
    print (root.find("./carrier_config[@mnc='16'][@mcc='502']/boolean[@value][2]").get('value'))
    

#show_vendor()
tree()
'''
mcc_mnc split to @mcc @mnc
volte =cmd1=mcc mnc
if cmd1 == "carrier_volte_available_bool"
 cmd1.get(value)
else:
 print cell NA for VOLTE
vowifi=cmd2 = mcc mnc
if cmd2 =='carrier_wfc_ims_available_bool'
 cmd2.get(value)
else:
 print  Cell NA for VOWIFI
