import sys
import codecs
import markdown

reload(sys)  # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')
# input_file = codecs.open("some_file.txt", mode="r", encoding="utf-8")

if len(sys.argv) == 2:
    input_file = sys.argv[1]
    output_file = 'output_md_file.html'
elif len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
else:
    print 'You should at least pass the input file'
    exit(0)

md = codecs.open(input_file, mode="r", encoding="utf-8").read()
begin_html = u'<!DOCTYPE html><html><head><meta charset="utf-8" /></head><body>'
md_html = markdown.markdown(md)
end_html = u'</body></html>'

output_html = begin_html + md_html + end_html
try:
    f = open(output_file, 'w')
    f.write(output_html)
    print 'html created in ', output_file
    f.close
except Exception as ex:
    print 'Error: ', ex

