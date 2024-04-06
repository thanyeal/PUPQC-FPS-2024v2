from django.test import TestCase

# This is a test page for test cases:

# This scripts is commented to save all the queries inserted in the database.
# Please do not modify and delete any of this or i will punch you in the face :)

# CREATE TABLE FacultyInfo (
# 	 FacultyId		INT IDENTITY(1100,1)
# 	,FacultyName	VARCHAR (100)
# 	,FacultyType	VARCHAR(10)
# 	,FacultyDegree	VARCHAR(100)
# 	,FacultyRank	VARCHAR(100)
# 	,CONSTRAINT PK_FacultyId PRIMARY KEY (FacultyId)
# );

# INSERT INTO FacultyInfo VALUES 
# ('Rodolfo Y. Aquino Jr.'		, 'Regular', 'Master in Business Administration'				, 'Instructor III')			,
# ('Mark Anthony R. Aribon III'	, 'Regular', 'Master in Information Technology Integration'		, 'Instructor III')			,
# ('Melanie F. Bactasa'			, 'Regular', 'Master of Arts in Education'						, 'Assistant Professor IV')	,
# ('Abraham Seth R. Bernardino'	, 'Regular', 'Bachelor in Physical Education'					, 'Instructor I')			,
# ('Berna A. Bulawit'				, 'Regular', 'Master in Educational Management'					, 'Instructor I')			,
# ('Mary Grace I. Cruz'			, 'Regular', 'Master in Educational Management'					, 'Associate Professor I')	,
# ('Celeste L. De Leon'			, 'Regular', 'Bachelor of Science in Chemical Engineering'		, 'Instructor I')			,
# ('Elijah Paul B. Delmo'			, 'Regular', 'Bachelor in Physical Education'					, 'Instructor I')			,
# ('Rodrigo S. Dolorosa'			, 'Regular', 'Doctor in Education Management'					, 'Associate Professor II')	,
# ('Roberto B. Doromal'			, 'Regular', 'Bachelor of Science in Information Technology'	, 'Instructor I')			,
# ('Cherrylyn P. Esparagoza'		, 'Regular', 'Master in Public Administration'					, 'Assistant Professor I')	,
# ('Ain Gueul E. Escober'			, 'Regular', 'Bachelor of Arts in Multimedia Studies'			, 'Instructor I')			,
# ('Zandro T. Estella'			, 'Regular', 'Master in Business Administration'				, 'Associate Professor V')	,
# ('Almac C. Fernandez'			, 'Regular', 'Master in Information Technology'					, 'Assistant Professor IV')	,
# ('Irynne P. Gatchalian'			, 'Regular', 'Bachelor of Science in Computer Science'			, 'Assistant Professor IV')	,
# ('Jaime Jr. P. Gutierrez'		, 'Regular', 'Master in Philippines Studies'					, 'Associate Professor V')	,
# ('Demelyn E. Monzon'			, 'Regular', 'PhD in Educational Leadership & Management'		, 'Associate Professor V')	,
# ('Joanna Marie DC. Oliquino'	, 'Regular', 'Bachelor of Arts in Philippine Studies'			, 'Instructor I')			,
# ('Rommel Y. Roxas'				, 'Regular', 'Master in Business Administration'				, 'Assistant Professor II')	,
# ('Cleotilde B. Servigon'		, 'Regular', 'Bachelor in Accountancy'							, 'Assistant Professor I')	,
# ('Philip SJ. Soberano'			, 'Regular', 'Master in Public Administration'					, 'Assistant Professor III'),
# ('Antonius C. Umali'			, 'Regular', 'Doctor in Public Administration'					, 'Associate Professor V')	,

# ('Karl Christian D. Abalos'			, 'Part-time', 'Bachelor of Arts in Philosophy'							,'Part-time-Instructor') ,
# ('Mary Ann Micah R. Baltazar, CPA'	, 'Part-time', 'Bachelor of Laws Bachelor of Science in Accountancy'	, 'Part-time-Instructor'),
# ('Richard B. Banate, CPA'			, 'Part-time', 'Bachelor of Science in Accountancy'						, 'Part-time-Instructor'),
# ('Girlie F. Bernardino'				, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Francisco S. Calingasan'			, 'Part-time', 'Master in Public Administration'						, 'Part-time-Instructor'),
# ('Atty. Eleazar E. Castillo'		, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Norberto V. Caturay'				, 'Part-time', 'Doctor in Education Management'							, 'Part-time-Instructor'),
# ('Nieva M. Cecogo'					, 'Part-time', 'Master of Educational Management'						, 'Part-time-Instructor'),
# ('Erwin Cipriano'					, 'Part-time', 'Bachelor of Arts in English'							, 'Part-time-Instructor'),
# ('Ricardo H. Clenuar'				, 'Part-time', 'Bachelor of Science in Business Administration'			, 'Part-time-Instructor'),
# ('Keinaz Domingo'					, 'Part-time', 'Master in Information Security'							, 'Part-time-Instructor'),
# ('Cherry M. Doromal'				, 'Part-time', 'Master in Information Technology'						, 'Part-time-Instructor'),
# ('Leah A. Dungca'					, 'Part-time', 'Master of Arts in Education'							, 'Part-time-Instructor'),
# ('Rosicar E. Escober, Ph.D.'		, 'Part-time', 'Doctor of Philosophy'									, 'Part-time-Instructor'),
# ('Firmo A. Esguerra'				, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Noel F. Fabela'					, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Jorgen Z. Fulleros'				, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Richard M. Fulleros'				, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Asuncion V. Gabasa'				, 'Part-time', 'Master of Arts in Language Teaching'					, 'Part-time-Instructor'),
# ('Maita C. Garcia'					, 'Part-time', 'Bachelor of Science in Accountancy'						, 'Part-time-Instructor'),
# ('Harold Q. Gardon'					, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Leslie O. Gatan'					, 'Part-time', 'Master in Public Administration'						, 'Part-time-Instructor'),
# ('Esther S. Gulmatico, Ph.D.'		, 'Part-time', 'Doctor of Philosophy'									, 'Part-time-Instructor'),
# ('Erwin Vicman Lara'				, 'Part-time', 'Master in Public Administration'						, 'Part-time-Instructor'),
# ('Jerome Chrstopher G. Leynes'		, 'Part-time', 'Master in Education Management'							, 'Part-time-Instructor'),
# ('Kezaiah M. Monzon'				, 'Part-time', 'Master of Science in Information Technology'			, 'Part-time-Instructor'),
# ('Ernesto J. Odpaga Jr.'			, 'Part-time', 'Bachelor of Science in Information Technology'			, 'Part-time-Instructor'),
# ('Jose Gil C. Pineda'				, 'Part-time', 'Master in Business Administration'						, 'Part-time-Instructor'),
# ('Maricar O. Soberano'				, 'Part-time', 'Bachelor of Business Education'							, 'Part-time-Instructor');
