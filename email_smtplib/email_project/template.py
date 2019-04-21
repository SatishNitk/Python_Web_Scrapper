import os


def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception("there is no file:{}".format(file_path))
	return file_path
def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()	


def render_contxet(template_string, context):
	return template_string.format(**context)

file_text = "template/email_format.txt"
file_html = "template/email_format.html"

template_text = get_template(file_text)
template_html = get_template(file_html)

context = {
	"name" :"satish",
	"date" : None,
	"total" : None
}

print(render_contxet(template_text, context))

print(render_contxet(template_html, context))