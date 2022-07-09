-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 09, 2022 at 11:39 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `academy`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `user_id` int(1) NOT NULL,
  `working_hours` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `user_id`, `working_hours`) VALUES
(1, 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `start_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `end_date` timestamp NULL DEFAULT NULL,
  `sessions_number` int(4) NOT NULL,
  `term` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`id`, `teacher_id`, `language_id`, `start_date`, `end_date`, `sessions_number`, `term`) VALUES
(3, 1, 0, '2022-07-02 10:21:15', NULL, 20, '4002'),
(4, 2, 0, '2022-07-02 11:04:36', NULL, 31, '4001'),
(5, 1, 1, '2022-07-04 06:46:03', NULL, 15, '0992');

-- --------------------------------------------------------

--
-- Table structure for table `class_time`
--

CREATE TABLE `class_time` (
  `id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `class_time` varchar(255) NOT NULL,
  `class_date` date NOT NULL DEFAULT current_timestamp(),
  `class_room` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class_time`
--

INSERT INTO `class_time` (`id`, `class_id`, `class_time`, `class_date`, `class_room`) VALUES
(1, 3, '12 to 14', '2022-07-02', '201'),
(2, 3, '14 to 16', '2022-07-01', '201'),
(3, 4, '8 to 10', '2022-06-01', '103'),
(4, 4, '10 to 12', '2022-06-05', '103'),
(5, 5, '18 to 20', '2020-12-12', '107');

-- --------------------------------------------------------

--
-- Table structure for table `language`
--

CREATE TABLE `language` (
  `id` int(11) NOT NULL,
  `language_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `language`
--

INSERT INTO `language` (`id`, `language_name`) VALUES
(1, 'english'),
(2, 'arabic'),
(3, 'italic'),
(4, 'spanish');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `start_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `passed_terms` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `user_id`, `start_date`, `passed_terms`) VALUES
(1, 3, '2022-07-02 11:48:50', 0),
(2, 5, '2022-07-02 11:48:50', 0),
(3, 7, '2022-07-04 06:57:46', 0),
(4, 9, '2022-07-04 07:06:47', 1),
(5, 10, '2022-07-04 07:19:19', 1);

-- --------------------------------------------------------

--
-- Table structure for table `students_rollcall`
--

CREATE TABLE `students_rollcall` (
  `id` int(11) NOT NULL,
  `admin_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `student_id` int(11) NOT NULL,
  `class_time_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students_rollcall`
--

INSERT INTO `students_rollcall` (`id`, `admin_id`, `teacher_id`, `student_id`, `class_time_id`, `status`, `date`, `description`) VALUES
(1, 0, 1, 1, 1, 1, '2022-09-24 20:30:00', 'nothing'),
(2, NULL, 2, 2, 1, 0, '2022-07-03 09:28:54', 'no'),
(3, 1, NULL, 3, 1, 1, '2022-07-04 10:39:45', ' was at class'),
(4, NULL, 1, 4, 3, 0, '2022-07-04 11:24:38', 'deasese');

-- --------------------------------------------------------

--
-- Table structure for table `student_classes`
--

CREATE TABLE `student_classes` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `grade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_classes`
--

INSERT INTO `student_classes` (`id`, `student_id`, `class_id`, `grade`) VALUES
(1, 1, 3, 19),
(2, 2, 4, 16),
(3, 5, 3, 0),
(5, 1, 4, 18),
(6, 5, 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `start_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `end_date` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `user_id`, `start_date`, `end_date`) VALUES
(1, 2, '2022-07-02 11:34:02', NULL),
(2, 4, '2022-07-03 06:16:15', NULL),
(3, 6, '2022-07-04 06:52:03', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `teachers_rollcall`
--

CREATE TABLE `teachers_rollcall` (
  `id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `class_time_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teachers_rollcall`
--

INSERT INTO `teachers_rollcall` (`id`, `admin_id`, `teacher_id`, `class_time_id`, `status`, `date`, `description`) VALUES
(1, 1, 2, 1, 0, '2022-07-04 10:35:05', 'nope');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_languages`
--

CREATE TABLE `teacher_languages` (
  `id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `teaching_language_id` int(11) NOT NULL,
  `degree` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher_languages`
--

INSERT INTO `teacher_languages` (`id`, `teacher_id`, `teaching_language_id`, `degree`) VALUES
(1, 3, 1, 'License'),
(2, 1, 2, 'license++'),
(3, 1, 4, 'diploma');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  `national_code` varchar(20) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `sex`, `role`, `national_code`, `phone_number`, `address`) VALUES
(1, 'reza', 'elahi', 'male', 'admin', '3496722571', '+989125401331', 'Tehran, kh alavi'),
(2, 'mohammad', 'mahdavi', 'male', 'teacher', '3678940599', '+989187466337', 'Hmaedan, shahrak farhangian'),
(3, 'ali', 'rezaei', 'male', 'student', '3554766336', '+989105947118', 'esfahan'),
(4, 'ahmad', 'hashemi', 'male', 'teacher', '3744680025', '+989153522791', 'Hamedan, HUT uni'),
(5, 'Ali', 'razavi', '', 'student', '3109978825', '+989304103354', 'Tehran, azadi'),
(6, 'ahamd', 'khaleghi', 'male', 'teacher', '3198713315', '+989928224556', 'Mazandaran, Shohada ST'),
(7, 'mona', 'lali', 'female', 'student', '3844633759', '+989358133676', 'kordestan, kordestan'),
(8, 'hojat', 'mahdavi', 'male', 'student', '3644139753', '+989204298037', 'Tehran'),
(9, 'mina', 'ghasemi', 'female', 'student', '3818713692', '+989603974114', 'Iran, Hamedan'),
(10, 'ali', 'babaei', 'male', 'student', '3410697163', '+98713369971', 'somewhere in space');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `class_time`
--
ALTER TABLE `class_time`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `language`
--
ALTER TABLE `language`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_rollcall`
--
ALTER TABLE `students_rollcall`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_classes`
--
ALTER TABLE `student_classes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teachers_rollcall`
--
ALTER TABLE `teachers_rollcall`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teacher_languages`
--
ALTER TABLE `teacher_languages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `class_time`
--
ALTER TABLE `class_time`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `language`
--
ALTER TABLE `language`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `students_rollcall`
--
ALTER TABLE `students_rollcall`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student_classes`
--
ALTER TABLE `student_classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `teachers_rollcall`
--
ALTER TABLE `teachers_rollcall`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `teacher_languages`
--
ALTER TABLE `teacher_languages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
