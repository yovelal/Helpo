from django.test import TestCase,tag
from associations.forms import volunteeringRequestform


class TestForms(TestCase):
    #Unit test for forms without data, to check the form is getting the all the needed erros
    @tag('UT')
    def test_create_volunteeringRequestform(self):
        form = volunteeringRequestform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)
    
    @tag('UT')
    def test_create_volunteeringRequestform_with_data(self):   
        form = volunteeringRequestform(data={'info':'i want to volunteer'})
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors),0)
