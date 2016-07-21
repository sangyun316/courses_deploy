from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, id):
        query = "SELECT * FROM courses WHERE id = :id"
        data = { 'id': id}
        return self.db.query_db(query, data)

    def add_course(self, course):
        query = "INSERT INTO courses (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW())"
        data = { 'title': course['title'], 'description': course['description'] }
        return self.db.query_db(query, data)
        
    def delete_course(self, id):
        query = "DELETE FROM courses WHERE id = :id"
        data = { "id": id }
        return self.db.query_db(query, data)
