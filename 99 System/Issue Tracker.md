# Issue tracker: GitHub

Repo: `BleedingDev/jeste-nevim-pribehy-latecka`

## Wayfinder konvence

- Mapa je GitHub issue s labelem `wayfinder:map`.
- Decision ticket je issue s právě jedním labelem:
  - `wayfinder:grilling`
  - `wayfinder:research`
  - `wayfinder:prototype`
  - `wayfinder:task`
- Pokud ticket není připojen nativně jako sub-issue, první řádek body je `Part of #<map>`.
- Výsledek rozhodnutí patří jako resolution comment na ticket; mapa jen přidá krátký odkaz do `Decisions so far`.
- Neřešené, ale ještě nepřesně formulovatelné oblasti zůstávají v `Not yet specified` na mapě.
- Nativní GitHub dependencies jsou preferované pro blocking/frontier. Pokud je konkrétní klient neumí vytvořit, nevyráběj falešnou dependency strukturu; raději ticket ještě nevytvářej a nech oblast ve fog-of-war.

## Frontier

Frontier = otevřené, neblokované a nepřiřazené decision tickety mapy.

## Claim

Před řešením ticket přiřaď aktivnímu člověku/agentovi. Assignee znamená claim.

## Resolve

1. Přidej resolution comment.
2. Zavři ticket.
3. Do `Decisions so far` na mapě přidej jednu větu + odkaz.
4. Z odpovědi případně vytvoř nově zpřesněné tickety; zbytek nech jako fog.

## Důležité

Wayfinder plánuje. Implementace finálního vaultu přijde až po vyčištění setup mapy.
