# User story 3:
# Som en användare
# vill jag kunna favoritmarkera böcker i katalogen
# så att jag kan lägga till böcker i vyn "Mina böcker"

# Acceptanskriterier:
# - När användaren klickar på hjärtat ska hjärtat framträda och boken läggas till i vyn "Mina böcker".

Feature: Favoritmarkera för att lägga böcker till "Mina böcker"
  Som en användare
  vill jag kunna favoritmarkera böcker i katalogen
  så att jag kan lägga till böcker i vyn "Mina böcker"

    Scenario: Favoritmarkera en bok
      Given användaren navigerar till startsidan
      When användaren klickar på hjärtikonen bredvid första boken
      Then boken favoritmarkeras genom att hjärtat framträder
      And den favoritmarkerade boken läggs till i vyn "Mina böcker
