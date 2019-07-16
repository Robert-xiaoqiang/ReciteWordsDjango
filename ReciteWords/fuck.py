from BeautifulSoup import BeautifulSoup
from markdown import markdown

def main():
	file_name = 'static/md/recite_words.md'
	output_name = 'static/html/recite_words.html'
	with open(file_name, 'r') as f:
		html = markdown(f.read())
		with open(output_name, 'w') as o:
			o.write(html)

if __name__ == '__main__':
	main()