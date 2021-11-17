import numpy as np
import pandas as pd
import gdown
import os

def pull_dataset_file(name_file):
    file_id = '11JVg39uGJsYZZPKssnVoALl4A4RG7gI8'
    url = 'https://drive.google.com/uc?id='+file_id

    gdown.download(url, name_file, quiet=False)

if __name__ == "__main__":
    name_file = "TRNcod.csv"
    if not os.path.exists(name_file):
        print("Arquivo não existe ainda")
        print("Fazendo downloading...")
        pull_dataset_file(name_file)
        print("Download finalizado!")
    print("Lendo arquivo...")
    dataset = pd.read_csv(name_file)
    print("Separando classes...")
    class_1 = dataset[dataset['IND_BOM_1_1']==1]
    class_2 = dataset[dataset['IND_BOM_1_2']==1]
    class_1 = class_1.sample(frac=1)
    class_2 = class_2.sample(frac=1)
    print("Dividindo dados em treinamento, validação e teste")
    class_1_train, class_1_validate, class_1_test = np.split(class_1,[int(0.5*len(class_1)),int(0.75*len(class_1))])
    class_2_train, class_2_validate, class_2_test = np.split(class_2,[int(0.5*len(class_2)),int(0.75*len(class_2))])
    
    print("Classe 1 - ","Treino:",len(class_1_train),"Validação:",len(class_1_validate),"Teste:",len(class_1_test))
    print("Classe 2 - ","Treino:",len(class_2_train),"Validação:",len(class_2_validate),"Teste:",len(class_2_test))

    print("Repetindo dados de treino e validação da classe 2")
    while len(class_2_train) < len(class_1_train):
        count = (len(class_1_train)-len(class_2_train)) % len(class_2_train)
        class_2_train = pd.concat([class_2_train[:count],class_2_train])
    while len(class_2_validate) < len(class_1_validate):
        count = (len(class_1_validate)-len(class_2_validate)) % len(class_2_validate)
        class_2_validate = pd.concat([class_2_validate[:count],class_2_validate])
    
    print("Classe 1 - ","Treino:",len(class_1_train),"Validação:",len(class_1_validate),"Teste:",len(class_1_test))
    print("Classe 2 - ","Treino:",len(class_2_train),"Validação:",len(class_2_validate),"Teste:",len(class_2_test))

    print("Juntandos dados das classes de acordo com o tipo de separação")
    data_train = pd.concat([class_1_train,class_2_train])
    data_train = data_train.sample(frac=1)
    data_validate = pd.concat([class_1_validate,class_2_validate])
    data_validate = data_validate.sample(frac=1)
    data_test = pd.concat([class_1_test,class_2_test])
    data_test = data_test.sample(frac=1)

    print("Treinamento:",len(data_train),"Validação:",len(data_validate),"Teste:",len(data_test))
