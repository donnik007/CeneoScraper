# CeneoScraper
## Etap 1 - Ekstracja pojedynczej opinii o produkcie , którego kod będzie wpisany w kodzie programu.
- pobranie kodu pojedynczej strony z opinaimi o produkcie
- wydobycie z kodu strony fragmentu odpowoadającego pojedynczej opinii
- zapisanie do pojedynczych zmiennych wartosci składowych opinii
- obsługa błędów
- transformacja danych do docelowych typów

 |Składowa|Selekotr CSS|Nazwa zmiennej|Typ danych|
 |--------|------------|--------------|----------|
 |Opinia|div.js_product-review|opinion|bs4.element.Tag|
 |Indentyfikator opinii|["data-entry-id"]|opinionId|str|
 |Autor|span.user-post__author-name|author|str|
 |Rekomendacja|span.user-post__author-recomendation > em|rcmd|bool|
 |Liczba gwiazdek|span.user-post__score-count|stars|float|
 |Treść opinii|div.user-post__text|content|str|
 |Lista zalet|div[class*="positives"] ~ div.review-feature__item|pros|list|
 |Lista wad|div[class*="negatives"] ~ div.review-feature__item|cons|list|
 |Czy potwierdzona zakupem|div.review-pz|purchased|bool|
 |Data wystawienia|span.user-post__published > time:nth-child(1)["datetime"]|publishDate|str|
 |Data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchaseDate|str|
 |Dla ilu osob przydatna|span[id^="votes-yes"]|useful|int|
 |Dla ilu osob nieprzydatna|span[id^="votes-no"]|useless|int|


## Etap 2 - Ekstracja wszytskich opinni o produkcie z pojedynczej strony.
- utworzenie słownika do przechowywania wszystkich składowych pojedynczej opinii
- utworzenie listy, do której będą dodawane słowniki reprezentujące pojedyncze opinie
- dodanie pętli, w której pobierane były składowe kolejnych opinii z pojedynczej strony

## Etap 3 - Ekstracja wszytskich opinii o produkcie z wszystkich stron
- dodanie pętli, w której:
    * pobierana jest strona z opiniami
    * dla każdej opinii na stronie pobierane są jej składowe
    * sprawdzane jest, czy istnieje kolejna strona z opiniami, które powinny zostać pobrane
- zapisanie wszytskich opinni o produkcie do pliku .json

# Etap 4 - Refaktoryzacja kodu
- parametryzacja indentyfatora opinii
- 

