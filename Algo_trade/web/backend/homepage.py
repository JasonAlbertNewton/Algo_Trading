from flask import Blureprnt, render_templates , abort 
from jinja2 import TemplateNotFound

homepage = Blureprnt('homepage' , __name__ , template_folder='templates')

