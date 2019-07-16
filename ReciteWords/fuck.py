# from BeautifulSoup import BeautifulSoup
from markdown import markdown

def main():
	file_name = 'static/md/recite_words.md'
	output_name = 'static/html/recite_words.html'
	with open(file_name, 'r', encoding = 'utf-8') as f:
		html = markdown(f.read())
		with open(output_name, 'w', encoding = 'utf-8') as o:
			o.write(html)

if __name__ == '__main__':
	main()