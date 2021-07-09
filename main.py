from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt

application = Flask(__name__)
application.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
application.config['MYSQL_USER'] = 'sql6423736'
application.config['MYSQL_PASSWORD'] = '1uncDdMBWn'
application.config['MYSQL_DB'] = 'sql6423736'
mysql = MySQL(application)

@application.route('/index')
def index():
    query_kesiapan = "SELECT COUNT(*) FROM data_kesiapan;"
    query_anggaran = "SELECT * FROM data_anggaran;"
    query_rekomendasi = "SELECT COUNT(*) FROM data_rekomendasi;"
    query_admin = "SELECT COUNT(*) FROM data_user;"

    cur = mysql.connection.cursor()
    cur.execute(query_kesiapan)
    kesiapan = cur.fetchall()
    cur.execute(query_anggaran)
    anggaran = cur.fetchall()
    cur.execute(query_rekomendasi)
    rekomendasi = cur.fetchall()
    cur.execute(query_admin)
    admin = cur.fetchall()
    cur.close()
    return render_template('index.html', kesiapan=kesiapan[0], anggaran=len(anggaran[0]), grafik=anggaran, rekomendasi=rekomendasi[0], admin=admin[0])

@application.route('/', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM data_user WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()
        print(password)
        if len(user) > 0:
            print(user["password"])

            if password == user["password"]:
                session['nama'] = user['nama']
                session['email'] = user['email']
                session["role"] = user["level"]
                if user["level"] == "user":
                    return redirect(url_for('index'))
                else :
                    return redirect(url_for('index'))
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")

@application.route('/register', methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        nama = request.form['nama']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        level = request.form['level']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data_user (nama, email, password, level) VALUES (%s,%s,%s,%s)",(nama,email,password,level))
        mysql.connection.commit()
        session['nama'] = request.form['nama']
        session['email'] = request.form['email']
        return redirect(url_for('login'))

@application.route('/data-anggaran')
def dataAnggaran():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data_anggaran")
    anggaran = cur.fetchall()
    cur.close()
    return render_template('data-anggaran.html', data=anggaran)

@application.route('/simpanAnggaran', methods=["POST"])
def simpanAnggaran():
    tahun = request.form['tahun']
    anggaran = request.form['anggaran']
    jumlah = request.form['jumlah']
    keterangan = request.form['keterangan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO data_anggaran (tahun, anggaran, jumlah, keterangan) VALUES (%s, %s, %s, %s)", (tahun, anggaran, jumlah, keterangan,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataAnggaran'))

@application.route('/ubahAnggaran', methods=["POST"])
def ubahAnggaran():
    id_anggaran = request.form['id_anggaran']
    tahun = request.form['tahun']
    anggaran = request.form['anggaran']
    jumlah = request.form['jumlah']
    keterangan = request.form['keterangan']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE data_anggaran SET tahun=%s, anggaran=%s, jumlah=%s, keterangan=%s WHERE id_anggaran=%s", (tahun, anggaran, jumlah, keterangan, id_anggaran,))
    mysql.connection.commit()
    return redirect(url_for('dataAnggaran'))

@application.route('/hapusAnggaran/<id_anggaran>', methods=["GET"])
def hapusAnggaran(id_anggaran):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data_anggaran WHERE id_anggaran=%s", (id_anggaran,))
    mysql.connection.commit()
    return redirect(url_for('dataAnggaran'))

@application.route('/data_kesiapan/')
def dataKesiapan():
    th = request.args.get('tahun')
    query = "SELECT * FROM `data_kesiapan`"
    if(th) :
        query = "SELECT * FROM `data_kesiapan` WHERE tahun="+str(th)
    cur = mysql.connection.cursor()
    cur.execute(query)
    kesiapanData = cur.fetchall()
    cur.close()
    return render_template('data_kesiapan.html', data = kesiapanData)

@application.route('/simpanFormdata', methods=["POST"])
def simpanFormdata():
    tahun = request.form['tahun']
    periode = request.form['periode']
    bulan = request.form['bulan']
    kekuatan = request.form['kekuatan']
    nilai_kesiapan = request.form['nilai_kesiapan']
    print(periode)

    periode_semua=12+int(periode)
    print(periode_semua)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO data_kesiapan(tahun, periode, periode_semua, bulan, kekuatan, nilai_kesiapan) VALUES (%s, %s, %s, %s, %s, %s)", (tahun, periode, str(periode_semua), bulan, kekuatan, nilai_kesiapan))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataKesiapan'))

@application.route('/ubah', methods=["POST"])
def ubah():
    id_kesiapan = request.form['id_kesiapan']
    tahun = request.form['tahun']
    periode = request.form['periode']
    bulan = request.form['bulan']
    kekuatan = request.form['kekuatan']
    nilai_kesiapan = request.form['nilai_kesiapan']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE data_kesiapan SET tahun=%s, periode=%s, bulan=%s, kekuatan=%s, nilai_kesiapan=%s WHERE id_kesiapan=%s", (tahun, periode, bulan, kekuatan, nilai_kesiapan, id_kesiapan,))
    mysql.connection.commit()
    return redirect(url_for('dataKesiapan'))

@application.route('/hapus/<id_kesiapan>', methods=["GET"])
def hapus(id_kesiapan):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data_kesiapan WHERE id_kesiapan=%s", (id_kesiapan,))
    mysql.connection.commit()
    return redirect(url_for('dataKesiapan'))

@application.route('/prediksiTotal')
def prediksiTotal():
    th = request.args.get('th')
    query = "SELECT * FROM `data_kesiapan`"
    if(th) :
        thSebelum = int(th)-1
        query = "SELECT * FROM `data_kesiapan` WHERE tahun="+str(thSebelum)
        query2 = "SELECT * FROM `data_kesiapan` WHERE tahun="+str(th)
    cur = mysql.connection.cursor()
    cur.execute(query)
    kesiapanDataSebelum = cur.fetchall()
    cur.execute(query2)
    kesiapanData = cur.fetchall()
    cur.close()
    x2 = sum(c[2]*c[2] for c in kesiapanDataSebelum)
    xy = sum(c[2]*c[6] for c in kesiapanDataSebelum)
    x = sum(c[2] for c in kesiapanDataSebelum)
    y = sum(c[6] for c in kesiapanDataSebelum)
    n = len(kesiapanDataSebelum)
    tmpA = (y * x2) - (x * xy)
    a = tmpA / ((n * x2) - (x*x))
   
    tmpB = (n*xy) - (x*y)
    b = tmpB / ((n * x2) - (x*x))
    print(a)
    print(b)
    return render_template('prediksiTotal.html', data=kesiapanData, a=a, b=b, tahun=th)

@application.route('/prediksi')
def prediksi():
    query = "SELECT * FROM `data_kesiapan`"
    cur = mysql.connection.cursor()
    cur.execute(query)
    kesiapanData = cur.fetchall()
    cur.close()
    return render_template('prediksi.html', data=kesiapanData)

@application.route('/hitungMape')
def hitungMape():
    th = request.args.get('th')
    query = "SELECT * FROM `data_kesiapan`"
    if(th) :
        thSebelum = int(th)-1
        query = "SELECT * FROM `data_kesiapan` WHERE tahun="+str(thSebelum)
        query2 = "SELECT * FROM `data_kesiapan` WHERE tahun="+str(th)
    cur = mysql.connection.cursor()
    cur.execute(query)
    kesiapanDataSebelum = cur.fetchall()
    cur.execute(query2)
    kesiapanData = cur.fetchall()
    cur.close()
    x2 = sum(c[2]*c[2] for c in kesiapanDataSebelum)
    y2 = sum(c[6]*c[6] for c in kesiapanDataSebelum)
    xy = sum(c[2]*c[6] for c in kesiapanDataSebelum)
    x = sum(c[2] for c in kesiapanDataSebelum)
    y = sum(c[6] for c in kesiapanDataSebelum)
    n = len(kesiapanDataSebelum)
    tmpA = (y * x2) - (x * xy)
    a = tmpA / ((n * x2) - (x*x))
    tmpB = (n*xy) - (x*y)
    b = tmpB / ((n * x2) - (x*x))

    totalPE = sum( abs((c[6] -( a + (b*c[3])))/c[6])  for c in kesiapanData)
    mape = totalPE/12

    tmpR = ((n*xy) - (x*y)) * ((n*xy) - (x*y))
    r = tmpR / (((n * x2) - (x*x)) * ((n* y2) - (y *y)))
    print(r)

    return render_template('hitungMape.html', mape=mape, totalPE=totalPE, tahun=th, r=r )

@application.route('/simpanHasil', methods=["POST"])
def simpanHasil():
    tahun = request.form['tahun']
    kekuatan = request.form['kekuatan']
    periode = request.form['periode']
    nilai_kesiapan = request.form['nilai_kesiapan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO prediksi(tahun, kekuatan, periode, nilai_kesiapan) VALUES (%s, %s, %s, %s)", (tahun, kekuatan, periode, nilai_kesiapan))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('prediksi'))

@application.route('/rekomendasi')
def rekomendasi():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data_rekomendasi")
    rekomendasi = cur.fetchall()
    cur.close()
    return render_template('rekomendasi.html', data=rekomendasi)

@application.route('/simpanRekomendasi', methods=["POST"])
def simpanRekomendasi():
    tahun = request.form['tahun']
    jml_anggaran = request.form['jml_anggaran']
    ket = request.form['ket']
    rekomendasi = request.form['rekomendasi']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO data_rekomendasi(tahun, jml_anggaran, ket, rekomendasi) VALUES (%s, %s, %s, %s)", (tahun, jml_anggaran, ket, rekomendasi))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('rekomendasi'))

@application.route('/ubahRekomendasi', methods=["POST"])
def ubahRekomendasi():
    id_rekomendasi = request.form['id_rekomendasi']
    tahun = request.form['tahun']
    jml_anggaran = request.form['jml_anggaran']
    ket = request.form['ket']
    rekomendasi = request.form['rekomendasi']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE data_rekomendasi SET tahun=%s, jml_anggaran=%s, ket=%s, rekomendasi=%s WHERE id_rekomendasi=%s", (tahun, jml_anggaran, ket, rekomendasi, id_rekomendasi,))
    mysql.connection.commit()
    return redirect(url_for('rekomendasi'))

@application.route('/hapusRekomendasi/<id_rekomendasi>', methods=["GET"])
def hapusRekomendasi(id_rekomendasi):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data_rekomendasi WHERE id_rekomendasi=%s", (id_rekomendasi,))
    mysql.connection.commit()
    return redirect(url_for('rekomendasi'))

@application.route('/admin')
def dataAdmin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data_user")
    admin = cur.fetchall()
    cur.close()
    return render_template('admin.html', data = admin)

@application.route('/simpandataAdmin', methods=["POST"])
def simpandataAdmin():
    nama = request.form['nama']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO data_user(nama, email, password) VALUES (%s, %s, %s)", (nama, email, password,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataAdmin'))

@application.route('/ubahAdmin', methods=["POST"])
def ubahAdmin():
    id_user = request.form['id_user']
    nama = request.form['nama']
    email = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE data_user SET nama=%s, email=%s, password=%s WHERE id_user=%s", (nama, email, password, id_user,))
    mysql.connection.commit()
    return redirect(url_for('dataAdmin'))

@application.route('/hapusAdmin/<id_user>', methods=["GET"])
def hapusAdmin(id_user):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data_user WHERE id_user=%s", (id_user,))
    mysql.connection.commit()
    return redirect(url_for('dataAdmin'))
