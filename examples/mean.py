"""
Script para calcular el promedio de todas
las materias aprobadas de un estudiante.
"""
from statistics import mean

from ucuenca import Ucuenca


student_id = input('Cédula: ')

uc = Ucuenca()

for career in uc.careers(student_id):
    career_id = career['carrera_id']
    career_plan = career['placar_id']
    curriculum_id = career['malla_id']

    notes = [
        class_['nota_final']
        for class_ in uc.curriculum_progress(
            student_id,
            career_id,
            curriculum_id,
            career_plan
        )
        if class_['estado'] == 'APROBADO'
    ]
    msg = """
    Carrera: {career}
    Materias aprobadas: {num}
    Suma: {sum}
    Promedio: {mean}

    """.format(
        career=career['carrera'],
        num=len(notes),
        sum=sum(notes),
        mean=mean(notes)
    )
    print(msg)
