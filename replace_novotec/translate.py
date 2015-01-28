# -*- coding: utf-8 -*-
import os, re
import ntpath

txts_es = {"login":"login-tr",
"Usuario":"Usuario-tr",
"Contraseña":"Contraseña-tr",
"Aceptar":"Aceptar-tr",
"Cargar facturas":"Cargar facturas-tr",
"ESPAÑOL":"ESPAÑOL-tr",
"INGLÉS":"INGLÉS-tr",
"DESCONECTARSE":"DESCONECTARSE-tr",
"Carga de facturas":"Carga de facturas-tr",
"Ubicación":"Ubicación-tr",
"CARGAR FACTURAS":"CARGAR FACTURAS-tr",
"Consultar facturas":"Consultar facturas-tr",
"RECLAMACIÓN":"RECLAMACIÓN-tr",
"CARGA":"CARGA-tr",
"Filtro de búsqueda":"Filtro de búsqueda-tr",
"Código cliente":"Código cliente-tr",
"Responsable SCO Applus":"Responsable SCO Applus-tr",
"Próxima acción":"Próxima acción-tr",
"Departamento:":"Departamento:-tr",
"Fecha próxima acción":"Fecha próxima acción-tr",
"LIMPIAR":"LIMPIAR-tr",
"BUSCAR":"BUSCAR-tr",
"CÓD. CL":"CÓD. CL-tr",
"NOMBRE CLIENTE":"NOMBRE CLIENTE-tr",
"CIF/NIF":"CIF/NIF-tr",
"RESULTADO ACCIÓN":"RESULTADO ACCIÓN-tr",
"IMPORTE":"IMPORTE-tr",
"Nº FACTURA":"Nº FACTURA-tr",
"F. VENCIMIENTO":"F. VENCIMIENTO-tr",
"DEPARTAMENTO":"DEPARTAMENTO-tr",
"COBRA, INSTAL Y SERV. S.A":"COBRA, INSTAL Y SERV. S.A-tr",
"A12345678":"A12345678-tr",
"Falta documentación de la factura":"Falta documentación de la factura-tr",
"BUIET ELECTRICO NO":"BUIET ELECTRICO NO-tr",
"COBRA, INSTAL Y SERV. S.A":"COBRA, INSTAL Y SERV. S.A-tr",
"EXPORTAR RESULTADO":"EXPORTAR RESULTADO-tr",
"Cliente / departamento / proyecto":"Cliente / departamento / proyecto-tr",
"Facturas":"Facturas-tr",
"VER DETALLE":"VER DETALLE-tr",
"Código":"Código-tr",
"Nombre":"Nombre-tr",
"Horario contacto":"Horario contacto-tr",
"Llamar tardes":"Llamar tardes-tr",
"CIF/NIF":"CIF/NIF-tr",
"N. descriptivo":"N. descriptivo-tr",
"Plazo de pago":"Plazo de pago-tr",
"Teléfono":"Teléfono-tr",
"E-mail":"E-mail-tr",
"Día de pago":"Día de pago-tr",
"Comentarios":"Comentarios-tr",
"ACTUALIZAR":"ACTUALIZAR-tr",
"departamento / proyecto":"departamento / proyecto-tr",
"Código":"Código-tr",
"Nombre":"Nombre-tr",
"Zona":"Zona-tr",
"Cód. proyecto":"Cód. proyecto-tr",
"Descripción proyecto":"Descripción proyecto-tr",
"División":"División-tr",
"Nº Jefe":"Nº Jefe-tr",
"Nombre jefe de proyecto":"Nombre jefe de proyecto-tr",
"Datos de la factura":"Datos de la factura-tr",
"Referencia":"Referencia-tr",
"Identificador":"Identificador-tr",
"Fecha":"Fecha-tr",
"Fecha vencimiento":"Fecha vencimiento-tr",
"Importe":"Importe-tr",
"Texto factura":"Texto factura-tr",
"Última acción sobre la factura":"Última acción sobre la factura-tr",
"Acción saliente":"Acción saliente-tr",
"Fecha acción salientes":"Fecha acción salientes-tr",
"Próxima acción":"Próxima acción-tr",
"Fecha próxima acción":"Fecha próxima acción-tr",
"Resultado acción saliente":"Resultado acción saliente-tr",
"Texto acción":"Texto acción-tr",
"Acciones sobre la factura":"Acciones sobre la factura-tr",
"ACCIÓN SALIENTE":"ACCIÓN SALIENTE-tr",
"F. ACCIÓN SALIENTE":"F. ACCIÓN SALIENTE-tr",
"PRÓXIMA ACCIÓN":"PRÓXIMA ACCIÓN-tr",
"F. PRÓXIMA ACCIÓN":"F. PRÓXIMA ACCIÓN-tr",
"TEXTO ACCIÓN":"TEXTO ACCIÓN-tr",
"ADJUNTOS":"ADJUNTOS-tr",
"Llamada saliente":"Llamada saliente-tr",
"Falta documentación de la factura. Se pide confirmación":"Falta documentación de la factura. Se pide confirmación-tr",
"Nueva acción sobre la factura":"Nueva acción sobre la factura-tr",
"Acción saliente":"Acción saliente-tr",
"Fecha acción saliente":"Fecha acción saliente-tr",
"Resultado acción saliente":"Resultado acción saliente-tr",
"Próxima acción":"Próxima acción-tr",
"Fecha próxima acción":"Fecha próxima acción-tr",
"Comentarios":"Comentarios-tr",
"CREAR ACCIÓN":"CREAR ACCIÓN-tr"}

txts = {}

def set_texts(t):
    global txts
    txts = t

def get_matched_txt(txt):
    for key in txts:
        if re.search(key, txt):
            return key
    return ""

def swap_lines(line):
    matched = get_matched_txt(line)
    if matched != "":
        return line.replace( matched, txts[matched])
    return line

def change_file_lang(fil):
    outputdir = "outputfiles"
    name = ntpath.basename(fil)
    if not os.path.exists(outputdir):
        os.mkdir(outputdir)
    new_file = open(os.path.join(outputdir, name), "w+")
    with open(fil) as f:
        for line in f:
            new_file.write(swap_lines(line))
    new_file.close()



def iter_txts():
    for key in txts:
        print key, txts[key]

if __name__ == '__main__':
    set_texts(txts_es)
    p = "files"
    for file in os.listdir(p):
        change_file_lang(os.path.join(p, file))


    """
    if get_matched_txt(txt):
        print txt.replace( "Resultado acción saliente", "output action result"   )


    for file in os.listdir(p):
        read_file(os.path.join(p, file))
    #iter_txts()
    """