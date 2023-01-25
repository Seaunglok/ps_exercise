T = int(input())
for test_case in range(1, T + 1):
    box_num = int(input())
    boxs = []
    for i in range(box_num):
        box = list(map(int, input().split()))
        boxs.append([box[0], box[1], box[2], i])
        boxs.append([box[1], box[2], box[0], i])
        boxs.append([box[2], box[0], box[1], i])
 
    boxs = sorted(boxs, key=lambda x: x[0] * x[1])
 
    db = [box[2] for box in boxs]
    db_list = [[boxs[i][3]] for i in range(box_num * 3)]
 
    for i in range(box_num * 3):
        for j in range(i, -1, -1):
            if i == j:
                continue
            if boxs[i][3] in db_list[j]:
                continue
            if (boxs[i][0] >= boxs[j][0] and boxs[i][1] >= boxs[j][1]) or (
                    boxs[i][0] >= boxs[j][1] and boxs[i][1] >= boxs[j][0]):
                if db[j] + boxs[i][2] > db[i]:
                    db[i] = db[j] + boxs[i][2]
                    db_list[i] = db_list[j] + [boxs[i][3]]
    print("#" + str(test_case) + " " + str(max(db)))