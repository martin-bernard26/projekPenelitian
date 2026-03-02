import streamlit as st

st.set_page_config(layout="wide")

if 'kondisi' not in st.session_state:
    st.session_state['kondisi']={'awal':True, 'Pertemuan1':False}


#------------------------------------

def materi1():
    tulisHTML='''
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bahan Ajar Projek Penelitian – PGSD</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #1a1209;
    --paper: #f5f0e8;
    --cream: #ede8da;
    --accent: #8b2a0f;
    --gold: #c8951a;
    --muted: #6b5f4e;
    --light-rule: #d4c9b0;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--paper);
    color: var(--ink);
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 16px;
    line-height: 1.75;
    overflow-x: hidden;
  }

  /* ─── NOISE TEXTURE overlay ─── */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none; z-index: 999;
  }

  /* ─── TOP RULE ─── */
  .top-stripe {
    background: var(--accent);
    height: 6px;
  }

  /* ─── HEADER ─── */
  header {
    background: var(--ink);
    color: var(--paper);
    padding: 60px 80px 50px;
    position: relative;
    overflow: hidden;
  }
  header::after {
    content: '✦';
    position: absolute;
    right: 60px; top: 50%;
    transform: translateY(-50%);
    font-size: 160px;
    color: var(--accent);
    opacity: 0.12;
    line-height: 1;
  }
  .header-label {
    font-family: 'Source Serif 4', serif;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 16px;
  }
  header h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 5vw, 60px);
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 12px;
  }
  header h1 span { color: var(--gold); }
  header p {
    font-size: 15px;
    color: #b0a898;
    font-style: italic;
  }

  /* ─── NAV ─── */
  nav {
    background: var(--cream);
    border-bottom: 1px solid var(--light-rule);
    padding: 0 80px;
    display: flex;
    gap: 0;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  nav a {
    display: block;
    padding: 16px 20px;
    font-size: 12px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
    text-decoration: none;
    border-bottom: 2px solid transparent;
    transition: color .2s, border-color .2s;
    white-space: nowrap;
  }
  nav a:hover, nav a.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
  }

  /* ─── MAIN ─── */
  main {
    max-width: 1080px;
    margin: 0 auto;
    padding: 60px 40px 100px;
  }

  /* ─── SECTIONS ─── */
  .section {
    margin-bottom: 72px;
    opacity: 0;
    transform: translateY(24px);
    transition: opacity .6s ease, transform .6s ease;
  }
  .section.visible { opacity: 1; transform: none; }

  .section-header {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 32px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--light-rule);
  }
  .section-num {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    font-weight: 900;
    color: var(--light-rule);
    line-height: 1;
  }
  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 700;
    color: var(--ink);
  }
  .section-title small {
    display: block;
    font-family: 'Source Serif 4', serif;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 400;
    margin-bottom: 2px;
  }

  /* ─── IDENTITY TABLE ─── */
  .identity-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2px;
    background: var(--light-rule);
    border: 1px solid var(--light-rule);
  }
  .identity-row {
    display: contents;
  }
  .identity-key {
    background: var(--cream);
    padding: 14px 20px;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 600;
  }
  .identity-val {
    background: var(--paper);
    padding: 14px 20px;
    font-size: 15px;
    color: var(--ink);
  }
  .identity-val.capaian {
    font-style: italic;
    line-height: 1.6;
    font-size: 14px;
    color: var(--muted);
  }
  .identity-row:first-child .identity-key,
  .identity-row:first-child .identity-val {
    background: var(--ink);
    color: var(--paper);
    font-weight: 600;
  }
  .identity-row:first-child .identity-key { color: var(--gold); }

  /* ─── CPL LIST ─── */
  .cpl-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .cpl-list li {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 16px 20px;
    background: var(--cream);
    border-left: 3px solid var(--accent);
    transition: background .2s;
  }
  .cpl-list li:hover { background: #e4ddd0; }
  .cpl-num {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 900;
    color: var(--accent);
    min-width: 32px;
    line-height: 1.2;
  }
  .cpl-text { font-size: 15px; color: var(--ink); }

  /* ─── PHASE TABLE ─── */
  .phase-grid {
    display: grid;
    grid-template-columns: 140px 120px 1fr 100px;
    gap: 2px;
    background: var(--light-rule);
    border: 1px solid var(--light-rule);
  }
  .phase-head {
    background: var(--ink);
    color: var(--gold);
    padding: 12px 18px;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 600;
  }
  .phase-cell {
    background: var(--paper);
    padding: 14px 18px;
    font-size: 14px;
    color: var(--ink);
    vertical-align: middle;
  }
  .phase-cell.phase-name {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 15px;
  }
  .phase-cell.persiapan { border-left: 4px solid #5b8a52; }
  .phase-cell.perancangan { border-left: 4px solid #4a7fa5; }
  .phase-cell.pelaksanaan { border-left: 4px solid #c8951a; }
  .phase-cell.analisis { border-left: 4px solid var(--accent); }

  .badge {
    display: inline-block;
    background: var(--ink);
    color: var(--paper);
    font-size: 11px;
    padding: 3px 10px;
    letter-spacing: 1px;
    font-weight: 600;
  }

  /* ─── PROGRESS BAR ─── */
  .progress-track {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 24px;
  }
  .progress-item { display: flex; align-items: center; gap: 14px; }
  .progress-label {
    min-width: 160px;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--muted);
  }
  .progress-bar-bg {
    flex: 1; height: 8px;
    background: var(--light-rule);
  }
  .progress-bar-fill {
    height: 100%;
    width: 0;
    transition: width 1s ease .4s;
  }
  .progress-pct {
    min-width: 36px;
    font-family: 'Playfair Display', serif;
    font-size: 14px;
    font-weight: 700;
    color: var(--ink);
    text-align: right;
  }
  .fill-persiapan { background: #5b8a52; }
  .fill-perancangan { background: #4a7fa5; }
  .fill-pelaksanaan { background: #c8951a; }
  .fill-analisis { background: var(--accent); }

  /* ─── CONTENT CARD ─── */
  .card {
    background: var(--cream);
    border: 1px solid var(--light-rule);
    padding: 28px 32px;
    margin-bottom: 16px;
    position: relative;
  }
  .card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: var(--gold);
  }
  .card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--ink);
  }
  .card p {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.8;
  }

  /* ─── TABS ─── */
  .tabs { margin-top: 8px; }
  .tab-buttons {
    display: flex;
    gap: 0;
    border-bottom: 1px solid var(--light-rule);
    margin-bottom: 24px;
  }
  .tab-btn {
    background: none; border: none;
    padding: 10px 22px;
    font-family: 'Source Serif 4', serif;
    font-size: 13px;
    color: var(--muted);
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: .2s;
    letter-spacing: .5px;
  }
  .tab-btn.active {
    color: var(--accent);
    border-bottom-color: var(--accent);
    font-weight: 600;
  }
  .tab-panel { display: none; }
  .tab-panel.active { display: block; }

  /* ─── FOOTER ─── */
  footer {
    background: var(--ink);
    color: #7a6e5f;
    text-align: center;
    padding: 36px 40px;
    font-size: 12px;
    letter-spacing: 1px;
  }
  footer strong { color: var(--gold); }

  /* ─── SCROLL TO TOP ─── */
  #totop {
    position: fixed;
    bottom: 32px; right: 32px;
    width: 44px; height: 44px;
    background: var(--accent);
    color: var(--paper);
    border: none;
    cursor: pointer;
    font-size: 18px;
    display: flex; align-items: center; justify-content: center;
    opacity: 0; pointer-events: none;
    transition: opacity .3s;
    z-index: 200;
  }
  #totop.show { opacity: 1; pointer-events: all; }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 700px) {
    header { padding: 40px 24px 36px; }
    nav { padding: 0 12px; overflow-x: auto; }
    main { padding: 40px 20px 80px; }
    .phase-grid { grid-template-columns: 1fr 1fr; }
    .phase-head:nth-child(3), .phase-head:nth-child(4),
    .phase-cell:nth-child(4n+3), .phase-cell:nth-child(4n) { display: none; }
    .identity-grid { grid-template-columns: 1fr; }
    .identity-key { border-bottom: none; padding-bottom: 4px; }
    .identity-val { padding-top: 4px; margin-bottom: 8px; border-bottom: 1px solid var(--light-rule); }
    .identity-row:first-child .identity-key,
    .identity-row:first-child .identity-val { background: var(--ink); }
  }
</style>
</head>
<body>

<div class="top-stripe"></div>

<header>
  <div class="header-label">Program Studi Pendidikan Guru Sekolah Dasar</div>
  <h1>Bahan Ajar<br><span>Projek Penelitian</span></h1>
  <p>Kode: PGSD &ensp;·&ensp; 4 SKS &ensp;·&ensp; Semester VI</p>
</header>

<nav>
  <a href="#identitas" class="active">Identitas</a>
  <a href="#cpl">Capaian</a>
  <a href="#distribusi">Distribusi</a>
  <a href="#materi">Materi</a>
  <a href="#penilaian">Penilaian</a>
</nav>

<main>

  <!-- I. IDENTITAS -->
  <section class="section" id="identitas">
    <div class="section-header">
      <span class="section-num">I</span>
      <div class="section-title">
        <small>Bagian Pertama</small>
        Identitas Mata Kuliah
      </div>
    </div>

    <div class="identity-grid">
      <div class="identity-row">
        <div class="identity-key">Komponen</div>
        <div class="identity-val">Keterangan</div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Nama Mata Kuliah</div>
        <div class="identity-val">Projek Penelitian</div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Kode Mata Kuliah</div>
        <div class="identity-val">PGS-XXX</div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Bobot SKS</div>
        <div class="identity-val">4 SKS <em>(2 Teori + 2 Praktik)</em></div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Semester</div>
        <div class="identity-val">VI (Enam)</div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Prasyarat</div>
        <div class="identity-val">Metodologi Penelitian, Statistik Pendidikan</div>
      </div>
      <div class="identity-row">
        <div class="identity-key">Capaian Pembelajaran</div>
        <div class="identity-val capaian">Mahasiswa mampu merancang, melaksanakan, dan menyusun laporan penelitian tindakan kelas (PTK) yang berkualitas untuk perbaikan pembelajaran di SD</div>
      </div>
    </div>
  </section>

  <!-- II. RPS / CPL -->
  <section class="section" id="cpl">
    <div class="section-header">
      <span class="section-num">II</span>
      <div class="section-title">
        <small>Rencana Pembelajaran Semester</small>
        Capaian Pembelajaran Lulusan
      </div>
    </div>

    <ul class="cpl-list">
      <li>
        <span class="cpl-num">1</span>
        <span class="cpl-text">Menguasai konsep dan teori penelitian tindakan kelas</span>
      </li>
      <li>
        <span class="cpl-num">2</span>
        <span class="cpl-text">Mampu mengidentifikasi masalah pembelajaran di kelas</span>
      </li>
      <li>
        <span class="cpl-num">3</span>
        <span class="cpl-text">Mampu merancang dan melaksanakan penelitian tindakan kelas</span>
      </li>
      <li>
        <span class="cpl-num">4</span>
        <span class="cpl-text">Mampu menganalisis data dan menyimpulkan hasil penelitian</span>
      </li>
      <li>
        <span class="cpl-num">5</span>
        <span class="cpl-text">Mampu menyusun laporan penelitian yang sistematis dan ilmiah</span>
      </li>
    </ul>
  </section>

  <!-- III. DISTRIBUSI PERTEMUAN -->
  <section class="section" id="distribusi">
    <div class="section-header">
      <span class="section-num">III</span>
      <div class="section-title">
        <small>RPS – Jadwal Perkuliahan</small>
        Distribusi Pertemuan
      </div>
    </div>

    <div class="phase-grid">
      <div class="phase-head">Fase</div>
      <div class="phase-head">Pertemuan</div>
      <div class="phase-head">Topik</div>
      <div class="phase-head">Bobot</div>

      <div class="phase-cell phase-name persiapan">Persiapan</div>
      <div class="phase-cell"><span class="badge">1–3</span></div>
      <div class="phase-cell">Fundamen &amp; Perencanaan</div>
      <div class="phase-cell">20%</div>

      <div class="phase-cell phase-name perancangan">Perancangan</div>
      <div class="phase-cell"><span class="badge">4–7</span></div>
      <div class="phase-cell">Desain &amp; Instrumentasi</div>
      <div class="phase-cell">25%</div>

      <div class="phase-cell phase-name pelaksanaan">Pelaksanaan</div>
      <div class="phase-cell"><span class="badge">8–11</span></div>
      <div class="phase-cell">Implementasi &amp; Pengumpulan Data</div>
      <div class="phase-cell">25%</div>

      <div class="phase-cell phase-name analisis">Analisis &amp; Pelaporan</div>
      <div class="phase-cell"><span class="badge">12–16</span></div>
      <div class="phase-cell">Analisis, Laporan &amp; Presentasi</div>
      <div class="phase-cell">30%</div>
    </div>

    <div class="progress-track" style="margin-top:28px;">
      <div class="progress-item">
        <span class="progress-label">Persiapan</span>
        <div class="progress-bar-bg"><div class="progress-bar-fill fill-persiapan" data-w="20"></div></div>
        <span class="progress-pct">20%</span>
      </div>
      <div class="progress-item">
        <span class="progress-label">Perancangan</span>
        <div class="progress-bar-bg"><div class="progress-bar-fill fill-perancangan" data-w="25"></div></div>
        <span class="progress-pct">25%</span>
      </div>
      <div class="progress-item">
        <span class="progress-label">Pelaksanaan</span>
        <div class="progress-bar-bg"><div class="progress-bar-fill fill-pelaksanaan" data-w="25"></div></div>
        <span class="progress-pct">25%</span>
      </div>
      <div class="progress-item">
        <span class="progress-label">Analisis &amp; Laporan</span>
        <div class="progress-bar-bg"><div class="progress-bar-fill fill-analisis" data-w="30"></div></div>
        <span class="progress-pct">30%</span>
      </div>
    </div>
  </section>

  <!-- IV. MATERI (TABS) -->
  <section class="section" id="materi">
    <div class="section-header">
      <span class="section-num">IV</span>
      <div class="section-title">
        <small>Konten Perkuliahan</small>
        Pokok Materi
      </div>
    </div>

    <div class="tabs">
      <div class="tab-buttons">
        <button class="tab-btn active" data-tab="t1">Persiapan</button>
        <button class="tab-btn" data-tab="t2">Perancangan</button>
        <button class="tab-btn" data-tab="t3">Pelaksanaan</button>
        <button class="tab-btn" data-tab="t4">Analisis</button>
      </div>

      <div class="tab-panel active" id="t1">
        <div class="card">
          <h3>Pertemuan 1 – Pengantar PTK</h3>
          <p>Hakikat, karakteristik, dan manfaat penelitian tindakan kelas. Paradigma penelitian kualitatif-kuantitatif dalam konteks PTK. Etika penelitian di lingkungan sekolah dasar.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 2 – Identifikasi Masalah</h3>
          <p>Teknik observasi kelas, jurnal reflektif guru, dan wawancara siswa. Analisis akar masalah (root cause analysis) dalam pembelajaran SD. Perumusan fokus permasalahan yang tajam dan terukur.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 3 – Kajian Literatur</h3>
          <p>Strategi penelusuran pustaka ilmiah (SINTA, Google Scholar). Penyusunan kerangka teori dan kerangka berpikir. Teknik parafrase dan sitasi sesuai APA 7th Edition.</p>
        </div>
      </div>

      <div class="tab-panel" id="t2">
        <div class="card">
          <h3>Pertemuan 4–5 – Desain PTK</h3>
          <p>Model spiral Kemmis &amp; McTaggart vs. model Hopkins. Perencanaan siklus: indikator keberhasilan, KKM, dan kriteria refleksi. Penyusunan proposal penelitian yang komprehensif.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 6–7 – Instrumentasi</h3>
          <p>Pengembangan lembar observasi, rubrik penilaian, dan pedoman wawancara. Uji validitas isi (content validity) oleh ahli. Reliabilitas instrumen dan kalibrasi observer.</p>
        </div>
      </div>

      <div class="tab-panel" id="t3">
        <div class="card">
          <h3>Pertemuan 8–9 – Implementasi Siklus I</h3>
          <p>Pelaksanaan tindakan sesuai RPP yang dirancang. Pengumpulan data observasi, catatan lapangan, dan dokumentasi. Refleksi siklus I dan perencanaan perbaikan.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 10–11 – Implementasi Siklus II</h3>
          <p>Perbaikan tindakan berdasarkan hasil refleksi. Triangulasi sumber data: guru, siswa, dokumen. Penentuan keberlanjutan siklus berdasarkan data empiris.</p>
        </div>
      </div>

      <div class="tab-panel" id="t4">
        <div class="card">
          <h3>Pertemuan 12–13 – Analisis Data</h3>
          <p>Analisis data kuantitatif: statistik deskriptif, persentase ketuntasan. Analisis data kualitatif: reduksi, penyajian, penarikan simpulan (Miles &amp; Huberman). Interpretasi hasil dan pembahasan komparatif antar-siklus.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 14 – Penulisan Laporan</h3>
          <p>Struktur laporan PTK sesuai standar LPPM dan jurnal ilmiah. Teknik penulisan pembahasan yang argumentatif. Penyusunan abstrak, simpulan, dan saran yang efektif.</p>
        </div>
        <div class="card">
          <h3>Pertemuan 15–16 – Presentasi &amp; Seminar</h3>
          <p>Teknik presentasi ilmiah yang efektif. Tanya-jawab dan pertahanan argumentasi penelitian. Revisi laporan final berdasarkan masukan seminar.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- V. PENILAIAN -->
  <section class="section" id="penilaian">
    <div class="section-header">
      <span class="section-num">V</span>
      <div class="section-title">
        <small>Evaluasi Pembelajaran</small>
        Komponen Penilaian
      </div>
    </div>

    <div class="phase-grid">
      <div class="phase-head">Komponen</div>
      <div class="phase-head">Bentuk</div>
      <div class="phase-head">Deskripsi</div>
      <div class="phase-head">Bobot</div>

      <div class="phase-cell phase-name persiapan">Proposal</div>
      <div class="phase-cell">Dokumen Tertulis</div>
      <div class="phase-cell">Kelengkapan &amp; kualitas proposal PTK</div>
      <div class="phase-cell">20%</div>

      <div class="phase-cell phase-name perancangan">Instrumen</div>
      <div class="phase-cell">Portofolio</div>
      <div class="phase-cell">Validitas &amp; reliabilitas instrumen penelitian</div>
      <div class="phase-cell">15%</div>

      <div class="phase-cell phase-name pelaksanaan">Proses PTK</div>
      <div class="phase-cell">Observasi</div>
      <div class="phase-cell">Pelaksanaan tindakan &amp; pengumpulan data</div>
      <div class="phase-cell">25%</div>

      <div class="phase-cell phase-name analisis">Laporan</div>
      <div class="phase-cell">Karya Ilmiah</div>
      <div class="phase-cell">Kualitas laporan akhir PTK</div>
      <div class="phase-cell">25%</div>

      <div class="phase-cell phase-name analisis" style="border-left-color:var(--ink)">Presentasi</div>
      <div class="phase-cell">Seminar</div>
      <div class="phase-cell">Kemampuan presentasi &amp; mempertahankan argumen</div>
      <div class="phase-cell">15%</div>
    </div>
  </section>

</main>

<footer>
  <strong>Bahan Ajar Projek Penelitian</strong> &ensp;·&ensp;
  Program Studi PGSD &ensp;·&ensp; Semester VI &ensp;·&ensp; PGS-XXX
  <br><br>
  Template ini dapat disesuaikan dengan kebijakan program studi masing-masing institusi.
</footer>

<button id="totop" title="Kembali ke atas" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>

<script>
  /* ── NAV ACTIVE ── */
  const sections = document.querySelectorAll('section.section');
  const navLinks = document.querySelectorAll('nav a');

  /* ── INTERSECTION OBSERVER (reveal + nav) ── */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        // animate progress bars if in distribusi
        e.target.querySelectorAll('.progress-bar-fill').forEach(bar => {
          bar.style.width = bar.dataset.w + '%';
        });
      }
    });
  }, { threshold: 0.12 });
  sections.forEach(s => io.observe(s));

  /* ── NAV HIGHLIGHT ── */
  window.addEventListener('scroll', () => {
    let cur = '';
    sections.forEach(s => {
      if (window.scrollY >= s.offsetTop - 100) cur = s.id;
    });
    navLinks.forEach(a => {
      a.classList.toggle('active', a.getAttribute('href') === '#' + cur);
    });
    document.getElementById('totop').classList.toggle('show', window.scrollY > 300);
  });

  /* ── TABS ── */
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      btn.closest('.tabs').querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.closest('.tabs').querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(target).classList.add('active');
    });
  });

  /* ── SMOOTH NAV SCROLL ── */
  navLinks.forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector(a.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
    });
  });
</script>
</body>
</html>
    '''
    st.components.v1.html(tulisHTML,height=4000)

def materi2():
    tulisHTML='''
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pertemuan 1 – Pengantar Projek Penelitian</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0f1923;
    --surface: #162030;
    --surface2: #1c2a3a;
    --border: #243347;
    --text: #e8edf2;
    --muted: #7a93aa;
    --dim: #3d5368;
    --teal: #2ec4b6;
    --teal-dim: #1a7a74;
    --amber: #f4a435;
    --amber-dim: #7d5218;
    --rose: #e05c7a;
    --rose-dim: #6e2d3c;
    --sage: #6cbf8e;
    --sage-dim: #2d5e40;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 15.5px;
    line-height: 1.8;
    min-height: 100vh;
  }

  /* BG GRID */
  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
      linear-gradient(var(--border) 1px, transparent 1px),
      linear-gradient(90deg, var(--border) 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: .35;
    pointer-events: none;
    z-index: 0;
  }

  /* GLOW ORBS */
  .orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
    z-index: 0;
  }
  .orb-1 { width: 400px; height: 400px; background: rgba(46,196,182,.07); top: -100px; right: -100px; }
  .orb-2 { width: 350px; height: 350px; background: rgba(244,164,53,.06); bottom: 200px; left: -80px; }

  /* LAYOUT */
  .wrap { position: relative; z-index: 1; max-width: 960px; margin: 0 auto; padding: 0 28px 100px; }

  /* ─── HEADER ─── */
  .page-header {
    padding: 64px 0 48px;
    position: relative;
  }
  .breadcrumb {
    font-size: 11px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .breadcrumb::before {
    content: '';
    display: inline-block;
    width: 28px; height: 1px;
    background: var(--teal);
  }
  .page-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(28px, 5vw, 52px);
    line-height: 1.15;
    color: var(--text);
    margin-bottom: 16px;
  }
  .page-header h1 em {
    font-style: italic;
    color: var(--teal);
  }
  .header-meta {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 24px;
  }
  .meta-tag {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 12px;
    letter-spacing: .5px;
    color: var(--muted);
    border: 1px solid var(--border);
    padding: 6px 14px;
    border-radius: 2px;
  }
  .meta-tag .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
  }

  /* ─── DIVIDER ─── */
  .rule {
    height: 1px;
    background: linear-gradient(to right, var(--teal), var(--border) 60%, transparent);
    margin-bottom: 52px;
  }

  /* ─── SECTION TITLE ─── */
  .sec-label {
    font-size: 10.5px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 10px;
  }
  .sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
  h2 {
    font-family: 'DM Serif Display', serif;
    font-size: 26px;
    color: var(--text);
    margin-bottom: 28px;
  }

  /* ─── TUJUAN CARDS ─── */
  .goals-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 14px;
    margin-bottom: 60px;
  }
  .goal-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-top: 2px solid var(--teal);
    padding: 22px 24px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity .5s ease, transform .5s ease, background .2s;
  }
  .goal-card:nth-child(2) { transition-delay: .1s; border-top-color: var(--amber); }
  .goal-card:nth-child(3) { transition-delay: .2s; border-top-color: var(--sage); }
  .goal-card.vis { opacity: 1; transform: none; }
  .goal-card:hover { background: var(--surface2); }
  .goal-num {
    font-family: 'DM Serif Display', serif;
    font-size: 36px;
    line-height: 1;
    color: var(--border);
    margin-bottom: 12px;
  }
  .goal-card p { font-size: 14px; color: var(--muted); line-height: 1.7; }

  /* ─── SECTION BLOCK ─── */
  .section-block {
    margin-bottom: 56px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity .6s ease, transform .6s ease;
  }
  .section-block.vis { opacity: 1; transform: none; }

  /* ─── DEFINITION BOX ─── */
  .definition {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--teal);
    padding: 24px 28px;
    margin-bottom: 28px;
    position: relative;
  }
  .def-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--teal);
    margin-bottom: 10px;
  }
  .definition p {
    font-size: 15px;
    color: var(--text);
    line-height: 1.85;
  }
  .definition cite {
    display: block;
    font-size: 12px;
    color: var(--muted);
    margin-top: 12px;
    font-style: normal;
  }

  /* ─── SIKLUS PTK ─── */
  .siklus-wrap {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 32px;
  }
  .siklus-item {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 18px 22px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
    cursor: default;
    transition: border-color .2s, background .2s;
  }
  .siklus-item:hover { background: var(--surface2); border-color: var(--teal-dim); }
  .siklus-icon {
    width: 38px; height: 38px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
  }
  .siklus-item:nth-child(1) .siklus-icon { background: rgba(46,196,182,.12); color: var(--teal); }
  .siklus-item:nth-child(2) .siklus-icon { background: rgba(244,164,53,.12); color: var(--amber); }
  .siklus-item:nth-child(3) .siklus-icon { background: rgba(108,191,142,.12); color: var(--sage); }
  .siklus-item:nth-child(4) .siklus-icon { background: rgba(224,92,122,.12); color: var(--rose); }
  .siklus-content h4 {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
  }
  .siklus-content p { font-size: 13px; color: var(--muted); line-height: 1.5; }

  /* ─── CYCLE DIAGRAM ─── */
  .cycle-diagram {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 32px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 28px;
  }
  .cycle-svg { width: 100%; max-width: 420px; height: auto; }

  /* ─── COMPARISON TABLE ─── */
  .comp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin-bottom: 8px;
  }
  .comp-table th {
    background: var(--surface2);
    color: var(--teal);
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 14px 18px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    font-weight: 600;
  }
  .comp-table th:first-child { color: var(--muted); }
  .comp-table td {
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: middle;
  }
  .comp-table tr:last-child td { border-bottom: none; }
  .comp-table td:first-child {
    color: var(--amber);
    font-weight: 600;
    font-size: 13px;
    white-space: nowrap;
    background: var(--surface);
  }
  .comp-table td:nth-child(2) { background: rgba(22,32,48,.5); color: var(--muted); }
  .comp-table td:nth-child(3) { background: rgba(46,196,182,.04); color: var(--text); }
  .comp-table tr:hover td { background: var(--surface2); }
  .comp-table tr:hover td:first-child { background: rgba(244,164,53,.06); }

  /* ─── MANFAAT LIST ─── */
  .benefit-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
  }
  .benefit-item {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 18px 20px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
    transition: border-color .2s;
  }
  .benefit-item:hover { border-color: var(--sage-dim); }
  .benefit-icon { color: var(--sage); font-size: 18px; margin-top: 2px; flex-shrink: 0; }
  .benefit-text { font-size: 13.5px; color: var(--muted); line-height: 1.6; }

  /* ─── AKTIVITAS ─── */
  .activity-list { display: flex; flex-direction: column; gap: 14px; }
  .activity-item {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 20px 24px;
    display: flex;
    gap: 18px;
    align-items: flex-start;
    position: relative;
    overflow: hidden;
  }
  .activity-item::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
  }
  .activity-item:nth-child(1)::before { background: var(--teal); }
  .activity-item:nth-child(2)::before { background: var(--amber); }
  .activity-item:nth-child(3)::before { background: var(--sage); }
  .activity-num {
    width: 32px; height: 32px;
    border-radius: 50%;
    background: var(--surface2);
    border: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    font-weight: 600;
    color: var(--muted);
    flex-shrink: 0;
  }
  .activity-content h4 { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
  .activity-content p { font-size: 13.5px; color: var(--muted); line-height: 1.6; }

  /* ─── TUGAS MANDIRI ─── */
  .tugas-box {
    background: var(--surface);
    border: 1px solid var(--teal-dim);
    padding: 32px 36px;
    position: relative;
    overflow: hidden;
  }
  .tugas-box::before {
    content: '📋';
    position: absolute;
    right: 28px; top: 24px;
    font-size: 48px;
    opacity: .08;
  }
  .tugas-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(46,196,182,.1);
    border: 1px solid var(--teal-dim);
    color: var(--teal);
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 5px 14px;
    margin-bottom: 18px;
  }
  .tugas-box h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    color: var(--text);
    margin-bottom: 14px;
  }
  .tugas-box p { font-size: 14.5px; color: var(--muted); line-height: 1.85; margin-bottom: 20px; }

  .tugas-sub {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .tugas-point {
    display: flex;
    gap: 12px;
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 12px 16px;
    align-items: flex-start;
  }
  .tugas-letter {
    width: 24px; height: 24px;
    background: var(--teal-dim);
    color: var(--teal);
    font-size: 11px;
    font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    border-radius: 2px;
  }
  .tugas-point p { font-size: 13.5px; color: var(--muted); margin: 0; line-height: 1.6; }

  /* ─── STICKY NAV ─── */
  .sticky-nav {
    position: fixed;
    right: 24px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 8px;
    z-index: 100;
  }
  .nav-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--dim);
    cursor: pointer;
    transition: background .2s, transform .2s;
    position: relative;
  }
  .nav-dot:hover, .nav-dot.active {
    background: var(--teal);
    transform: scale(1.3);
  }
  .nav-dot::after {
    content: attr(data-label);
    position: absolute;
    right: 18px;
    top: 50%;
    transform: translateY(-50%);
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 11px;
    white-space: nowrap;
    padding: 4px 10px;
    pointer-events: none;
    opacity: 0;
    transition: opacity .2s;
    letter-spacing: .5px;
  }
  .nav-dot:hover::after { opacity: 1; }

  /* ─── PROGRESS ─── */
  .reading-bar {
    position: fixed;
    top: 0; left: 0;
    height: 2px;
    background: var(--teal);
    z-index: 200;
    width: 0;
    transition: width .1s;
  }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 640px) {
    .siklus-wrap { grid-template-columns: 1fr; }
    .sticky-nav { display: none; }
    .tugas-box { padding: 24px 20px; }
    .comp-table th, .comp-table td { padding: 10px 12px; font-size: 13px; }
  }
</style>
</head>
<body>

<div class="reading-bar" id="readbar"></div>
<div class="orb orb-1"></div>
<div class="orb orb-2"></div>

<!-- STICKY SIDE NAV -->
<nav class="sticky-nav">
  <div class="nav-dot active" data-section="header" data-label="Atas"></div>
  <div class="nav-dot" data-section="tujuan" data-label="Tujuan"></div>
  <div class="nav-dot" data-section="definisi" data-label="A. Definisi"></div>
  <div class="nav-dot" data-section="karakteristik" data-label="B. Karakteristik"></div>
  <div class="nav-dot" data-section="manfaat" data-label="C. Manfaat"></div>
  <div class="nav-dot" data-section="aktivitas" data-label="Aktivitas"></div>
  <div class="nav-dot" data-section="tugas" data-label="Tugas"></div>
</nav>

<div class="wrap">

  <!-- HEADER -->
  <header class="page-header" id="header">
    <div class="breadcrumb">PGSD · Projek Penelitian · Pertemuan 1</div>
    <h1>Pengantar <em>Projek Penelitian</em><br>&amp; Orientasi Mata Kuliah</h1>
    <div class="header-meta">
      <span class="meta-tag"><span class="dot" style="background:var(--teal)"></span> Pertemuan 1</span>
      <span class="meta-tag"><span class="dot" style="background:var(--amber)"></span> Semester VI</span>
      <span class="meta-tag"><span class="dot" style="background:var(--sage)"></span> Fase Persiapan</span>
      <span class="meta-tag"><span class="dot" style="background:var(--rose)"></span> Bobot 20%</span>
    </div>
  </header>

  <div class="rule"></div>

  <!-- TUJUAN PEMBELAJARAN -->
  <section id="tujuan">
    <div class="sec-label">Tujuan Pembelajaran</div>
    <h2>Yang Akan Anda Capai</h2>
    <div class="goals-grid">
      <div class="goal-card">
        <div class="goal-num">01</div>
        <p>Memahami ruang lingkup dan tujuan mata kuliah Projek Penelitian</p>
      </div>
      <div class="goal-card">
        <div class="goal-num">02</div>
        <p>Menjelaskan pentingnya penelitian bagi guru SD dalam konteks profesionalisme</p>
      </div>
      <div class="goal-card">
        <div class="goal-num">03</div>
        <p>Mengidentifikasi perbedaan penelitian ilmiah dan penelitian tindakan kelas (PTK)</p>
      </div>
    </div>
  </section>

  <!-- A. DEFINISI -->
  <section class="section-block" id="definisi">
    <div class="sec-label">Materi Pokok A</div>
    <h2>Definisi dan Konsep Dasar</h2>

    <div class="definition">
      <div class="def-label">Definisi PTK</div>
      <p>Penelitian Tindakan Kelas (PTK) adalah penelitian yang dilakukan oleh guru di kelasnya sendiri dengan tujuan memperbaiki kualitas pembelajaran. PTK bersifat kolaboratif, reflektif, dan berkelanjutan sehingga dapat diterapkan langsung dalam konteks nyata oleh guru.</p>
      <cite>— Kemmis &amp; McTaggart, 1988</cite>
    </div>

    <p style="color:var(--muted);font-size:14.5px;margin-bottom:20px;">Menurut Kemmis &amp; McTaggart (1988), PTK memiliki <strong style="color:var(--text)">empat komponen utama</strong> yang membentuk sebuah siklus berulang:</p>

    <div class="siklus-wrap">
      <div class="siklus-item">
        <div class="siklus-icon">📐</div>
        <div class="siklus-content">
          <h4>Perencanaan <span style="color:var(--muted);font-weight:400;font-size:12px">(Planning)</span></h4>
          <p>Merancang tindakan perbaikan berdasarkan identifikasi masalah</p>
        </div>
      </div>
      <div class="siklus-item">
        <div class="siklus-icon">⚡</div>
        <div class="siklus-content">
          <h4>Tindakan <span style="color:var(--muted);font-weight:400;font-size:12px">(Action)</span></h4>
          <p>Melaksanakan rencana yang telah disusun di kelas nyata</p>
        </div>
      </div>
      <div class="siklus-item">
        <div class="siklus-icon">🔍</div>
        <div class="siklus-content">
          <h4>Pengamatan <span style="color:var(--muted);font-weight:400;font-size:12px">(Observation)</span></h4>
          <p>Mengumpulkan data dan merekam proses tindakan</p>
        </div>
      </div>
      <div class="siklus-item">
        <div class="siklus-icon">🔄</div>
        <div class="siklus-content">
          <h4>Refleksi <span style="color:var(--muted);font-weight:400;font-size:12px">(Reflection)</span></h4>
          <p>Mengevaluasi hasil dan merencanakan siklus berikutnya</p>
        </div>
      </div>
    </div>

    <!-- SVG Cycle Diagram -->
    <div class="cycle-diagram">
      <svg class="cycle-svg" viewBox="0 0 400 340" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Center circle -->
        <circle cx="200" cy="170" r="42" fill="#162030" stroke="#243347" stroke-width="1.5"/>
        <text x="200" y="166" text-anchor="middle" fill="#7a93aa" font-size="10" font-family="DM Sans, sans-serif" letter-spacing="1">SIKLUS</text>
        <text x="200" y="180" text-anchor="middle" fill="#7a93aa" font-size="10" font-family="DM Sans, sans-serif" letter-spacing="1">PTK</text>

        <!-- Nodes -->
        <!-- Planning (top) -->
        <circle cx="200" cy="52" r="36" fill="#1c2a3a" stroke="#1a7a74" stroke-width="1.5"/>
        <text x="200" y="48" text-anchor="middle" fill="#2ec4b6" font-size="11" font-family="DM Sans, sans-serif" font-weight="600">Planning</text>
        <text x="200" y="62" text-anchor="middle" fill="#7a93aa" font-size="9.5" font-family="DM Sans, sans-serif">Perencanaan</text>

        <!-- Action (right) -->
        <circle cx="332" cy="170" r="36" fill="#1c2a3a" stroke="#7d5218" stroke-width="1.5"/>
        <text x="332" y="166" text-anchor="middle" fill="#f4a435" font-size="11" font-family="DM Sans, sans-serif" font-weight="600">Action</text>
        <text x="332" y="180" text-anchor="middle" fill="#7a93aa" font-size="9.5" font-family="DM Sans, sans-serif">Tindakan</text>

        <!-- Observation (bottom) -->
        <circle cx="200" cy="288" r="36" fill="#1c2a3a" stroke="#2d5e40" stroke-width="1.5"/>
        <text x="200" y="284" text-anchor="middle" fill="#6cbf8e" font-size="11" font-family="DM Sans, sans-serif" font-weight="600">Observation</text>
        <text x="200" y="298" text-anchor="middle" fill="#7a93aa" font-size="9.5" font-family="DM Sans, sans-serif">Pengamatan</text>

        <!-- Reflection (left) -->
        <circle cx="68" cy="170" r="36" fill="#1c2a3a" stroke="#6e2d3c" stroke-width="1.5"/>
        <text x="68" y="166" text-anchor="middle" fill="#e05c7a" font-size="11" font-family="DM Sans, sans-serif" font-weight="600">Reflection</text>
        <text x="68" y="180" text-anchor="middle" fill="#7a93aa" font-size="9.5" font-family="DM Sans, sans-serif">Refleksi</text>

        <!-- Arrows (curved arcs) -->
        <path d="M 228 75 Q 300 90 310 140" stroke="#2ec4b6" stroke-width="1.5" fill="none" marker-end="url(#arrowTeal)"/>
        <path d="M 318 200 Q 310 270 235 278" stroke="#f4a435" stroke-width="1.5" fill="none" marker-end="url(#arrowAmber)"/>
        <path d="M 170 282 Q 100 278 86 210" stroke="#6cbf8e" stroke-width="1.5" fill="none" marker-end="url(#arrowSage)"/>
        <path d="M 78 136 Q 86 80 168 62" stroke="#e05c7a" stroke-width="1.5" fill="none" marker-end="url(#arrowRose)"/>

        <defs>
          <marker id="arrowTeal" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
            <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#2ec4b6"/>
          </marker>
          <marker id="arrowAmber" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
            <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#f4a435"/>
          </marker>
          <marker id="arrowSage" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
            <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#6cbf8e"/>
          </marker>
          <marker id="arrowRose" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
            <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#e05c7a"/>
          </marker>
        </defs>
      </svg>
    </div>
  </section>

  <!-- B. KARAKTERISTIK -->
  <section class="section-block" id="karakteristik">
    <div class="sec-label">Materi Pokok B</div>
    <h2>Karakteristik PTK</h2>
    <p style="color:var(--muted);font-size:14.5px;margin-bottom:22px;">Berikut perbandingan antara penelitian ilmiah konvensional dengan penelitian tindakan kelas (PTK) berdasarkan beberapa aspek kunci:</p>

    <div style="overflow-x:auto;margin-bottom:8px;">
      <table class="comp-table">
        <thead>
          <tr>
            <th>Aspek</th>
            <th>Penelitian Ilmiah</th>
            <th>PTK ✦</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Tujuan</td>
            <td>Menemukan teori/kebenaran umum</td>
            <td>Memperbaiki praktik pembelajaran</td>
          </tr>
          <tr>
            <td>Lokasi</td>
            <td>Bervariasi</td>
            <td>Kelas sendiri</td>
          </tr>
          <tr>
            <td>Pelaku</td>
            <td>Peneliti eksternal</td>
            <td>Guru / Sendiri</td>
          </tr>
          <tr>
            <td>Siklus</td>
            <td>Satu kali</td>
            <td>Berulang (siklus)</td>
          </tr>
          <tr>
            <td>Fokus</td>
            <td>Umum</td>
            <td>Spesifik pada masalah kelas</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:12px;color:var(--dim);">✦ PTK lebih kontekstual, praktis, dan berorientasi pada solusi nyata di lapangan.</p>
  </section>

  <!-- C. MANFAAT -->
  <section class="section-block" id="manfaat">
    <div class="sec-label">Materi Pokok C</div>
    <h2>Manfaat PTK bagi Guru SD</h2>
    <div class="benefit-list">
      <div class="benefit-item">
        <span class="benefit-icon">🎯</span>
        <span class="benefit-text">Memecahkan masalah pembelajaran yang nyata di kelas</span>
      </div>
      <div class="benefit-item">
        <span class="benefit-icon">🌱</span>
        <span class="benefit-text">Mengembangkan profesionalisme keguruan secara berkelanjutan</span>
      </div>
      <div class="benefit-item">
        <span class="benefit-icon">📈</span>
        <span class="benefit-text">Meningkatkan hasil belajar siswa secara terukur</span>
      </div>
      <div class="benefit-item">
        <span class="benefit-icon">📝</span>
        <span class="benefit-text">Menghasilkan karya tulis ilmiah yang dapat dipublikasikan</span>
      </div>
    </div>
  </section>

  <!-- AKTIVITAS -->
  <section class="section-block" id="aktivitas">
    <div class="sec-label">Aktivitas Pembelajaran</div>
    <h2>Kegiatan di Kelas</h2>
    <div class="activity-list">
      <div class="activity-item">
        <div class="activity-num">1</div>
        <div class="activity-content">
          <h4>Ice Breaking: "Masalahku, Solusiku"</h4>
          <p>Mahasiswa berbagi pengalaman masalah pembelajaran saat PPL secara bergantian. Setiap mahasiswa menceritakan satu masalah nyata dan solusi yang pernah dicoba.</p>
        </div>
      </div>
      <div class="activity-item">
        <div class="activity-num">2</div>
        <div class="activity-content">
          <h4>Diskusi Kelompok</h4>
          <p>Analisis kasus PTK sederhana yang telah disiapkan. Kelompok mengidentifikasi komponen PTK, siklus yang digunakan, dan keberhasilan tindakan dalam kasus tersebut.</p>
        </div>
      </div>
      <div class="activity-item">
        <div class="activity-num">3</div>
        <div class="activity-content">
          <h4>Tugas Kelas</h4>
          <p>Menulis refleksi singkat tentang masalah pembelajaran yang pernah dihadapi selama PPL. Dikumpulkan sebelum akhir pertemuan.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- TUGAS MANDIRI -->
  <section class="section-block" id="tugas">
    <div class="sec-label">Evaluasi Mandiri</div>
    <h2>Tugas Mandiri</h2>
    <div class="tugas-box">
      <div class="tugas-badge">📋 Refleksi Jurnal</div>
      <h3>Jurnal Refleksi Pengalaman Mengajar</h3>
      <p>Buat jurnal refleksi <strong style="color:var(--text)">1 halaman</strong> tentang pengalaman Anda mengajar (PPL/Praktik) yang menggambarkan masalah pembelajaran nyata. Tuliskan dengan jujur dan reflektif menggunakan sudut pandang orang pertama.</p>
      <div class="tugas-sub">
        <div class="tugas-point">
          <div class="tugas-letter">a</div>
          <p>Masalah apa yang terjadi dalam proses pembelajaran yang Anda amati atau alami?</p>
        </div>
        <div class="tugas-point">
          <div class="tugas-letter">b</div>
          <p>Bagaimana Anda menangani atau merespons masalah tersebut saat itu?</p>
        </div>
        <div class="tugas-point">
          <div class="tugas-letter">c</div>
          <p>Apakah solusi yang Anda terapkan efektif? Apa indikator keberhasilan atau kegagalannya?</p>
        </div>
      </div>
    </div>
  </section>

</div><!-- /wrap -->

<script>
  // ── READING PROGRESS ──
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = (scrollTop / docHeight) * 100;
    document.getElementById('readbar').style.width = pct + '%';
  });

  // ── INTERSECTION OBSERVER ──
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('vis');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.goal-card, .section-block').forEach(el => io.observe(el));

  // ── STICKY NAV DOTS ──
  const sections = ['header','tujuan','definisi','karakteristik','manfaat','aktivitas','tugas'];
  const dots = document.querySelectorAll('.nav-dot');

  const navIO = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = e.target.id;
        dots.forEach(d => d.classList.toggle('active', d.dataset.section === id));
      }
    });
  }, { rootMargin: '-40% 0px -40% 0px' });

  sections.forEach(id => {
    const el = document.getElementById(id);
    if (el) navIO.observe(el);
  });

  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      const target = document.getElementById(dot.dataset.section);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
</script>
</body>
</html>
    '''
    st.components.v1.html(tulisHTML,height=4000)
#------------------------------------

if st.session_state.kondisi['awal']:
    materi1()
if st.session_state.kondisi['Pertemuan1']:
    materi2()

#-------------------------------------


if st.sidebar.button("pengenalan"):
    st.session_state['kondisi']={'awal':True, 'Pertemuan1':False}
    st.rerun()
if st.sidebar.button("pertemuan1"):
    st.session_state['kondisi']={'awal':False, 'Pertemuan1':True}
    st.rerun()
