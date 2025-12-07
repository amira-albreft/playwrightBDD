# User story 4:
# Som en användare
# vill jag kunna ta bort favoritmarkering på böcker i katalogen
# så att jag kan ta bort dem från vyn "Mina böcker"

# Acceptanskriterier:
# - När användaren favoritmarkerat en bok så ska användaren kunna klicka på hjärtat för att ta bort favoritmarkeringen.
# - När användaren klickar på det mörkröda hjärtat ska hjärtat försvinna och boken tas bort från vyn "Mina böcker".


Feature: Ta bort favoritmarkering från böcker i "Mina böcker"
  Som en användare
  vill jag kunna ta bort favoritmarkering på böcker i katalogen
  så att jag kan ta bort dem från vyn "Mina böcker"

  Scenario: Ta bort favoritmarkering från en bok
    Given användaren har favoritmarkerat en bok i katalogen
    When användaren klickar på hjärtikonen bredvid boken
    Then boken tas bort från vyn "Mina böcker"