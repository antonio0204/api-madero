import unittest
import datetime

from app.main import db
from app.main.model.terrenos import Terreno
from app.test.base import BaseTestCase

from app.main.service.terrenos_service import get


class TestUserModel(BaseTestCase):

    def test_min_codigo_postal_construction_type(self):
        codigo_postal = 7320
        aggregate = 'min'
        construction_types = {
            1: 'Áreas verdes',
            2: 'Centro de barrio',
            3: 'Equipamiento',
            4: 'Habitacional',
            5: 'Habitacional y comercial',
            6: 'Industrial',
            7: 'Sin Zonificación'
        }
        construction_type = construction_types[7]

        resultado, status = get(aggregate, codigo_postal, construction_type)

        self.assertTrue(status == 201)
        self.assertTrue(resultado['status'])
        self.assertTrue(resultado['payload']['type'] == 'min')


if __name__ == '__main__':
    unittest.main()
