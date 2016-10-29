import unittest

from ucuenca.ucuenca import Ucuenca
from ucuenca.ucuenca import UcuencaException


class TestUcuenca(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_academic_record(self):
        """Check 0706455136's academic_record."""
        student_id = '0706455136'
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
        """Check 0706455136's academic_record with lower case keys."""
        student_id = '0706455136'
        expected_result = self._get_academic_record(student_id)
        expected_result = {k.lower(): v  for k, v in expected_result.items()}
        self.ucuenca.lowercase_keys = True
        actual_result = self.ucuenca.academic_record(student_id)
        self.assertEqual(expected_result, actual_result)


    def _get_academic_record(self, student_id):
        academic_records = {
            '0706455136': {"PERSONA_ID":"0706455136","NOMBRE":"GALLEGOS CEVILLA SANTOS EDUARDO","MALLA":"MALLA MODERNA SISTEMAS 2013","PLACAR_ID":1,"FECHA_MATRICULA":"2016-08-30 12:59:18.0","SECCION":"GENERAL","ESTADO_MATRICULA":"MATRICULADO","ESTA_ANULADA":"N","CARRERA_ID":37,"PERIODO_LECTIVO":"SEPTIEMBRE 2016-FEBRERO 2017","CARRERA":"INGENIERIA DE SISTEMAS","NIVEL_NUMERO":2,"PERLEC_ID":115,"NRO_MATRICULA":13074,"FACULTAD":"FACULTAD DE INGENIER&Iacute;A","SECCIONID":4,"ESGRATUITA":"SI","MALLA_ID":7,"PLAN_CARRERA":"PLAN DE CARRERA DE SISTEMAS CREDITOS 2008"}
        }
        return academic_records[student_id]
