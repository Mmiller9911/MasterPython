# inheritance is concerned with the IS-A relationship ie. a magpie IS A duck
# composition is concerned with the HAS-A relationship ie. a magpie HAS A wing


class Tag(object):  # the other classes inherit from this one so the program uses inheritance

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return '{0.start_tag}{0.contents}{0.end_tag}'.format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag): # doctype IS-A tag

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd','')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self.header_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.header_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.header_contents:
            self.contents += str(tag)

        super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self.body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):          # the HTML doc is composed of the other three classes, this is composition

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents, location):
        if location == 'body':
            self._body.add_tag(name, contents)
        else:
            self._head.add_tag(name, contents)
        # this just delegates the job to the body class method

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('<html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('title', 'rock', 'head')
    my_page.add_tag('h1', 'main heading', 'body')
    my_page.add_tag('h2', 'sub heading', 'body')
    my_page.add_tag('p', 'paragraphmcparagraphface','body')
    with open('test.html', 'w') as file_doc:
        my_page.display(file=file_doc)

