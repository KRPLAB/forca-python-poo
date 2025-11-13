class Palavra:
    def __init__(self, palavra):
        self.palavra = palavra.lower()
        self.letras_acertadas = []

    def verificar_letra(self, letra):
        letra = letra.lower()
        if letra in self.palavra:
            if letra not in self.letras_acertadas:
                self.letras_acertadas.append(letra)
            return True
        return False
    
    def mostrar_palavra(self):
        palavra_mostrada = ""
        for letra in self.palavra:
            if letra in self.letras_acertadas:
                palavra_mostrada += letra
            else:
                palavra_mostrada += "_"
        return palavra_mostrada