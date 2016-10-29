import unittest

from ucuenca.ucuenca import Ucuenca
from ucuenca.ucuenca import UcuencaException


class TestUcuenca(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_academic_record(self):
        """Check 0104926787's academic_record."""
        student_id = '0104926787'
        expected_result = self._get_academic_record(student_id)
        actual_result = self.ucuenca.academic_record(student_id)
        self.assertEqual(expected_result, actual_result)

    def test_academic_record_invalid_student(self):
        """Check invalid student's academic record."""
        student_id = '1234567890'
        with self.assertRaises(UcuencaException) as e:
            self.ucuenca.academic_record(student_id)
        self.assertEqual(404, e.exception.status_code)

    def test_academic_record_lower_case_keys(self):
        """Check 0104926787's academic_record with lower case keys."""
        student_id = '0104926787'
        expected_result = self._get_academic_record(student_id)
        expected_result = {k.lower(): v  for k, v in expected_result.items()}
        self.ucuenca.lowercase_keys = True
        actual_result = self.ucuenca.academic_record(student_id)
        self.assertEqual(expected_result, actual_result)


    def _get_academic_record(self, student_id):
        academic_records = {
            '0104926787': {"PERSONA_ID":"0104926787","NOMBRE":"ALVAREZ BARROS PAOLA KATHERINE","MALLA":"MALLA CONTABILIDAD Y AUDITORIA 2008","PLACAR_ID":4,"FECHA_MATRICULA":"2013-03-03 09:37:08.0","SECCION":"GENERAL","ESTADO_MATRICULA":"MATRICULADO","ESTA_ANULADA":"N","CARRERA_ID":44,"PERIODO_LECTIVO":"MARZO2013-AGOSTO2013","CARRERA":"CONTABILIDAD Y AUDITORIA","NIVEL_NUMERO":6,"PERLEC_ID":108,"NRO_MATRICULA":8151,"FACULTAD":"FACULTAD DE CIENCIAS ECON&Oacute;MICAS Y ADMINISTRATIVAS","SECCIONID":4,"ESGRATUITA":"NO","MALLA_ID":1,"PLAN_CARRERA":"PLAN CONTABILIDAD Y AUDITORIA 2008"}
        }
        return academic_records[student_id]
