import csv
import sys
from tqdm import tqdm
import re
from openpyxl import Workbook


def whatsapp_to_csv_xlsx(input_filename, output_csv, output_xlsx):
    """Convierte un archivo de chat de WhatsApp a CSV y XLSX.


    Args:
        input_filename: Nombre del archivo de chat de WhatsApp de entrada (formato txt, UTF-8).
        output_csv: Nombre del archivo CSV de salida.
        output_xlsx: Nombre del archivo XLSX de salida.
    """


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


        # Contar líneas en el archivo para mostrar el progreso
        num_lines = sum(1 for line in f_in)
        f_in.seek(0)  # Volver al principio del archivo


        # Mostrar progreso utilizando tqdm
        message_buffer = []
        date = time = sender = ''
        date_time_sender_pattern = re.compile(r"^\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\s?[ap]\.?\s?m\.? - .+?: ")


        for line in tqdm(f_in, total=num_lines, desc="Procesando"):
            line = line.strip()
            if line:  # Ignorar líneas vacías
                if date_time_sender_pattern.match(line):  # Nueva fecha, hora y remitente
                    if message_buffer:
                        # Procesar el mensaje anterior
                        date, time, sender, message = process_message(message_buffer, date, time, sender)
                        writer.writerow([date, time, sender, message])
                        ws.append([date, time, sender, message])
                        message_buffer = []
                    parts = line.split(' - ', 1)
                    date_time, sender_message = parts
                    date, time = date_time.split(', ')
                    sender, message = sender_message.split(': ', 1)
                    message_buffer.append(message)
                else:
                    # Continuación de un mensaje anterior
                    message_buffer.append(line)


        # Procesar el último mensaje
        if message_buffer:
            date, time, sender, message = process_message(message_buffer, date, time, sender)
            writer.writerow([date, time, sender, message])
            ws.append([date, time, sender, message])


        # Guardar el archivo XLSX
        wb.save(output_xlsx)


def process_message(message_buffer, date, time, sender):
    """Procesa un mensaje que puede contener varias líneas"""
    message = '\n'.join(message_buffer).replace(" ", " ")
    return date, time, sender, message


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python whatsapp_converter.py <input.txt> <output.csv> <output.xlsx>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_csv = sys.argv[2]
    output_xlsx = sys.argv[3]
    whatsapp_to_csv_xlsx(input_filename, output_csv, output_xlsx)
