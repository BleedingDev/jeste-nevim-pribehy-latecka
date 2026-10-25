# Obsidian bootstrap

Toto jsou pouze kroky nutné pro práci na setup Wayfinderu. Finální plugin stack a vault taxonomie jsou zatím otevřené rozhodnutí.

## 1. Otevření vaultu

Naklonuj repozitář a v Obsidianu zvol **Open folder as vault** na jeho kořen.

## 2. Wayfinder Maps

V Obsidianu:

1. Settings → Community plugins → Browse.
2. Najdi **Wayfinder Maps** a nainstaluj ho.
3. V GitHubu vytvoř fine-grained PAT omezený na tento repo s read-only přístupem k Issues.
4. V Settings → Wayfinder Maps nastav repo `BleedingDev/jeste-nevim-pribehy-latecka` a vlož PAT.
5. Otevři Wayfinder view přes příkaz nebo compass ikonu.

**Důležité:** Wayfinder Maps ukládá token do `.obsidian/plugins/wayfinder-maps/data.json`. Tento soubor je v `.gitignore` a nesmí se commitnout.

## 3. Git

Repo už je Git repozitář. Způsob synchronizace (CLI, GitHub Desktop, Obsidian Git, jiný klient) je součást setup rozhodnutí; teď není potřeba instalovat další plugin.

## 4. Práce během setup mapy

- vstupní nápady → `00 Inbox`;
- rozhodnutí → GitHub Wayfinder issues;
- systémové instrukce → `99 System`;
- finální složky pro postavy/svět/scény vytvoříme až po vyčištění mapy #1.
