#to implement em example of the following link: https://www.zhihu.com/question/27976634/answer/39132183

from functools import reduce
import math


INPUT_DATA = [[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]]
EPSILON = 0.002

if __name__ == "__main__":
    print('Begin Training')

    theta_a = 0.60
    theta_b = 0.50
    distribution = []

    for i in range(100):
        #E step
        sample_len = len(INPUT_DATA)
        sum_head_a = 0
        sum_tail_a = 0
        sum_head_b = 0
        sum_tail_b = 0
        for j in range(sample_len):
            x = reduce(lambda x, y: x+y, INPUT_DATA[j], 0)

            prob_a = math.pow(theta_a, x) * math.pow(1-theta_a, 10-x)
            prob_b = math.pow(theta_b, x) * math.pow(1-theta_b, 10-x)

            norm_a = round(prob_a / (prob_a + prob_b), 2)
            norm_b = round(prob_b / (prob_a + prob_b), 2)

            print('Norm a: %f, Norm b: %f' % (norm_a, norm_b))

            head_a = round(norm_a * x, 1)
            tail_a = round(norm_a*(10-x), 1)
            head_b = round(norm_b * x, 1)
            tail_b = round(norm_b*(10-x), 1)

            print('Head a: %f, Tail a:%f, Head b: %f, Tail b: %f' % (head_a, tail_a, head_b, tail_b))

            sum_head_a += head_a
            sum_tail_a += tail_a
            sum_head_b += head_b
            sum_tail_b += tail_b

        print('Sum Head a: %f, Sum Tail a:%f, Sum Head b: %f, Sum Tail b: %f'
              % (sum_head_a, sum_tail_a, sum_head_b, sum_tail_b))

        # M step
        new_theta_a = sum_head_a / (sum_head_a + sum_tail_a)
        new_theta_b = sum_head_b / (sum_head_b + sum_tail_b)

        print('New Theta a: %f, New Theta b: %f' % (new_theta_a, new_theta_b))

        if abs(new_theta_a - theta_a) < EPSILON and abs(new_theta_b - theta_b) < EPSILON:
                print('Done %d: Theta a: %f, New Theta a: %f, Theta b: %f, New Theta b: %f' % (i, theta_a, new_theta_a, theta_b, new_theta_b))
                break

        theta_a = new_theta_a
        theta_b = new_theta_b

    print('Stop Training')



