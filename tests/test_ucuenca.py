import unittest
import json
import os

from ucuenca.ucuenca import Ucuenca
from ucuenca.ucuenca import UcuencaException

TEST_RESOURCES = os.path.join(os.path.dirname(__file__), "..", "tests_resources")


class GetCareersTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_careers(self):
        """Check 0104926787's careers."""
        student_id = '0104926787'
        expected_result = self._get_careers()
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
        expected_result = self._get_careers()
        expected_result = {k.lower(): v for k, v in expected_result.items()}
        self.ucuenca.lowercase_keys = True
        actual_result = self.ucuenca.careers(student_id)
        self.assertEqual(expected_result, actual_result)

    def _get_careers(self):
        path = os.path.join(TEST_RESOURCES, "careers.json")
        with open(path) as f:
            json_file = json.load(f)
        return json_file[0]


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
        expected_result = self._get_schedule()
        actual_result = self.ucuenca.schedule(student_id)
        self.assertEqual(actual_result, expected_result)

    def test_careers_invalid_student(self):
        """Check invalid student's schedule."""
        student_id = '1234567890'
        result = self.ucuenca.schedule(student_id)
        self.assertIsNone(result)

    def _get_schedule(self):
        path = os.path.join(TEST_RESOURCES, "schedule.json")
        with open(path) as f:
            json_file = json.load(f)
        return json_file[0]


class GetCurriculumProgressTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_curriculum_progress(self):
        """Check 0104926787's curriculum progress."""
        student_id = '0104926787'
        career_id = 44
        curriculum_id = 1
        career_plan = 4
        expected_result = self._get_curriculum_progress()
        actual_result = self.ucuenca.curriculum_progress(
            student_id, career_id, curriculum_id, career_plan
        )
        self.assertEqual(actual_result, expected_result)

    def test_curriculum_progress_invalid_student(self):
        """Check invalid student's curriculum progress."""
        student_id = '1234567890'
        career_id = 44
        curriculum_id = 1
        career_plan = 4
        result = self.ucuenca.curriculum_progress(
            student_id, career_id, curriculum_id, career_plan
        )
        self.assertIsNone(result)

    def _get_curriculum_progress(self):
        path = os.path.join(TEST_RESOURCES, "curriculum_progress.json")
        with open(path) as f:
            json_file = json.load(f)
        return json_file


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.ucuenca = Ucuenca()

    def test_bad_password(self):
        """Check authentication with a bad password."""
        user = 'santos.gallegos'
        passw = '1234'
        self.ucuenca.lowercase_keys = True
        result = self.ucuenca.authentication(user, passw)
        self.assertFalse(result['autenticacion'])
