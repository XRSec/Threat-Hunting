#!/usr/bin/env python3

import re


def de_weight(file_data):
    print("Start")
    lists = []
    for i in file_data:
        if re.match(r'^10\.', i.strip()) or re.match(r'^192\.168\.', i.strip()) or re.match(r'^172\.',
                                                                                            i.strip()) or i == '\n':
            print("delete", i.strip())
        else:
            lists.append(i.strip() + "\n")
    return lists


def main():
    ip_data = open("ip.txt")
    x_data = open("x.txt")
    ip_resut = de_weight(ip_data)
    x_resut = de_weight(x_data)
    hack_ip = list(set(ip_resut) & set(x_resut))
    with open("hack.txt", "w") as f:
        f.writelines(hack_ip)
    f.close()
    ip_data.close()
    x_data.close()


main()
