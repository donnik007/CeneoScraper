# CeneoScraper
## Etap 1 - pobieranie opinii o produkcie
### Eato1.1 - porbanie skladowych pojedynczej opinii
- pobranie kodu pojedynczej strony z opinaimi o produkcie
- wydobycie z kodu strony fragmentu odpowoadającego pojedynczej opinii
- zapisanie do pojedynczych zmiennych wartosci składowych opinii

 |Składowa|Selekotr CSS|Nazwa zmiennej|Typ danych|
 |--------|------------|--------------|----------|
 |Opinia|div.js_product-review|opinion||
 |Indentyfikator opinii|["data-entry-id"]|opinionId||
 |Autor|span.user-post__author-name|author||
 |Rekomendacja|span.user-post__author-recomendation > em|rcmd||
 |Liczba gwiazdek|span.user-post__score-count|stars||
 |Treść opinii|div.user-post__text|content||
 |Lista zalet|div[class*="positives"] ~ div.review-feature__item|pros||
 |Lista wad|div[class*="negatives"] ~ div.review-feature__item|cons||
 |Czy potwierdzona zakupem|div.review-pz|purchased||
 |Data wystawienia|span.user-post__published > time:nth-child(1)["datatimes"]|publishDate||
 |Data zakupu|span.user-post__published > time:nth-child(2)["datatimes"]|purchaseDate||
 |Dla ilu osob przydatna|span[id^="votes-yes"]|useful||
 |Dla ilu osob nieprzydatna|span[id^="votes-no"]|useless||
