# coding:UTF-8
import numpy as np
import random

output_array = []


class osGraph:
    col = 1
    row = 1
    current_p = [row, col]
    map_array = None
    count = 1
    prohibited_number = [1]
    existing_pattern = []

    def __init__(self, size):
        self.col = 1
        self.row = 1
        self.current_p = [self.row, self.col]
        self.count = 1
        self.prohibited_number = [1]

        self.map_array = np.array(
            [
                [1 for i in range(size + 2)]
                for j in range(size + 2)]
        )
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                self.map_array[i][j] = 0

        # スタート位置には戻らない
        self.map_array[1][1] = 1
        # print(self.map_array)
        # current_p = self.start_p

    def generate_randInt():
        return random.randint(0, 3)

    def solve_graph(self):
        updated = False
        self.count += 1
        self.prohibited_number.append(self.count)
        around_area = [
            self.map_array
            [self.current_p[0] + 1]
            [self.current_p[1]],
            self.map_array
            [self.current_p[0] -
             1]
            [self.current_p[1]],
            self.map_array
            [self.current_p[0]
             ]
            [self.current_p[1] + 1],
            self.map_array
            [self.current_p[0]]
            [self.current_p[1] - 1]]
        while updated == False:
            # 八方塞がりになったらやり直し
            if 0 not in around_area:
                break

            # 次進む方角を決める乱数の生成
            d_num = osGraph.generate_randInt()
            # print('direction', d_num)
            # print('現在位置', self.current_p)
            if d_num == 0:
                if self.map_array[self.current_p[0] - 1][self.current_p[1]] in self.prohibited_number:
                    continue
                self.current_p[0] -= 1
                updated = True
            elif d_num == 1:
                if self.map_array[self.current_p[0]][self.current_p[1] + 1] in self.prohibited_number:
                    continue
                self.current_p[1] += 1
                updated = True
            elif d_num == 2:
                if self.map_array[self.current_p[0] + 1][self.current_p[1]] in self.prohibited_number:
                    continue
                self.current_p[0] += 1
                updated = True
            elif d_num == 3:
                if self.map_array[self.current_p[0]][self.current_p[1] - 1] in self.prohibited_number:
                    continue
                self.current_p[1] -= 1
                updated = True

        # print('count', self.count)

        # マップの更新
        self.map_array[self.current_p[0]][self.current_p[1]] = self.count

        return self.map_array

    def check_end(self):
        # num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        position = []
        for i in range(len(self.map_array)):
            for j in range(len(self.map_array[i])):
                position.append(self.map_array[i][j])
        # print('position', position)
        if 0 not in position:
            return True
        else:
            return False

    def check_duplication(self, array):
        dup_flag = False
        # print(type(array))
        # print(type(self.existing_pattern[0]))
        for i in range(len(self.existing_pattern)):
            if np.allclose(array, self.existing_pattern[i]) == True:
                dup_flag = True
                break
        if not dup_flag:
            self.existing_pattern.append(array)
            output_array.append(array)

        # print('len(self.existing_pattern)', len(self.existing_pattern))
        # print('output_array', len(output_array))
        return len(self.existing_pattern)


if __name__ == '__main__':
    k = 0
    t = None
    GRAPH_SIZE = 5  # GRAPH_SIZE*GRAPH_SIZEの正方行列を生成
    PATTERN = 5  # 発見したいパターン数を指定
    search_times = 100  # 探索回数

    for i in range(search_times):  # 大きな値を入れておく
        # print('現在', i, '週目')
        g = osGraph(GRAPH_SIZE)
        # if k == 0:
        #     g.existing_pattern.append(t)

        while True:
            # 探索開始
            t = g.solve_graph()

            # 全てのマスを踏んだとき
            if g.check_end():
                if k == 0:
                    g.existing_pattern.append(t)
                    output_array.append(t)
                else:
                    g.check_duplication(t)
                # print(k)
                # print(t, end='\n\n')
                break
            # 解決不可能なとき(全てのマスを踏めなかった時)一度初期化する
            if g.count > GRAPH_SIZE * GRAPH_SIZE:
                g.__init__(GRAPH_SIZE)
                continue

        # 任意のパターン数発見したら処理を抜ける
        # if g.check_duplication(t) > PATTERN:
        #     break
        k += 1

    print(search_times, '回探索した時点で', len(g.existing_pattern), '通り見つかりました')
    # 見つけたパターンを出力する
    for i in range(len(output_array)):
        if i >= PATTERN:
            break
        print(i + 1, '通り目')
        print(output_array[i])

        # k = 0
        # output_array.clear()
        # print('*' * 100)
