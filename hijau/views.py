from django.shortcuts import redirect, render
from django.db import connection
from django.db.models.functions import datetime

# Create your views here.
def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def r_ujian_kualifikasi(request):
    query_list_ujian = """
                SELECT
                    tahun,
                    batch,
                    tempat,
                    tanggal,
                FROM
                    ujian_kualifikasi
                GROUP BY
                    tahun,
                    batch,
                    tempat,
                    tanggal,
                ORDER BY
                    tanggal ASC;
            """
    cursor = connection.cursor()
    cursor.execute('SET search_path to babadu;')
    cursor.execute(query_list_ujian)
    data_list_ujian = fetch(cursor)
    response = {'ujian_kualifikasi': data_list_ujian}

    return render(request, 'r_ujian_kualifikasi.html', response)

def c_ujian_kualifikasi(request):
    if request.method == 'GET':
        return render(request, 'c_ujian_kualifikasi.html')
    elif request.method == 'POST':
        tahun = request.POST['tahun']
        batch = request.POST['batch']
        tempat = request.POST['tempat']
        tanggal = request.POST['tanggal']

        if not (tahun and batch and tempat and tanggal):
            return render(request, 'c_ujian_kualifikasi.html', {'error': 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu'})

        query = f"""
            INSERT INTO ujian_kualifikasi (tahun, batch, tempat, tanggal)
            VALUES ('{tahun}', '{batch}', '{tempat}', '{tanggal}');
        """
        cursor = connection.cursor()
        cursor.execute('SET search_path TO babadu;')
        cursor.execute(query)

        return redirect('hijau:r_ujian_kualifikasi')
    
def c_k_ujian_kualifikasi(request):
    if request.method == 'POST':
        # Process the form submission
        answers = request.POST.getlist('answer')  # Assuming the input fields have name="answer[]"
        
        # Check the answers and calculate the score
        score = 0
        for answer in answers:
            # Check if the answer is correct and update the score accordingly
            if answer == "correct":
                score += 1
        
        # Check if the athlete has passed the qualification exam
        if score >= 4:
            # Perform the necessary actions for a passed qualification exam
            # For now, let's print the score as an example
            print(f"Score: {score} - Qualification exam passed")
        else:
            # Perform the necessary actions for a failed qualification exam
            # For now, let's print the score as an example
            print(f"Score: {score} - Qualification exam failed")
        
        # Redirect the athlete to the "Riwayat Ujian Kualifikasi" page
        return redirect('landing_page:riwayat_ujian_kualifikasi')

    else:
        # Render the page with the qualification exam questions
        questions = [
            {
                'question': 'Question 1',
                'choices': ['Choice 1', 'Choice 2', 'Choice 3'],
            },
            {
                'question': 'Question 2',
                'choices': ['Choice 1', 'Choice 2', 'Choice 3'],
            },
            # Add more questions as needed
        ]

        return render(request, 'c_k_ujian_kualifikasi.html', {'questions': questions})

def r_k_ujian_kualifikasi(request):
    query_kualifikasi =  """
                SELECT
                M.nama,
                UK.tahun,
                UK.batch,
                UK.tempat
                FROM
                member M
                JOIN
                atlet A ON M.id = A.id
                JOIN
                atlet_kualifikasi AK ON A.id = AK.id_atlet
                LEFT JOIN
                ujian_kualifikasi UK ON 1 = 0
                ORDER BY
                UK.tanggal ASC;
            """
    cursor = connection.cursor()
    cursor.execute('SET search_path to babadu;')
    cursor.execute(query_kualifikasi)
    data_kualifikasi = fetch(cursor)

    query_non_kualifikasi =  """
                SELECT
                M.nama,
                UK.tahun,
                UK.batch,
                UK.tempat
                FROM
                member M
                JOIN
                atlet A ON M.id = A.id
                JOIN
                atlet_non_kualifikasi ANK ON A.id = ANK.id_atlet
                LEFT JOIN
                ujian_kualifikasi UK ON 1 = 0
                ORDER BY
                UK.tanggal ASC;
            """
    cursor = connection.cursor()
    cursor.execute('SET search_path to babadu;')
    cursor.execute(query_non_kualifikasi)
    data_non_kualifikasi = fetch(cursor)

    response = {'riwayat_atlet_kualifikasi': data_kualifikasi,
                'riwayat_atlet_non_kualifikasi':data_non_kualifikasi}
    return render(request, 'r_k_ujian_kualifikasi.html')


