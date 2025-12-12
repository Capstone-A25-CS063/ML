**🏦 Bank Marketing Intelligence System (End-to-End)**

Proyek ini adalah solusi lengkap Machine Learning untuk memprediksi potensi nasabah deposito bank. Terdiri dari dua komponen utama:

**Model Training**: Eksplorasi data dan pelatihan model menggunakan XGBoost & SMOTE.

**Deployment API**: Layanan REST API berbasis FastAPI untuk prediksi real-time dan batch, dilengkapi simulasi data ekonomi otomatis.

**📋 Daftar Isi**
1. Struktur Proyek
2. Tentang Dataset & Model
3. Fitur API
4. Teknologi
5. Instalasi & Requirements
6. Cara Menjalankan Training
7. Cara Menjalankan API
   

**📂 Struktur Proyek**

Berdasarkan implementasi kode, berikut adalah struktur direktori proyek:

```
/bank-marketing-project
│
├── 📁 models/                  # Folder penyimpanan model
│   └── modelCapstoneAsahLeadScoring.joblib  # Model hasil training (Wajib ada untuk API)
│
├── 📁 services/                # Folder modul bantuan (helper)
│   └── economic_data.py        # Script simulasi indikator ekonomi makro
│
├── bank-additional-full.csv    # Dataset mentah
├── CapstoneAsahFinal.ipynb     # Jupyter Notebook untuk training & analisis
├── main.py                     # Aplikasi utama (FastAPI Server)
├── README.md                   # Dokumentasi proyek
└── requirements.txt            # Daftar dependensi library
```

**📊 Tentang Dataset & Model**
- Dataset: Bank Marketing Dataset (UCI) dengan 20 fitur input + target y.
- Preprocessing: Handling imbalance dengan SMOTE, Scaling, dan Encoding.
- Model: XGBoost Classifier dengan Hyperparameter Tuning.
- Performa: Fokus pada keseimbangan Precision & Recall.

**🚀 Fitur API**
- Aplikasi backend (main.py) menyediakan fitur cerdas:
- Auto-Fetch Economic Data: Input tidak perlu memasukkan data ekonomi makro (seperti euribor3m, conf.idx). API secara otomatis mensimulasikan data terkini melalui modul services/economic_data.py.
- Smart Scoring & Insights: Memberikan rekomendasi aksi ("HUBUNGI" / "IGNORE") dan mendeteksi risiko spam jika nasabah terlalu sering dihubungi (fatigued_client).
- Batch Prediction: Mendukung upload file CSV untuk memprediksi ratusan data nasabah sekaligus.
- Dokumentasi Interaktif: Menggunakan Swagger UI untuk mencoba API secara langsung.

**🛠 Teknologi**
- Core: Python 3.12+
- Data Science: Pandas, NumPy, Scikit-Learn, XGBoost, Imbalanced-Learn.
- Web Framework: FastAPI, Uvicorn.
- Utilities: Joblib (Model serialization), Pydantic (Data validation).

**💻 Instalasi & Requirements**
Clone/Download Repository ini.
- Buat Virtual Environment (Opsional tapi disarankan):
python -m venv venv
  - Windows
  ```venv\Scripts\activate ```
  - Mac/Linux
  ```source venv/bin/activate ```

- Install Dependensi: Simpan daftar library di bawah ke requirements.txt lalu jalankan:
pip install -r requirements.txt

- Isi requirements.txt:
   - pandas
   - numpy
   - scikit-learn
   - xgboost
   - imbalanced-learn
   - joblib
   - fastapi
   - uvicorn
   - python-multipart

**🏃‍♂️ Cara Menjalankan Training**
Gunakan Jupyter Notebook untuk melatih ulang model jika diperlukan.
- Buka CapstoneAsahFinal.ipynb.
- Jalankan semua sel ("Run All").
- Hasil training akan disimpan. Penting: Pindahkan dan ganti nama file model hasil training ke folder models/ dengan nama modelCapstoneAsahLeadScoring.joblib agar terbaca oleh API.

**🌐 Cara Menjalankan API**
Setelah model tersedia di folder models/:
- Jalankan file main.py
- Buka postman
- Uji Coba Endpoint:
  - POST /predict: Masukkan data satu nasabah (JSON).
  - POST /predict_batch_csv: Upload file CSV berisi daftar nasabah.
