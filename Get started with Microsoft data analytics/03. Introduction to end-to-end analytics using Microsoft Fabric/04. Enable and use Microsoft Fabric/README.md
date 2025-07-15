🛠️ Learning Path: Enable and Use Microsoft Fabric
🚀 Mengaktifkan Microsoft Fabric
Sebelum menggunakan fitur Microsoft Fabric secara penuh, layanan ini harus diaktifkan oleh admin organisasi. Berikut peran yang bisa mengaktifkan Fabric:

Fabric Admin: Mengatur konfigurasi Fabric dari portal admin Power BI.

Power Platform Admin: Mengelola layanan Power Platform termasuk Fabric.

Microsoft 365 Admin: Mengelola layanan Microsoft secara menyeluruh, termasuk aktivasi Fabric.

🔧 Cara mengaktifkan:

Masuk ke Admin Portal > Tenant Settings pada Power BI Service.

Fabric bisa diaktifkan untuk seluruh organisasi atau grup tertentu di Microsoft 365 / Microsoft Entra.

Pengaturan ini dapat didelegasikan pada pengguna lain berdasarkan kapasitas.

💡 Tips: Jika belum memiliki akses, kamu bisa mendaftar free trial Microsoft Fabric.

🗂️ Workspace di Microsoft Fabric
Workspaces adalah lingkungan kolaboratif untuk membuat dan mengelola aset seperti lakehouses, warehouses, dan laporan. Semua data tersimpan dalam OneLake.

Pengaturan workspace meliputi:
Tipe lisensi untuk fitur Fabric.

Akses OneDrive ke workspace.

Koneksi ke Azure Data Lake Gen2.

Integrasi Git untuk version control.

Pengaturan Spark workload (untuk optimasi performa).

Role workspace:
Admin: Pengelola penuh.

Contributor: Bisa menambah dan mengedit konten.

Member: Bisa melihat dan memberi komentar.

Viewer: Hanya bisa melihat.

Untuk kontrol lebih detail, gunakan item-level permissions.

🔎 Temukan Data dengan OneLake Catalog
OneLake Catalog membantu menemukan dan mengakses data yang telah dibagikan kepada pengguna.

Fitur pencarian meliputi:

Filter berdasarkan workspace atau domain.

Eksplorasi berdasarkan kategori.

Filter berdasarkan keyword atau tipe item.

🧱 Buat Item dengan Fabric Workloads
Setelah workspace aktif, kamu bisa mulai membuat item sesuai kebutuhan bisnis:

Workload	Deskripsi
Data Engineering	Buat lakehouse, transformasi data, dan automasi.
Data Factory	Ingest, transformasi, dan orkestrasi data.
Data Science	Deteksi pola, prediksi tren, dan modeling ML.
Data Warehouse	Gabungkan berbagai sumber ke dalam gudang data.
Databases	Kelola database dan query data.
Industry Solutions	Solusi data out-of-the-box untuk industri.
Real-Time Intelligence	Proses dan analisis data streaming secara langsung.
Power BI	Buat laporan dan dashboard interaktif.

Fabric menyatukan fitur dari Power BI, Azure Synapse, dan Azure Data Factory ke dalam satu platform tanpa perlu akses langsung ke Azure resources.

🧭 Arsitektur Data Mesh
Fabric mendukung data mesh architecture:

Desentralisasi kepemilikan data

Tetap mempertahankan governance terpusat

Tidak perlu akses langsung ke Azure, menyederhanakan proses data untuk semua peran.

