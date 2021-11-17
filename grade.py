css_answers = ['2D Transforms', '3D Transforms', 'Aligning Elements', 'Animations', 'Attributes Selectors', 'Backgrounds', 'Backgrounds', 'Border Images', 'Borders', 'Box Model', 'Box Sizing', 'Buttons', 'Colors', 'Combinators', 'Comments', 'Counters', 'Display', 'Dropdowns', 'Flexbox', 'Floating', 'Fonts', 'Forms', 'Gradients', 'Grid', 'Height/Width', 'How To / Where To', 'Icons', 'Image Gallery', 'Image Reflection', 'Image Sprites', 'Inline-block', 'Links', 'Lists', 'Margins', 'Media Queries', 'Media Queries - More Examples', 'Multiple Columns', 'Navigation Bars', 'Object-fit', 'Object-position', 'Opacity', 'Outline', 'Overflow', 'Padding', 'Pagination', 'Positioning', 'Pseudo-classes', 'Pseudo-elements', 'Responsive Webdesign', 'Rounded Corners', 'Selectors', 'Shadow Effects', 'Style Images', 'Syntax', 'Tables', 'Text', 'Text Effects', 'Tooltips', 'Transitions', 'User Interface', 'Variables', 'Web Fonts', 'Website Layout']
html_answers = ['Attributes', 'Basic', 'Block and inlines elements', 'CSS', 'Canvas Graphics', 'Classes', 'Comments', 'Computercode Elements', 'Form Elements', 'Forms', 'Geolocation', 'HTML Examples', 'Headings', 'IFrame', 'Id', 'Images', 'Input Attributes', 'Input Types', 'Layout', 'Links', 'Lists', 'Local Storage', 'Media', 'Media', 'Paragraphs', 'Quotations and Citations', 'SVG Graphics', 'Scripts', 'Styles', 'Tables', 'Text Formatting']

css_lower_answers = list(map(str.lower,css_answers))
html_lower_answers = list(map(str.lower,html_answers))

# CSS

print("파일 읽는중...")
CSS_answer_fp = open("./CSS_input.txt", 'r')
read_lines = []
while True:
    line = CSS_answer_fp.readline()
    if not line: 
        break
    read_lines.append(line.lower().strip('\n').strip())
CSS_answer_fp.close()

print("/ CSS 채점 중...")

print("====== CSS 채점 결과 ======")
# result = [i for i, css_lower_answer in enumerate(css_lower_answers) if css_lower_answer in read_lines]
CSS_result = [False] * len(css_answers)
for i, css_lower_answer in enumerate(css_lower_answers):
    # 정답 찾기
    if css_lower_answer in read_lines:
        CSS_result[i] = True 
print("총 개수 {}, 맞은 개수 {}, 틀린 개수 {}, 누락된 정답 표시".format(len(css_answers), CSS_result.count(True), CSS_result.count(False)))
for i,bool in enumerate(CSS_result):
    if bool == False:
        print(css_answers[i])


# HTML

print("파일 읽는중...")
HTML_answer_fp = open("./HTML_input.txt", 'r')
read_lines = []
while True:
    line = HTML_answer_fp.readline()
    if not line: 
        break
    read_lines.append(line.lower().strip().strip('\n'))
HTML_answer_fp.close()



print("====== HTML 채점 결과 ======")

HTML_result = [False] * len(html_answers)
for i, css_lower_answer in enumerate(html_lower_answers):
    # 정답 찾기
    if css_lower_answer in read_lines:
        HTML_result[i] = True 
print("총 개수 {}, 맞은 개수 {}, 틀린 개수 {}, 누락된 정답 표시".format(len(HTML_result), HTML_result.count(True), HTML_result.count(False)))
for i,bool in enumerate(HTML_result):
    if bool == False:
        print(html_answers[i])