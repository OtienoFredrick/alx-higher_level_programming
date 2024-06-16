-- The script converst database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

ALTER DATABASE hbtn_Oc_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_Oc_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8bmb4 COLLATE utfb8mb4_unicode_ci;
