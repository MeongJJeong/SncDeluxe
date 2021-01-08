import os

def calRate(this , point):
    result = this / int(problem) * 100
    return round(result,point)


if __name__ == '__main__':

    problem = input("총갯수 => ")
    point = int(input("소수점 => "))


    while True:
        x = input(">>")
        if x == "k":
            break
        elif x == "s":
            print("Settings")
        else:
            print(calRate(int(x),point),end=" ")
        print()

    print("끝!!!")


    print()
    os.system("pause")