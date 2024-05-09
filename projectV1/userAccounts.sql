-- Create a table for users
CREATE TABLE Users (
    UserID VARCHAR(5) PRIMARY KEY,
    UserName VARCHAR(50) NOT NULL,
    UserType TEXT NOT NULL,
    Password TEXT NOT NULL
);

-- Create a table for courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    CourseCode VARCHAR(20) NOT NULL
);

-- Create a table for sections
CREATE TABLE Sections (
    SectionID INT PRIMARY KEY,
    SectionName VARCHAR(50) NOT NULL,
    CourseID INT,
    FacultyID VARCHAR(5),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (FacultyID) REFERENCES Users(UserID)
);

-- Create a table for faculty courses
CREATE TABLE FacultyCourses (
    FacultyCourseID INT PRIMARY KEY,
    CourseID INT,
    SectionID INT,
    FacultyID VARCHAR(5),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (SectionID) REFERENCES Sections(SectionID),
    FOREIGN KEY (FacultyID) REFERENCES Users(UserID)
);

-- Create a table for student courses
CREATE TABLE StudentCourses (
    StudentCourseID INT PRIMARY KEY,
    CourseID INT,
    StudentID VARCHAR(5),
    QuarterEnrolled VARCHAR(10),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Users(UserID)
);

-- Insert sample engineering courses
INSERT INTO Courses (CourseID, CourseName, CourseCode)
VALUES 
    (1, 'Introduction to Electrical Engineering', 'EE101'),
    (2, 'Circuit Analysis', 'EE201'),
    (3, 'Digital Signal Processing', 'EE301'),
    (4, 'Introduction to Mechanical Engineering', 'ME101'),
    (5, 'Thermodynamics', 'ME201'),
    (6, 'Mechanical Design', 'ME301'),
    (7, 'Introduction to Civil Engineering', 'CE101'),
    (8, 'Structural Analysis', 'CE201'),
    (9, 'Transportation Engineering', 'CE301'),
    (10, 'Introduction to Computer Engineering', 'CPE101');

-- sample accounts
INSERT INTO Users (UserID, UserName, UserType, Password)
VALUES
    ('S0001', 'student1', 'student', '1234'),
    ('F0001', 'faculty1', 'faculty', '5678');
