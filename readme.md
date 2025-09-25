# Atividade Avaliativa de Programação Orientada a Objetos ministrada pelo professor Izaque Esteves da Silva

## Professor Ministrante: Izaque Esteves 

## Alunos: 
- Fernando Lopes
- Kauan da Rosa Paulino
- Vinicius Eduardo da Fonseca Sirino

### Proposta e Objetivo de atividade

#### Objetivo
Criar um jogo da **forca clássico** utilizando os conceitos da **programação orientada a objetos** em Python.

---

#### Requisitos

#### Classe `Palavra`
- **Atributos**:  
  - `palavra` (string)  
  - `letras_acertadas` (lista)

- **Métodos**:  
  - `verificar_letra` → retorna `True` se a letra existe na palavra.  
  - `mostrar_palavra` → mostra a palavra com as letras acertadas e **underlines** (`*`) para as letras não acertadas.  

---

#### Classe `Jogo`
- **Atributos**:  
  - `palavra_atual`  
  - `tentativas_restantes`

- **Métodos**:  
  - `iniciar_jogo`  
  - `jogar` → pede uma letra ao usuário e verifica se está correta.  
  - `verificar_vitoria`  
  - `verificar_derrota`  

---

#### Mecânicas do Jogo
- O jogo escolhe uma palavra **aleatoriamente** de uma lista.  
- O jogador tenta adivinhar as letras da palavra.  
- Acertando a letra, somente as letras da palavra que já foram descobertas serão mostradas.  

#### Exemplo:
- Palavra: `abacate`  
- Usuário acertou a letra **a**  
- Exibição: `a_a_a__`

