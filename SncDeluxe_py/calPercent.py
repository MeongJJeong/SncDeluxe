import os

def calRate(this , point):
    result = this / int(problem) * 100
    return round(result,point)

# def show():
#     print("------결과------")
#     for x in range(int(problem)):
#         print('%d%s' % (x + 1, "번"), end=" ")
#
#         for y in range(int(examples)):
#             print('%d%s%d%s' % (y + 1, ": ", array[x][y + 1], "개("), end=" ")
#             print('%6.2f%s' % (calRate(array[x][y + 1]), "%)"), end=" ")
#         print()
#
#     print('%s%d%s'%("무효표 ",abnormal,"개 나옴."))
#     return

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

    # x = 0
    # right = True
    # while x < int(people):
    #     if not right:
    #         x - 1
    #         right = True
    #     print('%s %d%s'%("======",x+1,"번째 입력"))
    #     print("**",end="")
    #     for k in range(int(problem)):
    #         print("*",end = "")
    #     print()
    #     result = input(">>")
    #
    #     if int(result) == 0:
    #         abnormal = abnormal + 1
    #         print('%s%d%s'%("무효 설문지가 ",abnormal,"개 입력되었습니다."))
    #         people = int(people) - 1
    #         continue
    #     elif result == "a":
    #         print(result)
    #
    #     elif len(result) != int(problem):
    #         print("덜이나 더 입력됐어용 > ")
    #     else:
    #         for y in range(int(problem)):
    #             if int(result[y]) > int(examples) or int(result[y]) < int(0):
    #                 print("잘못 입력했습니다.")
    #                 right = False
    #
    #         if right:
    #             for y in range(int(problem)):
    #                 array[y][int(result[y])] = array[y][int(result[y])] + 1

            # if right:
            #     for y in range(int(problem)):
            #         array[y][result[y]] = array[y][result[y]] + 1


    #             x = x + 1
    #         else:
    #             pass
    #
    # print()
    # show()
    print()
    os.system("pause")