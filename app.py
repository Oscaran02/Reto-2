def cliente(info: dict) -> dict:
    new_value = {"nombre": "", "edad": 0, "atraccion": "", "apto": False, "primer_ingreso": False, "total_boleta": 0.0}

    if info['edad'] > 18:
        new_value['apto'] = True
        if info['primer_ingreso']:
            new_value['total_boleta'] = 20000 - (20000 * 0.05)
        else:
            new_value['total_boleta'] = 20000
        new_value['atraccion'] = "X-Treme"

    elif 15 <= info['edad'] <= 18:
        new_value['apto'] = True
        if info['primer_ingreso']:
            new_value['total_boleta'] = 5000 - (5000 * 0.07)
        else:
            new_value['total_boleta'] = 5000
        new_value['atraccion'] = "Carros chocones"

    elif 7 <= info['edad'] < 15:
        new_value['apto'] = True
        if info['primer_ingreso']:
            new_value['total_boleta'] = 10000 - (10000 * 0.05)
        else:
            new_value['total_boleta'] = 10000
        new_value['atraccion'] = "Sillas voladoras"

    else:
        new_value['apto'] = False
        new_value['atraccion'] = "N/A"
        new_value['total_boleta'] = "N/A"

    new_value['primer_ingreso'] = info['primer_ingreso']
    new_value['nombre'] = info['nombre']
    new_value['edad'] = info['edad']
    return new_value

