# IO_projekt2

> English version below / Wersja angielska poniżej

## Opis projektu

Projekt **IO_projekt2** to jeden z dwóch projektów przygotowanych w języku Python jako zaliczenie przedmiotu **Inteligencja Obliczeniowa**, który miałem na czwartym semestrze studiów I stopnia na kierunku **Informatyka o profilu praktycznym**. Obejmował on między innymi zagadnienia związane ze współczesnym rozwojem sztucznej inteligencji, przede wszystkim: algorytmy klasyfikacyjne, trenowanie sieci neuronowych, sieci generatywne GAN oraz duże modele językowe (w skrócie z ang. LLM).

W poprzednim projekcie, o nazwie [IO_projekt1](https://github.com/mwojciechowski653/IO_projekt1) analizowałem skuteczność kilku metod klasyfikacyjnych (`Naive Bayes`, `KNN`, `Decision Tree`, `Neural Networks` oraz wpływ `PCA` na ich skuteczność) na danych wejściowych z autorskiej gry strategicznej.

Celem tego projektu było znalezienie z pomocą **algorytmu genetycznego** _"rozwiązania"_ ww. gry strategicznej, czyli takiego układu armii, który średnio wygrywałby najwięcej walk z losowanym przeciwnikiem. Walka jest nierówna, ponieważ przeciwnik ma o prawie 45% więcej budżetu na zbudowanie armii. Dodatkowo, nie przekazałem algorytmowi informacji o tym, jakie jednostki są najlepsze, ile kosztują oraz czy są jakieś inne, ukryte bonusy (np. bonus za flankowanie). Moim zadaniem było stworzenie odpowiedniej `fitness function` tak, aby nie tylko algorytm stosował się do zasad gry, ale również znalazł najlepszy układ wojsk od walki z dużo potężniejszym przeciwnikiem.

Projekt zawiera również system do generowania danych wejściowych (bitew lub samych armii przeciwnika), samą grę, przechowywanie wyników graczy oraz tworzenie wykresu wyników algorytmu genetycznego na przestrzeni kolejnych generacji.

## Koncept gry oraz struktura danych do badań

Punktem wyjścia tego projektu był plik `bitwa.py` który zawiera grę napisaną przeze mnie na pierwszym semestrze studiów. Nie jest on idealny, natomiast jako urozmaicenie (i utrudnienie) postanowiłem trzymać się zasady, aby ten kod był "nietykalny", co miało symulować scenariusz z wykorzystaniem zewnętrznego kodu. Sama gra to bardziej rozbudowana wersja klasycznego _kamień, papier, nożyce_, gdzie możemy wystawić trzy rodzaje jednostek - _piechurzy_, _konnica_ lub _artylerzysci_ na pole bitwy - po jednym rodzaju na każde skrzydło (lewe skrzydło, centrum lub prawe skrzydło). Jednostki mają różną cenę oraz różne współczynniki walki między sobą. Po określeniu poziomu trudności (wybraniu jak duży budżet mamy w porównaniu do przeciwnika) losowana jest armia przeciwnika, następnie możemy dokonać zwiadu za odpowiednią opłatą, aby podejrzeć wybrane skrzydło/a przeciwnika. Później wybieramy typ jednostek oraz ich liczebność na każde skrzydło. Walka przebiega przez roztrzyganie osobno, kolejno lewego skrzydła, prawego skrzydła, a na końcu walki w centrum, gdzie brane pod uwagę (z odpowiednim bonusem za flankowanie) są pozostałości z walk na skrzydłach. Przy każdej walce losowany jest pseudolosowy współczynnik, tak żeby wyniki nie były w pełni przewidywalne. Jeśli wygraliśmy, obliczana jest końcowa punktacja na podstawie tego, ile jednostek oraz jakiego typu nam zostało. Wynik zapisywany jest wraz z imieniem/nickem w pliku o nazwie `wynikiGraczy.txt`.

W tym projekcie najważniejszy był proces stworzenia odpowiedniej `fitness function` nagradzającej za stosowanie się do zasad gry (na przykład nie przekraczanie budżetu) oraz jednocześnie ustawianie wojsk w naturalny sposób, przez obstawianie obu skrzydeł i ich wygrywanie, co było odpowiednio nagradzane.

Dane, na których algorytm genetyczny był testowany są inne niż w poprzednim projekcie - to algorytm generuje wojska "gracza", dlatego w bazie danych jest tylko 6 kolumn informujących o wojskach "przeciwnika". Wygenerowane bitwy znajdują się w pliku `rozgrywkiSamWrog.txt`. W kolumnach podane są kolejno typy jednostek oraz ich liczebność na każdym skrzydle. Do wygenerowania odpowiednich danych stworzyłem generator, który znajduje się w pliku `generatorBitw.py`.

## Struktura katalogu

```
IO_projekt2/
├── wykresy/                          # Katalog z przykładowymi wykresami wyników działania algorytmu
├── IO2_Bitwa.pdf                     # Dokumentacja projektu i przedstawienie wyników (PDF)
├── LICENSE                           # Licencja projektu
├── algorytmGenetyczny.py             # Fitness function, sam algorytm oraz tworzenie wykresu
├── bitwa.py                          # Logika symulacji pojedynczej bitwy
├── funkcjeRobocze.py                 # Funkcja pomocnicza (wczytanie i przygotowanie danych z pliku)
├── generatorBitw.py                  # Generator danych
├── ileWygranych.py                   # Analiza ile podana armia wygra bitew + statystyki
├── main.py                           # Menu - zagranie w grę lub wygenerowanie danych
├── requirements.txt                  # Wymagania i zależności potrzebne do uruchomienia projektu
├── rozgrywkiSamWrog.txt              # Dane wejściowe zawierające armie przeciwnika
└── wynikiGraczy.txt                  # Zapis wyników uzyskanych przez graczy

```

## Wymagania

Projekt wymaga Pythona 3.7 lub nowszego oraz następujących bibliotek:

- `numpy`
- `pandas`
- `pygad`
- `matplotlib`

Instalacja:

```bash
pip install -r requirements.txt
```

## Uruchomienie

1. Sklonuj repozytorium:

```bash
git clone https://github.com/mwojciechowski653/IO_projekt2.git
cd IO_projekt2
```

2. Uruchom środowisko wirtualne (opcjonalnie):

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Uruchom główny skrypt aby zagrać lub wygenerować nowe rekordy dla algorytmu:

```bash
python main.py
```

Alternatywnie, urucham skrypt z algorytmem genetycznym, który na przestrzeni 20 generacji wygeneruje najlepsze znalezione rozwiązanie i statystyki dla niego:

```bash
python algorytmGenetyczny.py
```

## Wizualizacja wyników

Przy każdym uruchomieniu pliku `algorytmGenetyczny.py`, na końcu działania programu, zostaje zapisany w folderze `wykresy/` wykres. Przedstawia on zmiany wartości wyniku `fitness function` na przekazanych danych w zależności od generacji. Domyślnie nowy wykres zawsze nazywa się `wykres.png`.

## Dokumentacja

Plik `IO2_Bitwa.pdf` zawiera opis projektu, założenia jakie określiłem względem bazy danych, a także `fitness function` oraz przedstawienie wyników i wniosków.

## Autor

- **Marcin Wojciechowski**  
  [GitHub](https://github.com/mwojciechowski653)

## Licencja

Projekt jest udostępniany na licencji **MIT**.  
Pełny tekst licencji znajdziesz w pliku [LICENSE](LICENSE).

W skrócie: możesz używać, kopiować, modyfikować i rozpowszechniać ten kod na warunkach MIT. Oprogramowanie dostarczane jest „tak jak jest”, bez żadnych gwarancji.

# IO_projekt2 English version

## Project Description

The **IO_projekt2** project is one of two projects developed in Python as part of the **Computational Intelligence** course I took during the fourth semester of my Bachelor’s studies in **Computer Science (practical profile)**. It covered topics related to modern AI development, including classification algorithms, neural network training, generative adversarial networks (GANs), and large language models (LLMs).

In the previous project, called [IO_projekt1](https://github.com/mwojciechowski653/IO_projekt1), I analyzed the effectiveness of several classification methods (`Naive Bayes`, `KNN`, `Decision Tree`, `Neural Networks` and the impact of `PCA` on their performance) using input data from my own strategy game.

The goal of this project was to use a **genetic algorithm** to find a _"solution"_ to the aforementioned strategy game - an army configuration that, on average, would win the most battles against a randomly generated opponent. The battle is unbalanced, as the opponent has almost 45% more budget to build their army. Additionally, the algorithm was not given information about which units are the best, their cost, or any hidden bonuses (e.g., flanking bonus). My task was to create an appropriate `fitness function` so that the algorithm not only followed the rules of the game but also found the best army configuration to fight against a much stronger opponent.

The project also includes a system for generating input data (battles or opponent armies), the game itself, player score storage, and generating a chart showing the performance of the genetic algorithm over generations.

## Game Concept and Research Data Structure

The starting point of this project was the `bitwa.py` file, which contains a game I wrote during my first semester. It is not perfect, but as an additional challenge I decided to keep this code "untouchable" to simulate working with external code. The game is an extended version of the classic _rock, paper, scissors_, where you can deploy three types of units - _infantry_, _cavalry_, or _artillery_ - on the battlefield, one type for each wing (left wing, center, or right wing). Units have different costs and combat effectiveness against each other. After selecting the difficulty level (determining how large our budget is compared to the opponent’s), the opponent’s army is randomly generated. You can then perform reconnaissance for a fee to peek at selected wings of the opponent. Afterwards, you choose the type and number of units for each wing. The battle unfolds separately: left wing, right wing, and finally the center, where the remnants from the wings (with flanking bonuses) are considered. A pseudorandom coefficient is drawn in each fight, making outcomes not fully predictable. If you win, the final score is calculated based on the remaining units and their types. The result is saved along with the player’s name/nickname in `wynikiGraczy.txt`.

In this project, the most important part was designing a `fitness function` that rewarded compliance with game rules (e.g., not exceeding the budget) and encouraged natural strategies such as deploying units on both flanks.

Compared to the previous project, the data tested with the genetic algorithm is different - here, the algorithm generates the player's army, so the dataset only contains 6 columns describing the enemy's army. Generated battles are stored in `rozgrywkiSamWrog.txt`. Columns specify unit types and their numbers per flank. I created a generator (`generatorBitw.py`) to produce these datasets.

## Directory Structure

```
IO_projekt2
├── wykresy/                          # Folder with example charts of algorithm performance
├── IO2_Bitwa.pdf                     # Project documentation and presentation of results (PDF)
├── LICENSE                           # Project license
├── algorytmGenetyczny.py             # Fitness function, the algorithm itself, and chart generation
├── bitwa.py                          # Logic for simulating a single battle
├── funkcjeRobocze.py                 # Helper function (loading and preparing data from file)
├── generatorBitw.py                  # Data generator
├── ileWygranych.py                   # Analysis of how many battles a given army wins + statistics
├── main.py                           # Menu – play the game or generate data
├── requirements.txt                  # Requirements and dependencies to run the project
├── rozgrywkiSamWrog.txt              # Input data containing enemy armies
└── wynikiGraczy.txt                  # Records of players' results
```

## Requirements

The project requires Python 3.7+ and the following libraries:

- `numpy`
- `pandas`
- `pygad`
- `matplotlib`

Installation:

```bash
pip install -r requirements.txt
```

## Running the Project

1. Clone the repository:

```bash
git clone https://github.com/mwojciechowski653/IO_projekt2.git
cd IO_projekt2
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Run the main script to play the game or generate data:

```bash
python main.py
```

Alternatively, run the genetic algorithm script to generate the best solution out of 20 generations:

```bash
python algorytmGenetyczny.py
```

## Results Visualization

Each time `algorytmGenetyczny.py` is run, at the end of execution, a chart is saved in the `wykresy/` directory. It shows the change in `fitness function` value across generations. By default, the chart is named `wykres.png`.

## Documentation

The `IO2_Bitwa.pdf` file contains a description of the project, database and `fitness function` assumptions, results, and conclusions.

## Author

- **Marcin Wojciechowski**\
  [GitHub](https://github.com/mwojciechowski653)

## License

This project is licensed under the **MIT** license.\
The full license text can be found in the [LICENSE](LICENSE) file.

In short: you are free to use, copy, modify, and distribute this code under the MIT terms. The software is provided “as is”, without any warranty.
