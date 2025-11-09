'''
Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada uno de los n clubes debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de n/2 simpatizantes en la comisión, y además queremos minimizar la cantidad simpatizantes a un mismo partido político; cada persona puede representar a solo un club, cada club debe estar representado por un miembro.

Implementar un modelo de programación lineal que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos permita obtener los representantes válidos, que además minimicen la cantidad de simpatizantes a un mismo partido político. Indicar la cantidad de inecuaciones definidas en el modelo.
'''

'''
- $H_i$: "Constante binaria, habitante $i$"
- $R_i$: "Variable binaria, el habitante $i$ es representante"
- $N$: "Constante entera, numero de clubes"
- $M_{PP}$: "Variable entera, cantidad máxima de representantes de un partido politico"

- $H-PP(H_i, PP)$: "Constante binaria, el habitante pertenence al partido politico dado"
- $H-C(H_i, C)$: "Constante binaria, el habitante pertenece al club dado"

$\min(M)$ -> Buscamos minimizar la cantidad de simpatizantes a un mismo partido político

Donde:  
    - $\sum_{i = 0}^{n} H-PP(H_i, PP) * R_i \le M$ -> (para todo $PP$)  
    - $\sum_{i = 0}^{n} H-PP(H_i, PP) * R_i \le N/2$ -> constante * variable (para todo $PP$)  
    - $\sum_{i = 0}^{n} H-C(H_i, C) * R_i = 1$ -> (para todo $C$)  
'''