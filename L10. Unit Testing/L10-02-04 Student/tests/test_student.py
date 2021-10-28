import unittest
from project.student import Student


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Test", {"math": ["my math notes"]})

    def test_student_attributes(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({"math": ["my math notes"]}, self.student.courses)

    def test_student_enroll_existing_course(self):
        notes = ["my new math notes"]
        expected_result = "Course already added. Notes have been updated."
        expected_notes = ["my math notes", "my new math notes"]
        actual_result = self.student.enroll("math", notes)
        actual_notes = self.student.courses["math"]
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_notes, actual_notes)

    def test_student_enroll_new_course_with_notes_null(self):
        course = "English"
        notes = ["my English notes"]
        expected_result = "Course and course notes have been added."
        expected_courses = {"math": ["my math notes"], "English": ["my English notes"]}
        actual_result = self.student.enroll(course, notes)
        actual_courses = self.student.courses
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll_new_course_with_notes_Y(self):
        course = "English"
        notes = ["my English notes"]
        expected_result = "Course and course notes have been added."
        expected_courses = {"math": ["my math notes"], "English": ["my English notes"]}
        actual_result = self.student.enroll(course, notes, add_course_notes="Y")
        actual_courses = self.student.courses
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll_new_course_without_notes(self):
        expected_result = "Course has been added."
        expected_courses = {"math": ["my math notes"], "English": []}
        actual_result = self.student.enroll("English", [], add_course_notes="N")
        actual_courses = self.student.courses
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll_new_course_without_notes_incorrect(self):
        expected_result = "Course has been added."
        expected_courses = {"math": ["my math notes"], "English": []}
        actual_result = self.student.enroll("English", ["my English notes"], add_course_notes="N")
        actual_courses = self.student.courses
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, actual_courses)

    def test_student_add_notes_to_existing_course(self):
        notes = "my new math notes"
        expected_result = "Notes have been updated"
        expected_notes = ["my math notes", "my new math notes"]
        actual_result = self.student.add_notes("math", notes)
        actual_notes = self.student.courses["math"]
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_notes, actual_notes)

    def test_student_add_notes_to_not_existing_course_raises(self):
        course = "English"
        notes = ["my English notes"]
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, notes)
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"math": ["my math notes"]}, self.student.courses)

    def test_student_leave_course_existing(self):
        expected_result = "Course has been removed"
        expected_courses = {}
        actual_result = self.student.leave_course("math")
        actual_courses = self.student.courses
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_courses, actual_courses)

    def test_student_leave_course_not_existing_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("English")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({"math": ["my math notes"]}, self.student.courses)


if __name__ == "__main__":
    unittest.main()
