'''
Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada uno de los n clubes debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de n/2​ simpatizantes en la comisión, y además queremos minimizar la cantidad simpatizantes a un mismo partido político; cada persona puede representar a solo un club, cada club debe estar representado por un miembro.

Implementar un modelo de programación lineal que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos permita obtener los representantes válidos, que además minimicen la cantidad de simpatizantes a un mismo partido político. Indicar la cantidad de inecuaciones definidas en el modelo.
'''

'''
- H_i: "Constante binaria, habitante i"
- PP: "Constante entera, partido politico"
- C: "Constante entera, club"

- X: "Constante entera, total de personas" -> \sum_{H = 0} H_i
- H-PP(H, PP): "Variable binaria, el habitante pertenence al partido politico dado" -> H + PP > 1
- H-C(H, C): "Variable binaria, el habitante pertenece al club dado"
'''