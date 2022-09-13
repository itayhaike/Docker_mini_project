#lists
my_list=["itayhaike" , 21 , "itay@gmail.com" , 544396123]
print("my name is: " + my_list[0] + "\nmy age is: " + str(my_list[1]) + "\nmy email is: " + my_list[2] + "\nmy phone is: " + str(my_list[3]))

ip_list=["192.168.1.1" , "155.155.10.254"]
print(ip_list)
ip_list.append("166.155.8.255")
ip_list.append("144.166.18.254")
ip_list.append("255.255.255.255")
ip_list.pop(2)
print(" how meny ips i have : " + str(len(ip_list)) + "\nmy finel list is: " + str(ip_list))
