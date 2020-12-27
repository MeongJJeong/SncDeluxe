import os


def calRate(this):
    result = this / int(people) * 100
    return result


def show():
    print("------결과------")
    for x in range(int(problem)):
        print('%d%s' % (x + 1, "번"), end=" ")

        for y in range(int(examples)):
            print('%d%s%d%s' % (y + 1, ": ", array[x][y + 1], "개("), end=" ")
            print('%6.2f%s' % (calRate(array[x][y + 1]), "%)"), end=" ")
        print()

    print('%s%d%s'%("무효표 ",abnormal,"개 나옴."))
    return


def snap():
    print("=================================================")
    print("VVsncVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    print("=================================================")
    print("+ 사용법")
    print("+ 총 문제 갯수와 선택 가능한 보기 갯수 입력")
    print("+ 선택한 숫자를 차례로 입력")
    print("+ ex) 12334 + enter")
    print("+ 보기 항목에 없는 값이나 문제보다 더 많은 값 입력시 재입력")
    print("+ 무효표가 있을 경울 0을 입력하면 무효표 추가 가능")
    print("=================================================")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("==========================================v0.1===")
    print()


if __name__ == '__main__':

    array = []
    ques_dic = {}

    snap()

    problem = input("문제 갯수 => ")
    examples = input("보기 갯수 => ")
    people = input("참여 인원 => ")
    abnormal = 0

    for x in range(int(problem)):
        array.append({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, "k": 0})

    x = 0
    right = True
    while x < int(people):
        if not right:
            x - 1
            right = True
        print('%s %d%s'%("======",x+1,"번째 입력"))
        print("**",end="")
        for k in range(int(problem)):
            print("*",end = "")
        print()
        result = input(">>")

        if int(result) == 0:
            abnormal = abnormal + 1
            print('%s%d%s'%("무효 설문지가 ",abnormal,"개 입력되었습니다."))
            people = int(people) - 1
            continue
        elif result == "a":
            print(result)

        elif len(result) != int(problem):
            print("덜이나 더 입력됐어용 > ")
        else:
            for y in range(int(problem)):
                if int(result[y]) > int(examples) or int(result[y]) < int(0):
                    print("잘못 입력했습니다.")
                    right = False

            if right:
                for y in range(int(problem)):
                    array[y][int(result[y])] = array[y][int(result[y])] + 1

            # if right:
            #     for y in range(int(problem)):
            #         array[y][result[y]] = array[y][result[y]] + 1


                x = x + 1
            else:
                pass

    print()
    show()
    print()
    os.system("pause")

    #
    # for x in range(len(all)):
    #     print(all[x])
    #
    # for x in range(int(all)):
    #     result = result+x
