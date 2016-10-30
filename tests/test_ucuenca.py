import unittest

from ucuenca.ucuenca import Ucuenca
from ucuenca.ucuenca import UcuencaException


class GetCareersTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_careers(self):
        """Check 0104926787's careers."""
        student_id = '0104926787'
        expected_result = self._get_careers(student_id)
        actual_result = self.ucuenca.careers(student_id)
        self.assertEqual(expected_result, actual_result)

    def test_careers_invalid_student(self):
        """Check invalid student's careers."""
        student_id = '1234567890'
        result = self.ucuenca.careers(student_id)
        self.assertIsNone(result)

    def test_careers_lower_case_keys(self):
        """Check 0104926787's careers with lower case keys."""
        student_id = '0104926787'
        expected_result = self._get_careers(student_id)
        expected_result = {k.lower(): v for k, v in expected_result.items()}
        self.ucuenca.lowercase_keys = True
        actual_result = self.ucuenca.careers(student_id)
        self.assertEqual(expected_result, actual_result)

    def _get_careers(self, student_id):
        academic_records = {
            '0104926787': {"PERSONA_ID":"0104926787","NOMBRE":"ALVAREZ BARROS PAOLA KATHERINE","MALLA":"MALLA CONTABILIDAD Y AUDITORIA 2008","PLACAR_ID":4,"FECHA_MATRICULA":"2013-03-03 09:37:08.0","SECCION":"GENERAL","ESTADO_MATRICULA":"MATRICULADO","ESTA_ANULADA":"N","CARRERA_ID":44,"PERIODO_LECTIVO":"MARZO2013-AGOSTO2013","CARRERA":"CONTABILIDAD Y AUDITORIA","NIVEL_NUMERO":6,"PERLEC_ID":108,"NRO_MATRICULA":8151,"FACULTAD":"FACULTAD DE CIENCIAS ECON&Oacute;MICAS Y ADMINISTRATIVAS","SECCIONID":4,"ESGRATUITA":"NO","MALLA_ID":1,"PLAN_CARRERA":"PLAN CONTABILIDAD Y AUDITORIA 2008"}
        }
        return academic_records[student_id]


class GetNotesTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    @unittest.expectedFailure
    def test_notes(self):
        """Check 0302068309's notes."""
        student_id = '0302068309'
        career_id = 16
        perdiod_id = 115
        expected_result = {}  # TODO
        actual_result = self.ucuenca.notes(student_id, career_id, perdiod_id)
        self.assertEqual(actual_result, expected_result)

    def test_notes_invalid_student(self):
        """Check invalid student's notes."""
        student_id = '1234567890'
        career_id = 34
        perdiod_id = 115
        result = self.ucuenca.notes(student_id, career_id, perdiod_id)
        self.assertIsNone(result)


class GetScheduleTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_schedule(self):
        """Check 0104378690's schedule."""
        student_id = '0104378690'
        expected_result = self._get_schedule(student_id)
        actual_result = self.ucuenca.schedule(student_id)
        self.assertEqual(actual_result, expected_result)

    def test_careers_invalid_student(self):
        """Check invalid student's schedule."""
        student_id = '1234567890'
        result = self.ucuenca.schedule(student_id)
        self.assertIsNone(result)

    def _get_schedule(self, student_id):
        schedules = {
            '0104378690': {"ARQUITECTURA":[{"HORA_FIN":"13:00","NOMBRE_DOCENTE":"MARIA SOLEDAD MOSCOSO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":1,"HORA_INICIO":"11:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"JAIME SEBASTIAN ASTUDILLO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":1,"HORA_INICIO":"09:00"},{"HORA_FIN":"12:00","NOMBRE_DOCENTE":"MARIA SOLEDAD MOSCOSO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":2,"HORA_INICIO":"10:00"},{"HORA_FIN":"10:00","NOMBRE_DOCENTE":"JAIME SEBASTIAN ASTUDILLO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":2,"HORA_INICIO":"08:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"JAIME SEBASTIAN ASTUDILLO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":3,"HORA_INICIO":"09:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"FAUSTO ADRIAN  CARDOSO MARTINEZ ","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":3,"HORA_INICIO":"09:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"MARIA SOLEDAD MOSCOSO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":3,"HORA_INICIO":"09:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"FAUSTO ADRIAN  CARDOSO MARTINEZ ","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":4,"HORA_INICIO":"09:00"},{"HORA_FIN":"11:00","NOMBRE_DOCENTE":"MARIA SOLEDAD MOSCOSO CORDERO","ASIGNATURA":"TALLER INTEGRAL 2 OPCION RESTAURACION","COD_GRUPO":1,"DIA":5,"HORA_INICIO":"09:00"},{"ESP_FISICOABREV":"C102","ESP_FISICOID":94,"HORA_FIN":"13:00","NOMBRE_DOCENTE":"OSWALDO HONORIO CORDERO DOMINGUEZ","ASIGNATURA":"TIP TESIS RESTAURACION URBANA ARQUITECTONICA","COD_GRUPO":1,"DIA":3,"ESP_FISICONOMBRE":"AULA C102","HORA_INICIO":"11:00"},{"ESP_FISICOABREV":"B204","ESP_FISICOID":85,"HORA_FIN":"13:00","NOMBRE_DOCENTE":"OSWALDO HONORIO CORDERO DOMINGUEZ","ASIGNATURA":"TIP TESIS RESTAURACION URBANA ARQUITECTONICA","COD_GRUPO":1,"DIA":4,"ESP_FISICONOMBRE":"AULA B204","HORA_INICIO":"11:00"},{"ESP_FISICOABREV":"B201","ESP_FISICOID":84,"HORA_FIN":"13:00","NOMBRE_DOCENTE":"OSWALDO HONORIO CORDERO DOMINGUEZ","ASIGNATURA":"TIP TESIS RESTAURACION URBANA ARQUITECTONICA","COD_GRUPO":1,"DIA":5,"ESP_FISICONOMBRE":"AULA B201","HORA_INICIO":"11:00"}]}
        }
        return schedules[student_id]
