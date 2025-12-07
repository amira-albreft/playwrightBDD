# User story 1:
# Som en användare
# vill jag kunna se en meny med knapparna "Katalog", "Lägg till bok" och "Mina böcker"
# så att jag kan välja vad jag vill göra utifrån menyvalen

# Acceptanskriterier:
# När användaren navigerar till sidan ska menyn visas med de tre knapparna: "Katalog", "Lägg till bok" och "Mina böcker".


Feature: Visa menyval med knappar
  Som en användare
  vill jag kunna se en meny med knapparna "Katalog", "Lägg till bok" och "Mina böcker"
  så att jag kan välja vad jag vill göra utifrån menyvalen

  Scenario: Visa meny med knappar
    Given användaren navigerar till startsidan
    When sidan laddas
    Then menyn ska visas med knapparna "Katalog", "Lägg till bok" och "Mina böcker"
