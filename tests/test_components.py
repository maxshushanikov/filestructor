from app.components import FileComponent, DirectoryComponent

class DummyVisitor:
    def __init__(self):
        self.visited = []

    def visit_file(self, file, prefix, is_last):
        self.visited.append(('file', file.name))

    def visit_directory(self, directory, prefix, is_last):
        self.visited.append(('dir', directory.name))

def test_file_component_accept():
    fc = FileComponent("test.txt")
    visitor = DummyVisitor()
    fc.accept(visitor)
    assert ('file', 'test.txt') in visitor.visited

def test_directory_component_accept_and_add_child():
    dc = DirectoryComponent("folder")
    fc = FileComponent("file.txt")
    dc.add_child(fc)
    visitor = DummyVisitor()
    dc.accept(visitor)
    assert ('dir', 'folder') in visitor.visited
    assert ('file', 'file.txt') in visitor.visited
