from BFPCode.BF import bfc

if __name__ == "__main__":
    c = [0 for i in range(128)]
    p = 0
    while True:
        code = input("BF> ")
        if code == "exit":
            break
        if code == "reset":
            c = bfc(code)
        if code == "print":
            print(c)
        if code == "help":
            print("""
exit    退出
reset   重置缓存
print   打印缓存
help    帮助""")
        c,p = bfc(code, c, p)