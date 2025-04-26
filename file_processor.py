import os

def analyze_file(input_path, output_path):
    """
    Analiza un archivo de texto y genera un resumen con:
    - Número de líneas
    - Número de palabras
    - Número de caracteres
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        lines = content.split('\n')
        words = content.split()
        
        stats = {
            'filename': os.path.basename(input_path),
            'lines': len(lines),
            'words': len(words),
            'characters': len(content),
            'path': os.path.abspath(input_path)
        }
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(f"Resumen del archivo: {stats['filename']}\n")
            output_file.write(f"Ubicación: {stats['path']}\n")
            output_file.write(f"Líneas: {stats['lines']}\n")
            output_file.write(f"Palabras: {stats['words']}\n")
            output_file.write(f"Caracteres: {stats['characters']}\n")
        
        return stats
    
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    input_file = "ejemplo.txt"
    output_file = "resumen.txt"
    
    if not os.path.exists(input_file):
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("Este es un archivo de ejemplo.\n")
            f.write("Contiene varias líneas.\n")
            f.write("Y varias palabras también.\n")
    
    result = analyze_file(input_file, output_file)
    print("Análisis completado. Resultados guardados en", output_file)