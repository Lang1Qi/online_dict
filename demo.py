def fun():
    while True:
        print("\n==========COMMAND==========")
        print("****       a      ****")
        print("****       b      ****")
        print("===========================")

        cmd = input("Command:")
        if cmd.strip() == "a":
            pass
        elif cmd.strip() == 'b':
            break
        else:
            print("请输入正确命令")

while True:
    print("\n==========COMMAND==========")
    print("****       A      ****")
    print("****       B      ****")
    print("===========================")

    cmd = input("Command:")
    if cmd.strip() == "A":
        pass
        fun()
    elif cmd.strip() == 'B':
        pass
        fun()
    else:
        print("请输入正确命令")
