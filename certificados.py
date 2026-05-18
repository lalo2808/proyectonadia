# certificados.py
# ------------------------------------------------------------
# Cursos de Regularización CECyTEM
# Generador de certificados PDF
# Compatible con:
# Python 3.11.9
# ReportLab
# ------------------------------------------------------------

import os
from datetime import datetime

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, grey
from reportlab.pdfgen import canvas

from utilidades import (
    LOGO_CECYTEM,
    FONDO_CERTIFICADO,
    ruta_certificado_modulo,
    ruta_certificado_curso,
    generar_folio,
    generar_hash_certificado,
    eliminar_archivo,
    fecha_formateada,
)


COLOR_AZUL = HexColor("#0B3C73")
COLOR_DORADO = HexColor("#C8A75D")
COLOR_GRIS = HexColor("#666666")


def dibujar_marco(pdf, width, height):
    """
    Marco decorativo premium.
    """
    pdf.setStrokeColor(COLOR_DORADO)
    pdf.setLineWidth(6)
    pdf.rect(1.2 * cm, 1.2 * cm, width - 2.4 * cm, height - 2.4 * cm)

    pdf.setStrokeColor(COLOR_AZUL)
    pdf.setLineWidth(2)
    pdf.rect(1.6 * cm, 1.6 * cm, width - 3.2 * cm, height - 3.2 * cm)


def dibujar_fondo(pdf, width, height):
    """
    Fondo opcional.
    """
    if os.path.exists(FONDO_CERTIFICADO):
        try:
            pdf.drawImage(
                FONDO_CERTIFICADO,
                0,
                0,
                width=width,
                height=height,
                preserveAspectRatio=False,
                mask='auto'
            )
        except Exception:
            pass


def dibujar_sello(pdf, width, height):
    """
    Logo como sello y marca de agua.
    """
    if not os.path.exists(LOGO_CECYTEM):
        return

    try:
        # Marca de agua central
        pdf.saveState()
        pdf.setFillAlpha(0.08)

        size = 8 * cm
        x = (width / 2) - (size / 2)
        y = (height / 2) - (size / 2)

        pdf.drawImage(
            LOGO_CECYTEM,
            x,
            y,
            width=size,
            height=size,
            mask='auto'
        )

        pdf.restoreState()

        # Sello esquina
        pdf.drawImage(
            LOGO_CECYTEM,
            width - 5 * cm,
            2 * cm,
            width=2.5 * cm,
            height=2.5 * cm,
            mask='auto'
        )

    except Exception:
        pass


def dibujar_encabezado(pdf, width, titulo):
    """
    Encabezado institucional.
    """
    pdf.setFillColor(COLOR_AZUL)
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(width / 2, 18 * cm, titulo)

    pdf.setFillColor(COLOR_GRIS)
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        width / 2,
        17 * cm,
        "Plataforma Académica de Refuerzo Educativo"
    )


def dibujar_firma(pdf, width):
    """
    Firma decorativa.
    """
    x = width / 2

    pdf.setStrokeColor(black)
    pdf.line(x - 3 * cm, 3.5 * cm, x + 3 * cm, 3.5 * cm)

    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(x, 3 * cm, "Dirección Académica")
    pdf.drawCentredString(x, 2.4 * cm, "Cursos de Regularización CECyTEM")


def generar_certificado_modulo(
    nombre_alumno,
    curso,
    modulo,
    calificacion,
    ruta_anterior=None
):
    """
    Genera certificado de módulo.
    """
    if ruta_anterior:
        eliminar_archivo(ruta_anterior)

    ruta_pdf = ruta_certificado_modulo(
        nombre_alumno,
        curso,
        modulo
    )

    folio = generar_folio("MOD")
    hash_cert = generar_hash_certificado(
        nombre_alumno,
        curso,
        modulo,
        calificacion,
        folio
    )

    width, height = landscape(A4)
    pdf = canvas.Canvas(ruta_pdf, pagesize=landscape(A4))

    # Fondo
    dibujar_fondo(pdf, width, height)

    # Marco
    dibujar_marco(pdf, width, height)

    # Sello
    dibujar_sello(pdf, width, height)

    # Encabezado
    dibujar_encabezado(pdf, width, "Cursos de Regularización CECyTEM")

    # Título
    pdf.setFillColor(COLOR_DORADO)
    pdf.setFont("Helvetica-Bold", 30)
    pdf.drawCentredString(width / 2, 14.7 * cm, "CERTIFICADO DE ACREDITACIÓN")

    # Texto principal
    pdf.setFillColor(black)
    pdf.setFont("Helvetica", 18)
    pdf.drawCentredString(width / 2, 12.7 * cm, "Se otorga a:")

    # Nombre
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(width / 2, 11.2 * cm, nombre_alumno)

    # Descripción
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(
        width / 2,
        9.7 * cm,
        "Por acreditar satisfactoriamente el módulo académico:"
    )

    # Curso
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(width / 2, 8.5 * cm, f"Curso: {curso}")

    # Módulo
    pdf.drawCentredString(width / 2, 7.6 * cm, f"Módulo: {modulo}")

    # Calificación
    pdf.setFillColor(COLOR_AZUL)
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(
        width / 2,
        6.3 * cm,
        f"Calificación obtenida: {calificacion}/10"
    )

    # Fecha
    pdf.setFillColor(COLOR_GRIS)
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(
        width / 2,
        5.2 * cm,
        f"Fecha de emisión: {fecha_formateada()}"
    )

    # Folio
    pdf.drawString(2 * cm, 2 * cm, f"Folio: {folio}")

    # Hash
    pdf.setFont("Helvetica", 8)
    pdf.drawString(2 * cm, 1.5 * cm, f"Hash: {hash_cert[:40]}...")

    # Firma
    dibujar_firma(pdf, width)

    pdf.save()

    return {
        "ruta_pdf": ruta_pdf,
        "folio": folio,
        "hash": hash_cert
    }


def generar_certificado_curso(
    nombre_alumno,
    curso,
    promedio,
    ruta_anterior=None
):
    """
    Genera certificado final de curso.
    """
    if ruta_anterior:
        eliminar_archivo(ruta_anterior)

    ruta_pdf = ruta_certificado_curso(
        nombre_alumno,
        curso
    )

    folio = generar_folio("CUR")
    hash_cert = generar_hash_certificado(
        nombre_alumno,
        curso,
        "CERTIFICADO_FINAL",
        promedio,
        folio
    )

    width, height = landscape(A4)
    pdf = canvas.Canvas(ruta_pdf, pagesize=landscape(A4))

    dibujar_fondo(pdf, width, height)
    dibujar_marco(pdf, width, height)
    dibujar_sello(pdf, width, height)
    dibujar_encabezado(pdf, width, "Cursos de Regularización CECyTEM")

    pdf.setFillColor(COLOR_DORADO)
    pdf.setFont("Helvetica-Bold", 32)
    pdf.drawCentredString(width / 2, 14.4 * cm, "CERTIFICADO MAESTRO")

    pdf.setFillColor(black)
    pdf.setFont("Helvetica", 18)
    pdf.drawCentredString(width / 2, 12.5 * cm, "Se reconoce a:")

    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(width / 2, 11 * cm, nombre_alumno)

    pdf.setFont("Helvetica", 17)
    pdf.drawCentredString(
        width / 2,
        9.5 * cm,
        f"Por completar satisfactoriamente el curso:"
    )

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, 8.2 * cm, curso)

    pdf.setFillColor(COLOR_AZUL)
    pdf.drawCentredString(
        width / 2,
        6.8 * cm,
        f"Promedio final: {promedio}/10"
    )

    pdf.setFillColor(COLOR_GRIS)
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(
        width / 2,
        5.5 * cm,
        f"Fecha de emisión: {fecha_formateada()}"
    )

    pdf.drawString(2 * cm, 2 * cm, f"Folio: {folio}")
    pdf.setFont("Helvetica", 8)
    pdf.drawString(2 * cm, 1.5 * cm, f"Hash: {hash_cert[:40]}...")

    dibujar_firma(pdf, width)

    pdf.save()

    return {
        "ruta_pdf": ruta_pdf,
        "folio": folio,
        "hash": hash_cert
    }


if __name__ == "__main__":
    resultado = generar_certificado_modulo(
        "Alumno de Prueba",
        "Primaria",
        "Matemáticas básicas",
        10
    )

    print("PDF generado:")
    print(resultado["ruta_pdf"])