from outils import convertir_note, moyenne, mention
notes_brutes = ["12.5", "15", "abc", "18.25"]
notes = []
for texte in notes_brutes:
    note = convertir_note(texte)
    if note is not None:
        notes.append(note)
if notes:
    moy = moyenne(notes)
    print("Notes ignorées :", len(notes_brutes) - len(notes))
    print(f"Moyenne : {moy:.2f}")
    print("Mention :", mention(moy))
else:
    print("Aucune note valide")