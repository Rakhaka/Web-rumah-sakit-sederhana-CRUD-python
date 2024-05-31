from flask import Flask, render_template, request, url_for, flash, session
from werkzeug.utils import redirect
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# @app.route('/')
# def pasien():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM pasien")
#     data_pasien = cur.fetchall()
#     cur.close()
#     return render_template('pasien.html', pasien=data_pasien)


# pasien
@app.route('/pasien')
def pasien():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pasien")
    data_pasien = cur.fetchall()
    cur.close()

    return render_template('pasien.html', pasien=data_pasien)

@app.route('/tambah_pasien', methods = ['POST'])
def tambah_pasien():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        tgl_lahir = request.form['tgl_lahir']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO pasien (id, nama, tgl_lahir, jenis_kelamin, alamat) VALUES (%s, %s, %s, %s, %s)", (id, nama, tgl_lahir, jenis_kelamin, alamat))
        mysql.connection.commit()
        return redirect(url_for('pasien'))

@app.route('/hapus_pasien/<string:id_data>', methods = ['GET'])
def hapus_pasien(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pasien WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('pasien'))

@app.route('/ubah_pasien', methods=['POST', 'GET'])
def ubah_pasien():
    if request.method == 'POST':
        id_data = request.form['id']
        id_pasien = request.form['id']
        nama = request.form['nama']
        tgl_lahir = request.form['tgl_lahir']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']

        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE pasien SET id=%s, nama=%s, tgl_lahir=%s, jenis_kelamin=%s, alamat=%s WHERE id=%s""",
            (id_pasien, nama, tgl_lahir, jenis_kelamin, alamat, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('pasien'))




# Dokter
@app.route('/dokter')
def dokter():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dokter")
    data_dokter = cur.fetchall()
    cur.close()

    return render_template('dokter.html', dokter=data_dokter)

@app.route('/tambah_dokter', methods = ['POST'])
def tambah_dokter():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        spesialis = request.form['spesialis']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO dokter (id, nama, jenis_kelamin, spesialis) VALUES (%s, %s, %s, %s)", (id, nama,  jenis_kelamin, spesialis))
        mysql.connection.commit()
        return redirect(url_for('dokter'))

@app.route('/hapus_dokter/<string:id_data>', methods = ['GET'])
def hapus_dokter(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM dokter WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('dokter'))

@app.route('/ubah_dokter', methods=['POST', 'GET'])
def ubah_dokter():
    if request.method == 'POST':
        id_data = request.form['id']
        id_pasien = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        spesialis = request.form['spesialis']

        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE dokter SET id=%s, nama=%s, jenis_kelamin=%s, spesialis=%s WHERE id=%s""",
            (id_pasien, nama, jenis_kelamin, spesialis, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('dokter'))
    
    
    

# Admin
@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin")
    data_admin = cur.fetchall()
    cur.close()

    return render_template('admin.html', admin=data_admin)

@app.route('/tambah_admin', methods = ['POST'])
def tambah_admin():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO admin (id, nama, jenis_kelamin, alamat) VALUES (%s, %s, %s, %s)", (id, nama,  jenis_kelamin, alamat))
        mysql.connection.commit()
        return redirect(url_for('admin'))

@app.route('/hapus_admin/<string:id_data>', methods = ['GET'])
def hapus_admin(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM admin WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('admin'))

@app.route('/ubah_admin', methods=['POST', 'GET'])
def ubah_admin():
    if request.method == 'POST':
        id_data = request.form['id']
        id = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        alamat = request.form['alamat']

        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE admin SET id=%s, nama=%s, jenis_kelamin=%s, alamat=%s WHERE id=%s""",
            (id, nama, jenis_kelamin, alamat, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('admin'))
    
    

# perawat
@app.route('/perawat')
def perawat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM perawat")
    data_perawat = cur.fetchall()
    cur.close()

    return render_template('perawat.html', perawat=data_perawat)

@app.route('/tambah_perawat', methods = ['POST'])
def tambah_perawat():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO perawat (id, nama, jenis_kelamin) VALUES (%s, %s, %s)", (id, nama,  jenis_kelamin ))
        mysql.connection.commit()
        return redirect(url_for('perawat'))

@app.route('/hapus_perawat/<string:id_data>', methods = ['GET'])
def hapus_perawat(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM perawat WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('admin'))

@app.route('/ubah_perawat', methods=['POST', 'GET'])
def ubah_perawat():
    if request.method == 'POST':
        id_data = request.form['id']
        id = request.form['id']
        nama = request.form['nama']
        jenis_kelamin = request.form['jenis_kelamin']
       

        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE perawat SET id=%s, nama=%s, jenis_kelamin=%s WHERE id=%s""",
            (id, nama, jenis_kelamin, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('perawat'))

    
    

# kamar
@app.route('/kamar')
def kamar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kamar")
    data_kamar = cur.fetchall()
    cur.close()

    return render_template('kamar.html', kamar=data_kamar)

@app.route('/tambah_kamar', methods = ['POST'])
def tambah_kamar():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        kelas = request.form['kelas']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO kamar (id, nama, kelas) VALUES (%s, %s, %s)", (id, nama, kelas ))
        mysql.connection.commit()
        return redirect(url_for('kamar'))

@app.route('/hapus_kamar/<string:id_data>', methods = ['GET'])
def hapus_kamar(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM kamar WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('kamar'))


# @app.route('/ubah_kamar', methods=['POST', 'GET'])
# def ubah_kamar():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         id = request.form['id']
#         nama = request.form['nama']
#         kelas = request.form['kelas']
       

#         cur = mysql.connection.cursor()
#         cur.execute(
#             """UPDATE kamar SET id=%s, nama=%s, kelas=%s, WHERE id=%s""",
#             (id, nama, kelas, id_data)
#         )

#         mysql.connection.commit()
#         cur.close()

#         flash("Data Updated Successfully")
#         return redirect(url_for('kamar'))

@app.route('/ubah_kamar', methods=['POST', 'GET'])
def ubah_kamar():
    if request.method == 'POST':
        id_data = request.form['id']
        nama = request.form['nama']
        kelas = request.form['kelas']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE kamar SET nama=%s, kelas=%s WHERE id=%s",
            (nama, kelas, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('kamar'))





# Obat
@app.route('/obat')
def obat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM obat")
    data_obat = cur.fetchall()
    cur.close()

    return render_template('obat.html', obat=data_obat)

@app.route('/tambah_obat', methods = ['POST'])
def tambah_obat():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        nama = request.form['nama']
        jenis = request.form['jenis']
       
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO obat (id, nama, jenis) VALUES (%s, %s, %s)", (id, nama, jenis))
        mysql.connection.commit()
        return redirect(url_for('obat'))

@app.route('/hapus_obat/<string:id_data>', methods = ['GET'])
def hapus_obat(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM obat WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('obat'))

@app.route('/ubah_obat', methods=['POST', 'GET'])
def ubah_obat():
    if request.method == 'POST':
        id_data = request.form['id']
        id = request.form['id']
        nama = request.form['nama']
        jenis = request.form['jenis']
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE obat SET id=%s, nama=%s, jenis=%s WHERE id=%s""",
            (id, nama, jenis, id_data)
        )

        mysql.connection.commit()
        cur.close()

        flash("Data Updated Successfully")
        return redirect(url_for('obat'))
    
    
    

#SignUp
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/signup', methods = ['POST'])
def sign_up():
    if request.method == "POST":
        flash('Account Created!')
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `login`(`username`, `password`) VALUES (%s, %s)",(username, password))
        mysql.connection.commit()
        return redirect(url_for('login'))

#LogIn    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login', methods = ['GET','POST'])
def log_in():
    msg=''
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM login WHERE username=%s AND password=%s',(username,password))
        record = cur.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html',msg=msg)





if __name__ == "__main__":
    app.run(debug=True)