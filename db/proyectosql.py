def cantidadPoblacion():
    return """select poblacion, sum(cantidad_personas) as cantidad
from beneficiados
group by poblacion;"""

def cantidadMeses():
    return """select a.mes, sum(b.cantidad_personas) as cantidad
from beneficiados b left join avances a on b.avance = a.codigo
group by mes;"""

def cantidadEdad():
    return """select genero, sum(cantidad_personas) as cantidad,
	case
		when edad > 0
			and edad <= 5 then '0-5 años'
		when edad > 5
			and edad <= 12 then '6-12 años'
		when edad > 12
			and edad <= 17 then '12-17 años'
		when edad > 17
			and edad <= 29 then '18-29 años'
		when edad > 29
			and edad <= 59 then '30-59 años'
		when edad > 60 then 'mayor de 60 años'
	end rango
from beneficiados
group by rango, genero;"""

def cantidadDeporte():
    return """SELECT distinct deporte,
 sum(cantidad_sesiones_mes) OVER (
 PARTITION BY deporte
 RANGE UNBOUNDED PRECEDING) total
FROM avances;"""

def cantidadProvincia():
    return """select distinct p.nombre, sum(bn.cantidad_personas)
from (((avances a left join beneficiados bn on bn.avance = a.codigo)
	    left join barrio_vereda b on a.zona = b.codigo) 
		left join municipio m on b.municip = m.codigo)
		left join provincia p on m.provinc = p.codigo
group by p.nombre;"""

def cantidadProg1():
    return """select * from get_programa_personas(1);"""

def cantidadProg2():
    return """select * from get_programa_personas(2);"""

def cantidadProg3():
    return """select * from get_programa_personas(3);"""
