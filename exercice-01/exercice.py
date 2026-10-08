produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2
total_ht = prix_ht*quantite
total_ttc = total_ht+taux_tva*total_ht
print(f"{quantite} * {produit} : {total_ttc} euros TTC")

prix_texte = "19.90"
total_ht_2 = float(prix_texte)*quantite
total_ttc_2 = total_ht+taux_tva*total_ht
print(f"{quantite} * {produit} : {total_ttc_2} euros TTC")

