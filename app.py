from flask import Flask, render_template, request, redirect, url_for, flash
import os
from file_processor import analyze_file

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se encontró ningún archivo')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No se seleccionó ningún archivo')
        return redirect(url_for('index'))
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        output_filename = f"resumen_{file.filename}.txt"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        stats = analyze_file(filepath, output_path)
        
        if 'error' in stats:
            flash(f"Error: {stats['error']}")
            return redirect(url_for('index'))
        
        with open(output_path, 'r', encoding='utf-8') as f:
            summary = f.read()
        
        return render_template('results.html', 
                             filename=file.filename,
                             summary=summary,
                             stats=stats)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)