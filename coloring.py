from __future__ import print_function

from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('BARRANQUILLA', 'PUERTO COLOMBIA', 'TUBARA', 'GALAPA', 'MALAMBO', 'SOLEDAD', 'JUAN DE ACOSTA','BARANOA','USIACURI','POLONUEVO','SABANAGRANDE','SANTO TOMAS','PALMAR DE VALERA','PIOJO','LURUACO','SABANALARGA'
             ,'PONEDERA','REPELON','MANATI','CANDELARIA','SANTA LUCIA','CAMPO DE LA CRUZ','SUAN')

domains = dict((v, ['ROJO', 'VERDE', 'AZUL','AMARRILLO','GRIS','MORADO','NARANJA','MARRON','ROSADO']) for v in variables)

def const_different(variables, values):
    return values[0] != values[1]  # expect the value of the neighbors to be different

constraints = [
    (('BARRANQUILLA', 'PUERTO COLOMBIA'), const_different),
    (('BARRANQUILLA', 'TUBARA'), const_different),
    (('BARRANQUILLA', 'GALAPA'), const_different),
    (('BARRANQUILLA', 'MALAMBO'), const_different),
    (('BARRANQUILLA', 'SOLEDAD'), const_different),
    (('PUERTO COLOMBIA', 'TUBARA'), const_different),
    (('TUBARA', 'GALAPA'), const_different),
    (('TUBARA', 'JUAN DE ACOSTA'), const_different),
    (('TUBARA', 'BARANOA'), const_different),
    (('GALAPA', 'BARANOA'), const_different),
    (('GALAPA', 'MALAMBO'), const_different),
    (('MALAMBO', 'BARANOA'), const_different),
    (('MALAMBO', 'SOLEDAD'), const_different),
    (('MALAMBO', 'POLONUEVO'), const_different),
    (('MALAMBO', 'SABANAGRANDE'), const_different),
    (('JUAN DE ACOSTA', 'BARANOA'), const_different),
    (('JUAN DE ACOSTA', 'PIOJO'), const_different),
    (('JUAN DE ACOSTA', 'USIACURI'), const_different),
    (('BARANOA', 'POLONUEVO'), const_different),
    (('BARANOA', 'USIACURI'), const_different),
    (('BARANOA', 'SABANALARGA'), const_different),
    (('USIACURI', 'PIOJO'), const_different),
    (('USIACURI', 'SABANALARGA'), const_different),
    (('POLONUEVO', 'SABANALARGA'), const_different),
    (('POLONUEVO', 'PONEDERA'), const_different),
    (('POLONUEVO', 'SABANAGRANDE'), const_different),
    (('POLONUEVO', 'SANTO TOMAS'), const_different),
    (('SABANAGRANDE', 'SANTO TOMAS'), const_different),
    (('SANTO TOMAS', 'PALMAR DE VALERA'), const_different),
    (('SANTO TOMAS', 'PONEDERA'), const_different),
    (('PALMAR DE VALERA', 'PONEDERA'), const_different),
    (('PIOJO', 'LURUACO'), const_different),
    (('PIOJO', 'SABANALARGA'), const_different),
    (('LURUACO', 'REPELON'), const_different),
    (('LURUACO', 'SABANALARGA'), const_different),
    (('SABANALARGA', 'REPELON'), const_different),
    (('SABANALARGA', 'PONEDERA'), const_different),
    (('SABANALARGA', 'MANATI'), const_different),
    (('SABANALARGA', 'CANDELARIA'), const_different),
    (('PONEDERA', 'CANDELARIA'), const_different),
    (('PONEDERA', 'CAMPO DE LA CRUZ'), const_different),
    (('REPELON', 'MANATI'), const_different),
    (('MANATI', 'CANDELARIA'), const_different),
    (('MANATI', 'SANTA LUCIA'), const_different),
    (('MANATI', 'CAMPO DE LA CRUZ'), const_different),
    (('CANDELARIA', 'CAMPO DE LA CRUZ'), const_different),
    (('SANTA LUCIA', 'CAMPO DE LA CRUZ'), const_different),
    (('SANTA LUCIA', 'SUAN'), const_different),
    (('CAMPO DE LA CRUZ', 'SUAN'), const_different),    
]

my_problem = CspProblem(variables, domains, constraints)

#print(backtrack(my_problem))
#print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))
#print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))
#print(backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
#print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
#print(min_conflicts(my_problem))
