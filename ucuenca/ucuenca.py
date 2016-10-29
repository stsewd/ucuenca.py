import json
import time
import requests


class UcuencaException(Exception):
    def __init__(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg

    def __str__(self):
        return "status code: {status_code} - {msg}".format(
            status_code=self.status_code,
            msg=self.msg,
        )


class Ucuenca:
    base_url = "http://evaluacion.ucuenca.edu.ec/ucuenca-rest-ws/api/v1/"
    max_retries = 10

    def __init__(self, token=None):
        self.token = token

    def _get(self, url, params=None):
        retries = Ucuenca.max_retries
        delay = 0.5

        while retries:
            try:
                return self._get_response(url, params)
            except UcuencaException as e:
                if retries == 1 or e.status_code == 404:
                    raise e
            except Exception:
                if retries == 1:
                    raise UcuencaException(0, "Unknow error.")
            retries -= 1
            time.sleep(delay)
            delay += 0.5

    def _get_response(self, url, params):
        response = requests.get(url, params)
        status_code = response.status_code
        if status_code != 200:
            raise UcuencaException(status_code, "Error")
        elif not response.json():
            raise UcuencaException(404, "Resource not found.")
        return response

    def _get_url(self, field):
        return "{}{}".format(Ucuenca.base_url, field)

    def _parse_response(self, response):
        return response.json()

    def academic_record(self, student_id):
        url = self._get_url('registroacademico')
        response = self._get(
            url,
            params={'idEstudiante': student_id}
        )
        return self._parse_response(response)
