# GitHub a pull requesty

## Před srazem
* Doporučuju projít si materiály https://naucse.python.cz/2019/gitworking-openalt/
* Nainstaluj si Git
* Na Windows pracuj v příkazové řádce Git Bash (v Průzkumníku si ho můžeš otevřít v kontextovém menu přes pravé tlačítko myši). Na Linux a v MacOS pracuj normálně.
* Nakonfiguruj si Git
    * jméno
    * e-mail
    * editor
* **Nedělej úkoly dopředu.** Rozdělíme si práci až společně na srazu.

## Aktivita na sraz

* Společně si všichni zkontrolujeme, že máme správně a shodně nastavený Git.
* Toto je speciální aktivita, kde se nebudeme řídit postupem pro odevzdávání úkolů, který jsem říkal doposud.
* Toto bude reprezentovat **skutečný způsob práce na GitHubu**, kdy budete chtít dosáhnout umístění svého kódu v branchi main v hlavním repu.

ChatGPT mi vytvořilo podle zadání bashový skript, který vygeneroval všechny tasky i unit testy. Musel jsem to trochu upravit, protože to nefungovalo hned out-of-the-box. Příkaz `pytest` spustí všechny testy.

Funkce s tasky používají _typing annotation_ - je to moderní způsob psaní funkcí v Pythonu, kdy určujeme datové typy parametrů funkce a datový typ návratové hodnoty.

Úkoly 01 až 25 jsou jednoduché. Výzvou jsou až úkoly 25 až 40.

### Postup samostatné práce

1. Vybereš si na jakém tasku budeš dělat. Napíšeme na tabuli, kdo na čem bude dělat.
1. Vyřešíš a otestuješ task
    * Spustíš na své řešení `autopep8` - přečti si o [Coding style](https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/coding-style/coding-style)
    * Spustíš na své řešení `pytest`
        * Jednotlivý test spustíš:
            ```
            pytest test_01_sum_two_numbers.py -vv
            ```

            Parametr `-v` a `-vv` zvyšuje vypisování detailů chyb.

1. Commitneš řešení do nové branche
    * Název branche by měl obsahovat tvoje jméno nebo iniciály, číslo tasku a krátký popisek:
        * `mz-01-sum-two-numbers`
    * **Commit message musí začínat číslem tasku** a pokračovat vhodným popiskem:
        * `01 Soucet dvou cisel`
    * Pushneš tuto branch do svého repa.
1. Vytvoříš PR, které bude chtít zamergovat branch s řešením tasku ze svého forku do branche main hlavního repa.
    * **PR musí obsahovat přesně jeden tvůj commit**
        * Nech si od koučů poradit s `git commit --amend` popř. `git rebase -i`.
    * Aby byla hra na práci co nejvěrnější, je v repozitáři nastaveno CI (Continuous integration)
        * GitHub Action automaticky spustí `autopep8` a `pytest` pro tvůj task
        * Toto GitHub Action [workflow](https://github.com/PyLadiesCZ-Brno/python-knihovny/blob/main/.github/workflows/pr-checks.yml) bylo také vygenerováno pomocí ChatGPT, ale bylo opět nutné ho rozfungovat a zlepšit.
