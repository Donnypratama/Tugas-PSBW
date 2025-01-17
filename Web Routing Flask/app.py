from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'flaskkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['nama'] = request.form.get('nama')
        session['nim'] = request.form.get('nim')
        session['jurusan'] = request.form.get('jurusan')
        session['email'] = request.form.get('email')
        session['tempattinggal'] = request.form.get('tempattinggal')
        session['tanggallahir'] = request.form.get('tanggallahir')
        session['kode'] = request.form.get('kode')
        session['matkul'] = request.form.get('matkul')
        nilai = request.form.get('nilai', type=float)
        sks = request.form.get('sks', type=int)

        if nilai and sks:
            session['nilai'] = nilai
            session['sks'] = sks
            session['ipk'] = 25 / (nilai * sks)  
        else:
            session['ipk'] = None  
        return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'nama' in session:
        return render_template('dashboard.html',
                               nama=session['nama'],
                               tempattinggal=session['tempattinggal'],
                               tanggallahir=session['tanggallahir'],
                               nim=session['nim'],
                               jurusan=session['jurusan'],
                               email=session['email'])
    return redirect(url_for('index'))

@app.route('/krs')
def krs():
    if 'nama' in session:
        return render_template('krs.html',
                               nama=session['nama'],
                               kode=session['kode'],
                               matkul=session['matkul'],
                               sks=session['sks'])
    return redirect(url_for('index'))

@app.route('/nilai')
def nilai():
    if 'nama' in session:
        return render_template('nilai.html',
                               nama=session['nama'],
                               matkul=session['matkul'],
                               sks=session['sks'],
                               nilai=session['nilai'])
    return redirect(url_for('index'))

@app.route('/laporan')
def laporan():
    if 'nama' in session:
        return render_template('laporan.html',
                               nama=session['nama'],
                               nim=session['nim'],
                               ipk=session['ipk'],
                               sks=session['sks'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)