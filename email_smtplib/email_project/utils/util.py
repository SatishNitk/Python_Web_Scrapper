import os

class TemplateFormat():

	def get_template_path(self,path):
		file_path = os.path.join(os.getcwd(), path)
		if not os.path.isfile(file_path):
			raise Exception("there is no file:{}".format(file_path))
		return file_path
	def get_template(self,path):
	    file_path = self.get_template_path(path)
	    return open(file_path).read()	


	def render_context(self,template_string, context):
		return template_string.format(**context)

	def get_final_plain_template(self,name, date):
		# file_text = os.path.abspath(os.path.join(os.getcwd(), '..')) + "/template/email_format.txt"
		file_text = os.getcwd() + "/template/email_format.txt"
		template_text = self.get_template(file_text)
		context = {
			"name" :name,
			"date" : date
		}
		return self.render_context(template_text, context)

	def get_final_html_template(self,name, date):
		# file_html = os.path.abspath(os.path.join(os.getcwd(), '..')) + "/template/email_format.html"
		file_html = os.getcwd() + "/template/email_format.html"
		template_html = self.get_template(file_html)
		context = {
			"name" :name,
			"date" : date
		}
		return self.render_context(template_html, context)

