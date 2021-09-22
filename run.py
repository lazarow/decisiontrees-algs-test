from chefboost import Chefboost as chef
import pandas as pd
import sys
import os
from shutil import copyfile
import itertools

enableParallelism = bool(sys.argv[1]) if len(sys.argv) > 1 else False;
nofCores = int(sys.argv[2]) if len(sys.argv) > 2 else 4;

dir = os.path.dirname(os.path.realpath(__file__))

experiments = [
    #{ "id": "", "training": "", "validation": "", "test": "", "nofColumns": 5 }
    { "id": "balance-scale", "training": "balance-scale_tr.data", "validation": "balance-scale_clean.data", "test": "balance-scale_te.data", "nofColumns": 5 },
    { "id": "breast-cancer", "training": "breast-cancer_tr.data", "validation": "breast-cancer_clean.data", "test": "breast-cancer_te.data", "nofColumns": 10 },
    { "id": "car", "training": "car_tr.data", "validation": "car_clean.data", "test": "car_te.data", "nofColumns": 7 },
    { "id": "lymphography", "training": "lymphography_tr.data", "validation": "lymphography_clean.data", "test": "lymphography_te.data", "nofColumns": 19 },
    { "id": "tic-tac-toe", "training": "tic-tac-toe_tr.data", "validation": "tic-tac-toe_clean.data", "test": "tic-tac-toe_te.data", "nofColumns": 10 }
]

algorithms = ["ID3", "C4.5", "CART", "CHAID"]

data = {}

for experiment in experiments:

    data[experiment["id"]] = {}

    names = list(map(lambda x: str(x), range(experiment["nofColumns"] - 1))) + ["Decision"]

    print("-------------------------")
    print("Experiment ID:", experiment['id'])

    for algorithm in algorithms:

        data[experiment["id"]][algorithm] = []

        print("-------------------------")
        print("Algorithm:", algorithm)

        # reloading here as fix to rearrange columns order
        trainingDF = pd.read_csv("datasets/" + experiment["training"], header=None, names=names)
        validationDF = pd.read_csv("datasets/" + experiment["validation"], header=None, names=names)
        testDF = pd.read_csv("datasets/" + experiment["test"], header=None, names=names)

        # fix for lymphography and ID3, it forces to change algorithm into Regression
        trainingDF['Decision'] = trainingDF['Decision'].astype(object)
        validationDF['Decision'] = validationDF['Decision'].astype(object)
        testDF['Decision'] = testDF['Decision'].astype(object)
        
        decisionValues = list(set(trainingDF['Decision'].tolist() + testDF['Decision'].tolist()))

        modelFilename = experiment["id"] + "." + algorithm + ".pkl"
        moduleFilename = experiment["id"] + "." + algorithm + ".py"
        if os.path.isfile(dir + "/models/" + modelFilename):
            if not os.path.exists(dir + "/outputs/rules"):
                os.makedirs(dir + "/outputs/rules")
            copyfile(dir + "/models/" + modelFilename, dir + "/outputs/rules/" + modelFilename)
            copyfile(dir + "/models/" + moduleFilename, dir + "/outputs/rules/rules.py")
            model = chef.load_model(modelFilename)
        else:
            model = chef.fit(
                df=trainingDF,
                validation_df=validationDF,
                config = {
                    "algorithm": algorithm,
                    "enableParallelism": enableParallelism,
                    "num_cores": nofCores
                }
            )
            chef.save_model(model, modelFilename)
            copyfile(dir + "/outputs/rules/" + modelFilename, dir + "/models/" + modelFilename)
            copyfile(dir + "/outputs/rules/rules.py", dir + "/models/" + moduleFilename)
        chef.evaluate(
            model=model,
            df=testDF,
            task="test"
        )
        results = {}
        for i, j in itertools.product(decisionValues, decisionValues):
            results[(str(i), str(j))] = 0
        for index, instance in testDF.iterrows():
            predicted = chef.predict(model, instance)
            actual = instance['Decision']
            results[(str(actual), str(predicted))] = results[(str(actual), str(predicted))] + 1
        
        for i, j in enumerate(sorted(results.items(), key=lambda item: item[1], reverse=True)):
            #print("{\"" + j[0][0] + "\", \"" + j[0][1] + "\"} => " + str(j[1]) + ("," if i < len(results) - 1 else ""))
            data[experiment["id"]][algorithm].append((j[0], j[1]))

# Database balance-scale:
data["balance-scale"]["mts"] = [(("R", "R"), 70), (("L", "L"), 77), (("B", "R"), 10), (("R", "L"), 6), (("L", "R"), 6), (("R", "B"), 9), (("L", "B"), 4), (("B", "L"), 6)]
# Database breast-cancer:
data["breast-cancer"]["mts"] = [(("no", "yes"), 4), (("no", "no"), 61), (("yes", "yes"), 4), (("yes", "no"), 15)]
# Database car:
data["car"]["mts"] = [(("acc", "acc"), 112), (("unacc", "unacc"), 364), (("vgood", "vgood"), 13), (("good", "good"), 14), (("unacc", "good"), 1), (("unacc", "acc"), 4), (("acc", "good"), 1), (("vgood", "good"), 3), (("good", "vgood"), 2), (("acc", "unacc"), 4), (("good", "acc"), 1)]
# Database lymphography:
data["lymphography"]["mts"] = [(("2", "2"), 21), (("3", "2"), 7), (("3", "3"), 10), (("2", "3"), 4), (("2", "1"), 1), (("2", "4"), 1), (("4", "2"), 1)]
# Database tic-tac-toe:
data["tic-tac-toe"]["mts"] = [(("positive", "positive"), 192), (("negative", "negative"), 83), (("negative", "positive"), 11), (("positive", "negative"), 2)]

for experiment in experiments:
    print("## Dataset:", experiment["id"])
    names = list(map(lambda x: str(x), range(experiment["nofColumns"] - 1))) + ["Decision"]
    trainingDF = pd.read_csv("datasets/" + experiment["training"], header=None, names=names)
    validationDF = pd.read_csv("datasets/" + experiment["validation"], header=None, names=names)
    testDF = pd.read_csv("datasets/" + experiment["test"], header=None, names=names)
    trainingDF['Decision'] = trainingDF['Decision'].astype(object)
    validationDF['Decision'] = validationDF['Decision'].astype(object)
    testDF['Decision'] = testDF['Decision'].astype(object)
    labels = list(set(trainingDF['Decision'].tolist() + testDF['Decision'].tolist()))
    algorithms = data[experiment["id"]]
    print("| Algorithm | Decision class | Accuracy | Precision | Recall | F1 |")
    print("| --- | --- | --- | --- | --- | --- |")
    for decision_class in labels:
        decision_class = str(decision_class)
        for algorithm in algorithms:
            fp = 0; fn = 0; tp = 0; tn = 0
            for (actual, prediction), count  in data[experiment["id"]][algorithm]:
                if actual == decision_class and prediction == decision_class:
                    tp = tp + count
                elif actual != decision_class and prediction != decision_class:
                    tn = tn + count
                elif actual != decision_class and prediction == decision_class:
                    fp = fp + count
                elif actual == decision_class and prediction != decision_class:
                    fn = fn + count
            epsilon = 0.0000001 #to avoid divison by zero exception
            precision = round(100*tp / (tp + fp + epsilon), 4)
            recall = round(100*tp / (tp + fn + epsilon), 4) #tpr
            f1_score = round((2 * precision * recall) / (precision + recall + epsilon), 4)
            accuracy = round(100 * (tp + tn) / (tp + tn + fp + fn + epsilon), 4)
            print("| " + algorithm, end="")
            print(" | " + decision_class + " | ", end = '')
            print(accuracy,"% | ", end='')
            print(precision,"% | ", end='')
            print(recall,"% | ", end='')
            print(f1_score,"% |")
        

'''

    
    
    for decision_class in labels:
        
        #if len(labels) < 3:
        #    break
'''
