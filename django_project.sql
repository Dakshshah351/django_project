-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2023 at 06:06 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add category', 6, 'add_category'),
(22, 'Can change category', 6, 'change_category'),
(23, 'Can delete category', 6, 'delete_category'),
(24, 'Can view category', 6, 'view_category'),
(25, 'Can add user', 7, 'add_usermodel'),
(26, 'Can change user', 7, 'change_usermodel'),
(27, 'Can delete user', 7, 'delete_usermodel'),
(28, 'Can view user', 7, 'view_usermodel'),
(33, 'Can add members', 9, 'add_members'),
(34, 'Can change members', 9, 'change_members'),
(35, 'Can delete members', 9, 'delete_members'),
(36, 'Can view members', 9, 'view_members'),
(37, 'Can add pending_projects', 10, 'add_pending_projects'),
(38, 'Can change pending_projects', 10, 'change_pending_projects'),
(39, 'Can delete pending_projects', 10, 'delete_pending_projects'),
(40, 'Can view pending_projects', 10, 'view_pending_projects');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'students', 'category'),
(9, 'students', 'members'),
(10, 'students', 'pending_projects'),
(7, 'students', 'usermodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-08-13 14:38:06.431244'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-08-13 14:38:06.478068'),
(3, 'auth', '0001_initial', '2023-08-13 14:38:06.689126'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-08-13 14:38:06.752391'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-08-13 14:38:06.758063'),
(6, 'auth', '0004_alter_user_username_opts', '2023-08-13 14:38:06.764248'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-08-13 14:38:06.770768'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-08-13 14:38:06.774786'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-08-13 14:38:06.780762'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-08-13 14:38:06.785779'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-08-13 14:38:06.792712'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-08-13 14:38:06.804726'),
(13, 'auth', '0011_update_proxy_permissions', '2023-08-13 14:38:06.812718'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-08-13 14:38:06.817714'),
(15, 'students', '0001_initial', '2023-08-13 14:38:07.102706'),
(16, 'admin', '0001_initial', '2023-08-13 14:38:07.252161'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-08-13 14:38:07.262137'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-13 14:38:07.270283'),
(19, 'sessions', '0001_initial', '2023-08-13 14:38:07.383367'),
(22, 'students', '0002_category', '2023-09-17 17:31:14.569917'),
(23, 'students', '0003_delete_category_alter_members_email_and_more', '2023-09-17 17:31:14.866144'),
(24, 'students', '0003_remove_members_email_remove_members_name_and_more', '2023-09-18 10:05:14.778746'),
(25, 'students', '0004_pending_projects', '2023-09-18 10:05:14.800950'),
(26, 'students', '0005_delete_pending_projects_members_email_members_name_and_more', '2023-09-18 10:05:14.848728'),
(27, 'students', '0006_category_pending_projects', '2023-09-18 10:25:28.707746'),
(28, 'students', '0007_alter_category_email_alter_category_name_and_more', '2023-09-18 10:29:14.577272'),
(29, 'students', '0008_alter_members_email_alter_members_name_and_more', '2023-09-18 10:29:57.504576'),
(30, 'students', '0009_remove_pending_projects_client_email_and_more', '2023-09-18 20:32:27.439971'),
(31, 'students', '0010_rename_client_emal_pending_projects_client_email', '2023-09-18 20:32:27.451301'),
(32, 'students', '0011_alter_pending_projects_client_email', '2023-09-18 20:33:43.129949'),
(33, 'students', '0006_category_pending_projects_alter_members_email_and_more', '2023-09-18 21:19:22.749269'),
(34, 'students', '0007_alter_pending_projects_id', '2023-09-18 21:19:22.811817'),
(35, 'students', '0008_pending_projects_upload_file', '2023-09-27 20:33:09.244046'),
(36, 'students', '0009_alter_pending_projects_upload_file', '2023-09-27 20:49:42.129733'),
(37, 'students', '0010_alter_pending_projects_upload_file', '2023-09-27 20:57:04.904220');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('d9wkg5h5a4digaqefuu5e5q5mzbncwvj', '.eJxVjMsOgjAUBf-la9O0QL2tS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVyMN6ffjZAfOu1A7jjdZsvztC4j2V2xB622n0Wf18P9OxiwDt86QhsppCLICOUcW0cqThxQ16lLmhxoDIVKIkkNNAzsNUYfXCvsEcz7A_dIOEY:1qcrj5:tkNHmLYU5w2otTatcEFQFNSJ4GcxtmGA0LzNd6-ML84', '2023-09-17 18:21:35.144640'),
('ja96c6tcgybwf14k0z3dzwkq1bmok2n6', '.eJxVjMsOgjAUBf-la9O0QL2tS_d8Q3NfFdRAQmFl_HclYaHbMzPnZTJu65C3qksexVyMN6ffjZAfOu1A7jjdZsvztC4j2V2xB622n0Wf18P9OxiwDt86QhsppCLICOUcW0cqThxQ16lLmhxoDIVKIkkNNAzsNUYfXCvsEcz7A_dIOEY:1qcm4B:sV9LeCvTgJFVrfPLtDXB0JZahPvjifUhMaRnhXJ2pYE', '2023-09-17 12:18:59.891042'),
('r351rul53zqvbh3e48ntc0ucm1hb2y8m', '.eJxVjMsOgjAQRf-la9PQlrHUpXu-gUznYVEDCYWV8d-VhIVu7znnvsyA21qGrcoyjGwuxpvT75aRHjLtgO843WZL87QuY7a7Yg9abT-zPK-H-3dQsJZvnbmDyIASzhrJUUD0rusSQQBP4Jqk4hBdy0rKEjk2sSFpvapLQcG8P_seOJM:1qnzwo:aEGZP3CTWJ2BV0QTr4IyNrLJjxwFjSZjenc40bQBFFQ', '2023-10-18 11:21:46.771350'),
('thg9h19mzw3x9pd3fhuee2fmyvquiugl', '.eJxVjDsOwjAQBe_iGlkx8W8p6TmDtfaucQDZUpxUiLuTSCmgnZn33iLgupSwdp7DROIilDj9sojpyXUX9MB6bzK1usxTlHsiD9vlrRG_rkf7d1Cwl21tvLPaEORMSM6CAc1ZJQ8DA5EaUAEgUzx7ZU3KTo_RAptIZsMeR_H5Au1FOF8:1qVD1u:K_KkZHst0hIS4NG468hCdYbclUSIPuoslMI6Pd31csU', '2023-08-27 15:29:22.487117');

-- --------------------------------------------------------

--
-- Table structure for table `students_category`
--

CREATE TABLE `students_category` (
  `id` bigint(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students_members`
--

CREATE TABLE `students_members` (
  `id` bigint(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students_pending_projects`
--

CREATE TABLE `students_pending_projects` (
  `id` bigint(20) NOT NULL,
  `client_name` varchar(255) NOT NULL,
  `project_title` varchar(255) NOT NULL,
  `Client_email` varchar(255) NOT NULL,
  `Upload_File` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students_pending_projects`
--

INSERT INTO `students_pending_projects` (`id`, `client_name`, `project_title`, `Client_email`, `Upload_File`) VALUES
(26, 'daksh', 'dakuPROJECT', 'Dakshshah351@gmail.com', 'Upload_File/type_convo.py');

-- --------------------------------------------------------

--
-- Table structure for table `students_usermodel`
--

CREATE TABLE `students_usermodel` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `userProfile` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students_usermodel`
--

INSERT INTO `students_usermodel` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `userProfile`) VALUES
(1, 'pbkdf2_sha256$600000$3WVHxS1y31vCJMAPESMGDr$5uUyu1QxjIUDGb5YmNzlt/PQl46dd/8P+4WxoRC6cdQ=', '2023-08-13 15:29:22.487117', 0, 'dakshshah', 'Daksh', 'Shah', 'Dakshshah351@gmail.com', 0, 1, '2023-08-13 14:42:09.891592', 'userProfile/IMG20220703195201.jpg'),
(2, 'pbkdf2_sha256$600000$qHJSdMv5IshIjooQz4T2cE$qGA6t3ge0jHz204B3iFSe7kR7iC0KpwCgGlOWKJaWuo=', '2023-10-04 11:21:46.760405', 0, 'dakshshah@123', 'Daksh', 'Shah', 'Dakshshah351@gmail.com', 0, 1, '2023-09-17 18:06:15.228651', 'userProfile/IMG20220703195201_OHZa65k.jpg'),
(3, 'pbkdf2_sha256$600000$tOUGoXhtUfRTOVWXCltY7V$j3x19bufsz426NZ1leTvypCHpdogRUYs9+pqvrcM/9Q=', '2023-09-18 10:55:42.171007', 1, 'daksh', '', '', 'dakshshah351@gmail.com', 1, 1, '2023-09-18 10:54:44.667652', ''),
(4, 'pbkdf2_sha256$600000$4wdtaBXthxrnKoqLcVG7G4$h+SoSKtLiXn+FNvrE1HVTcfU2EX4kMp+iOGwymtEsaE=', '2023-10-04 10:47:53.607863', 0, 'divythakkar', 'divy', 'thakkar', 'divythakkar@gmail.com', 0, 1, '2023-10-04 10:47:18.480890', 'userProfile/IMG20220703195201.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `students_usermodel_groups`
--

CREATE TABLE `students_usermodel_groups` (
  `id` bigint(20) NOT NULL,
  `usermodel_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students_usermodel_user_permissions`
--

CREATE TABLE `students_usermodel_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usermodel_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_students_usermodel_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `students_category`
--
ALTER TABLE `students_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_members`
--
ALTER TABLE `students_members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_pending_projects`
--
ALTER TABLE `students_pending_projects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_usermodel`
--
ALTER TABLE `students_usermodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `students_usermodel_groups`
--
ALTER TABLE `students_usermodel_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `students_usermodel_groups_usermodel_id_group_id_1897b001_uniq` (`usermodel_id`,`group_id`),
  ADD KEY `students_usermodel_groups_group_id_29766096_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `students_usermodel_user_permissions`
--
ALTER TABLE `students_usermodel_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `students_usermodel_user__usermodel_id_permission__894ecf5a_uniq` (`usermodel_id`,`permission_id`),
  ADD KEY `students_usermodel_u_permission_id_9b540be2_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `students_category`
--
ALTER TABLE `students_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students_members`
--
ALTER TABLE `students_members`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `students_pending_projects`
--
ALTER TABLE `students_pending_projects`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `students_usermodel`
--
ALTER TABLE `students_usermodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `students_usermodel_groups`
--
ALTER TABLE `students_usermodel_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students_usermodel_user_permissions`
--
ALTER TABLE `students_usermodel_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_students_usermodel_id` FOREIGN KEY (`user_id`) REFERENCES `students_usermodel` (`id`);

--
-- Constraints for table `students_usermodel_groups`
--
ALTER TABLE `students_usermodel_groups`
  ADD CONSTRAINT `students_usermodel_g_usermodel_id_ca9ad86f_fk_students_` FOREIGN KEY (`usermodel_id`) REFERENCES `students_usermodel` (`id`),
  ADD CONSTRAINT `students_usermodel_groups_group_id_29766096_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `students_usermodel_user_permissions`
--
ALTER TABLE `students_usermodel_user_permissions`
  ADD CONSTRAINT `students_usermodel_u_permission_id_9b540be2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `students_usermodel_u_usermodel_id_e5853b06_fk_students_` FOREIGN KEY (`usermodel_id`) REFERENCES `students_usermodel` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
