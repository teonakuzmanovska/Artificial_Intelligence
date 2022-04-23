# from sklearn import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
           [6.4, 2.8, 5.6, 2.1, 0],
           [5.1, 3.3, 1.7, 0.5, 1],
           [5.1, 3.5, 1.4, 0.2, 1],
           [4.6, 3.1, 1.5, 0.2, 1],
           [5.8, 2.7, 5.1, 1.9, 0],
           [5.5, 3.5, 1.3, 0.2, 1],
           [5.7, 2.6, 3.5, 1.0, 2],
           [5.0, 3.5, 1.3, 0.3, 1],
           [6.3, 2.5, 5.0, 1.9, 0],
           [6.2, 2.2, 4.5, 1.5, 2],
           [5.0, 3.4, 1.6, 0.4, 1],
           [5.7, 4.4, 1.5, 0.4, 1],
           [4.9, 2.4, 3.3, 1.0, 2],
           [4.4, 2.9, 1.4, 0.2, 1],
           [5.5, 2.4, 3.7, 1.0, 2],
           [5.6, 2.5, 3.9, 1.1, 2],
           [5.6, 2.8, 4.9, 2.0, 0],
           [4.8, 3.4, 1.6, 0.2, 1],
           [5.6, 3.0, 4.5, 1.5, 2],
           [6.0, 3.0, 4.8, 1.8, 0],
           [6.3, 3.3, 4.7, 1.6, 2],
           [4.8, 3.0, 1.4, 0.1, 1],
           [7.9, 3.8, 6.4, 2.0, 0],
           [4.9, 3.0, 1.4, 0.2, 1],
           [4.3, 3.0, 1.1, 0.1, 1],
           [6.8, 3.2, 5.9, 2.3, 0],
           [5.6, 2.7, 4.2, 1.3, 2],
           [5.2, 4.1, 1.5, 0.1, 1],
           [6.2, 2.9, 4.3, 1.3, 2],
           [6.5, 2.8, 4.6, 1.5, 2],
           [5.4, 3.9, 1.3, 0.4, 1],
           [5.8, 2.6, 4.0, 1.2, 2],
           [5.4, 3.7, 1.5, 0.2, 1],
           [4.5, 2.3, 1.3, 0.3, 1],
           [6.3, 3.4, 5.6, 2.4, 0],
           [6.2, 3.4, 5.4, 2.3, 0],
           [5.7, 2.5, 5.0, 2.0, 0],
           [5.8, 2.7, 3.9, 1.2, 2],
           [6.4, 2.7, 5.3, 1.9, 0],
           [5.1, 3.8, 1.6, 0.2, 1],
           [6.3, 2.5, 4.9, 1.5, 2],
           [7.7, 2.8, 6.7, 2.0, 0],
           [5.1, 3.5, 1.4, 0.3, 1],
           [6.8, 2.8, 4.8, 1.4, 2],
           [6.1, 3.0, 4.6, 1.4, 2],
           [5.5, 4.2, 1.4, 0.2, 1],
           [5.0, 2.0, 3.5, 1.0, 2],
           [7.7, 3.0, 6.1, 2.3, 0],
           [5.1, 2.5, 3.0, 1.1, 2],
           [5.9, 3.0, 5.1, 1.8, 0],
           [7.2, 3.2, 6.0, 1.8, 0],
           [4.9, 3.1, 1.5, 0.2, 1],
           [5.7, 3.0, 4.2, 1.2, 2],
           [6.1, 2.9, 4.7, 1.4, 2],
           [5.0, 3.2, 1.2, 0.2, 1],
           [4.4, 3.2, 1.3, 0.2, 1],
           [6.7, 3.1, 5.6, 2.4, 0],
           [4.6, 3.6, 1.0, 0.2, 1],
           [5.1, 3.4, 1.5, 0.2, 1],
           [5.2, 2.7, 3.9, 1.4, 2],
           [6.4, 3.1, 5.5, 1.8, 0],
           [7.4, 2.8, 6.1, 1.9, 0],
           [4.9, 3.1, 1.5, 0.1, 1],
           [5.0, 3.5, 1.6, 0.6, 1],
           [6.7, 3.1, 4.7, 1.5, 2],
           [6.4, 3.2, 5.3, 2.3, 0],
           [6.3, 2.7, 4.9, 1.8, 0],
           [5.8, 4.0, 1.2, 0.2, 1],
           [6.9, 3.1, 5.4, 2.1, 0],
           [5.9, 3.2, 4.8, 1.8, 2],
           [6.6, 2.9, 4.6, 1.3, 2],
           [6.1, 2.8, 4.0, 1.3, 2],
           [7.7, 2.6, 6.9, 2.3, 0],
           [5.5, 2.6, 4.4, 1.2, 2],
           [6.3, 2.9, 5.6, 1.8, 0],
           [7.2, 3.0, 5.8, 1.6, 0],
           [6.5, 3.0, 5.8, 2.2, 0],
           [5.4, 3.9, 1.7, 0.4, 1],
           [6.5, 3.2, 5.1, 2.0, 0],
           [5.9, 3.0, 4.2, 1.5, 2],
           [5.1, 3.7, 1.5, 0.4, 1],
           [5.7, 2.8, 4.5, 1.3, 2],
           [5.4, 3.4, 1.5, 0.4, 1],
           [4.6, 3.4, 1.4, 0.3, 1],
           [4.9, 3.6, 1.4, 0.1, 1],
           [6.7, 2.5, 5.8, 1.8, 0],
           [5.0, 3.6, 1.4, 0.2, 1],
           [6.7, 3.3, 5.7, 2.5, 0],
           [4.4, 3.0, 1.3, 0.2, 1],
           [6.0, 2.2, 5.0, 1.5, 0],
           [6.0, 2.2, 4.0, 1.0, 2],
           [5.0, 3.4, 1.5, 0.2, 1],
           [5.7, 2.8, 4.1, 1.3, 2],
           [5.5, 2.4, 3.8, 1.1, 2],
           [5.1, 3.8, 1.9, 0.4, 1],
           [6.9, 3.1, 5.1, 2.3, 0],
           [5.6, 2.9, 3.6, 1.3, 2],
           [6.1, 2.8, 4.7, 1.2, 2],
           [5.5, 2.5, 4.0, 1.3, 2],
           [5.5, 2.3, 4.0, 1.3, 2],
           [6.0, 2.9, 4.5, 1.5, 2],
           [5.1, 3.8, 1.5, 0.3, 1],
           [5.7, 3.8, 1.7, 0.3, 1],
           [6.7, 3.3, 5.7, 2.1, 0],
           [4.8, 3.1, 1.6, 0.2, 1],
           [5.4, 3.0, 4.5, 1.5, 2],
           [6.5, 3.0, 5.2, 2.0, 0],
           [6.8, 3.0, 5.5, 2.1, 0],
           [7.6, 3.0, 6.6, 2.1, 0],
           [5.0, 3.0, 1.6, 0.2, 1],
           [6.7, 3.0, 5.0, 1.7, 2],
           [4.8, 3.4, 1.9, 0.2, 1],
           [5.8, 2.8, 5.1, 2.4, 0],
           [5.0, 2.3, 3.3, 1.0, 2],
           [4.8, 3.0, 1.4, 0.3, 1],
           [5.2, 3.5, 1.5, 0.2, 1],
           [6.1, 2.6, 5.6, 1.4, 0],
           [5.8, 2.7, 4.1, 1.0, 2],
           [6.9, 3.2, 5.7, 2.3, 0],
           [6.4, 2.9, 4.3, 1.3, 2],
           [7.3, 2.9, 6.3, 1.8, 0],
           [6.3, 2.8, 5.1, 1.5, 0],
           [6.2, 2.8, 4.8, 1.8, 0],
           [6.7, 3.1, 4.4, 1.4, 2],
           [6.0, 2.7, 5.1, 1.6, 2],
           [6.5, 3.0, 5.5, 1.8, 0],
           [6.1, 3.0, 4.9, 1.8, 0],
           [5.6, 3.0, 4.1, 1.3, 2],
           [4.7, 3.2, 1.6, 0.2, 1],
           [6.6, 3.0, 4.4, 1.4, 2]]

if __name__ == '__main__':

    train_set1 = dataset[:int(0.3 * len(dataset))]  # okej mi e da ima : od dvete strani za vtorite 30%?
    train_x1 = [t[:-1] for t in train_set1]  # site karakteristiki na mnozhestvoto osven klasata(posledniot element)
    train_y1 = [t[-1] for t in train_set1]  # site karakteristiki samo na klasata(posledniot element)

    train_set2 = dataset[int(0.3 * len(dataset)):int(0.6 * len(dataset))]  # okej mi e da ima : od dvete strani za vtorite 30%?
    train_x2 = [t[:-1] for t in train_set2]  # site karakteristiki na mnozhestvoto osven klasata(posledniot element)
    train_y2 = [t[-1] for t in train_set2]  # site karakteristiki samo na klasata(posledniot element)

    train_set3 = dataset[int(0.6 * len(dataset)):]  # okej mi e da ima : od dvete strani za vtorite 30%?
    train_x3 = [t[:-1] for t in train_set3]  # site karakteristiki na mnozhestvoto osven klasata(posledniot element)
    train_y3 = [t[-1] for t in train_set3]  # site karakteristiki samo na klasata(posledniot element)

    classifier1 = DecisionTreeClassifier(criterion='entropy')
    classifier1.fit(train_x1, train_y1)  # za da go trenirame klasifikatorot

    classifier2 = DecisionTreeClassifier(criterion='entropy')
    classifier2.fit(train_x2, train_y2)  # za da go trenirame klasifikatorot

    classifier3 = DecisionTreeClassifier(criterion='entropy')
    classifier3.fit(train_x3, train_y3)  # za da go trenirame klasifikatorot

    entry = [float(el) for el in input().split(", ")]
    entry = entry[:-1]

    predict1 = classifier1.predict([entry])
    predict2 = classifier2.predict([entry])
    predict3 = classifier3.predict([entry])

    predictions = []
    predictions.append(predict1[0])
    predictions.append(predict2[0])
    predictions.append(predict3[0])

    correct_samples_zero = 0
    correct_samples_one = 0
    correct_samples_two = 0

    for pred in predictions:
        if pred == 0:
            correct_samples_zero += 1
        if pred == 1:
            correct_samples_one += 1
        if pred == 2:
            correct_samples_two += 1

    election = []
    election.append(correct_samples_zero)
    election.append(correct_samples_one)
    election.append(correct_samples_two)

    max = 0
    for i in election:
        if i < max:
            max = i

    max = 0
    if correct_samples_zero > correct_samples_one and correct_samples_zero > correct_samples_two:
        max = 0
    elif correct_samples_one > correct_samples_zero and correct_samples_one > correct_samples_two:
        max = 1
    elif correct_samples_two > correct_samples_zero and correct_samples_two > correct_samples_one:
        max = 2
    else:
        max = 'unknown'

    print("Glasovi: {"+f'0: {correct_samples_zero}, 1: {correct_samples_one}, 2: {correct_samples_two}'+"}")
    print(f'Predvidena klasa: {max}')
