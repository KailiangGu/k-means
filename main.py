import random
import math
import numpy as np


# 聚类
def clustering(data, S):
    cluster = []
    # 计算每个点与质点的距离
    for point in data:
        distances = []
        for s in S:
            distances.append(distance(point,s))

        # 找出最近的距离，这个距离的index就对应了这个点属于的类别
        min_index = distances.index(min(distances))
        cluster.append(min_index)

    return cluster


# 更新质点
def updated_S(cluster, data, S, k):
    # 创建distances空集，还有记数counts空集
    m = data[0].shape
    distances = [np.zeros(m)] * k
    counts = [0] * k

    # 对于每个点，计算其与其质点的各纬度距离，然后加入到这个质点所属的distance集里
    for i in range(len(cluster)):
        group = cluster[i]
        distances[group] += S[group] - data[i]
        counts[group] += 1

    # 平均，得出质点应该移动的距离
    S_new = np.true_divide(distances, counts)
    # 更新质点
    S = S + S_new

    return S


def distance(p1,p2):
    #计算欧几里得距离
    return np.sqrt(np.sum(np.power((p1+p2),2)))
    #return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)



def main():
    data = []
    # 设定k值
    k = 3

    # 随机生成数据点
    for _ in range(100):
        data.append(np.array([random.randint(0,100),random.randint(0,100)]))

    # 随机设定最初质点并记录质点index
    S_index = [random.randint(0,99)]
    S = [data[S_index[0]]]


    # 增加k-1个质地点
    for _ in range(k-1):
        max_distance = 0
        max_index = 0

        for i in range(len(data)):
            #找出当前点与所有质点的最大距离D
            if i not in S_index:
                max_k_distance = 0
                max_k_index = 0
                for s in S:
                    local_distance = distance(s, data[k])
                    if local_distance > max_k_distance:
                        max_k_index = i
                        max_k_distance = local_distance

                #找出所有点中与某个质点有最大D的点作为新的质点
                if max_k_distance > max_distance:
                    max_distance = max_k_distance
                    max_index = max_k_index

        S.append(data[max_index])
        S_index.append(max_index)


    # 一直聚类，知道无质点更新
    S_new = S
    cluster = None

    while S_new == S:
        S = S_new
        cluster = clustering(data, S)
        S_new = updated_S(cluster, data, S_new, k)

    return cluster



if __name__ == '__main__':
    main()