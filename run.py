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

for experiment in experiments:
    names = list(map(lambda x: str(x), range(experiment["nofColumns"] - 1))) + ["Decision"]

    print("-------------------------")
    print("Experiment ID:", experiment['id'])

    for algorithm in algorithms:

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
            print("{\"" + j[0][0] + "\", \"" + j[0][1] + "\"} => " + str(j[1]) + ("," if i < len(results) - 1 else ""))

    print("\n") # make some space for the next experiment
