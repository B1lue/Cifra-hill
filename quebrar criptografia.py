from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from main import equivalenteDecimal, cifraHill, A


def converter_para_numeros(texto, length=5):
    # Converte o texto para números e preenche com zeros se for muito curto
    return [equivalenteDecimal(char) for char in texto.ljust(length, '0')]


textos_simples = ["oi", "ola", "tudo", "bem"]

textos_cifrados = [cifraHill(texto, A) for texto in textos_simples]

X = [converter_para_numeros(texto) for texto in textos_cifrados]
y = [converter_para_numeros(texto) for texto in textos_simples]

X = [converter_para_numeros(texto) for texto in textos_cifrados]
y = [converter_para_numeros(texto) for texto in textos_simples]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)

accuracy = 0
while accuracy < 0.95:
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = sum([y1 == y2 for y1, y2 in zip(y_pred, y_test)]) / len(y_test)
    print("Acurácia: ", accuracy)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)

    clf.fit(X_train, y_train)

    #
    y_pred = clf.predict(X_test)

    # Calcula a precisão do modelo
    accuracy = accuracy_score(y_test, y_pred)
    print("Acurácia: ", accuracy)
