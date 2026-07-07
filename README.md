# eprints-pnrr

Genera la lista dei progetti PNRR, per il popolamento automatico del campo finanzimento per [EPrints](https://eprints.org).

La lista dei progetti `progetti.csv` deve essere scaricata da [OpenPNRR](https://openpnrr.it/opendata/) e copiata nella cartella `data/`.

Il formato del file di output è modellato sull'esempio delle [API di OpenAIRE per EPRints e DSpace](https://graph.openaire.eu/docs/apis/dspace-eprints-api)

## Mappatura dei campi

Le colonne del file `data/progetti.csv` sono stati mappati nel formato:

```
info:eu-repo/grantAgreement/Funder/FundingProgram/ProjectID/[Jurisdiction]/[ProjectName]/[ProjectAcronym]
```

- Funder è "EC"
- FundingProgram è "Next Generation Europe - PNRR - `descrizione`"
- Project id è il `cup`
- Jurisdiction è "IT"
- ProjectName è preso dal primo e dall'ultimo dei campi separati da "*" della colonna `titolo`.
- ProjectAcronym è il campo `progetto_id`

## Uso

Questo progetto utilizza [uv](https://github.com/astral-sh/uv) per la gestione delle dependency.

1. Installa uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Installa le dependencies: `uv sync`
3. Lancia lo script: `uv run eprint-pnrr.py`

## Licenza

Il codice è rilasciato con licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)