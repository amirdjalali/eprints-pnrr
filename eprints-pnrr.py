import pandas as pd
from pathlib import Path

pnrr_df = pd.read_csv("data/progetti.csv")
out_path = Path("out/progetti_pnrr_eprints.html")

pnrr_list = []
i = 0
n_projects = len(pnrr_df)

SMALL = {
    "A","AD","AL","ALLO","ALLA","AGLI","ALLE",
    "D", "DA","DAL","DALLO","DALLA","DAGLI","DALLE",
    "DI","DEL","DELLO","DELLA","DEI","DEGLI","DELLE", "DELL'"
    "IN","NEL","NELLO","NELLA","NEI","NEGLI","NELLE",
    "SU","SUL","SULLO","SULLA","SUI","SUGLI","SULLE",
    "IL", "LA", "LO", "I", "GLI", "LE", "L'"
    "TRA","FRA",
    "CON","PER","PRO","CONTRO",
    "E","O","MA","NÉ","NE","ANCHE","PURE",
    "CHE","CUI",
}

def italian_title_case(input_string: str) -> str:
    tokens = input_string.split(" ")
    out_tokens = []
    for token in tokens:
        if token not in SMALL:
            out_tokens.append(token.title())
        else:
            out_tokens.append(token.lower())
    return " ".join(out_tokens)

for idx, row in pnrr_df.iterrows():
    i += 1
    title_parts = row["titolo"].split("*")
    nice_title = f"{italian_title_case(title_parts[0])} - {italian_title_case(title_parts[-1])}"
    print(f"parsing project {i} of {n_projects}", end="\r")
    project = f"""{row["progetto_id"]} - {nice_title}&#9;<li style='border-right: solid 50px #30FF30' >{row["cup"]} - {row["progetto_id"]} - {nice_title}<ul><li id="for:value:component:_wt_project_id">info:eu-repo/grantAgreement/EC/Next Generation Europe - PNRR - {row["descrizione"]}/{row["cup"]}/IT</li></ul></li>\n"""
    pnrr_list.append(project)

print(f"\nDone parsing {len(pnrr_list)} projects!")

i = 0

out_path.parent.mkdir(parents=True, exist_ok=True)
with out_path.open("w", encoding="utf-8") as f: 
    for project in pnrr_list:
        i += 1
        print(f"Writing project {i} of {n_projects}", end="\r")
        f.write(project)

f.close()

print(f"\nDone writing {len(pnrr_list)} projects!")