import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

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
    train_y = [t[-1] for t in train_set] # site karakteristiki samo na klasata(posledniot element)

    test_set = dataset[int(0.7 * len(dataset)):]  # gi zimame poslednite 30%
    test_x = [t[:-1] for t in test_set]  # se od pochetokot, bez posledniot element
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    # od ovde e novo

    classifier = RandomForestClassifier(n_estimators=3, criterion='entropy')  # 3 drva na odluka
    classifier.fit(train_x, train_y)

    correct_samples = 0
    for x,y in zip(test_x, test_y):
        y_predicted = classifier.predict([x])[0]
        if y_predicted == y:
            correct_samples += 1

    print(f'Accuracy: {correct_samples / len(test_set)}')

    feature_importances = list(classifier.feature_importances_)
    most_important_feature = feature_importances.index(max(feature_importances))
    least_important_feature = feature_importances.index(min(feature_importances))

    print(f'Most important feature: {most_important_feature}')
    print(f'Least important feature: {least_important_feature}')


