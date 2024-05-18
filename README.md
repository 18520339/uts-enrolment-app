# Software Development for UTS Enrolment Application

A local university wants to develop a new interactive system that allows students to self-enroll in semester subjects. Your team is expected to develop the application in 2 parts, **Part 1** and **Part 2**, then demonstrate the result to the stakeholders in **Part 3**:

**(Part 1)** Complete and deliver a comprehensive software requirements analysis report, which includes: 
- Transform the requirements into User-Stories and map the User-Stories to a requirements table (or backlog).
- Create a UML Use-Case diagram and explain in detail the goals, actors, cases and their relationships in the diagram.
- Create a UML Class Diagram and explain the classes, their properties, and their relationships in detail. 

**(Part 2)** Develop and implement the application based on the requirement analysis, modelling and design completed in **Part 1**. The application is composed of a `CLI` application and an optional `GUI` implementation for that app. 

**(Part 3)** This is the assessment formal showcase. Each team will present their **Part 2** working application based on their collaborative **Part 1** design.

***NOTE**: The enrolment is only for 1 semester at a time. Hence, the choice of multiple semester enrolment is outside the application scope.

## How to Run

1. For `CLI` app: `python src/views/cli_views.py`

2. For `GUI` app:

  ```bash
  pip install tkmacosx
  python src/views/login_window.py
  ```

## System Menu Requirements

The program system is composed of 4 system menus: [University System](#i-university-system), [Student System](#ii-student-system), [Student Course System](#iii-student-course-system), and [Admin System](#iv-admin-system).

### I. University System

The university is requesting a CLI application called **CLIUniApp** offering access to 2 interactive sub-system menus for students and admins actions:

- The university menu system should enable users to choose to go the Admin or Student Menu: **(A) Admin**, **(S) Student**, **(x) Exit**.
- **CLIUniApp** stores students' data in a local file, `students.data`. 
- All **CLIUniApp** CRUD operations should be operated with this storage file `students.data`. 

| Entity       | Criteria                                              | 
|--------------|-------------------------------------------------------|
| Student      | Student can go to student menu                        |
| Admin        | Admin can go to the admin menu                              |
| Browsing     | Student/Admin can browse between menus                | 
| Matching I/O | I/O wording, coloring, indentation matches the sample | 

### II. Student System

> Students have the choice to register or login if they are previously registered.

Students must register before they can access the system and enroll in subjects. The student menu system should enable students to Login and Register as follows: 

**(r) Register:**

- On sign-up, a unique student ID will be auto-generated for each student:
  - The student unique ID is between 1 and 999999. 
  - If the size of the generated ID is not 6 digits, then the ID should be pre-fixed with zeroes to complete the 6-digit size (ex: 002340 is valid, 2345 is not). 

- Students' emails should have the extension `@university.com`. The students' emails and the password should be validated against existing patterns, for example:
  - `firstname.lastname@university.com` is a valid email.
  - `firstname.lastname@university` is not a valid email.

- The student password is considered valid if it matches the following pattern:
  - Starts with upper-case characters.
  - Minimum 6 letters followed by 3 or more digits.

- The student should be checked if they exist. Only register students that do not exist in `students.data`. 

=> On registration, student data should be stored in the file `students.data`.

**(l) Login**: 

- Students should be able to login. 
- Then the student should be checked if they exist. 
- Only a registered student should login. 
- When login, your program should read the students' data from `students.data` and verify the student credentials. 
- After login, a student goes to **Student Course Menu** that offers the choices.

**(x) Exit**

***NOTE**: In the Login/Register scenarios, students' credentials are verified against regular expressions stored as constants in an `Utils` class.

| Entity         | Criteria                                              | 
|----------------|-------------------------------------------------------|
| Register       | Student can register – data saved to file             |
| Login          | Student can login – data read from file               |
| RegEx          | For login and register                                |
| Error Handling | Exceptions, errors, logical scenarios are handled     | 
| Matching I/O   | I/O wording, coloring, indentation matches the sample | 

### III. Student Course System

Registered students can then log into the application and access this menu to perform the following actions:

**(c) Change**: Enables a student to change their password

**(e) Enroll**: Enroll in a subject. A student can enroll in maximum **4** subjects.

**(r) Remove**: Remove a subject from the subjects' enrolment list.

**(s) Show**: Shows the enrolled subjects and the marks & grades for each subject.

**(x) Exit**

Students don't need to select a subject to enroll in (to simplify the application). Subjects should be available for students on enrolment: 
- A subject is identified by a unique 3-digit auto-generated ID (1 <= ID <= 999).
- Once a student selects the enrolment command/action, a new subject will be added to their enrolment list (given the list has < **4** subjects).
- The enrolment system will keep track of the subjects in the student's list and will notify the student if the subject count exceeds **4**.
- A random subject mark (between 25 and 100) will be autogenerated and allocated for that subject. Then the subject grade will be auto-calculated based on the mark: mark < 50 (Z), 50 <= mark < 65 (P), 65 <= mark < 75 (C), 75 <= mark < 85 (D), mark >= 85 (HD).
- Subject enrolment data is saved to `students.data` within the Student objects.

***NOTE**: In the enrolment scenario, no controls are needed to sort the subjects. Every time a student enrols in a subject, the overall mark should be re-calculated.

| Entity             | Criteria                                               | 
|--------------------|--------------------------------------------------------|
| Enroll             | Student can enroll in a subject – 4 maximum            |
| Tracking           | Subject enrolment is tracked                           |
| Remove a subject   | Remove by ID                                           |
| Show subjects      | Subject listing                                        | 
| Change password    | Student can change their password                      | 
| Read/Write to file | Student and subject data are read/written from/to file | 
| Error Handling     | Exceptions, errors, logical scenarios are handled      | 
| Matching I/O       | I/O wording, coloring, indentation matches the sample  | 

### IV. Admin System

> Admins have their own subsystem to perform student management operations

Admins are existing university staff and do not need to register. Admins can simply use the admin sub-system. Admin menu offers the following actions:

**(c) Clear database file**: Enable admin to clear the entire `students.data` file store.

**(g) Group students by grade**: Show students organized with respect to the grade.

**(p) Partition students**: Partition and show students based on `PASS`/`FAIL` distribution (using grades & marks).

**(r) Remove student**: Enable admin to remove a student by ID.

**(s) Show**: Show all registered students from file.

**(x) Exit**

***NOTE**: 
- The data file `students.data` should also be available to Admins to perform students' management operations with the students' data.
- The admin should read the students data from `students.data` and produce the outputs shown in the scenario (listing, grouping, partitioning).
- When the admin removes 1 student or all students, that data should be removed from `students.data`.

| Entity             | Criteria                                               | 
|--------------------|--------------------------------------------------------|
| Show students      | Admin list all students                                |
| Group students     | Admin groups students according to the grade           |
| Partition students | Admin partitions students as PASS/FAIL                 |
| Remove a student   | Admin can remove a student by ID                       | 
| Clear file         | Admin can remove all students and clear the file       | 
| Read/Write to file | Student and subject data are read/written from/to file | 
| Error Handling     | Exceptions, errors, logical scenarios are handled      | 
| Matching I/O       | I/O wording, coloring, indentation matches the sample  | 

## Part 1: Requirements Analysis

### I. User-Story Table (Backlog)

Your team is expected to read thoroughly the customer (university) requirements and transform the requirements into User-Story. The User-Story should be simple so that each story is later translated into a function (or action). 

| Entity                    | Criteria                                               |
|---------------------------|--------------------------------------------------------|
| User stories are specific | User stories are decomposed into simple story = action | 
| User stories consistency  | User stories align with the project requirements       |
| Backlog correctness       | User stories are correctly mapped into the backlog     | 

Each story will have a unique 3-digit ID. If a group of stories is related to the same features, then the hundreds (number) will match for all those stories. For example, considering all the following stories are related to the same Login feature, their ID should start with the same hundreds number:
- Story: match username & password with the ones on file -> 101
- Story: verify username & password against patterns -> 105
- Story: show an error message if credentials do not match -> 106
- Story: take student to student sub-menu if credentials are correct -> 100

=> The refined User-Stories should be mapped into a requirements table (or backlog) formatted as follows:

| ID                              | User                                   | Action                       | Result                              | Function        |
|---------------------------------|----------------------------------------|------------------------------|-------------------------------------|-----------------|
| A unique 3 digits user story ID | The person or entity taking the action | The action taken by the user | The result or outcome of the action | The action name |

### II. UML Use-Case and UML Class Diagrams

- **UML Use-Case diagram**: Identify the actors, the goals, the case, and their relationships. 

| Entity                  | Criteria                                                 | 
|-------------------------|----------------------------------------------------------|
| Entities identification | Goals, cases, actors, relationships correctly identified |
| Entities description    | Entities are correctly explained and reported            |
| Actors action           | Actors initiate accurate cases                           | 
| Case relationships      | Accurate and consistent case relationships               | 
| Labelling               | Use of correct relationship labeling                     | 

- **UML Class diagram**: Identify the classes, fields, methods, visibility, multiplicity, and their relationships.

| Entity        | Criteria                                        | 
|---------------|-------------------------------------------------|
| Class         | Class properly identified and explained         |
| Fields        | Properly identified. Accurate visibility choice | 
| Methods       | Correct method naming, type, visibility         |
| Relationships | Consistent class relationships                  | 
| Multiplicity  | Accurate relationship multiplicities            | 

Please provide explanations for each actor, goal, case, relationship. Ensure that your diagram is consistent and aligned with the provided explanations about all involved entities.

## Part 2: Software Development

> Feel free to add more classes following the class diagram in **Part 1**. 

### I. Sample Model Classes

The program model has at least 3 classes: `Student`, `Subject`, and `Database`. These classes are responsible for storing the program data and for supplying the program controllers (see section 4) with functionalities and data. You may add more classes based on Part 1 design.

**1. Student Class**

- The Student class has following properties:
  - name, email, password, and a list of subjects.
  - ID randomly generated 1 <= ID <= 999999, unique and formatted as 6-digits width. IDs < 6-digits width should be completed with zeroes from the left.
- A student can only enroll in 4 subject maximum (A course of 4 subjects).
- A student can enroll/drop a subject at any time.
- Upon enrolment in a subject a random mark is generated for this subject 25 <= mark <= 100 and the grade of that subject is calculated based on the mark.
- A student is `PASS`/`FAIL` a course if the average mark of the subjects is >= 50
- A student can change their password at any time.

**2. Subject Class**

The Subject class has following properties:
- ID randomly generated 1 <= ID <= 999, unique and formatted as 3-digits width. IDs < 3-digits width should be completed with zeroes from the left.
- mark is randomly generated where 25 <= mark <= 100.
- grade is determined based on the mark.

**3. Database Class**

The Database class should contain the methods to:
- Check if the file `students.data` exists before using it.
- Create the file `students.data` if it doesn't exists.
- Write objects to the file `students.data`.
- Read objects from the file `students.data`.
- Clear the objects from the file `students.data`.

***NOTE**: All program menu(s) actions (Admin and Student) should use the `students.data` data and perform CRUD operations with this data.

**4. BEST PRACTICES AND RECOMMENDATIONS**

The program is best developed using classes (controllers) to manage the data exchange between the model classes (Student, Subject, Database) and the menu(s) actions. The controllers (for example: StudentController, SubjectController, etc…) are normal classes that use the `students.data` data and perform CRUD operations with this data. The controllers contain the system menus that use the model objects and work with the data file `students.data`.

***NOTE**: You may add any controller classes based on **Part 1** case study design. Groups can implement the controllers the way that suits their program.

### II. Sample I/O

The sample I/O should be used as a reference and guidance to help you understand the scenarios of the program. The sample I/O outlines several scenarios to help you understand how the program should work and how the output should be designed and formatted:
1. The University System Scenario
2. The Student System – Register
3. The Student System – Login
4. The Student Course System – Enrolment
5. The Student Course System – Remove Subject
6. The Student Course System – Change Password
7. The Admin System – View Students – Groups - Partitions
8. The Admin System – Remove a Student and Removing all Students

### III. Case Study GUI Implementation (Optional)

> Develop a GUI application called **GUIUniApp** only for students

The university is also requesting a standalone GUI application called **GUIUniApp**, which is a prototype designed only for students to simplify the implementation. The case study GUI software implementation is an **optional** challenge task of **Part 2**. Your **GUIUniApp** should have at least **4** windows:
- Login window: **GUIUniApp** should allow students (no Admin options) to login into the system. The login window is the GUI main window.
- Enrolment window: Once a student logins correctly, they can enroll into subjects (**4** subjects maximum).
- Subjects window: Every time a student is enrolled in a subject, the subject is added to the subject GUI menu enrolment list
- Exception window: Handle possible exceptions, for example: empty login fields, incorrect student credentials, incorrect email format, enrolment in > **4** subjects, ...

| Entity            | Criteria                                                                                                                       | 
|-------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Login window      | Login window works and on login, students are taken to the enrolment window. Use the registered students from `students.data`  |
| Enrolment window  | Enrolment window allows students to add subjects (maximum **4**)                                                               |
| Subjects window   | Enrolled subjects are added to the list in the subjects' window                                                                |
| Exception window  | Handle incorrect format exception and max 4 subjects' exception                                                                | 

In the GUI application, assume that the students are already registered:
- Create and add a few student accounts to the application for testing.
- You can work with registered students details already saved in the file `students.data` and use them to login into the **GUIUniApp**.
- In **GUIUniApp**, the rules for student enrolment into a subject are the same rules as **CLIUniApp**. 
- There is no need to store students' data in a file when using **GUIUniApp**.