from robot.api import ResultVisitor
from robot.utils.markuputils import html_format

TEST_ORDER = 0

class TestResults(ResultVisitor):

    def __init__(self, test_list):
        self.test_list = test_list
    
    def visit_test(self, test):
        global TEST_ORDER
        TEST_ORDER += 1
        suite_name = test.parent if test.parent else test.parent.name
        test_json = {
            "Order" : TEST_ORDER,
            "Suite Name" : self.construct_suite_name(test, 1),
            "Test Name" : self.construct_suite_name(test) + "." + test.name,
            "Test Id" : test.id,
            "Status" : test.status,
            "Documentation" : html_format(test.doc),
            "Time" : test.elapsedtime,
            "Message" : html_format(test.message),
            # "Message" : str(test.message).replace("*HTML*",""),
            "Tags" : test.tags,
            'start_time': test.starttime,
            'end_time': test.endtime,
        }
        self.test_list.append(test_json)
    
    def construct_suite_name(self, test, extract_level=None, strip_top_level=False, keep_at_least_one_level=True):
        s = test.parent
        names = [s.name]
        while s.parent:
            s = s.parent
            names.insert(0, s.name)
        if extract_level:
            if extract_level >= len(names):
                return ""
            else:
                return names[extract_level]
        if strip_top_level:
            if not (keep_at_least_one_level and len(names) == 1):
                names = names[1:]
        return ".".join(names)
