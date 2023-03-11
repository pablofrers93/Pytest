import pytest 
from app.task import Task
from datetime import datetime
class TestTask():
    
    def test_task(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now()
        task = Task('Title', 'Description', 'eduardo.gpg', due_date)

        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'eduardo.gpg'
        assert task.due_date == due_date
