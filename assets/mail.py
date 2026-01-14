import os
from dotenv import load_dotenv

load_dotenv()

MAIL_CONT = os.getenv("MAIL_CONT")
FORM_CONT_PAS = os.getenv("FORM_CONT_PAS")
CUIT = os.getenv("CUIT")

content_mail = f"""
  <strong>¡Bienvenido/a a AILES!</strong>

  En este correo encontrarán la información que deben conocer acerca de los procesos administrativos/contables.

  <strong>Importante - ESTE MAIL ES AUTOMÁTICO Y NO ACEPTA RESPUESTAS.</strong>
  Por consultas comunicarse a {MAIL_CONT}

  <p style="margin:0;text-decoration: underline;"><strong>Confección de facturas:</strong></p>
    <li>Emitir Factura C:
      A nombre de: <strong>MARIA SIMOND</strong>
      CUIT: <strong>{CUIT}</strong>
      Condición frente al IVA: <strong>Responsable Inscripto.</strong>
      Dirección: <strong>O’Higgins 2244 piso 1D - CABA</strong>
    </li>
    <li> El período facturado debe corresponder al mes trabajado.
        <strong>Ejemplo:</strong> si se factura marzo 2026, el período debe ser desde
        01/03/2026 - hasta 31/03/2026.
    </li>
    <li> La <strong>descripción</strong> de la factura debe incluir apellido y nombre del paciente,
        mes y año facturado.
    </li>
    Las facturas que no cumplan con estos requisitos SERÁN RECHAZADAS.

  <p style="margin:0;text-decoration: underline;"><strong>Carga de facturas:</strong></p>
    Dentro del sistema INDYCO, en el apartado DOCUMENTACIÓN, encontrarán instructivos con el 
    paso a paso y videos explicativos para la carga de facturas.

    Recibimos facturas ÚNICAMENTE a través del portal INDYCO. Desde allí, podrán:
    <li>Acceder a sus órdenes de pago.
    </li>
    <li>Consultar el historial de pagos.
    </li>
    <li>Ver el estado de las facturas cargadas.
    </li>
    <li>Conocer la fecha estimada de pago.
    </li>
    Las órdenes de pago con el monto a facturar se generan a mes vencido, hasta el día 10 del mes siguiente.
    Ejemplo: las órdenes correspondientes a marzo estarán disponibles entre el 1 y el 10 de abril.

    UNA VEZ HABILITADA LA ORDEN DE PAGO, PODRÁN CARGAR LAS FACTURAS.

    El valor mensual a facturar se calcula según el nomenclador vigente y contempla el descuento por 
    inasistencias injustificadas (el valor POR DÍA se calcula dividiendo el monto total mensual por la 
    cantidad de días que asiste a la escuela durante el mes).

    Recomendamos cargar la factura apenas reciban la orden de pago, para evitar demoras en el cobro.

  <p style="margin:0;text-decoration: underline;"><strong>Pagos:</strong></p>
    Los pagos se realizan cada mes del 5 al 10 inclusive, de acuerdo con la modalidad del acompañamiento:
    <li> Procesos COMPLETOS (5 días por semana): pago a 30 días DE PRESENTADA LA FACTURA.
        Ejemplo: octubre se cobra en diciembre.
    </li>
    <li> Procesos PARCIALES (menos de 5 días por semana): pago a 60 días DE PRESENTADA LA FACTURA.
        Ejemplo: octubre se cobra en enero.
    </li>
    Para poder realizar el pago, es indispensable que tengan la factura cargada y aprobada, y haber informado 
    en INDYCO el CBU de una cuenta bancaria.

    <strong>NO</strong> se realizan pagos a billeteras virtuales (Mercado Pago, NaranjaX, Cuenta DNI, etc.) ni a cuentas del Banco Credicoop. 
    <strong>La cuenta informada debe pertenecer a una entidad bancaria.</strong>

    Ofrecemos y recomendamos fuertemente a todos los acompañantes la posibilidad de obtener una cuenta sueldo del banco 
    BBVA GRATUITA y bonificada, para poder cobrar allí sus honorarios.

    Quienes estén interesados/as pueden completar el siguiente formulario:

    {FORM_CONT_PAS}

    Tengan en cuenta que, debido a la carga habitual de trabajo, las respuestas a mails pueden demorar hasta 24 horas.
  <p style="margin:0;">Quedamos a disposición! Muchas gracias.</p>
  <p style="margin:0;"><strong>Equipo AILES</strong></p>
"""