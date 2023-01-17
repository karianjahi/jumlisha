"""This is the testing area for the count_words.py
The tests ensures that we cover every available user option/usage
to make sure that we have the error handled before the user knows about it
- We use pytest module to test our code
- pip install pytest if you don't have it
- usually (perhpas not always -- check this) the word test appears at the beginning of the method. check if by having test anywhere in your testing script filename has pytest recognize the file as a test.
"""
from count_words import WordCounter
inst = WordCounter()
import pytest
class TestWordCounter:
    """This is the class where tests are implemented
    """
    def test_empty(self):
        text = ""
        assert inst.count_words(text) == 0
    
    def test_one(self):
        text = "Cascabel"
        assert inst.count_words(text) == 1
    
    def test_multiple_words(self):
        text = "I study data science"
        assert inst.count_words(text ) == 4
    
    def test_hyphens(self):
        text = "How-are-you-doing?"
        assert inst.count_words(text) == 4
    
    def test_linebreaks(self):
        text = "\nHow\nare\nyou\ndoing"
        assert inst.count_words(text) == 4
    
    def test_hmtl(self):
        text = "<h1> I am a student </h1>"
        assert inst.count_words(text) == 4
        
    def test_spaces(self):
        text = "  test spaces   "
        assert inst.count_words(text) == 2
    
    def test_data_type_error(self):
        text = ["name"]
        with pytest.raises(Exception) as my_error:
            inst.count_words(text)
        assert "Strings only" in str(my_error.value)