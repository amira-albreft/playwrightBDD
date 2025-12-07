# User story 2:
# Som en användare
# vill jag kunna hamna på menyvalet "Katalog" per default när jag navigerar till sidan
# så att jag kan se vilka böcker som finns i katalogen

# Acceptanskriterier:
# - När användaren navigerar till sidan ska användaren automatiskt hamna på menyvalet "Katalog".
# - I katalog-vyn ska användaren kunna se en lista med böcker som finns i katalogen.


Feature: Visa katalog-vyn med böcker per default
    Som en användare
    vill jag kunna hamna på menyvalet "Katalog" per default när jag navigerar till sidan
    så att jag kan se vilka böcker som finns i katalogen

    Scenario: Visa katalog-vyn med böcker per default
        Given användaren navigerar till startsidan
        When sidan laddas
        Then texten "Välkommen!" visas
        And en katalog med böcker visas