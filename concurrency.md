# Współbieżność

## Cel:
Umiejętność wykorzystania asynchronicznego przetwarzania w API.

## Zadanie:
Utwórz prosty serwis w Spring Boot'cie który zawiera jeden endpoint z dwoma parametrami 'start' i 'end'. Endpoint ten powinien zwracać ilość liczb pierwszych w przedziale [start, end].

Następnie utwórz dwa skrypty pythonowe, które dla par wartości (start, end) w [values.json](values.json) policzą ilość liczb pierwszych, oraz wypiszą czas trwania obliczeń. Jeden powinien używać do tego żądań asynchronicznych (możesz tutaj skorzystać np. z biblioteki [aiohttp](https://docs.aiohttp.org/en/stable/)), drugi za to powinien używac żądań synchronicznych (np. z biblioteki [requests](https://requests.readthedocs.io/en/latest/)). Porównaj czas wykonania obu skryptów.

## Przykłady:
Żądania:
```
GET localhost:8080/primes?start=0&end=4
GET localhost:8080/primes?start=2&end=7
GET localhost:8080/primes?start=10&end=100
```
Zwracane wartości:
```
2
4
21
```

## Rezultat:
Twoje rozwiązanie powinno zawierać:
 - aplikację Springową budowaną przy użyciu narzędzia [gradle](https://spring.io/guides/gs/gradle/)
 - 2 skrypty pythonowe: jeden z przetwarzaniem asynchronicznym, a drugi z synchronicznym
 - plik 'requirements.txt' z zainstalowanymi paczkami pythonowymi
 - plik 'output.json' z wynikami

## Przydatne linki:
 - https://start.spring.io/
 - https://www.baeldung.com/building-a-restful-web-service-with-spring-and-java-based-configuration#controller
 