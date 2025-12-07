# User story 5:
# Som en användare
# vill jag kunna lägga till en bok
# så att jag kan lägga till nya böcker i katalogen

# Acceptanskriterier:
# - Knappen "Lägg till ny bok" ska vara inaktiverad tills både titel och författare är ifyllda.



  Feature: Lägga till ny bok med endast titel ifylld
  Som en användare
  vill jag inte kunna lägga till en ny bok i katalogen om jag endast anger titel
  så att jag inte får ofullständiga böcker i katalogen

    Scenario: Försöka lägga till en ny bok med endast titel ifylld
      Given användaren navigerar till "Lägg till bok"
      When ett formulär visas
      And användaren fyller i "Titel" med "test"
      Then knappen "Lägg till ny bok" är inaktiverad och det går inte att lägga till boken i "Katalog"
