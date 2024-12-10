import csv
import sys
from tqdm import tqdm
import re
from openpyxl import Workbook

def whatsapp_to_csv_xlsx(input_filename, output_csv, output_xlsx):
    """Convertir un chat de WhatsApp a formato CSV y Excel."""
    with open(input_filename, 'r', encoding='utf-8-sig') as f_in, \
            open(output_csv, 'w', encoding='utf-8-sig', newline='') as f_out_csv:

        writer = csv.writer(f_out_csv)

        # Escribe el encabezado del CSV
        writer.writerow(['Fecha', 'Hora', 'Remitente', 'Mensaje'])

        # Crear el archivo XLSX
        wb = Workbook()
        ws = wb.active
        ws.title = "WhatsApp Chat"
        ws.append(['Fecha', 'Hora', 'Remitente', 'Mensaje'])

        # Expresión regular para detectar nuevos mensajes
        message_pattern = re.compile(r"^\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}(:\d{2})?\s?[ap]\.?\s?m\.?)\] (.+?): (.*)$")
        system_message_pattern = re.compile(r"^\[(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}(:\d{2})?\s?[ap]\.?\s?m\.?)\] (.+)$")

        current_date = current_time = sender = None
        message_buffer = []

        # Contar líneas para mostrar progreso
        lines = f_in.readlines()
        for line in tqdm(lines, total=len(lines), desc="Procesando"):
            line = line.strip()

            # Eliminar caracteres no imprimibles (como \u200e) de la línea
            line = line.replace('\u200e', '')

            if not line:
                continue

            # Si coincide con un mensaje nuevo
            match = message_pattern.match(line)
            system_match = system_message_pattern.match(line)

            if match:
                # Guardar el mensaje anterior antes de procesar el nuevo
                if message_buffer:
                    save_message(writer, ws, current_date, current_time, sender, message_buffer)
                    message_buffer = []

                # Extraer información del nuevo mensaje
                current_date, current_time, _, sender, message = match.groups()
                message_buffer.append(message)
            elif system_match:
                # Mensaje del sistema
                if message_buffer:
                    save_message(writer, ws, current_date, current_time, sender, message_buffer)
                    message_buffer = []

                current_date, current_time, _, message = system_match.groups()
                sender = "Sistema"
                message_buffer.append(message)
            else:
                # Línea que pertenece al mensaje anterior (multilinea)
                message_buffer.append(line)

        # Guardar el último mensaje
        if message_buffer:
            save_message(writer, ws, current_date, current_time, sender, message_buffer)

        # Guardar el archivo XLSX
        wb.save(output_xlsx)

def save_message(writer, ws, date, time, sender, message_buffer):
    """Guardar un mensaje en el CSV y Excel."""
    message = '\n'.join(message_buffer).replace(" ", " ")
    writer.writerow([date, time, sender, message])
    ws.append([date, time, sender, message])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python whatsapp_converter.py <input.txt> <output.csv> <output.xlsx>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_csv = sys.argv[2]
    output_xlsx = sys.argv[3]
    whatsapp_to_csv_xlsx(input_filename, output_csv, output_xlsx)
