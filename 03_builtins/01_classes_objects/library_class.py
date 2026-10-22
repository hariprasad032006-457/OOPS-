class LibraryVisit:
    """Store and display a student's library visit details."""

    def __init__(self, name, roll_no, purpose, in_time, out_time):
        self.name = name
        self.roll_no = roll_no
        self.purpose = purpose
        self.in_time = in_time
        self.out_time = out_time

    def display_if_reading(self, name):
        if self.name == name and self.purpose.lower() == "reading":
            print(f"Name: {self.name}")
            print(f"Roll No: {self.roll_no}")
            print(f"Purpose: {self.purpose}")
            print(f"In Time: {self.in_time}")
            print(f"Out Time: {self.out_time}")


if __name__ == "__main__":
    student = LibraryVisit("Sneha", 1, "reading", "10:00", "11:00")
    student.display_if_reading("Sneha")
