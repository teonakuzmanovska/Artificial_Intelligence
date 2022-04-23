import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    # se stava r pred path za da konvertira normalen vo raw string
    with open(r"C:\Users\Lenovo\PycharmProjects\pythonProject1\aud6_naive_bayes\cars.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]  # vo dataset gi smestuvame site osven prviot red(iminjata na kolonite)

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]  #slicing nema da raboti bez int, gi zimame prvite 70%
    train_x = [t[:-1] for t in train_set]  # site karakteristiki na mnozhestvoto osven klasata(posledniot element)
    train_x = encoder.transform(train_x)  # ova go smestuvame vo train_x
    train_y = [t[-1] for t in train_set]  # site karakteristiki samo na klasata(posledniot element)

    test_set = dataset[int(0.7 * len(dataset)):]  # gi zimame poslednite 30%
    test_x = [t[:-1] for t in test_set]  # se od pochetokot, bez posledniot element
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    classifier = DecisionTreeClassifier(criterion='entropy')
    classifier.fit(train_x, train_y)  # za da go trenirame klasifikatorot

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    correct_samples = 0
    for x, y in zip(test_x, test_y):
        y_predicted = classifier.predict([x])[0]
        if y_predicted == y:
            correct_samples += 1

    accuracy = correct_samples / len(test_set)
    print(f'Accuracy: {accuracy}')

    feature_importances = list(classifier.feature_importances_)
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Most important feature: {most_important_feature}')
    print(f'Least important feature: {least_important_feature}')

    train_x_2 = list()
    for t in train_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]  # se trga most important, analogno kje trgnesh i za ispiti
        train_x_2.append(sample)  # se dodava redicata

    test_x_2 = list()
    for t in test_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]  # se trga most important, analogno kje trgnesh i za ispiti
        test_x_2.append(sample)  # se dodava redicata

    train_x_3 = list()
    for t in train_x:
        sample = [t[i] for i in range(len(t)) if i != least_important_feature]  # se trga most important, analogno kje trgnesh i za ispiti
        train_x_3.append(sample)  # se dodava redicata

    test_x_3 = list()
    for t in test_x:
        sample = [t[i] for i in range(len(t)) if i != least_important_feature]  # se trga most important, analogno kje trgnesh i za ispiti
        test_x_3.append(sample)  # se dodava redicata

    classifier_2 = DecisionTreeClassifier(criterion='entropy')
    classifier_3 = DecisionTreeClassifier(criterion='entropy')

    classifier_2.fit(train_x_2, train_y)  # bidejkji nemame promena vo klasite, predavame train_y
    classifier_3.fit(train_x_3, train_y)

    print(f'Depth(removed most important feature): {classifier_2.get_depth()}')
    print(f'Number of leaves(removed most important feature): {classifier_2.get_n_leaves()}')

    print(f'Depth(removed least important feature): {classifier_3.get_depth()}')
    print(f'Number of leaves(removed least important feature): {classifier_3.get_n_leaves()}')

    correct_samples_2 = 0
    for x, y in zip(test_x_2, test_y):
        y_predicted = classifier_2.predict([x])[0]
        if y_predicted == y:
            correct_samples_2 += 1

    correct_samples_3 = 0
    for x,y in zip(test_x_3, test_y):
        y_predicted = classifier_3.predict([x])[0]
        if y_predicted == y:
            correct_samples_3 += 1

    accuracy_2 = correct_samples_2 / len(test_set)
    accuracy_3 = correct_samples_3 / len(test_set)

    print(f'Accuracy(removed most important criteria): {accuracy_2}')
    print(f'Accuracy(removed least important criteria): {accuracy_3}')
