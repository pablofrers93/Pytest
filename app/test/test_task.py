import pytest

from app.task import Task
from app.task import DueDateError

from datetime import datetime
from datetime import timedelta

class TestTask():
     
    @pytest.mark.news 
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days = 1)
        task = Task('Title', 'Description', 'eduardo.gpg', due_date)

        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'eduardo.gpg'
        assert task.due_date == due_date
        
    @pytest.mark.errors
    @pytest.mark.due_date
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days = 1)
            Task('Title', 'Description', 'eduardo.gpg', due_date)

    @pytest.mark.due_date 
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days = 1)
        task = Task('Title', 'Description', 'eduardo.gpg', due_date)
        
        assert task.due_date > datetime.now()
