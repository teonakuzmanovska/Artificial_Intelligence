import csv
from sklearn.preprocessing import OrdinalEncoder
import math
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    with open("cars.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # for row in csv_reader:
        #     print(row)

        dataset = list(csv_reader)[1:]  # za da ja nemame prvata redica e [1:]
        # print(dataset)

        encoder = OrdinalEncoder()
        # encoder.fit(dataset)
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])
        # dataset = encoder.transform(dataset)

        train_set = dataset[0:math.ceil(0.7 * len(dataset))]
        test_set = dataset[math.ceil(0.7 * len(dataset)):]

        X = [train_set[i][:-1] for i in range(len(train_set))]
        X = encoder.transform(X)
        Y = [train_set[i][-1] for i in range(len(train_set))]

        clf = CategoricalNB()
        clf.fit(X, Y)

        #print(clf.predict_proba([test_set[0][0:-1]]))  # test_set, ne train_set - davashe drugi vrednosti
        # print(dataset)

        test_set_x = encoder.transform([test_set[i][:-1] for i in range(len(test_set))])
        accuracy = 0
        for i in range(len(test_set)):
            predict = clf.predict([test_set_x[i]])
            if predict[0] == test_set[i][-1]:
                accuracy += 1

        print(accuracy/len(test_set))

        entry = [el for el in input().split(" ")]
        entry = encoder.transform([entry])  # vaka se dobiva dvodimenzionalna niza
        print(clf.predict(entry))

#         vhigh vhigh 2 2 med low
