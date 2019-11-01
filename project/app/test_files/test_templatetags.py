from django.test import TestCase
from app.templatetags.core_tags import split_str
from django.template import Template, Context
from django.template.loader import render_to_string
# from django.shortcuts import render_to_response

class SplitStrTempTagTest(TestCase):
    def setUp(self):
        self.test_str = "slkdjflk sdokhf lsif skdf"
        self.split_value = " "
        self.test_str2 = "sdjkhfk sidbf ksjdbf skidjbf "
        self.split_value2 = "s"

    def test_temp_tags(self):
        # test 1
        template_tag_result = split_str(self.test_str, self.split_value)
        actual_result = self.test_str.split(self.split_value)
        self.assertEqual(actual_result, template_tag_result)
        # test 2
        template_tag_result = split_str(self.test_str2, self.split_value2)
        actual_result = self.test_str2.split(self.split_value2)
        self.assertEqual(actual_result, template_tag_result)
    
    def test_template(self):
        context = Context({'stri': self.test_str})
        template_to_render = Template(
        '''{% load core_tags %} {% split_str stri ' ' as         array %}
        {{array}}
        ''')
        actual_result = self.test_str.split(self.split_value)
        rendered_template = template_to_render.render(context)
        print(actual_result)
        print(rendered_template)
        # self.assertInHTML(actual_result, rendered_template)
        