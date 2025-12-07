# User story 5:
# Som en användare
# vill jag kunna lägga till en bok
# så att jag kan lägga till nya böcker i katalogen

# Acceptanskriterier:
# - När användaren klickar på menyvalet "Lägg till bok" ska ett formulär visas med fälten "Titel", "Författare" och en knapp "Lägg till bok".
# - Knappen "Lägg till ny bok" ska vara inaktiverad tills både titel och författare är ifyllda.
# - När användaren fyller i både titel och författare och klickar på knappen "Lägg till bok" ska den nya boken läggas till i katalogen.
# - Efter att boken lagts till ska fälten i formuläret vara tomma igen.

  Feature: Lägg till ny bok i katalogen
  Som en användare
  vill jag kunna lägga till en ny bok i katalogen
  så att jag kan hantera nya böcker i katalogen

    Scenario Outline: Lägga till en ny bok med giltig titel och författare
      Given användaren navigerar till "Lägg till bok"
      When ett formulär visas
      And användaren fyller i "Titel" med "<title>"
      And användaren fyller i "Författare" med "<author>"
      And användaren klickar på knappen "Lägg till ny bok" och formuläret är tomt igen
      Then boken med titeln "<title>" och författaren "<author>" läggs till i "Katalog"

      Examples:
        | title               | author               |
        | Den lilla prinsen   | Jakob Jakobsson      |
        | Harry Potter        | J.K. Rowling         |
        | Bamse               | Rune Andréasson      |

