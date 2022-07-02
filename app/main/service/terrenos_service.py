from statistics import mean

from app.main import db
from app.main.model.terrenos import Terreno


def get(type_, zip_code, uso_construccion):
    result = Terreno.query.filter_by(codigo_postal=zip_code, uso_construccion=uso_construccion).all()

    price_unit = None
    price_unit_construction = None

    if type_ == 'min':
        price_unit = min(result, key=lambda e: e.price_unit).price_unit
        price_unit_construction = min(result, key=lambda e: e.price_unit_construction).price_unit_construction
    elif type_ == 'max':
        price_unit = max(result, key=lambda e: e.price_unit).price_unit
        price_unit_construction = max(result, key=lambda e: e.price_unit_construction).price_unit_construction
    else:
        price_unit = mean((e.price_unit for e in result))
        price_unit_construction = mean((e.price_unit_construction for e in result))

    object_result = {
        'status': True,
        'payload': {
            'type': type_,
            'price_unit': price_unit,
            'price_unit_construction': price_unit_construction,
            'elements': len(result)
        }
    }

    print(object_result)

    return object_result, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()
