-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Agu 2021 pada 13.39
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_kesiapan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_anggaran`
--

CREATE TABLE `data_anggaran` (
  `id_anggaran` int(11) NOT NULL,
  `tahun` int(11) NOT NULL,
  `anggaran` varchar(20) NOT NULL,
  `jumlah` varchar(20) NOT NULL,
  `keterangan` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_anggaran`
--

INSERT INTO `data_anggaran` (`id_anggaran`, `tahun`, `anggaran`, `jumlah`, `keterangan`) VALUES
(1, 2016, '98,1 triliun', '-', '-'),
(2, 2017, '117,3 triliun', '19,2 triliun', 'Bertambah'),
(3, 2018, '106,8 triliun', '10,5 triliun', 'Berkurang'),
(4, 2019, '108,4 triliun', '1,6 triliun', 'Bertambah'),
(5, 2020, '127,4 triliun', '19 triliun', 'Bertambah'),
(10, 2021, '137 triliun', '9,6 triliun', 'Bertambah');

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_kesiapan`
--

CREATE TABLE `data_kesiapan` (
  `id_kesiapan` int(11) NOT NULL,
  `tahun` varchar(10) NOT NULL,
  `sirkulasi` int(11) NOT NULL,
  `bulan` varchar(20) NOT NULL,
  `kekuatan` int(11) DEFAULT NULL,
  `nilai_kesiapan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_kesiapan`
--

INSERT INTO `data_kesiapan` (`id_kesiapan`, `tahun`, `sirkulasi`, `bulan`, `kekuatan`, `nilai_kesiapan`) VALUES
(1, '2016', 2, 'Januari', 220, 100),
(2, '2016', 2, 'Februari', 220, 96),
(3, '2016', 4, 'Maret', 220, 90),
(4, '2016', 2, 'April', 220, 100),
(5, '2016', 2, 'Mei', 220, 98),
(6, '2016', 3, 'Juni', 220, 94),
(7, '2016', 2, 'Juli', 220, 98),
(8, '2016', 2, 'Agustus', 220, 96),
(9, '2016', 3, 'September', 220, 93),
(10, '2016', 2, 'Oktober', 220, 98),
(11, '2016', 2, 'November', 220, 99),
(12, '2016', 2, 'Desember', 220, 100),
(13, '2017', 4, 'Januari', 262, 90),
(14, '2017', 3, 'Februari', 262, 92),
(15, '2017', 3, 'Maret', 262, 94),
(16, '2017', 2, 'April', 262, 100),
(17, '2017', 1, 'Mei', 262, 105),
(18, '2017', 2, 'Juni', 262, 98),
(19, '2017', 4, 'Juli', 262, 90),
(20, '2017', 2, 'Agustus', 262, 96),
(21, '2017', 1, 'September', 262, 105),
(22, '2017', 3, 'Oktober', 262, 92),
(23, '2017', 3, 'November', 262, 95),
(24, '2017', 1, 'Desember', 262, 110),
(25, '2018', 4, 'Januari', 234, 90),
(26, '2018', 4, 'Februari', 234, 88),
(27, '2018', 3, 'Maret', 234, 91),
(28, '2018', 2, 'April', 234, 100),
(29, '2018', 4, 'Mei', 234, 89),
(30, '2018', 3, 'Juni', 234, 92),
(31, '2018', 4, 'Juli', 234, 90),
(32, '2018', 3, 'Agustus', 234, 93),
(33, '2018', 2, 'September', 234, 100),
(34, '2018', 2, 'Oktober', 234, 98),
(35, '2018', 2, 'November', 234, 96),
(36, '2018', 3, 'Desember', 234, 93),
(37, '2019', 4, 'Januari', 238, 87),
(38, '2019', 3, 'Februari', 238, 95),
(39, '2019', 2, 'Maret', 238, 100),
(40, '2019', 3, 'April', 238, 91),
(41, '2019', 3, 'Mei', 238, 95),
(42, '2019', 2, 'Juni', 238, 100),
(43, '2019', 3, 'Juli', 238, 93),
(44, '2019', 2, 'Agustus', 238, 100),
(45, '2019', 2, 'September', 238, 96),
(46, '2019', 1, 'Oktober', 238, 105),
(47, '2019', 4, 'November', 238, 87),
(48, '2019', 2, 'Desember', 238, 100),
(49, '2020', 4, 'Januari', 283, 90),
(50, '2020', 3, 'Februari', 283, 92),
(51, '2020', 2, 'Maret', 283, 98),
(52, '2020', 1, 'April', 283, 107),
(53, '2020', 1, 'Mei', 283, 110),
(54, '2020', 4, 'Juni', 283, 90),
(55, '2020', 1, 'Juli', 283, 110),
(56, '2020', 2, 'Agustus', 283, 96),
(57, '2020', 3, 'September', 283, 95),
(58, '2020', 2, 'Oktober', 283, 99),
(59, '2020', 1, 'November', 283, 110),
(60, '2020', 1, 'Desember', 283, 100),
(101, '2021', 2, 'Januari', 238, 98);

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_rekomendasi`
--

CREATE TABLE `data_rekomendasi` (
  `id_rekomendasi` int(11) NOT NULL,
  `tahun` varchar(50) NOT NULL,
  `jml_anggaran` varchar(50) NOT NULL,
  `ket` varchar(100) NOT NULL,
  `rekomendasi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_rekomendasi`
--

INSERT INTO `data_rekomendasi` (`id_rekomendasi`, `tahun`, `jml_anggaran`, `ket`, `rekomendasi`) VALUES
(1, '2017', '117,3 triliun', 'Anggaran Bertambah', 'Kekuatan Alutsista Ditambahkan'),
(2, '2018', '106,8 triliun', 'Anggaran Berkurang', 'Melakukan optimasi anggaran agar persiapan operasi alutsista stabil'),
(3, '2019', '108,4 triliun', 'Anggaran Bertambah', 'Kekuatan Alutsista Ditambahkan'),
(4, '2020', '12,27 triliun', 'Anggaran Bertambah', 'Kekuatan Alutsista Ditambahkan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_user`
--

CREATE TABLE `data_user` (
  `id_user` int(11) NOT NULL,
  `nama` varchar(35) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `level` enum('user','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_user`
--

INSERT INTO `data_user` (`id_user`, `nama`, `email`, `password`, `level`) VALUES
(1, 'dimas', 'dimas@dimas.com', 'dimas', 'admin'),
(2, 'shella', 'shella@shella.com', 'shella', 'user');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_anggaran`
--
ALTER TABLE `data_anggaran`
  ADD PRIMARY KEY (`id_anggaran`);

--
-- Indeks untuk tabel `data_kesiapan`
--
ALTER TABLE `data_kesiapan`
  ADD PRIMARY KEY (`id_kesiapan`);

--
-- Indeks untuk tabel `data_rekomendasi`
--
ALTER TABLE `data_rekomendasi`
  ADD PRIMARY KEY (`id_rekomendasi`);

--
-- Indeks untuk tabel `data_user`
--
ALTER TABLE `data_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `data_anggaran`
--
ALTER TABLE `data_anggaran`
  MODIFY `id_anggaran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `data_kesiapan`
--
ALTER TABLE `data_kesiapan`
  MODIFY `id_kesiapan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT untuk tabel `data_rekomendasi`
--
ALTER TABLE `data_rekomendasi`
  MODIFY `id_rekomendasi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `data_user`
--
ALTER TABLE `data_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
