'''
Shubham Patel (22/02/2020)
Email: srpatel980@gmail.com
Github: github.com/shubham-00
LinkedIn: linkedin.com/in/srpatel980
I would like to join projects, ideas, start-ups.
'''

import random
import math
import matplotlib.pyplot as plt

def main():
    datasize = 10
    data = get_data(datasize)
    X = [i[0] for i in data]
    y = [i[1] for i in data]

    fig_no = 1
    
    for k in range(1, datasize+1):
        centroids = []
        for i in range(k):
            centroids.append([X[i], y[i]])

        for five in range(300):
            group, distance = group_and_distance(datasize, k, X, y, centroids)            
            x_ = [0 for _ in range(len(centroids))]
            y_ = [0 for _ in range(len(centroids))]
            count = [0 for _ in range(len(centroids))]
            
            for centroid in range(len(centroids)):
                for feature in range(datasize):
                    if group[feature] == centroid:
                        x_[centroid] += X[feature]
                        y_[centroid] += y[feature]
                        count[centroid] += 1

            for centroid in range(len(centroids)):
                if count[centroid] != 0:
                    centroids[centroid] = [x_[centroid]/count[centroid], y_[centroid]/count[centroid]]
                    squared_error = get_squared_error(distance)
                    
        print("Classes:", k)
        print("Squared error:", squared_error)

        color = []
        for i in range(datasize):
            if group[i] == 0:
                color.append('#880000')
            elif group[i] == 1:
                color.append('#FF0000')
            elif group[i] == 2:
                color.append('#008800')
            elif group[i] == 3:
                color.append('#00FF00')
            elif group[i] == 4:
                color.append('#000088')
            elif group[i] == 5:
                color.append('#0000FF')
            elif group[i] == 6:
                color.append('#888800')
            elif group[i] == 7:
                color.append('#FFFF00')
            elif group[i] == 8:
                color.append('#008888')
            elif group[i] == 9:
                color.append('#00FFFF')
            else:
                color.append('#880088')

        for i in range(datasize):
            plt.scatter(X[i], y[i], color = color[i])
            
        for i in range(len(centroids)):
            plt.scatter(centroids[i][0], centroids[i][1], color = '#000000', marker='x')
            
        plt.gcf().canvas.set_window_title('Figure ' + str(k))
        plt.title('Number of classes: ' + str(k) + '\n' + 'Squared error: ' + str(squared_error))
        plt.xlabel('X')
        plt.ylabel('y')
        # plt.show()
        plt.savefig("Figure " + str(fig_no))
        fig_no += 1
        plt.clf()

def get_squared_error(distance):
    return sum(distance)

def get_data(datasize):
    data = []
    
    for i in range(datasize):
        a = math.floor(random.random() * datasize)
        b = math.floor(random.random() * datasize)
        data.append([a, b])
    return data

def group_and_distance(datasize, k, X, y, centroids):
    group = []
    distances = []
    
    for feature in range(datasize):
        min_distance = datasize * 100
        min_centroid = 0
        
        for centroid in range(k):
            distance = ( (X[feature] - centroids[centroid][0])**2 + (y[feature] - centroids[centroid][1])**2 ) ** 0.5
            
            if distance < 0:
                distance = -distance
                
            if distance < min_distance:
                min_distance = distance
                min_centroid = centroid
                
        group.append(min_centroid)
        distances.append(min_distance)
    return group, distances

main()

'''
Shubham Patel (22/02/2020)
Email: srpatel980@gmail.com
Github: github.com/shubham-00
LinkedIn: linkedin.com/in/srpatel980
I would like to join projects, ideas, start-ups.
'''
